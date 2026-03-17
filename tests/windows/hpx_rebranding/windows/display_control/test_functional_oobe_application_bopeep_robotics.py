import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe_robotics")
class Test_Suite_Display_control(object):
    
    #this suite should only run in bopeep
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_oobe_default_with_rgb_color_C42891323(self):
        # clean up logs possibly left by previous tests
        self.vcosmos.clean_up_logs()
        self.fc.check_and_navigate_to_display_control_page()
        # restore all apps default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=4)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(5)
        # restore disney + default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_low_blue_light_red_slider_lthree_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_green_slider_lthree_page()
        self.fc.fd["display_control"].click_display_control_low_blue_light_blue_slider_lthree_page()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int >= 54, "Red value does not match"
            assert green_int >= 69, "Green value does not match"
            assert blue_int >= 35, "Blue value does not match"
        self.vcosmos.clean_up_logs()
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
            assert red_int <= 13, "Red value does not match"
            assert green_int <= 14, "Green value does not match"
            assert blue_int <= 10, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        self.fc.close_myHP()
        self.fc.fd["display_control"].launch_all_apps("Disney+")
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 13, "Red value does not match"
            assert green_int <= 14, "Green value does not match"
            assert blue_int <= 10, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        self.driver.ssh.send_command('powershell taskkill /f /im pwahelper.exe', raise_e=False, timeout=10)

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_oobe_default_with_global_application_2_C42891330(self):
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.swipe_window(direction="up", distance=4)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        assert self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 0)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
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
            clear_int = int(clear)
            assert clear_int <= 5, "Clear value does not match"
            assert red_int <= 5, "Red value does not match"
            assert green_int <= 5, "Green value does not match"
            assert blue_int <= 5, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page_selected() == "true", "Global application is not selected"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            clear_int = int(clear)
            assert clear_int != 0, "Clear value does not match"
            assert red_int != 0, "Red value does not match"
            assert green_int != 0, "Green value does not match"
            assert blue_int != 0, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        #reverting back the chnages
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected() == "true", "Disney app is not selected"
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_oobe_default_with_any_application_in_the_app_list_1_C42891331(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        self.fc.fd["display_control"].enter_app_name_in_display_control_add_app_search_bar_ltwo_page("Access")
        self.fc.fd["display_control"].select_display_control_access_app_on_add_application_popup_lthree_page()
        self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
        time.sleep(5)
        #restore Access app default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].verify_display_control_access_app_ltwo_page(), "Access app is not present"
        assert self.fc.fd["display_control"].verify_is_display_control_access_app_selected() == "true", "Access app is not selecetd"
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_gaming_ltwo_page")
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Gaming", "Brightness slider is not Gaming"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_red_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_green_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_low_blue_light_blue_slider_lthree_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "0", "Red value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "0", "Green value is not 0"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "0", "Blue value is not 0"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 5, "Red value does not match"
            assert green_int <= 5, "Green value does not match"
            assert blue_int <= 5, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        # Click on the title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=6)
        assert self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"Iqiyi app exist"
        self.fc.fd["display_control"].click_display_control_iqiyi_app_ltwo_page()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=6)
        assert  self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page_selected() == "true", "Iqiyi app is not selected"
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Brightness slider is not Movie"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not 100"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int != 0, "Red value does not match"
            assert green_int != 0, "Green value does not match"
            assert blue_int != 0, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        #revert back changes for tc
        self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_oobe_default_with_any_application_in_the_app_list_2_C42891332(self):
        self.fc.check_and_navigate_to_display_control_page()
        self.fc.fd["display_control"].click_display_control_iqiyi_app_ltwo_page()
        time.sleep(5)#restore iqiyi to default values in case of previous case failure
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert  self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page_selected() == "true", "Iqiyi app is not selected"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie", "Mode is not Movie"
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_warm_ltwo_page")
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Brightness slider is not Native"
        self.fc.fd["display_control"].set_slider_value_by_keys("display_control_brightness_slider_button_ltwo_page", 0, 0, 100)
        self.fc.fd["display_control"].click_title_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not 0"
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
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
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int <= 5, "Red value does not match"
            assert green_int <= 5, "Green value does not match"
            assert blue_int <= 5, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        # Click on the title bar to prevent app lockup
        self.fc.fd["display_control"].click_title_bar()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
        time.sleep(5)
        assert  self.fc.fd["display_control"].verify_is_display_control_access_app_selected() == "true", "Access app is not selected"
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page() == "100", "Red value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page() == "100", "Green value is not 100"
        assert self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page() == "100", "Blue value is not 100"
        self.fc.swipe_window(direction="up", distance=6)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Brightness slider is not Neutral"
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not 76"
        self.vcosmos.get_red_green_blue_clear_value()
        red, green, blue, clear = self.vcosmos.verify_led_values()
        if red is not None and green is not None and blue is not None and clear is not None:
            red_int = int(red)
            green_int = int(green)
            blue_int = int(blue)
            assert red_int != 0, "Red value does not match"
            assert green_int != 0, "Green value does not match"
            assert blue_int != 0, "Blue value does not match"
        self.vcosmos.clean_up_logs()
        #revert back changes for upcoming tc
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["display_control"].click_display_control_iqiyi_app_ltwo_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()