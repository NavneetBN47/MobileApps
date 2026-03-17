from MobileApps.libs.flows.windows.jweb_storage_manager.home import Home
from MobileApps.libs.flows.windows.jweb_storage_manager.storage_plugin import StoragePlugin
from MobileApps.libs.ma_misc import ma_misc
from time import sleep

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.fd = {"home": Home(driver),
                   "storage_plugin": StoragePlugin(driver)}

    @property
    def flow(self):
        return self.fd

    def navigate_to_storage_plugin(self):
        """
        Navigate to Storage Manager weblet
        """
        self.driver.restart_app()
        self.fd["home"].select_storage_manager_weblet_settings_btn()
        self.fd["home"].select_tenancy_retrieval_function_checkbox()
        sleep(3)
        self.fd["home"].select_tenant_id_to_return_textfield("JarvisAuto-rcb")
        self.fd["home"].select_tenant_id_to_return_set_btn()
        self.fd["home"].select_storage_manager_weblet()