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
    
    # this suite should run in bopeep
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_AIO_Bopeep_TC_Restore_Default_C34324915(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        self.fc.fd["devices"].click_display_control()
        time.sleep(2)
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        assert bool(self.fc.fd["display_control"].verify_brightness_contrast_label()) is True, "Brightness and contrast label is not visible"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True, "Brightness slider is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "100", "Brightness slider value is not 100"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_contrast_slider_is_present()) is True, "Contrast slider is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].set_slider_value_decrease(100,"Contrast_slider")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "0", "Contrast slider value is not 0"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_game_mode_title()) is True, "Game mode is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(1)
        assert self.fc.fd["display_control"].get_game_mode() == "Gaming", "Game mode is not selected"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_low_blue_light_text()) is True, "Low blue light text is not visible"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_low_blue_light_toggle_text()) is True, "Low blue light toggle is not visible"
        time.sleep(2)
        self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        time.sleep(10)
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light_on() == "1", "Low blue light toggle is turned off"
        time.sleep(1)
        self.fc.fd["display_control"].click_close_btn_advanced_settings
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_restore_default_button) is True, "Restore default button is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_default_button_1()
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_continue_on_delete_app_setting) is True, "Continue button is not visible"
        time.sleep(3)
        self.fc.fd["display_control"].click_continue_button_dialog()
        time.sleep(6)
        assert bool(self.fc.fd["display_control"].verify_brightness_slider_is_present()) is True, "Brightness slider is not visible"
        time.sleep(6)
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "76", "Brightness slider value is not 76"
        time.sleep(1)
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "100",  "Contrast slider value is not 100"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "Natural image mode is not visible"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_low_blue_light_text()) is True, "Low blue light text is not visible"
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_low_blue_light_toggle_text()) is True, "Low blue light toggle is not visible"
        time.sleep(1)
        assert self.fc.fd["display_control"].get_toggle_of_low_blue_light_on() == "0", "Low blue light toggle is turned on"
        time.sleep(1)
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)

    @pytest.mark.ota
    def test_02_display_control_and_app_settings_first_launch_C37825787(self):
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        self.fc.fd["devices"].click_display_control()
        time.sleep(1)
        assert bool(self.fc.fd["display_control"].verify_brightness_contrast_label) is True, "Brightness and contrast label is not visible"
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        assert "Add Application" in self.fc.fd["display_control"].verify_add_application_text(),"Add Application text is not visible"
        time.sleep(10)
        brightness_slider_value=self.fc.fd["display_control"].get_brightness_slider_value_100()
        assert round(float(brightness_slider_value)) == 76,"Brightness slider value is not 76"
        contrast_slider_value=self.fc.fd["display_control"].get_contrast_slider_value_100()
        assert round(float(contrast_slider_value)) == 100,"Contrast slider value is not 100"
        time.sleep(1)
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(10)
        toggle_state = self.fc.fd["display_control"].get_toggle_of_low_blue_light()
        assert toggle_state == '0' , "Low blue light toggle is turned on"
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red slider value is not 100"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green slider value is not 100"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue slider value is not 100"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_mode_selecttion_when_enable_lbl_toggle_button_C34324911(self):
        time.sleep(3)
        # self.fc.reset_myhp_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()
        time.sleep(3)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
       # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not show"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
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
        # verify movie image mode is still be selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not show"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button status is not 1"
        time.sleep(1)
        # get turn on time drop down is 11:00
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # get turn on time state am show
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        # get turn off time drop down is 6:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off6:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        # get turn off time state pm show
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(3)
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

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_mode_selecttion_when_disable_lbl_toggle_button_C34324912(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()
        time.sleep(4)
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
       # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not show"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True
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
        # verify movie image mode is still be selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not show"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced Settings button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert bool(self.fc.fd["display_control"].verify_advanced_settings_title()) is True, "Advanced settings title is not visible"
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not show"
        time.sleep(1)
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
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify movie image mode is still be selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "Movie image mode is not show"
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

    # @pytest.mark.consumer
    # @pytest.mark.function
    # def test_05_continoulsy_switch_between_red_green_blue_slider_C34324890(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     time.sleep(10)
    #     # go to navigated bar
    #     self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
    #     time.sleep(1)
    #     # click pc device menu
    #     self.fc.fd["navigation_panel"].click_PC_device_menu()
    #     time.sleep(1)
    #     # click display control card
    #     self.fc.fd["devices"].click_display_control()
    #     time.sleep(1)
    #     # verify restore default button show
    #     assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
    #     time.sleep(1)
    #     # click restore default button
    #     self.fc.fd["display_control"].click_restore_defaults_button()
    #     time.sleep(1)
    #     # click "continue" button
    #     self.fc.fd["display_control"].click_restore_pop_up_continue_button()
    #     time.sleep(10)
    #     # verify settings button show
    #     assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not show"
    #     time.sleep(1)
    #     # click settings button
    #     self.fc.fd["display_control"].click_advaced_setting()
    #     time.sleep(1)
    #     # verify string of "advanced settings" show
    #     assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
    #     time.sleep(1)
    #     # verify red color slider show
    #     assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
    #     time.sleep(1)
    #     # verify red color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 5 for red color slider 
    #     self.fc.fd["display_control"].set_red_slider_value_decrease(5,"red_slider")
    #     time.sleep(1)
    #     # get red color slider value is 95
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "95", "Red color slider value is not 95"
    #     time.sleep(1)
    #     # verify green color slider show
    #     assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
    #     time.sleep(1)
    #     # verify green color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 10 for green color slider
    #     self.fc.fd["display_control"].set_green_slider_value_decrease(10,"green_slider")
    #     time.sleep(1)
    #     # get green color slider value is 90
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "90", "Green color slider value is not 90"
    #     time.sleep(1)
    #     # verify blue color slider show
    #     assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
    #     time.sleep(1)
    #     # verify blue color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 15 for blue color slider
    #     self.fc.fd["display_control"].set_blue_slider_value_decrease(15,"blue_slider")
    #     time.sleep(1)
    #     # get blue color slider value is 85
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "85", "Blue color slider value is not 85"
    #     time.sleep(3)
    #     # get red color slider value is 95
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "95", "Red color slider value is not 95"
    #     time.sleep(1)
    #     # increase 3 for red color slider
    #     self.fc.fd["display_control"].set_slider_value_increase(3,"red_slider")
    #     time.sleep(1)
    #     # get red color slider value is 98
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "98", "Red color slider value is not 98"
    #     time.sleep(1)
    #     # get green color slider value is 90
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "90", "Green color slider value is not 90"
    #     time.sleep(1)
    #     # increase 5 for green color slider
    #     self.fc.fd["display_control"].set_slider_value_increase(5,"green_slider")
    #     time.sleep(1)
    #     # get green color slider value is 95
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "95", "Green color slider value is not 95"
    #     time.sleep(1)
    #     # get blue color slider value is 85
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "85", "Blue color slider value is not 85"
    #     time.sleep(1)
    #     # increase 7 for blue color slider
    #     self.fc.fd["display_control"].set_slider_value_increase(7,"blue_slider")
    #     time.sleep(1)
    #     # get blue color slider value is 92
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "92", "Blue color slider value is not 92"
    #     time.sleep(1)
    #     # click "x" button in advanced settings
    #     self.fc.fd["display_control"].click_close_btn_advanced_settings()
    #     time.sleep(1)

    # @pytest.mark.consumer
    # @pytest.mark.function
    # def test_06_red_slider_color_visual_C34324891(self):
    #     time.sleep(2)
    #     self.fc.re_install_app_and_skip_fuf(self.driver.session_data["installer_path"])
    #     time.sleep(5)
    #     # go to navigated bar
    #     self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
    #     time.sleep(1)
    #     # click pc device menu
    #     self.fc.fd["navigation_panel"].click_PC_device_menu()
    #     time.sleep(1)
    #     # click display control card
    #     self.fc.fd["devices"].click_display_control()
    #     time.sleep(1)
    #     # verify restore default button show
    #     assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
    #     time.sleep(1)
    #     # click restore default button
    #     self.fc.fd["display_control"].click_restore_defaults_button()
    #     time.sleep(1)
    #     # click "continue" button
    #     self.fc.fd["display_control"].click_restore_pop_up_continue_button()
    #     time.sleep(10)
    #     # verify settings button show
    #     assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not show"
    #     time.sleep(1)
    #     # click settings button
    #     self.fc.fd["display_control"].click_advaced_setting()
    #     time.sleep(1)
    #     # verify string of "advanced settings" show
    #     assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
    #     time.sleep(1)
    #     # verify red color slider show
    #     assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
    #     time.sleep(1)
    #     # verify red color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for red color slider 
    #     self.fc.fd["display_control"].set_red_slider_value_decrease(100,"red_slider")
    #     time.sleep(1)
    #     # get red color slider value is 0
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "0", "Red color slider value is not 0"
    #     time.sleep(1)
    #     # verify green color slider show
    #     assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
    #     time.sleep(1)
    #     # verify green color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for green color slider
    #     self.fc.fd["display_control"].set_green_slider_value_decrease(100,"green_slider")
    #     time.sleep(1)
    #     # get green color slider value is 0
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "0", "Green color slider value is not 0"
    #     time.sleep(1)
    #     # verify blue color slider show
    #     assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
    #     time.sleep(1)
    #     # verify blue color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for blue color slider
    #     self.fc.fd["display_control"].set_blue_slider_value_decrease(100,"blue_slider")
    #     time.sleep(1)
    #     # get blue color slider value is 0
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "0", "Blue color slider value is not 0"
    #     time.sleep(3)
    #     # get red color slider value is 0
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "0", "Red color slider value is not 0"
    #     time.sleep(1)
    #     # increase 100 for red color slider
    #     self.fc.fd["display_control"].set_slider_value_increase(100,"red_slider")
    #     time.sleep(1)
    #     # get red color slider value is 100
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
    #     time.sleep(1)
    #     # click "x" button in advanced settings
    #     self.fc.fd["display_control"].click_close_btn_advanced_settings()
    #     time.sleep(1)

    # @pytest.mark.consumer
    # @pytest.mark.function
    # def test_07_green_slider_color_visual_C34324892(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     time.sleep(10)
    #     # go to navigated bar
    #     self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
    #     time.sleep(1)
    #     # click pc device menu
    #     self.fc.fd["navigation_panel"].click_PC_device_menu()
    #     time.sleep(1)
    #     # click display control card
    #     self.fc.fd["devices"].click_display_control()
    #     time.sleep(1)
    #     # verify restore default button show
    #     assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
    #     time.sleep(1)
    #     # click restore default button
    #     self.fc.fd["display_control"].click_restore_defaults_button()
    #     time.sleep(1)
    #     # click "continue" button
    #     self.fc.fd["display_control"].click_restore_pop_up_continue_button()
    #     time.sleep(10)
    #     # verify settings button show
    #     assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not show"
    #     time.sleep(1)
    #     # click settings button
    #     self.fc.fd["display_control"].click_advaced_setting()
    #     time.sleep(1)
    #     # verify string of "advanced settings" show
    #     assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
    #     time.sleep(1)
    #     # verify red color slider show
    #     assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
    #     time.sleep(1)
    #     # verify red color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for red color slider 
    #     self.fc.fd["display_control"].set_red_slider_value_decrease(100,"red_slider")
    #     time.sleep(1)
    #     # get red color slider value is 0
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "0", "Red color slider value is not 0"
    #     time.sleep(1)
    #     # verify green color slider show
    #     assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
    #     time.sleep(1)
    #     # verify green color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for green color slider
    #     self.fc.fd["display_control"].set_green_slider_value_decrease(100,"green_slider")
    #     time.sleep(1)
    #     # get green color slider value is 0
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "0", "Green color slider value is not 0"
    #     time.sleep(1)
    #     # verify blue color slider show
    #     assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
    #     time.sleep(1)
    #     # verify blue color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for blue color slider
    #     self.fc.fd["display_control"].set_blue_slider_value_decrease(100,"blue_slider")
    #     time.sleep(1)
    #     # get blue color slider value is 0
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "0", "Blue color slider value is not 0"
    #     time.sleep(3)
    #     # get green color slider value is 0
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "0", "Green color slider value is not 0"
    #     time.sleep(1)
    #     # increase 100 for green color slider
    #     self.fc.fd["display_control"].set_slider_value_increase(100,"green_slider")
    #     time.sleep(1)
    #     # get green color slider value is 100
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
    #     time.sleep(1)
    #     # click "x" button in advanced settings
    #     self.fc.fd["display_control"].click_close_btn_advanced_settings()
    #     time.sleep(1)

    # @pytest.mark.consumer
    # @pytest.mark.function
    # def test_8_blue_slider_color_visual_C34324893(self):
    #     time.sleep(3)
    #     self.fc.restart_myHP()
    #     time.sleep(10)
    #     # go to navigated bar
    #     self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
    #     time.sleep(1)
    #     # click pc device menu
    #     self.fc.fd["navigation_panel"].click_PC_device_menu()
    #     time.sleep(1)
    #     # click display control card
    #     self.fc.fd["devices"].click_display_control()
    #     time.sleep(1)
    #     # verify restore default button show
    #     assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "Restore default button is not show"
    #     time.sleep(1)
    #     # click restore default button
    #     self.fc.fd["display_control"].click_restore_defaults_button()
    #     time.sleep(1)
    #     # click "continue" button
    #     self.fc.fd["display_control"].click_restore_pop_up_continue_button()
    #     time.sleep(10)
    #     # verify settings button show
    #     assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "Advanced settings button is not show"
    #     time.sleep(1)
    #     # click settings button
    #     self.fc.fd["display_control"].click_advaced_setting()
    #     time.sleep(1)
    #     # verify string of "advanced settings" show
    #     assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced settings title is incorrect"
    #     time.sleep(1)
    #     # verify red color slider show
    #     assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "Red color slider is not show"
    #     time.sleep(1)
    #     # verify red color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "Red color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for red color slider 
    #     self.fc.fd["display_control"].set_red_slider_value_decrease(100,"red_slider")
    #     time.sleep(1)
    #     # get red color slider value is 0
    #     assert self.fc.fd["display_control"].verify_red_slider_value() == "0", "Red color slider value is not 0"
    #     time.sleep(1)
    #     # verify green color slider show
    #     assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "Green color slider is not show"
    #     time.sleep(1)
    #     # verify green color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "Green color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for green color slider
    #     self.fc.fd["display_control"].set_green_slider_value_decrease(100,"green_slider")
    #     time.sleep(1)
    #     # get green color slider value is 0
    #     assert self.fc.fd["display_control"].verify_green_slider_value() == "0", "Green color slider value is not 0"
    #     time.sleep(1)
    #     # verify blue color slider show
    #     assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "Blue color slider is not show"
    #     time.sleep(1)
    #     # verify blue color slider value default is 100
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
    #     time.sleep(1)
    #     # decrease 100 for blue color slider
    #     self.fc.fd["display_control"].set_blue_slider_value_decrease(100,"blue_slider")
    #     time.sleep(1)
    #     # get blue color slider value is 0
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "0", "Blue color slider value is not 0"
    #     time.sleep(3)
    #     # increase 100 for blue color slider
    #     self.fc.fd["display_control"].set_slider_value_increase(100,"blue_slider")
    #     time.sleep(1)
    #     # get blue color slider value is 100
    #     assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "Blue color slider value is not 100"
    #     time.sleep(1)
    #     # click "x" button in advanced settings
    #     self.fc.fd["display_control"].click_close_btn_advanced_settings()
    #     time.sleep(1)