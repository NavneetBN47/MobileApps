from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
import time
from SAF.decorator.saf_decorator import screenshot_compare

class DevicesDetailsPCMFE(HPXFlow):
    flow_name = "devices_details_pc_mfe"

# *********************************************************************************
#                                VERIFICATION FLOWS                               *
# *********************************************************************************
    def verify_pc_device_name_show_up(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("devices_name", raise_e=raise_e, timeout=timeout)

    def verify_device_updates(self, raise_e=True):
        self.driver.scroll_element("device_updates")
        return self.driver.wait_for_object("device_updates", raise_e=raise_e, timeout=20)

    def click_on_check_for_updates(self, raise_e=True):
        self.driver.scroll_element("check_for_updates_button")
        return self.driver.click("check_for_updates_button", raise_e=raise_e, timeout=20)

    def verify_check_for_updates_page(self, raise_e=True):
        self.driver.scroll_element("device_updates_page")
        return self.driver.wait_for_object("device_updates_page", raise_e=raise_e, timeout=20)

    def return_nick_name_of_pc_device(self):
        return self.driver.get_attribute("devices_name", "Name", timeout=15)

    def verify_audio_card_show_up(self):
        if self.driver.wait_for_object("audio_card", raise_e=False, timeout=30) is False:
            self.driver.scroll_element("audio_card", direction="down", distance=2, time_out=20)
        return self.driver.wait_for_object("audio_card", raise_e=False, timeout = 30)

    def verify_hppk_card_show_up(self):
        return self.driver.wait_for_object("hppk_card",timeout = 10)
    
    def verify_display_control_lone_page(self):
        return self.driver.get_attribute("display_control_card_lone_page", "Name",  timeout = 15)
    
    def verify_touch_pad_lone_page(self):
        return self.driver.wait_for_object("touchpad_card", raise_e=False, timeout = 10)

    def verify_back_devices_button_on_pc_devices_page_show_up(self):
        return self.driver.wait_for_object("back_devices_button_on_pc_devices_page", raise_e=False, timeout = 15)

    def verify_advertise_on_pc_devices_page_show_up(self):
        return self.driver.wait_for_object("advertise_on_pc_devices_page", raise_e=False, timeout=15)
    
    def verify_product_information_title_show_up(self):
        self.driver.scroll_element("product_information_title")
        return self.driver.wait_for_object("product_information_title", raise_e=False, timeout=15)
    
    def verify_wellbeing_card_lone_page_show(self):
        return self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout=15)
    
    def verify_battery_manager_card_lone(self):
        return self.driver.wait_for_object("battery_manager_card_lone", raise_e=False, timeout=15)

    def verify_battery_manager_card_optimize_battery_performance_lone(self):
        return self.driver.wait_for_object("battery_manager_card_optimize_battery_performance_lone", raise_e=False, timeout=15)

    def verify_battery_manager_text_lone(self):
        return self.driver.wait_for_object("battery_manager_text_lone", raise_e=False, timeout=15)

    def verify_battery_manager_icon_lone(self):
        return self.driver.wait_for_object("battery_manager_icon_lone", raise_e=False, timeout=15)
    
    def verify_gesture_card_lone_page_show(self):
        return self.driver.wait_for_object("gesture_card", raise_e=False, timeout=15)
    
    def verify_system_control_lone_page_show(self):
        return self.driver.wait_for_object("system_control_card_lone_page", raise_e=False, timeout=15)
    
    def verify_presence_sensing_lone_page_show(self):
        return self.driver.wait_for_object("presence_sensing_card_lone_page", raise_e=False, timeout=15)

    def verify_presence_detection_card_lone_page(self):
        return self.driver.wait_for_object("presence_detection_card_lone_page",raise_e=False, timeout = 10)

    def verify_audio_control_card_show(self):
        return self.driver.wait_for_object("audio_control_card_lone_page", timeout = 10)

    def verify_energy_consumption_card_show(self):
        return self.driver.wait_for_object("energy_consumption_card_lone_page", timeout = 10)

    def verfiy_product_information_header_show(self,raise_e=False, timeout=15):
        self.driver.scroll_element("product_info_header")
        return self.driver.wait_for_object("product_info_header", raise_e=raise_e, timeout=timeout) is not False

    def verfiy_product_number_show(self):
        self.driver.scroll_element("product_number")
        return self.driver.wait_for_object("product_number", raise_e=False, timeout=10) is not False

    def verfiy_serial_number_show(self):
        self.driver.scroll_element("serial_number")
        return self.driver.wait_for_object("serial_number", raise_e=False, timeout=10) is not False

    def verfiy_warranty_status_show(self):
        self.driver.scroll_element("warranty_status")
        return self.driver.wait_for_object("warranty_status", raise_e=False, timeout=10) is not False

    def verify_more_information_button_show(self):
        self.driver.scroll_element("more_information")
        return self.driver.wait_for_object("more_information", raise_e=False, timeout=10) is not False

    def verify_video_lone_page(self):
        return self.driver.wait_for_object("video_card_lone_page",raise_e=False, timeout = 10)
    
    def verify_battery_status_icon_show(self):
        return self.driver.wait_for_object("device_battery_icon",raise_e=False, timeout = 10)
    
    def get_battery_status_icon_text(self):
        return self.driver.get_attribute("device_battery_icon", "Name",  timeout = 15)

    def verify_hp_go_card_show_on_pc_device_page(self):
        return self.driver.wait_for_object("hp_go_card", timeout=10, raise_e=False)

    def verify_app_version_on_the_top(self):
        return self.driver.wait_for_object("app_version_on_the_top", raise_e=False, timeout = 10)
    
    def get_system_module_name(self):
        return self.driver.get_attribute("system_module_name", "Name",  timeout = 15, raise_e=False)
    
    def verify_task_group_lone_page(self):
        return self.driver.wait_for_object("task_group_lone_page",raise_e=False, timeout = 10)
    
    def verify_smart_displays_lone_page(self):
        return self.driver.wait_for_object("smart_displays_lone_page",raise_e=False, timeout = 10)

    def get_hp_go_text_on_hpgo_card(self):
        return self.driver.get_attribute("hp_go_text_on_hpgo_card", "Name",  timeout = 15, raise_e=False)

    def get_usage_on_hpgo_card(self):
        return self.driver.get_attribute("usage_on_hpgo_card", "Name",  timeout = 15, raise_e=False)

    def verify_hpgo_icon_on_card(self):
        return self.driver.wait_for_object("hpgo_icon_on_card", raise_e=False, timeout=10)

    def press_enter(self, element):
        self.driver.send_keys(element, Keys.ENTER)    

    def verify_hp_ai_assistant_button_show_up(self):
        return self.driver.wait_for_object("hp_ai_assistant_button", raise_e=False)

    def verify_optimize_performance_button_show_up(self):
        self.driver.scroll_element("optimize_performance_button")
        return self.driver.wait_for_object("optimize_performance_button")

    def verify_check_for_audio_issues_button_show_up(self):
        self.driver.scroll_element("check_for_audio_issues_button")
        return self.driver.wait_for_object("check_for_audio_issues_button")

    def verify_run_system_tests_button_show_up(self):
        self.driver.scroll_element("run_system_tests_button")
        return self.driver.wait_for_object("run_system_tests_button")

    def verify_run_hardware_tests_button_show_up(self):
        self.driver.scroll_element("run_hardware_tests_button")
        return self.driver.wait_for_object("run_hardware_tests_button")

    def verify_get_help_module_show_up(self,raise_e=False,timeout=15):
        self.driver.scroll_element("get_help_module_title")
        return self.driver.wait_for_object("get_help_module_title", raise_e=raise_e,timeout=timeout)
    
    def verify_start_virtual_assistant_button_show_up(self,raise_e=False,timeout=15):
        self.driver.scroll_element("start_virtual_assistant_button")
        return self.driver.wait_for_object("start_virtual_assistant_button",raise_e=raise_e,timeout=timeout)

    def verify_view_manual_and_guides_link_show_up(self):
        self.driver.scroll_element("view_manual_and_guides_link")
        return self.driver.wait_for_object("view_manual_and_guides_link",raise_e=False)

    def verify_find_a_repair_center_link_show_up(self):
        self.driver.scroll_element("find_a_repair_center_link")
        return self.driver.wait_for_object("find_a_repair_center_link",raise_e=False)

    def verify_start_a_repair_order_link_show_up(self):
        self.driver.scroll_element("start_a_repair_order_link")
        return self.driver.wait_for_object("start_a_repair_order_link",raise_e=False)

    def verify_get_more_help_on_our_website_link(self):
        self.driver.scroll_element("get_more_help_on_our_website_link")
        return self.driver.wait_for_object("get_more_help_on_our_website_link",raise_e=False)

    def verify_campaign_ads_show_up(self):
        self.driver.scroll_element("campaign_ads_pc_devices_page")
        return self.driver.wait_for_object("campaign_ads_pc_devices_page", raise_e=False)
          
    def verify_general_specifications_title_show(self,raise_e=False, timeout=15):
        self.driver.scroll_element("general_specifications_title")
        return self.driver.wait_for_object("general_specifications_title", raise_e=raise_e, timeout=timeout)

    def verify_more_information_panel(self, timeout=15):
        self.driver.scroll_element("operating_system")
        elements = [
            "operating_system",
            "microprocessor",
            "system_memory",
            "memory_slot1",
            "system_board",
            "system_bios"
        ]
        for element in elements:
            self.driver.wait_for_object(element, timeout=timeout)
        return True

    def verify_contact_us_button_show_up(self,raise_e=False,timeout=15):
        self.driver.scroll_element("contact_us_button")
        return self.driver.wait_for_object("contact_us_button", raise_e=raise_e,timeout=timeout)

    def verify_contact_us_panel(self):
        self.driver.wait_for_object("chat_with_an_agent")
        self.driver.wait_for_object("call_an_agent")
        self.driver.wait_for_object("ask_the_hp_community")
        return True

    def verify_trouble_shoot_fix(self):
        self.driver.scroll_element("troubleshooting_fixes_section")
        return self.driver.wait_for_object("troubleshooting_fixes_section", raise_e=False)

    def verify_trouble_shoot_panel(self,timeout=15,raise_e=False):
        elements=["optimize_performance_link","check_for_audio_issues_link","run_system_tests_link","run_hardware_tests_link"]
        for element in elements:
            self.driver.scroll_element(element)
            self.driver.wait_for_object(element, timeout=timeout,raise_e=raise_e)
        return True
    
    def verify_campaign_ads_contextual_card_show_up(self, raise_e=False):
        return self.driver.wait_for_object("campaign_ads_contextual_card", raise_e=raise_e, timeout=10)

# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************

    def click_audio_card(self):
        return self.driver.click("audio_card", timeout = 15)
 
    def click_hppk_card(self):
        return self.driver.click("hppk_card", timeout = 20)
    
    def click_display_control_lone_page(self):
        self.driver.click("display_control_card_lone_page", timeout=15)
    
    def click_touchpad_card(self):
        return self.driver.click("touchpad_card", timeout = 10)

    def click_wellbeing_card(self):
        time.sleep(5)
        el = self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        time.sleep(2)
        el.send_keys(Keys.ENTER)

    def click_battery_manager_card_lone(self):
        self.driver.click("battery_manager_card_lone", timeout=15)
    
    def click_gesture_card(self):
        time.sleep(5)
        el = self.driver.wait_for_object("gesture_card", raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        time.sleep(2)
        el.send_keys(Keys.ENTER)
    
    def click_system_control_card_lone_page(self):
        self.driver.click("system_control_card_lone_page", timeout = 10)
    
    def click_presence_sensing_card_lone_page(self):
        self.driver.click("presence_sensing_card_lone_page")

    def click_presence_detection_card_lone_page(self, element):
        time.sleep(5)
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        time.sleep(2)
        el.send_keys(Keys.ENTER)

    def click_back_devices_button(self):
        self.driver.click("back_devices_button_on_pc_devices_page", timeout = 30)

    def click_audio_control_card(self):
        self.driver.click("audio_control_card_lone_page", timeout = 10)

    def click_energy_consumption_card(self):
        self.driver.click("energy_consumption_card_lone_page", timeout = 10)

    def click_video_card_lone_page(self):
        self.driver.click("video_card_lone_page", timeout=15)

    def click_hp_go_card(self):
        self.driver.click("hp_go_card")

    def click_to_copy_product_number_lone_page(self):
        self.driver.click("copy_product_number_lone_page", timeout = 15)

    def click_to_copy_serial_number_lone_page(self):
        self.driver.click("copy_serial_number_lone_page", timeout = 15)   

    def click_return_button_on_top_left_corner(self):
        self.driver.click("return_button_on_top_left_corner", timeout = 15)

    def swipe_to_touchpad_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to touchpad card
        for i in range(5):
            element = self.driver.wait_for_object("touchpad_card", raise_e=False, timeout = 5)
            if element:
                #swipe down one more distance in case the card is not fully displayed.
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("touchpad_card", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find touchpad card after swiping down 5 times")
    
    def swipe_to_presence_sensing_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to presence sensing card
        for i in range(5):
            element = self.driver.wait_for_object("presence_sensing_card_lone_page", raise_e=False, timeout = 5)
            if element:
                #swipe down one more distance in case the card is not fully displayed.
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("presence_sensing_card_lone_page", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find presence sensing card after swiping down 5 times")

    def swipe_to_gesture_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to gesture card
        for i in range(5):
            element = self.driver.wait_for_object("gesture_card", raise_e=False, timeout = 5)
            if element:
                #swipe down one more distance in case the card is not fully displayed.
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("gesture_card", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find gesture card after swiping down 5 times")

    def swipe_to_system_control_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to system control card
        for i in range(5):
            element = self.driver.wait_for_object("system_control_card_lone_page", raise_e=False, timeout = 5)
            if element:
                #swipe down one more distance in case the card is not fully displayed.
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("system_control_card_lone_page", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find system control card after swiping down 5 times")

    def swipe_to_wellbeing_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to wellbeing card
        for i in range(5):
            element = self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout = 5)
            if element:
                #swipe down one more distance in case the card is not fully displayed.
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find wellbeing card after swiping down 5 times")

    def swipe_to_audio_control_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to audio control card
        for i in range(5):
            element = self.driver.wait_for_object("audio_control_card_lone_page", raise_e=False, timeout = 5)
            if element:
                #swipe down one more distance in case the card is not fully displayed.
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("audio_control_card_lone_page", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find audio control card after swiping down 5 times")
    
    def swipe_to_hppk_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to hppk card
        self.driver.scroll_element("hppk_card", direction="down", distance=2, time_out=20)
        #swipe down one more distance in case the card is not fully displayed.
        self.driver.swipe(direction="down", distance=1)
        return self.driver.wait_for_object("hppk_card", raise_e=False, timeout = 5)

    def verify_devices_name(self):
        return self.driver.wait_for_object("devices_name", raise_e=False, timeout = 5) 
    

    def verify_system_module_name(self):
        return self.driver.get_attribute("device_system_module_name", "Name", timeout=15)

    def verify_device_details_device_name(self):
        return self.driver.get_attribute("device_details_device_name", "Name")
            
    def swipe_to_presence_detection_card(self):
        #swipe to top
        self.driver.swipe(direction="up", distance=10)
        #swipe down to presence detection card
        self.driver.scroll_element("presence_detection_card_lone_page", direction="down", distance=2, time_out=20)
        #swipe down one more distance in case the card is not fully displayed.
        self.driver.swipe(direction="down", distance=1)
        return self.driver.wait_for_object("presence_detection_card_lone_page", raise_e=False, timeout = 5) 
    
    def click_task_group_card_lone_page(self):
        self.driver.click("task_group_lone_page", timeout = 10)
    
    def click_smart_displays_lone_page(self):
        self.driver.click("smart_displays_lone_page", timeout = 10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_audio_control_card_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("audio_control_card_lone_page", raise_e=False, timeout = 10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"])
    def verify_product_number_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("product_number", raise_e=False, timeout=10) is not False

    @screenshot_compare(include_param=["machine_name", "page_number", "color"])
    def verify_audio_control_card_show_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object("audio_control_card_lone_page", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"])
    def verify_product_number_show_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object("product_number", raise_e=False, timeout=10) is not False
    
    @screenshot_compare(include_param=["mode"])
    def verify_audio_control_card_show_mode(self, mode):
        return self.driver.wait_for_object("audio_control_card_lone_page", raise_e = False, timeout = 10)

    @screenshot_compare(include_param=["mode"])
    def verify_product_number_show_mode(self, mode):
        return self.driver.wait_for_object("product_number", raise_e = False, timeout = 10)

    def click_optimize_performance_button(self):
        self.driver.scroll_element("optimize_performance_button")
        return self.driver.click("optimize_performance_button",change_check={"wait_obj": "optimize_performance_clicked"})

    def click_check_for_audio_issues_button(self):
        self.driver.scroll_element("check_for_audio_issues_button")
        return self.driver.click("check_for_audio_issues_button",change_check={"wait_obj": "check_for_audio_issues_clicked"})

    def click_run_system_tests_button(self):
        self.driver.scroll_element("run_system_tests_button")
        return self.driver.click("run_system_tests_button", change_check={"wait_obj": "run_system_tests_clicked"})

    def click_run_hardware_tests_button(self):
        self.driver.scroll_element("run_hardware_tests_button")
        return self.driver.click("run_hardware_tests_button", change_check={"wait_obj": "run_hardware_tests_clicked"})

    def close_optimize_performance_popup(self):
        tasklist = self.driver.ssh.send_command("tasklist.exe")
        if "HPPerformanceTuneup" in tasklist["stdout"]:
            self.driver.ssh.send_command("taskkill /F /IM HPPerformanceTuneup.exe")

    def close_check_for_audio_issues_popup(self):
        tasklist = self.driver.ssh.send_command("tasklist.exe")
        if "HPAudioCheck.exe" in tasklist["stdout"]:
            self.driver.ssh.send_command("taskkill /F /IM HPAudioCheck.exe")

    def close_run_system_tests_popup(self):
        tasklist = self.driver.ssh.send_command("tasklist.exe")
        if "HPOSCheck.exe" in tasklist["stdout"]:
            self.driver.ssh.send_command("taskkill /F /IM HPOSCheck.exe")

    def close_run_hardware_tests_popup(self):
        tasklist = self.driver.ssh.send_command("tasklist.exe")
        if "chrome.exe" in tasklist["stdout"] and self.driver.wait_for_object("run_hardware_tests_clicked", raise_e=False) is not False:
            self.driver.ssh.send_command('powershell taskkill /f /im chrome.exe', raise_e=False)

    def click_more_information_button(self):
        self.driver.scroll_element("more_information")
        self.driver.click("more_information")

    def click_contact_us_button(self):
        self.driver.scroll_element("contact_us_button")
        self.driver.click("contact_us_button")

    def click_start_virtual_assistant_button(self):
        self.driver.scroll_element("start_virtual_assistant_button")
        self.driver.click("start_virtual_assistant_button")

    def validate_display_control_lone_page(self):
        return self.driver.wait_for_object("display_control_card_lone_page", raise_e=False, timeout=10) is not False
    
    def swipe_to_wellbeing_card_with_large_text_size(self):
        self.driver.swipe(direction="up", distance=10)
        for i in range(10):
            element = self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout = 5)
            if element:
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find wellbeing card after swiping down 10 times")


    def swipe_to_gesture_card_with_large_text_size(self):
        self.driver.swipe(direction="up", distance=10)
        for i in range(10):
            element = self.driver.wait_for_object("gesture_card", raise_e=False, timeout = 5)
            if element:
                self.driver.swipe(direction="down", distance=1)
                return self.driver.wait_for_object("gesture_card", raise_e=False, timeout = 5)
            self.driver.swipe(direction="down", distance=2)
        raise Exception("Unable to find gesture card after swiping down 10 times")
    
    def get_pc_device_production_number(self):
        return self.driver.get_attribute("copy_product_number", "Name", timeout=15)

    def get_pc_device_serial_number(self):
        return self.driver.get_attribute("copy_serial_number", "Name", timeout=15)

    def verify_smart_displays_commercial_lone_page(self):
        return self.driver.wait_for_object("smart_displays_commercial_lone_page",raise_e=False, timeout = 10)
    
    def click_smart_displays_commercial_lone_page(self):
        self.driver.click("smart_displays_commercial_lone_page", timeout = 10)

    def click_campaign_ads_contextual_card_show_up(self):
        self.driver.click("campaign_ads_contextual_card", timeout=10)
        
    def click_on_shop_now_ads_button(self):
        self.driver.click("show_now_btn")