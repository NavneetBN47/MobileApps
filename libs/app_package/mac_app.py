from abc import ABCMeta, abstractmethod
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.app_package.base_class import BaseClass

class MACApp(BaseClass):
    __metaclass__ = ABCMeta

    platform = "MAC"

    @abstractmethod
    def get_build_url(self, *args, **kwarg):
        raise NotImplementedError("Please Implement this method")

class MACNexusApp(MACApp):
    location = "nexus"
    location_type = "server"

    def __init__(self, couch_info):
        if couch_info is None:
            couch_info = ma_misc.load_system_config_file().get("database_info", None)
        super(MACApp, self).__init__(couch_info)

    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.nexus_api.get_file_from_nexus_artifact(self.artifact_name, self.nexus_location, app_version=build_number)

class MACJweb(MACNexusApp):
    project_name = "JWEB"
    artifact_name = "jarvis_mac_webview"
    nexus_location = "san"

class MACSmart(MACApp):
    location = "github"
    location_type = "server"
    project_name = "SMART"
    def __init__(self, couch_info):
        #Due to where the IOS Smart app is located a couchdb is required to automate this
        if couch_info is None:
            raise RuntimeError("MAC Smart app_module requires couch_info to be not None")
        super(MACApp, self).__init__(couch_info)

    def get_build_url(self, build_type="adhoc", build_version=None, build_number=None):
        return self.github_api.get_build_url(build_type=build_type, build_version=build_version, build_number=build_number, unzip=False)
