import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_04_Add_Shortcut:
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
    
    def test_01_verify_the_screen_when_the_user_enables_only_the_save_destination_in_the_add_shortcut_screen(self):
        """
        Description: C51953686
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on the Add new shortcuts in shortcuts screen.
            5.Then click on the Create your own shortcut arrow button.
            6.Enable only the 'Save' destination toggle bar in 'Add Shortcut' screen.
            7.Then click on the Continue button.
            8.Verify the screen.
        Expected Result:
            User should be navigated to the 'Add Save' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        assert self.hpx_shortcuts.verify_add_save_shortcut_title()

    def test_02_verify_the_screen_when_user_clicks_on_back_button_in_add_print_screen(self):
        """
        Description: C51953687
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on the Add new shortcuts in shortcuts screen.
            5.Then click on the Create your own shortcut arrow button.
            6.Navigate 'Add save' screen.
            7.Click on the back button.
            8.Verify the screen.
        Expected Result:
            User should be navigated to the 'Add Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_add_save_shortcut_title()
        self.driver.back()
        assert self.hpx_shortcuts.verify_add_new_shortcut_title()

    def test_03_verify_the_screen_when_user_click_on_sign_in_link_of_any_cloud_accounts_under_add_accounts_in_add_save_screen(self):
        """
        Description: C51953688
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on the Add new shortcuts in shortcuts screen.
            5.Then click on the Create your own shortcut arrow button.
            6.Navigate 'Add save' screen.
            7.Click on the 'Sign in' link of any cloud accounts in Add save screen.
            8.Verify the behavior.
        Expected Result:
            User should be able to signed in with the desired cloud accounts.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.verify_add_new_shortcut_title()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_add_save_shortcut_title()
        self.hpx_shortcuts.click_google_drive_signin_link()