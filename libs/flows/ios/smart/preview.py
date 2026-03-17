import logging
import time
import re
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc.ma_misc import format_printer_name
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from MobileApps.resources.const.ios.const import OBJECT_SIZE

class InvalidElementNameException(Exception):
    pass

class Preview(SmartFlow):
    flow_name = "preview"

    # top header bar
    BACK_BUTTON = "_shared_back_arrow_btn"
    CANCEL_BUTTON = "_shared_cancel"
    DONE_BUTTON = "_shared_done"
    PREVIEW_TITLE = "preview_txt"
    PRINT_PREVIEW_TITLE = "print_preview"
    SHARE_AND_SAVE_TEXT = "share_save_text"
    SMART_TASKS_PREVIEW_TITLE = "smart_tasks_preview"
    SAVE_PREVIEW_TITLE = "save_preview"
    REORDER_BUTTON = "reorder_btn"
    FAX_PREVIEW_TITLE = "fax_preview"
    CONTINUE_TO_FAX_BTN = "continue_to_fax_btn"
    REDACTION_TITLE = "redaction"
    TEXT_EXTRACT_TITLE = "text_extract"

    # middle
    EDIT_BUTTON = "edit_btn"
    ADD_PAGE_BUTTON = "add_page_btn"
    ROTATE_BUTTON = "rotate_btn_txt"
    REDACT_BUTTON = "redact_btn"
    TEXT_EXTRACT_BUTTON = "text_extract"
    SCRIBBLE_BUTTON = "scribble_btn"

    PAPER_SIZE_INFO = "paper_size_info"
    PREVIEW_IMAGE = "image_of_preview"
    PRINTER_NAME = "printer_name"
    PDF_BUTTON = "_const_file_type_pdf"
    JPG_BUTTON = "_const_file_type_jpg"
    FILE_NAME_FIELD = "file_name_textfield"
    FILE_SIZE_SMALL = "file_size_small"
    FILE_SIZE_ACTUAL = "file_size_actual"
    FILE_SIZE_MEDIUM = "file_size_medium"
    FILE_SIZE_LARGE = "file_size_large"
    ADD_PASSWORD_PROTECTION = "add_password_protection"

    # bottom navigation bar
    PRINT = "print_text"
    SMART_TASKS = "smart_tasks_text"
    SHARE_AND_SAVE_BTN = "share_btn"
    FAX = "fax_text"

    SMART_TASKS_SIGN_IN = "smart_tasks_sign_in_link"

    # action success popup
    GREEN_CHECK_ICON = "print_completed_icon"
    CONTINUE_BUTTON = "continue_btn"
    HOME_BUTTON = "home_btn"

    # dynamic locators
    DYNAMIC_PREVIEW_BUTTON = "_shared_dynamic_button"
    DYNAMIC_PREVIEW_TOOLBAR = "dynamic_toolbar_icons"

    # Share Screen
    FILE_NAME_TITLE = "file_name_title"
    FILE_SETTINGS_TITLE = "file_settings_title"
    # TODO: FORMAT string refactoring in next sprint
    FORMAT = "file_type"
    FILE_SIZE = "file_size"
    SHARE_SETTINGS_TIP = "share_settings_tip"
    FILE_SIZE_ACTUAL = "file_size_actual"
    FILE_SIZE_MEDIUM = "file_size_medium"
    FILE_SIZE_LARGE = "file_size_large"
    FILE_SIZE_SMALL = "file_size_small"
    SHARE_SAVE_BTN = "share_save_text"

    # Print Screen
    RE_PRINT_BTN = "re_print_btn"
    YES_BTN = "yes_btn"
    NO_BTN = "no_btn"
    CANCEL_JOB_POP_UP_TITLE = "print_job_cancel_pop_up_title"
    CANCEL_JOB_POP_DES = "print_job_cancel_pop_up_txt"

    # Transform Screen
    TF_RESIZE_TXT = "resize_and_move_btn_txt"
    TF_ROTATE_TXT = "rotate_btn_txt"
    TF_COLLECTION_VIEW = "transform_collection_view"

    # print settings screen
    PRINT_SETTING_OPTIONS = "print_setting_options"
    PRINT_COPY = "print_copy_txt"
    COPIES_MINUS_BTN = "copies_minus_btn"
    COPIES_PLUS_BTN = "copies_plus_btn"
    PAPER = "paper_txt"
    COLOR_OPTION = "color_option_txt"
    PAGE_RANGE = "page_range_txt"
    PRINT_QUALITY = "print_quality_txt"
    TWO_SIDED = "two_sided_txt"
    PR_SCREEN_OPTIONS_UI = "page_range_options"
    PR_PAGE_SELECT_IMG = "page_selected_image"

    DELETE_PAGE_ICON = "delete_page_icon"
    REPLACE_BTN = "replace_btn"
    DELETE_BTN = "delete_btn"

    ROTATE_UPSIDEDOWN_ICON = "rotate_upsidedown_icon"
    ROTATE_RIGHT_ICON = "rotate_right_icon"

    SEARCHABLE_PDF = "searchable_pdf"
    WORD_DOCUMENT = "word_document"
    PLAIN_TXT = "plain_text"
    CREATE_FILE_BTN = "create_file_btn"
    LANGUAGE_OPTION = "language_option"
    INFO_ICON = "info_icon"
    USE_DEFAULT_LANGUAGE = "use_default_language"

    PREVIEW_TOOLBAR_ICONS = [
        PRINT,
        SHARE_AND_SAVE_TEXT,
        SMART_TASKS,
        FAX
    ]

    IMAGE_EDIT_OPTION_BUTTONS = [
        ADD_PAGE_BUTTON,
        ROTATE_BUTTON,
        TEXT_EXTRACT_BUTTON,
        SCRIBBLE_BUTTON,
        REDACT_BUTTON
    ]

    PREVIEW_BUTTON_NAMES = [
        PRINT,
        SHARE_AND_SAVE_BTN,
        SMART_TASKS,
        FAX,
        ADD_PAGE_BUTTON,
    ]

    ACTION_SUCCESS_POPUP_ELEMENTS = [
        GREEN_CHECK_ICON,
        CONTINUE_BUTTON,
        HOME_BUTTON
    ]

    PRINT_PREVIEW_UI_ELEMENTS = [
        BACK_BUTTON,
        PRINT_PREVIEW_TITLE,
        PREVIEW_IMAGE,
        PRINTER_NAME,
        PRINT
    ]

    PREVIEW_UI_ELEMENTS = [
        BACK_BUTTON,
        PREVIEW_TITLE,
        PREVIEW_IMAGE,
        SHARE_AND_SAVE_TEXT,
        SMART_TASKS,
        REORDER_BUTTON
    ]

    SHARE_PREVIEW_UI_ELEMENTS = [
        SHARE_AND_SAVE_TEXT,
        BACK_BUTTON,
        FILE_NAME_FIELD,
        FILE_NAME_TITLE,
        FILE_SETTINGS_TITLE,
        FORMAT,
        FILE_SIZE,
        SHARE_SETTINGS_TIP,
        SHARE_AND_SAVE_BTN
    ]

    SHARE_PREVIEW_PRO_USER_UI_ELEMENTS = SHARE_PREVIEW_UI_ELEMENTS + [ADD_PASSWORD_PROTECTION]

    SMART_TASKS_PREVIEW_UI_ELEMENTS = [
        SMART_TASKS_PREVIEW_TITLE,
        SMART_TASKS_SIGN_IN
    ]

    SAVE_PREVIEW_UI_ELEMENTS = [
        ADD_PAGE_BUTTON,
        PREVIEW_IMAGE,
        FILE_NAME_FIELD,
        SAVE_PREVIEW_TITLE
    ]

    PRINT_SETTINGS_UI_ELEMENTS = [
        PRINT_COPY,
        COPIES_MINUS_BTN,
        COPIES_PLUS_BTN,
        PAPER,
        COLOR_OPTION,
        PAGE_RANGE,
        PRINT_QUALITY,
        TWO_SIDED,
        PRINT
    ]

    CANCEL_JOB_ELEMENTS = [
        CANCEL_JOB_POP_UP_TITLE,
        CANCEL_JOB_POP_DES,
        YES_BTN,
        NO_BTN
    ]

    TRANSFORM_SCREEN_UI_ELEMENTS = [
        TF_RESIZE_TXT,
        TF_ROTATE_TXT
    ]

    PREVIEW_EDIT_OPTIONS = [
        EDIT_BUTTON,
        REPLACE_BTN,
        DELETE_BTN
    ]

    # File Reduction
    FILE_REDUCTION_POPUP = "reduce_size_popup"
    FILE_REDUCTION_ACTUAL_SIZE = "_const_save_actual_size"
    FILE_REDUCTION_MEDIUM_SIZE = "_const_save_medium_size"
    FILE_REDUCTION_SMALL_SIZE = "_const_save_small_size"

    # FILE_REDUCTION_MESSAGE = "file_reduction_msg"
    # FILE_REDUCTION_TIP = "file_reduction_tip"

    # Print Setting Options
    COLOR_OPTIONS = ["Color", "Black Only", "Grayscale"]
    PAGE_RANGE_OPTIONS = ["1", "2", "Pages 1-2", "Select All", "Deselect All", "Manual Input", "Page Range"]
    PRINT_QUALITY_OPTIONS = ["Draft", "Normal", "Best"]
    TWO_SIDED_OPTIONS = ["Off", "Short Edge", "Long Edge"]

    # Transform screen options
    TF_RESIZE_MOVE_OPTIONS = ["Manual", "Original Size", "Fit to Page", "Fill Page"]
    TF_ROTATE_OPTIONS = ["Left", "Right", "Flip H", "Flip V"]

    #Print Size for Novelli printers
    PRINT_SIZE_4x6_TWO_SIDED = "print_size_4x6_two_sided_btn"
    PRINT_SIZE_4x6 = "print_size_4x6"
    PRINT_SIZE_5x7 = "print_size_5x7"
    PRINT_SIZE_5x5 = "print_size_5x5"
    PRINT_SIZE_4x12 = "print_size_4x12"
    PRINT_SIZE_5x11 = "print_size_5x11"
    PRINT_SIZE_A4 = "print_size_a4"

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Preview Screen
    #                                                                                                                      #
    ########################################################################################################################

    def get_no_pages_from_preview_label(self, get_current_page=False):
        if self.driver.wait_for_object("preview_page_no_label", raise_e=False) is not False:
            page_count_label = str(self.driver.get_attribute("preview_page_no_label", attribute="label"))
            page_count_label = page_count_label.split()
            page_count = int(page_count_label[2])
            current_page = int(page_count_label[0])
            if get_current_page:
                return (page_count, current_page)
        else:
            page_count = 1
        return page_count

    def verify_preview_navigate_back_popup(self):
        """
        this popup will return to home screen or scanner screen
        """
        self.driver.wait_for_object("preview_exit_popup", timeout=10)
        self.driver.wait_for_object("yes_new_scan_btn")
        self.driver.wait_for_object("yes_go_home_btn")
        self.driver.wait_for_object("no_add_img_btn")
        self.driver.wait_for_object("cancel_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Print Preview
    #                                                                                                                      #
    ########################################################################################################################

    # Print job completion varies on printer and hence need extended timeout to validate
    def verify_job_sent_and_reprint_buttons_on_print_preview(self, timeout=60):
        self.dismiss_feedback_pop_up()
        self.driver.wait_for_object("printing_btn_txt", raise_e=False)
        self.driver.wait_for_object("print_job_sent_btn", raise_e=False)
        self.verify_re_print_btn(timeout=timeout)

    def go_to_print_preview_pan_view(self, paper_size=OBJECT_SIZE.SIZE_LETTER, pan_view=True):
        """
        Click on pan view to expand or close Print settings screen
        """
        self.select_paper_size(paper_size=paper_size)
        self.verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.select_toolbar_icon(Preview.PRINT)
        self.verify_preview_screen_title(Preview.PRINT_PREVIEW_TITLE)
        self.dismiss_print_preview_coach_mark()
        if pan_view:
            self.driver.swipe("print_preview_pan_view", per_offset=0.35)

    def get_print_setting_selected_value(self, print_option):
        return self.driver.wait_for_object("print_option_selected_value",
                                           format_specifier=[print_option]).get_attribute("name")

    def verify_printer_name_displayed(self, printer_name, timeout=25, displayed=False, delay=0):
        time.sleep(delay)
        if displayed_printer_name := self.driver.get_attribute("printer_name", "label", timeout=timeout, displayed=displayed, raise_e=False):
            return displayed_printer_name in printer_name
        return False
    
    def change_print_copies(self, copies_btn, no_of_copies=1):
        for _ in range(no_of_copies):
            self.driver.click(copies_btn)

    def get_copies_btn_enabled_status(self, copies_btn):
        return self.driver.get_attribute(copies_btn, "enabled")

    def get_no_of_copies(self):
        if self.driver.wait_for_object("print_multiple_copies_txt", raise_e=False) is not False:
            copies_label = self.driver.get_attribute("print_multiple_copies_txt", attribute="label")
            copies_label = copies_label.split()
            count = list(copies_label[1])
            copies_count = int(count[1])
        else:
            copies_count = 1
        return copies_count

    # Longer wait times is to accommodate printing progress verification
    def verify_printing_status_btn_changes(self, multi_print=False, timeout=60):
        if multi_print:
            self.driver.wait_for_object("multi_page_printing_txt", timeout=timeout)
        else:
            self.driver.wait_for_object("printing_btn_txt", raise_e=False)
        self.driver.wait_for_object("printing_msg_txt", raise_e=False)
        self.driver.wait_for_object("cancel_btn", raise_e=False)
        self.driver.wait_for_object("print_job_sent_btn", raise_e=False, timeout=timeout)
        self.verify_re_print_btn(timeout=timeout)

    def verify_re_print_btn(self, timeout=60):
        timeout = time.time() + timeout
        while time.time() < timeout:
            self.dismiss_feedback_pop_up()
            if self.driver.wait_for_object("re_print_btn", raise_e=False) is not False:
                logging.info("Re-Print button displayed")
                break
            else:
                time.sleep(5)
        return self.driver.wait_for_object("re_print_btn", timeout=3)

    def verify_id_card_front_screen(self, timeout=10):
        self.driver.wait_for_object("id_card_front", timeout=timeout)

    def verify_id_card_back_screen(self):
        self.driver.wait_for_object("id_card_back")

    def verify_rotate_right_icon(self):
        """
        Rotate right icon is shown in id card front screen
        """
        self.driver.wait_for_object(self.ROTATE_RIGHT_ICON)

    def verify_rotate_upsidedown_icon(self):
        """
        Upside down icon is shown in id card back screen
        """
        self.driver.wait_for_object(self.ROTATE_UPSIDEDOWN_ICON)

    def verify_discard_changes_popup(self):
        self.driver.wait_for_object("discard_changes")
        self.driver.wait_for_object("changes_not_saved")
        self.driver.wait_for_object("yes_btn")
        self.driver.wait_for_object("no_btn")

    def handle_print_size_and_verify_print_preview_screen(self):
        if self.verify_print_size_screen(raise_e=False):
            self.select_print_size_btn(self.PRINT_SIZE_4x6)
        self.verify_preview_screen_title()

    def verify_file_is_processing_popup_title(self):
        self.driver.wait_for_object("file_is_processing_title", timeout=20)

    def select_continue_file_processing(self):
        self.driver.click("continue_file_processing", timeout=15)


    ########################################################################################################################
    #                                                                                                                      #
    #                                               Share / Save screen
    #                                                                                                                      #
    ########################################################################################################################

    def rename_file(self, file_name):
        """
        clears the file text field and inputs a new string in the text field
        :param file_name: string of the new file name
        :return:
        """
        self.driver.wait_for_object(self.FILE_NAME_FIELD).click()
        self.select_rename_value_to_change(re_name=file_name, press_enter=True)

    def select_file_type(self, file_type):
        """
         Click Format option and select file_type
        """
        self.dismiss_new_file_types_coachmark()
        self.driver.wait_for_object(self.FORMAT).click()
        self.driver.wait_for_object("_shared_dynamic_navigation_bar",
                                    format_specifier=[self.get_text_from_str_id(self.FORMAT)])
        if self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[file_type],
                                       raise_e=False) is not False:
            self.driver.click("_shared_dynamic_text", format_specifier=[file_type])
            return True
        else:
            return False

    def select_file_size(self, file_size):
        self.driver.click(file_size)         
    
    def verify_unable_to_read_document(self):
        self.driver.wait_for_object("unable_to_read_document")

    def toggle_smart_file_name(self, enable=True):
        switch = self.driver.wait_for_object("smart_file_name_switch")
        if (bool(int(switch.get_attribute("value")))) != enable:
            switch.click()

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Action Flows
    #                                                                                                                      #
    ########################################################################################################################

    def save_scan_result(self, file_name=""):
        """
        Save the scan result
        End of flow: Preview screen
        Device: Phone
        """
        self.select_file_name()
        if file_name != "":
            self.driver.send_keys(self.FILE_NAME_FIELD, file_name)
        self.driver.click("rename_btn")

    # FIXME: use select_button()
    def select_preview_back(self):
        """
        Click on Back button on Preview screen
        End of flow: Home screen
        Device: Phone
        """
        self.driver.click("back_btn")

    def select_file_name_on_preview_screen(self):
        """
        Click on File name on Preview screen
        End of flow: Scan screen
        Device: Phone
        """
        self.driver.click("file_name_textfield")

    def select_rename_value_to_change(self, re_name="New_rename_file", press_enter=False):
        """
        :param re_name:
        """
        self.driver.click("clear_text_btn")
        if re_name != "":
            self.driver.send_keys(self.FILE_NAME_FIELD, re_name, press_enter=press_enter)

    def select_rename_button(self):
        self.driver.click("rename_btn")

    def select_delete_page_icon(self):
        self.driver.click("delete_page_icon")

    def select_file_converting_format(self, file_type):
        self.driver.click(file_type)
        current_file_format = self.driver.find_object(file_type).get_attribute("value")
        ga_dynamic_key_value = current_file_format

    def select_save_to_hp_smart_btn(self):
        self.driver.click("save_hp_smart_btn", timeout=20)

    def select_file_rename_cancel(self):
        self.driver.click("rename_cancel_btn")

    def select_file_rename_save_btn(self):
        """
        Click on Save button on Scan result
        End of flow: Scan Result screen with Save As popup
        Device: Phone
        """
        self.driver.click("save_btn")

    def select_print_btn(self):
        """
        From the print page, after selecting printer, select the print btn
        """
        self.driver.click("print_btn", timeout=5)

    def select_send_btn(self):
        self.driver.click("send_btn")

    def select_rotate_right_icon(self):
        """
        Right icon is shown in id card front screen
        """
        self.driver.click(self.ROTATE_RIGHT_ICON)

    def select_rotate_upsidedown_icon(self):
        """
        Upside down icon is shown in id card back screen
        """
        self.driver.click(self.ROTATE_UPSIDEDOWN_ICON)

    def select_page_cell(self, index):
        """
        select the page/image on rotate preview, page starts from 1 while object starts from 0
        """
        self.driver.click("page_cell", index=index - 1)

    def select_multiple_page_cells(self, indices):
        for index in indices:
            self.select_page_cell(index)

    def select_reset_btn(self):
        self.driver.click("reset_btn")
    
    def dismiss_redaction_coachmark(self, raise_e=False):
        self.driver.click("close_coachmark_btn", raise_e=raise_e)

    def select_finish_shortcut_btn(self):
        self.driver.click("finish_shortcut_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Verification Flows                                                     #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_rename_popup(self):
        """
        Verify Rename popup screen
        """
        self.driver.wait_for_object("rename_title")

    def verify_preview_screen(self, raise_e=True):
        """
        Verify Preview screen with the following elements:
            - Preview title
        """
        self.dismiss_feedback_pop_up()
        return self.driver.wait_for_object(self.PREVIEW_TITLE, timeout=120, interval=5, raise_e=raise_e)

    def verify_rotate_btn(self, raise_e=True):
        return self.driver.wait_for_object(self.ROTATE_BUTTON, raise_e=raise_e) is not False

    def verify_preview_share_screen(self):
        self.driver.wait_for_object("preview_share_screen")

    def verify_print_preview_collection_view(self):
        """
        verifies the image on the preview screen
        """
        self.driver.wait_for_object(self.PREVIEW_IMAGE)

    def verify_delete_page_x_icon(self):
        """
        :return: True if x button is present else False
        """
        return self.driver.find_object("delete_page_icon", multiple=True, raise_e=False)

    def verify_delete_button(self):
        self.driver.click("delete_page_icon")
        delete_button = self.driver.wait_for_object("delete_btn", raise_e=False)
        self.driver.click_by_coordinates(area='bl')
        return delete_button

    def verify_rotate_screen_tray_options(self):
        self.driver.wait_for_object(self.ROTATE_BUTTON)
        self.driver.wait_for_object(self.DELETE_BTN)

    def verify_file_type_selected(self, option, raise_e=False):
        return self.driver.wait_for_object("file_format_type", format_specifier=[option], raise_e=raise_e)

    def verify_preview_screen_title(self, title=PREVIEW_TITLE):
        """
        :param title: preview title name
        """
        self.dismiss_feedback_pop_up()
        return self.driver.wait_for_object("preview_navigation_bar_title_text",
                                           format_specifier=[self.get_text_from_str_id(title)], timeout=10,
                                           raise_e=False)

    def verify_printer_is_selected(self, printer_name):
        """
        From the printer page, verify that we are currently selecting a given printer
        """
        if current_printer_label := self.driver.get_attribute("printer_name", "label", raise_e=False):
            return current_printer_label in printer_name
        return False

    def handle_share_preview_screen(self):
        if self.driver.wait_for_object(self.SHARE_AND_SAVE_TEXT, raise_e=False):
            pass
        else:
            self.driver.click("share_btn")

    def select_back_to_exit_with_out_saving(self):

        self.select_navigate_back()
        self.verify_exit_with_out_saving_popup_options()
        self.select_cancel()

    def rename_scanned_file(self, choose_name="New_rename_for_file"):

        self.select_file_name_on_preview_screen()
        self.select_rename_value_to_change(re_name=choose_name)

    # ----------------------------- VERIFICATION FLOWS ----------------------------------------------
    def verify_toolbar_icons(self):
        """
        verifies the icons at the bottom of the preview screen:
            Print
            Share/Save
            Smart Tasks
        """
        for i in self.PREVIEW_TOOLBAR_ICONS:
            self.driver.wait_for_object(i)

    def verify_print_preview_ui_elements(self, printer_name):
        self.dismiss_print_preview_coach_mark()
        for element in self.PRINT_PREVIEW_UI_ELEMENTS:
            if element == self.PRINTER_NAME:
                option_displayed = self.driver.get_attribute(element, "label") in printer_name
            else:
                option_displayed = self.driver.wait_for_object(element, timeout=20, raise_e=False)
            if not option_displayed:
                raise Exception(element + " - not displayed/not applicable")

    def go_home_from_preview_screen(self):
        """
        Go back to home from preview screen
        """
        self.dismiss_feedback_pop_up()
        self.driver.click("_shared_back_arrow_btn", change_check={"wait_obj": "preview_exit_popup"}, timeout=10)
        self.verify_preview_navigate_back_popup()
        self.driver.click("yes_go_home_btn")

    def select_go_home(self):
        self.driver.click("go_home_btn")

    def select_ok_button(self, index):
        """
        Press Ok button on screen.
        Args:
            index (integer): Index of the desired ok button to be pressed
        """
        self.driver.click("ok_btn", index=index)
        
    def verify_file_saved_pop_up(self, raise_e=True):
        time.sleep(1)
        return self.driver.wait_for_object("file_saved_popup_title", timeout=20, raise_e=raise_e)

    def verify_exit_with_out_saving_popup_options(self):
        self.driver.wait_for_object("preview_exit_popup")
        self.driver.wait_for_object("yes_go_home_btn")
        self.driver.wait_for_object("yes_new_scan_btn")
        self.driver.wait_for_object("no_add_img_btn")
        self.driver.wait_for_object("cancel_btn")

    def verify_scan_exit_screen(self):
        self.driver.wait_for_object("cancel_btn")

    def verify_preview_edit_options(self):
        self.driver.wait_for_object("edit_btn")
        self.driver.wait_for_object("replace_btn")

    def verify_reset_button(self):
        self.driver.wait_for_object("reset_btn")

    # ----------------------------- ACTION FLOWS ----------------------------------------------
    def select_select_printer_btn(self):
        """
        From the print page, select the 'select printer' btn
        """
        self.driver.click("select_printer_btn")

    def select_printer_from_list(self, printer_name):
        """
        After selecting the 'select printer' btn 
        """
        if not self.verify_printer_is_selected(printer_name):
            self.select_select_printer_btn()
            time.sleep(5)
            self.driver.scroll("printer_option_from_list", scroll_object="printer_options_from_list_container", format_specifier=[printer_name], timeout=380)
            self.driver.click("printer_option_from_list", format_specifier=[printer_name])

    def select_printer_options_btn(self):
        """
        From the print page, after selecting a printer, select the 'Options' btn
        """
        self.driver.click("printer_options_btn")

    def select_paper_option_btn(self):
        """
        From the print page, after selecting options btn, select paper option
        """
        self.driver.click("paper_option_btn")

    def select_save(self):
        """
        Save Button on the save preview tab
        """
        self.driver.wait_for_object(self.DYNAMIC_BUTTON, format_specifier=[self.get_text_from_str_id(self.SAVE)],
                                    timeout=5)
        self.driver.click(self.DYNAMIC_BUTTON, format_specifier=[self.get_text_from_str_id(self.SAVE)])

    def select_toolbar_icon(self, icon, displayed=True, delay=0):
        """
        Click on bottom navigation icon (XCUIElementTypeStaticText)
        :param icon: name attribute of the element
        :return:
        """
        time.sleep(delay)
        self.dismiss_feedback_pop_up()
        self.driver.click(icon, displayed=displayed)

    def select_button(self, button):
        """
        Click on a XCUIElementTypeButton on the page
        :param button: name attribute of the element
        :return:
        """
        if button not in self.PREVIEW_BUTTON_NAMES:
            raise InvalidElementNameException("Object: " + button + " not a valid button name")
        self.driver.scroll(button, timeout=15, click_obj=True)
        
    def select_image_edit_option_button(self, button, raise_e=True):
        '''
            the buttons on the top scroll bar
            Common buttons:
            ADD_PAGE_BUTTON,
            ROTATE_BUTTON,

            Pro users buttons:
            TEXT_EXTRACT_BUTTON,
            SCRIBBLE_BUTTON,
            REDACT_BUTTON
        '''
        if button not in self.IMAGE_EDIT_OPTION_BUTTONS:
            raise InvalidElementNameException("Object: " + button + " not a valid button name")
        self.driver.scroll(button, scroll_object="image_edit_option_slider", 
                direction="right", check_end=False, timeout=60, raise_e=raise_e).click()

    def select_add_page(self):
        """
        Click on Add Page icon button on Preview screen
        """
        self.driver.click(self.ADD_PAGE_BUTTON, timeout=15)

    def select_rotate_btn(self):
        """
        Click on rotate button on Preview screen
        """
        self.driver.wait_for_object(self.ROTATE_BUTTON, timeout=15).click()

    def select_delete_btn(self):
        self.driver.click(self.DELETE_BTN)

    def select_edit(self, change_check=None):
        """
        Click on Edit button
        """
        self.dismiss_feedback_pop_up()
        if self.driver.wait_for_object(self.EDIT_BUTTON, raise_e=False) is not False:
            self.driver.click(self.EDIT_BUTTON)
        else:
            self.select_preview_image(change_check=change_check)

    def select_home_button(self):
        """
        Click on Home button
        """
        self.driver.wait_for_object(self.HOME_BUTTON, timeout=10).click()

    def select_yes_btn(self):
        self.driver.click("yes_btn", timeout=5)

    def select_yes_go_home_btn(self):
        self.driver.click("yes_go_home_btn")

    def select_yes_new_scan_btn(self):
        self.driver.click("yes_new_scan_btn")

    def select_no_add_img_btn(self):
        self.driver.click("no_add_img_btn")

    def select_preview_image(self, change_check=None):
        self.driver.wait_for_object(self.PREVIEW_IMAGE, timeout=5)
        self.driver.click(self.PREVIEW_IMAGE, change_check=change_check)

    def zoom_preview_image(self):
        self.driver.wait_for_object(self.PREVIEW_IMAGE)
        self.driver.pinch(pinch_obj=self.PREVIEW_IMAGE, move_in=False)

    def verify_zoomed_mode(self):
        self.driver.wait_for_object("zoomed_mode")

    # ------------------- File Reduction Popup --------------------------------------

    def verify_file_reduction_popup(self):
        names = [attr for attr in dir(Preview) if attr.startswith("FILE_REDUCTION_")]
        for name in names:
            self.driver.wait_for_object(getattr(Preview, name), timeout=10)

    def select_file_reduction_size(self, size):
        if size not in [getattr(Preview, attr) for attr in dir(Preview) if attr.endswith("_SIZE")]:
            raise InvalidElementNameException("Object {}: is not a valid File Reduction size option".format(size))
        self.driver.wait_for_object(size).click()

    def get_reduced_file_sizes(self):
        p = re.compile(r'\((.*?) MB\)')
        actual_size = re.search(p, self.driver.wait_for_object(self.FILE_REDUCTION_ACTUAL_SIZE).text).group(1).strip()
        medium_size = re.search(p, self.driver.wait_for_object(self.FILE_REDUCTION_MEDIUM_SIZE).text).group(1).strip()
        small_size = re.search(p, self.driver.wait_for_object(self.FILE_REDUCTION_SMALL_SIZE).text).group(1).strip()
        return int(actual_size), int(medium_size), int(small_size)

    def get_option_selected_value(self, option, displayed=True):
        print_option = self.driver.get_attribute(option, "name", displayed=displayed)
        return self.driver.get_attribute("cell_selected_value_txt", "name", format_specifier=[print_option], displayed=displayed)

    def verify_pages_selected(self, page_no):
        return self.driver.wait_for_object("page_selected_image", format_specifier=[page_no], raise_e=False)

    def select_or_unselect_pages(self, page_no):
        for i in range(len(page_no)):
            self.driver.click("page_no_txt", format_specifier=[page_no[i]])

    def get_page_range(self, displayed=False):
        page_range = self.driver.get_attribute("page_range_displayed_txt", "name", displayed=displayed)
        return page_range.encode("ascii", "ignore").decode()

    def check_manual_input_pop_up_msg(self, input_page_range=False):
        if self.driver.wait_for_object("in_app_alert", raise_e=False) is not False:
            if input_page_range:
                return self.driver.wait_for_object("manual_input_pop_up_msg", raise_e=False)
            else:
                return self.driver.wait_for_object("manual_input_pop_up_warning_msg", raise_e=False)
        else:
            return False

    def enter_page_range(self, page_nos):
        self.driver.click("clear_text_btn", raise_e=False)
        self.driver.send_keys("page_range_input_txt_field", page_nos)

    def verify_default_option_selected(self, option_name):
        return self.driver.wait_for_object("option_selected_image", format_specifier=[option_name], invisible=True,
                                           raise_e=False)

    def verify_button(self, button_name, timeout=30, displayed=True):
        return self.driver.wait_for_object(self.DYNAMIC_PREVIEW_BUTTON, format_specifier=[self.get_text_from_str_id(button_name)], timeout=timeout, displayed=displayed, raise_e=False)

    def verify_transform_screen_title(self, title):
        self.dismiss_feedback_pop_up()
        if title == self.PREVIEW_IMAGE:
            return self.driver.wait_for_object("transform_title")
        else:
            return self.driver.wait_for_object("preview_navigation_bar_title_text",
                                           format_specifier=[title])            

    def select_transform_options(self, tf_option1, tf_option_select=None):
        self.driver.click(tf_option1)
        self.verify_transform_screen_title()
        if tf_option_select is not None:
            self.driver.click("_shared_dynamic_text", format_specifier=[tf_option_select])

    def get_print_page_collection_view_cell(self, page_index=None):
        page_labels = []
        no_of_pages = self.driver.find_object("reorder_page_collection", multiple=True)
        if page_index is not None:
            page_labels = no_of_pages[page_index].text
        else:
            for i in range(len(no_of_pages)):
                page_label = no_of_pages[i].text
                page_labels.append(page_label)
        logging.debug(page_labels)
        return page_labels

    def toggle_share_as_original_btn(self, uncheck=False):
        self.driver.check_box("share_as_original_toggle_btn", uncheck=uncheck)

    # implementation in progress, not tested yet
    def reorder_page_collection(self, index=1, direction="right"):
        page_objects = self.driver.find_object("page_cell", multiple=True)
        self.driver.drag_and_drop(page_objects[index], destination=direction)

    def preview_img_screenshot(self):
        return saf_misc.load_image_from_base64(self.driver.screenshot_element(self.PREVIEW_IMAGE))

    def page_cell_img_screenshot(self, index):
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("page_cell_image", index=index-1))

    def verify_preview_image_edit_btn(self):
        self.driver.wait_for_object(self.DELETE_PAGE_ICON, displayed=False)

    def verify_choose_your_printer_option(self):
        self.driver.wait_for_object("choose_your_printer_option")

    def dismiss_new_file_types_coachmark(self, raise_e=False):
        if self.driver.wait_for_object("new_file_types_coachmark", displayed=False, raise_e=raise_e) is not False:
            self.driver.click_by_coordinates(area='bl')

    def nav_detect_edges_screen(self):
        # Depending on printer, scan job takes longer sometimes
        self.driver.wait_for_object("adjust_boundaries_title", timeout=30)
        self.driver.click("next_btn", timeout=10)

    def verify_print_preview_coach_mark(self, timeout=10, displayed=False, raise_e=False):
        return self.driver.wait_for_object("print_preview_coach_mark", timeout=timeout, displayed=displayed, raise_e=raise_e)

    def dismiss_print_preview_coach_mark(self, timeout=10):
        if self.verify_print_preview_coach_mark(timeout=timeout) is not False:
            self.driver.click_by_coordinates(area='bl')
            logging.info("Print setting coach mark closed")
            time.sleep(2)

    def select_edit_btn_on_preview_screen(self):
        self.driver.click("edit_btn")

    def verify_detect_edges_screen(self):
        self.driver.wait_for_object("adjust_boundaries_title", timeout=30)

    def select_replace_btn_on_preview(self):
        self.driver.click("replace_btn")

    def verify_language_selected(self, language="default language", raise_e=True):
        obj = self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[language], timeout=5)
        return self.driver.wait_for_object("blue_checkmark", invisible=True, root_obj=obj, raise_e=raise_e)

    def verify_language_option(self, raise_e=True):
        return self.driver.wait_for_object("language_option", raise_e=raise_e) is not False
    
    def select_info_icon(self, index=1):
        '''
            two info icon will be showing in the same screen
            index: 
                0: Smart File Name info icon
                1: Language option info icon
        '''
        self.driver.click("info_icon", index=index)
    
    def verify_language_coachmark(self):
        self.driver.wait_for_object("select_language_of_document_coachmark", invisible=True)

    def verify_file_processing_popup(self, raise_e=True):
        return self.driver.wait_for_object("file_processing_popup", raise_e=raise_e)

    def select_paper_size(self, raise_e=False, paper_size=OBJECT_SIZE.SIZE_LETTER):
        if self.driver.wait_for_object("print_size_screen_title", raise_e=raise_e) is not False:
            self.driver.click(paper_size)

    def verify_finish_shortcut_btn(self):
        return self.driver.wait_for_object("finish_shortcut_btn")
    
    ########################################################################################################################                                                                                                                  #
    #                                              Novelli                                                                                                                #
    ########################################################################################################################

    def verify_print_size_screen(self, invisible=False, raise_e=True):
        """
        Verify Print Size screen through:
        - Title
        """
        return self.driver.wait_for_object("print_size_screen_title", invisible=invisible, raise_e=raise_e)

    def verify_two_sided_preview_screen(self):
        """
        Verify 2-Sided Preview screen through:
        - Title
        - Front button
        """
        self.driver.wait_for_object("two_sided_preview_title", timeout=15)
        self.driver.wait_for_object("front_btn")

    def verify_quickly_switch_sides_coachmark(self, raise_e=True):
        """
        Verify coachmark message on the screen: Quickly switch sides with a tap
        :return:
        """
        return self.driver.wait_for_object("quickly_switch_coachmark", raise_e=raise_e, timeout=15, displayed=False)

    def select_print_size_btn(self, size_btn, change_check={"wait_obj": "print_size_screen_title", "invisible": True}):
        """
        Click on button on Print Size screen
        Note: This screen is just for Novelli printer.
        :param size_btn: using following class constant.
                    PRINT_SIZE_4x6_TWO_SIDED
                    PRINT_SIZE_4x6_STANDARD
                    PRINT_SIZE_5x7
                    PRINT_SIZE_5x5_SQUARE
                    PRINT_SIZE_4x12_PANORAMIC
                    PRINT_SIZE_8_5x11_LETTER
                    PRINT_SIZE_A4
        """
        self.driver.click(size_btn, change_check=change_check)

    def select_back_button(self):
        """
        Select Back button from 2-Sided Preview screen
        """
        self.driver.click("novelli_back_btn")

    def select_front_button(self):
        """
        Select Front button from 2-Sided Preview screen
        """
        self.driver.click("front_btn")

    def select_print_preview_button(self):
        """
        Select Print Preview button from Preview screen
        """
        self.driver.click("print_preview")

    def dismiss_quickly_switch_sides_coachmark(self):
        """
        Dismiss quickly switch sides coachmark
        """
        if self.verify_quickly_switch_sides_coachmark(raise_e=False) is not False:
            self.driver.click_by_coordinates(area="mm")

    def verify_requires_two_sided_paper_popup(self):
        """
        Verify the "This print requires two-sided photo paper" popup
         - title text
         - continue button
        """
        self.driver.wait_for_object("double_sided_paper_popup_title_txt")
        self.driver.wait_for_object("double_sided_paper_popup_continue_btn")

    def select_delete_pages_in_current_job(self, no_of_pages_to_delete=2):
        """
        Click on 3dots icon of each page on Preview screen; 
        Click on Delete and handle Delete Confirmation Popup
        """
        try:
            for page in range(no_of_pages_to_delete):
                self.driver.click(self.DELETE_PAGE_ICON)
                self.driver.click("delete_btn")
                if self.driver.wait_for_object("delete_popup_msg", raise_e=False):
                    self.driver.click("delete_popup_delete_btn")
        except TimeoutException:
            logging.info("we don't have {} many pages to delete on preview screen:".format(no_of_pages_to_delete))

    def select_preview_next_btn(self):
        """
        Click on Next button on Preview screen
        """
        self.driver.click("preview_next_btn")

    def select_shutter_card_btn(self):
        """
        Click on Shutter Card button on Preview screen
        """
        self.driver.click("shutter_card_btn", timeout=10)

    def select_three_dots_icon(self, index=0):
        """
        Click on 3dots icon of each page on Preview screen
        :param index: index of the page to select 3dots icon
        """
        self.driver.click("three_dots_icon", index=index)

    def select_edit_on_three_dots(self, index=0):
        """
        Click on Edit option on 3dots icon of each page on Preview screen
        :param index: index of the page to select 3dots icon
        """
        self.driver.click("edit_on_three_dots", index=index)

    def select_delete_on_three_dots(self, index=0):
        """
        Click on Delete option on 3dots icon of each page on Preview screen
        :param index: index of the page to select 3dots icon
        """
        self.driver.click("delete_on_three_dots", index=index)

    def select_replace_on_three_dots(self, index=0):
        """
        Click on Replace option on 3dots icon of each page on Preview screen
        :param index: index of the page to select 3dots icon
        """
        self.driver.click("replace_on_three_dots", index=index)

    def select_adjust_btn_on_edit(self):
        """
        Click on Adjust button on Edit screen
        """
        self.driver.click("adjust_btn")

    def select_crop_btn_on_edit(self):
        """
        Click on Crop button on Edit screen
        """
        self.driver.click("crop_btn", timeout=10)

    def select_shortcuts_on_preview_screen(self):
        """
        Click on Shortcuts button on Preview screen
        """
        self.driver.click("shortcuts_btn", timeout=10)

    def select_swipe_up_documents_on_shortcuts(self):
        """
        Click on Swipe Up Documents button on Shortcuts screen
        """
        self.driver.click("swipe_up_documents_btn", timeout=10)

    def select_first_document_to_preview_on_shortcuts(self):
        """
        Click on first document to preview on Swipe Up Documents screen
        """
        self.driver.click("first_document_to_preview", timeout=10)

    def select_filters_btn_on_edit(self):
        """
        Click on Filters button on Edit screen
        """
        self.driver.click("hpx_edit_filter", timeout=10)

    def select_text_btn_on_edit(self):
        """
        Click on Text button on Edit screen
        """
        self.driver.click("hpx_edit_text", timeout=10)

    def select_markup_btn_on_edit(self):
        """
        Click on Markup button on Edit screen
        """
        self.driver.click("hpx_edit_Markup", timeout=10)

    def select_auto_btn_on_edit(self):
        """
        Click on Auto button on Edit screen
        """
        self.driver.click("hpx_auto_btn", timeout=10)

    def select_cancel_btn_on_edit(self):
        """
        Click on Cancel button on Edit screen
        """
        self.driver.click("hpx_cancel_btn", timeout=10)

    def select_discard_btn_on_edit(self):
        """
        Click on Discard button on Edit screen
        """
        self.driver.click("hpx_discard_btn", timeout=10)

    def select_cancel_btn_on_delete(self):
        """
        Click on Cancel button on Delete Confirmation Popup
        """
        self.driver.click("delete_popup_cancel_btn")

    def select_delete_btn_on_delete(self):
        """
        Click on Delete button on Delete Confirmation Popup
        """
        self.driver.click("delete_popup_delete_btn")

    def select_done_button_on_preview(self, timeout=10):
        """
        Click on Delete button on preview screen
        """
        self.driver.click("_shared_done", timeout=timeout)

    def select_no_btn(self):
        self.driver.click("no_btn", timeout=5)

    def verify_pages_option(self):
        """
        Verify if the page option is displayed on the preview screen
        """
        if self.driver.wait_for_object("preview_page_no_label", raise_e=False):
            return True
        else:
            return False

    def verify_popup_after_click_done_btn(self):
        """
        Verify the popup after clicking on done button
        """
        self.driver.wait_for_object("yes_go_home_btn")
        self.driver.wait_for_object("cancel_btn")

    def click_cancel_on_popup(self):
        """
        click cancel on the popup
        """
        self.driver.click("cancel_btn")

    def verify_preview_more_options(self):
        """
        Verify the more options on the preview screen
        """
        self.driver.wait_for_object("edit_on_three_dots")
        self.driver.wait_for_object("replace_on_three_dots")
        self.driver.wait_for_object("delete_on_three_dots")

    def verify_cancel_btn_popup(self):
        """
        verify Cancel button popup after clicking on Cancel button
        """
        self.driver.wait_for_object("discard_changes_popup", timeout=10)

    def verify_cancel_popup(self):
        """
        Verify the cancel popup after clicking on back button on preview screen
        """
        self.driver.wait_for_object("delete_popup_msg")
        self.driver.wait_for_object("cancel_popup_msg")
        self.driver.wait_for_object("yes_btn")
        self.driver.wait_for_object("no_btn")

    def verify_delete_popup(self):
        """
        Verify the delete popup after clicking on delete button
        """
        self.driver.wait_for_object("delete_popup_msg")

    def select_roate_on_edit(self):
        """
        select roatate on edit screen
        """
        self.driver.click("rotate_btn_on_edit")

    def verify_add_page(self):
        """
        verify on Add Page icon button on Preview screen
        """
        self.driver.wait_for_object(self.ADD_PAGE_BUTTON, timeout=15)

    def verify_delete_page_icon(self):
        self.driver.wait_for_object("delete_page_icon")    

    def verify_add_roatate_reorder_btn(self):
        """
        verify on Add Page, Rotate and Reorder icon button on Preview screen
        """
        self.driver.wait_for_object(self.ADD_PAGE_BUTTON, timeout=15)
        self.driver.wait_for_object(self.ROTATE_BUTTON, timeout=15)
        self.driver.wait_for_object(self.REORDER_BUTTON, timeout=15)

    def select_reorder_btn(self):
        """
        Click on reorder button on Preview screen
        """
        self.driver.wait_for_object(self.REORDER_BUTTON, timeout=15).click()

    def verify_smart_file_name_option(self):
        """
        verify Smart File Name option on preview screen
        """
        self.driver.wait_for_object("smart_file_name")

    def verify_file_size_option(self):
        """
        verify File size option on preview screen
        """
        self.driver.wait_for_object("file_size_button")
    
    def verify_file_type_option(self):
        """
        verify File type option on preview screen
        """
        self.driver.wait_for_object("file_type_dropdown_ios")

    def select_continue_btn(self):
        """
        verify continue option on preview screen
        """
        self.driver.click("continue_btn")

    def select_save_image_as_btn(self):
        """
        verify save image as option on preview screen
        """
        self.driver.click("save_image_as_option")

    def select_save_document_as_btn(self):
        """
        verify save document as option on preview screen
        """
        self.driver.click("save_document_as_option")

    def verify_default_save_image_as_option(self):
        """
        verify save image as option on preview screen
        """
        self.driver.wait_for_object("save_image_as_option")
        self.driver.wait_for_object("save_image_as_default_option")

    def verify_default_save_document_as_option(self):
        """
        verify save document as option on preview screen
        """
        self.driver.wait_for_object("save_document_as_option")
        self.driver.wait_for_object("save_document_as_default_option")

    def verify_file_saving_defaults_screen(self):
        """
        verify save document as option on preview screen
        """
        self.driver.wait_for_object("file_saving_defaults")

    def verify_airdrop_icon(self):
        """
        verify airdrop icon on share screen
        """
        if self.driver.wait_for_object("airdrop_icon"):
            return True
        else:
            return False

    def select_mobile_fax_on_preview(self):
        """
        select mobile fax button on preview screen
        """
        self.driver.click("mobile_fax_on_preview_page")

    def verify_mobile_fax_screen(self):
        """
        verify mobile fax screen
        """
        self.driver.wait_for_object("compose_fax_title")
        self.driver.wait_for_object("fax_file")

    def send_mobile_fax_from_preview(self, fax_number):
        """
        send mobile fax 
        """
        self.driver.send_keys("fax_to_filed", fax_number)
        self.driver.click("send_fax")

    def select_printer_name(self, printer_name, timeout=10):
        self.driver.click(printer_name, timeout=timeout)

    def verify_printer_name_ui(self, printer_name, timeout=10):
        self.driver.wait_for_object(printer_name, timeout=timeout)

    def verify_resize_and_move_options(self):
        """
        verify on resize and move options are displayed
        """
        self.driver.wait_for_object("Manual_btn")
        self.driver.wait_for_object("_shared_original_size")
        self.driver.wait_for_object("_shared_fit_to_page")
        self.driver.wait_for_object("_shared_fill_page")

    def verify_file_name_on_preview_screen(self):
        """
        verify file name on preview screen
        """
        self.driver.wait_for_object("file_name_textfield")

    def verify_print_screen(self):
        """
        verify the print page
        """
        self.driver.wait_for_object("print_btn", timeout=5)
        self.driver.wait_for_object("print_preview_pan_view", timeout=5)
        self.driver.wait_for_object("image_of_preview", timeout=5)

    def verify_paper_screen_in_print_page(self):
        """
        Verify paper screen in print screen
        """
        self.driver.wait_for_object("paper_ready_to_use_txt")
        self.driver.wait_for_object("additional_paper_options_txt")

    def verify_paper_quality_in_print_page(self):
        """
        Verify paper quality in print screen
        """
        self.driver.wait_for_object("print_quality_txt")

    def verify_color_options_in_print_page(self):
        """
        Verify color options in print screen
        """
        self.driver.wait_for_object("color_option_txt")
