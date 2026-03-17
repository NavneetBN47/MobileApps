import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control(object):
   
    #this suite should run on bopeep
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_verify_app_contrast_slider_displays_correctly_as_set_up_C42891132(self):
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        #select any mode Default,Native and entertainment Display mode
        self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
        self.fc.fd["display_control"].scroll_modes_native(direction="down",desired_mode_name="Native",desired_mode_id="display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page("display_modes_select_box_option_native_ltwo_page")
        self.fc.fd["display_control"].get_focus_on_app("display_control_contrast_toggle")
        self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
        assert self.fc.fd["display_control"].get_contrast_slider_value() == "100", "Contrast slider value is not matching."
        #set contrast slider value to 95
        self.fc.fd["display_control"].set_slider_value("display_control_contrast_slider_lthree_page",95)
        assert self.fc.fd["display_control"].get_contrast_slider_value() == "95", "Contrast slider value is not matching."
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_brightness_strings_C42891117(self):
        brightness_text_ltwo_page = self.fc.fd["display_control"].verify_display_control_brightness_text_ltwo_page()
        assert brightness_text_ltwo_page == "Brightness" ,"Brightness text is not present."
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        restore_default_button_ltwo_page = self.fc.fd["display_control"].verify_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        assert restore_default_button_ltwo_page == "Restore default", "Restore Default button is not present on the L2 page."
        #click restore defaults to get the default values
        self.fc.fd["display_control"].get_focus_on_app("display_control_advanced_settings_restore_defaults_button_ltwo_page")
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        list_of_options = ["Neutral", "Gaming", "Reading", "Night", "Movie", "HP enhance+", "Native"]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        time.sleep(3)
        options = ["display_modes_select_box_option_neutral_ltwo_page","display_modes_select_box_option_gaming_ltwo_page","display_modes_select_box_option_reading_ltwo_page","display_modes_select_box_option_night_ltwo_page","display_modes_select_box_option_movie_ltwo_page","display_modes_select_box_option_hp_enhance_ltwo_page","display_modes_select_box_option_native_ltwo_page"]
        # Scroll until "Neutral" option is found
        for i in range(20):
            if self.fc.fd["display_control"].verify_display_modes_dropdown_value("display_modes_select_box_option_neutral_ltwo_page")=="Neutral":
                break
            self.fc.fd["display_control"].scroll_up_display_modes_list_window(2)
        for i in range(6):
            logging.info(f"Checking brightness value for {list_of_options[i]} mode")
            self.fc.fd["display_control"].select_display_modes_dropdown_value(options[i])
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            time.sleep(2)
            assert self.fc.fd["display_control"].get_display_modes_dropdown_value(options[i]) == list_of_options[i], f"{list_of_options[i]} is not matching."
            self.fc.fd["display_control"].scroll_modes(direction="down",desired_mode_name=list_of_options[i], desired_mode_id=options[i])
            time.sleep(4)
        advance_display_settings_txt_ltwo_page = self.fc.fd["display_control"].verify_display_control_advanced_settings_card_ltwo_page()
        assert "Advanced display settings" in advance_display_settings_txt_ltwo_page , "Advanced display settings text is not present on the L2 page."
