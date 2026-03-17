import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe_robotics")
class Test_Suite_Display_control(object):

    # tc for keelung 32
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_global_application_with_respective_rgb_for_oobe_default_C42891324(self):
        self.fc.check_and_navigate_to_display_control_page()
        #restore all apps default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        #global application is name as all application in method
        self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page_selected() == "true", "Global application is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 5, f"Red value is not less than or equal to 5, actual value: {red_int}"
            assert green_int <= 5, f"Green value is not less than or equal to 5, actual value: {green_int}"
            assert blue_int <= 5, f"Blue value is not less than or equal to 5, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(20)
        assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0"," HDR is turned on"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 5, f"Red value is not less than or equal to 5, actual value: {red_int}"
            assert green_int <= 5, f"Green value is not less than or equal to 5, actual value: {green_int}"
            assert blue_int <= 5, f"Blue value is not less than or equal to 5, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        self.fc.fd["display_control"].click_display_control_tencent_app_ltwo_page()
        time.sleep(20)
        assert  self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page_seleted() == "true", "Tecent app is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        # If element is found, proceed to check visibility (or other actions)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0"," HDR is turned on"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 5, f"Red value is not less than or equal to 5, actual value: {red_int}"
            assert green_int <= 5, f"Green value is not less than or equal to 5, actual value: {green_int}"
            assert blue_int <= 5, f"Blue value is not less than or equal to 5, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        self.fc.fd["display_control"].click_display_control_iqiyi_app_ltwo_page()
        time.sleep(20)
        assert  self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page_selected() == "true", "Iqiyi app is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle is off"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0"," HDR is turned on"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 5, f"Red value is not less than or equal to 5, actual value: {red_int}"
            assert green_int <= 5, f"Green value is not less than or equal to 5, actual value: {green_int}"
            assert blue_int <= 5, f"Blue value is not less than or equal to 5, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page_selected() == "true", "Global application is not selected"
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_oobe_default_restore_button_C42891333(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(20)
        assert  self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["devicesMFE"].maximize_app()
        #carries changes from tc 1
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0"," HDR is turned on"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled() == "true", "display mode is not disabled"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 5, f"Clear value is not less than or equal to 5, actual value: {clear_int}"
            assert red_int <= 5, f"Red value is not less than or equal to 5, actual value: {red_int}"
            assert green_int <= 5, f"Green value is not less than or equal to 5, actual value: {green_int}"
            assert blue_int <= 5, f"Blue value is not less than or equal to 5, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        #description for OOB app
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_description_onpopup_window_page() == "Restore the selected application settings to the HP recommended defaults?", "Restore default description is not matching for OOBE"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "0", "Don't show again check box is not checked"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1"," HDR is turned on"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled() == "false", "display mode is not disabled"
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0"," HDR is turned on"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 5, f"Clear value is not less than or equal to 5, actual value: {clear_int}  "
            assert red_int >= 5, f"Red value is not less than or equal to 5, actual value: {red_int}  "
            assert green_int >= 5, f"Green value is not less than or equal to 5, actual value: {green_int}  "
            assert blue_int >= 5, f"Blue value is not less than or equal to 5, actual value: {blue_int}  "
        self.vcosmos.clean_up_logs()
        #restoring the value of disney for new tc.
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_oobe_default_with_global_application_1_C42891329(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page_selected() == "true", "Global application is not selected"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "Brightness slider is not P3(D65)"
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "sRGB D65", "Brightness slider is not sRGB D65"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness slider value is not 36"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 100, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 89, f"Clear value is not less than or equal to 89, actual value: {clear_int}"
            assert red_int <= 65, f"Red value is not less than or equal to 65, actual value: {red_int}"
            assert green_int <= 74, f"Green value is not less than or equal to 74, actual value: {green_int}"
            assert blue_int <= 59, f"Blue value is not less than or equal to 59, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1"," HDR is turned off"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page_is_enabled_disabled() == "false", "display mode is not disabled"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 290, f"Clear value is not greater than or equal to 290, actual value: {clear_int}"
            assert red_int >= 160, f"Red value is not greater than or equal to 160, actual value: {red_int}"
            assert green_int >= 210, f"Green value is not greater than or equal to 210, actual value: {green_int}"
            assert blue_int >= 120, f"Blue value is not greater than or equal to 120, actual value: {blue_int}"
        self.vcosmos.clean_up_logs()
        #restore the changes made in tc
        self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page_selected() == "true", "Global application is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()