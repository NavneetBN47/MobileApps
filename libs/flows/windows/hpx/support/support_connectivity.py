from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SupportConnectivity(HPXFlow):
    flow_name = "support_connectivity"

    def click_service_setup_switch_wifi_link(self):
        self.driver.click("setup_link")

    def click_service_data_usage_link(self):
        self.driver.click("usage_link")

    def click_service_turn_off_link(self):
        self.driver.click("turn_off_link")

    def click_start_va(self):
        self.driver.click("start_va_btn")
    
    def click_close_btn(self):
        self.driver.click("close_button")

    def get_start_va_btn_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("start_va_btn", raise_e=raise_e, timeout=timeout).text
