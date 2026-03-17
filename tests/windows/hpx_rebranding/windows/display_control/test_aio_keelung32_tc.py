import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control(object):
    
    #this suite should run on keelung32 platform
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_advanced_setting_page_ui_for_keelung_32_C51248442(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(4)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "P3 (D65) mode is not selected."
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness value is not 36 for P3 (D65) mode."
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle switch state is 1 on the L2 page."
        assert bool(self.fc.fd["display_control"].verify_display_control_advanced_settings_card_ltwo_page()) is True, "Advanced settings card is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
        assert bool(self.fc.fd["display_control"].verify_display_control_input_switch_tooltip_lthree_page_keelung32()) is True, "Input switch tooltip is not present on the L3 page."
        assert self.fc.fd["display_control"].verify_display_control_color_adjustment_text_lthree_page() == "Color adjustment", "Color adjustment text is not present on the L3 page."
        assert bool(self.fc.fd["display_control"].verify_display_control_low_blue_light_red_slider_lthree_page()) is True, "Red Color adjustment is not present on the L3 page."
        assert bool(self.fc.fd["display_control"].verify_display_control_low_blue_light_green_slider_lthree_page()) is True, "Green Color adjustment is not present on the L3 page."
        assert bool(self.fc.fd["display_control"].verify_display_control_low_blue_light_blue_slider_lthree_page()) is True, "Blue Color adjustment is not present on the L3 page."
        assert self.fc.fd["display_control"].verify_display_control_input_switch_text_lthree_page_keelung32() == "Input switch", "Input switch text is not present on the L3 page."
        self.fc.fd["devicesMFE"].click_back_button_rebranding()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_ui_modes_for_keelung32_C51248416(self):
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1":
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        
        mode_list = ["display_modes_select_box_option_P3(D65)_ltwo_page_keelung32","display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32", "display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32", "display_modes_select_box_option_native_ltwo_page_keelung32", "display_modes_select_box_option_hp_enhance_ltwo_page_keelung32", "display_modes_select_box_option_cool_ltwo_page_keelung32", "display_modes_select_box_option_warm_ltwo_page_keelung32", "display_modes_select_box_option_neutral_ltwo_page"]
        mode_name_list = ["P3 (D65)", "BT709 (D65)", "sRGB D65", "Native", "HP enhance+", "Cool", "Warm", "Neutral"]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        for i in range(7):
            self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page(mode_list[i])
            time.sleep(3)
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == mode_name_list[i], f"{mode_name_list[i]} is not matching."
            self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
            time.sleep(2)
            self.fc.fd["display_control"].scroll_up_display_modes_list_window()
            time.sleep(3)
