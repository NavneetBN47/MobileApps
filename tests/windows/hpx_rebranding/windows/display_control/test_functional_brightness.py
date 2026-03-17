import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control(object):
   
    #this suite should run on bopeep
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_brightness_minimum_value_relaunch_C42891125(self):
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching." 
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",0)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not matching."
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "0", "Brightness slider value is not matching."
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_brightness_maximum_value_relaunch_C42891126(self):
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",100)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not matching."
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100", "Brightness slider value is not matching."
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_03_brightness_medium_value_relaunch_C42891127(self):
        #set brightness slider value to 50
        if int(self.fc.fd["display_control"].get_brightness_slider_value()) <= 50:
            self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",50)
        else:
            self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",50)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "50", "Brightness slider value is not matching."
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "50", "Brightness slider value is not matching."
        
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_contrast_maximum_value_relaunch_C42891129(self):
        #click restore defaults to get the default values
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        #select any mode Default,Native and entertainment Display mode
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].scroll_modes_native(direction="down",desired_mode_name="Native",desired_mode_id="display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page("display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].get_focus_on_app("display_control_contrast_toggle")
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()

        self.fc.fd["display_control"].set_slider_value("display_control_contrast_slider_lthree_page",100)

        assert self.fc.fd["display_control"].get_contrast_slider_value() == "100", "Contrast slider value is not matching."
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert bool(self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()) is True, "Display modes select box is not present on the L2 page."
        assert bool(self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page()) is True, "Brightness slider is not present on the L2 page."
        self.fc.fd["display_control"].get_focus_on_app("display_control_contrast_toggle")
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()

        assert self.fc.fd["display_control"].get_contrast_slider_value() == "100", "Contrast slider value is not matching."
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_05_contrast_medium_value_relaunch_C42891130(self):
        #set contrast slider value to 50
        if int(self.fc.fd["display_control"].get_contrast_slider_value()) <= 50:
            self.fc.fd["display_control"].set_slider_value("display_control_contrast_slider_lthree_page",50)
        else:
            self.fc.fd["display_control"].set_slider_value("display_control_contrast_slider_lthree_page",50)
        assert self.fc.fd["display_control"].get_contrast_slider_value() == "50", "Brightness slider value is not matching."
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert bool(self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page()) is True, "Display modes select box is not present on the L2 page."
        assert bool(self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page()) is True, "Brightness slider is not present on the L2 page."
        self.fc.fd["display_control"].get_focus_on_app("display_control_contrast_toggle")
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        assert self.fc.fd["display_control"].get_contrast_slider_value() == "50", "Brightness slider value is not matching."
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_06_brightness_slider_value_remains_the_same_after_relaunch_the_app_C42891135(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        #set brightness slider value to 80
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",80)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "80", "Brightness slider value is not matching."
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "80", "Brightness slider value is not matching."
            
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_verify_app_brightness_slider_is_same_as_system_C42891131(self):
        #app stuck so have to restart the app
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #click restore defaults to get the default values
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness slider value is not matching."
        #set brightness slider value to 74
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",74)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "74", "Brightness slider value is not matching."
        assert self.fc.fd["display_control"].get_brightness_slider_value_from_system_tray() == "74", "Brightness slider value is not matching."
