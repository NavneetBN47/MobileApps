import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_01_Add_Shortcut:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_hpx_flow_setup ,load_printers_session):
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

    def test_01_verify_the_screen_when_user_clicks_on_the_create_your_own_shortcut_arrow_button_in_add_new_shortcuts_screen(self):
        """
        Description: C4374
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on Add new shortcuts in shortcuts screen.
            5.The click on the Create your own shortcut arrow button.
            6.Verify the screen.
        Expected Result:
            User should be navigated to the 'Add shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        assert self.hpx_shortcuts.verify_add_new_shortcut_screen_title()

    def test_02_verify_the_screen_when_user_clicks_on_the_back_button_in_add_shortcut_screen(self):
        """
        Description: C4375
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on Add new shortcuts in shortcuts screen.
            5.Then click on the Create your own shortcut arrow button.
            6.Click on the back button in Add Shortcut screen.
            7.Verify the pop up screen.
        Expected Result:
            Cancel this Shortcut?' pop up window should be displayed.
        """
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
    
    def test_03_verify_the_position_of_the_buttons_on_the_cancel_shortcut_creation_pop_up_window(self):
        """
        Description: C4376
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to the shortcuts screen.
            3.Then click on the Add new shortcut arrow button.
            4.Click on the Create your own shortcut arrow button.
            5.Click on the back button in Add Shortcut screen.
            6.Verify the buttons of cancel shortcut creation pop up window.
            7.Verify the pop up screen.
        Expected Result:
            The position of the buttons on the 'Cancel Shortcut Creation' screen should have 'Yes, cancel' as the primary button and 'Go back' as the secondary button.
        """
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        assert self.hpx_shortcuts.verify_cancel_shortcut_go_back_btn()
    
    def test_04_verify_the_screen_when_the_user_clicks_on_go_back_button(self):
        """
        Description: C4377
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on Add new shortcuts in shortcuts screen.
            5.The click on the Create your own shortcut arrow button.
            6.Click on the back button in Add Shortcut screen.
            7.Click on 'Go back' button on pop up screen.
            8.Verify the screen.
        Expected Result:
            User should be redirected to the 'Add Shortcut' screen.
        """
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        assert self.hpx_shortcuts.verify_add_new_shortcut_title()

    def test_05_verify_the_screen_when_user_clicks_on_the_yes_cancel_button(self):
        """
        Description: C4378
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on Add new shortcuts in shortcuts screen.
            5.The click on the Create your own shortcut arrow button.
            6.Click on the back button in Add Shortcut screen.
            7.Click on 'Yes,cancel' button on pop up screen.
            8.Verify the screen.
        Expected Result:
            User should be redirected to the 'Shortcuts' screen.
        """
        self.hpx_shortcuts.click_cancel_shortcut_go_back_btn()
        self.hpx_shortcuts.verify_cancel_this_shortcut_title()
        self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
    
    def test_06_verify_the_behavior_when_user_enables_the_print_destination_toggle_bar_in_add_shortcut_screen(self):
        """
        Description: C4379
        Steps:
            1.Install and Launch the HPX app.
            2.Click on the printer icon on the root view screen.
            3.Then click on the shortcuts tile on the device details page.
            4.Click on the Add new shortcuts in shortcuts screen.
            5.Then click on the Create your own shortcut arrow button.
            6.Enable the 'Print' destination toggle bar in 'Add Shortcut' screen
            7.Verify the screen.
        Expected Result:
            User should be able to Enable the 'Print' destination toggle bar in 'Add shortcut' screen.
            After enabling the 'Print' destination toggle bar, 'continue' button should be enabled.
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
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        assert self.hpx_shortcuts.is_continue_btn_enabled(), "Continue button should be enabled after toggling print option"
