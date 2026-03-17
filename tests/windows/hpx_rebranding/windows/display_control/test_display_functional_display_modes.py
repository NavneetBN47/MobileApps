import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Bopeep(object):
    
    #this suite should run on willie,herbie
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_modes_restore_defaults_C42891275(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",80)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == '80', "Brightness value is not matching."
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1":
           self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        #select modes -entertainment
        self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
        self.fc.fd["display_control"].scroll_modes_native(direction="down",desired_mode_name="Entertainment",desired_mode_id="display_modes_select_box_option_entertainment_ltwo_page")
        self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page("display_modes_select_box_option_entertainment_ltwo_page")
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Entertainment", "Entertainment mode is not selected."
        #click on restore defaults button
        time.sleep(4)
        self.fc.fd["display_control"].get_focus_on_app("display_control_advanced_settings_restore_defaults_button_ltwo_page")
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        #verify brightness value should be on default value
        assert self.fc.fd["display_control"].get_brightness_slider_value() == '90', "Brightness value is not matching."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Default mode is not selected."
          
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_mode_strings_C42891261(self):
        mode_name_list = [ "Default","Native", "Photos and Videos (P3 D65)","Printing and Imaging (Adobe RGB)","sRGB (Web)","Entertainment"]
        mode_list = ["display_modes_select_box_option_default_ltwo_page","display_modes_select_box_option_willie_native_ltwo_page","display_modes_select_box_option_photos_videos_ltwo_page","display_modes_select_box_option_adobe_RGB_painting_and_imaging_ltwo_page","display_modes_select_box_option_sRGB_web_ltwo_page","display_modes_select_box_option_entertainment_ltwo_page"]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        for i in range(5):
            self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page(mode_list[i])
            time.sleep(3)
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == mode_name_list[i], f"{mode_name_list[i]} is not matching."
            self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
            time.sleep(2)
            self.fc.fd["display_control"].scroll_up_display_modes_list_window(1)
            time.sleep(3)
        self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
        self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page("display_modes_select_box_option_sRGB_web_ltwo_page")
        #Click Restore Default button,Check default values.
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Default mode is not selected."
