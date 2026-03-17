from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SupportOnedrive(HPXFlow):
    flow_name = "support_onedrive"

    def click_using_MS_cloud_storage_link(self):
        self.driver.click("using_ms_cloud_storage_link")

    def click_active_MS_cloud_storage_link(self):
        self.driver.click("active_ms_cloud_storage_link")

    def click_install_MS_cloud_storage_link(self):
        self.driver.click("install_ms_cloud_storage_link")
    
    def click_M365_account_link(self):
        self.driver.click("m365_account_link")

    def click_google_one_account_link(self):
        self.driver.click("google_one_account_link")

    def click_start_va(self):
        self.driver.click("start_va_btn")

    def click_close_btn(self):
        self.driver.click("close_button")

    def get_start_va_btn_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("start_va_btn", raise_e=raise_e, timeout=timeout).text

    def get_MS_cloud_storage_title(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("MS_cloud_storage_lbl", raise_e=raise_e, timeout=timeout)
        return self.driver.find_object("MS_cloud_storage_title").text