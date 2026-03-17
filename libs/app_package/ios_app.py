from abc import ABCMeta, abstractmethod
from MobileApps.libs.app_package.base_class import BaseClass

class IOSApp(BaseClass):
    __metaclass__ = ABCMeta

    platform="IOS"
    @abstractmethod
    def get_build_url(self):
        raise NotImplementedError("Please Implement this method")

class IOSSmart(IOSApp):
    location = "github"
    location_type = "server"
    project_name = "SMART"
    def __init__(self, couch_info):
        #Due to where the IOS Smart app is located a couchdb is required to automate this
        if couch_info is None:
            raise RuntimeError("IOSSmart app_module requires couch_info to be not None")
        super(IOSApp, self).__init__(couch_info)

    def get_build_url(self, build_type="adhoc", build_version=None, build_number=None):
        return self.github_api.get_build_url(build_type=build_type, build_version=build_version, build_number=build_number)

class IOSNexusApp(IOSApp):
    location = "nexus"
    location_type = "server"

    def __init__(self, couch_info):
        super(IOSNexusApp, self).__init__(couch_info)

    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.nexus_api.get_file_from_nexus_artifact(self.artifact_name, self.nexus_location, app_version=build_number)

class IOSJweb(IOSNexusApp):
    project_name = "JWEB"
    artifact_name = "jarvis_ios_webview"
    nexus_location = "san"

class IOSAuth(IOSNexusApp):
    project_name = "JWEB_AUTH"
    artifact_name = "jarvis_ios_auth"
    nexus_location = "san"

class IOSJwebServiceRouting(IOSNexusApp):
    project_name = "JWEB_SERVICE_ROUTING"
    artifact_name = "jarvis_ios_service_routing"
    nexus_location = "san"

class IOSJwebEventService(IOSNexusApp):
    project_name = "JWEB_EVENT_SERVICE"
    artifact_name = "jarvis_ios_event_service"
    nexus_location = "san"

class IOSJwebDataCollection(IOSNexusApp):
    project_name = "JWEB_DATA_COLLECTION"
    artifact_name = "jarvis_ios_data_collection"
    nexus_location = "san"

class IOSJwebDocProvider(IOSNexusApp):
    project_name = "JWEB_DOC_PROVIDER"
    artifact_name = "jarvis_ios_doc_provider"
    nexus_location = "san"

class IOSJwebValueStore(IOSNexusApp):
    project_name = "JWEB_VALUE_STORE"
    artifact_name = "jarvis_ios_value_store"
    nexus_location = "san"