import os
import re
import sys
import abc
import json
import uuid
import time
import shutil
import logging
import requests
from SAF.misc import saf_misc
from SAF.misc.factory_util import *
from MobileApps.libs.ma_misc import ma_misc

logger = logging.getLogger('app_module.github_api')

class PkgSearchException(Exception):
    pass

class BadBuildVersionException(PkgSearchException):
    pass


def github_api_factory(platform, project_name, db_utils):
    for _cls in all_subclasses(GithubAPI):
        if is_abstract(_cls) or not getattr(_cls, "platform", False):
            continue

        if _cls.platform.upper() == platform.upper() and project_name.upper() in _cls.project_name:
            return _cls(platform, project_name, db_utils)
    
    logger.error("Cannot satisfy module type: " + platform + " for project: " + project_name)
    sys.exit()

class GithubAPI(abc.ABC):
    def __init__(self, platform, project_name, db_utils):
        self.db_utils = db_utils
        self.system_config = ma_misc.load_system_config_file()
        rd_jenkins_paths = saf_misc.load_json(ma_misc.get_abs_path("libs/app_package/data/rd_jenkins_paths.json"))

        self.project_name = project_name
        self.platform = platform

        token_name = next(i for i in rd_jenkins_paths["GITHUB"]["token_name"] if platform in i["projects"].keys() and project_name in i["projects"][platform])["name"]
        self.root_url = next(i for i in rd_jenkins_paths["GITHUB"]["github_root"] if platform in i["projects"].keys() and project_name in i["projects"][platform])["url"]
        self.releases_api_url = next(i for i in rd_jenkins_paths["GITHUB"]["release_url"] if platform in i["projects"].keys() and project_name in i["projects"][platform])["url"]
        self.build_type_dict = next(i for i in rd_jenkins_paths["GITHUB"]["build_type_dict"] if platform == i["platform"] and project_name in i["projects"])["build_type_dict"]
        self.build_extension = next(i for i in rd_jenkins_paths["GITHUB"]["build_type_dict"] if platform == i["platform"] and project_name in i["projects"])["extension"]
        self.version_regex = next(i for i in rd_jenkins_paths["GITHUB"]["build_type_dict"] if platform == i["platform"] and project_name in i["projects"]).get("version_regex", None)
        self.access_token = self.system_config[token_name]

        self.request_paging = "?page=1&per_page=100"
        self.tag_api_url = "/tags/{}"
        self.auth_header = {"Authorization": "token " + self.access_token}
        #During transition I'll keep this the same
        self.db_view_section = "IOS_view"
        self.db_view_doc = self.platform.lower() + "_package_view"

    def download_build(self,build_type=None, build_version=None, build_number=None, release_type=None, save_location="./", unzip=True):
        url, _, _, _ = self.find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        ma_misc.download_build_to_local(url, save_path=save_location, auth_header=self.auth_header, unzip=unzip)

    def get_build_url(self, build_type=None, build_version=None, build_number=None, release_type=None, unzip=True):
        """
        Params: build_type: The type of build (adhoc (ios), debug(android), loggable, ga, etc)
                build_version: The major version of the app (8.6.1, 8.7.0, etc)
                build_number: The build number of that major version (25, 8695, etc)
                release_type: Android HP Smart/HPPS specific (consists of daily or stable builds)
        """
        #look for it in the database
        match_key = [self.project_name, build_type, build_version, build_number, release_type]    
        database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc)
        if database_url:
            return database_url

        url, actual_build_version, actual_daily_version, app_info = self.find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        logger.info("Build Version: " + actual_build_version + " Daily Version: " + actual_daily_version + " App Info: " + app_info)
        match_key = [self.project_name, build_type, actual_build_version, actual_daily_version, release_type]
        database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc)
        if database_url:
            return database_url

        if self.platform == "WINDOWS" and self.project_name == "HPX":
            self.auth_header["Accept"] = "application/octet-stream"
            str_header = json.dumps(self.auth_header)
            str_header = str_header.replace(": ", "=")
            str_header = str_header.replace(",", ";")
            return f"{url} -Headers @{str_header}", app_info

        doc = {"build_type": build_type,
                "os": self.platform,
                "build_version": actual_build_version,
                "daily_version": actual_daily_version,
                "project": self.project_name,
                "release_type": release_type, 
                "app_info": app_info
                }
        unique_id = uuid.uuid4().hex
        unique_folder_path = "./" + unique_id
        fname = ma_misc.download_build_to_local(url, save_path=unique_folder_path, auth_header=self.auth_header, unzip=unzip)
        if fname.endswith(".zip"):
            unique_file_path = "./" + unique_id + "/" + os.listdir(unique_folder_path)[0]
        else:
            unique_file_path = "./" + unique_id + "/" + fname
        
        for _ in range(5):
            attachment_url = self.db_utils.upload_build_to_database(doc, unique_file_path)
            if attachment_url is None:
                database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc)
                if database_url:
                    shutil.rmtree("./" + unique_id)
                    return database_url   
                else:
                    time.sleep(10)
            else:
                shutil.rmtree("./" + unique_id)
                return attachment_url, app_info         

        return attachment_url, app_info

    @abc.abstractmethod
    def find_build(self, build_type=None, build_version=None, build_number=None, release_type=None):
        if build_number is not None and build_version is None:
            raise ValueError("You cannot only use build_number, you also need to pass in build_version")
        

    def get_all_releases(self):
        req = requests.get(self.root_url + self.releases_api_url + self.request_paging, headers=self.auth_header)
        if req.status_code != 200:
            req.raise_for_status() 
        return json.loads(req.text)

    def all_releases_find_build(self, build_type, build_version=None, build_number=None, prerelease_only=False, unzip=True):
        desired_release = None
        skipped_build = 0
        if build_version and build_number:
            search_version = ".".join([build_version,build_number])
        else:
            search_version = None
        all_release = self.get_all_releases()
        for release in all_release:
            if not release["name"]:
                #Release with no name? Ridiclous skip
                continue

            if prerelease_only is not release.get("prerelease", True):
                continue
            
            if self.version_regex and not re.match(self.version_regex, self.clean_release_name(release["name"])):
                continue

            if search_version: 
                if self.clean_release_name(release["name"]) != search_version:
                    continue

            elif build_version:
                release_build_version = ".".join(self.clean_release_name(release["name"]).split("."))
                if build_version != release_build_version:
                    continue

            if desired_release is None:
                if self.find_asset(release, build_type, raise_e=False) is not False:
                    desired_release = release
                else:
                    skipped_build += 1
                    if skipped_build > 30:
                        raise PkgSearchException("Asset build_type: " + build_type + " was not found in more than 30 skips")
                    else:
                        continue
            else:
                cur_version = self.clean_release_name(release["name"]).split(".")[:-1]
                cur_build = self.clean_release_name(release["name"]).split(".")[-1]
                cache_version = self.clean_release_name(desired_release["name"]).split(".")[:-1]
                cache_build = self.clean_release_name(desired_release["name"]).split(".")[-1]
                if self.compare_version(cur_version, cache_version, cur_build, cache_build):
                    if self.find_asset(release, build_type, raise_e=False) is not False:
                        desired_release = release

        if desired_release is None or desired_release.get("message", None) == "Not Found":
            raise PkgSearchException("Cannot locate release for build_version: "  + str(build_version) + " build_number: " + str(build_number))
            
        return self.find_asset(desired_release, build_type)

    def compare_version(self, cur_version, cached_version, cur_build, cached_build):
        for index, value in enumerate(cur_version):
            patten = r"\d+"
            value = re.findall(patten, value)[0]
            if int(value) > int(cached_version[index]):
                return True
            elif int(value) < int(cached_version[index]):
                return False
                
        return int(cur_build) > int(cached_build)

    def find_asset(self, desired_release, build_type, raise_e=True):
        actual_build_version = ".".join(self.clean_release_name(desired_release["name"]).split("."))
        actual_daily_version = self.clean_release_name(desired_release["name"]).split(".")[-2]
        for asset in desired_release["assets"]:
            if ("rebrand" not in build_type and "REBRAND" in asset["name"]) or ("rebrand" in build_type and "REBRAND" not in asset["name"]):
                continue
            if bool(re.search(self.build_type_dict[build_type], asset["name"])) and asset["name"].split(".")[-1] == self.build_extension:
                return asset["url"], actual_build_version, actual_daily_version, asset["name"]
        if raise_e:
            raise PkgSearchException("Somehow the asset was not found :( build_type: " + build_type)
        else:
            return False

    def clean_release_name(self, release_name):
        if "HPAIExperienceCenter" in release_name:
            release_name = release_name.split(" ")[1]

        if "Testing | " in release_name:
            release_name = release_name.split("Testing | ")[1]

        if release_name[0]=="v":
            release_name = release_name[1:]
                
        if "-" in release_name:
            release_name = release_name[0:release_name.index("-")]
            
            
        return release_name

class AndroidGithubAPI(GithubAPI):
    platform = "ANDROID"
    project_name = ["HPX", "SMART", "HPPS"]
    def find_build(self, build_type="debug", build_version=None, build_number=None, release_type=None):
        super().find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        if release_type=="daily":
            return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number)
        elif release_type=="stable":
            #This API returns the latest "Released" build which is the stable branch build
            #if not build_version:
                #Doesn't work the latest "release" isn't the latest "release" FML
                #return self.find_asset(json.loads((requests.get(self.root_url + self.releases_api_url + "/latest", headers=self.auth_header).text)), build_type)
                
            #else:
            return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number, prerelease_only=False)

class IOSHPGithubAPI(GithubAPI):
    platform = "IOS"
    project_name = ["SMART"]
    def find_build(self, build_type="adhoc", build_version=None, build_number=None, release_type=None):
        super().find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number)

class WINDOWSGithubAPI(GithubAPI):
    platform = "WINDOWS"
    project_name = ["HPX", "HPAI"]
        
    def find_build(self, build_type="integration", build_version=None, build_number=None, release_type=None):
        super().find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        if self.project_name == "HPX":
            prerelease = False
        elif self.project_name == "HPAI":
            prerelease = True
            
        if release_type=="daily":
            return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number, prerelease_only=prerelease)
        elif release_type=="stable":
            #TODO need to add way to fetch 'release' builds
            pass
        
class MACGithubAPI(GithubAPI):
    platform = "MAC"
    project_name = ["SMART"]
    
    def find_build(self, build_type="adhoc", build_version=None, build_number=None, release_type=None):
        super().find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number, unzip=False)