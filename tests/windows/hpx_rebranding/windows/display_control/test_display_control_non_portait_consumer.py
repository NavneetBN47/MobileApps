import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):
    
    #this suite should be Consumer platform where HDR feature is available in windows settings For ex : Thompson,Grand,Park,Zonin etc
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_control_and_hdr_first_launch_and_dependency_check_C52975785(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) is True, "Add application button is not present"
        #need to add restore defaults btn action coz br always picking what ever set in system setting.
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()        
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
        assert self.fc.fd["display_control"].verify_display_control_advanced_settings_restore_defaults_button_ltwo_page() == "Restore default", "Restore default button is not present"

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_control_and_hdr_restore_default_settings_C52975793(self):
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) is True, "Add application button is not present"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()        
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) is True, "Restore default description is not visible"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "0", "Don't show again check box is not unchecked"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page() == "Continue", "Continue button is not present"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page() == "Cancel", "Cancel button is not present"
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
        #.perform random changes to the brightness and the HDR option
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",85)
        self.fc.fd["display_control"].get_focus_on_app("display_control_hdr_toggle_switch_ltwo_page")
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        #The changes will be applied and will be in sync with windows application
        time.sleep(2)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "85", "Brightness slider value is not 85"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle button is not on"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.open_system_settings_display()
        assert self.fc.fd["display_control"].get_system_setting_brightness_slider() == "85", "Brightness slider value is not 85"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle button is not on"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()        
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) is True, "Restore default description is not visible"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "0", "Don't show again check box is not unchecked"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page() == "Continue", "Continue button is not present"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page() == "Cancel", "Cancel button is not present"
        self.fc.fd["display_control"].click_display_control_restore_defaults_do_not_show_again_checkbox()
        assert self.fc.fd["display_control"].get_display_control_restore_defaults_do_not_show_again_checkbox_state() == "1", "Don't show again check box is not checked"
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",85)
        self.fc.fd["display_control"].get_focus_on_app("display_control_hdr_toggle_switch_ltwo_page")
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        assert self.fc.fd["display_control"].get_system_setting_brightness_slider() == "85", "Brightness slider value is not 85"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle button is not on"
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        self.fc.fd["display_control"].get_focus_on_app("display_control_advanced_settings_restore_defaults_button_ltwo_page")
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) == False, "Restore default description is visible"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
