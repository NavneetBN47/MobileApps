import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control(object):
    
    #this suite should run on keelung32 platform
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_default_value_for_all_modes_for_first_launch_on_keelung_32_C51248443(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        br_value=[36,6,36,100,36,22,6,36]
        mode_name_list = ["P3 (D65)", "BT709 (D65)", "sRGB D65", "Native", "HP enhance+", "Cool", "Warm", "Neutral"]
        mode_list = ["display_modes_select_box_option_P3(D65)_ltwo_page_keelung32","display_modes_select_box_option_BT709(D65)_ltwo_page_keelung32", "display_modes_select_box_option_sRGB(D65)_ltwo_page_keelung32", "display_modes_select_box_option_native_ltwo_page_keelung32", "display_modes_select_box_option_hp_enhance_ltwo_page_keelung32", "display_modes_select_box_option_cool_ltwo_page_keelung32", "display_modes_select_box_option_warm_ltwo_page_keelung32", "display_modes_select_box_option_neutral_ltwo_page"]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        for i in range(7):
            self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page(mode_list[i])
            time.sleep(3)
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == mode_name_list[i], f"{mode_name_list[i]} is not matching."
            assert int(self.fc.fd["display_control"].get_brightness_slider_value()) == br_value[i], f"Brightness value for {mode_name_list[i]} mode is not matching."
            self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
            time.sleep(2)
            self.fc.fd["display_control"].scroll_up_display_modes_list_window()
            time.sleep(3)
