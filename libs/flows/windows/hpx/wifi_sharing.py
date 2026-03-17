from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class WifiSharing(HPXFlow):
    flow_name = "wifi_sharing"
    
    def verify_wifi_sharing_title_show(self):
        return self.driver.wait_for_object("wifi_sharing_title", raise_e=False, timeout=20)
    
    def verify_wifi_sharing_subtitle_show(self):
        return self.driver.wait_for_object("wifi_sharing_subtitle", raise_e=False, timeout=20)
    
    def verify_wifi_sharing_first_one_title_show(self):
        return self.driver.wait_for_object("first_one_title", raise_e=False, timeout=20)
    
    def verify_wifi_sharing_first_one_image_show(self):
        return self.driver.wait_for_object("first_one_image", raise_e=False, timeout=20)
    
    def verify_wifi_sharing_second_one_title_show(self):
        return self.driver.wait_for_object("second_one_title", raise_e=False, timeout=20)

    def verify_wifi_sharing_second_one_image_show(self):
        return self.driver.wait_for_object("second_one_image", raise_e=False, timeout=20)
    
    def verify_wifi_sharing_third_one_title_show(self):
        return self.driver.wait_for_object("third_one_title", raise_e=False, timeout=20)

    def verify_wifi_sharing_third_one_image_show(self):
        return self.driver.wait_for_object("third_one_image", raise_e=False, timeout=20)
    
    def verify_windows_network_settings_button_show(self):
        return self.driver.wait_for_object("windows_network_settings", raise_e=False, timeout=20)