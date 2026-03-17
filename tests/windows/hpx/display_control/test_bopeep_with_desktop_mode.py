from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control_With_Bopeep(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
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
    def test_01_brightness_slider_tooltips_C36043633(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(8)
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        self.fc.fd["display_control"].set_slider_value_increase(100, "Brightness_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "Brightness slider value is not 100"
        time.sleep(2)
        self.sf.click_windows_battery_icon()
        time.sleep(2)
        assert self.sf.get_windows_brightness_value() == "100", "Brightness value is not 100"
        time.sleep(2)
        self.sf.click_windows_battery_icon()
    
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_contrast_slider_tooltips_C36043658(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        
        time.sleep(8)
        self.fc.fd["display_control"].set_slider_value_decrease(100, "Contrast_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "0", "Contrast slider value is not 0"
    

    def test_03_brightness_slider_position_C36043698(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        
        time.sleep(8)
        self.fc.fd["display_control"].set_slider_value_decrease(100, "Brightness_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "0", "Brightness slider value is not 0"
    

    def test_04_contrast_slider_position_C36043743(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        
        time.sleep(8)
        self.fc.fd["display_control"].set_slider_value_increase(100, "Contrast_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "Contrast slider value is not 100"

    @pytest.mark.ota
    def test_05_restore_dault_C38791570(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # verify string of restore defaults show
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_title() == "Restore defaults", "Restore defaults title is not show"
        time.sleep(1)
        # verify string of restore the settings to the hp factory defaults show
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_subtitle() == "Restore the settings to the HP factory defaults?", "Restore the settings to the HP factory defaults is not show"
        time.sleep(1)
        # verify "do not show again" checkbox show
        assert bool(self.fc.fd["display_control"].get_restore_pop_up_windows_do_not_show_again_checkbox()) is True, "Do not show again checkbox is not show"
        time.sleep(1)
        # verify string of "do not show again" show
        assert self.fc.fd["display_control"].get_restore_pop_up_windows_do_not_show_text() == "Do not show again", "Do not show again is not show"
        time.sleep(1)
        # verify "cancel" button show
        assert bool(self.fc.fd["display_control"].get_restore_pop_up_windows_cancel_text()) is True, "Cancel button is not show"
        time.sleep(1)
        # verify "continue" button show
        assert bool(self.fc.fd["display_control"].get_restore_pop_up_windows_continue_text()) is True, "Continue button is not show"
        time.sleep(1)
        # click "cancel" button
        self.fc.fd["display_control"].click_restore_pop_up_windows_cancel_button()
        time.sleep(1)
        # verify restore defaults diaolog disappear
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) is False, "Restore defaults dialog is shown"
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "do not show again" checkbox
        self.fc.fd["display_control"].click_restore_pop_up_do_not_show_checkbox()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(1)
        # verify restore defaults diaolog disappear
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) is False, "Restore defaults dialog is shown"
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # verify restore defaults diaolog disappear
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) is False, "Restore defaults dialog is shown"
        time.sleep(1)

    @pytest.mark.ota
    @pytest.mark.consumer
    @pytest.mark.function
    def test_06_restore_default_button_for_neutral_C34324916(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.restart_myHP()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify neutral image mode show
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # click neutral image mode
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(1)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is not show"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not show"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not show"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not show"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not show"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not show"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not show"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not show"
        time.sleep(1)
         # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not show"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not show"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 97
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "Red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # decrease 2 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(2,"green_slider")
        time.sleep(1)
        # get green color slider value is 97
        assert self.fc.fd["display_control"].verify_green_slider_value() == "98", "Green color slider value is not 98"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # decrease 3 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(3,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 97
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "97", "Blue color slider value is not 97"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is not show"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_restore_default_button_for_gaming_C34324917(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify gaming image mode show
        assert bool(self.fc.fd["display_control"].verify_game_mode_title()) is True, "Gaming image mode is not show"
        time.sleep(1)
        # click gaming image mode
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(1)
        # verify gaming image mode is selected
        assert bool(self.fc.fd["display_control"].get_game_mode()) is True, "Gaming image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advance Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is not show"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not show"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not show"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not show"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not show"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not show"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not show"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not show"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not show"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not show"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 97
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "Red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # decrease 2 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(2,"green_slider")
        time.sleep(1)
        # get green color slider value is 97
        assert self.fc.fd["display_control"].verify_green_slider_value() == "98", "Green color slider value is not 98"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # decrease 3 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(3,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 97
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "97", "Blue color slider value is not 97"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is not show"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True,  "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # verify turn on time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_drop_down_is_grey()) is True, "Turn on time drop down is not grey"
        time.sleep(1)
        # verify turn on time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_state_is_grey()) is True, "Turn on time state is not grey"
        time.sleep(1)
        # verify turn off time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_drop_down_is_grey()) is True, "Turn off time drop down is not grey"
        time.sleep(1)
        # verify turn off time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_state_is_grey()) is True, "Turn off time state is not grey"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_restore_default_button_for_reading_C34324918(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify reading image mode show
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "Reading image mode is not show"
        time.sleep(1)
        # click reading image mode
        self.fc.fd["display_control"].click_reading_mode()
        time.sleep(1)
        # verify reading image mode is selected
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "Reading image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is not show"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not show"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not show"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not show"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not show"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not show"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not show"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not show"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not show"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not show"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 97
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "Red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # decrease 2 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(2,"green_slider")
        time.sleep(1)
        # get green color slider value is 97
        assert self.fc.fd["display_control"].verify_green_slider_value() == "98", "Green color slider value is not 98"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # decrease 3 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(3,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 97
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "97", "Blue color slider value is not 97"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is not show"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # verify turn on time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_drop_down_is_grey()) is True, "Turn on time drop down is not grey"
        time.sleep(1)
        # verify turn on time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_state_is_grey()) is True, "Turn on time state is not grey"
        time.sleep(1)
        # verify turn off time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_drop_down_is_grey()) is True, "Turn off time drop down is not grey"
        time.sleep(1)
        # verify turn off time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_state_is_grey()) is True, "Turn off time state is not grey"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)