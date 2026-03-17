from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
from time import sleep

class Home(JwebStorageManagerFlow):
    flow_name = "home"

    def select_storage_manager_weblet(self):
        """
        Clicks on the Storage Manager Weblet tab
        """
        self.driver.click("storage_manager_weblet")
        sleep(2)

    def select_storage_manager_weblet_settings_btn(self):
        """
        Clicks Storage Manager Weblet tab settings button
        """
        self.driver.click("storage_manager_weblet_settings_btn")
 
    def select_tenancy_retrieval_function_checkbox(self):
        """
        Clicks on the Tenancy Retrieval Function checkbox if not already checked
        """
        if self.driver.get_attribute("tenancy_retrieval_function_checkbox", "Toggle.ToggleState") != "1":
            self.driver.click("tenancy_retrieval_function_checkbox")
 
    def select_tenant_id_to_return_textfield(self, text):
        """
        Clicks on the Tenant ID to Return text field
        """
        self.driver.click("select_tenant_id_to_return_textfield")
        self.driver.clear_text("select_tenant_id_to_return_textfield")
        self.driver.send_keys("select_tenant_id_to_return_textfield", text)
   
    def select_tenant_id_to_return_set_btn(self):
        """
        Clicks on the Set button for Tenant ID to Return
        """
        self.driver.click("tenant_id_to_return_set_btn")