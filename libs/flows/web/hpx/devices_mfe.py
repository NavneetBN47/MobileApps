from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from time import sleep
from SAF.decorator.saf_decorator import screenshot_compare
import logging
import time

class DevicesMFE(HPXFlow):
    flow_name = "devices_mfe"


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_new_hp_app_popup(self, raise_e=True):
        return self.driver.wait_for_object("new_hp_app_popup_skip_btn", raise_e=raise_e)
    
    def verify_home_nav(self, timeout=10, raise_e=True):
        return self.verify_app_bar_mfe(timeout=timeout, raise_e=raise_e)
    
    def verify_windows_dummy_printer(self, _printer, timeout=10, raise_e=True):
        #Alpha code, cannot add printer so using a dummy printer by using a recent device list xml file 8/26/2024
        return self.driver.wait_for_object("windows_dummy_printer_device", format_specifier=[_printer], timeout=timeout, raise_e=raise_e)
    
    def verify_windows_dummy_printer_removed(self, _printer, timeout=20, invisible=True, raise_e=False):
        self.driver.wait_for_object("windows_dummy_printer_device", format_specifier=[_printer], timeout=timeout, invisible=invisible, raise_e=raise_e)

    def verify_printer_friend_name(self, timeout=10):
        return self.driver.get_attribute("printer_friend_name", attribute="Name", timeout=timeout)

    def verify_printer_model_name(self):
        return self.driver.wait_for_object("printer_model_name")

    def verify_supply_levels_card(self, timeout=10, raise_e=True):
        if not self.driver.wait_for_object("supply_levels_card", timeout=timeout, raise_e=False):
            el = self.driver.wait_for_object("main_webview_pane")
            el.click()
            return el.send_keys(Keys.CONTROL+"r")
        sleep(3)
        self.driver.wait_for_object("supply_levels_card", timeout=timeout, raise_e=raise_e)

    def verify_app_bar_mfe(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("app_bar_mfe_section", timeout=timeout, raise_e=raise_e)
    
    def verify_device_status_mfe(self):
        return self.driver.wait_for_object("device_status_section", displayed=False)
    
    def verify_side_panel_mfe(self):
        return self.driver.wait_for_object("account_panel_section")
    
    def verify_home_loggedin(self, timeout=3, raise_e=False):
        return self.driver.wait_for_object("top_signin_button", invisible=True, timeout=timeout, raise_e=raise_e)
    
    def verify_device_card_show_up(self, raise_e=True, timeout=60):
        return self.driver.wait_for_object("device_card", raise_e=raise_e, timeout=timeout)
    
    def verify_top_devices_icon_show_up(self, raise_e=True):
        return self.driver.wait_for_object("top_devices_icon", raise_e=raise_e)
    
    def verify_shop_icon_show_up(self):
        return self.driver.wait_for_object("shop_icon")

    def verify_add_device_button_show_up(self, timeout=10, raise_e=True):
        if self.driver.wait_for_object("top_add_button", timeout=timeout, raise_e=False) is False and self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="up", distance=8)
        return self.driver.wait_for_object("top_add_button", timeout=timeout, raise_e=raise_e)

    def verify_bell_icon_show_up(self, raise_e=True):
        return self.driver.wait_for_object("top_notifications_button", raise_e=raise_e)
    
    def verify_profile_icon_show_up(self, timeout=20, raise_e=False):
        return self.driver.wait_for_object("top_profile_button", timeout=timeout, raise_e=raise_e)

    def verify_sign_in_button_show_up(self, raise_e=True):
        return self.driver.wait_for_object("top_signin_button", raise_e=raise_e)

    def verify_login_successfully(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("top_notifications_button", timeout=timeout, raise_e=raise_e) and \
            self.driver.wait_for_object("top_profile_button", timeout=2, raise_e=False) is False and \
            self.driver.wait_for_object("top_signin_button", timeout=2, raise_e=False) is False

    def verify_logout_successfully(self, raise_e=True):
        return self.driver.wait_for_object("top_profile_button", raise_e=raise_e) and \
            self.driver.wait_for_object("top_signin_button", raise_e=raise_e)
    
    def verify_window_maximize(self):
        self.driver.wait_for_object("maximize_myHP", raise_e=False, timeout=20)
        return self.driver.get_attribute("maximize_myHP","Name")

    def click_home_loggedin(self):
        return self.driver.click("top_signin_button")
    
    def verfiy_device_container_show(self):
        return self.driver.wait_for_object("device_card", raise_e=False, timeout=60) is not False
    
    def verify_pen_card_show(self):
        return self.driver.wait_for_object("pen_card", raise_e=False, timeout=20) is not False

    def verify_browser_webview_pane(self,raise_e=False, timeout=15):
        return self.driver.wait_for_object("main_webview_pane", raise_e=raise_e, timeout=timeout)
    
    def verify_dock_station_card_show(self):
        return self.driver.wait_for_object("dock_station_card", raise_e=False, timeout = 10)
    
    def verify_system_charging_status(self):
        return self.driver.get_attribute("charging_status", "Name",  timeout = 10)
    
    def verify_hpai_assistant_button_on_header(self):
        return self.driver.wait_for_object("hpai_assistant_button_on_header", raise_e=False, timeout = 10)
    
    def verify_profile_and_settings_icon_button_lzero_page(self):
        return self.driver.wait_for_object("profile_and_settings_icon_button_lzero_page", raise_e=False, timeout=30)

    def verify_device_mfe_panel_show_up(self):
        self.verify_profile_icon_show_up()
        self.verify_sign_in_button_show_up()
        return True

    def verify_shop_icon_preview(self, raise_e=False):
        return self.driver.wait_for_object("shop_icon_create_account_button", raise_e=raise_e, timeout=10)
    
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_myhp_window(self):
        self.driver.click("myhp_window")
    
    def scroll_to_printer(self, _printer, timeout=40):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.driver.wait_for_object("windows_dummy_printer_device", format_specifier=[_printer], raise_e=False):
                return
            el = self.driver.wait_for_object("main_webview_pane")
            el.send_keys(Keys.PAGE_DOWN)
            sleep(1)

    def click_top_minimize_btn(self):
        self.driver.click("minimize_btn")
    
    def click_top_maximize_btn(self):
        self.driver.click("maximize_btn")
    
    def click_top_close_btn(self):
        self.driver.click("close_btn")
        
    def click_new_hp_app_popup_skip(self):
        return self.driver.click("new_hp_app_popup_skip_btn")
        
    def refresh_device_mfe(self):
        el = self.driver.wait_for_object("main_webview_pane")
        self.driver.click_by_coordinates_with_offset(el, x_offset=0.9, y_offset=0.9)
        sleep(1)
        return el.send_keys(Keys.CONTROL+"r")
    
    def swipe_to_end(self):
        el = self.driver.wait_for_object("main_webview_pane")
        el.click()
        return el.send_keys(Keys.END)

    def click_windows_dummy_printer(self, _printer):
        if self.driver.click("windows_dummy_printer_device", format_specifier=[_printer], change_check={"wait_obj": "device_card", "invisible": True}, retry=2, delay=1,  raise_e=False) is False:
            el = self.driver.wait_for_object("windows_dummy_printer_device", format_specifier=[_printer], timeout=2)
            el.send_keys(Keys.ENTER)
        if self.driver.wait_for_object("feature_unavailable_text", raise_e=False, timeout=2):
            self.driver.click("dialog_ok_btn")
        # For some printers, "Firmware Update Available" dialog may pop up
        if self.driver.wait_for_object("fw_update_title", raise_e=False, timeout=2):
            self.driver.click("fw_update_no_btn", change_check={"wait_obj": "fw_update_no_btn", "invisible": True})

    def get_first_printer_device_card_info(self):
        return self.driver.get_attribute("first_printer_device_card", attribute="Name")
        
    def click_add_button(self):
        self.verify_add_device_button_show_up()
        self.driver.click("top_add_button", change_check={"wait_obj": "add_device_text", "flow_change": "add_printer"}, retry=3, delay=2)
        
    def click_device_tile(self):
        self.driver.click("device_tile")
        
    def click_profile_button(self):
        self.driver.click("top_profile_button",change_check={"wait_obj": "profile_side_panel"},retry=3)

    def click_device_icon(self):
        self.driver.click("device_icon")

    def click_close_button(self):
        el = self.driver.wait_for_object("account_panel_close_button", displayed=False)
        self.driver.wdvr.execute_script("arguments[0].click();", el)

    def click_device_card(self):
        if self.driver.wait_for_object("device_card_stage_prod", raise_e=False, timeout=10) is not False:
            self.driver.click("device_card_stage_prod", timeout = 10)
        elif self.driver.wait_for_object("device_card", raise_e=False, timeout=5) is not False:
            self.driver.click("device_card", timeout = 10)
        else:
            logging.info("There is no pc device L0 page")
        if self.driver.wait_for_object("feature_not_available_itg_pop_up", raise_e=False, timeout=10) is not False:
            self.driver.click("itg_pop_up_ok_button", timeout = 10)
    
    def maximize_app(self):
        self.driver.click("maximize_myHP")

    def restore_app(self):
        self.driver.click("restore_myHP")

    def minimize_app(self):
        self.driver.click("minimize_app")

    def close_app(self):
        self.driver.click("close_myHP" , timeout = 10)
    
    def click_minimize_app(self):
        if self.driver.wait_for_object("minimize_app", timeout=10):
            self.driver.click("minimize_app")

    def click_myhp_on_task_bar(self):
        if self.driver.wait_for_object("myhp_on_task_bar", raise_e=False, timeout=10) is not False:
            self.driver.click("myhp_on_task_bar", timeout= 20)    

    def click_profile_and_settings_icon_button_lzero_page(self):
        self.driver.click("profile_and_settings_icon_button_lzero_page", timeout=15)

    def click_navigation_bar_settings_card_arrow_lzero_page(self):
        if self.driver.wait_for_object("sideflyout_sign_in_link", raise_e=False, timeout=15):
            self.driver.click("navigation_bar_settings_card_arrow_lzero_page")

    def get_hpx_version_lzero_page(self):
        return self.driver.get_attribute("hpx_version_lzero_page","Name")
        
    def click_back_button_rebranding(self):
        if self.driver.wait_for_object("back_button_rebranding", raise_e=False, timeout=60) is not False:
            self.driver.click("back_button_rebranding", timeout = 20)
        if self.driver.wait_for_object("feature_not_available_itg_pop_up", raise_e=False, timeout=10) is not False:
            self.driver.click("itg_pop_up_ok_button", timeout = 10)     
        else:
            logging.info("Back button on device card page is not present")

    def click_navigation_bar_menu_arrow_lzero_page(self):
        self.driver.click("menu_back_button_sign_in_side_navbar_lzero", timeout = 10)

    def click_navigation_bar_close_button_arrow_lzero_page(self):
        self.driver.click("close_button_sign_in_side_navbar_lzero", timeout = 10)

    def click_ok_btn_error_popup(self):
        self.driver.click("ok_btn_error_popup", timeout = 10)
    
    def click_device_card_by_index(self, index=0):
        if self.driver.wait_for_object("device_card_stage_prod", raise_e=False, timeout=10) is not False:
            self.driver.click("device_card_stage_prod", index, timeout = 20)
        else:
            self.driver.click("device_card", index, timeout = 20)

    def click_secondary_device_card_by_index(self, index=0):
        if self.driver.wait_for_object("secondary_device_card", raise_e=False, displayed=False,  timeout=10) is not False:
            self.driver.find_object("secondary_device_card", multiple=True)[index].click()

    def select_my_hp_account_btn(self):
        self.driver.click("top_signin_button", timeout=30)

    def click_pen_card(self):
        self.driver.click("pen_card", timeout = 10)

    def click_pen_card_by_index(self, index=0):
        self.driver.click("pen_card", index, displayed=False, timeout = 10)

    def click_top_profile_icon(self):
        self.driver.click("top_profile_button", timeout=60)

    def verify_top_profile_icon(self):
        return self.driver.wait_for_object("top_profile_button", timeout=10) is not False

    def verify_system_charging_status(self):
        return self.driver.get_attribute("charging_status", "Name",  timeout = 10)

    def click_dock_station_card(self):
        self.driver.click("dock_station_card", timeout = 15) 

    def maximize_the_hpx_window(self):
        if "Maximize HP" == self.verify_window_maximize():
            self.maximize_app()

    @screenshot_compare(root_obj="pen_card", raise_e=False)
    def verify_pen_card_image(self):
        return self.driver.wait_for_object("pen_card", raise_e=False, timeout=20)
    
    def navigate_back_from_page_using_locator(self, locator):
        if self.driver.wait_for_object(locator, raise_e=False, timeout=10) is not False:
            self.click_back_button_rebranding()      

    def verify_back_button_rebranding_text(self):
        return self.driver.get_attribute("back_button_rebranding", "Name",  timeout = 10)

    def click_hpai_assistant_button_on_header(self):
        self.driver.click("hpai_assistant_button_on_header", timeout= 20)

    def click_devices_button_on_header(self):
        self.driver.click("devices_button_on_header", timeout= 20)

    def click_door_open_sms_btn(self):
        self.driver.click("door_open_sms_btn")

    def click_close_app(self):
        self.driver.click("close_myhp_app" , timeout = 10)

    def click_shop_icon(self):
        self.driver.click("shop_icon", timeout =10)
        