import pytest
from time import sleep
from MobileApps.libs.flows.web.shortcuts.shortcuts_flow import Shortcutsflow
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import re
from selenium.webdriver.common.keys import Keys

class Shortcuts_Create_Edit(Shortcutsflow):
    flow_name = "shortcuts_create_edit"

    SINGLE_COPIES_BTN = "single_copies_label"
    MULTIPLE_COPIES_BTN = "mul_copies_label"
    COLOR_BTN = "color_option"
    GRAYSCALE_BTN = "grayscale_option"
    OFF_BTN = "off_option"
    SHORT_EDGE_BTN = "short_edge_option"
    LONG_EDGE_BTN = "long_edge_option"

    def __init__(self, driver, context=None):
        super(Shortcuts_Create_Edit, self).__init__(driver, context=context)

    # *********************************************************************************
    #                                ACTION FLOWS--Create Shortcuts                   *
    # *********************************************************************************

    def click_add_shortcut(self):
        """
        Click on Add Shortcut button on Shortcuts screen
        """
        self.driver.click("add_shortcuts_btn", timeout=5)

    def click_help_btn(self, is_win=False):
        """
        Click on Help button on Shortcuts screen
        """
        if not is_win:
            self.driver.selenium.js_click("shortcuts_help_btn", displayed=False)
        else:
            self.driver.click("shortcuts_help_btn")

    def click_shortcuts_help_expand_page_btn(self, timeout=10):
        """
        From the Help Page, click on the arrow expanding the Shortcuts Help page
        """
        self.driver.scroll("shortcuts_expand_help_message", click_obj=True, timeout=timeout)

    def click_back_btn(self):
        """
        Click on Back button on Shortcuts screen
        """
        self.driver.click("shortcuts_back_btn")
    
    def click_create_your_own_shortcut_btn(self):
        """
        Click on Create your own Shortcut button on Shortcuts screen
        """
        self.driver.click("create_your_own_shortcut_btn")
    
    def click_save_to_google_drive_btn(self):
        """
        Click on Save to Google Drive button on Shortcuts screen
        """
        self.driver.click("save_to_google_drive_btn")
    
    def click_print_email_and_save_btn(self):
        """
        Click on Print, Email, and Save button on Shortcuts screen
        """
        self.driver.click("print_email_and_save_btn")
    
    def click_print_btn(self):
        """
        Click on Print item button on Add Shortcut screen
        """
        self.driver.click("print_item")
    
    def select_copies(self, copies_num):
        """
        Select Copies on Add Print screen
        - SINGLE_COPIES
        - MULTIPLE_COPIES
        """
        self.driver.click("copies_label")
        self.driver.click(copies_num)
    
    def select_color(self, color_btn):
        """
        Select Color on Add Print screen
        True: Color
        False:Grayscale
        COLOR_BTN = "color_option"
        GRAYSCALE_BTN = "grayscale_option"
        """
        self.driver.click("color_label")
        self.driver.click(color_btn)

    def select_two_sided(self, two_sided_option):
        """
        Select Two-sided option on Add Print screen
        OFF_BTN = "off_option"
        SHORT_EDGE_BTN = "short_edge_option"
        LONG_EDGE_BTN = "long_edge_option"
        """
        self.driver.click("two-sided_label")
        self.driver.click(two_sided_option)
    
    def click_add_to_shortcut_btn(self):
        """
        Click on Add to Shortcut button on Add Print / Add Email / Add Save screen
        """
        self.driver.click("add_to_shortcut_btn")
    
    def click_cancel_btn(self):
        """
        Click on Cancel button on Add Shortcut or Add Print screen
        """
        self.driver.click("cancel_btn")
    
    def click_email_btn(self):
        """
        Click on Email item button on Add Shortcut screen
        """
        el = self.driver.find_object("email_item")
        if pytest.platform.lower() in ["android", "ios"]:
            el.click()
        else:
            width, height = el.rect["width"], el.rect["height"]
            self.driver.click_by_coordinates(el, width * 0.94, height * 0.5)
        
    def enter_email_receiver(self, to_email):
        """
        Input receiver email on To section of Add Email screen
        """
        if not self.driver.click("email_receive_box", raise_e=False):
            self.driver.send_keys("email_item", Keys.PAGE_DOWN)
            self.driver.click("email_receive_box")
        self.driver.send_keys("email_receive_box", to_email)

    def enter_subject_receiver(self, subject):
        """
        Input Content on Subject section of Add Email screen
        """
        self.driver.click("email_subject_box")
        self.driver.send_keys("email_subject_box", subject)

    def enter_body_receiver(self, body):
        """
        Input Contect on Body section of Add Email screen
        """
        self.driver.click("email_body_box")
        self.driver.send_keys("email_body_box", body)
    
    def click_save_btn(self):
        """
        Click on Save item button on Add Shortcut screen
        """
        if pytest.platform.lower() in ["android", "ios"]:
            self.driver.click("save_item", timeout=10)
        else:
            el = self.driver.wait_for_object("save_item")
            width, height = el.rect["width"], el.rect["height"]
            self.driver.click_by_coordinates(el, width * 0.94, height * 0.5)

    def click_checkbox_for_saving(self, index):
        """
        Check the checkobx for saving option:
        index==0: google drive option
        index==1: dropbox option
        """
        return self.driver.click("save_checkbox", index=index)
    
    def click_first_checkbox_for_saving(self):
        if self.driver.click("first_accounts_checkbox", raise_e=False) is False:
            self.driver.send_keys("first_accounts_checkbox", Keys.PAGE_DOWN)
            self.driver.click("first_accounts_checkbox")

    def click_google_drive_checkbox(self):
        """
        Check the Google drive checkobx for saving option:
        """
        self.driver.click("google_drive_checkbox", displayed=False)

    def click_dropbox_checkbox(self):
        """
        Check the Dropbox checkbox for saving option:
        """
        self.driver.click("dropbox_checkbox", displayed=False)

    def click_one_drive_checkbox(self):
        """
        Check the One Drive checkobx for saving option:
        """
        if not self.driver.wait_for_object("one_drive_checkbox", raise_e=False, timeout=3):
            self.driver.swipe("one_drive_checkbox")
        self.driver.click("one_drive_checkbox")
    
    def click_continue_btn(self):
        """
        Click on Continue button on Add Shortcut screen
        """
        self.driver.click("continue_btn", displayed=False)

    def click_file_type_btn(self):
        """
        Click on File Type button on Settings screen
        """
        self.driver.click("file_type_item")

    def click_files_type_back_btn(self):
        """
        Click on Back button from  File Type screen
        """
        self.driver.click("back_btn")

    def enter_shortcut_name(self, shortcut_name):
        """
        Input Shortcut name on Settings screen
        """
        self.driver.click("shortcut_name_item")
        self.driver.send_keys("shortcut_name_item", shortcut_name)
   
    def clear_shortcut_name(self, is_win=False):
        if not is_win:
            self.driver.selenium.js_clear_text("shortcut_name_item")
        else:
            self.driver.click("shortcut_name_item")
            self.driver.clear_text("shortcut_name_item", not_input=True)

    def click_save_shortcut_btn(self):
        """
        Click on Save Shortcut button on Settings screen
        """
        self.driver.click("save_shortcut_btn")
    
    def click_start_shortcut_btn(self):
        """
        Click on Start Shortcut button on Shortcut Saved screen
        """
        self.driver.click("start_shortcut_btn", timeout=15)
    
    def click_my_shortcuts_btn(self):
        """
        Click on Save Shortcut button on Shortcut Saved screen
        """
        self.driver.click("my_shortcuts_btn")
    
    def click_home_btn(self):
        """
        Click on Home button on Shortcut Saved screen
        """
        self.driver.click("home_btn")

    def format_shortcut_name(self, shortcut_name):
        # shortcut header changed to "shortcut-card-{name}" where name formatted as only lower case char, number, "-" and "_", 
        formatted_shortcut_name = re.sub('[^a-zA-Z0-9_]', "-", shortcut_name).lower()
        return formatted_shortcut_name

    def delete_single_shortcut(self, shortcut_name, is_delete=True, raise_e=True):
        """
        - Select any shortcut from shortcut list screen
        - Click on More Option screen
        - Click on Delete button, then can choose delete or cancel
        :param shortcut_name:
        :param is_delete: True or False
        """
        shortcut_name = self.format_shortcut_name(shortcut_name)
        try:
            self.select_shortcut(shortcut_name, click_obj=False)
            self.driver.click("shortcut_options_icon", format_specifier=[shortcut_name])
            self.driver.click("delete_btn")
            if is_delete:
                self.driver.click("delete_shortcut_popup_delete")
            else:
                self.driver.click("delete_shortcut_popup_cancel")
            return True
        except (TimeoutException, NoSuchElementException) as ex:
            if raise_e:
                raise ex
            return False

    def select_shortcut(self, shortcut_name, click_obj=True, raise_e=True):
        """
        :param shortcut_name:
        :param click_obj:
            True: click the object
            False: return the object
        :return:
        """
        shortcut_name = self.format_shortcut_name(shortcut_name)
        try:
            shortcut_obj = self.driver.wait_for_object("shortcut_card", format_specifier=[shortcut_name], raise_e=raise_e)
            if click_obj is True:
                shortcut_obj.click()
            else:
                return shortcut_obj
        except (TimeoutException, NoSuchElementException) as ex:
            if raise_e:
                raise ex
            return False

    def select_shortcuts_close_btn(self):
        self.driver.click("shortcuts_get_started_close_btn")

    def dismiss_coachmark(self, timeout=10, raise_e=False):
        if self.verify_coachmark_close_btn(timeout=timeout, raise_e=raise_e):
            if pytest.platform == "MAC":
                self.driver.click_using_frame("close_coachmark_btn", offset_x=5, offset_y=5)
            else:
                self.driver.click("close_coachmark_btn")

    def click_email_toggle(self):
        """
        Click the Email toggle.
        """
        # el = self.driver.find_object("email_item")
        # width, height = el.rect["width"], el.rect["height"]
        # self.driver.click_by_coordinates(el, width * 0.96, height * 0.455)
        self.driver.click("email_toggle_btn")

    def click_save_toggle(self):
        """
        Click the Save toggle.
        """
        self.driver.swipe("save_toggle_btn")
        # el = self.driver.find_object("save_item")
        # width, height = el.rect["width"], el.rect["height"]
        # self.driver.click_by_coordinates(el, width * 0.96, height * 0.455)
        self.driver.click("save_toggle_btn")

    def close_save_toggle(self):
        """
        close the Save item.
        """
        self.driver.swipe("save_toggle_btn", direction="up")
        # el = self.driver.find_object("save_item")
        # width, height = el.rect["width"], el.rect["height"]
        # self.driver.click_by_coordinates(el, width * 0.96, height * 0.455)
        self.driver.click("save_toggle_btn")

    def click_print_toggle(self):
        """
        Click the Print toggle.
        """
        self.driver.swipe("print_toggle_btn")
        # el = self.driver.find_object("print_item")
        # width, height = el.rect["width"], el.rect["height"]
        # self.driver.click_by_coordinates(el, width * 0.96, height * 0.455)
        self.driver.click("print_toggle_btn")
    
    def click_quick_run_checkbox(self):
        """
        Click Quick Run checkbox
        """
        self.driver.click("quick_run_checkbox")

    def select_tile_color(self, index):
        """
        Click Quick Run checkbox
        """
        self.driver.click("tile_color_item", format_specifier=[index])

    def get_current_shortcut_name(self):
        """
        Get current File Name 
        """
        file_name = self.driver.get_attribute("shortcut_name_item", attribute="Value.Value")
        return file_name

    def clear_email_subject_text(self):
        self.driver.clear_text("email_subject_box", not_input=True)

    def click_one_drive_sign_in_btn(self):
        self.driver.click("one_drive_sign_in_btn")

    # *********************************************************************************
    #                                ACTION FLOWS--Edit / Delete Shortcuts            *
    # *********************************************************************************

    def select_shortcut_more_option(self, shortcut_name):
        """
        Click on shortcut more option icon for the shortcut you need
        :param shortcut_name:
        """
        self.driver.click("shortcut_options_icon", format_specifier=[shortcut_name])

    def click_edit_btn(self):
        """
        Click on Edit button on Shortcut More Option screen
        """
        self.driver.click("edit_btn")

    def click_delete_btn(self):
        """
        Click on Delete button on Shortcut More Option screen
        """
        self.driver.click("delete_btn")

    def click_start_opt_btn(self):
        """
        Click on Start button on Shortcut More Option screen
        """
        self.driver.click("start_btn")

    def click_remove_btn(self):
        """
        Click on Remove button on Edit Shortcut more option screen
        """
        self.driver.click("remove_btn")

    def click_edit_delete_btn(self):
        """
        Click on Delete button on Edit Shortcut screen
        """
        self.driver.click("edit_delete_btn")

    def click_delete_popup_cancel_btn(self, is_win=False):
        """
        Click on Cancel button on Delete Shortcut popup screen
        """
        if not is_win:
            self.driver.selenium.js_click("delete_shortcut_popup_cancel", displayed=False)
        else:
            self.driver.click("delete_shortcut_popup_cancel")

    def click_delete_popup_delete_btn(self, is_win=False):
        """
        Click on Delete button on Delete Shortcut popup screen
        """
        if not is_win:
            self.driver.selenium.js_click("delete_shortcut_popup_delete", displayed=False)
        else:    
            self.driver.click("delete_shortcut_popup_delete")

    def click_edits_more_option_btn(self):
        """
        Click on 3 dots icon on Edit Shortcut screen
        """
        self.driver.click("edit_more_option_btn", timeout=5)

    def click_edits_more_option_another_btn(self):
        """
        Click on 3 dots icon on Edit Shortcut screen
        """
        self.driver.click("edit_more_option_another_btn")

    def check_shortcut_item_name(self, num):
        """
        Click on 3 dots icon on Edit Shortcut screen
        """
        return self.driver.get_attribute("shortcut_group_item", attribute="AutomationId", format_specifier=[num], raise_e=False)

    def click_shortcut_option_btn(self, num=2):
        """
        Click on 3 dots icon on Edit Shortcut screen
        """
        self.driver.click("shortcut_group_option_btn", format_specifier=[num])

    def click_remove_popup_remove_btn(self):
        """
        Click on Remove button on Remove Shortcut popup screen
        """
        self.driver.selenium.js_click("remove_shortcut_popup_remove", displayed=False)

    def click_remove_popup_cancel_btn(self):
        """
        Click on Cancel button on Remove Shortcut popup screen
        """
        self.driver.selenium.js_click("remove_shortcut_popup_remove", displayed=False)

    def click_edit_save_btn(self):
        """
        Click on Save button on Edit Print / Edit Email / Edit Save screen
        """
        self.driver.click("save_btn", change_check={"wait_obj": "save_btn", "invisible": True})

    def click_edits_cancel_popup_yes_btn(self, is_win=False):
        """
        Click on Yes, Cancel Edits button on Edits Cancel popup screen
        """
        if not is_win:
            self.driver.selenium.js_click("yes_cancel_edits_btn", displayed=False)
        else:
            self.driver.click("yes_cancel_edits_btn")

    def click_edits_cancel_popup_no_btn(self, is_win=False):
        """
        Click on No, Continue Edits button on Edits Cancel popup screen
        """
        if not is_win:
            self.driver.selenium.js_click("no_continue_edits_btn", displayed=False)
        else:
            self.driver.click("no_continue_edits_btn")

    def click_copies_dropdown(self):
        """
        Click copies dropdown
        """
        self.driver.click("copies_label")

    def click_color_dropdown(self):
        """
        Click color dropdown
        """
        self.driver.click("color_label")

    def click_two_sided_dropdown(self):
        """
        Click Two-sided dropdown
        """
        self.driver.click("two-sided_label")

    def click_remove_listitem(self):
        """
        Click dropdown listitem
        """
        self.driver.click("remove_listitem")

    

    # *********************************************************************************
    #                                ACTION FLOWS--Shortcuts Access       *
    # *********************************************************************************
    def click_enable_btn(self):
        """
        Click on Enable button on Shortcuts screen
        """
        self.driver.click("enable_button")

    def click_close_btn(self):
        """
        Click on Close button on Shortcuts screen
        """
        self.driver.click("close_button")

    def click_settings_btn(self):
        """
        Click on Settings icon on Shortcuts screen
        """
        self.driver.click("settings_button")

    def click_more_access_options_btn(self):
        """
        Click on More Options icon on Access Shortcuts screen
        """
        self.driver.selenium.js_click("more_options_button", displayed=False)

    def click_access_off_option(self):
        """
        Click on Access Off option on Access Shortcuts screen
        """
        self.driver.selenium.js_click("access_off_option", displayed=False)

    def click_one_year_most_convenient_option(self):
        """
        Click on 1 year -- most convenient option on Access Shortcuts screen
        """
        self.driver.selenium.js_click("1_year_most_convenient_option", displayed=False)

    def click_one_day_most_secure_option(self):
        """
        Click on 1 day -- most secure option on Access Shortcuts screen
        """
        self.driver.selenium.js_click("1_day_most_secure_option", displayed=False)

    def click_custom_option(self):
        """
        Click on 1 day -- most secure option on Access Shortcuts screen
        """
        self.driver.selenium.js_click("custom_option", displayed=False)

    def click_date_picker(self):
        self.driver.click("date_picker_calendar_button")

    def click_next_month(self):
        self.driver.click("next_month_btn")
    
    def pick_custom_date(self):
        self.click_custom_option()
        self.click_date_picker()
        self.click_next_month()
        self.driver.click("first_day_of_second_month_btn")

    def click_fewer_options_btn(self):
        """
        Click on Fewer Options icon on Access Shortcuts screen
        """
        self.driver.selenium.js_click("fewer_options_button", displayed=False)

    def click_ok_btn(self):
        """
        Click the Ok button on the Access Shortcuts Enabled/Disabled screen
        """
        self.driver.click("shortcuts_access_enabled_ok_button")

    def click_printer_access_arrow_btn(self, timeout=10):
        """
        Click on Printer Access arrow button on Shortcuts screen
        """
        self.driver.click("access_expires_arrow_button", timeout=timeout)

    def click_already_exists_no_btn(self):
        """
        Verify "" already exists screen:
        Do you want to rename this shortcut to avoid confusion?
        No / Rename Button
        """
        self.driver.click("already_exists_no_btn")

    def click_already_exists_rename_btn(self):
        """
        Verify "" already exists screen:
        Do you want to rename this shortcut to avoid confusion?
        Click Rename Button
        """
        self.driver.click("already_exists_rename_btn")

    def dismiss_connecting_to_service_dialog(self):
        """
        click close button on connecting to a service screen
        """
        if self.driver.wait_for_object("connecting_to_service_title", raise_e=False):
            sleep(3)
            self.driver.click("dialog_close_btn")

    def click_shortcuts_title(self):
        self.driver.click("shortcuts_title")

    def click_onedrive_menu_btn(self):
        self.driver.swipe("onedrive_menu_btn", direction="up")
        sleep(3)
        self.driver.click("onedrive_menu_btn")

    def click_right_arrow_btn(self):
        self.driver.click("right_arrow_btn")

    def click_left_arrow_btn(self):
        self.driver.click("left_arrow_btn")

    def click_tick_btn(self):
        self.driver.click("tick_btn")

    def click_dialog_return_to_home_btn(self):
        self.driver.click("dialog_return_to_home_btn")

    def click_dialog_cancel_btn(self):
        self.driver.click("dialog_cancel_btn")

    def click_skip_printing_btn(self):
        self.driver.click("skip_printing_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_shortcuts_screen(self, timeout=25):
        """
        Verify current screen is Shortcuts screen via:
            - title
            - Add Shortcut button
        """
        self.driver.wait_for_object("shortcuts_title", timeout=timeout, displayed=False)
        if pytest.platform == "MAC":
            self.dismiss_coachmark(timeout=timeout)
        self.driver.wait_for_object("add_shortcuts_btn", timeout=timeout)
    
    def verify_shortcuts_title(self, timeout=10):
        self.driver.wait_for_object("shortcuts_title", timeout=timeout, displayed=False)

    def verify_empty_shortcuts_screen(self):
        """
        Verify current screen is empty Shortcuts screen via:
            - title
            - Body message "Save time with Shortcuts....."
            - Add Shortcut button
        """
        # sleep(20)
        if not self.driver.wait_for_object("save_time_with_shrotcuts_icon", raise_e=False, timeout=60):
            self.click_edits_more_option_btn()
            self.click_delete_btn()
            self.verify_shortcut_delete_screen()
            self.click_delete_popup_delete_btn(is_win=True)
        self.driver.wait_for_object("shortcuts_title")
        self.driver.wait_for_object("save_time_with_shrotcuts_icon")
        self.driver.wait_for_object("add_shortcuts_btn")

    def verify_coachmark_close_btn(self, timeout=10, raise_e=False):
        return self.driver.wait_for_object("close_coachmark_btn", timeout=timeout, raise_e=raise_e)

    def verify_shortcuts_list_screen(self, timeout=10):
        """
        Verify current screen is Shortcuts list screen via:
            - title
            - Shortcut List button
        """
        self.driver.wait_for_object("shortcuts_list", timeout=timeout)
    
    # issue on iOS: two webview contexts with different urls (shortcuts help screen and shortcuts screen) on the same page
    # TODO: add decorator to specify the webview context this function applies
    # change context parameter of shortcuts in the flow container this after the fix
    def verify_shortcuts_help_screen(self, timeout=10):
        """
        Verify current screen is Shortcuts Help screen via:
            - message
        """
        if pytest.platform.lower() == "ios":
            self.driver.switch_to_webview()
        self.driver.wait_for_object("shortcuts_help_message", timeout=timeout)

    def verify_printer_problem_dialog(self, scene=None, no_printer=False):
        """
        Verify the "Printer Problem" dialog shows with some scene
        """
        self.driver.wait_for_object("printer_problem_dialog_title")
        if scene == "Print destination only":
            self.driver.wait_for_object("dialog_cancel_btn")
            if no_printer:
                self.driver.wait_for_object("printer_problem_dialog_text_3")
            else:
                self.driver.wait_for_object("printer_problem_dialog_text_1")
                self.driver.wait_for_object("dialog_return_to_home_btn")
        else:
            self.driver.wait_for_object("dialog_cancel_btn")
            self.driver.wait_for_object("skip_printing_btn")
            if no_printer:
                self.driver.wait_for_object("printer_problem_dialog_text_4")
            else:
                self.driver.wait_for_object("printer_problem_dialog_text_2")
                self.driver.wait_for_object("dialog_return_to_home_btn")

    def verify_printer_offline_dialog(self, scene=None):
        """
        Verify the "Printer is offline" dialog shows with some scene
        """
        self.driver.wait_for_object("Printer_offline_dialog_title")
        self.driver.wait_for_object("dialog_cancel_btn")
        if scene == "Print destination only":
            self.driver.wait_for_object("printer_offline_dialog_text_1")
        else:
            self.driver.wait_for_object("printer_offline_dialog_text_2")
            self.driver.wait_for_object("skip_printing_btn")

    # -------------------       Edit / Remove Shortcuts  ---------------------------------------
    def verify_edit_shortcut_screen(self):
        """
        Verify current screen is Edit Shortcut screen via:
            - title
            - Shortcut destinations list
            - Continue button
            - Delete button
        """
        self.driver.wait_for_object("edit_shortcut_title")
        self.driver.wait_for_object("edit_shortcut_destinations")
        self.driver.wait_for_object("edit_delete_btn")
        self.driver.wait_for_object("continue_btn")

    def verify_shortcut_delete_screen(self):
        """
        Verify current screen is Shortcut delete popup screen via:
            - title
        """
        self.driver.wait_for_object("delete_popup_title", displayed=False)

    def verify_shortcut_cancel_edits_popup(self):
        """
        Verify current screen is Cancel Edits popup screen via:
            - title
            - Yes, Cancel Edits button
            - No, Continue Edits button
        """
        self.driver.wait_for_object("are_you_sure_popup", displayed=False)
        self.driver.wait_for_object("yes_cancel_edits_btn", displayed=False)
        self.driver.wait_for_object("no_continue_edits_btn", displayed=False)

    def verify_shortcut_remove_edits_popup(self):
        """
        Verify current screen is Remove destination popup screen via:
            - title
            - remove button
            - cancel button
        """
        self.driver.wait_for_object("remove_popup_title", displayed=False)
        self.driver.wait_for_object("remove_shortcut_popup_remove", displayed=False)
        self.driver.wait_for_object("remove_shortcut_popup_cancel", displayed=False)

    def verify_edit_print_screen(self):
        """
        Verify current screen is Edit Print screen via:
            - Message "Print your scanned files to the..."
            - Cancel button
            - Body Item
        """
        self.driver.wait_for_object("edit_print_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("copies_label")
        self.driver.wait_for_object("color_label")
        self.driver.wait_for_object("two-sided_label")

    def verify_edit_email_screen(self):
        """
        Verify current screen is Edit Save screen via:
            - Title
            - Send To item
            - Subject item
        """
        self.driver.wait_for_object("edit_email_title")
        self.driver.wait_for_object("email_receive_box")
        self.driver.wait_for_object("email_subject_box")

    def verify_edit_save_screen(self):
        """
        Verify current screen is Edit Save screen via:
            - Message "Send your scanned files to your...."
            - Dropbox Item
            - Google Drive item
        """
        self.driver.wait_for_object("edit_save_title", timeout=20)
        self.driver.wait_for_object("dropbox_item")
        self.driver.wait_for_object("google_drive_item")

    # -------------------       Create You own Shortcuts  ---------------------------------------
    def verify_add_shortcuts_screen(self):
        """
        Verify current screen is Add Shortcut screen via:
            - title
            - Create your own shortcut item
            - Save to Google Drive item
            - Print, Email, and Save item
        """
        self.driver.wait_for_object("add_shortcuts_title")
        self.driver.wait_for_object("create_your_own_shortcut_btn")
        self.driver.wait_for_object("save_to_google_drive_btn")
        self.driver.wait_for_object("print_email_and_save_btn")
    
    def verify_add_your_own_shortcut_screen(self):
        """
        Verify current screen is Add your own Shortcut screen via:
            - title
            - Print item
            - Email item
            - Save item
        """
        self.driver.wait_for_object("add_shortcuts_title")
        self.driver.wait_for_object("print_item")
        self.driver.wait_for_object("email_item")
        self.driver.wait_for_object("save_item")
    
    def verify_add_print_screen(self):
        """
        Verify current screen is Add Print screen via:
            - Title
            - Cancel button
            - Body Item
        """
        self.driver.wait_for_object("add_print_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("copies_label")
        self.driver.wait_for_object("color_label")
        self.driver.wait_for_object("two-sided_label")
    
    def verify_add_email_screen(self):
        """
        Verify current screen is Add Email screen via:
            - Title
            - Send To item
            - Subject item
        """
        if pytest.platform != "MAC":
            self.driver.wait_for_object("add_email_title")
        self.driver.wait_for_object("email_receive_box")
        self.driver.wait_for_object("email_subject_box")

    def verify_invalid_email_message_screen(self):
        """
        Verify invalid email address message popup
        """
        self.driver.wait_for_object("invalid_email_message")
    
    def verify_add_save_screen(self):
        """
        Verify current screen is Add Save screen via:
            - Title
            - Dropbox Item
            - Google Drive item
        """
        self.driver.wait_for_object("add_save_title")
        self.driver.wait_for_object("dropbox_item", timeout=20)
        self.driver.wait_for_object("google_drive_item")

    def verify_shortcuts_cancel_popup(self, timeout=10):
        """
        Verify current screen is Shortcuts cancel popup screen via:
            - Message
            - Yes, Cancel Shortcut button
            - No, Continue Shortcut button
        """
        self.driver.wait_for_object("are_you_sure_popup", timeout=timeout)
        self.driver.wait_for_object("yes_cancel_shortcut_btn")
        self.driver.wait_for_object("no_continue_shortcut_btn")
    
    def verify_settings_screen(self, invisible=False):
        """
        Verify current screen is Settings screen via:
            - Title
            - File Type (depends on printer connected or not)
            - Shortcut Name
        """
        self.driver.wait_for_object("settings_title")
        self.driver.wait_for_object("shortcut_name_item")
        self.driver.wait_for_object("file_type_item", invisible=invisible)
        self.driver.wait_for_object("shortcut_list_tile_color")

    def verify_file_type_screen(self):
        """
        Verify current screen is File Type screen via:
            - Title
            - Image (p.jpg)
            - PDF
        """
        if pytest.platform.lower() == "android":
            self.driver.swipe()
        else:
            self.driver.swipe("file_type_title")
        self.driver.wait_for_object("file_type_title")
        self.driver.wait_for_object("image_jpg_item")
        self.driver.wait_for_object("pdf_item")
    
    def verify_shortcut_saved_screen(self, timeout=10, is_first_time=False):
        """
        Verify current screen is Shortcut Saved screen via:
            - Title
            - Start Shortcut button
            - My Shortcuts button
            - Home button
        """
        self.driver.wait_for_object("home_btn", timeout=timeout)
        self.driver.wait_for_object("my_shortcuts_btn")
        self.driver.wait_for_object("start_shortcut_btn")
        if not is_first_time:
            self.driver.wait_for_object("shortcut_saved_title")
        else:
            self.driver.wait_for_object("you_just_created_title")
    
    def change_email_subject_text(self, text):
        self.driver.send_keys("email_subject_box", text)
    
    def open_shortcuts_menu(self, shortcut_name):
        shortcut_name = self.format_shortcut_name(shortcut_name)
        self.driver.click("shortcut_options_icon", format_specifier=[shortcut_name])
    
    def verify_shortcuts_option_menu(self):
        sleep(10)
        self.driver.wait_for_object("start_btn", timeout=20)
        self.driver.wait_for_object("edit_btn")
        self.driver.wait_for_object("delete_btn")
    
    def verify_invalid_shortcut_name_text(self, raise_e=True):
        return self.driver.wait_for_object("shortcut_name_invalid_txt", raise_e=raise_e, displayed=False)
    
    def verify_shortcut_name_required_txt(self, raise_e=True):
        return self.driver.wait_for_object("shortcut_name_required_txt", raise_e=raise_e, displayed=False)

    def verify_edit_shortcut_screen_for_win(self):
        self.driver.wait_for_object("edit_delete_btn", timeout=20)
        self.driver.wait_for_object("edit_cancel_btn")
        self.driver.wait_for_object("save_shortcut_btn")
        assert self.driver.get_attribute("shortcuts_title", attribute="Name") =="Edit Shortcut"

    def verify_save_toggle_is_on(self):
        self.driver.swipe("save_detail")
        self.driver.wait_for_object("save_detail")

    def verify_print_toggle_is_on(self):
        self.driver.wait_for_object("print_detail")

    def verify_email_toggle_is_on(self):
        self.driver.wait_for_object("email_detail")
        self.driver.wait_for_object("email_body_box")
        self.driver.wait_for_object("email_receive_box")
        self.driver.wait_for_object("email_subject_box")

    def verify_all_the_toggles_is_on(self):
        self.verify_print_toggle_is_on()
        self.verify_email_toggle_is_on()
        self.verify_save_toggle_is_on()

    def verify_file_type_screen_not_show(self):
        if self.driver.wait_for_object("file_type_title", raise_e=False):
            raise NoSuchElementException("File Type section display")
        return True

    def verify_save_shortcuts_btn(self, is_enabled=True):
        """
        Verify "Save Shortcut" button is disabled or enabled
        """
        value = self.driver.get_attribute("save_shortcut_btn", attribute="IsEnabled")
        if is_enabled:
            assert value.lower() == "true"
        else:
            assert value.lower() == "false"

    def verify_email_icon(self):
        self.driver.wait_for_object("email_icon_image")

    def verify_printer_icon(self):
        self.driver.wait_for_object("printer_icon_image")

    def verify_dropdown_listitem(self, name):
        return self.driver.wait_for_object("dynamic_listitem", format_specifier=[name])

    def verify_remove_hp_smart_access_dialog(self):
        self.driver.wait_for_object("remove_hp_smart_access_title")

    def verify_color_settings_opt(self):
        self.driver.wait_for_object("color_option")
        self.driver.wait_for_object("grayscale_option")

    def verify_two_sided_settings_opt(self):
        self.driver.wait_for_object("off_option")
        self.driver.wait_for_object("short_edge_option")
        self.driver.wait_for_object("long_edge_option")
    
    def verify_copies_settings_opt(self):
        for num in range(50):
            self.driver.wait_for_object("copies_option", format_specifier=[num], displayed=False)

    def verify_invalid_emails_txt(self):
        self.driver.wait_for_object("invalid_emails_txt")
        
    # -------------------       Shortcuts Access Off through Shortcuts tile ---------------------------------------
    def verify_shortcuts_access_off_item(self, invisible=False):
        """
        Verify Shortcuts Access Off item on Shortcuts screen with:
        - Shortcut Access Off
        - Enable button
        - X button
        """
        self.driver.wait_for_object("shortcuts_access_off", invisible=invisible, displayed=False)
        self.driver.wait_for_object("enable_button", invisible=invisible)
        self.driver.wait_for_object("close_button", invisible=invisible)

    def verify_access_shortcuts_screen(self, timeout=10):
        """
        Verify Access Shortcuts screen with:
        - Access Shortcuts title
        - Access Off option
        - 1 year--Most convenient option
        - Save button
        """
        self.driver.wait_for_object("access_shortcuts_title", timeout=timeout)
        self.driver.wait_for_object("access_shortcuts_body")
        self.driver.wait_for_object("access_off_option", displayed=False)
        self.driver.wait_for_object("1_year_most_convenient_option", displayed=False)
        self.driver.wait_for_object("save_btn")

    def verify_custom_option(self, invisible=False):
        """
        Verify Custom option displays on Access Shortcuts screen or not
        """
        self.driver.wait_for_object("custom_option", invisible=invisible, displayed=False)

    def verify_one_day_most_secure_option(self, invisible=False):
        """
        Verify 1 day--Most secure option displays on Access Shortcuts screen or not
        """
        self.driver.wait_for_object("1_day_most_secure_option", invisible=invisible, displayed=False)

    def verify_access_expiring_message_with_one_year_option(self):
        """
        Verify Expiring message in 365 days on Printer Access item
        """
        self.driver.wait_for_object("printer_access_item")
        self.driver.wait_for_object("access_expires_in_message")
        self.driver.wait_for_object("365_days_message")

    def verify_shortcuts_access_enabled_screen(self):
        """
        Verify Shortcuts Access Enabled screen with:
        - Shortcut Access Off
        - Enable button
        - X button
        """
        self.driver.wait_for_object("shortcuts_access_enabled_title")
        self.driver.wait_for_object("shortcuts_access_enabled_message")
        self.driver.wait_for_object("shortcuts_access_enabled_ok_button")

    def verify_shortcuts_access_disabled_screen(self):
        """
        Verify Shortcuts Access Disabled screen with:
        - Shortcut Access Off
        - Enable button
        - X button
        """
        self.driver.wait_for_object("shortcuts_access_disabled_title")
        self.driver.wait_for_object("shortcuts_access_disabled_message")
        self.driver.wait_for_object("shortcuts_access_enabled_ok_button")

    def verify_shortcuts_get_started_screen_without_printer(self):
        # w/o printer selected
        # The screen shows after clicking shortcuts tile.
        self.driver.wait_for_object("shortcuts_get_started_image")
        self.driver.wait_for_object("shortcuts_get_started_create_account_btn")
        self.driver.wait_for_object("shortcuts_get_started_sign_in_btn")
        self.driver.wait_for_object("shortcuts_get_started_close_btn")

    def verify_save_shortcut_screen(self):
        """
        Verify the current screen is Save shortcut screen.
        """
        self.driver.wait_for_object("shortcut_name_item", timeout=30)
        self.driver.wait_for_object("save_shortcut_btn")

    def verify_not_empty_shortcuts_screen(self):
        """
        Verify the current screen is Not Empty Shortcuts screen.
        """
        self.driver.wait_for_object("add_shortcuts_btn", timeout=60)
        assert self.driver.wait_for_object("save_time_with_shrotcuts_icon", raise_e=False) is False

    def verify_limited_email_message(self, raise_e=True):
        """
        Verify limited email address message popup
        """
        return self.driver.wait_for_object("limited_email_message", raise_e=raise_e, displayed=False)

    def verify_default_shortcuts_shows(self):
        """
        Verify "Default" Shortcut tile shows
        """
        self.driver.wait_for_object("coach_mark_dialog", timeout=120)
        self.verify_email_icon()

    def verify_coach_mark_dialog_page_1(self):
        """
        Verify coach mark dialog UI
        """
        self.driver.wait_for_object("right_arrow_btn")

    def verify_coach_mark_dialog_page_2(self):
        """
        Verify coach mark dialog UI
        """
        self.driver.wait_for_object("right_arrow_btn")
        self.driver.wait_for_object("left_arrow_btn")

    def verify_coach_mark_dialog_page_3(self):
        """
        Verify coach mark dialog UI
        """
        self.driver.wait_for_object("left_arrow_btn")
        self.driver.wait_for_object("tick_btn")

    def verify_no_shortcuts_job(self, raise_e=False):
        """
        Verify the current screen is Empty Shortcuts screen.
        """
        return self.driver.wait_for_object("save_time_with_shrotcuts_icon", raise_e=raise_e)

    def verify_dynamic_shortcuts_item(self, file_name):
        return self.driver.click("dynamic_shortcuts_item", format_specifier=[file_name], raise_e=False) 
 
    # -------------------       Shortcuts Access Off through Printer Settings ---------------------------------------
    def verify_printer_access_off_message(self, timeout=20):
        """
        Verify Access Off message on Printer Access item
        """
        # from Printer Settings screen to Shortcut Access webview screen, it needs time to load it
        self.driver.wait_for_object("printer_access_item", timeout=timeout)
        # self.driver.wait_for_object("access_off_status")


class MobileShortcutsCreateEdit(Shortcuts_Create_Edit):
    context = "NATIVE_APP"

    def click_camera_btn(self):
        """
        Click on Camera button on source select screen
        """
        self.driver.click("camera_option")

    def click_scanner_btn(self):
        """
        Click on Scanner button on source select screen
        """
        self.driver.click("scanner_option")

    def click_files_photo_btn(self):
        """
        Click on Files & Photos button on source select screen
        """
        self.driver.click("files_photo_option")

    def click_x_btn(self):
        """
        Click on X button on source select screen
        """
        self.driver.click("close_btn")

    def click_start_btn(self):
        """
        Click on Start XXX on Shortcuts Preview screen
        """
        self.driver.click("start_shortcuts", timeout=10)

    def click_i_icon(self):
        """
        Click on i icon on Shortcuts Preview screen
        """
        self.driver.click("info_btn")

    def click_shortcuts_home_btn(self):
        """
        Click on Home button on Your Shortcuts is in progress screen
        """
        self.driver.click("shortcuts_home_btn")

    def click_activity_btn(self):
        """
        Click on Activity button on Your Shortcuts is in progress screen
        """
        self.driver.click("shortcuts_activity_center_btn")

    def click_more_options_btn(self):
        """
        Click on More Options button on Your Shortcuts is in progress screen
        """
        self.driver.click("shortcuts_more_options_btn")

    def click_yes_cancel_shortcut_btn(self):
        """
        Click on Yes, Cancel Shortcut button on Shortcut cancel popup screen
        """
        self.driver.click("yes_cancel_shortcut_btn")

    def click_no_continue_shortcut_btn(self):
        """
        Click on Yes, Cancel Shortcut button on Shortcut cancel popup screen
        """
        self.driver.click("no_continue_shortcut_btn")
    
    def click_info_icon(self):
        """
        Click on info icon 'i' on the preview page
        """
        self.driver.click("info_icon")

    def verify_source_select_popup(self):
        """
        Verify current screen is Source Select popup screen via:
            - Message
            - Camera Scan option
            - Files & Photos Option
        """
        self.driver.wait_for_object("source_select_message")
        self.driver.wait_for_object("camera_option")
        self.driver.wait_for_object("files_photo_option")

    def dismiss_source_select_popup(self, raise_e=False):
        """
        Dismisses the source select popup if the Select Source Dialog appears
        """
        if self.driver.wait_for_object("source_select_message", raise_e=raise_e, timeout=5):
            self.click_x_btn()

    def verify_shortcuts_start_preview_screen(self, timeout=15):
        """
        Verify current screen is Shortcuts Start Preview screen via:
            - Photo name
            - Start Shortcuts Name button
        """
        self.driver.wait_for_object("file_name")
        self.driver.wait_for_object("start_shortcuts", timeout=timeout)

    def verify_your_file_is_being_uploaded_popup(self, timeout=5, raise_e=False):
        """
        Verify current screen is Your file is being uploaded for processing screen
        """
        self.driver.wait_for_object("shortcuts_your_file_is_being_uploaded_message", timeout=timeout, raise_e=raise_e)

    def verify_your_shortcut_is_in_progress_screen(self, timeout=25):
        """
        Verify current screen is Your Shortcut is in progress screen via:
            - Message
            - Home button
            - Activity Center button
            - Continue button
        """
        self.driver.wait_for_object("shortcuts_in_process_message", timeout=timeout)
        self.driver.wait_for_object("shortcuts_home_btn")
        self.driver.wait_for_object("shortcuts_activity_center_btn")
        if pytest.platform.lower() == "ios":
            self.driver.wait_for_object("continue_btn")
        else:
            self.driver.wait_for_object("shortcuts_more_options_btn")
    
    def verify_shortcut_coachmark_and_dismiss(self):
        """
        Verify Shortcuts coachmark that appears after clicking "i" button
        """
        self.driver.wait_for_object("shortcut_coachmark")
        self.dismiss_coachmark(raise_e=True)

    def verify_info_btn(self):
        self.driver.wait_for_object("info_btn")

    def verify_file_already_exists_dialog(self):
        """
        Verify "" already exists screen:
        Do you want to rename this shortcut to avoid confusion?
        No / Rename Button
        """
        return self.driver.wait_for_object("already_exists_rename_btn", raise_e=False) and \
               self.driver.wait_for_object("already_exists_no_btn", raise_e=False) and \
               self.driver.wait_for_object("already_exists_title", raise_e=False)
    
    def verify_delete_shortcuts_dialog_disapper(self):
        self.driver.wait_for_object("delete_popup_title", invisible=True, timeout=10)

    def click_dynamic_three_dot(self, file_name):
        return self.driver.click("dynamic_three_dot", format_specifier=[file_name], raise_e=False)
    
    def click_done_button(self, timeout=10, raise_e=False):
        return self.driver.click("info_screen_done_button", raise_e=raise_e, timeout=timeout)

    def click_shortcuts_help_expand_page_btn(self):
        """
        From the Help Page, click on the arrow expanding the Shortcuts Help page
        """
        if pytest.platform == "IOS":
            # Perform a call to scroll after swipe so that the UI element for Shortcuts Expand is found and then clicked on
            for i in range(2):
                self.driver.swipe(check_end=True)
            self.driver.scroll("shortcuts_expand_help_message", click_obj=True, timeout=30)
        else:
            self.driver.scroll("shortcuts_expand_help_message", click_obj=False, timeout=30)
            #sometimes the click one time doesn't work, so need to use click function with retry function
            self.driver.click("shortcuts_expand_help_message")

    def click_connecting_to_your_printer_expand_page_btn(self, clickable=False):
        """
        From the Help Page, try to find the Connecting to Your Printer section
        """
        # permission screen displays sometimes
        self.driver.click("accept_btn", timeout=15, raise_e=False)
        self.driver.scroll("connecting_to_your_printer", click_obj=clickable)

    # --------------------- verify shortcuts navigation ----------------------------------

    def verify_sign_in_page(self, timeout=10):
        """
        Verify Sign in page:
        """
        return self.driver.wait_for_object("sign_in_title", timeout=timeout)

    def verify_create_account_page(self, timeout=10):
        """
        Verify Create Account page:
        """
        return self.driver.wait_for_object("create_account_title", timeout=timeout)
    
    def verify_email_toggle(self, raise_e=False):
        return self.driver.wait_for_object("email_toggle_btn", raise_e=raise_e, timeout=10)

class MACShortcutsCreateEdit(MobileShortcutsCreateEdit):

    def click_print_btn(self):
        """
        Click on Print item button on Add Shortcut screen
        """
        frame = self.driver.get_attribute("print_item", "frame")
        self.driver.click_using_frame("print_item", offset_x=frame['width'] * 0.97)
    
    def select_color(self, color_btn):
        """
        Select Color on Add Print screen
        True: Color
        False:Grayscale
        COLOR_BTN = "color_option"
        GRAYSCALE_BTN = "grayscale_option"
        """
        self.driver.click("color_label")
        frame = self.driver.get_attribute("color_label", "frame")
        button_frame = self.driver.get_attribute(color_btn, "frame")
        self.driver.click_by_coordinates(x=frame["x"] + frame["width"] // 2, y=button_frame["y"] + 10)
    
    def click_email_btn(self):
        """
        Click on Email button on source select screen
        """
        frame = self.driver.get_attribute("email_item", "frame")
        self.driver.click_using_frame("email_item", offset_x=frame["width"] * 0.97)

    def enter_email_receiver(self, to_email):
        self.driver.click_using_frame("email_receive_box")
        self.driver.execute_script("macos:keys", {"keys": list(to_email)})
    
    def enter_shortcut_name(self, name):
        self.driver.click_using_frame("shortcut_name_item")
        self.driver.execute_script("macos:keys", {"keys": list(name)})
    
    def click_save_shortcut_btn(self):
        """
        Click on Save Shortcut button on Settings screen
        """
        self.driver.click_using_frame("save_shortcut_btn")
    
    def click_home_btn(self):
        """
        Click on Home button on Shortcut Saved screen
        """
        self.driver.click_using_frame("home_btn", timeout=15)