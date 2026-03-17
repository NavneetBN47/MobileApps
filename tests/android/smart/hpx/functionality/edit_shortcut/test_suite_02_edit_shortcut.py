import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_suite_02_Edit_Shortcut:
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

    def test_01_verify_the_behavior_when_the_user_selects_any_value_in_the_copies_dropdown_on_the_edit_print_screen(self):
        """
        Description: C51953725
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable only the 'Print' destination toggle bar.
            6.Click on the 'Copies' dropdown.
            7.Select any other value.
            8.verify the screen.
        Expected Result:
            The selected value should be displayed in 'Copies' dropdown.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
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
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        self.hpx_shortcuts.verify_select_copies_number(copies_number="three")

    def test_02_verify_the_behavior_when_the_user_selects_any_option_in_the_color_dropdown_on_the_edit_print_screen(self):
        """
        Description: C51953726
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable only the 'Print' destination toggle bar.
            6.Click on the 'Color' dropdown.
            7.Select any other value.
            8.verify the screen.
        Expected Result:
            The selected option should be displayed in 'Color' dropdown.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
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
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")

    def test_03_verify_the_behavior_when_the_user_selects_any_option_in_the_two_sided_dropdown_on_the_edit_print_screen(self):
        """
        Description: C51953727
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable only the 'Print' destination toggle bar.
            6.Click on the 'Two-sided' dropdown.
            7.Select any other value.
            8.verify the screen.
        Expected Result:
            The selected option should be displayed in 'Two-sided' dropdown.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
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
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")

    def test_04_verify_the_screen_when_the_user_enables_only_the_email_destination_in_the_edit_shortcut_screen(self):
        """
        Description: C51953730
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable only the 'Email' destination toggle bar.
            6.Click on the continue button.
            7.verify the screen.
        Expected Result:
            User should be navigated to the 'Edit Email' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
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
        is_save_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_save_toggle_btn")
        if is_save_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
            self.hpx_shortcuts.verify_toggle_disabling_confirmation_msg_title(raise_e=False)
            self.hpx_shortcuts.click_toggle_disabling_remove_btn(raise_e=False)
        is_email_toggle_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("edit_shortcut_email_toggle_btn")
        if not is_email_toggle_enabled:
            self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()

    def test_05_verify_the_subject_dropdown_in_edit_email_screen(self):
        """
        Description: C51953736
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Select any option from subject dropdown.
            7.Click on the 'Continue' button.
            8.Verify the behavior.
        Expected Result:
            User should able to view the selected subject in the subject field.
        """
        self.hpx_shortcuts.verify_edit_shortcut_email_subject_label()

    def test_06_verify_the_body_section_of_the_edit_email_screen_when_the_user_modifies_text(self):
        """
        Description: C51953737
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Modify the text in 'Body' section.
            7.Click on the 'Continue' button.
            8.Verify the behavior.
        Expected Result:
            User should able to modify the text in body section and user should be moved forward.
        """
        self.hpx_shortcuts.verify_edit_shortcut_email_body_field()

    def test_07_verify_the_screen_when_the_user_clicks_the_back_button_on_the_edit_email_screen(self):
        """
        Description: C51953731
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer detail screen and click on Shortcuts tile.
            3.Navigate to Shortcuts screen.
            4.Click on the Edit icon.
            5.Enable only the 'Email' destination toggle bar.
            6.Click on the continue button.
            7.Click on the back button in Edit email screen.
            8.verify the screen.
        Expected Result:
            User should be navigated to 'Edit Shortcuts' screen.
        """
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.driver.back()
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()

    def test_08_verify_the_to_section_when_the_user_enters_a_invalid_email_address_in_the_edit_email_screen(self):
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
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_email_screen_title()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_edit_shortcut_invalid_email_id_error_msg()

    def test_09_verify_the_to_section_when_the_user_enters_a_invalid_email_address_in_the_edit_email_screen(self):
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
        assert not self.hpx_shortcuts.is_continue_btn_enabled()

    def test_10_verify_the_to_section_when_the_user_enters_more_than_one_email_address_in_the_edit_email_screen(self):
        """
        Description: C51953734
        Steps:
            1.Install and Launch the HPX app.
            2.Navigate to printer details screen.
            3.Navigate to 'Edit Shortcuts' screen.
            4.Enable only the 'Email' destination toggle bar.
            5.Click on the Continue button.
            6.Enter the more than one email address in 'To' section. (Ex: abc@gmail.com, xyz@yopmail.com)
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

    def test_11_verify_the_screen_when_the_user_enables_only_the_save_destination_in_the_edit_shortcut_screen(self):
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
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
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

    def test_12_verify_the_screen_when_user_clicks_on_back_button_in_edit_print_screen(self):
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
        self.hpx_shortcuts.verify_edit_shortcuts_screen_title()