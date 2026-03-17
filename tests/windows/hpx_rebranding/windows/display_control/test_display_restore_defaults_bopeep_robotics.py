import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    #TC is specifically can only be ran in Bopeep due to system modes, All the RGBC value has 5 difference to validate if brightness,RGB value is between 0 to 100 in UI.
    #System will restart and install new build and restore to default modes,values before tc run.
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restore_default_button_for_neutral_C42891307(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(20)
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        #assert RGB value is 100 as default.
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #validate default neutral value.
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 93, "Clear value is not matching"
            assert red_int >= 55, "Red value doesnot match"
            assert green_int >= 68, "Green value doesnot match"
            assert  blue_int >= 35, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        #change the settings
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 80)
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(3)
        #click title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=6)
        #validating the default value after clicking restore.
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_restore_default_button_for_gaming_C42891308(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_gaming_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "84", "Brightness slider value is not 84"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        #assert RGB value is 100 as default.
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        # Verify LED values (Red, Green, Blue, Clear)get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 100, "Brightness visual is not matching"
            assert red_int >= 60, "Red value doesnot match"
            assert green_int >= 75, "Green value doesnot match"
            assert blue_int >= 39, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        #change the settings
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 80)
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(3)
        #click title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=6)
        #validating the default value after clicking restore.
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_gaming_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "84", "Brightness slider value is not 84"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_restore_default_button_for_reading_C42891309(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_reading_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_reading_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Reading", "Brightness slider is not Reading"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "52", "Brightness slider value is not 52"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        #assert RGB value is 100 as default.
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        # Verify LED values (Red, Green, Blue, Clear)get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 55, "Brightness visual is not matching"
            assert red_int >= 32, "Red value doesnot match"
            assert green_int >= 38, "Green value doesnot match"
            assert blue_int >= 13, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        #change the settings
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 80)
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(3)
        #click title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=6)
        #validating the default value after clicking restore.
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_reading_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_reading_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Reading", "Brightness slider is not Reading"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "52", "Brightness slider value is not 52"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_restore_default_button_for_night_C42891310(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_night_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_night_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Night", "Brightness slider is not Night"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "28", "Brightness slider value is not 28"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        #assert RGB value is 100 as default.
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int <= 39, "Brightness visual is not matching"
            assert red_int <= 31, "Red value doesnot match"
            assert green_int <= 30, "Green value doesnot match"
            assert blue_int <= 15, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        #change the settings
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 80)
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(3)
        #click title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=6)
        #validating the default value after clicking restore.
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_night_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_night_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Night", "Brightness slider is not Night"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "28", "Brightness slider value is not 28"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_restore_default_button_for_movie_C42891311(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_movie_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_movie_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "20", "Brightness slider value is not 20"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        #assert RGB value is 100 as default.
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert clear_int >= 34, "Brightness visual is not matching"
            assert red_int >= 17, "Red value doesnot match"
            assert green_int >= 23, "Green value doesnot match"
            assert blue_int >= 9, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        #change the settings
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 80)
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(3)
        #click title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=6)
        #validating the default value after clicking restore.
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_movie_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_movie_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "20", "Brightness slider value is not 20"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_restore_default_button_for_hpenhance_C42891312(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "HP enhance+", "Brightness slider is not HP enhance+"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        #assert RGB value is 100 as default.
        self.vcosmos.get_red_green_blue_clear_value()
        # Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            clear_int = int(clear)
            assert clear_int >= 95, "Brightness visual is not matching"
        self.vcosmos.clean_up_logs()
        #change the settings
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        # click restore value to restore the value.
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        #validating the default value after clicking restore.
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_hp_enhance_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_hp_enhance_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "HP enhance+", "Brightness slider is not HP enhance+"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_07_restore_default_button_for_native_C42891313(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        #assert RGB value is 100 as default.
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        # Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int >= 112, "Brightness visual is not matching"
            assert red_int >= 71, "Red value doesnot match"
            assert green_int >= 89, "Green value doesnot match"
            assert blue_int >= 47, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        #change the settings
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_red_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_green_slider_lthree_page", 80)
        self.fc.fd["display_control"].set_slider_value("display_control_low_blue_light_blue_slider_lthree_page", 80)
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(3)
        #click title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        #click restore value to restore the value.
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=8)
        #validating the default value after clicking restore.
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id="display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
        time.sleep(10)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"