from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow

class DevicesMFE(SmartFlow):
    flow_name = "devices_mfe"


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_new_hp_app_popup(self, raise_e=True):
        return self.driver.wait_for_object("new_hp_app_popup_skip_btn", raise_e=raise_e)
    
    def verify_home_nav(self, timeout=10, raise_e=True):
        return self.verify_app_bar_mfe(timeout=timeout, raise_e=raise_e)
    
    def verify_windows_dummy_printer(self, timeout=10):
        #Alpha code, cannot add printer so using a dummy printer by using a recent device list xml file 8/26/2024
        return self.driver.wait_for_object("windows_dummy_printer_device", timeout=timeout)
    
    def verify_app_bar_mfe(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("app_bar_mfe_section", timeout=timeout, raise_e=raise_e)
    
    def verify_device_status_mfe(self):
        return self.driver.wait_for_object("device_status_section", displayed=False)
    
    def verify_side_panel_mfe(self):
        return self.driver.wait_for_object("account_panel_section")
    
    def verify_home_loggedin(self, timeout=3, raise_e=False):
        return self.driver.wait_for_object("top_signin_button", invisible=True, timeout=timeout, raise_e=raise_e)
    
    def verify_device_card_show_up(self):
        return self.driver.wait_for_object("device_card")
    
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
        
    def click_new_hp_app_popup_skip(self):
        return self.driver.click("new_hp_app_popup_skip_btn")
        
    def refresh_device_mfe(self):
        el = self.driver.wait_for_object("main_webview_pane")
        el.click()
        return el.send_keys(Keys.CONTROL+"r")

    def click_windows_dummy_printer(self):
        #Alpha code, cannot add printer so using a dummy printer by using a recent device list xml file 8/26/2024
        self.driver.click("windows_dummy_printer_device")
        
    def click_add_button(self):
        self.driver.click("top_add_button")
        
    def click_device_tile(self):
        self.driver.click("device_tile")
        
    def click_profile_button(self):
        self.driver.click("top_profile_button")

    def click_device_icon(self):
        self.driver.click("device_icon")

    def click_close_button(self):
        el = self.driver.wait_for_object("account_panel_close_button", displayed=False)
        self.driver.wdvr.execute_script("arguments[0].click();", el)

    def click_device_card(self):
        return self.driver.click("device_card")
    
    def click_home_loggedin(self):
        return self.driver.click("top_signin_button")
    
    def get_hpx_whats_new_popup_title(self, timeout=10):
        """
        Get the title of the What's New popup
        """
        self.driver.wait_for_object("hpx_whats_new_popup_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_title")
    
    def get_hpx_whats_new_popup_sub_title(self, timeout=10):
        """
        Get the sub title of the What's New popup
        """
        self.driver.wait_for_object("hpx_whats_new_popup_sub_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_sub_title")
    
    def get_hpx_whats_new_popup_second_screen_title(self, timeout=10):
        """
        Get the title of the What's New popup second screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_title", timeout=10)
        return self.driver.get_text("hpx_whats_new_popup_second_screen_title")
    
    def get_hpx_whats_new_popup_second_screen_sub_title(self, timeout=10):
        """
        Get the sub title of the What's New popup second screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_sub_title", timeout=10)
        return self.driver.get_text("hpx_whats_new_popup_second_screen_sub_title")
    
    def get_hpx_whats_new_popup_third_screen_title(self, timeout=10):
        """
        Get the title of the What's New popup third screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_title", timeout=10)
        return self.driver.get_text("hpx_whats_new_popup_third_screen_title")
    
    def get_hpx_whats_new_popup_third_screen_sub_title(self, timeout=10):
        """
        Get the sub title of the What's New popup third screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_sub_title", timeout=10)
        return self.driver.get_text("hpx_whats_new_popup_third_screen_sub_title")
    
    def click_hpx_whats_new_popup_next_btn(self, timeout=10):
        """
        Click on the next button on the What's New popup
        """
        self.driver.click("hpx_whats_new_popup_next_btn",timeout=timeout)

    def verify_hpx_whats_new_popup(self, timeout=10):
        """
        Verify HPX Whats New Popup
        """
        self.driver.wait_for_object("hpx_whats_new_popup_title", timeout=timeout)
        self.driver.wait_for_object("hpx_whats_new_popup_sub_title", timeout=timeout)
    
    def verify_hpx_whats_new_popup_second_screen(self, timeout=10):
        """
        Verify HPX Whats New Popup Second Screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_title", timeout=timeout)
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_sub_title", timeout=timeout)
    
    def verify_hpx_whats_new_popup_third_screen(self, timeout=10):
        """
        Verify HPX Whats New Popup Third Screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_title", timeout=timeout)
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_sub_title", timeout=timeout)
    
    def click_hpx_whats_new_popup_next_btn(self, timeout=10):
        """
        Click on the next button on the What's New popup
        """
        self.driver.click("hpx_whats_new_popup_next_btn",timeout=timeout)
    
    def click_hpx_whats_new_popup_back_btn(self, timeout=10):
        """
        Click on the back button on the What's New popup
        """
        self.driver.click("hpx_whats_new_popup_back_btn",timeout=timeout)
    
    def verify_hpx_home(self, timeout=10):
        """
        Verify HPX Home screen
        """
        self.driver.wait_for_object("hpx_lets_get_started_title", timeout=timeout)
        self.driver.wait_for_object("hpx_lets_get_started_sub_title", timeout=timeout)
    
    def click_hpx_whats_new_popup_done_btn(self, timeout=10):
        """
        Click on the done button on the What's New popup
        """
        self.driver.click("hpx_whats_new_popup_done_btn",timeout=timeout)
    
    def click_hpx_whats_new_popup_back_btn(self, timeout=10):
        """
        Click on the back button on the What's New popup
        """
        self.driver.click("hpx_whats_new_popup_back_btn",timeout=timeout)
    
    def click_hpx_whats_new_popup_next_btn(self, timeout=10):
        """
        Click on the next button on the What's New popup
        """
        self.driver.click("hpx_whats_new_popup_next_btn",timeout=timeout)