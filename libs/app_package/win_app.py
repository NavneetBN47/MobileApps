from abc import ABCMeta, abstractmethod
from MobileApps.libs.app_package.base_class import BaseClass

class WINAppException(Exception):
    pass

class WINApp(BaseClass):
    __metaclass__ = ABCMeta

    platform = "WINDOWS"

    @abstractmethod
    def get_build_url(self, *args, **kwarg):
        raise NotImplementedError("Please Implement this method")

class WINNexusApp(WINApp):
    location = "nexus"
    location_type = "server"

    def __init__(self, couch_info):
        super(WINNexusApp, self).__init__(couch_info)

    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.nexus_api.get_file_from_nexus_artifact(self.artifact_name, self.nexus_location, app_version=build_version, app_build=build_number)

class WINJweb(WINNexusApp):
    project_name = "JWEB"
    artifact_name = "jarvis_windows_webview_x64"
    nexus_location = "san"

class WINJwebStorageManager(WINNexusApp):
    project_name = "JWEB_STORAGE_MANAGER"
    artifact_name = "jarvis_windows_storage_x64"
    nexus_location = "san"

class WINJwebDataCollection(WINNexusApp):
    project_name = "JWEB_DATA_COLLECTION"
    artifact_name = "jarvis_windows_datacollection_x64"
    nexus_location = "san"

class WINJwebServiceRouting(WINNexusApp):
    project_name = "JWEB_SERVICE_ROUTING"
    artifact_name = "jarvis_windows_service-routing_x64"
    nexus_location = "san"

class WINJwebEventService(WINNexusApp):
    project_name = "JWEB_EVENT_SERVICE"
    artifact_name = "jarvis_windows_event_service_x64"
    nexus_location = "san"

class WINAuth(WINNexusApp):
    project_name = "JWEB_AUTH"
    artifact_name = "jarvis_windows_auth_x64"
    nexus_location = "san"

class WINJwebValueStore(WINNexusApp):
    project_name = "JWEB_VALUE_STORE"
    artifact_name = "jarvis_windows_valuestore_x64"
    nexus_location = "san"

class WINJwebDocProvider(WINNexusApp):
    project_name = "JWEB_DOC_PROVIDER"
    artifact_name = "jarvis_windows_docprovider_x64"
    nexus_location = "san"

class WINJwebConfigurationService(WINNexusApp):
    project_name = "JWEB_CONFIGURATION_SERVICE_WINUI"
    artifact_name = "jarvis_windows_configuration_service_winui_x64"
    nexus_location = "san"

class WinSmart(WINNexusApp):
    project_name = "GOTHAM"
    artifact_name = "GothamUltron"
    nexus_location = "san"

class WINGithubApp(WINApp):
    location = "github"
    location_type = "server"
    def __init__(self, couch_info):
        super(WINApp, self).__init__(couch_info)

    def get_build_url(self, build_type="integration", build_version=None, build_number=None, release_type="daily"):
        return self.github_api.get_build_url(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type, unzip=False)

class WinHPX(WINGithubApp):
    project_name = "HPX"

    
class WinHPAI(WINGithubApp):
    project_name = "HPAI"