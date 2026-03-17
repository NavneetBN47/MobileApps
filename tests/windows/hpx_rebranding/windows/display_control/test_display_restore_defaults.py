import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Display_Control(object):
    
    #this suite should run on willie
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_win_hover_over_restore_default_button_C42891305(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert self.fc.fd["display_control"].verify_display_control_advanced_settings_restore_defaults_button_ltwo_page() == "Restore default", "Restore defaults button is not present on the L2 page."
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_description_onpopup_window_page() == "Restore the settings to the HP factory defaults?", "Restore defaults description is not matching."
        #click on cancel btn in popup to close popup
        self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_ltwo_page()

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_modes_restore_default_non_aio_portrait_supported_C42891306(self):
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1":
            self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("0")
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        #select any mode from dropdown
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_willie_native_ltwo_page")
        #Set Brightness to random value in the range between minimum to maximum value
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page",85)
        self.fc.fd["display_control"].get_focus_on_app("display_control_advanced_settings_restore_defaults_button_ltwo_page")
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not matching."
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Display modes value is not matching."
