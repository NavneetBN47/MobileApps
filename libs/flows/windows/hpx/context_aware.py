from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow


class ContextAware(HPXFlow):
    flow_name = "context_aware"

    def verify_context_aware(self):
        return self.driver.get_attribute("add_application_button", "Name")
    
    def click_add_application(self):
        self.driver.click("add_application_button", timeout = 10)
    
    def verify_add_application_modal(self):
        return self.driver.get_attribute("add_application_add_applications_text", "Name")
    
    def click_add_application_search_box(self):
        self.driver.click("add_application_search_application_textbox", timeout = 15)
    
    def search_application(self,app_name):
        self.driver.send_keys("add_application_search_application_textbox",app_name)
    
    def verify_application(self, ui_name):
        return self.driver.wait_for_object(ui_name, raise_e=False, timeout=20)
    
    def click_application(self, ui_name):
        self.driver.click(ui_name, timeout = 20)
    
    def verify_application_icon(self, ui_name):
        return self.driver.get_attribute(ui_name, "Name")
    
    def verify_add_application_add_button(self):
        return self.driver.wait_for_object("add_application_add_button", raise_e=False, timeout=20)
    
    def click_add_application_add_button(self):
        self.driver.click("add_application_add_button", timeout = 20)
    
    def application_icon(self):
        return self.driver.wait_for_object("select_application_button", raise_e=False, timeout=20)
    
    def click_all_applications(self):
        self.driver.click("all_applications_icon")
    
    def verify_left_arrow(self):
        return self.driver.wait_for_object("scroll_applications_left_button", raise_e=False, timeout=20)
    
    def verify_right_arrow(self):
        return self.driver.wait_for_object("scroll_applications_right_button", raise_e=False, timeout=20)
    
    def click_left_arrow(self):
        self.driver.click("scroll_applications_left_button", timeout = 10)
    
    def click_right_arrow(self):
        self.driver.click("scroll_applications_right_button", timeout = 10)
    
    def click_application_icon(self):
        self.driver.click("select_application_button", timeout = 10)
    
    def verify_delete_application_button(self, ui_name):
        return self.driver.get_attribute("delete_application_button" + "_" + ui_name, "Name")
    
    def click_delete_application_button(self, ui_name):
        self.driver.click("delete_application_button" + "_" + ui_name)
    
    def click_delete_continue_application_button(self):
        self.driver.click("delete_application_continue_button", timeout = 10)
    
    def click_delete_cancel_application_button(self):
        self.driver.click("delete_application_cancel_button", timeout = 10)

    def click_cancel_button(self):
        self.driver.click("add_application_cancel_button", timeout = 10)
    
    def click_do_not_show_checkbox(self):
        self.driver.click("delete_application_donotshowagain_checkbox", timeout = 10)

    def verify_disney_plus_app_show(self):
        return self.driver.wait_for_object("disney+", raise_e=False, timeout = 10) is not False
    
    def verify_tencent_video_app_show(self):
        return self.driver.wait_for_object("tencent", raise_e=False, timeout = 10) is not False
    
    def verify_iqiyi_app_show(self):
        return self.driver.wait_for_object("iqiyi", raise_e=False, timeout = 10) is not False
    
    def click_access_app(self):
        self.driver.click("access", timeout = 10)
    
    def click_disney_icon(self):
        self.driver.click("disney+", timeout = 10)

    def click_delete_disney_icon(self):
        self.driver.click("delete_application_button_disney+", timeout = 10)
    
    def click_iqiyi(self):
        self.driver.click("iqiyi", timeout = 10)
    
    def click_delete_iqiyi_icon(self):
        self.driver.click("delete_application_button_iqiyi", timeout = 10)
    
    def verify_delete_do_not_show_checkbox(self):
        return self.driver.wait_for_object("delete_application_donotshowagain_checkbox", raise_e=False, timeout = 10) is not False
    
    def verify_iqiyi_icon_show(self):
        return self.driver.wait_for_object("iqiyi", raise_e=False, timeout = 10) is not False
    
    def click_calculator_icon(self):
        self.driver.click("calculator", timeout = 10)
    
    def verify_calculator_delete_icon_show(self):
        return self.driver.wait_for_object("delete_application_button_calculator", raise_e=False, timeout = 10) is not False
    
    def verify_context_aware_show(self):
        return self.driver.wait_for_object("all_applications_icon", raise_e=False, timeout = 10) is not False
    
    def verify_add_application_button_show(self):
        return self.driver.wait_for_object("add_application_button", raise_e=False, timeout = 10) is not False
    
    def verify_privacy_settings_button_show(self):
        return self.driver.wait_for_object("privacy_setting", raise_e=False, timeout = 10) is not False

    def get_access_name(self):
        return self.driver.get_attribute("access", "Name")

    def click_calculator_delete_icon(self):
         self.driver.click("delete_application_button_calculator", timeout = 10)  

    def click_camera_icon(self):
         self.driver.click("camera", timeout = 10)     
        
    def click_camera_delete_icon(self):
         self.driver.click("delete_application_button_camera", timeout = 10)
    
    def verify_camera_icon_show(self):
        return self.driver.wait_for_object("camera", raise_e=False, timeout = 10) is not False
