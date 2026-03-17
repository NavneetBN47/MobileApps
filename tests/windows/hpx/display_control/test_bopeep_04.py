from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import re
import time

pytest.app_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Bopeep(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
        time.sleep(5)
    
    #this suite should run bopeep
    @pytest.mark.consumer
    @pytest.mark.function
    def test_01_relaunch_advanced_setting_page_C34324936(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
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
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # turn off low blue light button
        self.fc.fd["display_control"].click_low_blue_light_toggle_off()
        time.sleep(1)
        # get low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # verify turn on time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_drop_down_is_grey()) is True, "Turn on time drop down is not grey"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_state_is_grey()) is True, "Turn on time state is not grey"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_drop_down_is_grey()) is True, "Turn off time drop down is not grey"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_state_is_grey()) is True, "Turn off time state is not grey"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 98
        assert self.fc.fd["display_control"].verify_red_slider_value() == "98", "The red color slider value is not 98"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 98
        assert self.fc.fd["display_control"].verify_green_slider_value() == "98", "The green color slider value is not 98"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 98
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "98", "The blue color slider value is not 98"
        time.sleep(3)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 0
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button status is not 0"
        time.sleep(1)
        # verify turn on time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_drop_down_is_grey()) is True, "Turn on time drop down is not grey"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_on_time_state_is_grey()) is True, "Turn on time state is not grey"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_drop_down_is_grey()) is True, "Turn off time drop down is not grey"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state is grey
        assert bool(self.fc.fd["display_control"].get_trun_off_time_state_is_grey()) is True, "Turn off time state is not grey"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 98
        assert self.fc.fd["display_control"].verify_red_slider_value() == "98", "The red color slider value is not 98"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 98
        assert self.fc.fd["display_control"].verify_green_slider_value() == "98", "The green color slider value is not 98"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 98
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "98", "The blue color slider value is not 98"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_02_relaunch_advanced_setting_page_for_neutral_modes_C34324937(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # select neutral image mode
        # verify neutral image mode show
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # click neutral image mode
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(1)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76", "The default brightness slider value is not 76"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_increase(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 86
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "86", "The brightness slider value is not 86"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # Select any other modes,Ex-Movie
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(3)
        # Navigate back to Neutral mode
        # verify neutral image mode show
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # click neutral image mode
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(1)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 86
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "86", "The brightness slider value is not 86"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_03_relaunch_advanced_setting_page_for_gaming_modes_C34324938(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select Gaming mode
        # verify gaming image mode show
        assert bool(self.fc.fd["display_control"].verify_game_mode_title()) is True, "The gaming image mode is not show"
        time.sleep(1)
        # click gaming image mode
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(1)
        # verify gaming image mode is selected
        assert bool(self.fc.fd["display_control"].get_game_mode()) is True, "The gaming image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "84", "The default brightness slider value is not 84"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_increase(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 100
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "94", "The brightness slider value is not 94"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # Select any other modes,Ex-Movie
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(3)
        # Navigate back to gaming mode
        # verify gaming image mode show
        assert bool(self.fc.fd["display_control"].verify_game_mode_title()) is True, "The gaming image mode is not show"
        time.sleep(1)
        # click gaming image mode
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(1)
        # verify gaming image mode is selected
        assert bool(self.fc.fd["display_control"].get_game_mode()) is True, "The gaming image mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 94
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "94", "The brightness slider value is not 94"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_04_relaunch_advanced_setting_page_for_reading_modes_C34324939(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select reading mode
        # verify reading image mode show
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "Reading image mode is not show"
        time.sleep(1)
        # click reading image mode
        self.fc.fd["display_control"].click_reading_mode()
        time.sleep(1)
        # verify reading image mode is selected
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "Reading image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "52", "The default brightness slider value is not 52"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_increase(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 62
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "62", "The brightness slider value is not 100"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # Select any other modes,Ex-Movie
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(3)
        # Navigate back to reading mode
        # verify reading image mode show
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "Reading image mode is not show"
        time.sleep(1)
        # click reading image mode
        self.fc.fd["display_control"].click_reading_mode()
        time.sleep(1)
        # verify reading image mode is selected
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "Reading image mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 62
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "62", "The brightness slider value is not 62"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_05_relaunch_advanced_setting_page_for_night_modes_C34324940(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select night mode
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "28", "The default brightness slider value is not 28"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_increase(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 38
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "38", "The brightness slider value is not 38"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # Select any other modes,Ex-Movie
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(3)
        # Navigate back to night mode
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 38
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "38", "The brightness slider value is not 38"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_06_relaunch_advanced_setting_page_for_movie_modes_C34324941(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select movie mode
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "20", "The default brightness slider value is not 20"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_increase(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "30", "The brightness slider value is not 30"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # Select any other modes,Ex-night
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(3)
        # Navigate back to movie mode
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "30", "The brightness slider value is not 30"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_07_relaunch_advanced_setting_page_for_hp_enhance_modes_C34324942(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select hp enhance  mode
        # verify hp enhance+ image mode show
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not show"
        time.sleep(1)
        # click hp enhance+ image mode
        self.fc.fd["display_control"].click_enhanceplus_mode()
        time.sleep(1)
        # verify hp enhance+ image mode is selected
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76", "The default brightness slider value is not 76"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_increase(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "86", "The brightness slider value is not 86"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # Select any other modes,Ex-night
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(3)
        # Navigate back to hp enhance mode
        # verify hp enhance+ image mode show
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not show"
        time.sleep(1)
        # click hp enhance+ image mode
        self.fc.fd["display_control"].click_enhanceplus_mode()
        time.sleep(1)
        # verify hp enhance+ image mode is selected
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "86", "The brightness slider value is not 86"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_08_relaunch_advanced_setting_page_for_native_modes_C34324943(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select native mode
        # verify native image mode show
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        # click native image mode
        self.fc.fd["display_control"].click_native_tile()
        time.sleep(1)
        # verify native image mode is selected
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "The default brightness slider value is not 100"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "The brightness slider value is not 90"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # Select any other modes,Ex-night
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "Night mode is not selected"
        time.sleep(3)
        # Navigate back to native mode
        # verify native image mode show
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        # click native image mode
        self.fc.fd["display_control"].click_native_tile()
        time.sleep(1)
        # verify native image mode is selected
        assert bool(self.fc.fd["display_control"].verify_native_tile()) is True, "Native image mode is not selected"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Native image mode is not selected"
        time.sleep(10)
        # Check previous changes
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "90", "The brightness slider value is not 90"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_09_relaunch_neutral_modes_C34324944(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select neutral mode
        # verify neutral image mode show
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not show"
        time.sleep(1)
        # click neutral image mode
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(1)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76", "The default brightness slider value is not 76"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "66", "The brightness slider value is not 66"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # Check previous changes
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "66", "The brightness slider value is not 66"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_10_relaunch_gaming_modes_C34324945(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(5)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
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
        # Select gaming mode
        # verify gaming image mode show
        assert bool(self.fc.fd["display_control"].verify_game_mode_title()) is True, "Gaming image mode is not show"
        time.sleep(1)
        # click gaming image mode
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(1)
        # verify gaming image mode is selected
        assert bool(self.fc.fd["display_control"].get_game_mode()) is True, "Gaming image mode is not selected"
        time.sleep(1)
        # Drag Brightness & Contrast slider to random value
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "84", "The default brightness slider value is not 84"
        time.sleep(1)
        # drag brightness slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "74", "The brightness slider value is not 74"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to random value
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # Navigate to Advance settings
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # Turn On Scheduler Toggle and Select random time
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on10:00Hour", "Turn on time drop down is not 10:00"
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
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm show
        assert bool(self.fc.fd["display_control"].verify_trun_on_am_pm_combobox_is_present()) is True, "Turn on time state is not show"
        time.sleep(1)
        # get default time state from Turn-on is (ex-pm) show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "pm", "Turn on time state is not pm"
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
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down show
        assert bool(self.fc.fd["display_control"].verify_trun_off_hr_combobox_is_present()) is True, "Turn off time drop down is not show"
        time.sleep(1)
        # verify default time from Turn-off is (ex-7) show
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off7:00Hour", "Turn off time drop down is not 7:00"
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
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am show
        assert bool(self.fc.fd["display_control"].verify_trun_off_am_pm_combobox_is_present()) is True, "Turn off time state is not show"
        time.sleep(1)
        # get default time state from Turn-off is (ex-am) show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "am", "Turn off time state is not am"
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
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # Drag Color Adjustment slider to random values
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
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
        # close application and Relaunch
        self.fc.restart_app()
        time.sleep(3)
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # Check previous changes
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Neutral image mode is not selected"
        time.sleep(1)
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 30
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "74", "The brightness slider value is not 74"
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 90
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "90", "The contrast slider value is not 90"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # verify turn on time drop down list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_drop_down_list_show()) is True, "Turn on time drop down list is not show"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # verify turn on time state pm list show
        assert bool(self.fc.fd["display_control"].verify_turn_on_time_state_list_show()) is True, "Turn on time state list is not show"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # verify turn off time drop down list show
        assert bool(self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show()) is True, "Turn off time drop down list is not show"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # verify turn off time state am list show
        assert bool(self.fc.fd["display_control"].verify_turn_off_time_state_list_show()) is True, "Turn off time state list is not show"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)