import logging
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Display_Control(object):

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_display_modes_ui_for_keelung27_FHD_and_UHD_C53000446(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."        
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        time.sleep(5)
        list_of_options = ["Neutral","Warm","Cool","HP enhance+","Native"]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        options = [
            "display_modes_select_box_option_neutral_ltwo_page",
            "display_modes_select_box_option_warm_ltwo_page_keelung32",
            "display_modes_select_box_option_cool_ltwo_page_keelung32",
            "display_modes_select_box_option_hp_enhance_ltwo_page_keelung32",
            "display_modes_select_box_option_native_ltwo_page_keelung32"
            ]
        #scroll until reach top mode - "Neutral"
        self.fc.fd["display_control"].scroll_modes(direction="up",desired_mode_name="Neutral",desired_mode_id="display_modes_select_box_option_neutral_ltwo_page")
        i=0
        for _ in range(4):
            logging.info(f"Checking brightness value for {list_of_options[i]} mode")
            self.fc.fd["display_control"].select_display_modes_dropdown_value(options[i])
            time.sleep(4)
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            time.sleep(4)
            assert self.fc.fd["display_control"].get_display_modes_dropdown_value(options[i]) == list_of_options[i], f"{options[i]} is not matching."
            self.fc.fd["display_control"].scroll_modes(direction="down",desired_mode_name=list_of_options[i],desired_mode_id=options[i])
            time.sleep(3)
            i=i+1

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_advanced_setting_page_ui_for_keelung27_FHD_and_UHD_C53000450(self):
        #to close mode dropdown
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].verify_display_control_brightness_text_ltwo_page() == "Brightness", "Brightness text is not present."
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        assert self.fc.fd["display_control"].verify_display_control_display_modes_text_ltwo_page() == "Display modes", "Display Modes text is not present."
        assert self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page(), "Display Modes select box is not present."
        assert self.fc.fd["display_control"].verify_display_control_brightness_slider_ltwo_page(), "Brightness Slider is not present on the L2 page."
        time.sleep(3)
        #Navigate to Advance settings page.
        self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()
        #verify Input Switch,2 : Color Adjustment
        assert self.fc.fd["display_control"].verify_display_control_color_adjustment_text_lthree_page() == "Color adjustment", "Color Adjustment text is not present."
        assert self.fc.fd["display_control"].verify_display_control_switch_btn_lfour_page() == "Switch", "Switch text is not present."

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_default_value_for_all_modes_for_first_launch_on_keelung27_FHD_C53000454(self):
        #back to L2 page
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        list_of_options = ["Neutral","Warm","Cool","HP enhance+","Native"]
        brightness_slider_value = [76,18,50,76,100]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        time.sleep(3)
        options = [
            "display_modes_select_box_option_neutral_ltwo_page",
            "display_modes_select_box_option_warm_ltwo_page_keelung32",
            "display_modes_select_box_option_cool_ltwo_page_keelung32",
            "display_modes_select_box_option_hp_enhance_ltwo_page_keelung32",
            "display_modes_select_box_option_native_ltwo_page_keelung32"
        ]
        # Verify and validate brightness values for each mode
        i=0
        for _ in range(4):
            logging.info(f"Checking brightness value for {list_of_options[i]} mode")
            self.fc.fd["display_control"].select_display_modes_dropdown_value(options[i])
            time.sleep(4)
            silder_value = int(self.fc.fd["display_control"].get_brightness_slider_value())
            time.sleep(3)
            assert silder_value == brightness_slider_value[i], f"Brightness value for {list_of_options[i]} mode is not matching."
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            time.sleep(3)
            self.fc.fd["display_control"].scroll_modes(direction="up",desired_mode_name=list_of_options[i],desired_mode_id=options[i])
            time.sleep(2)
            i=i+1
