from MobileApps.libs.flows.windows.jweb_value_store.jweb_value_store_flow import JwebValueStoreFlow

class ValueStore(JwebValueStoreFlow):
    flow_name = "value_store"

    def verify_native_view_buttons(self):
        """
        Verify that the Get, Put, and Remove buttons are present
        """
        self.driver.wait_for_object("get_btn", timeout=3)
        self.driver.wait_for_object("put_btn", timeout=3)
        self.driver.wait_for_object("remove_btn", timeout=3)
