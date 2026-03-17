import pytest
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Shortcuts(SmartFlow):
    flow_name = "shortcuts"

    def click_add_shortcut(self, timeout=10):
        """
        Click on Add Shortcuts button
        :return:
        """
        self.driver.click("add_shortcuts_btn", timeout=timeout)

    def click_back_btn(self, timeout=10):
        """
        Click on Back button on Shortcuts screen
        """
        self.driver.click("shortcuts_back_btn", timeout=timeout)

    def click_shortcuts_tile_btn(self, timeout=10):
        """
        Click on Shortcuts tile button
        """
        self.driver.click("_shared_smart_task_tile", timeout=timeout)

    def click_create_your_own_shortcut_btn(self, timeout=10):
        """
        Click on Create your own Shortcut button on Shortcuts screen
        """
        self.driver.click("create_your_own_shortcut_btn", timeout=timeout)

    def select_copies(self):
        self.driver.click("copies_dropdown")
        self.driver.click("copies_dropdown_2")

    def select_color(self):
        self.driver.click("color_dropdown")
        self.driver.click("graycolor_dropdown_option")

    def click_cancel_btn(self, timeout=10):
        """
        Click on Cancel button on Add Shortcut or Add Print screen
        """
        self.driver.click("cancel_btn", timeout=timeout)

    def click_cancel_yes_btn(self, timeout=10):
        """
        Click on Yes, Cancel button on Add Shortcut or Add Print screen
        """
        self.driver.click("cancel_yes_btn", timeout=timeout)

    def click_email_destination_toggle(self, timeout=10):
        """
        Click the Email toggle.
        """
        self.driver.click("email_destinations_toggle", timeout=timeout)

    def click_save_destination_toggle(self, timeout=10):
        """
        Click the Save toggle.
        """
        self.driver.click("save_destinations_toggle", timeout=timeout)

    def click_print_destination_toggle(self, timeout=10):
        """
        Click the Print toggle.
        """
        self.driver.click("print_destinations_toggle", timeout=timeout)

    def click_copies_dropdown(self, timeout=10):
        """
        Click copies dropdown
        """
        self.driver.click("copies_dropdown", timeout=timeout)

    def click_color_dropdown(self, timeout=10):
        """
        Click color dropdown
        """
        self.driver.click("color_dropdown", timeout=timeout)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_shortcuts_screen(self, timeout=25):
        """
        Verify current screen is Shortcuts screen via:
            - title
            - Add Shortcut button
        """
        self.driver.wait_for_object(
            "shortcuts_title", timeout=timeout, displayed=False)
        if pytest.platform == "MAC":
            self.dismiss_coachmark(timeout=timeout)
        self.driver.wait_for_object("add_shortcuts_btn", timeout=timeout)

    def verify_continue_btn(self, timeout=10):
        """
        Verify Continue button is displayed and click only if enabled
        """
        btn = self.driver.wait_for_object("continue_btn", timeout=timeout)
        is_enabled = self.driver.get_attribute("continue_btn", "enabled")
        if is_enabled:
            btn.click()
        else:
        # Optionally, you can log or raise an exception if needed
            pass

    def verify_save_destination_toggle(self, timeout=10):
        """
        Verify Save destination toggle is displayed on Shortcuts screen
        """
        self.driver.wait_for_object("save_destinations_toggle", timeout=timeout)
        self.driver.get_attribute("save_destinations_toggle", "enabled")

    def verify_shortcuts_tile_btn(self):
        """
        Verify the Shortcuts tile button is displayed
        """
        self.driver.wait_for_object("_shared_smart_task_tile", timeout=10)

    def click_edit_btn(self):
        """
        Click on Edit button on Shortcuts screen
        """
        self.driver.click("edit_btn")
    
    def verify_default_email_shortcuts_shows(self):
        """
        Verify "Default" Email Shortcut tile shows
        """
        self.driver.wait_for_object("email_icon_image")

    def click_delete_email_shortcut_btn(self):
        """
        Click on Delete Email Shortcut button on Shortcuts screen
        """
        self.driver.click("delete_email_shortcut_btn", timeout=10)

    def verify_settings_screen(self, timeout=10):
        """
        Verify current screen is Settings screen via:
            - title
            - Save button
        """
        self.driver.wait_for_object("settings_title", timeout=timeout)

    def click_settings_btn(self):
        """
        Click on Settings button on Shortcuts screen
        """
        self.driver.click("settings_button")

    def verify_edit_page_disabled_shortcuts_btn(self):
        """
        Verify the Edit page has disabled Shortcuts button
        """
        self.driver.wait_for_object("edit_btn_disabled")
        self.driver.wait_for_object("edit_add_shortcut_btn_disabled")

    def select_pop_up_ok_btn(self):
        """
        Click on OK button on pop-up
        """
        if self.driver.wait_for_object("_shared_str_ok", raise_e=False):
            self.driver.click("_shared_str_ok")

    def select_edit_btn_print_shortcuts_on_edit_shortcuts_screen(self, timeout=10):
        """
        Select Print Shortcuts on Edit Shortcuts screen
        """
        self.driver.click("edit_shortcuts_print_btn", timeout=timeout)

    def select_edit_btn_email_shortcuts_on_edit_shortcuts_screen(self, timeout=10):
        """
        Select Email Shortcuts on Edit Shortcuts screen
        """
        self.driver.click("edit_shortcuts_email_btn", timeout=timeout)

    def select_edit_btn_save_shortcuts_on_edit_shortcuts_screen(self, timeout=10):
        """
        Select Save Shortcuts on Edit Shortcuts screen
        """
        self.driver.click("edit_shortcuts_save_btn", timeout=timeout)

    def verify_print_destination_toggle_disabled(self):
        """
        Verify Print destination toggle is disabled on Shortcuts screen
        """
        self.driver.wait_for_object("print_destinations_toggle")
        is_enabled = self.driver.get_attribute("print_destinations_toggle", "enabled")
        assert not is_enabled, "Print destination toggle should be disabled"

    def verify_email_destination_toggle_disabled(self):
        """
        Verify Email destination toggle is disabled on Shortcuts screen
        """
        self.driver.wait_for_object("email_destinations_toggle")
        is_enabled = self.driver.get_attribute("email_destinations_toggle", "enabled")
        assert not is_enabled, "Email destination toggle should be disabled"

    def verify_save_destination_toggle_disabled(self):
        """
        Verify Save destination toggle is disabled on Shortcuts screen
        """
        self.driver.wait_for_object("save_destinations_toggle")
        is_enabled = self.driver.get_attribute("save_destinations_toggle", "enabled")
        assert not is_enabled, "Save destination toggle should be disabled"

    def verify_edit_print_screen_page_displayed(self):
        """
        Verify Edit Print Screen page is displayed
        """
        self.driver.wait_for_object("edit_print_screen_title")

    def click_continue_btn(self, timeout=10):
        """
        Click on Continue button
        """
        self.driver.click("continue_btn", timeout=timeout)

    def click_two_sided_dropdown(self, timeout=10):
        """
        Click on Two-sided dropdown
        """
        self.driver.click("two-sided_dropdown", timeout=timeout)

    def verify_two_sided_dropdown_selection(self,option =None):
        """
        Verify the selected option is displayed in Two-sided dropdown
        """
        if option:
            if option == "off":
                self.driver.click_element("two_sided_dropdown_option")
            elif option == "shortedge":
                self.driver.click_element("two_sided_dropdown_shortedge")
            elif option == "longedge":
                self.driver.click_element("two_sided_dropdown_longedge")
            else:
                raise ValueError("Invalid option. Must be 'off', 'shortedge', or 'longedge'.")

    def click_add_to_email_shortcut_btn(self, timeout=10):
        """
        Click on 'Add to Email Shortcut' button
        """
        self.driver.click("add_email_screen_title", timeout=timeout)

    def click_add_to_shortcut_btn(self, timeout=10):
        """
        Click on 'Add to Shortcut' button
        """
        self.driver.click("add_to_shortcut_btn", timeout=timeout)

    def verify_add_email_screen_displayed(self):
        """
        Verify Add Email screen is displayed
        """
        self.driver.wait_for_object("add_email_screen_title")

    def enter_email_address_in_to_section(self, email_address):
        """
        Enter email address in the 'To' section of Add Email screen
        """
        self.driver.send_keys("email_to_field", email_address)

    def verify_email_error_message_displayed(self):
        """
        Verify error message is displayed for invalid email
        """
        self.driver.wait_for_object("email_error_message")
        self.driver.get_attribute("email_error_message", "name")

    def enter_multiple_email_addresses_in_to_section(self, email_count=20):
        """
        Create and enter multiple email addresses in the 'To' section
        :param email_count: Number of email addresses to create and enter (max 21)
        """
        if email_count > 21:
            raise ValueError("Number of emails cannot exceed 21")
        if email_count < 1:
            raise ValueError("Number of emails must be at least 1")
        # Create email list
        email_list = [f"test{i}@example.com" for i in range(1, email_count + 1)]
        # Join emails with comma separator and enter in the field
        email_string = ", ".join(email_list)
        self.driver.send_keys("email_to_field", email_string)

    def verify_too_many_emails_error_message_displayed(self):
        """
        Verify error message is displayed for too many email addresses
        """
        self.driver.wait_for_object("too_many_emails_error_message")

    def click_subject_field(self):
        """
        Click on Subject field in Add Email screen
        """
        self.driver.click("subject_to_field")

    def enter_subject_field(self, subject_text):
        """
        Enter text in the Subject field
        """
        self.driver.send_keys("subject_to_field", subject_text)

    def modify_email_body_text(self, body_text):
        """
        Modify the text in email body section
        """
        self.driver.send_keys("email_body_field", body_text)

    def verify_add_shortcut_screen_displayed(self):
        """
        Verify Add Shortcut screen is displayed
        """
        self.driver.wait_for_object("add_shortcut_screen_title")
    
    def verify_accounts_section_displayed(self):
        """
        Verify Accounts section is displayed on Add Save screen
        """
        self.driver.wait_for_object("google_drive_accounts", timeout=10)

    def click_existing_shortcuts(self):
        """
        Click on Existing Shortcuts button
        """
        self.driver.click("existing_shortcuts_button")

    def verify_select_source_from_screen_popup(self):
        """
        Verify current screen is Source Select popup screen via:
            - Camera Scan option
            - Print scan option
            - Files & Photos Option
            - cancel button
        """
        self.driver.wait_for_object("select_source_message")
        self.driver.wait_for_object("camera_scan_option")
        self.driver.wait_for_object("print_scan_option")
        self.driver.wait_for_object("files_photo_option")
        self.driver.wait_for_object("cancel_btn")

    def select_firsttime_scan_setting_permission_popup(self, raise_e=False):
        """
        Verify Scan Setting Permission popup is displayed
        """
        for _ in range(4):
            self.driver.click("next_btn", raise_e=raise_e)

    def verify_printing_status_btn_changes(self, timeout=60):
        """
        Verify the Printing Status button changes to 'Printing…' after clicking Finish Shortcut
        """
        self.driver.wait_for_object("printing_status_btn", timeout=timeout)
        printing_text = self.driver.get_attribute("printing_status_btn", "name")
        assert "Printing…" in printing_text, "Printing status button did not change to 'Printing…'"
        self.driver.wait_for_object("cancel_btn", timeout=timeout)