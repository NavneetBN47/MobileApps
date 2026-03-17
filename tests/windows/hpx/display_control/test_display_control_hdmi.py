from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import re
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Bopeep(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
    
    #this suite should run on bopeep
    @pytest.mark.ota
    def test_01_verify_hdmi_ui_C35607426(self):
        self.fc.restart_myHP()
        time.sleep(10)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(7)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        self.fc.fd["devices"].click_display_control()
        time.sleep(3)
        self.fc.fd["display_control"].click_advaced_setting()
        actual_use_hdmi_input_text=self.fc.fd["display_control"].get_use_hdmi_input()
        soft_assertion.assert_equal(actual_use_hdmi_input_text, "Use HDMI Input","HDMI input title is not visible")

        actual_switch_text=self.fc.fd["display_control"].get_switch_text()
        soft_assertion.assert_equal(actual_switch_text, "Switch","Switch text is not visible")

        self.fc.fd["display_control"].click_use_hdmi_input_tooltip()
        time.sleep(3)
        actual_tooltip_use_hdmi_input_text = self.fc.fd["display_control"].get_use_hdmi_input_tooltip()
        expected_tooltip_use_hdmi_input_text = "Switch to the HDMI input to use your PC as a display. You can also switch to the input using the physical button of your device."
        soft_assertion.assert_equal(actual_tooltip_use_hdmi_input_text, expected_tooltip_use_hdmi_input_text,"switch to HDMI input1 tooltip text is not visible")

        keys_text = self.fc.fd["display_control"].verify_hpmi_input_description()
        soft_assertion.assert_equal(keys_text, "Press Ctrl + Shift + S + D to switch back to the PC desktop.","switch back text is not visible")

        hdmi_input_osd_help_text = self.fc.fd["display_control"].get_hdmi_input_osd_help_text()
        soft_assertion.assert_equal(hdmi_input_osd_help_text, "HDMI Input OSD Help","HDMI Input OSD Help text is not visible")

        self.fc.fd["display_control"].click_switch_btn()
        if self.fc.fd["display_control"].verify_windows_do_not_show_visible():
            back_to_pc_desktop_text=self.fc.fd["display_control"].get_back_to_pc_desktop_window_title()
            soft_assertion.assert_equal(back_to_pc_desktop_text, "Back to PC Desktop","Back to PC Desktop text is not visible")

            expected_back_to_pc_desktop_sub_title_text = "While in  HDMI Input, use these keyboard keys to switch back to the PC desktop."
            actual_back_to_pc_desktop_sub_title_text = self.fc.fd["display_control"].get_back_to_pc_desktop_window_sub_title()
            soft_assertion.assert_equal(actual_back_to_pc_desktop_sub_title_text, expected_back_to_pc_desktop_sub_title_text ,"HDMI input functions text is not visible")

            actual_keys_to_stop_text = self.fc.fd["display_control"].get_keys_to_stop_using_pcdesktop_text()
            expected_keys_to_stop_text = "Press Ctrl + Shift + S + D to stop using PC as a display"
            soft_assertion.assert_equal(actual_keys_to_stop_text, expected_keys_to_stop_text,"Press Ctrl + Shift + S + D text is not visible")

            do_not_show_again_text=self.fc.fd["display_control"].get_do_not_show_text_on_back_to_pc_desktop_window()
            soft_assertion.assert_equal(do_not_show_again_text, "Do not show again","Do not show again text is not visible")

            actual_cancel_btn_text=self.fc.fd["display_control"].get_cancel_btn_on_back_to_pc_desktop_window()
            soft_assertion.assert_equal(actual_cancel_btn_text, "Cancel","Cancel button text is not visible")

            actual_continue_btn_text=self.fc.fd["display_control"].get_continue_btn_on_back_to_pc_desktop_window()
            soft_assertion.assert_equal(actual_continue_btn_text, "Continue","Continue button text is not visible")
            self.fc.fd["display_control"].click_continue_btn_on_back_to_pc_desktop_window()
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_02_verify_hdmi_tooltips_C35607427(self):
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        self.fc.fd["devices"].click_display_control()
        time.sleep(2)
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(2)

        self.fc.fd["display_control"].click_use_hdmi_input_tooltip()
        time.sleep(3)
        actual_tooltip_use_hdmi_input_text = self.fc.fd["display_control"].get_use_hdmi_input_tooltip()
        expected_tooltip_use_hdmi_input_text = "Switch to the HDMI input to use your PC as a display. You can also switch to the input using the physical button of your device."
        soft_assertion.assert_equal(actual_tooltip_use_hdmi_input_text, expected_tooltip_use_hdmi_input_text,"switch to HDMI input2 tooltip text is not visible")

        time.sleep(2)
        self.fc.fd["display_control"].click_hdmi_input_osd_help_link()
        time.sleep(2)
        soft_assertion.assert_equal("While in  HDMI Input, use these keyboard keys to access and navigate the HDMI Input functions.", self.fc.fd["display_control"].get_hdmi_input_osd_help_sub_title_text())
        time.sleep(2)
        self.fc.fd["display_control"].click_close_btn_on_hdmi_input_osd_help_window()

        time.sleep(2)
        self.fc.fd["display_control"].click_switch_btn()
        expected_back_to_pc_desktop_sub_title_text = "While in  HDMI Input, use these keyboard keys to switch back to the PC desktop."
        actual_back_to_pc_desktop_sub_title_text = self.fc.fd["display_control"].get_back_to_pc_desktop_window_sub_title()
        soft_assertion.assert_equal(actual_back_to_pc_desktop_sub_title_text, expected_back_to_pc_desktop_sub_title_text ,"HDMI input functions text is not visible")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_03_hdmi_cancel_button_C35607433(self):
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        self.fc.fd["devices"].click_display_control()
        time.sleep(2)
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(2)
        print("--------",self.fc.fd["display_control"].verify_advanced_settings_title())
        soft_assertion.assert_equal(self.fc.fd["display_control"].verify_advanced_settings_title(), "Advanced Settings", "The advanced settings string is incorrect")
        soft_assertion.assert_equal(self.fc.fd["display_control"].get_use_hdmi_input(),"Use HDMI Input", "Use HDMI input text is not matching")
        self.fc.fd["display_control"].click_switch_btn()
        soft_assertion.assert_true(bool(self.fc.fd["display_control"].verify_windows_do_not_show_visible()), "The back to pc desktop window is not visible")
        soft_assertion.assert_equal(self.fc.fd["display_control"].get_do_not_show_text_on_back_to_pc_desktop_window(),"Do not show again", "Do not show again text is not matching")
        self.fc.fd["display_control"].click_check_box_on_backup_to_pc_desktop()
        #Able to click on "Do not show again" check box ,verification not possible due to -https://hp-jira.external.hp.com/browse/HPXWC-18188
        #soft_assertion.assert_equal(self.fc.fd["display_control"].verify_click_check_box_on_backup_to_pc_desktop_is_selected(),"1","The check box is not selected")
        self.fc.fd["display_control"].click_cancel_btn_on_back_to_pc_desktop_window()
        soft_assertion.assert_false(bool(self.fc.fd["display_control"].verify_windows_do_not_show_visible()), "The back to pc desktop window is not visible")
        self.fc.fd["display_control"].click_switch_btn()
        #Back to PC Desktop page should popup and check box should not checked,verification not possible due to-https://hp-jira.external.hp.com/browse/HPXWC-18188
        #soft_assertion.assert_equal(self.fc.fd["display_control"].verify_click_check_box_on_backup_to_pc_desktop_is_selected(),"0","The check box is selected")
        soft_assertion.raise_assertion_errors()
