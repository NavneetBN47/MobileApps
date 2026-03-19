import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_05_Add_Shortcut:
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
    
    def test_01_verify_the_position_of_the_buttons_on_the_delete_this_shortcut_pop_up_window(self):
        """
        Description: C4401
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to Shortcuts screen then click on edit link.
            3.Click on Delete icon on shortcuts screen.
            4.Verify the buttons of delete this shortcut pop up window.
        Expected Result:
            The user should be able to view the delete this shortcut pop up window 
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        assert self.hpx_shortcuts.verify_cancel_this_shortcut_title()

    def test_02_verify_the_screen_when_user_clicks_on_delete_button_in_pop_up_window(self):
        """
        Description: C4402
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to Shortcut edit turn on screen.
            3.Click on Delete icon on shortcuts screen.
            4.Then click on Delete button on delete this shortcut confirmation screen.
            5.Verify the screen.
        Expected Result:
            User should be navigated to the shortcuts screen and deleted shortcuts no longer should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to delete the shortcut since element is not available in the page source
        self.hpx_shortcuts.verify_delete_this_shortcut_title()
        self.hpx_shortcuts.click_delete_shortcut_yes_delete_btn()
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()

    def test_03_verify_the_screen_when_user_clicks_on_the_print_email_and_save_section(self):
        """
        Description: C4403
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Add Shortcuts' screen.
            4.Click on the 'Add New Shortcut' button.
            5.Click on the 'Print, Email and Scan'.
            6.Verify the screen.
        Expected Result:
            User should be redirected to the 'Add Print' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        assert self.hpx_shortcuts.verify_shortcuts_add_print_screen_title()
    
    def test_04_verify_the_screen_when_user_removes_the_print_destination_shortcut(self):
        """
        Description: C4404
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Print shortcut.
            6.Verify the pop up.
        Expected Result:
            Remove this destination?' pop up should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular edit for the created print shortcut button
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
    
    def test_05_verify_the_screen_when_user_clicks_on_the_remove_button_of_print_destination_shortcut(self):
        """
        Description: C4405
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Print shortcut.
            6.Click on the remove button of pop up screen.
            7.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen and selected 'Print' destination should be removed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular edit for the created print shortcut button
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
        self.hpx_shortcuts.click_toggle_disabling_remove_btn()

    def test_06_verify_the_screen_when_user_clicks_on_the_cancel_button_of_print_destination_shortcut(self):
        """
        Description: C4406
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Print shortcut.
            6.Click on the cancel button of pop up screen.
            7.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular edit for the created print shortcut button
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        self.hpx_shortcuts.verify_cancel_this_shortcut_title()
        self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()
    
    def test_07_verify_the_screen_when_user_removes_the_email_destination_shortcut(self):
        """
        Description: C4407
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Email shortcut.
            6.Verify the pop up.
        Expected Result:
            Remove this destination?' pop up should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular email edit for the created email shortcut button

        is_email_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if is_email_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
        else:
            raise AssertionError("Email toggle is not enabled, cannot proceed with the test.")

    def test_08_verify_the_screen_when_user_clicks_on_the_remove_button_of_email_destination_shortcut(self):
        """
        Description: C4408
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Email shortcut.
            6.Click on the remove button of pop up screen.
            7.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen and selected 'Email' destination should be removed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular email edit for the created email shortcut button

        is_email_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if is_email_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
            self.hpx_shortcuts.click_toggle_disabling_remove_btn()
            self.hpx_shortcuts.verify_shortcuts_screen_title()
        else:
            raise AssertionError("Email toggle is not enabled, cannot proceed with the test.")
    
    def test_09_verify_the_screen_when_user_clicks_on_the_cancel_button_of_email_destination_shortcut(self):
        """
        Description: C4409
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Email shortcut.
            6.Click on the cancel button of pop up screen.
            7.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular email edit for the created email shortcut button

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        self.hpx_shortcuts.verify_cancel_this_shortcut_title()
        self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
        assert self.hpx_shortcuts.verify_shortcuts_screen_title()
    
    def test_10_verify_the_screen_when_user_removes_the_save_destination_shortcut(self):
        """
        Description: C4410
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Save shortcut.
            6.Verify the pop up.
        Expected Result:
            Remove this destination?' pop up should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular save edit for the created save shortcut button

        is_save_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if is_save_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
        else:
            raise AssertionError("Save toggle is not enabled, cannot proceed with the test.")
    
    def test_11_verify_the_screen_when_user_clicks_on_the_remove_button_of_save_destination_shortcut(self):
        """
        Description: C51953713
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Save shortcut.
            6.Click on the remove button of pop up screen.
            7.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen and selected 'Save' destination should be removed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular save edit for the created save shortcut button

        is_save_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if is_save_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
            self.hpx_shortcuts.verify_cancel_this_shortcut_title()
            self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
        else:
            raise AssertionError("Save toggle is not enabled, cannot proceed with the test.")
    
    def test_12_verify_the_screen_when_user_clicks_on_the_cancel_button_of_save_destination_shortcut(self):
        """
        Description: C51953714
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Shortcuts' screen.
            4.Click on the edit link.
            5.Click on the Edit icon of the Save shortcut.
            6.Click on the cancel button of pop up screen.
            7.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source
        # Particular save edit for the created save shortcut button

        is_save_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if is_save_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title()
            self.hpx_shortcuts.verify_cancel_this_shortcut_title()
            self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
            self.hpx_shortcuts.verify_cancel_this_shortcut_title()
            self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
            self.hpx_shortcuts.verify_shortcuts_screen_title()
        else:
            raise AssertionError("Save toggle is not enabled, cannot proceed with the test.")
