from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Bopeep_App_Setting(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request,windows_test_setup):
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
            time.sleep(3)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
    
    #this suite should be run on bopeep
    @pytest.mark.ota
    def test_01_launch_selected_application_in_appsettings_bar_C37825790(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()

        self.fc.fd["display_control"].click_neutral_mode_container()
        time.sleep(4)
        self.fc.fd["display_control"].click_add_application_btn()
        assert bool(self.fc.fd["display_control"].verify_applications_display()) == True ,"Applications title is not present"
        self.fc.fd["display_control"].search_application("Calculator")
        self.fc.fd["display_control"].click_calculator_in_app_window()
        self.fc.fd["display_control"].click_add_btn()

        self.fc.fd["display_control"].select_calculator_in_app_list()
        self.fc.fd["display_control"].click_native_tile()
        time.sleep(5)
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native tile is not selected"
        self.fc.fd["display_control"].set_slider_value_decrease(20,"Brightness_slider")
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "80","Brightness slider value is not 80"
        self.fc.fd["display_control"].set_slider_value_decrease(20,"Contrast_slider")
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "80","Contrast slider value is not 80"
        self.fc.fd["display_control"].click_advaced_setting()
        self.fc.fd["display_control"].set_slider_value_decrease(20,"red_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(20,"green_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(20,"blue_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].verify_red_slider_value() == "80","Red slider value is not 80"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "80","Green slider value is not 80"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "80","Blue slider value is not 80"
        self.fc.fd["display_control"].click_close_btn_on_restore_popup()

        self.fc.fd["display_control"].click_global_app_icon()
        time.sleep(3)
        self.fc.fd["display_control"].select_calculator_in_app_list()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "80","Brightness slider value is not 80"
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "80","Contrast slider value is not 80"
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native tile is not selected"
        
        self.fc.fd["display_control"].click_advaced_setting()
        assert self.fc.fd["display_control"].verify_red_slider_value() == "80","Red slider value is not 80"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "80","Green slider value is not 80"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "80","Blue slider value is not 80"
        self.fc.fd["display_control"].click_close_btn_on_restore_popup()
    
    def test_02_adding_new_application_post_making_changes_in_global_settings_C37825795(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        #click restore btn to reset all slider values
        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
        #click global application
        self.fc.fd["display_control"].click_global_app_icon()
        #click native mode
        self.fc.fd["display_control"].click_native_tile()
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native tile is not selected"
        self.fc.fd["display_control"].set_slider_value_decrease(20,"Brightness_slider")
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "80","Brightness slider value is not 80"
        self.fc.fd["display_control"].set_slider_value_decrease(20,"Contrast_slider")
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "80","Contrast slider value is not 80"
        self.fc.fd["display_control"].click_advaced_setting()
        self.fc.fd["display_control"].set_slider_value_decrease(20,"red_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(20,"green_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(20,"blue_slider")
        time.sleep(2)
        assert self.fc.fd["display_control"].verify_red_slider_value() == "80","Red slider value is not 80"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "80","Green slider value is not 80"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "80","Blue slider value is not 80"
        self.fc.fd["display_control"].click_close_btn_on_restore_popup()
        self.fc.fd["display_control"].click_add_application_btn()
        assert bool(self.fc.fd["display_control"].verify_applications_display()) == True ,"Applications title is not present"
        self.fc.fd["display_control"].search_application("Calculator")
        self.fc.fd["display_control"].click_calculator_in_app_window()
        self.fc.fd["display_control"].click_add_btn()

        self.fc.fd["display_control"].select_calculator_in_app_list()
        assert bool(self.fc.fd["display_control"].is_Native_tile_selected()) == True,"Native tile is not selected"
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "80","Brightness slider value is not 80"
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "80","Contrast slider value is not 80"
        self.fc.fd["display_control"].click_advaced_setting()
        assert self.fc.fd["display_control"].verify_red_slider_value() == "80","Red slider value is not 80"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "80","Green slider value is not 80"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "80","Blue slider value is not 80"
        self.fc.fd["display_control"].click_close_btn_on_restore_popup()

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_relaunch_app_when_lbl_toggle_button_off_C32194994(self):
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
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
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
        # select random time from Turn-off (ex-8)
        self.fc.fd["display_control"].select_turn_off_time_drop_down_list_as_eight()
        time.sleep(1)
        # get turn off time drop down is 8:00
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off8:00Hour", "Turn off time drop down is not 6:00"
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
        self.fc.fd["display_control"].click_low_blue_light_toggle_off()
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
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
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        time.sleep(1)
        # verify low blue light button show
        assert bool(self.fc.fd["display_control"].get_toggle_of_low_blue_light()) is True, "Low blue light button is not visible"
        time.sleep(1)
        # get low blue light button status is 1
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0", "Low blue light button is not off"
        time.sleep(1)
        assert self.fc.fd["display_control"].get_turn_off_time_drop_down_list_show() == "Turn off8:00Hour", "Turn off time drop down is not 6:00"
        time.sleep(1)
        assert self.fc.fd["display_control"].get_turn_off_time_state_show() == "pm", "Turn off time state is not pm"
        time.sleep(1)
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        time.sleep(1)
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        self.fc.close_myHP()
    
    def test_04_relaunch_advance_setting_page_when_lbl_toggle_button_on_C32320194(self):
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
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        if self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "0":
            self.fc.fd["display_control"].click_low_blue_light_toggle_on()
        assert self.fc.fd["display_control"].get_low_blue_light_toggle_status() == "1", "Low blue light button is not on"
        #select 11 am turn on time
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        # select random time from Turn-on (ex-11 am)
        self.fc.fd["display_control"].select_turn_on_time_drop_down_list()
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        self.fc.fd["display_control"].select_turn_on_time_state_am()
        #verify 11 am turn on time selected
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        #select turn off time is 10 pm
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        self.fc.swipe_window(direction="down",distance=4)
        self.fc.fd["display_control"].select_dropdown_on_item_default()
        self.fc.fd["display_control"].click_turn_off_combo_advanced_settings()
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
        #verify 10 pm turn off time selected
        assert self.fc.fd["display_control"].verify_off_hour_time() == "Turn off10:00Hour", "Turn off time drop down is not 10:00"
        assert self.fc.fd["display_control"].verify_turn_off_default_am_time() == "pm", "Turn off time state is not pm"
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
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "Advanced Settings title is not displayed"
        #verify 11 am turn on time selected
        assert self.fc.fd["display_control"].get_turn_on_time_drop_down_list_show() == "Turn on11:00Hour", "Turn on time drop down is not 11:00"
        assert self.fc.fd["display_control"].get_turn_on_time_state_show() == "am", "Turn on time state is not am"
        #verify 10 pm turn off time selected
        assert self.fc.fd["display_control"].verify_off_hour_time() == "Turn off10:00Hour", "Turn off time drop down is not 10:00"
        assert self.fc.fd["display_control"].verify_turn_off_default_am_time() == "pm", "Turn off time state is not pm"
        
        #need to reset time as default(turn on time 10 pm and turn off time 7 am)
        self.fc.fd["display_control"].click_turn_on_time_drop_down_list()
        time.sleep(1)
        #turn on time 10 pm
        self.fc.fd["display_control"].select_dropdown_on_item_default()
        self.fc.fd["display_control"].click_turn_on_combo_advanced_settings()
        self.fc.fd["display_control"].click_turn_on_time_state_list()
        #turn off time 7 am
        self.fc.fd["display_control"].click_turn_off_time_drop_down_list()
        self.fc.fd["display_control"].select_dropdown_on_item()
        self.fc.fd["display_control"].click_turn_off_combo_advanced_settings()
        self.fc.fd["display_control"].select_turn_off_time_state_pm()
    