from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import re
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Bopeep(object):
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
    
    #this suite should run on bopeep
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_verify_display_mode_ui_C34324866(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_natural_mode_title(), "Neutral", "Neutral mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_game_mode_title(), "Gaming", "Gaming mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_reading_mode_title(), "Reading", "Reading mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_night_mode_title(), "Night", "Night mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_movie_mode_title(), "Movie", "Movie mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_enhanceplus_mode_title(), "HP Enhance+", "HP Enhanc mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_native_tile(), "Native", "HP Enhanc mode is not found")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_display_modes_title(), "Display modes", "Display mode title is not found")
        soft_assertion.raise_assertion_errors()


    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_advance_setting_ui_C34324867(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].click_advaced_setting()

        advanced_setting_title_text = self.fc.fd["display_control"].verify_advanced_settings_title()
        soft_assertion.assert_equal(advanced_setting_title_text,"Advanced Settings", "Advanced setting title text is not matching")
        low_blue_light_tool_tip_text = self.fc.fd["display_control"].verify_low_blue_light_toggle_text()
        soft_assertion.assert_equal(low_blue_light_tool_tip_text,"Low Blue Light reduces the emission of blue light from a display in order to reduce eye fatigue." , "Low blue light tooltip toggle text is not matching")

        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        toggle_state=self.fc.fd["display_control"].get_toggle_of_low_blue_light()
        if (toggle_state == '0'):
            self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_low_blue_light_toggle_is_present(),True , "Low blue light toggle is not visible")

        low_blue_light_text = self.fc.fd["display_control"].verify_low_blue_light_text()
        soft_assertion.assert_equal(low_blue_light_text,"Low blue light" , "Low blue light text is not matching")

        turn_off_text = self.fc.fd["display_control"].verify_turn_off_text()
        soft_assertion.assert_equal(turn_off_text,"Turn off", "Turn off text is not matching")
        turn_on_text = self.fc.fd["display_control"].verify_turn_on_text()
        soft_assertion.assert_equal(turn_on_text,"Turn on", "Turn on text is not matching")

        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present(),True , "trun on am/pm combobox is not visible")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present(),True , "trun off am/pm combobox is not visible")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present(),True , "turn on hour combobox is not visible")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present(),True , "turn off hour combobox is not visible")
        time.sleep(3)
        color_adjestments_text = self.fc.fd["display_control"].get_color_adjestments()
        soft_assertion.assert_equal(color_adjestments_text,"Color Adjustments", "Color Adjustments text is not matching")

        color_adjestments_tooltip_text = self.fc.fd["display_control"].verify_color_adjestments_tooltip_text()
        soft_assertion.assert_equal(color_adjestments_tooltip_text,"Fine tune your display panel by adjusting the red (R), green (G), and blue (B) color values.", "Color Adjustments text is not matching")

        red_slider_text = self.fc.fd["display_control"].verify_red_slider()
        soft_assertion.assert_equal(red_slider_text,"Red", "Red slider is not visible")

        green_slider_text = self.fc.fd["display_control"].verify_green_slider()
        soft_assertion.assert_equal(green_slider_text,"Green", "Green slider is not visible")

        blue_slider_text = self.fc.fd["display_control"].verify_blue_slider()
        soft_assertion.assert_equal(blue_slider_text,"Blue", "Blue slider is not visible")
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_03_verify_lbl_toggle_status_C34324906(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()        
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        self.fc.fd["display_control"].click_advaced_setting()

        toggle_state = self.fc.fd["display_control"].get_toggle_of_low_blue_light()
        if (toggle_state == '0'):
            soft_assertion.assert_equal(toggle_state,'0' , "Low blue light toggle is turned off")
            self.fc.fd["display_control"].click_low_blue_light_toggle_on()
            toggle_state = self.fc.fd["display_control"].get_toggle_of_low_blue_light()
            soft_assertion.assert_equal(toggle_state,'1' , "Low blue light toggle is turned on")
            soft_assertion.raise_assertion_errors()
        else:
            soft_assertion.assert_equal(toggle_state,'1' , "Low blue light toggle is turned on")
            self.fc.fd["display_control"].click_low_blue_light_toggle_on()
            toggle_state = self.fc.fd["display_control"].get_toggle_of_low_blue_light()
            soft_assertion.assert_equal(toggle_state,'0' , "Low blue light toggle is turned off")
            soft_assertion.raise_assertion_errors()
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()

    
    def test_04_verify_brightness_contrast_ui_C34324865(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_brightness_contrast_label(), "Brightness & Contrast", "Brightness & Contrast label is not present or visible")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_brightness_slider_is_present(), True, "Brightness slider is not present or visible")
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_contrast_slider_is_present(), True, "Contrast slider is not present or visible")
        soft_assertion.raise_assertion_errors()

    
    def test_05_verify_dafault_value_advance_setting_C34324869(self):
        self.fc.restart_myHP()
        time.sleep(10)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not present"
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        self.fc.fd["display_control"].verify_advaced_setting_visible()
        self.fc.fd["display_control"].click_advaced_setting()

        toggle_state = self.fc.fd["display_control"].get_toggle_of_low_blue_light()
        if (toggle_state == '0'):
            self.fc.fd["display_control"].click_low_blue_light_toggle_on()

        self.fc.fd["display_control"].click_turn_on_advanced_settings_dropdown()
        
        turn_on_pm_text = self.fc.fd["display_control"].verify_turn_on_default_pm_time()
        soft_assertion.assert_equal(turn_on_pm_text,"pm", "pm text is not matching")

        actual_turn_off_am_text = self.fc.fd["display_control"].verify_turn_off_default_am_time()
        soft_assertion.assert_equal(actual_turn_off_am_text,"am","Turn off am text is not matching")
        
        turn_on_time=self.fc.fd["display_control"].verify_on_hour_time()
        actual_turn_on_time=re.search("([0-9]{1,2}:[0-9]{1,2})",str(turn_on_time))
        turn_on_time1=actual_turn_on_time.group(1)
        assert  "10:00" in  turn_on_time1,"Time is not present"
        turn_off_time=self.fc.fd["display_control"].verify_off_hour_time()
        actual_turn_off_time=re.search("([0-9]{1,2}:[0-9]{1,2})",str(turn_off_time))
        turn_off_time1=actual_turn_off_time.group(1)
        assert  "7:00" in turn_off_time1,"Time is not present"
        red_slider_value = self.fc.fd["display_control"].verify_red_slider_value()
        soft_assertion.assert_equal(red_slider_value,"100","red slider value is not matching")
        green_slider_value = self.fc.fd["display_control"].verify_green_slider_value()
        soft_assertion.assert_equal(green_slider_value,"100","green slider value is not matching")
        blue_slider_value = self.fc.fd["display_control"].verify_blue_slider_value()
        soft_assertion.assert_equal(blue_slider_value,"100","blue slider value is not matching")
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_06_verify_low_blue_light_scheduler_default_value_C35370271(self):
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(8)
        self.fc.fd["devices"].click_display_control()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        self.fc.fd["display_control"].click_advaced_setting()
        advance_settings_title_text = self.fc.fd["display_control"].verify_advanced_settings_title()
        assert advance_settings_title_text=="Advanced Settings","Advance Setting text is not visible at display control page - {}".format(advance_settings_title_text)    
        #this is to click on tooltip
        self.fc.fd["display_control"].hover_on_advanced_settings_lbl_tooltip_icon()
        low_blue_light_tooltip_text = self.fc.fd["display_control"].verify_advanced_settings_lbl_tooltip_icon()
        assert "Low Blue Light reduces" in low_blue_light_tooltip_text,"Tooltip text is not visible - {}".format(low_blue_light_tooltip_text)
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light_status() == True,"Toggle is not present or visible"
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
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        self.fc.fd["display_control"].click_advaced_setting()
        
    @pytest.mark.ota
    def test_07_verify_low_blue_light_scheduler_enable_toggle_value_C34324907(self):
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        self.fc.fd["display_control"].click_advaced_setting()
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
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        self.fc.fd["display_control"].click_advaced_setting()

    @pytest.mark.ota
    def test_08_verify_low_blue_light_scheduler_disable_toggle_value_C34324908(self):
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        self.fc.fd["display_control"].click_advaced_setting(),
        if self.fc.fd["display_control"].toggle_notification_state()=="1":
            self.fc.fd["display_control"].click_schedule_toggle_turn_off()
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
        self.fc.fd["display_control"].click_advaced_setting()
        self.fc.fd["display_control"].click_restore_default_button()
        self.fc.fd["display_control"].click_advaced_setting()
        assert self.fc.fd["display_control"].toggle_notification_state()=="0","Toggle is not off"
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        self.fc.close_app()

    @pytest.mark.ota
    def test_09_verify_error_message_on_same_time_C34324913(self):
        self.fc.launch_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["display_control"].click_restore_default_button()
        time.sleep(5)
        self.fc.fd["display_control"].click_advaced_setting()
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        self.fc.fd["display_control"].select_dropdown_on_item()#--7:00
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        time.sleep(2)
        self.fc.fd["display_control"].select_am_on_am_pm_turn_on_drop_down()
        time.sleep(1)
        assert self.fc.fd["display_control"].get_advance_setting_error_message()=="Time cannot be same","Error message did not show"
        soft_assertion.assert_equal(self.fc.fd["display_control"].get_advance_setting_error_message(), "Time cannot be same", "Error message did not show")
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        self.fc.fd["display_control"].select_dropdown_on_item_default()
        time.sleep(2)
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        time.sleep(2)
        self.fc.fd["display_control"].select_pm_on_am_pm_turn_on_drop_down()
        time.sleep(3)
        self.fc.fd["display_control"].click_schedule_toggle_turn_on()

    
    def test_10_verify_display_modes_default_brightness_slider_value_C34324868(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        # make sure diplay control setting is default
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "76","natural mode brightness is not 76")
 
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "84","Gaming mode brightness is not 84")

        self.fc.fd["display_control"].click_reading_mode()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "52","reading mode brightness is not 52")

        self.fc.fd["display_control"].click_night_mode()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "28","night mode brightness is not 28")

        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "20","movie mode brightness is not 20")

        self.fc.fd["display_control"].click_enhanceplus_mode()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "76","nhanceplus mode brightness is not 76")

        self.fc.fd["display_control"].click_native_tile()
        time.sleep(15)
        app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        soft_assertion.assert_equal(app_brightness_value, "100","native mode brightness is not 100")
        soft_assertion.raise_assertion_errors()