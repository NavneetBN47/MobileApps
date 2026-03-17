from enum import unique
import re
import sys
import abc
import uuid
import time
import shutil
import logging
import requests
import urllib.parse
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth
from requests.exceptions import InvalidURL
from SAF.misc import saf_misc
from SAF.misc.factory_util import *
from MobileApps.libs.ma_misc import ma_misc

logger = logging.getLogger('app_module.nexus_api')

def nexus_api_factory(platform, project_name, db_utils):
    for _cls in all_subclasses(NexusAPI):
        if is_abstract(_cls) or not getattr(_cls, "platform", False):
            continue

        if _cls.platform.upper() == platform.upper() and project_name.upper() in _cls.project_name:
            return _cls(platform, project_name, db_utils)
    
    logger.error("Cannot satisfy module type: " + platform + " for project: " + project_name)
    sys.exit()

class CannotFindArtifact(Exception):
    pass

class NexusAPI(abc.ABC):
    def __init__(self, platform, project_name, db_utils):
        self.db_utils = db_utils
        self.system_config = ma_misc.load_system_config_file()
        self.rd_jenkins_paths = saf_misc.load_json(ma_misc.get_abs_path("libs/app_package/data/rd_jenkins_paths.json"))

        self.project_name = project_name.lower()
        self.platform = platform
        self.http_auth = None

        try:
            self.artifact_name = next(i for i in self.rd_jenkins_paths["NEXUS"]["artifact_name"] if platform in i["platform"] and project_name in i["projects"])["projects"][project_name]
            self.root_url = next(i for i in self.rd_jenkins_paths["NEXUS"]["nexus_root"] if self.artifact_name in i["projects"])["url"]
            self.repo_url = next(i for i in self.rd_jenkins_paths["NEXUS"]["repo_name"] if self.artifact_name in i["projects"])["url"]
            self.group_url = next(i for i in self.rd_jenkins_paths["NEXUS"]["group_id"] if self.artifact_name in i["projects"])["url"]
            self.pkg_ext = next(i for i in self.rd_jenkins_paths["NEXUS"]["pkg_ext"] if self.artifact_name in i["projects"])["ext"]
        except KeyError:
            logger.error("Does not know how to find nexus url for: '" + project_name)
            sys.exit()

        self.db_view_section = "IOS_view"
        self.db_view_doc = self.platform.lower() + "_package_view"

    def check_branched_folders(self, root_url, project_name, version=None):
        req = requests.get(root_url, auth=self.http_auth)
        version = version if not version or "." not in version else version.split(".")[0]
        project_folders = []
        if req.status_code != 200:
            raise InvalidURL("Cannot find parent folder? URL: " + root_url)

        tree = ET.fromstring(req.text)
        all_folders = tree.findall(".//content-item")
        if not all_folders:
            return (None, None)
        for folder in all_folders:
            name = folder.find(".//text")
            if name.text.startswith(project_name) and (not version or version and version in name.text):
                project_folders.append(name.text)
        if not project_folders:
            #if specific version is not branched then return None
            return None, None

        app_version = self.get_latest_version((branched_url:=root_url+project_folders[-1]), "san", project_name)
        return app_version, branched_url

    def get_latest_version(self, project_url, nexus_location, project_name, set_app_version=None):
        req = requests.get(maven_url:="{}/maven-metadata.xml".format(project_url), auth=self.http_auth)
        if req.status_code == 200:
            tree = ET.fromstring(req.text)
            app_version = tree.findall(".//release")[0].text
            # find the latest version of a project with an acceptable pkg extension
            if (set_app_version is not None) or (not self.valid_nexus_file_found(nexus_location, project_url, app_version)):
                versions = list(tree.find(".//versions"))
                sorted_version = sorted([x.text for x in versions])
                sorted_version.reverse()
                for version in sorted_version:
                    app_version = version
                    if set_app_version and not version.startswith(str(set_app_version)):
                        continue
                    if self.valid_nexus_file_found(nexus_location, project_url, app_version):
                        break
                else:
                    raise CannotFindArtifact("Can't find a build for project: {} with pkg extension: {} or set version number: {}".format(project_name, self.pkg_ext, set_app_version))
        elif nexus_location == "san":
            # if we are unable to locate maven-metadata.xml, locate latest version using a regular expression on the full san nexus page
            req_project = requests.get(project_url) 
            if req_project.status_code != 200:
                raise InvalidURL("The URL: {} returned: {}".format(project_url, req.status_code))
            req_project_versions = re.findall("<text>([0-9].*?)</text>", req_project.text)
            app_version = ma_misc.get_newest_application_version(req_project_versions)
        elif nexus_location == "int":
            raise CannotFindArtifact("Cannot find maven file for nexus int server, no alternative avaliable url: " + maven_url)
        return app_version

    def get_file_from_nexus_artifact(self, project_name, nexus_location, app_version=None, app_build=None): 
        #Check if app is already in database if app_version is given
        if nexus_location == 'int':
            if app_version:
                match_key = [self.project_name, self.artifact_name, app_version, self.platform]    
                database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc, nexus=True)
                if database_url:
                    return database_url
            try:
                self.token_name = next(i for i in self.rd_jenkins_paths["NEXUS"]["token_name"] if project_name in i["projects"])["name"]
                self.rest_url = next(i for i in self.rd_jenkins_paths["NEXUS"]["rest_url"] if project_name in i["projects"])["url"]
                self.access_username = next(i for i in self.rd_jenkins_paths["NEXUS"]["token_name"] if project_name in i["projects"])["username"]
                self.access_token = self.system_config[self.token_name]
            except KeyError:
                logger.error("Does not know how to find nexus int url for: '" + project_name)
                sys.exit()
            project_url = "{}{}{}{}".format(self.root_url, self.repo_url, self.group_url, project_name)
            self.http_auth = HTTPBasicAuth(self.access_username, self.access_token)
        else:
            root_url = "{}{}content{}".format(self.root_url, self.repo_url, self.group_url)
            project_url = root_url + project_name
        
        #Get actual app version 
        if app_version is not None and app_build is not None:
            app_version = "{}.{}".format(app_version, app_build)
        elif app_version is None:
            app_version = self.get_latest_version(project_url, nexus_location, project_name)
        else:
            app_version = self.get_latest_version(project_url, nexus_location, project_name, set_app_version=app_version)

        #Check if the actual app version is already in the database
        if nexus_location == 'int':
            match_key = [self.project_name, self.artifact_name, app_version, self.platform]    
            database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc, nexus=True)
            if database_url:
                return database_url

        if nexus_location == "san":
            branched_app_version, branched_url = self.check_branched_folders(root_url, project_name, version=app_version)
            if branched_app_version and app_version != ma_misc.get_newest_application_version([app_version, branched_app_version]):
                project_url = branched_url

                if not app_build:
                    app_version = ma_misc.get_newest_application_version([app_version, branched_app_version])

            req = requests.get("{}/{}".format(project_url, app_version))
            if req.status_code !=200:
                raise InvalidURL("The URL: {}/{} returned: {}".format(project_url, app_version, req.status_code))
            pkg_xml = ET.fromstring(req.text)
            resource_uri = next(i.text for i in pkg_xml.findall(".//resourceURI") if i.text.split(".")[-1] == self.pkg_ext)
            package_name = resource_uri.split("/")[-1]
            logger.info("Using package: " + package_name)
            return resource_uri, package_name
        
        else:
            artifact_url = "{}/{}/{}-{}-debug.{}".format(project_url, app_version, project_name, app_version, self.pkg_ext)
            unique_id = uuid.uuid4().hex
            unique_folder_path = "./" + unique_id
            fname = ma_misc.download_build_to_local(artifact_url, save_path=unique_folder_path, auth_header=False, http_auth=self.http_auth)
            unique_file_path = "./{}/{}".format(unique_id, fname)

            doc = {"os": self.platform,
            "app_version": app_version,
            "project": self.project_name,
            "artifact_name": self.artifact_name, 
            "app_info": artifact_url.split("/")[-1]
            }

            for _ in range(5):
                attachment_url = self.db_utils.upload_build_to_database(doc, unique_file_path)
                if attachment_url is None:
                    database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc, nexus=True)
                    if database_url:
                        shutil.rmtree("./" + unique_id)
                        return database_url   
                    else:
                        time.sleep(10)
                else:
                    logger.info("Using package: " + artifact_url.split("/")[-1])
                    shutil.rmtree("./" + unique_id)
                    return attachment_url, artifact_url.split("/")[-1]
            logger.info("Using package: " + artifact_url.split("/")[-1])
            return attachment_url, artifact_url.split("/")[-1]

    def valid_nexus_file_found(self, nexus_location, project_url, app_version):
        if nexus_location == "san":
            req = requests.get(project_url + "/" + app_version)
            if req.status_code != 200:
                raise InvalidURL("The URL: {}/{} returned: {}".format(project_url, app_version, req.status_code))
            pkg_xml = ET.fromstring(req.text)
            return any(i.text for i in pkg_xml.findall(".//resourceURI") if i.text.split(".")[-1] == self.pkg_ext)
        else:
            endpoint = "/v1/search/assets"
            params = urllib.parse.urlencode({"repository": self.repo_url.replace("/", ""), "maven.extension": self.pkg_ext, 
                                             "name": self.artifact_name, "version": app_version, "sort": "version"})
            url = f"{self.rest_url}{endpoint}?{params}"
            response = requests.get(url, auth=self.http_auth)
            if response.status_code != 200:
                raise InvalidURL("The URL: {} returned: {}".format(url, response.status_code))
            response = response.json()
            return [item['downloadUrl'] for item in response['items']]

class AndroidNexusAPI(NexusAPI):
    platform = "ANDROID"
    project_name = ["JWEB", "JWEB_EVENT_SERVICE", "JWEB_SERVICE_ROUTING", "JWEB_DOC_PROVIDER", "JWEB_DATA_COLLECTION", "JWEB_EVENT_SERVICE", "JWEB_VALUE_STORE"]

class IOSNexusAPI(NexusAPI):
    platform = "IOS"
    project_name = ["JWEB", "JWEB_AUTH", "JWEB_EVENT_SERVICE", "JWEB_SERVICE_ROUTING", "JWEB_DATA_COLLECTION", "JWEB_EVENT_SERVICE", "JWEB_DOC_PROVIDER", "JWEB_VALUE_STORE"]

class WindowsNexusAPI(NexusAPI):
    platform = "WINDOWS"
    project_name = ["GOTHAM", "JWEB", "JWEB_DATA_COLLECTION", "JWEB_SERVICE_ROUTING", "JWEB_VALUE_STORE", "JWEB_DOC_PROVIDER", "JWEB_EVENT_SERVICE", "JWEB_AUTH", "JWEB_STORAGE_MANAGER", "JWEB_CONFIGURATION_SERVICE_WINUI"]
    
class MacNexusAPI(NexusAPI):
    platform = "MAC"
    project_name = ["SMART", "JWEB"]