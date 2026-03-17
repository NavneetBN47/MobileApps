from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class NavigationPanel(HPXFlow):
    flow_name = "navigation_panel"

    def get_stack_info(self):
        return self.driver.session_data['request'].config.getoption("--stack")

    def click_navigation_icon(self):
        self.driver.click("navigation_icon")

    def navigate_to_welcome(self):
        self.driver.click("navigate_welcome_module")

    def navigate_to_support(self):
        self.driver.wait_for_object("navigate_support_module", timeout=30)
        time.sleep(3)
        self.driver.click("navigate_support_module")

    def navigate_to_pc_audio(self):
        self.driver.click("navigate_PCdevice_module", timeout=30)
        if self.get_stack_info() == "pie":
            time.sleep(5)
            self.driver.click("audio_module_itg", timeout=20)
        else:
            self.driver.click("navigate_pc_audio_module", timeout=20)

    def navigate_to_feature_apps(self):
        self.driver.click("navigate_feature_apps_module")

    def navigate_to_settings(self):
        self.get_setting_module()
        self.click_setting_module()

    def navigate_to_devices(self, timeout=10):
        self.verify_welcome_module_show()
        time.sleep(5)
        self.driver.click("navigate_devices_module")

    def select_my_hp_account_btn(self):
        self.verify_my_hp_account_btn()
        time.sleep(3)
        self.driver.click("sign_in_icon")

    def verify_my_hp_sign_in(self, timeout=10):
        self.driver.wait_for_object("sign_in_text", timeout=timeout)
    
    def select_my_hp_sign_out_btn(self):
        self.driver.click("sign_out_item")

    def click_close_btn(self):
        self.driver.click("close_btn")

    def click_close_btn(self):
        self.driver.click("close_button")
    
    def click_hamburger_navigation(self):
        self.driver.wait_for_object("hamburger_menu",timeout=20)
        self.driver.click("hamburger_menu")
    
    def navigate_to_pc_device(self):
        self.driver.wait_for_object("navigate_PCdevice_module", timeout=20)
        self.driver.click("navigate_PCdevice_module", timeout = 10)
    
    def verify_pc_device_show(self):
        return self.driver.wait_for_object("navigate_PCdevice_module", raise_e=False, timeout=10)
    
    def get_pc_device_name(self):
        return self.driver.wait_for_object("navigate_PCdevice_module").get_attribute("Name")
    
    def close_popup(self):
        self.driver.click("popup_close_button")

    def verify_welcome_module_show(self):
        return self.driver.wait_for_object("navigate_welcome_module", raise_e=False, timeout=10)

    def verify_navigationicon_show(self):
        return self.driver.wait_for_object("navigation_icon", raise_e=False, timeout=60)

    def verify_pc_audio_show(self):
        time.sleep(10)
        self.driver.click("navigate_PCdevice_module")
        time.sleep(10)
        self.driver.wait_for_object("pcdevice_audio_module", raise_e=False, timeout=30) 
    
    def verify_pc_audio_show_on_PCdevice(self):
        return self.driver.wait_for_object("pcdevice_audio_module", raise_e=False, timeout=5)
    
    def verify_fly_out_sign_in_page(self, timeout=10, raise_e=False):
        return self.driver.wait_for_object("my_account_item", timeout=timeout, raise_e=raise_e) and \
               self.driver.wait_for_object("go_my_account_item", timeout=timeout, raise_e=raise_e) and \
               self.driver.wait_for_object("sign_out_item", timeout=timeout, raise_e=raise_e)

    def verify_my_hp_account_btn(self, raise_e=True):
        return self.driver.wait_for_object("sign_in_icon", raise_e=raise_e, clickable=True)

    
    def navigate_pc_programmable_key_module(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.click("hppk_module_itg")
        else:
            self.driver.click("programmable_key_link")     

    def navigate_pc_smartcamV3_module(self):
        self.driver.click("navigate_PCdevice_module")
        time.sleep(2)
        self.driver.wait_for_object("smartcamV3_link", raise_e=False, timeout=20)
        self.driver.click("smartcamV3_link")

    def navigate_pc_display_control_module(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.click("displaycontrol_module_itg",timeout=20)
        else:
            self.driver.click("display_control_link",timeout=20)  

    def verify_hamburger_menu_navigation(self):
        return self.driver.get_attribute("hamburger_menu","Name")

    def verify_home_menu_navigation(self):
        return self.driver.get_attribute("navigate_welcome_module","Name")

    def verify_powermanager_menu_navigation(self):
        return self.driver.get_attribute("navigate_power_manager","Name")

    def verify_devices_menu_navigation(self):
        return self.driver.get_attribute("navigate_devices_module","Name", timeout = 20)

    def verify_support_menu_navigation(self):
        return self.driver.get_attribute("navigate_support_module","Name")

    def verify_settings_menu_navigation(self):
        return self.driver.get_attribute("navigate_settings_module","Name")

    def verify_PC_device_menu(self,state):
        if (state=="Collapsed"):
            self.driver.click("navigate_devices_module", timeout = 20)
        return self.driver.get_attribute("navigate_PCdevice_module","Name", timeout = 20)

    def click_PC_device_menu(self):
        self.driver.click("navigate_PCdevice_module", timeout=20)

    def check_PC_device_menu_arrow(self):
        return self.driver.get_attribute("navigate_devices_module","ExpandCollapse.ExpandCollapseState", timeout = 20)

    def click_devices_menu_navigation(self):
        self.driver.click("navigate_devices_module")
        return self.driver.wait_for_object("navigation_icon")

    def navigate_to_pc_device_menu(self):
        text = self.driver.get_attribute("hamburger_menu","Name", timeout=60)
        if text=="Open Navigation":
            self.driver.click("hamburger_menu")

    def navigate_to_privacy_alert(self):
        self.navigate_to_pc_device()
        self.driver.click("privacy_alert_link")


    def navigate_to_auto_dimming(self):
        self.navigate_to_pc_device()
        self.driver.click("dimming_link")
    
    def navigate_to_5G_module(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.click("fiveG_module_itg")
        else:
            self.driver.click("fiveG_link")

    def navigate_to_rgb_keyboard_module(self):
        self.navigate_to_pc_device()
        self.driver.click("rgb_keyboard_link")

    def navigate_to_pen_control_module(self):
        self.driver.wait_for_object("navigate_pencontrol_module",raise_e=False, timeout = 60) 
        self.driver.click("navigate_pencontrol_module",timeout =60)

    def verify_fly_out_sign_in_page(self, timeout=10, raise_e=False):
        return self.driver.wait_for_object("my_account_item", timeout=timeout, raise_e=raise_e) and \
               self.driver.wait_for_object("go_my_account_item", timeout=timeout, raise_e=raise_e) and \
               self.driver.wait_for_object("sign_out_item", timeout=timeout, raise_e=raise_e)

    def verify_my_hp_account_btn(self, raise_e=True):
        return self.driver.wait_for_object("sign_in_icon", raise_e=raise_e)

    def make_my_hp_sign_out(self):
        logged_in = self.verify_fly_out_sign_in_page()
        if logged_in:
            self.select_my_hp_sign_out_btn()
            time.sleep(1)
            self.select_my_hp_account_btn()
            time.sleep(2)

    def verify_support_module_show(self):
        return self.driver.wait_for_object("navigate_support_module", raise_e=False, timeout=20)

    def verify_pcdevice_module_show(self):
        return self.driver.wait_for_object("navigate_devices_module",raise_e=False, timeout=10)

    def verify_setting_module_show(self):
        return self.driver.wait_for_object("navigate_settings_module",raise_e=False, timeout=10)

    def verify_home_navagation(self):
        return self.driver.wait_for_object("navigate_welcome_module",raise_e=False, timeout=10)

    def verify_pen_control_visible(self): 
        return self.driver.wait_for_object("navigate_pencontrol_module",raise_e=False, timeout=10) 
    
    def navigate_to_system_control(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.click("systemcontrol_module_itg", raise_e=False, timeout=10)
        else:
            self.driver.click("navigate_system_control", raise_e=False, timeout=10)
    
    def navigate_to_screen_time(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.click("screentime_module_itg")
        else:
            self.driver.click("navigate_screen_time")
    
    def navigate_to_screen_distance(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.click("screendistance_module_itg")
        else:
            self.driver.click("navigate_screen_distance")
    
    def navigate_external_mouse_module(self):
        self.navigate_to_pc_device()
        self.driver.wait_for_object("external_mouse_module",raise_e=False, timeout=10) 
        self.driver.click("external_mouse_module")
    
    def navigate_external_keyboard_module(self):
        self.driver.wait_for_object("external_keyboard_module",raise_e=False, timeout=30)
        time.sleep(3)
        self.driver.click("external_keyboard_module")
    
    def navigate_touchpad_module(self):
        self.navigate_to_pc_device()
        if self.get_stack_info() == "pie":
            self.driver.wait_for_object("touchpad_module_itg",raise_e=False, timeout=20) 
            self.driver.click("touchpad_module_itg")
        else:
            self.driver.wait_for_object("touchpad_module",raise_e=False, timeout=20) 
            self.driver.click("touchpad_module")
    
    def verify_navigate_PCdevice_module(self):
        return self.driver.wait_for_object("navigate_PCdevice_module",raise_e=False, timeout=10)
    
    def navigate_to_battery_module(self):
        self.navigate_to_pc_device()
        self.driver.wait_for_object("battery_module_itg",raise_e=False, timeout=20) 
        self.driver.click("battery_module_itg", raise_e=False, timeout=20)

    def get_battery_manager_text_settings(self):
        return self.driver.get_attribute("battery_manager_text_settings","Name")
    
    def verify_battery_manager_text_settings(self, timeout=10):
        self.driver.wait_for_object("battery_manager_text_settings", timeout=timeout)

    def click_battery_manager_text(self):
        self.driver.click("battery_manager_text_settings", timeout = 20)


    def navigate_to_gesture_module(self):
        self.navigate_to_pc_device()
        self.driver.wait_for_object("gesture_card_on_pc_device_page",raise_e=False, timeout=20) 
        self.driver.click("gesture_card_on_pc_device_page", raise_e=False, timeout=20)

    def get_user_initials_icon_text(self):
        return self.driver.get_attribute("user_initials_icon","Name")

    def verify_presence_sensing_module_show(self):
        return self.driver.wait_for_object("presence_sensing_module",raise_e=False, timeout=10)
    
    def click_presence_sensing_module(self):
        self.driver.wait_for_object("presence_sensing_module",raise_e=False, timeout=10) 
        self.driver.click("presence_sensing_module")

    def verify_power_battery_settings_page_show(self):
        return self.driver.wait_for_object("power_battery_settings_page",raise_e=False, timeout=10)
    
    def click_close_button_on_power_battery_settings_page(self):
        self.driver.click("close_button_on_power_battery_settings_page")

    def verify_home_audio_card_show(self):
        return self.driver.wait_for_object("audio_card_home", raise_e=False, timeout=20)

    def verify_updated_pop_window_show(self):
        return self.driver.wait_for_object("updated_pop_window_title", raise_e=False, timeout=5)

    def click_update_pop_window_agree_button(self):
        self.driver.click("updated_pop_window_agree_button", timeout = 5)

    def navigate_to_presence_detection(self):
        self.navigate_to_pc_device()
        self.driver.click("presence_detection")  

    def get_setting_module(self):
        return self.driver.get_attribute("navigate_settings_module","Name", timeout=10)
    
    def click_setting_module(self):
        time.sleep(5)
        self.driver.click("navigate_settings_module")
        self.driver.click("navigate_settings_module")