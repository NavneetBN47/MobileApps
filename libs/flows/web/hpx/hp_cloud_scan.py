from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow

class HPCloudScan(HPXFlow):
    flow_name = "hp_cloud_scan"


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_hp_cloud_scan_sign_in_screen(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("sign_in_screen_header", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("sign_in_screen_body", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("sign_in_screen_create_account_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("sign_in_screen_sign_in_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("sign_in_screen_exit_btn", timeout=timeout, raise_e=raise_e)

    def verify_hp_cloud_scan_printer_not_added_screen(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("printer_not_added_screen_icon", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("printer_not_added_screen_header", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("printer_not_added_screen_body", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("printer_not_added_screen_link", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("top_back_btn", timeout=timeout, raise_e=raise_e)

    def verify_hp_cloud_printer_screen(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("icon_printer_image", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("no_files_body_text", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("settings_menu", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("top_back_btn", timeout=timeout, raise_e=raise_e)

    def verify_cloud_connected_screen(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("cloud_connected_screen_header", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("cloud_connected_screen_body", timeout=timeout, raise_e=raise_e)
    
    def verify_check_printer_supports_hp_cloud_scans_dialog(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("check_printer_supports_dialog_header", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("check_printer_supports_dialog_body_1", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("check_printer_supports_dialog_body_2", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("check_printer_supports_dialog_body_3", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("check_printer_supports_dialog_body_4", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("close_btn_on_dialog", timeout=timeout, raise_e=raise_e)

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_sign_in_btn(self):
        self.driver.click("sign_in_screen_sign_in_btn", change_check={"wait_obj": "sign_in_screen_sign_in_btn", "invisible": True}, retry=2, delay=1)
    
    def click_settings_menu_btn(self):
        self.driver.click("not_added_screen_settings_menu", change_check={"wait_obj": "not_added_screen_settings_menu", "invisible": True}, retry=2, delay=1)  
    
    def click_back_btn_on_settings_menu(self):
        self.driver.click("top_back_btn", change_check={"wait_obj": "cloud_connected_screen_body", "invisible": True}, retry=3, delay=1)
    
    def click_back_btn(self):
        self.driver.click("top_back_btn")
        
    def click_check_printer_support_link(self):
        self.driver.click("printer_offline_screen_link", change_check={"wait_obj": "printer_offline_screen_link", "invisible": True}, retry=2, delay=1)