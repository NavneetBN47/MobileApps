import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):
    
    #this suite should be run on bopeep platform and keelung 27 platform 
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_hdmi_cancel_button_C42892355(self):
        time.sleep(3)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()
        time.sleep(3)
        self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
        #back to desktop
        assert self.fc.fd["display_control"].verify_display_control_back_to_pc_desktop_text_hdmi_popup_page() == "Back to PC desktop","Back to PC desktop Text is not matching."
        assert self.fc.fd["display_control"].verify_display_control_back_to_pc_desktop_description_hdmi_popup_page() == "While in HDMI input, use these keyboard keys to switch back to the PC desktop.","Back to PC desktop description is not matching."
        self.fc.fd["display_control"].click_display_control_hdmi_popup_page_do_not_show_again_text()
        assert self.fc.fd["display_control"].get_toggle_display_control_hdmi_popup_page_do_not_show_again_text() == "1","Do not show again text is not matching."
        self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
        assert self.fc.fd["display_control"].verify_display_control_use_hdmi_input_txt_lthree_page() == "Use HDMI input", "Use HDMI input Text is not matching."
        self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
        assert self.fc.fd["display_control"].get_toggle_display_control_hdmi_popup_page_do_not_show_again_text() == "0","Do not show again text is not matching."

        #click cancel on back to pc desktop popup to reach L2 page in display control
        self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_input_switch_feature_ui_C42892348(self):
        time.sleep(3)
        # 1-Title : "Use HDMI input"
        assert self.fc.fd["display_control"].verify_display_control_use_hdmi_input_txt_lthree_page() == "Use HDMI input", "Use HDMI input Text is not matching."
        # 2-(i) Button "Switch" to HDMI input to use your PC as Display You can aslo switch to the input using the physical button on the side of your device"
        assert self.fc.fd["display_control"].verify_display_control_switch_btn_lfour_page() == "Switch", "Switch Text is not matching."
        # 3.Press Ctrl + Shift + S + D to switch back to PC desktop. "Input OSD Help"
        assert "Hold Ctrl + Shift + S + D to switch back to the PC desktop. HDMI input OSD help" in self.fc.fd["display_control"].get_display_control_hdmi_link_text_lthree_page(), "Hold Ctrl + Shift + S + D to switch back to the PC desktop. HDMI input OSD help Switch Text is not matching."
        self.fc.fd["display_control"].click_display_control_hdmi_link("display_control_advancedsettings_hdmi_link_lthree_page")
        assert self.fc.fd["display_control"].get_display_control_hdmi_link_title_text() == "HDMI input OSD help", "HDMI input OSD help text is not matching."
        time.sleep(1)
        assert self.fc.fd["display_control"].get_display_control_hdmi_popup_description_1_text() == "Up and down arrows: Navigate OSD menu or change values of a selected function.","Up and down arrows: Navigate OSD menu or change values of a selected function. Text is not matching."
        #verify skip and next btn displayed
        assert self.fc.fd["display_control"].get_display_control_advancedsettings_hdmi_link_skip_button() == "Skip", "Skip Text is not matching."
        assert self.fc.fd["display_control"].get_display_control_next_btn_hdmi_popup_window() == "Next", "Next Text is not matching."
        self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
        self.fc.fd["devicesMFE"].maximize_app()
        #click next btn on popup
        self.fc.fd["display_control"].click_display_control_next_btn_hdmi_popup_window()
        assert self.fc.fd["display_control"].get_display_control_hdmi_popup_description_2_text() == "Enter: Select function. Also opens the Input OSD (On-Screen Display) menu.","Enter: Select a function. Also opens the HDMI Input OSD (On-Screen Display) menu. Text is not matching."
        self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["display_control"].click_display_control_next_btn_hdmi_popup_window()
        assert self.fc.fd["display_control"].get_display_control_hdmi_popup_description_3_text() == "Backspace: Go back to the previous menu item or exit the OSD menu.","Backspace: Go back to the previous menu item or exit the OSD menu Text is not matching."
        assert self.fc.fd["display_control"].get_display_control_close_btn_hdmi_popup_window() == "Close", "Close Text is not matching."
        #click previous btn to reach first description
        self.fc.fd["display_control"].click_display_control_previous_btn_hdmi_popup_window()
        self.fc.fd["display_control"].click_display_control_previous_btn_hdmi_popup_window()
        
        self.fc.fd["display_control"].click_hdmi_link_skip_btn_lfour_page()
        # click switch btn
        self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
        assert self.fc.fd["display_control"].verify_display_control_back_to_pc_desktop_text_hdmi_popup_page() == "Back to PC desktop","Back to PC desktop Text is not matching."
        assert self.fc.fd["display_control"].verify_display_control_back_to_pc_desktop_description_hdmi_popup_page() == "While in HDMI input, use these keyboard keys to switch back to the PC desktop.","Back to PC desktop description is not matching."
        assert self.fc.fd["display_control"].get_display_control_back_to_pc_desktop_description_2_hdmi_popup_page() == "Example: Hold Ctrl + Shift + S + D to stop using PC as a display.","Example: Hold Ctrl + Shift + S + D to stop using PC as a display Text is not matching."
        #do not show again chk box and text
        assert self.fc.fd["display_control"].get_display_control_hdmi_popup_page_do_not_show_again_text() == "Do not show again", "Do not show again Text is not matching."
        assert self.fc.fd["display_control"].get_display_control_hdmi_popup_page_cancel_button() == "Cancel"," Cancel Text is not matching."
        assert self.fc.fd["display_control"].get_display_control_hdmi_popup_page_continue_button() == "Continue","Continue Text is not matching."
        #to close popup
        self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_03_input_switch_hdmi_feature_tooltip_C42892349(self):
        self.fc.reset_hp_application()
        time.sleep(2)
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()
        assert self.fc.fd["display_control"].verify_display_control_use_hdmi_input_txt_lthree_page() == "Use HDMI input", "Use HDMI input Text is not matching."
        self.fc.fd["display_control"].click_use_hdmi_input_tooltip()
        use_hdmi_tooltip_text = self.fc.fd["display_control"].get_use_hdmi_input_tooltip()
        assert use_hdmi_tooltip_text == "Switch between inputs to use your pc as a display.You can also switch to the input using the physical button on the side of your device.", f"Use HDMI input Tooltip Text is not matching. expected 'Switch between inputs to use your pc as a display.You can also switch to the input using the physical button on the side of your device.', got '{use_hdmi_tooltip_text}'"
        #switch btn
        switch_text = self.fc.fd["display_control"].verify_display_control_switch_btn_lfour_page()
        assert switch_text == "Switch", f"Switch Text is not matching. expected 'Switch', got '{switch_text}'"
        self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
        back_to_pc_text = self.fc.fd["display_control"].verify_display_control_back_to_pc_desktop_text_hdmi_popup_page()
        assert back_to_pc_text == "Back to PC desktop", f"Back to PC desktop is not matching. expected 'Back to PC desktop', got '{back_to_pc_text}'"
        self.fc.fd["display_control"].click_display_control_hdmi_popup_page_cancel_button()
        self.fc.fd["display_control"].click_display_control_hdmi_link("display_control_advancedsettings_hdmi_link_lthree_page")
        time.sleep(2)
        hdmi_input_osd_text = self.fc.fd["display_control"].get_display_control_hdmi_link_title_text()
        assert hdmi_input_osd_text == "HDMI input OSD help", f"HDMI input OSD help text is not matching. expected 'HDMI input OSD help', got '{hdmi_input_osd_text}'"

