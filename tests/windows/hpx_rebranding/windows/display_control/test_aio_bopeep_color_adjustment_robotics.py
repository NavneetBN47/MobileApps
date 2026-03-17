import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):

    #TC is specifically can only be ran in Bopeep due to system modes, All the RGBC value has 5 difference to validate if brightness,RGB value is between 0 to 100 in UI.
    #System will restart and install new build and restore to default modes,values before tc run.
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_continously_switch_between_rgb_slider_C42892317(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(10)
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
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
            assert red_int >= 55, "Red value doesnot match"
            assert green_int >= 68, "Green value doesnot match"
            assert  blue_int >= 35, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0 , 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 8, "Red value doesnot match"
            assert green_int <= 8, "Green value doesnot match"
            assert blue_int <= 8, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_rgb_slider_value_C42892318(self):
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 100 , 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 100, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
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
            assert red_int >= 55, "Red value doesnot match"
            assert green_int >= 68, "Green value doesnot match"
            assert  blue_int >= 35, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_red_slider_color_visual_C42892319(self):
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        #Verify LED values (Red, Green, Blue, Clear)
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 22, "Red value doesnot match"
            assert green_int <= 27, "Green value doesnot match"
            assert blue_int <= 12, "Blue value doesnot match"
            assert red_int > green_int, "Red value should be higher than Green"
            assert red_int > blue_int, "Red value should be higher than Blue"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_green_slider_color_visual_C42892320(self):
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        #Verify LED values (Red, Green, Blue, Clear)
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 37, "Red value doesnot match"
            assert green_int >= 47, "Green value doesnot match"
            assert blue_int <= 19, "Blue value doesnot match"
            assert green_int > red_int, "Green value should be higher than Red"
            assert green_int > blue_int, "Green value should be higher than Blue"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_blue_slider_color_visual_C42892321(self):
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 100, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        #Verify LED values (Red, Green, Blue, Clear)
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 21, "Red value doesnot match"
            assert green_int <= 22, "Green value doesnot match"
            assert blue_int >= 19, "Blue value doesnot match"
            assert blue_int > green_int, "Blue value should be higher than Green"
            assert blue_int > red_int, "Blue value should be higher than Red"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(5)
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_rgb_slider_visual_for_neutral_modes_C42892325(self):
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
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
            assert red_int >= 55, "Red value doesnot match"
            assert green_int >= 68, "Green value doesnot match"
            assert  blue_int >= 35, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 8, "Red value doesnot match"
            assert green_int <= 8, "Green value doesnot match"
            assert blue_int <= 8, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_07_rgb_slider_visual_for_gaming_modes_C42892326(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        if self.fc.fd["display_control"].verify_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")=="Gaming" and self.fc.fd["display_control"].is_item_onscreen("display_modes_select_box_option_gaming_ltwo_page") == True:
            self.fc.fd["display_control"].click_title_bar()
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
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
            assert red_int >= 60, "Red value doesnot match"
            assert green_int >= 75, "Green value doesnot match"
            assert  blue_int >= 39, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_title_bar()
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        self.vcosmos.get_red_green_blue_clear_value()
        #Verify LED values (Red, Green, Blue, Clear)
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 8, "Red value doesnot match"
            assert green_int <= 8, "Green value doesnot match"
            assert blue_int <= 8, "Blue value doesnot match"
        self.vcosmos.clean_up_logs()
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()