import logging
from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
from selenium.common.exceptions import NoSuchElementException
import time
import pytest

class ComposeFax(SoftFaxFlow):
    flow_name = "compose_fax"

    FILES_PHOTOS_BTN = "files_photos_btn"
    CAMERA_BTN = "camera_btn"
    SCANNER_BTN = "scanner_btn"
    MENU_SAVE_DRAFT_BTN = "menu_save_draft"
    MENU_CLEAR_FIELDS_BTN = "menu_clear_fields"
    MENU_FAX_HISTORY_BTN = "menu_fax_history"
    MENU_FAX_SETTINGS_BTN = "menu_fax_settings"
    MENU_HOME_BTN = "menu_home"
    MENU_NEW_COMPOSE_BTN = "menu_new_compose"
    EMPTY_PHONE_MSG = "empty_phone_number_msg"
    INVALID_FORMAT_MSG = "invalid_format_phone_number_msg"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    # -------------------       Files and Cover Page        -----------------------------
    def click_files_and_cover_page(self):
        """
        Click on Files and Cover Page on Compose Fax screen
        """
        self.driver.click("files_cover_page_dropdown")
    

    def enter_subject(self, name):
        """
        Enter a subject name
        :param name: required parameter
        """
        self.driver.wait_for_object("subject_name_edit_tf")
        self.driver.selenium.js_clear_text("subject_name_edit_tf")
        self.driver.send_keys("subject_name_edit_tf", name)
        if self.driver.driver_info['platform'].lower() == "ios":
            self.click_done_btn()

    def click_trash_icon(self):
        """
        Click on Trash icon under Files and Cover Page section
        """
        self.driver.click("trash_icon")

    def click_save_cover_page_template(self):
        """
        Click on Save cover page template under Files and Cover Page section
        """
        self.driver.click("save_cover_page_template_btn")

    def enter_cover_page_name(self, cover_page_name):
        """
        Enter a cover page name
        :param name: required parameter
        """
        self.driver.wait_for_object("cover_page_name_edit_tf")
        self.driver.send_keys("cover_page_name_edit_tf", cover_page_name)
        if self.driver.driver_info['platform'].lower() == "ios":
            self.click_done_btn()

    def click_cancel_btn(self):
        """
        Click on CANCEL button on Name your cover page template screen
        """
        self.driver.click("cancel_btn")

    def click_save_btn(self):
        """
        Click on Sve button on Name your cover page template screen
        """
        self.driver.click("save_btn")
    
    def click_template_btn(self):
        """
        Click on Template button under Files and Cover Page section
        """
        self.driver.click("template_title")

    def click_none_option(self):
        """
        Click on None on Template option list
        """
        self.driver.click("none_option")

    def click_create_a_new_cover_page_template_option(self):
        """
        Click on Create a new cover page template on option list
        """
        self.driver.click("create_a_new_cover_page_template_option")

    def click_edit_btn(self):
        """
        Click on Edit button on option list
        """
        self.driver.click("edit_btn")

    def click_close_btn(self):
        """
        Click Close button on correct Error message screen.
        """
        self.driver.click("close_btn")

    def click_add_files_option_btn(self, btn_name):
        """
        Click on a button in Add File
        :param btn_name: using class constant
                        FILES_PHOTOS_BTN
                        CAMERA_BTN
                        SCANNER_BTN
        """
        self.click_files_and_cover_page()
        if not self.driver.wait_for_object(btn_name, invisible=False, timeout=10, raise_e=False):
            self.driver.click("files_cover_page_dropdown")
        time.sleep(3)
        if self.driver.wait_for_object("trash_icon", raise_e=False):
            self.click_trash_icon()
            time.sleep(3)
        self.driver.click(btn_name)

    def click_recipient_dropdown(self):
        self.driver.click("recipient_dropdown")

    def verify_add_your_files_options(self):
        self.click_files_and_cover_page()
        self.driver.wait_for_object(self.FILES_PHOTOS_BTN)
        self.driver.wait_for_object(self.CAMERA_BTN)
        self.driver.wait_for_object(self.SCANNER_BTN)

    def delete_added_file(self):
        """
        Click on trash icon in files and cover page after adding new file
        """
        self.driver.click("delete_icon_btn")

    def get_added_file_information(self):
        """
        Get information of added file:
        :return: file name and number of page
        """
        self.driver.wait_for_object("files_cover_page_dropdown", timeout=10)
        self.driver.click("files_cover_page_dropdown")
        file_name = self.driver.find_object("file_name").text
        number_pages = self.driver.find_object("file_number_pages").text
        return file_name, number_pages

    def verify_file_added(self, raise_e=False):
        return self.driver.wait_for_object("file_name", raise_e=raise_e)

    # -------------------       To and From section        -----------------------------
    def enter_recipient_information(self, phone_no, name=None):
        """
        Enter recipient information
        :param phone_no: required parameter
        :param country_code: country code. Example: +1 , 1
        :param name: optional parameter.
        """
        self.driver.wait_for_object("recipient_dropdown", timeout=10)
        self.driver.click("recipient_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("recipient_phone_edit_tf", timeout=5)
        self.driver.send_keys("recipient_phone_edit_tf", phone_no)
        if name:
            self.driver.send_keys("recipient_name_edit_tf", name)
        if self.driver.driver_info['platform'].lower() == "ios":
            self.click_done_btn()

    def get_recipient_information(self):
        """
        Get Recipient Information
        :return: (phone number, name)
        """
        self.driver.wait_for_object("recipient_dropdown", timeout=10)
        self.driver.click("recipient_dropdown")
        # Switch back to Native App for this element
        phone_edit_tf = self.driver.wait_for_object("recipient_phone_edit_tf", timeout=5)
        phone = phone_edit_tf.get_property("value").strip()
        country_code_elem = self.driver.wait_for_object("recipient_phone_country_code")
        country_code = country_code_elem.get_property("value").strip()
        name = self.driver.get_text("recipient_name_edit_tf")
        return phone, name, country_code

    def click_contacts_icon(self):
        """
        From Compose Fax screen, Clicking on person icon in To area
        """
        self.driver.wait_for_object("recipient_dropdown", timeout=10)
        self.driver.click("recipient_dropdown")
        self.driver.click("recipient_contact_icon")

    def enter_sender_information(self, name, phone_no):
        """
        Enter a sender information
        :param name: required parameter
        :param phone_no: required parameter
        :param country_code: country code. Example: +1, 1
        """
        # Make sure start from top of screen
        self.driver.wait_for_object("sender_dropdown", timeout=10)
        self.driver.click("sender_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("sender_phone_edit_tf", timeout=5)
        if pytest.platform == "IOS":
            self.driver.selenium.js_clear_text("sender_phone_edit_tf")  
        self.driver.send_keys("sender_phone_edit_tf", phone_no)
        if pytest.platform == "IOS":
            self.driver.selenium.js_clear_text("sender_name_edit_tf")
        self.driver.send_keys("sender_name_edit_tf", name)
        if pytest.platform == "IOS":
            self.click_done_btn()

    def get_sender_information(self):
        """
        Get Recipient Information
        :return: (phone number, name)
        """
        self.driver.wait_for_object("sender_dropdown", timeout=10)
        self.driver.click("sender_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("sender_phone_edit_tf", timeout=5)
        phone = self.driver.get_attribute("sender_phone_edit_tf", "value")
        name = self.driver.get_attribute("sender_name_edit_tf", "value")
        return phone, name

    def click_send_fax(self, raise_e=True):
        """
        Click on Sex Fax button
        """
        # self.driver.wait_for_object("send_fax_btn")
        # return self.driver.click("send_fax_btn", change_check={"wait_obj": "send_fax_btn", "invisible": True},
        #                          raise_e=raise_e)
        self.driver.click("send_fax_btn")
        if self.driver.wait_for_object("dialog_continue_btn", raise_e=False):
            self.driver.click("dialog_continue_btn")

    def click_menu_option_btn(self, btn_name, popup_action=""):
        """
        Click on a button in Menu Option
        :param btn_name: using class constant
                MENU_SAVE_DRAFT_BTN
                MENU_CLEAR_FIELDS_BTN
                MENU_FAX_HISTORY_BTN
                MENU_FAX_SETTINGS_BTN
                MENU_HOME_BTN
                MENU_NEW_COMPOSE_BTN
        :return:
        """
        self.driver.click("3_dots_menu_btn")
        self.driver.wait_for_object(btn_name, timeout=5)
        self.driver.click(btn_name)
        if popup_action:
            self.driver.click(popup_action, timeout=5, raise_e=False)

    def verify_3_dots_menu_options(self):
        options_missing = []
        options = [self.MENU_SAVE_DRAFT_BTN, self.MENU_CLEAR_FIELDS_BTN, self.MENU_FAX_HISTORY_BTN,
                   self.MENU_FAX_SETTINGS_BTN, self.MENU_HOME_BTN]
        if not self.driver.click("3_dots_menu_btn", raise_e=False):
            return False
        for option in options:
            if self.driver.wait_for_object(option, raise_e=False) is False:
                options_missing.append(option)
        if len(options_missing) > 0:
            logging.info("Following options {}:not displayed".format(options_missing))
            return False
        else:
            return True

    def verify_save_as_draft_pop_up(self):
        """
        Verify save as draft pop_up elements: title, message and buttons
        """
        self.driver.wait_for_object("save_as_draft_popup_title")
        self.driver.wait_for_object("save_as_drat_popup_msg")
        self.driver.wait_for_object("save_as_draft_popup_save_draft_btn")
        self.driver.wait_for_object("save_as_draft_popup_exit_bn")
        self.driver.wait_for_object("save_as_draft_popup_cancel_btn")

    def handle_save_as_draft_popup(self, button_to_select):
        """
        Select one option from save as draft popup using one of the following parameters:
        "save_as_draft_popup_save_draft_btn" -> Select save as draft button
        "save_as_draft_popup_cancel_btn"     -> Select cancel button
        "save_as_draft_popup_exit_bn"        -> Select exit button
        
        :param button_to_select: -> one of the locators above used to handle the popup
        """
        option_list = [
            "save_as_draft_popup_exit_bn",
            "save_as_draft_popup_save_draft_btn",
            "save_as_draft_popup_cancel_btn"
            ]
        if not button_to_select in option_list:
            raise ValueError(f"The button {button_to_select} should be present on 'Save as Draft' popup. No action is executed.")
        if self.driver.wait_for_object("save_as_draft_popup_title", timeout=10, raise_e=False):
            self.driver.click(button_to_select, timeout=5)
            return True
        return False

    def click_save_this_contact_btn(self):
        """
        Click on Save this contact button on Compose Fax screen
        """
        self.driver.click("save_this_contact_btn")

    def click_add_optional_info_btn(self):
        """
        Click on Add Optional info button under From section
        """
        self.driver.click("add_optional_info_btn")

    def verify_add_optional_info_btn(self, raise_e=True):
        return self.driver.wait_for_object("add_optional_info_btn", raise_e=raise_e)

    def click_save_as_profile_btn(self):
        """
        Click on Save as profile button under From section
        """
        self.driver.click("save_as_profile_btn")

    def click_collapse_btn(self):
        """
        Click on Collapse button under From section
        """
        self.driver.click("collapse_btn")

    def verify_collapse_btn(self, raise_e=True):
        return self.driver.wait_for_object("collapse_btn", raise_e=raise_e)

    def verify_reply_fax_number(self):
        self.driver.wait_for_object("reply_fax_number")

    def enter_profile_name(self, profile_name):
        """
        Enter a profile name
        :param name: profile_name
        """
        self.driver.wait_for_object("profile_name_edit_tf")
        self.driver.send_keys("profile_name_edit_tf", profile_name)

    def click_fax_feature_update_compose_new_fax_btn(self, raise_e=True):
        """
        Click on Compose New Fax button on Fax Feature Update screen
        """
        self.driver.click("fax_feature_compose_new_fax_btn", raise_e=raise_e)

    def click_fax_feature_update_dismiss_btn(self, raise_e=True):
        """
        Click on Dismiss button on Fax Feature Update screen
        """
        self.driver.click("fax_feature_dismiss_btn", raise_e=raise_e)

    def click_save_as_a_draft_btn(self, raise_e=False):
        """
        Click on Save as a Draft button from the Draft popup
        """
        self.driver.click("save_as_draft_popup_save_draft_btn", raise_e=raise_e)

    def click_exit_btn(self, raise_e=False):
        """
        Click on Exit button from Draft popup
        """
        self.driver.click("save_as_draft_popup_exit_bn", raise_e=raise_e)

    # -------------------       Mobile Fax Home screen on Windows HP Smart        -----------------------------
    def select_compose_fax_menu(self):
        """
        Click Compose Fax menu on Mobile Fax Home page.
        """
        self.driver.click("compose_fax_menu")

    def select_sent_menu(self):
        """
        Click Sent menu on Mobile Fax Home page.
        """
        self.driver.click("sent_menu")

    def select_drafts_menu(self):
        """
        Click Drafts menu on Mobile Fax Home page.
        """
        self.driver.click("drafts_menu")

    def select_fax_settings_menu(self):
        """
        Click Fax Settings menu on Mobile Fax Home page.
        """
        self.driver.click("fax_settings_menu")

    def click_delete_this_fax_btn(self):
        self.driver.click("delete_this_fax_btn")

    def click_delete_btn(self):
        self.driver.click("delete_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_compose_fax_screen(self, timeout=90, raise_e=True):
        """
        Verify current screen is Compose Fax screen via:
            - title
            - Send Fax button
        """
        # performance issue: softfax screen takes longer to load 
        # https://hp-jira.external.hp.com/browse/AIOI-16018
        time.sleep(5)
        return self.driver.wait_for_object("title", timeout=timeout,
                                           raise_e=raise_e) is not False and self.driver.wait_for_object("send_fax_btn",
                                                                                                         timeout=timeout,
                                                                                                         raise_e=raise_e) is not False

    # -------------------       To and From section       -----------------------------
    def verify_phone_validation_message(self, error_msg, is_sender=False, raise_e=True):
        """
        Verify validation message after entering invalid recipient phone (visible/invisible)
        :param error_msg: using class constant
                EMPTY_PHONE_MSG
                INVALID_FORMAT_MSG
        :param raise_e:
        """
        if is_sender:
            self.driver.wait_for_object("sender_dropdown", timeout=10)
            self.driver.click("sender_dropdown")
        else:
            self.driver.click("recipient_dropdown")
        return self.driver.wait_for_object(error_msg, timeout=10, raise_e=raise_e, displayed=False)

    def verify_sender_name_error_message(self, raise_e=True):
        """
        Verify error message after entering invalid sender name
        :param raise_e:
        """
        self.driver.wait_for_object("sender_dropdown", timeout=10)
        self.driver.click("sender_dropdown")
        return self.driver.wait_for_object("sender_name_error_message", timeout=10, raise_e=raise_e)

    def verify_save_this_contact_btn(self, invisible=False, raise_e=True):
        """
        Verify Save this contact button is invisible or not on Compose Fax screen
        """
        return self.driver.wait_for_object("save_this_contact_btn", invisible=invisible, raise_e=raise_e)

    def verify_saved_btn(self, invisible=False, raise_e=True):
        """
        Verify Saved button is invisible or not on Compose Fax screen
        """
        return self.driver.wait_for_object("saved_btn", invisible=invisible, raise_e=raise_e)

    def verify_organization_name(self, invisible=False, raise_e=True):
        """
        Verify organization name label is invisible or not under From section
        """
        return self.driver.wait_for_object("organization_name", invisible=invisible, raise_e=raise_e)

    def verify_email(self, invisible=False, raise_e=True):
        """
        Verify email label is invisible or not under From section
        """
        return self.driver.wait_for_object("organization_name", invisible=invisible, raise_e=raise_e)

    def verify_name_your_profile_screen(self):
        """
        Verify current screen is Name your profile screen via:
            - title
            - CANCEL and SAVE button
        """
        self.driver.wait_for_object("name_your_profile_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("save_btn")

    def verify_profile_label(self, raise_e=True):
        """
        Verify Profile: label under from section:
        """
        return self.driver.wait_for_object("profile_label", raise_e=raise_e)

    def get_sender_profile_label(self):
        self.driver.click("sender_dropdown")
        if self.verify_profile_label(raise_e=False) is not False:
            # empty profile will return "None" as a sender
            return self.driver.get_attribute("sender_profile_label", "text")
        else:
            return None

    def verify_template_edit_view(self):
        """
        Verify on template edit page
        """
        self.driver.wait_for_object("edit_template_delete_btn")
        self.driver.wait_for_object("edit_template_name")
        self.driver.wait_for_object("edit_template_subject")
        self.driver.wait_for_object("edit_template_message")
        self.driver.wait_for_object("edit_template_save_btn")

    # -------------------       Files and Cover Page        -----------------------------
    def verify_added_pages_number(self, page_number):
        """
        Verify page number in file and cover page
        :param page_number:
        :type page_number: int
        """
        # Make sure start from top of screen
        self.driver.wait_for_object("files_cover_page_dropdown", timeout=10)
        self.driver.click("files_cover_page_dropdown")
        self.driver.wait_for_object("file_number_pages", timeout=10)
        actual_page = int(self.driver.find_object("file_number_pages").text.split(" ")[0])
        if actual_page != page_number:
            raise ValueError(
                "Expected {} page(s) is not on the screen. Actual: {} page(s)".format(page_number, actual_page))

    def verify_uploaded_file(self, timeout=30):
        """
        Verify file is uploaded successfully.
        :param timeout: uploading timeout
        """
        # Make sure start from top of screen
        self.click_files_and_cover_page()
        self.driver.wait_for_object("file_name", timeout=timeout)
        self.driver.wait_for_object("file_number_pages", timeout=10)

    def verify_no_updated_file(self):
        """
        Verify that there is no file which i added by visible:
            - file & photos button
            - camera button
            - printer scanner button
        """
        self.click_files_and_cover_page()
        self.driver.wait_for_object("files_photos_btn", timeout=10)
        self.driver.wait_for_object("camera_btn", timeout=10)
        self.driver.wait_for_object("scanner_btn", timeout=10)

    def verify_subject(self, invisible=False):
        """
        Verify Subject * under Files and Cover Page section
        """
        self.driver.wait_for_object("subject_name_edit_tf", invisible=invisible)

    def verify_message(self, invisible=False):
        """
        Verify Message under Files and Cover Page section
        """
        self.driver.wait_for_object("message_name_edit_tf", invisible=invisible)

    def verify_one_page(self, invisible=False):
        """
        Verify 1 page shows in add cover page screen
        """
        self.driver.wait_for_object("one_cover_page", invisible=invisible)

    def verify_cover_page_magnifier(self, invisible=False):
        """
        Verify Cover Page Magnifier image
        """
        self.driver.wait_for_object("cover_page_magnifier", invisible=invisible)

    def click_cover_page_magnifier(self):
        """
        Click Cover Page Magnifier image
        """
        self.driver.wait_for_object("cover_page_magnifier")
        self.driver.click("cover_page_magnifier")

    def click_file_item_magnifier(self):
        """
        Click File Item Magnifier image
        """
        self.driver.click("file_item_magnifier", timeout=10)

    def verify_trash_icon(self, invisible=False):
        """
        Verify trash icon is present
        """
        self.driver.wait_for_object("trash_icon", invisible=invisible)

    def verify_subject_invalid_message(self):
        """
        Verify message "Fax Subject is required"
        """
        self.driver.wait_for_object("subject_invalid_message")
    
    def verify_template_title_is_required(self):
        """
        Verify message 'A cover page template titile is required'
        """
        self.driver.wait_for_object("template_title_is_required")

    def verify_name_your_cover_page_template(self):
        """
        Verify name your cover page template screen with:
        - Title
        - CANCEL & SAVE button
        """
        self.driver.wait_for_object("save_cover_page_template_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("save_btn")

    def verify_no_cover_page_template_title_message(self):
        """
        Verify message "A cover page template title is required"
        """
        self.driver.wait_for_object("no_cover_page_template_title_message")

    def verify_cover_template(self, invisible=False, raise_e=True):
        """
        Verify Template: under Files and Cover Page section
        """
        self.driver.wait_for_object("template_title", invisible=invisible, raise_e=raise_e)

    def verify_cover_template_option_screen(self):
        """
        Verify Template option screen with:
        - None
        - Create a new cover page template
        - Currently template list
        """
        self.driver.wait_for_object("none_option")
        self.driver.wait_for_object("list_option")
        self.driver.wait_for_object("create_a_new_cover_page_template_option")

    def verify_template_list(self, template_name):
        """
        Verify template name is visible or invisible under Files and Cover Page / Template section
        :param template_name
        :param invisible
        """
        self.driver.wait_for_object("template_name", format_specifier=[template_name], displayed=True)

    def toggle_need_a_cover_page_on_off(self, on=True):
        """
        switch on/off button for need a cover page
        :param enable: True or False
        """
        self.driver.selenium.check_box("need_a_cover_page_btn", state=on)

    def verify_cover_page(self, invisible=False, displayed=True):
        """
        Verify Cover Page on compose fax screen
        """
        self.driver.wait_for_object("cover_page", invisible=invisible, displayed=displayed)

    def verify_one_cover_page(self, invisible=False, displayed=True):
        """
        Verify 1 page under Files and Cover Page section
        """
        self.driver.wait_for_object("one_cover_page", invisible=invisible, displayed=displayed)

    # -------------------       Mobile Fax Home screen on Windows HP Smart        -----------------------------
    def verify_mobile_fax_get_started_screen(self):
        return self.driver.wait_for_object("get_started_btn", timeout=25, raise_e=False)

    def verify_mobile_fax_home_screen(self, raise_e=True):
        if self.driver.wait_for_object("fax_feature_dismiss_btn", timeout=10, raise_e=False):
            self.driver.click("fax_feature_dismiss_btn")
        return self.driver.wait_for_object("compose_fax_menu", raise_e=raise_e) and \
                self.driver.wait_for_object("sent_menu", raise_e=raise_e) and \
                self.driver.wait_for_object("drafts_menu", raise_e=raise_e) and \
                self.driver.wait_for_object("fax_settings_menu", raise_e=raise_e)

    def verify_add_files_successfully(self, timeout=30, raise_e=True):
        """
        Verify the Add Your Files successfully
        """
        return self.driver.wait_for_object("trash_icon", timeout=timeout,  raise_e=raise_e)

    def verify_job_is_sending(self):
        """
        Verify the job is in the sending state.
        """
        self.driver.wait_for_object("cancel_fax_btn")
        # assert "Dialing"  == self.driver.get_attribute("status", attribute="Name")
        # assert "Sending" in self.driver.get_attribute("status", attribute="Name")

    def verify_job_sent_successfully(self, sent_result=True):
        """
        Verify Mobile Fax sent successfully
        """
        self.driver.wait_for_object("delete_this_fax_btn", timeout = 300)
        self.driver.wait_for_object("edit_and_forward_btn")
        self.driver.wait_for_object("export_fax_report_btn")
        if sent_result:
            assert self.driver.get_attribute("status", attribute="Name") =="Fax Delivered!"
        else:
            assert self.driver.get_attribute("status", attribute="Name") =="Delivery Failed!"

    def verify_are_you_sure_dialog(self):
        """
        Verify the current screen is Are you sure dialog
        """
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("delete_btn")

    def verify_no_faxes_yet(self):
        """
        Verify the No Faxes Yet msg display
        """
        self.driver.wait_for_object("empty_faxes_text")

    def verify_correct_error_screen(self):
        """
        Verify correct Error message shows
        """
        self.driver.wait_for_object("close_btn")

    def verify_invalid_name_entry(self):
        """
        verify invalid name entry for template edit
        """   
        self.driver.wait_for_object("template_name_invalid")

    def verify_invalid_subject_entry(self):
        """
        verify invalid subject entry for template edit
        """    
        self.driver.wait_for_object("subject_invalid_message")

    def enter_name_one_character(self, name):
        """
        clear field and enter single character. This will be deleted to create an invalid entry
        """
        self.driver.selenium.js_clear_text("edit_template_name")
        self.driver.send_keys('edit_template_name', name[0:1])

    def enter_subject_one_character(self, name):
        """
        clear subject field and enter single character. This will be deleted to create an invalid entry
        """
        self.driver.selenium.js_clear_text("edit_template_subject")
        self.driver.send_keys('edit_template_subject', name[0:1])

    def click_back_btn(self):
        """
        click back button
        """
        self.driver.click("back_btn")

    def click_close_preview(self):
        """
        Close coverpage preview
        """
        self.driver.click("close_cover_page_preview")

class MobileComposeFax(ComposeFax):
    context = "NATIVE_APP"

    def click_send_fax_native_btn(self, change_check={"wait_obj": "send_fax_btn", "invisible": True}):
        """
        Click on Send Fax button
        """
        self.driver.click("send_fax_btn", change_check=change_check, timeout=10)

    def toggle_need_a_cover_page_on_off(self, on=True):
        """
        switch on/off button for need a cover page
        :param enable: True or False
        """

        self.driver.check_box("need_a_cover_page_btn", uncheck=not on)

    def verify_need_a_cover_page_only(self):
        """
        Verify need a cover page button button is displayed
        and not other elements
        """
        self.driver.find_object("need_a_cover_page_btn")
        self.verify_subject(invisible=True)

    def wait_processing_msg_disappears(self):
        self.driver.wait_for_object("processing_msg", invisible=True, raise_e=False)

    def get_cover_page_subject(self):
        """
        Verify updated cover page has correct entries
        """
        return self.driver.get_attribute("subject_name_edit_tf", "value")
        
    def click_done_btn(self):
        """
        Click Done Button on Keyboard
        """
        self.driver.click('done_btn')

    def click_delete_key(self):
        """
        Click Delete Button on Keyboard
        """
        self.driver.click('delete_key')

    def clear_entry(self): 
        """
        clear entry
        """   
        self.click_delete_key()
        self.click_done_btn()

    def click_mobile_fax_get_started_btn(self):
        self.driver.click("get_started_btn")

    def verify_cover_page_name(self, name, invisible=False):
        """
        Verify updated cover page has correct entries
        """
        self.driver.wait_for_object('template_title', format_specifier=[name], invisible=invisible)