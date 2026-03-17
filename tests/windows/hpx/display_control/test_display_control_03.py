import re
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
from SAF.misc import saf_misc
import pytest
import time
from datetime import datetime

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

soft_assertion = SoftAssert()

class Test_Suite_Display_Control_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    #This suite should run in willie and bopeep
    def test_01_advance_setting_icon_C32194977(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        self.fc.fd["devices"].click_display_control()
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_brightness_contrast_label()) is True, "Brightness and contrast label is not visible"
        self.fc.fd["display_control"].click_advaced_setting()
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
    
    def test_02_verify_low_blue_light_scheduler_strings_on_display_control_ui_C32194964(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        self.driver.swipe(direction="up", distance=3)
        advance_settings_for_lbl_scheduler_icon = self.fc.fd["display_control"].verify_advaced_setting_visible()
        assert advance_settings_for_lbl_scheduler_icon=="Advance Setting","Advance Setting is not visible at display control page - {}".format(advance_settings_for_lbl_scheduler_icon)
        self.fc.fd["display_control"].click_advaced_setting()
        advance_settings_title_text = self.fc.fd["display_control"].verify_advanced_settings_title()
        assert advance_settings_title_text=="Advanced Settings","Advance Setting text is not visible at display control page - {}".format(advance_settings_title_text)
        #this is to click on tooltip
        self.fc.fd["display_control"].click_low_blue_light_toggle()
        low_blue_light_tooltip_text = self.fc.fd["display_control"].verify_low_blue_light_toggle_text()
        assert "Low Blue Light reduces" in low_blue_light_tooltip_text,"Tooltip text is not visible - {}".format(low_blue_light_tooltip_text)
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light_status() == True,"Toggle is not present or visible"
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        assert self.fc.fd["display_control"].verify_turn_on_text() == "Turn on","Turn on text is not present"
        turn_on_time=self.fc.fd["display_control"].verify_on_hour_time()
        actual_turn_on_time=re.search("([0-9]{1,2}:[0-9]{1,2})",str(turn_on_time))
        turn_on_time1=actual_turn_on_time.group(1)
        assert  "10:00" in  turn_on_time1,"Time is not present"
        assert self.fc.fd["display_control"].get_turn_on_am_pm_advanced_settings() == "pm","pm is not present"
        assert self.fc.fd["display_control"].verify_turn_off_text() == "Turn off","Turn off text is not present"
        turn_off_time=self.fc.fd["display_control"].verify_off_hour_time()
        actual_turn_off_time=re.search("([0-9]{1,2}:[0-9]{1,2})",str(turn_off_time))
        turn_off_time1=actual_turn_off_time.group(1)
        assert  "7:00" in turn_off_time1,"Time is not present"
        assert self.fc.fd["display_control"].get_turn_off_am_pm_advanced_settings() == "am","pm is not present"
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_defaults_button()

    @pytest.mark.ota
    def test_03_lbl_error_message_C32194981(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        time.sleep(4)
        self.fc.fd["display_control"].click_advaced_setting()
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()#6:00
        time.sleep(3)
        #select am from am/pm dd
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        self.fc.fd["display_control"].select_turn_on_time_state_am()

        assert self.fc.fd["display_control"].get_item_turn_on_time_drop_down_list_show() == "6:00", "Time is not selected"
        
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()#6:00
        time.sleep(3)
        self.fc.fd["display_control"].click_turn_off_time_state_is_am()
        assert self.fc.fd["display_control"].get_item_turn_off_time_drop_down_list_show() == "6:00", "Time is not selected"

        assert self.fc.fd["display_control"].get_advance_setting_error_message()=="Time cannot be same","Error message did not show"
    
    @pytest.mark.ota
    def test_04_lbl_scheduler_toggler_button_off_message_C32319192(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].click_advaced_setting()
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()#6:00
        time.sleep(1)
        #select am from am/pm dd
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        self.fc.fd["display_control"].select_turn_on_time_state_am()

        assert self.fc.fd["display_control"].get_item_turn_on_time_drop_down_list_show() == "6:00", "Time is not selected"
        
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()#6:00
        time.sleep(1)
        self.fc.fd["display_control"].click_turn_off_combo_advanced_settings()
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        assert self.fc.fd["display_control"].get_item_turn_off_time_drop_down_list_show() == "6:00", "Time is not selected"

        assert self.fc.fd["display_control"].get_advance_setting_error_message()=="Time cannot be same","Error message did not show"

        self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        assert self.fc.fd["display_control"].toggle_notification_state()=="0","Scheduler is not off"
        assert self.fc.fd["display_control"].get_item_turn_off_time_drop_down_list_show() == "6:00", "Time is not selected"

    @pytest.mark.ota
    def test_05_verify_low_blue_light_scheduler_times_format_C32194979(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        self.fc.fd["devices"].click_display_control()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        self.driver.swipe(direction="up", distance=3)
        advance_settings_for_lbl_scheduler_icon = self.fc.fd["display_control"].verify_advaced_setting_visible()
        assert advance_settings_for_lbl_scheduler_icon=="Advance Setting","Advance Setting is not visible at display control page - {}".format(advance_settings_for_lbl_scheduler_icon)
        self.fc.fd["display_control"].click_advaced_setting()
        advance_settings_title_text = self.fc.fd["display_control"].verify_advanced_settings_title()
        assert advance_settings_title_text=="Advanced Settings","Advance Setting text is not visible at display control page - {}".format(advance_settings_title_text)
        #this is to click on tooltip
        self.fc.fd["display_control"].click_low_blue_light_toggle()
        low_blue_light_tooltip_text = self.fc.fd["display_control"].verify_low_blue_light_toggle_text()
        assert "Low Blue Light reduces" in low_blue_light_tooltip_text,"Tooltip text is not visible - {}".format(low_blue_light_tooltip_text)
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light_status() == True,"Toggle is not present or visible"
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        assert self.fc.fd["display_control"].verify_turn_on_text() == "Turn on","Turn on text is not present"
        turn_on_time=self.fc.fd["display_control"].verify_on_hour_time()
        actual_turn_on_time=re.search("([0-9]{1,2}:[0-9]{1,2})",str(turn_on_time))
        turn_on_time1=actual_turn_on_time.group(1)
        am_pm_time = self.fc.fd["display_control"].get_turn_on_am_pm_advanced_settings()
        time_format = f"{turn_on_time1} {am_pm_time}"
        assert self.is_12_hour_format(time_format) == True, "Turn on time is not in 12 hour format"
        turn_off_time=self.fc.fd["display_control"].verify_off_hour_time()
        actual_turn_off_time=re.search("([0-9]{1,2}:[0-9]{1,2})",str(turn_off_time))
        turn_off_time1=actual_turn_off_time.group(1)
        am_pm_time = self.fc.fd["display_control"].get_turn_off_am_pm_advanced_settings()
        time_format = f"{turn_off_time1} {am_pm_time}"
        assert self.is_12_hour_format(time_format) == True, "Turn off time is not in 12 hour format"

    def is_12_hour_format(self, time_str):
        try:
            datetime.strptime(time_str, "%I:%M %p")
            return True
        except ValueError:
            return False
            