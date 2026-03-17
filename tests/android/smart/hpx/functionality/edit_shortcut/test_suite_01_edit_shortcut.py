import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_suite_01_Edit_Shortcut:
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

    def test_01_verify_the_edit_shortcut_screen_when_user_clicks_on_edit_icon_in_shortcuts_screen(self):
        """
        Description: C51953715
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Verify the screen.
        Expected Result:
            User should be navigated to the 'Edit shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()

    def test_02_verify_the_screen_when_user_clicks_on_the_back_button_in_edit_shortcut_screen(self):
        """
        Description: C51953716
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Click on Back button.
            6.Verify the screen.
        Expected Result:
            User should be navigated to 'Shortcuts' screen.
        """
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.driver.back()
        self.hpx_shortcuts.verify_shortcuts_screen_title()

    def test_03_verify_the_behavior_when_user_enables_the_print_destination_toggle_bar_in_edit_shortcut_screen(self):
        """
        Description: C51953717
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable the Print destination toggle bar.
            6.Verify the screen.
        Expected Result:
            User should be able to Enable the 'Print' destination toggle bar in 'Edit Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")
        if not is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        assert self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")

    def test_04_verify_the_behavior_when_user_disables_the_print_destination_toggle_bar_in_edit_shortcut_screen(self):
        """
        Description: C51953718
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Disable the Print destination toggle bar.
            6.Verify the screen.
        Expected Result:
            User should be able to Disable the 'Print' destination toggle bar in 'Edit Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")
        if is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        else:
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        assert not self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")

    def test_05_verify_the_behavior_when_user_enables_the_email_destination_toggle_bar_in_edit_shortcut_screen(self):
        """
        Description: C51953719
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable the Email destination toggle bar.
            6.Verify the screen.
        Expected Result:
            User should be able to Enable the 'Email' destination toggle bar in 'Edit Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if not is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        assert self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")

    def test_06_verify_the_behavior_when_user_disables_the_email_destination_toggle_bar_in_edit_shortcut_screen(self):
        """
        Description: C51953720
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Disable the Email destination toggle bar.
            6.Verify the screen.
        Expected Result:
            User should be able to Disable the 'Email' destination toggle bar in 'Edit Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        else:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        assert not self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")

    def test_07_verify_the_behavior_when_user_enables_the_save_destination_toggle_bar_in_edit_shortcut_screen(self):
        """
        Description: C51953721
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Save icon.
            5.Enable the Save destination toggle bar.
            6.Verify the screen.
        Expected Result:
            User should be able to Enable the 'Save' destination toggle bar in 'Edit Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if not is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        assert self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")

    def test_08_verify_the_behavior_when_user_disables_the_save_destination_toggle_bar_in_edit_shortcut_screen(self):
        """
        Description: C51953722
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Disable the save destination toggle bar.
            6.Verify the screen.
        Expected Result:
            User should be able to Disable the 'Save' destination toggle bar in 'Edit Shortcut' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        else:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        assert not self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")

    def test_09_verify_the_screen_when_the_user_enables_only_the_print_destination_in_the_edit_shortcut_screen(self):
        """
        Description: C51953723
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable the print destination toggle bar.
            6.Click on the continue button.
            7.Verify the screen.
        Expected Result:
            User should be navigated to the 'Edit print' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile()
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        # Write click to edit the shortcut since element is not available in the page source

        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_print_toggle_btn")
        if not is_enabled:
            self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_print_screen_title()

    def test_10_verify_the_screen_when_user_clicks_on_back_button_in_edit_print_screen(self):
        """
        Description: C51953724
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable the print destination toggle bar.
            6.Click on the continue button.
            7.Click on the back button in Edit print screen.
            8.Verify the screen.
        Expected Result:
            User should be redirected to the 'Edit Shortcut' screen without any error.
        """
        self.driver.back()
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()