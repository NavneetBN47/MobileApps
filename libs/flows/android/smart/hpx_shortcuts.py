from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time
import logging

class HpxShortcuts(SmartFlow):
    flow_name = "hpx_shortcuts"

    def verify_shortcuts_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Shortcuts screen.
        """
        self.driver.wait_for_object("shortcuts_screen_title", timeout=timeout, raise_e=raise_e)

    def click_shortcuts_edit_btn(self, timeout=10, raise_e=True):
        """
        Click the Edit button on the Shortcuts screen.
        """
        self.driver.wait_for_object("shortcuts_edit_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_edit_shortcuts_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("edit_shortcuts_screen_title", timeout=timeout, raise_e=raise_e)

    def click_cancel_shortcut_yes_cancel_btn(self, timeout=10, raise_e=True):
        """
        Click the Yes Cancel button on the Cancel Shortcut dialog.
        """
        self.driver.wait_for_object("cancel_shortcut_yes_cancel_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_cancel_shortcut_yes_cancel_btn(self, timeout=10, raise_e=True):
        """
        Click the Yes Cancel button on the Cancel Shortcut dialog.
        """
        self.driver.wait_for_object("cancel_shortcut_yes_cancel_btn", timeout=timeout)

    def click_edit_shortcut_print_toggle_btn(self, timeout=10, raise_e=True, enable=True):
        """
        Click the Print toggle button on the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("edit_shortcut_print_toggle_btn", timeout=timeout, raise_e=raise_e).click()

    def check_toggle_enabled_or_disabled(self, locator, raise_e=True, timeout=10):
        """
        Check if the toggle is enabled or disabled.
        :param locator: The locator of the toggle element.
        :param raise_e: Whether to raise an exception if the toggle is not found.
        :param timeout: The time to wait for the toggle to be found.
        :return: True if the toggle is enabled, False if it is disabled.
        """
        return self.driver.get_attribute(locator, "enabled", timeout=timeout, raise_e=raise_e)

    def verify_toggle_disabling_confirmation_msg_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Toggle Disabling Confirmation message.
        """
        self.driver.wait_for_object("toggle_disabling_confirmation_msg_title", timeout=timeout, raise_e=raise_e)

    def click_toggle_disabling_remove_btn(self, timeout=10, raise_e=True):
        """
        Click the Remove button on the Toggle Disabling Confirmation message.
        """
        self.driver.wait_for_object("toggle_disabling_remove_btn", timeout=timeout, raise_e=raise_e).click()

    def click_toggle_disabling_cancel_btn(self, timeout=10, raise_e=True):
        """
        Click the Cancel button on the Toggle Disabling Confirmation message.
        """
        self.driver.wait_for_object("toggle_disabling_cancel_btn", timeout=timeout, raise_e=raise_e).click()

    def click_edit_shortcut_email_toggle_btn(self, timeout=10, raise_e=True, enable=True):
        """
        Click the Email toggle button on the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("edit_shortcut_email_toggle_btn", timeout=timeout, raise_e=raise_e).click()

    def click_edit_shortcut_save_toggle_btn(self, timeout=10, raise_e=True):
        """
        Click the Save button on the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("edit_shortcut_save_toggle_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_edit_print_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Edit Print screen.
        """
        self.driver.wait_for_object("edit_print_screen_title", timeout=timeout, raise_e=raise_e)

    def click_edit_shortcut_continue_btn(self, timeout=10, raise_e=True):
        """
        Click the Continue button on the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("continue_btn", timeout=timeout, raise_e=raise_e).click()

    def is_continue_btn_enabled(self, timeout=10, raise_e=True):
        """
        Check if the Continue button is enabled on the Edit Shortcuts screen.
        :return: True if the Continue button is enabled, False otherwise.
        """
        return self.driver.get_attribute("continue_btn", "enabled", timeout=timeout, raise_e=raise_e)

    def click_edit_print_copies_dropdown_btn(self, timeout=10, raise_e=True):
        """
        Click the Copies dropdown button on the Edit Print screen.
        """
        self.driver.wait_for_object("edit_print_copies_dropdown_btn", timeout=timeout, raise_e=raise_e).click()

    def click_select_color_dropdown_btn(self, timeout=10, raise_e=True):
        """
        Click the Color dropdown button on the Edit Print screen.
        """
        self.driver.wait_for_object("select_color_dropdown_btn", timeout=timeout, raise_e=raise_e).click()

    def click_two_sided_dropdown_btn(self, timeout=10, raise_e=True):
        """
        Click the Two-Sided dropdown button on the Edit Print screen.
        """
        self.driver.wait_for_object("two_sided_dropdown_btn", timeout=timeout, raise_e=raise_e).click()

    def select_copies_number(self, copies_number, timeout=10, raise_e=True):
        """
        Select the number of copies on the Edit Print screen.
        :param copies_number: The number of copies to select.
        """
        locator = f"select_copies_{copies_number}_dropdown_item"
        self.driver.wait_for_object(locator, timeout=timeout, raise_e=raise_e).click()

    def verify_select_copies_number(self, copies_number, timeout=10, raise_e=True):
        """
        Verify the selected number of copies on the Edit Print screen.
        :param copies_number: The number of copies to verify.
        """
        locator = f"select_copies_{copies_number}_dropdown_item"
        return self.driver.get_attribute(locator, "selected", timeout=timeout, raise_e=raise_e)

    def select_color_option(self, color_option, timeout=10, raise_e=True):
        """
        Select the color option on the Edit Print screen.
        :param color_option: The color option to select "color" or "grayscale".
        """
        locator = f"select_color_dropdown_item_{color_option}"
        self.driver.wait_for_object(locator, timeout=timeout, raise_e=raise_e).click()

    def verify_select_color_option(self, color_option, timeout=10, raise_e=True):
        """
        Verify the selected color option on the Edit Print screen.
        :param color_option: The color option to verify "color" or "grayscale".
        """
        locator = f"select_color_dropdown_item_{color_option}"
        return self.driver.get_attribute(locator, "selected", timeout=timeout, raise_e=raise_e)

    def select_two_sided_option(self, two_sided_option, timeout=10, raise_e=True):
        """
        Select the two-sided option on the Edit Print screen.
        :param two_sided_option: The two-sided option to select
            off
            short_edge
            long_edge.
        """
        locator = f"select_two_sided_dropdown_item_{two_sided_option}"
        self.driver.wait_for_object(locator, timeout=timeout, raise_e=raise_e).click()

    def verify_select_two_sided_option(self, two_sided_option, timeout=10, raise_e=True):
        """
        Verify the selected two-sided option on the Edit Print screen.
        :param two_sided_option: The two-sided option to verify
            off
            short_edge
            long_edge.
        """
        locator = f"select_two_sided_dropdown_item_{two_sided_option}"
        return self.driver.get_attribute(locator, "selected", timeout=timeout, raise_e=raise_e)

    def verify_edit_shortcut_email_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Edit Shortcut Email screen.
        """
        self.driver.wait_for_object("edit_shortcut_email_screen_title", timeout=timeout, raise_e=raise_e)

    def enter_edit_shortcut_email_receiver_email_id_field(self, email_id, timeout=10, raise_e=True):
        """
        Enter the receiver's email ID in the Edit Shortcut Email screen.
        :param email_id: The email ID to enter.
        """
        self.driver.wait_for_object("edit_shortcut_email_receiver_email_id_field", timeout=timeout, raise_e=raise_e).send_keys(email_id)

    def verify_edit_shortcut_invalid_email_id_error_msg(self, timeout=10, raise_e=True):
        """
        Verify the invalid email ID error message on the Edit Shortcut Email screen.
        """
        self.driver.wait_for_object("edit_shortcut_invalid_email_id_error_msg", timeout=timeout, raise_e=raise_e)

    def verify_shortcut_settings_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Shortcut Settings screen.
        """
        self.driver.wait_for_object("shortcut_settings_screen_title", timeout=timeout, raise_e=raise_e)

    def verify_edit_shortcut_email_subject_label(self, timeout=10, raise_e=True):
        """
        Verify the label of the Email Subject field on the Edit Shortcut Email screen.
        """
        self.driver.wait_for_object("edit_shortcut_email_subject_label", timeout=timeout, raise_e=raise_e)

    def enter_edit_shortcut_email_subject_field(self, subject, timeout=10, raise_e=True):
        """
        Enter the subject in the Email Subject field on the Edit Shortcut Email screen.
        :param subject: The subject to enter.
        """
        self.driver.wait_for_object("edit_shortcut_email_subject_field", timeout=timeout, raise_e=raise_e).send_keys(subject)

    def verify_edit_shortcut_email_body_field(self, timeout=10, raise_e=True):
        """
        Verify the Email Body field on the Edit Shortcut Email screen.
        """
        self.driver.wait_for_object("edit_shortcut_email_body_field", timeout=timeout, raise_e=raise_e)

    def enter_edit_shortcut_email_body_field(self, body, timeout=10, raise_e=True):
        """
        Enter the body in the Email Body field on the Edit Shortcut Email screen.
        :param body: The body to enter.
        """
        self.driver.wait_for_object("edit_shortcut_email_body_field", timeout=timeout, raise_e=raise_e).send_keys(body)

    def verify_shortcut_edit_save_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Shortcut Edit Save screen.
        """
        self.driver.wait_for_object("shortcut_edit_save_title", timeout=timeout, raise_e=raise_e)
    
    def verify_shortcuts_edit_btn(self, timeout=10, raise_e=True):
        """
        Verify the presence of the Edit button on the Shortcuts screen.
        """
        return self.driver.wait_for_object("shortcuts_edit_btn", timeout=timeout, raise_e=raise_e)
    
    def click_shortcuts_settings_icon(self, timeout=10, raise_e=True):
        """
        Click the settings button on the Shortcuts screen.
        """
        self.driver.wait_for_object("settings_icon", timeout=timeout, raise_e=raise_e).click()

    def verify_add_new_shortcut_btn(self, timeout=10, raise_e=True):
        """
        Verify the presence of the Add New Shortcut button on the Shortcuts screen.
        """
        return self.driver.wait_for_object("add_new_shortcut_btn", timeout=timeout, raise_e=raise_e)
    
    def click_add_new_shortcut_btn(self, timeout=10, raise_e=True):
        """
        Click the Add New Shortcut button on the Shortcuts screen.
        """
        self.driver.wait_for_object("add_new_shortcut_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_add_new_shortcut_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Add New Shortcut screen.
        """
        self.driver.wait_for_object("add_new_shortcut_screen_title", timeout=timeout, raise_e=raise_e)

    def click_shortcuts_back_btn(self, timeout=10, raise_e=True):
        """
        Click the back button on the Shortcuts screen.
        """
        self.driver.wait_for_object("shortcuts_back_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_shortcuts_email_btn(self, timeout=10, raise_e=True):
        """
        Verify the presence of the Email button on the Shortcuts screen.
        """
        return self.driver.wait_for_object("shortcuts_email_btn", timeout=timeout, raise_e=raise_e)
    
    def click_create_your_own_shortcut(self, timeout=10, raise_e=True):
        """
        Click the Create Your Own Shortcut on the Shortcuts screen.
        """
        self.driver.wait_for_object("create_your_own_shortcut", timeout=timeout, raise_e=raise_e).click()

    def click_cancel_shortcut_go_back_btn(self, timeout=10, raise_e=True):
        """
        Click the Go Back button on the Cancel Shortcut dialog.
        """
        self.driver.wait_for_object("cancel_shortcut_go_back_btn", timeout=timeout, raise_e=raise_e).click()
    
    def verify_cancel_shortcut_go_back_btn(self, timeout=10, raise_e=True):
        """
        Verify the Go Back button on the Cancel Shortcut dialog.
        """
        return self.driver.wait_for_object("cancel_shortcut_go_back_btn", timeout=timeout, raise_e=raise_e).is_displayed()

    def click_google_drive_signin_link(self, timeout=10, raise_e=True):
        """
        Click the Google Drive Sign In link on the Edit Shortcut Email screen.
        """
        self.driver.wait_for_object("google_drive_signin_link", timeout=timeout, raise_e=raise_e).click()

    def verify_google_drive_redirection(self, timeout=10, raise_e=True):
        """
        Verify the redirection to Google Drive Sign In page.
        """
        self.driver.wait_for_object("google_drive_redirection", timeout=timeout, raise_e=raise_e)

    def verify_delete_shortcut_confirmation_msg_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Delete Shortcut Confirmation message.
        """
        self.driver.wait_for_object("delete_shortcut_confirmation_msg_title", timeout=timeout, raise_e=raise_e)

    def click_delete_shortcut_yes_delete_btn(self, timeout=10, raise_e=True):
        """
        Click the Yes Delete button on the Delete Shortcut Confirmation message.
        """
        self.driver.wait_for_object("delete_shortcut_yes_delete_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_delete_shortcut_yes_delete_btn(self, timeout=10, raise_e=True):
        """
        Verify the Yes Delete button on the Delete Shortcut Confirmation message.
        """
        self.driver.wait_for_object("delete_shortcut_yes_delete_btn", timeout=timeout, raise_e=raise_e).is_displayed()

    def click_delete_shortcut_no_cancel_btn(self, timeout=10, raise_e=True):
        """
        Click the No Cancel button on the Delete Shortcut Confirmation message.
        """
        self.driver.wait_for_object("delete_shortcut_no_cancel_btn", timeout=timeout, raise_e=raise_e).click()
    
    def verify_add_new_shortcut_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Add New Shortcut screen.
        """
        self.driver.wait_for_object("add_new_shortcut_title", timeout=timeout, raise_e=raise_e)

    def verify_cancel_this_shortcut_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Cancel This Shortcut dialog.
        """
        self.driver.wait_for_object("cancel_this_shortcut_title", timeout=timeout, raise_e=raise_e)

    def verify_shortcuts_add_print_screen_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Shortcuts Add Print screen.
        """
        self.driver.wait_for_object("shortcuts_add_print_screen_title", timeout=timeout, raise_e=raise_e)
    
    def click_hpx_quick_run_radio_btn(self, timeout=10, raise_e=True):
        """
        Click the HPX Quick Run radio button on the Add New Shortcut screen.
        """
        self.driver.wait_for_object("hpx_quick_run_radio_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_add_save_shortcut_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Add Save Shortcut screen.
        """
        self.driver.wait_for_object("add_save_shortcut_title", timeout=timeout, raise_e=raise_e)

    def verify_save_destination(self, timeout=10, raise_e=True):
        """
        Verify the Save Destination field on the Add Save Shortcut screen.
        """
        self.driver.wait_for_object("edit_shortcut_print_toggle_btn", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("edit_shortcut_email_toggle_btn", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("edit_shortcut_save_toggle_btn", timeout=timeout, raise_e=raise_e)

    def verify_add_shorcuts_destinations(self, timeout=10, raise_e=True):
        """
        Verify the presence of Print, Email and Save Destinations on Add Shortcuts screen.
        """
        self.driver.wait_for_object("print_destination_txt", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("email_destination_txt", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("save_destination_txt", timeout=timeout, raise_e=raise_e)

    def verify_file_type_in_shortcut_settings_screen(self, timeout=10, raise_e=True):
        """
        Verify that the File Type is not displayed in the Shortcut Settings screen.
        """
        self.driver.wait_for_object("file_type_label", timeout=timeout, raise_e=False)

    def enter_shortcut_name(self, shortcut_name, timeout=10, raise_e=True):
        """
        Enter text into the Shortcut Name input box on the Edit Shortcut screen.
        :param shortcut_name: The text to enter into the input box.
        """
        locator = "shortcut_name_box"
        input_field = self.driver.wait_for_object(locator, timeout=timeout, raise_e=raise_e)
        input_field.clear()
        input_field.send_keys(shortcut_name)

    def verify_save_shortcut_btn(self, timeout=10, raise_e=True):
        """
        Verify the presence of the Save Shortcut button on the Edit Shortcuts screen.
        """
        return self.driver.wait_for_object("save_shortcut_btn", timeout=timeout, raise_e=raise_e)
    
    def click_save_shortcut_btn(self, timeout=10, raise_e=True):
        """
        Click the Save Shortcut button on the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("save_shortcut_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_quick_run_toggle(self, timeout=10, raise_e=True):
        """
        Verify the Quick Run toggle button on the Edit Shortcuts screen.
        """
        return self.driver.wait_for_object("quick_run_toggle_btn", timeout=timeout, raise_e=raise_e)
    
    def click_quick_run_toggle_btn(self, timeout=10, raise_e=True):
        """
        Click the Quick Run toggle button on the Edit Shortcuts screen.
        """
        self.driver.wait_for_object("quick_run_toggle_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_img_file_type(self, timeout=10, raise_e=True):
        """
        Click the Image File Type option on the Add Shortcuts screen.
        """
        return self.driver.wait_for_object("img_file_type", timeout=timeout, raise_e=raise_e)
    
    def click_image_file_type(self, timeout=10, raise_e=True):
        """
        Click the toggle switch on the shortcut settings screen.
        """
        self.driver.wait_for_object("img_file_type", timeout=timeout, raise_e=raise_e).click()
    
    def verify_pdf_file_type(self, timeout=10, raise_e=True):
        """
        Click the PDF File Type option on the Add Shortcuts screen.
        """
        return self.driver.wait_for_object("pdf_file_type", timeout=timeout, raise_e=raise_e)
    
    def verify_add_button(self, timeout=10, raise_e=True):
        """
        Verify the presence of the Add button on the Add Shortcuts screen.
        """
        self.driver.swipe(direction="down")
        return self.driver.wait_for_object("add_button", timeout=timeout, raise_e=raise_e)
    
    def click_add_button(self, timeout=10, raise_e=True):
        """
        Click the Add button on the Add Shortcuts screen.
        """
        self.driver.swipe(direction="down")
        self.driver.wait_for_object("add_button", timeout=timeout, raise_e=raise_e).click()

    def click_color_card_by_index(self, index, timeout=10, raise_e=True):
        """
        Click a color card by index on the shortcut settings screen.
        :param index: The index of the color card to click (1-based indexing)
        :param timeout: The time to wait for the element
        :param raise_e: Whether to raise an exception if element is not found
        """
        locator = f"color_card_{index}"
        self.driver.wait_for_object(locator, timeout=timeout, raise_e=raise_e).click()
    
    def verify_color_card_selection(self, index, timeout=10, raise_e=True):
        """
        Verify if a color card is selected by index.
        :param index: The index of the color card to verify (1-based indexing)
        :param timeout: The time to wait for the element
        :param raise_e: Whether to raise an exception if element is not found
        :return: True if the color card is selected, False otherwise
        """
        locator = f"color_card_{index}"
        return self.driver.get_attribute(locator, "selected", timeout=timeout, raise_e=raise_e)
    
    def click_done_btn(self, timeout=10, raise_e=True):
        """
        Click the Done button on the Shortcuts saved screen.
        """
        self.driver.wait_for_object("done_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_shortcut_present_in_list(self, shortcut_name, timeout=10, raise_e=True):
        """
        Verify that a shortcut with the given name is present in the shortcuts list.
        """
        return self.driver.wait_for_object("shortcut_by_name", format_specifier=[shortcut_name], timeout=timeout, raise_e=raise_e)
    
    def click_run_this_shortcut_btn(self, timeout=10, raise_e=True):
        """
        Click the Run This Shortcut button on the Shortcuts screen.
        """
        self.driver.wait_for_object("run_this_shortcut_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_delete_this_shortcut_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Delete This Shortcut dialog.
        """
        return self.driver.wait_for_object("delete_this_shortcut_title", timeout=timeout, raise_e=raise_e)

    def verify_delete_shortcut_btn_delete_btn(self, timeout=10, raise_e=True):
        """
        Verify the Delete button on the Delete Shortcut Confirmation message.
        """
        return self.driver.wait_for_object("delete_shortcut_btn_delete_btn", timeout=timeout, raise_e=raise_e)

    def verify_delete_shortcut_btn_cancel_btn(self, timeout=10, raise_e=True):
        """
        Verify the Cancel button on the Delete Shortcut Confirmation message.
        """
        return self.driver.wait_for_object("delete_shortcut_btn_cancel_btn", timeout=timeout, raise_e=raise_e)
    
    def click_delete_shortcut_btn_delete_btn(self, timeout=10, raise_e=True):
        """
        Click the Delete button on the Delete Shortcut Confirmation message.
        """
        self.driver.click("delete_shortcut_btn_delete_btn", timeout=timeout, raise_e=raise_e)
    
    def click_delete_shortcut_btn_cancel_btn(self, timeout=10, raise_e=True):
        """
        Click the Cancel button on the Delete Shortcut Confirmation message.
        """
        self.driver.click("delete_shortcut_btn_cancel_btn", timeout=timeout, raise_e=raise_e)

    def click_account_selection(self, timeout=10, raise_e=True):
        """
        Click the account selection on the Shortcuts screen.
        """
        self.driver.wait_for_object("account_selection", timeout=timeout, raise_e=raise_e).click()

    def verify_your_shortcut_is_running_title(self, timeout=10, raise_e=True):
        """
        Verify the title of the Your Shortcut is Running screen.
        """
        return self.driver.wait_for_object("your_shortcut_is_running_title", timeout=timeout, raise_e=raise_e)
    
    def click_view_status_btn(self, timeout=10, raise_e=True):
        """
        Click the View Status button on the Your Shortcut is Running screen.
        """
        self.driver.wait_for_object("view_status_btn", timeout=timeout, raise_e=raise_e).click()

    def click_shortcuts_btn(self, timeout=10, raise_e=True):
        """
        Click the Shortcuts button on the Your Shortcut is Running screen.
        """
        self.driver.wait_for_object("shortcuts_btn_in_your_shortcut_is_running_screen", timeout=timeout, raise_e=raise_e).click()

    def click_three_dot_in_account(self, timeout=10, raise_e=True):
        """
        Click the three dots in the account section on the Shortcuts screen.
        """
        self.driver.wait_for_object("three_dot_in_account", timeout=timeout, raise_e=raise_e).click()

    def click_remove_btn_in_account(self, timeout=10, raise_e=True):
        """
        Click the Remove button in the account section on the Shortcuts screen.
        """
        self.driver.wait_for_object("toggle_disabling_remove_btn", timeout=timeout, raise_e=raise_e).click()

    def verify_remove_hp_access_confirmation_msg(self, timeout=10, raise_e=True):
        """
        Verify the Remove HP Access Confirmation message.
        """
        return self.driver.get_attribute("remove_hp_access_confirmation_msg", "text", timeout=timeout, raise_e=raise_e)