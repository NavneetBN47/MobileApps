import pytest
from datetime import datetime as Datetime
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_04_Shortcut_Settings(object):

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

    def test_01_verify_the_already_created_shortcut_when_the_user_runs_it_for_the_email_destination(self):
        """
        Description: C51953801
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on the created Shortcuts.
           Run the shortcut.
           Capture a file.
           Click on the 'Next' on detect edges page and click Next.
           Go tp preview screen.
           Click on the Shortcuts button.
           Select Email shortcut.
           Verify the behavior.
        Expected Result:
           Your file is processing' pop up should be dsiplayed.
           Your Shortcut is on its way' pop up should be displayed.
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
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_quick_run_toggle_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.clcik_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"

    def test_02_verify_the_shortcut_settings_screen_with_only_save_option(self):
        """
        Description: C51953802
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add Save' screen.
            Click on the Add to shortcut button.
            Verify the Shortcut settings screen.
        Expected Result:
            The 'File Type' Should be displayed in the 'Shortcut setting' screen.
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
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()

    def test_03_verify_screen_when_user_clicks_back_button_in_shortcut_setting_screen(self):
        """
        Description: C51953803
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

    def test_04_verify_the_shortcut_setting_screen_when_user_enters_a_text_into_the_shortcut_name_field(self):
        """
        Description: C51953804
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

    def test_05_verify_the_shortcut_setting_screen_when_user_enters_a_numerical_value_into_the_shortcut_name_field(self):
        """
        Description: C51953805
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the numerical value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the numerical value into the Shortcut name field without any error.
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

    def test_06_verify_the_shortcut_setting_screen_when_user_enters_alpha_numerical_value_into_the_shortcut_name_field(self):
        """
        Description:C51953806
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the alphanumerical value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the alphanumerical value into the Shortcut name field without any error.
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

    def test_07_verify_the_shortcut_setting_screen_when_user_enters_special_characters_value_into_the_shortcut_name_field(self):
        """
        Description: C51953807
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the special characters value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the special characters value into the Shortcut name field without any error.
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

    def test_08_verify_the_shortcut_setting_screen_when_user_clicks_on_quick_run_toggle(self):
        """
        Description: C51953808
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on 'Quick run' toggle in 'Shortcut setting' screen.
           Verify the Quick run toggle option.
        Expected Result:
           User should be able to select the 'Quick run' toggle in 'Shortcut setting' screen.
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
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("quick_run_toggle_btn")
        if not is_enabled:
            self.hpx_shortcuts.click_quick_run_toggle_btn()
        assert self.hpx_shortcuts.check_toggle_enabled_or_disabled("quick_run_toggle_btn")

    def test_09_verify_shortcut_setting_screen_when_user_clicks_on_smart_file_name_toggle(self):
        """
        Description: C51953809
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on 'Smart file name' toggle in 'Shortcut setting' screen.
           Verify the Quick run toogle option.
        Expected Result:
           User should be able to select the 'Smart file name' toogle in 'Shortcut setting' screen. 
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
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()

    def test_10_verify_shortcut_setting_screen_when_user_clicks_on_desired_color(self):
        """
        Description: C51953810
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on the desired shortcut color in 'Shortcut setting' screen.
           Verify the shortcut color option.
        Expected Result:
           User should be able to select the desired shortcut color in shortcut setting screen.
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
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")   
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")