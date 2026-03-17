import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_suite_03_Edit_Shortcut:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_hpx_flow_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_hpx_flow_setup
        cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        # Enable HPX Flag
        cls.fc.hpx = True
    
    def test_01_verify_the_to_section_when_the_user_enters_a_invalid_email_address_in_the_edit_email_screen(self):
        """
        Description: C51953732
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable only the 'Email' destination toggle bar.
            6.Click on the continue button.
            7.Enter the Invalid email address in 'To' section and click on continue button.
            8.verify the screen.
        Expected Result:
            User should be redirected to the 'Edit Shortcut' screen with saved details from 'Edit email' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        assert self.hpx_shortcuts.verify_edit_shortcut_invalid_email_id_error_msg()
    
    def test_02_verify_the_to_section_when_the_user_enters_a_invalid_email_address_in_the_edit_email_screen(self):
        """
        Description: C51953733
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter the invalid email Address in 'To' section.
            7.Click on the 'Continue' button.
            8.Verify the behavior.
        Expected Result:
            Error message should be displayed and the user should not be able to move forward.
        """
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        assert self.hpx_shortcuts.is_continue_btn_enabled() == 'false'
    
    def test_03_verify_the_to_section_when_the_user_enters_more_than_one_email_address_in_the_edit_email_screen(self):
        """
        Description: C51953734
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter the more than one email address in 'To' section.
            7.Click on the 'Continue' button.
            8.Verify the behavior.
        Expected Result:
            User should be redirected to the 'Edit Shortcut' screen with saved details from 'Edit email' screen.
        """
        self.driver.back()
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        if not is_email_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field("testqama@gmail.com, testqama3@gmail.com")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_04_verify_the_screen_when_the_user_enables_only_the_save_destination_in_the_edit_shortcut_screen(self):
        """
        Description: C51953739
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Save' destination toggle bar.
            5.Then click on the Continue button.
            6.Verify the screen.
        Expected Result:
            User should be navigated to the 'Edit Save' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_print_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")
        if is_print_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        is_email_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if is_email_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        is_save_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if not is_save_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        assert self.hpx_shortcuts.verify_shortcut_edit_save_title()

    def test_05_verify_the_screen_when_user_clicks_on_back_button_in_edit_print_screen(self):
        """
        Description: C51953740
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Save' destination toggle bar.
            5.Then click on the Continue button.
            6.Click on the back button in edit save screen.
            6.Verify the screen.
        Expected Result:
            User should be navigated to the 'Edit Shortcut' screen.
        """
        self.hpx_shortcuts.verify_shortcut_edit_save_title()
        self.driver.back()
        assert self.hpx_shortcuts.verify_edit_shortcuts_screen_title()

    def test_06_verify_the_screen_when_user_clicks_on_sign_in_link_of_any_cloud_accounts_under_add_accounts_in_edit_save_screen(self):
        """
        Description: C51953741
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Save' destination toggle bar.
            6.Navigate 'Edit save' screen.
            7.Click on the 'Sign in' link of any cloud accounts in Edit save screen.
            8.Verify the behavior.
        Expected Result:
            User should be redirected to the 'Sign In' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_print_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")
        if is_print_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        is_email_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if is_email_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        is_save_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if not is_save_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_shortcut_edit_save_title()
        self.hpx_shortcuts.click_google_drive_signin_link()
    
    def test_07_verify_the_confirmation_dialog_when_user_deletes_the_shortcut(self):
        """
        Description: C51953754
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to Shortcuts screen then click on edit link.
            3.Click on Delete icon on shortcuts screen.
            4.Verify the screen.
        Expected Result:
            The 'Delete this shortcut' confirmation dialog should be displayed as shown in the screen below.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to delete the shortcut since element is not available in the page source

        assert self.hpx_shortcuts.verify_delete_shortcut_confirmation_msg_title()

    def test_08_verify_the_position_of_the_buttons_on_the_delete_this_shortcut_pop_up_window(self):
        """
        Description: C51953755
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to Shortcuts screen then click on edit link.
            3.Click on Delete icon on shortcuts screen.
            4.Verify the buttons of delete this shortcut pop up window.
        Expected Result:
            Verify the Delete this shortcut pop up window shows
        """
        assert self.hpx_shortcuts.verify_delete_shortcut_yes_delete_btn()

    def test_09_verify_the_screen_when_user_clicks_on_cancel_button_in_pop_up_window(self):
        """
        Description: C51953757
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to Shortcut edit turn on screen.
            3.Click on Delete icon on shortcuts screen.
            4.Click on cancel button.
            5.Verify the screen.
        Expected Result:
            User should be navigated to the 'Edit Shortcuts' screen.
        """
        self.hpx_shortcuts.click_delete_shortcut_no_cancel_btn()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()

    def test_10_verify_the_screen_when_user_clicks_on_delete_button_in_pop_up_window(self):
        """
        Description: C51953756
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to Shortcut edit turn on screen.
            3.Click on Delete icon on shortcuts screen.
            4.Then click on Delete button on delete this shortcut confirmation screen.
            5.Verify the screen.
        Expected Result:
            User should be navigated to the shortcuts screen and deleted shortcuts no longer should be displayed.
        """
        # Write click to delete the shortcut since element is not available in the page source
        self.hpx_shortcuts.click_delete_shortcut_yes_delete_btn()
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()