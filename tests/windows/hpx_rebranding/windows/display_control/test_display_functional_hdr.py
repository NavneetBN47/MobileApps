import logging
import pytest
import MobileApps.resources.const.windows.const as w_const
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Display_control(object):

    #this suite should run on willie
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_control_and_hdr_first_launch_and_dependency_check_C42891425(self):
        time.sleep(3)
        try:
            result = self.driver.ssh.send_command( '''Get-Package -Name "*HP Display Control*" | Select-Object Name, Version''')['stdout'].strip()
            logging.info(f"The current devices has {result}")
            is_package_version_present = (result !="")
            is_display_control_service_preinstall_file_present = self.driver.ssh.send_command( '''Test-Path -Path "{}" -PathType Container'''.format(w_const.TEST_DATA.DISPLAY_CONTROL_SERVIVE))['stdout'].strip()
            is_hpdc_preinstall_file_present = self.driver.ssh.send_command( '''Test-Path -Path "{}" -PathType Container'''.format(w_const.TEST_DATA.HPDC_SERVICE))['stdout'].strip()
            is_hpdc_installed = is_package_version_present and is_display_control_service_preinstall_file_present and is_hpdc_preinstall_file_present
            assert is_hpdc_installed, "HPDC service is not install please install it manually"
        except Exception as e:
            logging.error(str(e))
            assert False, "HPDC service is not install please install it manually"
        
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        # verify display modes dropdown
        assert self.fc.fd["display_control"].verify_display_control_display_modes_select_box_ltwo_page() is True,"Display modes dropdown is not present"
        #contrast toggle button should be present
        assert self.fc.fd["display_control"].verify_display_control_contrast_toggle() is True, "Contrast toggle button is not present"
        #Brightness should be present
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 90"
        #HDR toggle button should be off
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
        #Restore to factory settings
        restore_default_button_ltwo_page = self.fc.fd["display_control"].verify_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        assert restore_default_button_ltwo_page == "Restore default", "Restore Default button is not present on the L2 page."
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_control_and_hdr_hdr_while_battery_options_is_unchecked_and_on_ac_mode_C42891429(self):
        self.fc.close_myHP()
        self.fc.open_hdr_settings()
        #HDR options will be displayed
        assert self.fc.fd["display_control"].verify_display_control_use_hdr_in_system_settings() == "Use HDR","HDR settings text is not matching"
        #navigate to batter option and uncheck the "Allow HDR games,videos and apps on battery"
        if bool(self.fc.fd["display_control"].verify_turn_off_hdr_chk_box_in_system_settings()) is False:
            self.fc.fd["display_control"].click_use_hdr_show_more_option_in_system_settings()
        if self.fc.fd["display_control"].get_state_hdr_chk_box_in_system_settings() == "1":
            self.fc.fd["display_control"].click_turn_off_hdr_chk_box_in_system_settings()
        assert self.fc.fd["display_control"].get_state_hdr_chk_box_in_system_settings() == "0", "HDR check box is not unchecked"
        assert self.fc.fd["display_control"].display_control_use_hdr_in_system_settings_is_enabled() == "true"
        self.fc.close_windows_settings_panel()
        #navigate to HPX application and observe HDR option
        self.fc.launch_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "true"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_03_display_control_and_hdr_hdr_while_battery_options_is_checked_and_on_ac_mode_C42891430(self):
        self.fc.close_myHP()
        self.fc.open_hdr_settings()
        #HDR options will be displayed
        assert self.fc.fd["display_control"].verify_display_control_use_hdr_in_system_settings() == "Use HDR","HDR settings text is not matching"
        #navigate to batter option and uncheck the "Allow HDR games,videos and apps on battery"
        if bool(self.fc.fd["display_control"].verify_turn_off_hdr_chk_box_in_system_settings()) is False:
            self.fc.fd["display_control"].click_use_hdr_show_more_option_in_system_settings()
        if self.fc.fd["display_control"].get_state_hdr_chk_box_in_system_settings() == "0":
            self.fc.fd["display_control"].click_turn_off_hdr_chk_box_in_system_settings()
        assert self.fc.fd["display_control"].get_state_hdr_chk_box_in_system_settings() == "1", "HDR check box is not checked"
        assert self.fc.fd["display_control"].display_control_use_hdr_in_system_settings_is_enabled() == "true"
        self.fc.close_windows_settings_panel()
        #navigate to HPX application and observe HDR option
        self.fc.launch_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "true"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_display_control_and_hdr_restore_default_settings_C42891437(self):
        #3.click on the restore Factory settings 
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        #option-3.Prompt to restore to factory settings be opened and below contents will be displayed,a) "Your changes will be removed and all will return to factory default.All application settings will be removed.
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_description_onpopup_window_page() == "Restore the settings to the HP factory defaults?", "Restore default description is not matching"
        # "b) "do not show again" check box will be unchecked
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "0", "Don't show again check box is not unchecked"
        # ,c) Cancel button
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page() == "Cancel", "Cancel button is not present"
        # d) Continue button
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page() == "Continue", "Continue button is not present"
        #click on the continue button
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        #4. the changes will be applied as follows-a)Brightness will be restored to 90
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 80"
        #HDR will be restored to off state
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
        #5.perform random changes to the brightness and the HDR options
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 85)
        self.fc.fd["display_control"].get_focus_on_app("display_control_hdr_toggle_switch_ltwo_page")
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        #The changes will be applied and will be in sync with windows application
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "85", "Brightness slider value is not 85"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle button is not on"
        #click on the restore factory settings button
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        #Prompt to restore  to factory settings be opened and below contents will be displayed-a) "Your changes will be removed and all will return to factory default.All application settings will be removed."
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_description_onpopup_window_page() == "Restore the settings to the HP factory defaults?", "Restore default description is not matching"
        #b) "do not show again" check box will be unchecked
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "0", "Don't show again check box is not unchecked"
        #c) Cancel button
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page() == "Cancel", "Cancel button is not present"
        #d) Continue button
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page() == "Continue", "Continue button is not present"
        #Check the "do not show again" check box
        self.fc.fd["display_control"].click_display_control_restore_defaults_do_not_show_again_checkbox()
        #check box will be display as checked
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "1", "Don't show again check box is not unchecked"
        #click on the continue button
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        #the changes will be applied as follows-a)Brightness will be restored to 90
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 80"
        #HDR will be restored to off state
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
        #perform random changes to the brightness and the HDR option
        self.fc.fd["display_control"].set_slider_value("display_control_brightness_slider_button_ltwo_page", 85)
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")
        #10.click on the restore factory settings button
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        #Prompt to restore  to factory settings will not be opened
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) == False, "Restore default description is visible"
        #the changes will be applied as follows-a)Brightness will be restored to 90
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness slider value is not 80"
        #HDR will be restored to off state
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not off"
