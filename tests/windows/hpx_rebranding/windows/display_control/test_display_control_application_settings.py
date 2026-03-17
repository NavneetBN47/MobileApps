import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Display_Control(object):
    
    #this suite should run on all platform
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restore_defaults_for_app_settings_C53000196(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #Display Control module should get open
        assert self.fc.fd["display_control"].verify_display_control_advanced_settings_restore_defaults_button_ltwo_page() == "Restore default", "Restore default button is not present"
        #click restore defaults
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        time.sleep(8)
        #Default value of the system will be applied-br should be 76 mode is neutral
        #click on speaker on task bar to open system brightness value
        if self.platform.lower() == 'bopeep' or self.platform.lower() == 'keelung27':
            assert self.fc.fd["display_control"].get_brightness_slider_value_from_system_tray() == "76", "Brightness value is not 76"
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness value is not 76"
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Mode value is not Neutral"
        if self.platform.lower() == 'willie' or self.platform.lower() == 'thompson' or self.platform.lower() == 'bucky':
            assert self.fc.fd["display_control"].get_brightness_slider_value_from_system_tray() == "90", "Brightness value is not 90"
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness value is not 90"
        if self.platform.lower() == 'willie':
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Mode value is not Default"
        if self.platform.lower() == 'bucky' or self.platform.lower() == 'thompson':
            logging.info("Mode value is not Default")
        if self.platform.lower() == 'keelung32':
            assert self.fc.fd["display_control"].get_brightness_slider_value_from_system_tray() == "36", "Brightness value is not 36"
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "36", "Brightness value is not 36"
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "Mode value is not P3 (D65)"
        #Add any application(Access) from app settings and change the brightness value and add display modes to that application
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        self.fc.fd["display_control"].enter_app_name_in_display_control_add_app_search_bar_ltwo_page("Access")
        self.fc.fd["display_control"].select_display_control_access_app_on_add_application_popup_lthree_page()
        self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
        #The selected application should be added and selected modes should be added
        assert "Access" in self.fc.fd["display_control"].verify_display_control_access_app_ltwo_page(), "Access app is not present"
        if self.platform.lower() == 'bopeep' or self.platform.lower() == 'keelung27':
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Mode value is not Neutral"
        if self.platform.lower() == 'willie':
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Default", "Mode value is not Default"
        if self.platform.lower() == 'keelung32':
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "P3 (D65)", "Mode value is not P3 (D65)"
        if self.platform.lower() == 'bucky' or self.platform.lower() == 'thompson':
            logging.info("Mode value is not Default")
        #Click on Restore default button
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        #Dialogue box will pop-up for the confirmation with three options and the check box,1. "Do not show again" check box default it is not checked,2.Continue button,3.Cancel button,4. 'x' (close) button at the top right--"X"btn not on this popup
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "0", "Don't show again check box is not unchecked"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_cancel_onpopup_window_ltwo_page() == "Cancel", "Cancel button is not present"
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_ltwo_page() == "Continue", "Continue button is not present"
        #Click on the Cancel button
        self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_ltwo_page()
        #Dialogue box will get close and Restore default functionality will not apply
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) == False, "Restore default description is visible"
        assert bool(self.fc.fd["display_control"].is_display_control_access_app_ltwo_page_visible()) == True, "Access app is not present"
        #Click on Restore default button
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        #Dialogue box will pop-up
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) == True, "Restore default description is not visible"
        self.fc.fd["display_control"].click_display_control_restore_defaults_do_not_show_again_checkbox()
        assert self.fc.fd["display_control"].verify_display_control_restore_defaults_do_not_show_again_checkbox() == "1", "Don't show again check box is not checked"
        #Click on the Continue button-Enable Do not show again checkbox
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        #Dialogue box will get close and Restore default functionality will apply,Able to check the do not show again checkbox
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) == False, "Restore default description is visible"
        if self.platform.lower() == 'bopeep' or self.platform.lower() == 'keelung27':
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "76", "Brightness value is not 76"
        if self.platform.lower() == 'willie' or self.platform.lower() == 'thompson' or self.platform.lower() == 'bucky':
            assert self.fc.fd["display_control"].get_brightness_slider_value() == "90", "Brightness value is not 90"
        if self.platform.lower() == 'keelung32':
            assert self.fc.fd["display_control"].get_brightness_slider_value_from_system_tray() == "36", "Brightness value is not 36"
        #Again Click on restore default button-Restore default will be applied without the dialogue box,Note: Need to Re-install the application for next dailogue box
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        assert bool(self.fc.fd["display_control"].is_display_control_restore_defaults_description_onpopup_window_page_visible()) == False, "Restore default description is visible"

    #bopeep only
    @pytest.mark.ota
    def test_02_launch_selected_application_in_appsettings_bar_C53000190(self):
        if self.platform.lower() == 'bopeep':
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            self.fc.fd["display_control"].scroll_down_display_modes_list_window()
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_neutral_ltwo_page")
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Display mode is not neutral"
            assert self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page(), "Add app button is not present"
            self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
            time.sleep(2)# Give UI a chance to update
            assert self.fc.fd["display_control"].verify_display_control_calculator_app_on_add_application_popup_lthree_page(), "Calculator is not present. Verify that add application pop up opened" #also validates that add application popup appeared

            self.fc.fd["display_control"].select_display_control_calculator_app_on_add_application_popup_lthree_page()
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            assert self.fc.fd["display_control"].verify_display_control_calculator_app_ltwo_page(), "Calculator app not found"
            
            self.fc.fd["display_control"].click_display_control_calculator_app_ltwo_page()
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            self.fc.fd["display_control"].scroll_modes_native(direction="down",desired_mode_name="Native",desired_mode_id="display_modes_select_box_option_native_ltwo_page")
            self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
            self.fc.fd["display_control"].click_title_bar()
            time.sleep(2)
            self.fc.fd["display_control"].click_display_mode_select_mode_ltwo_page("display_modes_select_box_option_native_ltwo_page")
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Display mode is not native"
            self.fc.fd["display_control"].set_slider_value(slider = "display_control_brightness_slider_button_ltwo_page", desired_value = 75)
            brightness_value = self.fc.fd["display_control"].get_brightness_slider_value()
            assert brightness_value == "75", "Brightness value is not 75. Brightness value is {}".format(brightness_value)
            self.fc.fd["display_control"].get_focus_on_app("display_control_contrast_toggle")
            self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
            self.fc.fd["display_control"].set_slider_value(slider = "display_control_contrast_slider_lthree_page", desired_value = 50)
            calculator_contrast = self.fc.fd["display_control"].get_contrast_slider_value()
            assert calculator_contrast == "50", "Contrast value is not 50. Contrast value is {}".format(calculator_contrast)
            self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
            default_red = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
            default_green = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
            default_blue = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
            assert default_red == "100", "Red value is not 100. Red value is {}".format(default_red)
            assert default_green == "100", "Green value is not 100. Green value is {}".format(default_green)
            assert default_blue == "100", "Blue value is not 100. Blue value is {}".format(default_blue)
            self.fc.swipe_window(direction="up", distance=4)
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()

            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            assert brightness_value == "75", "Brightness value is not 75. Brightness value is {}".format(brightness_value)
            self.fc.fd["display_control"].click_display_control_advanced_settings_arrow_ltwo_page()
            self.fc.swipe_window(direction="down", distance=4)
            assert calculator_contrast == "50", "Contrast value is not 50. Contrast value is {}".format(calculator_contrast)
            assert default_red == "100", "Red value is not 100. Red value is {}".format(default_red)
            assert default_green == "100", "Green value is not 100. Green value is {}".format(default_green)
            assert default_blue == "100", "Blue value is not 100. Blue value is {}".format(default_blue)
            self.fc.swipe_window(direction="up", distance=4)
            # Restore defaults and return to basic settings page for next test
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
            self.fc.swipe_window(direction="up", distance=6)
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()

    #bopeep only
    @pytest.mark.ota
    def test_03_first_launch_C53000187(self):
        if self.platform.lower() == 'bopeep':
            self.fc.restart_myHP() # Test case is looking for values after a fresh launch
            assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=6)
          
            display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
            assert display_card_lone_page == "Display","Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
            time.sleep(3)
            # Context aware UI should visible below the Display title
            # a) Global application should be highlighted
            assert bool(self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()) is True, "All Applications button is not present"
            assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page_selected() == "true", "Global application is not selected"

            # b) OOB application should show if installed
            assert "Disney+" in self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
            assert "腾讯视频" in self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
            # c) Add application button should be visible with " +
            assert self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page(), "Add application button is not present"
            # Default Display modes should be selected
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Neutral", "Display mode is not neutral"
            default_brightness = self.fc.fd["display_control"].get_brightness_slider_value()
            assert default_brightness == "76", "Brightness value is not 76. Brightness value is {}".format(default_brightness)

            self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
            if bool(self.fc.fd["display_control"].verify_display_control_advanced_display_settings_title_lthree_page()) is False:
                self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()

            default_red = self.fc.fd["display_control"].get_display_control_low_blue_light_red_slider_lthree_page()
            default_green = self.fc.fd["display_control"].get_display_control_low_blue_light_green_slider_lthree_page()
            default_blue = self.fc.fd["display_control"].get_display_control_low_blue_light_blue_slider_lthree_page()
            assert default_red == "100", "Red value is not 100. Red value is {}".format(default_red)
            assert default_green == "100", "Green value is not 100. Green value is {}".format(default_green)
            assert default_blue == "100", "Blue value is not 100. Blue value is {}".format(default_blue)
    
            self.fc.swipe_window(direction="down", distance=6)
            self.fc.fd["display_control"].verify_display_control_restore_defaults_button_lthree_page(), "Restore defaults button not found"
        
    @pytest.mark.ota
    def test_04_display_control_and_app_settings_add_any_application_C53000189(self):
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
            time.sleep(2)# Give UI a chance to update
            assert self.fc.fd["display_control"].verify_display_control_calculator_app_on_add_application_popup_lthree_page(), "Calculator is not present. Verify that add application pop up opened" #also validates that add application popup appeared
            #click/select  camera app in application window
            self.fc.fd["display_control"].click_camera_app_on_install_modal()
            assert self.fc.fd["display_control"].verify_focus_on_element("camera_app_on_install_modal") == "true", "Camera app is not selected"
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            # Application is added to List and added application is highlighted in the list
            assert "Camera" in self.fc.fd["display_control"].verify_app_name_on_carousel("camera_app_carousel"), "Camera app is not visible in the carousel"
            assert self.fc.fd["display_control"].verify_app_carousel_isSelected("camera_app_carousel") == "true", "Camera app is not selected in the carousel"
            print("selection status=", self.fc.fd["display_control"].verify_app_carousel_isSelected("camera_app_carousel"))

