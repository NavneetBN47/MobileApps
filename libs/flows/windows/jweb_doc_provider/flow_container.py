from MobileApps.libs.flows.windows.jweb_doc_provider.home import Home
from MobileApps.libs.flows.windows.jweb_doc_provider.doc_provider_plugin import DocProviderPlugin
from MobileApps.libs.flows.windows.jweb_data_collection.files import Files

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "doc_provider_plugin": DocProviderPlugin(driver),
                   "files": Files(driver)}

    def load_doc_source_weblet(self, reset_app=True, enable_launch_as_web_service=True):
        if reset_app:
            self.driver.restart_app()
        self.fd["doc_provider_plugin"].select_navigate_back_btn(raise_e=False)
        if enable_launch_as_web_service: 
            self.fd["home"].enable_launch_as_web_service_btn()
        self.fd["home"].select_service_btn("Doc Source")
