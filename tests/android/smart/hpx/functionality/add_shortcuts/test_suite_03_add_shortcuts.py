import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_03_Add_Shortcut:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        # Enable HPX Flag
        cls.fc.hpx = True
    
    def test_01_verify_the_screen_when_the_user_enables_only_the_email_destination_in_the_add_shortcut_screen(self):
        """
        Description: C51953678
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on the Add new shortcuts in shortcuts screen.
            5.Then click on the Create your own shortcut arrow button.
            6.Enable only the 'Email' destination toggle bar in 'Add Shortcut' screen.
            7.Then click on the Continue button.
            8.Verify the screen.
        Expected Result:
            User should be navigated to the 'Add Email' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
    
    def test_02_verify_the_screen_when_the_user_clicks_the_back_button_on_the_add_print_screen(self):
        """
        Description: C51953679
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Click on the back button in Add email screen.
            7.verify the behavior.
        Expected Result:
            User should be redirected to the 'Add Shortcut' screen without any error.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.driver.back()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
    
    def test_03_verify_the_to_section_when_the_user_enters_a_valid_email_address_in_the_add_email_screen(self):
        """
        Description: C51953680
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter the valid email address in 'To' section.
            7.Click on the 'Add to Shortcut' button.
            8.Verify the behavior.
        Expected Result:
            User should be redirected to the 'Add Shortcut' screen with saved details from 'Add email' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field("test@example.com")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_04_verify_the_to_section_when_the_user_enters_a_invalid_email_address_in_the_add_email_screen(self):
        """
        Description: C51953681
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter the invalid email address in 'To' section.
            7.Click on the 'Add to Shortcut' button.
            8.Verify the behavior.
        Expected Result:
            Error message should be displayed and the user should not be able to move forward.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field("test@.com")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_invalid_email_id_error_msg()
    
    def test_05_verify_the_to_section_when_the_user_enters_more_than_one_email_address_in_the_add_email_screen(self):
        """
        Description: C51953682
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter more than one email address in 'To' section.
            7.Click on the 'Add to Shortcut' button.
            8.Verify the behavior.
        Expected Result:
            User should be redirected to the 'Add Shortcut' screen with saved details from 'Add email' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field("test@gmail.com, test2@gmail.com")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()
    
    def test_06_verify_the_to_section_when_the_user_enters_more_than_20_email_address_in_the_add_email_screen(self):
        """
        Description: C51953683
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter more than 20 email address in 'To' section.
            7.Click on the 'Add to Shortcut' button.
            8.Verify the behavior.
        Expected Result:
            Error message should be displayed and the user should not be able to move forward.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field("test@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com, test2@gmail.com")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()
    
    def test_07_verify_the_body_section_of_the_add_email_screen_when_the_user_modifies_text(self):
        """
        Description: C51953685
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Modify the text in 'Body' section.
            7.Click on the 'Add to Shortcut' button.
            8.Verify the behavior.
        Expected Result:
            User should able to modify the text in body section and user should be moved forward.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field("test@gmail.com")
        self.hpx_shortcuts.enter_edit_shortcut_email_body_field("This is the sample body message for testing")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()