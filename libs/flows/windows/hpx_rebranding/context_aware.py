from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare

class ContextAware(HPXRebrandingFlow):
    flow_name = "context_aware"

    def click_all_application_button_ltwo_page(self):
        self.driver.click("all_application_button_ltwo_page", timeout = 10)

    def click_add_button_ltwo_page(self):
        self.driver.click("add_application_button_ltwo_page", timeout = 10)

    def click_add_app_cancel_button_ltwo_page(self):
        self.driver.click("add_app_cancel_onpopup_window_page", timeout = 10)

    def click_add_app_continue_button_ltwo_page(self):
        self.driver.click("add_app_continue_onpopup_window_page", timeout = 10)

    def click_delete_profile_button(self):
        self.driver.click("delete_profile_button", timeout = 15)

    def click_do_not_show_again_check_box(self):
        self.driver.click("do_not_show_checkbox_ltwo_page", timeout=10)  

    def verify_do_not_show_again_check_box_state(self):
        return self.driver.get_attribute("do_not_show_checkbox_ltwo_page", "Toggle.ToggleState",  timeout = 10)

    def click_next_button_arrow_for_carousel_item(self):
        self.driver.click("next_button_on_applicatio_settings", timeout = 10)

    def click_disney_plus_app_carousel(self):
        self.driver.click("disney_plus_app_carousel", timeout = 10)

    def click_tencent_app_carousel(self):
        self.driver.click("tencent_app_carousel", timeout = 10)

    def click_iqiyi_app_carousel(self):
        self.driver.click("iqiyi_app_carousel", timeout = 10)

    def click_access_app_carousel(self):
        self.driver.click("access_app_carousel", timeout = 10)

    def click_calculator_app_carousel(self):
        self.driver.click("calculator_app_carousel", timeout = 10)

    def click_clock_app_carousel(self):
        self.driver.click("clock_app_carousel", timeout = 10)

    def click_paint_app_carousel(self):
        self.driver.click("paint_app_carousel", timeout = 10)

    def click_calendar_app_carousel(self):
        self.driver.click("calender_app_carousel", timeout = 10)

    def click_camera_app_carousel(self):
        self.driver.click("camera_app_carousel", timeout = 10)

    def click_copilot_app_carousel(self):
        self.driver.click("copilot_app_carousel", timeout = 10)

    def enter_app_name_in_add_app_search_bar_ltwo_page(self,app_name,locator):
        self.driver.click("add_application_button_ltwo_page")
        self.driver.click("add_app_search_bar_ltwo_page", timeout = 10)
        self.driver.send_keys("add_app_search_bar_ltwo_page", app_name)
        self.driver.click(locator, timeout = 10)
        self.driver.click("add_app_continue_onpopup_window_page", timeout = 10)

    def delete_app(self,locator):
        self.driver.click(locator, timeout = 10)
        self.driver.click("delete_profile_button", timeout = 10)
        self.driver.click("add_app_continue_onpopup_window_page", timeout = 10)
    
    def verify_clock_app_carousel(self):
        return self.driver.wait_for_object("clock_app_carousel", raise_e=False, timeout=15)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_all_application_button_ltwo_page_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("all_application_button_ltwo_page", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_add_app_cancel_button_ltwo_page_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("add_app_cancel_onpopup_window_page", raise_e=False, timeout=10)

    @screenshot_compare(pass_ratio=0.02)
    def verify_color_filter_page1(self):
        return self.driver.wait_for_object("all_application_button_ltwo_page", raise_e=False, timeout=10)

    @screenshot_compare(pass_ratio=0.02)
    def verify_color_filter_page2(self):
        return self.driver.wait_for_object("add_app_cancel_onpopup_window_page", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["mode"], pass_ratio=0.02)
    def verify_all_application_button_ltwo_page_mode(self, mode):
        return self.driver.wait_for_object("all_application_button_ltwo_page", raise_e = False, timeout = 10)
    
    @screenshot_compare(include_param=["mode"], pass_ratio=0.02)
    def verify_add_app_cancel_button_ltwo_page_mode(self, mode):
        return self.driver.wait_for_object("add_app_cancel_onpopup_window_page", raise_e = False, timeout = 10)

