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
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restore_default_button_for_night_mode_C34324919(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
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
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button default is on"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button is not on"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not visible"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "default Turn on time drop down is not 10:00"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not visible"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not visible"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "default Turn on time state is not pm"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not visible"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not visible"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "default Turn off time drop down is not 7:00"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not visible"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not visible"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "default Turn off time state is not am"    
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not visible"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not off"
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
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not visible"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not visible"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not visible"
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
    def test_02_restore_default_button_for_movie_mode_C34324920(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
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
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button default is on"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button is not on"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not visible"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "default Turn on time drop down is not 10:00"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not visible"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not visible"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "default Turn on time state is not pm"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not visible"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not visible"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "default Turn off time drop down is not 7:00"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not visible"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not visible"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "default Turn off time state is not am"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not visible"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not off"
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
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not visible"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not visible"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not visible"
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
    def test_03_restore_default_button_for_HP_Enhance_mode_C34324921(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
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
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify hp enhance+ image mode show
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "HP Enhance+ mode is not selected"
        time.sleep(1)
        # click hp enhance+ image mode
        self.fc.fd["display_control"].click_enhanceplus_mode()
        time.sleep(1)
        # verifyhp enhance+ image mode is selected
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "HP Enhance+ mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button default is on"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button is not on"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not visible"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "default Turn on time drop down is not 10:00"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not visible"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not visible"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "default Turn on time state is not pm"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not visible"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not visible"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "default Turn off time drop down is not 7:00"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not visible"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not visible"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "default Turn off time state is not am"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not visible"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not off"
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
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_restore_default_button_for_native_mode_C34324922(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
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
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify native image mode show
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        # click native image mode
        self.fc.fd["display_control"].click_native_tile()
        time.sleep(1)
        # verify native image mode is selected
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get default low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button default is on"
        time.sleep(1)
        # click low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button is not on"
        time.sleep(1)
        # verify turn on time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_on_hr_combobox_is_present()) is True, "Turn on time drop down is not visible"
        time.sleep(1)
        # get default time from Turn-on is (ex-10) show
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "default Turn on time drop down is not 10:00"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not visible"
        time.sleep(1)
        # click turn on time drop down list
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not visible"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "default Turn on time state is not pm"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not visible"
        time.sleep(1)
        # click turn on time state pm list
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        time.sleep(3)
        # select random time state from Turn-on (ex-am)
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        time.sleep(2)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not visible"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "default Turn off time drop down is not 7:00"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not visible"
        time.sleep(1)
        # click turn off time drop down list
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-off (ex-6)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list()
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not visible"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "default Turn off time state is not am"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not visible"
        time.sleep(1)
        # click turn off time state am list
        self.fc.fd["display_control"].click_turn_off_time_state_list()
        time.sleep(1)
        # select random time state from Turn-off (ex-pm)
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        time.sleep(3)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not visible"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get low blue light button status is off
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not off"
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
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not visible"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not visible"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not visible"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)