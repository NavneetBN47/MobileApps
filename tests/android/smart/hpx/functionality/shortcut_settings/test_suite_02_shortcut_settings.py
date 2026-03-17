import pytest
from datetime import datetime as Datetime
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_02_Shortcut_Settings(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_the_screen_when_the_user_clicks_the_save_shortcut_button_after_selecting_settings_from_the_shortcut_settings_screen(self):
        """
        Description: C51953782
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add print' screen.
            Click on the Add to shortcut button.
            Select the desired settings from shortcut setting screen.
            Click on the Save shortcut button.
            Verify the screen.
        Expected Result:
            User shoul be able to save the desired settings successfully without any issue.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        assert self.hpx_shortcuts.verify_select_copies_number(copies_number="three")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")  
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_done_btn()
        assert self.hpx_shortcuts.verify_shortcut_present_in_list(shortcut_name), f"The created shortcut '{shortcut_name}' should be present in the shortcuts list"

    def test_02_verify_the_screen_when_the_user_clicks_on_run_this_shortcut_button(self):
        """
        Description: C51953783
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add print' screen.
            Click on the Add to shortcut button.
            Select the desired settings from shortcut setting screen.
            Click on the Save shortcut button.
            Click on Run this Shortcut button.
            Verify the screen.
        Expected Result:
            User should be navigated to the 'Select a source' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        assert self.hpx_shortcuts.verify_select_copies_number(copies_number="three")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")  
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        assert self.camera_scan.verify_select_scan_source_screen(), "scan source screen should be displayed after clicking 'Run this Shortcut' button"

    def test_03_verify_screen_when_user_clicks_shortcuts_button(self):
        """
        Description: C51953784
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add print' screen.
            Click on the Add to shortcut button.
            Select the desired settings from shortcut setting screen.
            Click on the Save shortcut button.
            Click on Shortcuts button.
            Verify the screen.
        Expected Result:
            The Shortcut should be saved and user should be navigated to the Shortcuts screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        assert self.hpx_shortcuts.verify_select_copies_number(copies_number="three")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")  
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_done_btn()
        assert self.hpx_shortcuts.verify_shortcut_present_in_list(shortcut_name), f"The created shortcut '{shortcut_name}' should be present in the shortcuts list"
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_04_verify_already_created_shortcut_when_user_runs_it_for_print_destination(self):
        """
        Description: C51953785
            Install and Launch the HPX app..Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on the created Shortcuts.
            Run the shortcut.
            Capture a file.
            Click on the 'Next' on detect edges page and click Next.
            Go to preview screen.
            Click on the Shortcuts button.
            Select Print shortcut.
            Verify the behavior.
        Expected Result:
            The shortcuts should be sent and printed successfully and also Your file is processing pop up should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_quick_run_toggle_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"

    def test_05_verify_shortcut_settings_screen_with_only_email_option(self):
        """
        Description: C51953786
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add Email' screen.
           Click on the Add to shortcut button.
           Verify the Shortcut settings screen.
        Expected Result:
           The 'File Type' Should not be displayed in the 'Shortcut setting' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        # self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()
        assert not self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen(), '"File Type" should not be present on the screen'

    def test_06_verify_the_screen_when_user_clicks_on_the_back_button_in_shortcut_setting_screen(self):
        """
        Description: C51953787
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen and click on Add to shortcut button.
           Click on the back button.
           Verify the screen.
        Expected Result:
           User should be redirected to the 'Add Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.driver.back()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()

    def test_07_verify_the_shortcut_setting_screen_when_user_enters_a_text_into_the_shortcut_name_field(self):
        """
        Description: C51953788
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the text into the shortcut name field.
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the text into the Shortcut name field without any error.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="shortcut test")
        assert self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(),'"Save Shortcut" button should be enabled when the shortcut name is entered'

    def test_08_verify_the_shortcut_setting_screen_when_user_enters_a_numerical_value_into_the_shortcut_name_field(self):
        """
        Description: C51953789
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the numerical value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the text into the Shortcut name field without any error.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="12345678")
        assert self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(),'"Save Shortcut" button should be enabled when the shortcut name is entered'

    def test_09_verify_the_shortcut_setting_screen_when_user_enters_a_alphanumerical_value_into_the_shortcut_name_field(self):
        """
        Description: C51953790
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the alphanumerical value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the text into the Shortcut name field without any error.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="A1b2c3")
        assert self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(),'"Save Shortcut" button should be enabled when the shortcut name is entered'

    def test_10_verify_shortcut_setting_screen_with_special_characters_in_shortcut_name(self):
        """
        Description: C51953791
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the special characters value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should not able to enter the text into the Shortcut name field without any error.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="!@#%$^&*")
        assert not self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(), '"Save Shortcut" button should be disabled when the special character shortcut name is entered'