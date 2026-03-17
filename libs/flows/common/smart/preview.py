import time
import logging
import json

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from MobileApps.libs.flows.common.smart.smart_flow import SmartFlow
from SAF.misc import saf_misc

class InvalidElementNameException(Exception):
    pass

class Preview(SmartFlow):
    flow_name = "preview"
    folder_name = "preview"

    # Title Str Locators
    PRINT_PREVIEW_TITLE = "print_preview_title"
    PREVIEW_TITLE = "preview_title_str"
    REDACTION_TITLE = "redaction_title_str"
    TEXT_EXTRACT_TITLE = "text_extract_title_str"
    PRINT_SIZE_TITLE = "print_size_title_str"
    ROTATE_TITLE = "auto_rotate_title_str"
    REORDER_TITLE = "reorder_title_str"
    TWO_SIDE_PREVIEW_TITLE = "two_side_preview_title_txt"

    # Top toolbar buttons for Preview Landing page
    BACK_BUTTON = "back_arrow_btn"
    ADD_BTN = "add_btn"
    ROTATE_BTN = "rotate_btn"
    TEXT_EXTRACT_BTN = "text_extract_btn"
    SCRIBBLE_BTN = "scribble_btn"
    REDACTION_BTN = "redaction_btn"
    REORDER_BTN = "reorder_btn"
    
    # Bottom Navbar buttons for Preview Landing page
    PRINT_BTN = "print_btn"
    SHORTCUTS_BTN = "shortcuts_btn"
    FAX_BTN = "fax_btn"
    PRINT_PREVIEW_BTN = "print_preview_btn"

    # Page Options buttons for Preview Landing Page
    EDIT_BTN = "edit_btn"
    DELETE_BTN = "delete_btn"
    REPLACE_BTN = "replace_btn"

    # More Options buttons for Preview Landing Page
    FORMAT_BTN = "more_options_format_btn"
    HELP_BTN = "more_options_help_btn"

    # Checkboxes for Print Help screen
    PRINT_PLUGIN_CB = "print_plugin_cb"
    PRINT_SETTINGS_CB = "print_settings_cb"
    PRINTER_SELECT_CB = "printer_select_cb"

    # File Types for Action screen
    BASIC_PDF = "basic_pdf"
    IMAGE_JPG = "image_jpg"
    SEARCHABLE_PDF = "searchable_pdf"
    WORD_DOCUMENT = "word_doc"
    PLAIN_TXT = "plain_txt"

    # Hint Strings for Action screen
    PWD_HINT = "pwd_hint_str"
    SHORT_PWD_HINT = "short_pwd_hint_str"
    SHORT_PWD_SPACES_HINT = "short_pwd_with_spaces_hint_str"
    LONG_PWD_HINT = "long_pwd_hint_str"
    LONG_PWD_SPACES_HINT = "long_pwd_with_spaces_hint_str"
    PWD_SPACES_HINT = "pwd_with_spaces_hint_str"

    # File Sizes for Action screen
    FILE_SIZE_ACTUAL = "file_size_actual"
    FILE_SIZE_SMALL = "file_size_small"
    FILE_SIZE_MEDIUM = "file_size_medium"
    FILE_SIZE_LARGE = "file_size_large"

    # Document Sizes for Action screen
    DOCUMENT_SIZE_A4 = "document_size_a4"
    DOCUMENT_SIZE_8x11 = "document_size_8.5x11"
    DOCUMENT_SIZE_8x14 = "document_size_8.5x14"
    DOCUMENT_SIZE_3x5 = "document_size_3.5x5"
    DOCUMENT_SIZE_4x6 = "document_size_4x6"
    DOCUMENT_SIZE_5x7 = "document_size_5x7"
    DOCUMENT_SIZE_BUSINESS_CARD = "document_size_business_card"
    DOCUMENT_SIZE_LICENSE = "document_size_license"

    # Print Size screen sizes
    PRINT_SIZE_4x6_TWO_SIDED = "print_size_4x6_two_sided"
    PRINT_SIZE_4x6 = "print_size_4x6"
    PRINT_SIZE_5x7 = "print_size_5x7"
    PRINT_SIZE_5x5 = "print_size_5x5"
    PRINT_SIZE_4x12 = "print_size_4x12"
    PRINT_SIZE_5x11 = "print_size_5x11"
    PRINT_SIZE_A4 = "print_size_a4"

    # Transform screen
    TRANSFORM_ROTATE_BTN = "rotate_image_btn"
    TRANSFORM_TITLE = "transform_title"

    # Detect Edges screen(iOS), Adjust boundaries screen (android)
    ADJUST_BOUNDARIES_TITLE = "adjust_boundaries_title"
    ADJUST_BOUNDARIES_NEXT_BTN = "next_btn"
    ADJUST_BOUNDARIES_AUTO_BTN = "adjust_boundaries_auto_btn"
    ADJUST_BOUNDARIES_FULL_BTN = "adjust_boundaries_full_btn"
    ADJUST_BOUNDARIES_FLATTEN_BTN = "adjust_boundaries_flatten_btn"
    
    # OCR Languages
    LANGUAGE_MAP = {}  # Locale Str: Language Str(What is displayed in app). Populate depending on platform.
    LOCALE_MAP = {}  # Language Str: Locale Str. Inverse of LANGUAGE_MAP. Populate depending on platform.

    PRINTER_NAME = "printer_name"
    PREVIEW_IMAGE = "preview_img"
    FILENAME_INFO_ICON = "smart_filename_info_btn"
    LANGUAGE_INFO_ICON = "language_info_btn"
    FILE_NAME_FIELD = "file_name_txt" 

    # DS Paper Size Options
    DS_PAPER_SIZE_5x7 = "ds_paper_size_5x7"
    DS_PAPER_SIZE_4x6 = "ds_paper_size_4x6"
    DS_PAPER_SIZE_8x5_11 = "ds_paper_size_8x5_11"
    DS_PAPER_SIZE_A4 = "ds_paper_size_a4"

    PREVIEW_EDIT_OPTIONS = [
        EDIT_BTN,
        REPLACE_BTN,
        DELETE_BTN
    ]

    DS_PAPER_SIZE_OPTIONS = [
        DS_PAPER_SIZE_5x7,
        DS_PAPER_SIZE_4x6,
        DS_PAPER_SIZE_8x5_11,
        DS_PAPER_SIZE_A4
    ]

    # ------------------------------------------------- Shared Verification Methods --------------------------------------------------
    def verify_title(self, title, timeout=10, invisible=False, raise_e=True, use_str_id=True):
        """
        Verifies the title of the preview screen.
        :param title: The expected title
        """
        if use_str_id:
            return self.driver.wait_for_object("title_txt", format_specifier=[self.driver.return_str_id_value(title)], timeout=timeout, invisible=invisible, raise_e=raise_e)
        else:
            return self.driver.wait_for_object(title, timeout=timeout, invisible=invisible, raise_e=raise_e)
        
    # ----------------------------------------------- Preview Landing - Action Methods -----------------------------------------------
    def select_bottom_nav_btn(self, btn):
        """
        Selects a button on the preview landing page's bottom navbar
        """
        if pytest.platform == "MAC":
            self.driver.click(btn, root_obj=self.driver.wait_for_object("bottom_navbar"))
        else:
            self.driver.click(btn, root_obj=self.driver.wait_for_object("bottom_navbar"), change_check={"wait_obj":"preview_title_str", "invisible": True})
    
    def select_top_toolbar_btn(self, btn):
        """
        Selects a button on the top of the preview landing page
        """
        top_toolbar = self.driver.wait_for_object("top_toolbar")
        if self.driver.click(btn, root_obj=top_toolbar, raise_e=False) is False:
            self.driver.swipe("top_toolbar", direction="left")
            self.driver.scroll(btn, scroll_object=top_toolbar, direction="right", click_obj=True)

    def select_more_options_btn(self, btn=None):
        """
        Selects the more options menu(vertical ellipses) button on the top right
        :param btn: "format" or "help"
        """
        self.driver.click("more_options_btn")
        if btn:
            self.driver.click(btn)

    def select_page_options_btn(self, btn=None):
        """
        Opens the page options menu(... button)
        :param btn: Selects the specified btn, only opens menu if btn is None
        """
        self.driver.click("page_options_btn")
        if btn:
            self.driver.click(btn)

    def select_rotate_btn(self, verify=False):
        """
        Selects the rotate button on the bottom right of the current page(Not the rotate button on the top bar)
        :param verify: If true verifies that the rotate image button goes invisible when rotating
        NOTE: the invisibility is too short to verify with wait_for_object so must check that the element's appium ID changed.
        """
        if verify:
            init_rotate_id = self.driver.get_attribute(self.TRANSFORM_ROTATE_BTN, "id")
            init_page_opt_id = self.driver.get_attribute("page_options_btn", "id")
            self.driver.click(self.TRANSFORM_ROTATE_BTN)
            assert init_rotate_id != self.driver.get_attribute(self.TRANSFORM_ROTATE_BTN, "id"), "Rotate image button id should have changed"
            assert init_page_opt_id != self.driver.get_attribute("page_options_btn", "id"), "Page options button id should have changed"
        else:
            self.driver.click(self.TRANSFORM_ROTATE_BTN)

    def select_exit_popup_btn(self, btn):
        """
        Selects a button on the "Are you done working?" popup
        :param btn: The button to select. "home", "scan", "add", or "cancel"
        """
        self.driver.click(f"exit_popup_{btn}_btn")

    def select_print_btn(self, timeout=5):
        """
        From the print page, after selecting printer, select the print btn
        """
        self.driver.click("print_btn", timeout=timeout)
    
    def select_replace_btn(self):
        self.driver.click(self.REPLACE_BTN)

    def swipe_to_page(self, page, timeout=30):
        """
        Swipe to a preview image
        :param page: The index of the desired image. Indexed at 1
        """
        end_time = time.time() + timeout
        current_page, total_pages = self.verify_preview_page_info(timeout=timeout)
        if page < 1  or page > total_pages:
            raise ValueError(f"Page {page} doesnt fall within range [1:{total_pages}]")
        while current_page != page:
            if time.time() >= end_time:
                raise TimeoutError(f"Could not swipe to preview image {page} in {timeout} seconds")
            self.driver.swipe(self.PREVIEW_IMAGE, direction="left" if current_page > page else "right")
            current_page, total_pages = self.verify_preview_page_info()

    def screenshot_all_preview_images(self):
        """
        Screenshots all the preview images
        :return: A list of preview images in order
        """
        page_count = self.verify_preview_page_info()[1]
        images = list()
        
        for i in range(1, page_count + 1):
            self.swipe_to_page(i)
            images.append(self.verify_preview_img())
        return images

    def zoom_preview_image(self):
        self.driver.wait_for_object(self.PREVIEW_IMAGE)
        self.driver.pinch(pinch_obj=self.PREVIEW_IMAGE, move_in=False)

    def select_preview_image(self, change_check=None):
        """
        Click on the image on Print Preview screen
        """
        self.driver.click("preview_img", change_check=change_check)

    # -------------------------------------------- Preview Dynamic Studio function --------------------------------------------
    def verify_select_printer_screen(self):
        """
        verify the select printer screen is visible
        """
        self.driver.wait_for_object("select_printer_title")

    def verify_dynamic_studio_screen(self, timeout=10):
        """
        Verify current screen is DS screen via:
        - Preview button
        """
        self.driver.wait_for_object("preview_btn", timeout=timeout)

    def verify_ds_image(self, timeout=10):
        """
        Verify the DS image is visible
        """
        self.driver.wait_for_object("ds_image", timeout=timeout)
    
    def verify_additional_paper_option(self):
        """
        Verify the additional paper option icon displays on Dynamic studido screen
        """
        self.driver.wait_for_object("additional_paper_option")
        self.driver.wait_for_object("image_potrait_orientation_option")
        self.driver.wait_for_object("image_landscape_orientation_option")

    def verify_additional_paper_size_options(self):
        """
        Verify Paper Size options after clicking on additional paper icon
        """
        self.driver.wait_for_object("check_mark_icon")
        self.driver.wait_for_object("ds_paper_size_8x5_11")

    def verify_cards_screen(self):
        """
        verify Cards screen on Dynamic stuido screen
        """
        self.driver.wait_for_object("front_btn")
        self.driver.wait_for_object("back_btn")

    def verify_mothers_day_template_option(self, invisible=False):
        """
        verify Mothers Day template option on Cards screen
        """
        self.driver.wait_for_object("mothers_day_template_option", invisible=invisible)

    def verify_graduation_template_option(self, invisible=False):
        """
        verify Graduation template option on Cards screen
        """
        self.driver.wait_for_object("graduation_tenplate_option", invisible=invisible)

    def verify_paper_main_tray_option(self, invisible=False, timeout=10, raise_e=True):
        """
        Verify if the main tray option on DS screen
        """
        self.driver.wait_for_object("ds_paper_main_tray", invisible=invisible, timeout=timeout, raise_e=raise_e)

    def verify_paper_main_tray_selected(self):
        """
        Verify if the Main tray option on DS screen
        """
        self.driver.wait_for_object("ds_paper_main_tray_selected")

    def verify_paper_photo_tray_option(self, invisible=False, raise_e=True):
        """
        Verify if the photo tray option on DS screen
        """
        self.driver.wait_for_object("ds_paper_photo_tray", invisible=invisible, raise_e=raise_e)

    def verify_paper_photo_tray_selected(self):
        """
        Verify if the photo tray option on DS screen
        """
        self.driver.wait_for_object("ds_paper_photo_tray_selected")

    def verify_exit_without_saving_popup(self):
        """
        verify current screen is Exit without Saving popup screen
        """
        self.driver.wait_for_object("exit_without_saving_popup_title")

    def verify_cards_options(self, invisible=False):
        """
        Verify Cards option shows on DS screen for Printer which supports photo duplex feature, like Novelli, Victoria
        """
        self.driver.wait_for_object("ds_cards_btn", invisible=invisible)

    def verify_layout_options(self):
        """
        verify Layout options on Dynamic stuido screen
        """
        self.driver.wait_for_object("ds_layout_fit_option")
        self.driver.wait_for_object("ds_layout_fill_option")
        self.driver.wait_for_object("ds_layout_rotate_option")
        self.driver.wait_for_object("ds_layout_flip_h_option")

    def verify_retrieving_page_size_popup(self, timeout=10, raise_e=True):
        """
        Verify Retrieving Page Size popup when opening DS screen for the first time
        """
        self.driver.wait_for_object("ds_retrieving_image_txt", timeout=timeout, raise_e=raise_e)
    
    def verify_paper_sizes(self):
        for size in self.DS_PAPER_SIZE_OPTIONS:
            self.driver.wait_for_object(size)
    
    def verify_paper_size(self, size):
        return self.driver.wait_for_object(f"ds_paper_size_{size}")
    
    def verify_paper_size_warning_message(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("ds_paper_size_warning_message", timeout=timeout, raise_e=raise_e)
    
    def verify_paper_size_warning_message_and_clear(self, default_size="8x5_11"):
        for size in self.DS_PAPER_SIZE_OPTIONS:
            click_result = self.driver.click(size, raise_e=False)
            if click_result and self.verify_paper_size_warning_message(timeout=5, raise_e=False):
                break
        self.select_paper_size(default_size)
        self.verify_paper_main_tray_option()
        
    def verify_info_btn(self, invisible=False):
        """
        verify info button on Dynamic studio screen
        """
        self.driver.wait_for_object("ds_info_unselected_btn", invisible=invisible)
    
    def verify_tooltip(self, timeout=10, raise_e=True):
        """
        verify tooltip on Dynamic studio screen when we select the info button
        """
        self.driver.wait_for_object("ds_info_selected_btn", timeout=timeout, displayed=False, raise_e=raise_e)
        return self.driver.wait_for_object("ds_info_tooltip", timeout=timeout, raise_e=raise_e)
    
    def verify_fit_and_fill_options_unselected(self):
        """
        Verifies that the fit and fill options are unselected
        """
        assert not self.driver.wait_for_object("ds_layout_fit_option_selected", timeout=5, raise_e=False) and not self.driver.wait_for_object("ds_layout_fill_option_selected", timeout=3, raise_e=False), "Fit and fill options should be unselected"
    
    def verify_landscape_orientation_button_selected(self, timeout=10, raise_e=True):
        """
        Verify that Landscape Orientation button on DS screen is selected
        """
        return self.driver.wait_for_object("image_landscape_orientation_option_selected", timeout=timeout, raise_e=raise_e)

    def verify_potrait_orientation_button_selected(self, timeout=10, raise_e=True):
        """
        Verify that Potrait Orientation button on DS screen is selected
        """
        return self.driver.wait_for_object("image_potrait_orientation_option_selected", timeout=timeout, raise_e=raise_e)

    def verify_zoom_in_btn(self, timeout=10, raise_e=True, invisible=False):
        """
        Verify Zoom In button on Print Preview screen
        """
        return self.driver.wait_for_object("zoom_in_btn", timeout=timeout, raise_e=raise_e, invisible=invisible)

    def verify_zoom_out_btn(self, timeout=10, raise_e=True, invisible=False):
        """
        Verify Zoom Out button on Print Preview screen
        """
        return self.driver.wait_for_object("zoom_out_btn", timeout=timeout, raise_e=raise_e, invisible=invisible)

    def screenshot_print_preview_image(self):
        """
        Screenshots the DS image
        """
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("preview_img"))

    def select_zoom_in_btn(self):
        """
        Click on Zoom In button on Print Preview screen
        """
        self.driver.click("zoom_in_btn")

    def select_zoom_out_btn(self):
        """
        Click on Zoom Out button on Print Preview screen
        """
        self.driver.click("zoom_out_btn")

    def select_info_btn(self):
        """
        Click on info button on Dynamic studio screen
        """
        self.driver.click("ds_info_unselected_btn")
    
    def select_paper_size(self, size):
        """
        Click on paper size on Dynamic studio screen
        """
        if size == "8.5x11 in":
            size = "8x5_11"
        self.driver.click(f"ds_paper_size_{size}")
    
    def select_no_btn(self):
        """
        Click on No button on from Exit Saving popup screen
        """
        self.driver.click("exit_without_saving_no_btn")

    def select_yes_btn(self):
        """
        Click on Yes button from Exit Saving popup screen
        """
        self.driver.click("exit_without_saving_yes_btn")

    def select_ds_layout_btn(self):
        """
        Click on Layout button on Dynamic Studio screen
        """
        self.driver.click("ds_layout_btn")

    def select_ds_paper_btn(self):
        """
        Click on paper button on the bottom of Dynamic Studio screen
        """
        self.driver.click("ds_paper_btn")

    def select_ds_cards_btn(self):
        """
        Click on Cards button on Dynamic Studio screen
        """
        self.driver.click("ds_cards_btn")

    def select_ds_paper_main_tray_option(self):
        """
        Click on Main Tray on DS screen
        """
        self.driver.click("ds_paper_main_tray")

    def select_ds_paper_photo_tray_option(self, timeout=10):
        """
        Click on Photo Tray on DS screen
        """
        self.driver.click("ds_paper_photo_tray", timeout=timeout)

    def select_cards_front_btn(self):
        """
        Click on Front button from Cards screen
        """
        self.driver.click("front_btn")

    def select_cards_back_btn(self):
        """
        Click on Back button from Cards screen
        """
        self.driver.click("back_btn")

    def select_mothers_day_template(self):
        """
        Select mothers day template from Cards screen
        """
        self.driver.click("mothers_day_template_option")

    def select_graduation_template(self):
        """
        Select graduation template from Cards screen
        """
        self.driver.click("graduation_template_option")

    def select_printer_title(self):
        """
        CLick on Printer object title to go to Select the printer screen
        """
        self.driver.click("printer_object_title")

    def select_undo_btn(self):
        """
        Click on Undo button on DS screen
        """
        self.driver.click("undo_btn")

    def select_redo_btn(self):
        """
        Click on Redo button on DS screen
        """
        self.driver.click("redo_btn")

    def select_landscape_orientation_button(self):
        """
        Click on Landscape Orientation button on DS screen
        """
        self.driver.click("image_landscape_orientation_option")

    def select_potrait_orientation_button(self):
        """
        Click on Potrait Orientation button on DS screen
        """
        self.driver.click("image_potrait_orientation_option")

    def select_additional_paper_btn(self):
        """
        Click on Additional Paper button on DS screen
        """
        self.driver.click("additional_paper_option")

    def select_fit_btn(self):
        """
        Click on Fit button from Layout options of DS screen
        """
        self.driver.click("ds_layout_fit_option")

    def select_fill_btn(self):
        """
        Click on Fill button from Layout options of DS screen
        """
        self.driver.click("ds_layout_fill_option")

    def select_ds_rotate_btn(self, timeout=10):
        """
        Click on rotate button from Layout options of DS screen
        """
        self.driver.click("ds_layout_rotate_option", timeout=timeout)

    def select_border_btn(self):
        """
        Click on Border button from Layout options of DS screen
        """
        self.driver.click("ds_layout_border_option")

    def select_crop_btn(self):
        """
        Click on Crop button from Layout options of DS screen
        """
        self.driver.click("ds_layout_crop_option")

    def select_flip_h_btn(self):
        """
        Click on Flip H button from Layout options of DS screen
        """
        self.driver.scroll("ds_layout_flip_h_option", direction="right", click_obj=True)

    def select_flip_v_btn(self):
        """
        Click on Flip V button from Layout options of DS screen
        """
        self.driver.click("ds_layout_flip_v_option")

    def select_preview_btn(self):
        """
        Click on Preview button on DS screen
        """
        self.driver.click("preview_btn", change_check={"wait_obj": "preview_btn", "invisible": True})

    def select_checkmark_btn_on_paper_selection_screen(self):
        """
        Click on Checkmark button on paper selection screen
        """
        self.driver.click("check_mark_icon")
    
    def dismiss_tooltip(self, raise_e=False):
        if self.verify_tooltip(timeout=3, raise_e=raise_e):
            self.driver.click_by_coordinates(area='mm')
    
    def go_to_paper_selection_screen_using_main_tray(self):
        self.driver.wdvr.execute_script("mobile:doubleTap", {"element": self.driver.wait_for_object("ds_paper_main_tray")})
    
    def get_default_paper_size(self):
        return self.driver.get_attribute("ds_default_paper_size", "name")
    
    def screenshot_ds_image(self):
        """
        Screenshots the DS image
        """
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("ds_image"))
    
    def double_tap_ds_image(self):
        """
        Double tap on DS image
        """
        self.driver.double_tap("ds_image")

    def select_ds_image(self):
        """
        Selects the image on DS screen
        """
        self.driver.click("ds_image")
    
    # -------------------------------------------- Preview Landing - Verification Methods --------------------------------------------
    def verify_preview_screen(self, chk_bottom_navbar=True):
        """
        Verifies the preview landing page
        """
        self.verify_title(self.PREVIEW_TITLE, timeout=30)
        if chk_bottom_navbar:
            return self.driver.wait_for_object("bottom_navbar")
        else:
            return True
    
    def verify_preview_img(self, screenshot=True, page_number=1):
        """
        Verifies the preview image.
        :param screenshot: Return a screenshot of the preview image.
        """
        if screenshot:
            if self.driver.driver_info["platformName"].lower() == "android":
                return saf_misc.load_image_from_base64(self.driver.screenshot_element(self.PREVIEW_IMAGE))
            else:
                if page_number == 1:
                    # The page source captures a part the images before and after the current image.
                    # If we're taking a screenshot of the 1st image we choose the first photo that shows up in the page source
                    return saf_misc.load_image_from_base64(self.driver.screenshot_element("preview_img_by_page", format_specifier=[page_number]))
                else:
                    # If it is not the 1st image we choose the 2nd photo that shows up in the page source
                    return saf_misc.load_image_from_base64(self.driver.screenshot_element("preview_img_by_page", format_specifier=[2]))
        return self.driver.wait_for_object(self.PREVIEW_IMAGE)

    def verify_preview_edit_options(self, verify_delete_option=True):
        """
        Verifies the page options menu
         - edit button
         - replace button
         - delete button
        """
        for option in self.PREVIEW_EDIT_OPTIONS:
            if option == self.DELETE_BTN and not verify_delete_option:
                continue
            self.driver.wait_for_object(option)
    
    def verify_rotate_btn(self, invisible=False):
        """
        Verifies the rotate button on the bottom right of the current page(Not the rotate button on the top bar)
        """
        self.driver.wait_for_object(self.TRANSFORM_ROTATE_BTN, invisible=invisible)

    def verify_is_image_selected(self, index=1, raise_e=True):
        """
        Verifies if an image with the specified index is selected (Indexing starts at 1)
        """
        return self.driver.wait_for_object("auto_rotate_image_checkmark", format_specifier=[index], raise_e=raise_e)

    def verify_preview_page_info(self, timeout=10, displayed=True, is_one_page=False):
        """
        Get the current page and total page count.
        if there is only one page the pages count doesn't show up on the screen
        :return: Returns a tuple of (current page, total pages)
        """
        if is_one_page:
            return self.driver.wait_for_object("preview_page_count_txt", invisible=True)
        else:
            counter_parts = self.driver.get_attribute("preview_page_count_txt", "text", timeout=timeout, displayed=displayed).strip().split("/")
            return (int(counter_parts[0]), int(counter_parts[-1]))

    def verify_processing_pages_popup(self):
        """
        Verifies the "Processing pages" popup that appears when clicking the redaction button.
        NOTE: Popup disappears very quickly if few pages are loaded. Recomended to load 4 pages for verifying this popup.
        Only Verifying Cancel button because the popup is disappearing quickly 
        """
        self.driver.wait_for_object("processing_popup_cancel_btn", interval=0.2)

    def verify_exit_popup(self):
        """
        Verifies the "Are you done working?" popup
        """
        self.driver.wait_for_object("exit_popup_title")
        self.driver.wait_for_object("exit_popup_home_btn")
        self.driver.wait_for_object("exit_popup_scan_btn")
        self.driver.wait_for_object("exit_popup_add_btn")
        self.driver.wait_for_object("exit_popup_cancel_btn")

    def verify_shortcuts_popup(self):
        """
        Verifies the shortcuts popup
        """
        self.driver.wait_for_object("shortcuts_file_name")

    def verify_no_shortcuts_popup(self):
        """
        Verify new Shortcuts popup
        """
        self.driver.wait_for_object("no_shortcuts_option", timeout=20)

    def verify_more_options_btns(self, btns=[FORMAT_BTN, HELP_BTN], invisible=False):
        """
        Verifies the more options menu
        :param btns: The buttons to verify
        """
        if not isinstance(btns, list):
            btns = [btns]
        for btn in btns:
            self.driver.wait_for_object(btn, invisible=invisible)
    
    def verify_top_toolbar(self, btns=[], invisible=False):
        """
        Verifies the top toolbar and the buttons specified
        """
        if not isinstance(btns, list):
            btns = [btns]

        if len(btns) == 0 and invisible:
            return self.driver.wait_for_object("top_toolbar", invisible=True)

        located_btns = set(btns if invisible else [])
        toolbar = self.driver.wait_for_object("top_toolbar")

        for btn in btns:
            if self.driver.wait_for_object(btn, root_obj=toolbar, timeout=5, invisible=invisible, raise_e=False):
                located_btns.add(btn)
            elif invisible:
                located_btns.remove(btn)

        if not invisible and len(located_btns) == len(btns):
            return True

        self.driver.swipe("top_toolbar", direction="right")

        for btn in btns:
            if (btn not in located_btns or invisible) and self.driver.wait_for_object(btn, root_obj=toolbar, timeout=5, invisible=invisible, raise_e=False):
                located_btns.add(btn)
            elif invisible:
                located_btns.remove(btn)
    
        missing_btns = [btn for btn in btns if btn not in located_btns]
        if len(missing_btns) > 0:
            raise NoSuchElementException(f'Could not locate {", ".join(missing_btns)} btns in top toolbar')
        return True

    def verify_bottom_nav(self, btns=[], invisible=False):
        """
        Verifies the bottom navbar and the buttons specified
        :param btns: List of buttons to verify
        :param invisible: The expected invisible status of the specified buttons
        """
        if not isinstance(btns, list):
            btns = [btns]
        navbar = self.driver.wait_for_object("bottom_navbar")
        for btn in btns:
            self.driver.wait_for_object(btn, root_obj=navbar, invisible=invisible)

    def verify_language_info_btn(self, displayed=True):
        """
        verifies the proper message appears.
        """
        self.driver.wait_for_object("language_info_str", displayed=displayed)

    # ---------------------------------- Action(Share/Save/Convert to Text) Screen - Action Methods ---------------------------------- 
    def select_action_btn(self, change_check=None):
        """
        Selects the action(Share / Save, Share, Save or Create File) button
        """
        if pytest.platform == "MAC":
            self.driver.click("action_btn")
        else:
            self.driver.scroll("action_btn", check_end=False, timeout=10)
            self.driver.click("action_btn", change_check=change_check)
    
    def rename_file(self, file_name):
        """
        Sets the file name
        """
        self.driver.send_keys(self.FILE_NAME_FIELD, file_name)
        
    def select_file_type(self, file_type=None):
        """
        Selects the specified file type
        :param file_type: The file type to select. If None leaves the file_type menu open.
        """
        raise NotImplementedError("Must implement per platform")
    
    def toggle_smart_file_name(self, enable=True):
        """
        Toggles the smart file name switch
        """
        self.driver.check_box("smart_filename_switch", uncheck=not enable)

    def select_smart_file_name_info_btn(self):
        """
        Selects the I button on smart file name and verifies the proper message appears.
        """
        self.driver.click(self.FILENAME_INFO_ICON, change_check={"wait_obj": "smart_filename_info_str", "invisible": False, "displayed": self.platform != "ios"})

    def toggle_pdf_password(self, enable=True):
        """
        Toggles the PDF password switch
        :param enable: Enable or disable the password protection switch
        """
        self.driver.check_box("pdf_password_switch", uncheck=not enable)

    def enter_pdf_password(self, password):
        """
        Sets the password to use for pdf password protection
        :param password: The password to enter.
        """
        self.driver.send_keys("pdf_password_txt", password, press_enter=self.platform == "ios")

    def select_file_size(self, file_size=None):
        """
        Opens the file size dropdown and selects the specified file size. If no file specified it only opens the file size dropdown menu.
        :param file_size: The file size to select.
        """
        self.driver.click("file_size_btn", raise_e=False)
        if file_size:
            self.driver.click("file_size_item", format_specifier=[self.driver.return_str_id_value(file_size).split("%s")[0]])

    def select_language_btn(self):
        """
        Selects the language button, opening the language menu.
        NOTE: Also used for the language button on the native text extract screen
        """
        self.driver.click("language_btn")

    def select_language(self, locale):
        """
        Selects the specified locale on the language menu.
        :param locale: The locale of the language to select.
        """
        self.driver.scroll("language_menu_item", format_specifier=[self.LANGUAGE_MAP[locale]], click_obj=True)

    def select_language_info_btn(self):
        """
        Selects the I button on the language selection and verifies the proper message appears.
        """
        self.driver.click("language_info_btn")

    def select_downloading_language_cancel_btn(self):
        """
        Selects the cancel button on the downloading language popup
        """
        self.driver.click("downloading_lang_cancel_btn", interval=0.2, change_check={"wait_obj": "downloading_lang_cancel_btn", "invisible": True})

    def dismiss_file_saved_popup(self):
        """
        Dismiss the "Your file has been saved!" popup
        """
        if self.driver.wait_for_object("file_saved_popup_ok_btn", raise_e=False):
            self.driver.click("file_saved_popup_ok_btn", change_check={"wait_obj": "file_saved_popup_ok_btn", "invisible": True})

    def click_go_to_home_button(self):
        """
        Dismiss the "Your file has been saved!" popup by clicking on "Go to Home" button
        """
        if self.driver.wait_for_object("go_to_home_btn", raise_e=False):
            self.driver.click("go_to_home_btn", change_check={"wait_obj": "go_to_home_btn", "invisible": True})

    def resize_image_on_ds_screen(self, source, destination):
        """
        Resize image on DS screen
        """
        self.driver.drag_and_drop(source, destination)

    def get_ds_image_coordinates(self):
        """
        Get the coordinates of the DS image
        """
        navbar_height = json.loads(self.driver.get_attribute("preview_btn", "rect"))["height"]
        d = json.loads(self.driver.get_attribute("ds_image", "rect"))
        return (d["width"] // 2, d["y"] + navbar_height)

    # ------------------------------- Action(Share/Save/Convert to Text) Screen - Verification Methods -------------------------------
    def verify_action_screen(self, invisible=False, pro=False):
        """
        Verifies the action screen
        :param pro: Verify pro features
        """
        self.driver.wait_for_object(self.FILE_NAME_FIELD, invisible=invisible)
        self.driver.wait_for_object("file_type_dropdown", invisible=invisible)
        self.driver.wait_for_object("action_btn", invisible=invisible)
        if pro:
            self.driver.wait_for_object("pdf_password_switch", invisible=invisible)

    def verify_file_name(self):
        """
        Verifies the current filename
        """
        return self.driver.get_text(self.FILE_NAME_FIELD)

    def verify_pdf_password(self, enabled=True):
        """
        Verifies the pdf password entry box.
        """
        switch_state = self.driver.get_attribute("pdf_password_switch", "checked" if self.platform == "android" else "value")
        switch_state = switch_state == "true" or switch_state == "1"
        assert switch_state == enabled, "Switch state is not enabled: {}".format(enabled)
        self.driver.wait_for_object("pdf_password_txt", invisible=not enabled)

    def verify_file_types(self, file_types, invisible=False):
        """
        Verifies file types
        :param file_types: A list of file_types
        """
        for f in file_types:
            self.driver.wait_for_object(f, invisible=invisible)

    def verify_selected_file_type(self, file_type):
        """
        Verifies the selected file type
        :param file_type: The expected file type
        """
        self.driver.wait_for_object("file_type_dropdown", format_specifier=[self.driver.return_str_id_value(file_type)])

    def verify_file_size(self, file_size):
        """
        Verifies file size(s). Can be used to verify selected file size(file size menu closed) or file size exists in menu(file size menu open).
        :param file_size: The file size(s) to verify. Can pass list of file sizes to verify multiple.
        """
        if not isinstance(file_size, list):
            file_size = [file_size]
        for fs in file_size:
            self.driver.wait_for_object("file_size_item", format_specifier=[self.driver.return_str_id_value(fs).split("%s")[0]])

    def verify_document_size(self, invisible=False, selected_size=None):
        """
        Verify Document size item on Save/Share Option screen
        :param invisible
        :param selected_size: If invisible == False verifies that the specified document size is selected.
        """
        self.driver.wait_for_object("document_size_spinner", invisible=invisible)
        if invisible is False and selected_size is not None:
            self.driver.wait_for_object(selected_size)

    def verify_hint(self, message):
        """
        Verifies the hint displays the specified message
        :param message: The locator of the message to verify.
        """
        self.driver.scroll(message)

    def verify_language_menu_items(self):
        """
        Gets the locales of the language menu items. Only verifies visible languages on android.
        """
        self.driver.wait_for_object("language_menu_item")
        return [self.LOCALE_MAP[e.text] for e in self.driver.find_object("language_menu_item", multiple=True)]

    def verify_selected_language(self, locale=None, on_menu=False, raise_e=True):
        """
        Returns the selected language's locale str.
        :param on_menu: Verify checkmark on language menu.
        """
        lang_locator = "selected_language_txt" if on_menu else "language_btn"
        if not raise_e and self.driver.wait_for_object(lang_locator, raise_e=False) is False:
            return False
        selected_locale = self.LOCALE_MAP[self.driver.get_text(lang_locator)]
        if locale is None:
            return self.LOCALE_MAP[self.driver.get_text(lang_locator)]
        elif raise_e:
            assert selected_locale == locale, f'Selected locale "{selected_locale}" != expected locale "{locale}"'
        return selected_locale == locale

    def verify_downloading_language_popup(self, invisible=False):
        """
        Verifies the downloading language popup
        """ # TODO: Verify these locators
        self.driver.wait_for_object("downloading_lang_title_txt", interval=0.2, invisible=invisible)
        self.driver.wait_for_object("downloading_lang_sub_txt", interval=0.2, invisible=invisible)
        self.driver.wait_for_object("downloading_lang_cancel_btn", interval=0.2, invisible=invisible)

    def verify_downloading_language_canceled_toast(self):
        """
        Verifies the "Language pack download aborted" toast message
        """
        self.driver.wait_for_object("downloading_lang_cancel_msg", interval=0.2, displayed=False)

    def verify_smart_file_name(self):
        """
        Verifies the smart filename elements and the state of the smart filename switch
        """
        self.driver.wait_for_object("smart_filename_txt")
        self.driver.wait_for_object(self.FILENAME_INFO_ICON)
        return True if self.driver.get_attribute("smart_filename_txt", "checked") == "true" else False
    
    # ---------------------------------------------- Print Help Screen - Action Methods ----------------------------------------------
    def select_ok_btn(self):
        """
        Selects the ok button the Print Help screen
        """
        self.driver.click("print_help_ok_btn")
    
    def toggle_print_help_option(self, option, enabled=True):
        """
        Toggles the checbkox on the Print Help screen
        :param option: The checkbox to toggle
        :param enabled: The desired state of the checkbox
        """
        self.driver.check_box(option, uncheck=not enabled)

    def select_print_help_link(self, link):
        """
        Selects a lin on the Print Help screen
        :param link: "google_play" or "settings"
        """
        self.driver.click(f"{link}_link")

    # ------------------------------------------- Print Help Screen - Verification Methods -------------------------------------------
    def verify_ok_btn(self, enabled=None):
        """
        Verify the ok button on the Print Help screen
        :param enabled: Enabled or disabled status of OK button
        """
        self.driver.wait_for_object("print_help_ok_btn")
        assert self.driver.get_attribute("print_help_ok_btn", "enabled").lower() == ("true" if enabled else "false")
    
    def verify_print_help_screen(self):
        """
        Verify Print Help screen
        """
        self.driver.wait_for_object("more_options_help_btn")
        self.driver.wait_for_object("google_play_link")
        self.driver.wait_for_object("settings_link")

    # --------------------------------------------- Print Format Screen - Action Methods ---------------------------------------------
    def select_print_format_option(self, format):
        """
        Selects a print format on the Print Format screen
        :param format: The format to select. "pdf" or "jpg"
        """
        self.driver.click(f"{format}_print_format")

    # ------------------------------------------ Print Format Screen - Verification Methods ------------------------------------------
    def verify_print_format_screen(self):
        """
        Verifies the print format screen
        """
        self.driver.wait_for_object("print_format_txt")
        self.driver.wait_for_object("jpg_print_format")
        self.driver.wait_for_object("pdf_print_format")

    # ---------------------------------------------- Print Size Screen - Action Methods ----------------------------------------------
    def select_print_size(self, btn=DOCUMENT_SIZE_8x11, timeout=10, raise_e=True):
        """
        Select a print size on the Print Size screen
        NOTE: Only appears for novelli printers
        :param btn: button to select
        """
        self.driver.click(btn, timeout=timeout, raise_e=raise_e)

    # ---------------------------------------------- Print Size Screen - Verification Methods ----------------------------------------------
    def verify_print_size_screen(self):
        return self.driver.wait_for_object(self.PRINT_SIZE_TITLE)
    
    # ------------------------------------------- Print Size Screen - Verification Methods -------------------------------------------
    def verify_two_side_print_unavailable(self):
        """
        Verifies the 4x6" Two-Sided print size option is disabled and has disabled subtext
        """
        self.driver.wait_for_object("two_side_print_unavailable_txt")

    # ----------------------------------------------------- Fax - Action Methods -----------------------------------------------------
    def select_fax_next(self):
        """
        Selects the next button on the compose fax screen.
        """
        self.driver.click("fax_next_btn", timeout=10)
    
    # -------------------------------------------------- Fax - Verification Methods --------------------------------------------------
    def verify_fax_limit_popup(self):
        """
        Verify milit popup for fax
        :param size_limit: Expect size limit
        """
        self.driver.wait_for_object("fax_limit_msg", timeout=20)

    # ---------------------------------------------- Two-Sided Preview - Action Methods ----------------------------------------------
    def select_two_sided_page_btn(self, btn):
        """
        Selects the front or back button on the two-sided preview screen
        :param btn: The button to select, "front" or "back"
        """
        self.driver.click(f"two_side_{btn}_btn")

    # ------------------------------------------- Two-Sided Preview - Verification Methods -------------------------------------------
    def verify_two_sided_preview_screen(self):
        """
        Verify Two-Sided Preview screen
         - Preview Title
         - Front button
         - Back button
         - Page options button
         - Rotate button
        """
        self.verify_title(self.TWO_SIDE_PREVIEW_TITLE)
        self.driver.wait_for_object("two_side_front_btn")
        self.driver.wait_for_object("two_side_back_btn")
        self.driver.wait_for_object("page_options_btn")

    def verify_two_sided_preview_img(self):
        """
        Verify and capture screenshot of Two-Sided Preview image
        """
        self.driver.wait_for_object("two_side_preview_img")
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("two_side_preview_img"))

    # --------------------------------------------- Auto-Rotate Screen - Action Methods ----------------------------------------------
    def select_auto_rotate_image(self, index, select=True):
        """
        Selects an image on the rotate screen
        :param index: The image index, indexed at 1. Matches numbering on ui.
        :param select: If True selects the desired image, if False deselects the desired image.
        """
        is_selected = self.driver.wait_for_object("auto_rotate_image_checkmark", format_specifier=[index], raise_e=False)
        if bool(is_selected) != select:
            self.driver.click("auto_rotate_image", format_specifier=[index], change_check={"wait_obj": "auto_rotate_image_checkmark", "format_specifier": [index], "invisible": not select, "timeout": 5})
        else:
            logging.info("Auto rotate image {} is already selected: {}".format(index, select))

    def select_multiple_images_on_rotate_screen(self, index_list):
        for index in index_list:
            try:
                self.select_auto_rotate_image(index)
            except NoSuchElementException:
                raise NoSuchElementException(f"Image with index {index} not found on rotate screen")

    def get_image_count_on_rotate_screen(self):
        """
        Get the number of images on the rotate screen
        """
        return len(self.driver.find_object("page_cell", multiple=True))

    def select_auto_rotate_option(self, option):
        """
        Selects a button on the rotate screen's slide bar.
        :param option: The button to select, the * component of "auto_rotate_*_btn" locators. 
            Possible Values: "delete", "rotate"
        """
        self.driver.click("auto_rotate_{}_btn".format(option))
        time.sleep(2)  # Delay to allow animation to complete

    def select_auto_rotate_reset_button(self):
        """
        Selects the reset button on the auto-rotate screen
        """
        self.driver.click("auto_rotate_reset_btn")

    def select_auto_rotate_done_button(self):
        """
        Selects the done button on the top right of the auto-rotate screen
        """
        self.driver.click("auto_rotate_done_btn")

    def hide_auto_rotate_slide_bar(self):
        """
        Drags the slide bar handle down
        """
        self.driver.drag_and_drop(self.driver.wait_for_object("auto_rotate_slide_bar_handle"), 
            self.driver.wait_for_object("auto_rotate_rotate_btn"), y_offset=20)

    def select_auto_rotate_discard_option(self, btn):
        """
        Selects the Yes or No button on the auto-rotate discard chagnes popup
        :param btn: Which button to press on the discard popup. Possbile Values: "yes" or "no"
        """
        self.driver.click("auto_rotate_discard_{}_btn".format(btn))

    def select_auto_rotate_delete_btn(self):
        self.driver.click("auto_rotate_delete_btn")

    def drag_bottom_navbar_down(self):
        self.driver.wdvr.execute_script("mobile: swipe", {"direction": "down", "element": self.driver.wait_for_object("bottom_navbar_handle")})
    # ------------------------------------------ Auto-Rotate Screen - Verification Methods -------------------------------------------
    def verify_auto_rotate_screen(self, image_selected=False):
        """
        Verifies the auto rotate screen.
         - "Rotate" title if image_selected == False
         - first image
         - reset button
         - Done button
        if image_selected == True verify visible otherwise verify invisible:
         - bottom slide bar handle
         - rotate button
         - delete button
        :param image_selected: If True verify the bottom slide bar with rotate and delete buttons
        """
        self.verify_title(self.ROTATE_TITLE, invisible=image_selected)
        self.driver.wait_for_object("auto_rotate_image")
        self.driver.wait_for_object("auto_rotate_reset_btn")
        self.driver.wait_for_object("auto_rotate_done_btn")
        self.driver.wait_for_object("auto_rotate_slide_bar_handle", invisible=not image_selected)
        self.driver.wait_for_object("auto_rotate_rotate_btn", invisible=not image_selected)
        self.driver.wait_for_object("auto_rotate_delete_btn", invisible=not image_selected)
    
    def verify_rotate_screen_tray_options(self):
        """
        Verifies the rotate screen tray options in the bottom when multiple images
        are added and at least one of them is selected (delete button won't be displayed if only one image is added)
        """
        self.driver.wait_for_object("auto_rotate_delete_btn")
        self.driver.wait_for_object("auto_rotate_rotate_btn")
    
    def verify_auto_rotate_image(self, index):
        """
        Captures a screenshot of a single auto_rotate_image
        :param index: The image index, indexed at 1
        """
        self.driver.wait_for_object("auto_rotate_image", format_specifier=[index])
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("auto_rotate_image", format_specifier=[index]))

    def verify_auto_rotate_reset_btn(self, active=None):
        """
        Verifies the reset button on the auto rotate screen
        :param active: If None ignore reset button state. If True verify reset button is clickable if False verify it is not clickable.
        """
        self.driver.wait_for_object("auto_rotate_reset_btn")
        if active is not None:
            assert self.driver.get_attribute("auto_rotate_reset_btn", "enabled") == "true" if active else "false", "Expected reset button to be enabled: {}".format(active)

    def verify_auto_rotate_image_count(self, count):
        """
        Get the number of images on the auto_rotate image screen
        """
        self.driver.wait_for_object("auto_rotate_image")
        img_count = len(self.driver.find_object("auto_rotate_image", multiple=True)) 
        assert img_count == count, "Image count: {} does not match desired count: {}".format(img_count, count)

    def verify_discard_changes_popup(self, raise_e=True):
        """
        Verifies the discard changes popup
        """
        return self.driver.wait_for_object("auto_rotate_discard_title", raise_e=raise_e) and self.driver.wait_for_object("auto_rotate_discard_txt", raise_e=raise_e)
    
    # ----------------------------------------------- Reorder Screen - Action Methods ------------------------------------------------
    def select_reorder_done(self):
        """Selects the done button on the reorder screen"""
        self.driver.click("reorder_done_btn")
    
    def reorder_image(self, to_move, destination):
        """
        Moves an image to the specified index
        :param to_move: The image index, indexed at 1
        :param destination: The index to move the image to, indexed at 1
        """
        to_move = self.driver.find_object("reorder_img", format_specifier=[to_move])
        destination = self.driver.find_object("reorder_img", format_specifier=[destination])
        get_offset = lambda axis: 25 if to_move.location[axis] < destination.location[axis] else -25
        self.driver.drag_and_drop(to_move, destination, x_offset=get_offset("x"), y_offset=get_offset("y"))

    def select_reorder_discard_option(self, btn):
        """
        Selects the Yes or No button on the reoeswe discard changes popup
        :param btn: Which button to press on the discard popup. Possbile Values: "yes" or "no"
        """
        self.driver.click("reorder_discard_{}_btn".format(btn))

    # -------------------------------------------- Reorder Screen - Verification Methods ---------------------------------------------
    def verify_reorder_screen(self):
        """
        Verify the reorder screen
         - "Reorder" title
         - done button
         - a reorder image
        """
        self.verify_title(self.REORDER_TITLE)
        self.driver.wait_for_object("reorder_done_btn")
        self.driver.wait_for_object("reorder_img", format_specifier=[1])

    # ------------------------------------------------ Text Extract - Action Methods -------------------------------------------------
    def select_text_extract_btn(self):
        """
        Click Text Extract Button
        """
        self.driver.click("text_extract_btn")

    # --------------------------------------------- Text Extract - Verification Methods ----------------------------------------------
    def verify_text_extract_screen(self, timeout=10):
        """
        Verifies the text extract screen which appears before the text extract webview
        """
        self.driver.wait_for_object(self.TEXT_EXTRACT_TITLE, timeout=timeout)
        self.driver.wait_for_object("continue_btn", timeout=timeout)
        self.driver.wait_for_object("language_btn", timeout=timeout)
    
    def verify_text_extract_edit_text_cancel_btn(self, timeout=30, raise_e=True):
        """
        Verify Cancel Button on Text Extract Edit screen
        raise_e for case where no text was extracted
        """
        self.driver.wait_for_object('text_extract_edit_text_cancel_btn', timeout=timeout, raise_e=raise_e)

    def verify_no_text_extracted_dialog(self):
        """
        Check for No Text Extracted Dialog
        """
        self.driver.wait_for_object("text_not_extracted", timeout=10)

    def verify_text_extract_btn(self, invisible=False):
        """
        Verify the add more page button on Preview
        :param invisible: verify if visibility or invisibility
               - True: is invisibility
               - False: is visibility
        """
        self.driver.wait_for_object("text_extract_btn", invisible=invisible, timeout=10)
    
    # --------------------------------------------- Adjust boundaries screen - Verification Methods ----------------------------------------------
    def verify_adjust_boundaries_screen(self, timeout=10):
        self.verify_title(self.ADJUST_BOUNDARIES_TITLE, timeout=timeout)
        return self.driver.wait_for_object(self.ADJUST_BOUNDARIES_NEXT_BTN)
    
    # --------------------------------------------- Adjust boundaries screen - Action Methods ----------------------------------------------
    def nav_detect_edges_screen(self):
        # Depending on printer, scan job takes longer sometimes
        self.verify_adjust_boundaries_screen(timeout=30)
        self.driver.click(self.ADJUST_BOUNDARIES_NEXT_BTN)

class AndroidPreview(Preview):
    platform = "android"

    # Title Str Locators
    CONVERT_TO_TEXT_TITLE = "convert_to_text_title_str"
    SHARE_TITLE = "share_title_str"
    SAVE_TITLE = "save_title_str"

    # Bottom Navbar buttons for Preview Landing page
    SHARE_BTN = "share_btn"
    SAVE_BTN = "save_btn"

    # Hint Strings for Action screen
    FORMAT_HINT = "format_hint_str"

    def __init__(self, driver):
        super().__init__(driver)
        self.LANGUAGE_MAP = {locale: self.driver.return_str_id_value_from_id("language_" + locale) for locale in ['ar', 'bg', 'ca', 'cs', 'da', 
            'de', 'de_LU', 'el', 'en', 'en_UK', 'es', 'et', 'fi', 'fr', 'ga', 'he', 'hr', 'hu', 'id', 'is', 'it', 'ja', 'ko', 'lt', 'lv', 
            'mi', 'mt', 'nl', 'no', 'pl', 'pt', 'pt_BR', 'ro', 'ru', 'sk', 'sl', 'sv', 'tr', 'zh_CN', 'zh_TW', 'gd']}
        self.LOCALE_MAP = {lang: locale for locale, lang in self.LANGUAGE_MAP.items()}

    # ---------------------------------- Action(Share/Save/Convert to Text) Screen - Action Methods ----------------------------------
    def select_action_btn(self, change_check={"wait_obj": "action_btn", "invisible": True}):
        """
        Selects the action(Share, Save or Create File) button
        """
        try:
            super().select_action_btn(change_check=change_check)
        except NoSuchElementException:
            self.driver.click("action_btn")
            if self.driver.wait_for_object("img_too_large_toast", interval=0.2, displayed=False, raise_e=False):
                pytest.skip("Skipping to avoid failure due to automation only issue. AIOA-12949")
            else:
                raise

    def select_file_type(self, file_type=None):
        """
        Selects the specified file type
        :param file_type: The file type to select. If None leaves the file_type menu open.
        """
        self.driver.click("file_type_dropdown", timeout=10, raise_e=file_type is None)
        if file_type:
            self.driver.click(file_type)

    def select_document_size(self, size=None):
        """
        Selects the document size on the Save/Share Option screen
        :param size: The document size to select. If None leaves the document size menu open.
        """
        self.driver.click("document_size_spinner", timeout=10, raise_e=size is None)
        if size:
            self.driver.click("document_size_spinner", format_specifier=[self.driver.return_str_id_value(size).split("%s")[0]])

    def click_print_settings_more_btn(self):
        """
        Click on More Options button on Print Preview screen
        """
        self.driver.click("print_more_options")

    def click_email(self):
        """
        Select click gmail option on Share screen
        """
        self.driver.click("share_gmail_str")

    def send_email(self):
        """
        Select send gmail
        """
        self.driver.click("send_btn")

    def select_share_destination(self, email_count=1):
        """
        Create and enter multiple email addresses in the 'To' section
        :param email_count: Number of email addresses to create and enter (max 21)
        """
        email_list = [f"test{i}@example.com" for i in range(1, email_count + 1)]
        # Join emails with comma separator and enter in the field
        email_string = ", ".join(email_list)
        self.driver.send_keys("to_tf", email_string)

    def toggle_save_to_hp_smart(self, enable=True):
        """
        Toggles the "Save Original to HP Smart Files" switch
        """
        self.driver.check_box("save_hp_files_switch", uncheck=not enable)

    def select_language(self, locale=None, index=None):
        """
        Selects a language by locale or index(visible elements only).
        :param language: Language to select
        :param index: Index(visible languages) of the language to select. Recommended to use index=-1 if trying to test downloading a language.
        """
        assert locale is None or index is None, "language and index are exclusive"
        if locale is not None:
            self.driver.scroll("language_menu_item", format_specifier=[self.LANGUAGE_MAP[locale]], click_obj=True)
        elif index is not None:
            self.driver.click("language_menu_item", index=index)
        else:
            raise ValueError("Must specify language or index")
        return True

    def select_language_done_btn(self):
        """
        Selects the done button on the language selection menu.
        """
        self.driver.click("language_done_btn", change_check={"wait_obj": "language_done_btn", "invisible": True}, retry=4)

    # ------------------------------- Action(Share/Save/Convert to Text) Screen - Verification Methods -------------------------------
    def verify_convert_to_text_screen(self):
        """
        Verifies the convert to text screen which appears when selecting an advanced file type on the action screen
        """
        # save to hp smart switch
        # language button
        # language info button
        # action button with "create file" text
        self.verify_title(self.CONVERT_TO_TEXT_TITLE)
        self.driver.wait_for_object("save_hp_files_switch")
        self.driver.wait_for_object("language_info_btn")
        self.driver.wait_for_object("language_btn")
        self.driver.wait_for_object("action_btn", format_specifier=[self.driver.return_str_id_value("create_file_str")])

    def verify_save_to_hp_smart(self, enabled=None):
        """
        Verifies the save to hp smart switch
        :param enabled: The expected state of the switch
        """
        assert self.driver.get_attribute("save_hp_files_switch", "checked") == ("true" if enabled else "false")
    
    def verify_language_menu_items(self, timeout=60):
        """
        Verifies all the languages on the languages menu.
        """
        expected_locales =[l for l in self.LANGUAGE_MAP.keys()]
        end_time = time.time() + timeout
        prior_end = None
        current_end = -1
        while prior_end != current_end:
            if time.time() > end_time:
                raise TimeoutException(f"Language spinner verification timed out after {timeout} seconds")
            displayed_locales = super().verify_language_menu_items()
            prior_end = current_end
            current_end = displayed_locales[-1]
            for loc in displayed_locales:
                if loc in expected_locales:
                    expected_locales.remove(loc)
            self.driver.swipe(swipe_object="language_menu_list")

        if len(expected_locales) > 0:
            raise ValueError("Missing languages: {}".format(", ".join([f"{lang}({locale})" for lang, locale in expected_locales.items()])))

    def verify_tooltip(self, timeout=10, invisible=False):
        """
        verify tooltip on Dynamic studio screen when we select the info button
        """
        self.driver.wait_for_object("ds_info_tooltip", timeout=timeout, invisible=invisible)

    def select_delete_page_icon_in_print_preview(self):
        """
        delete page from print preview screen
        """
        self.driver.click("delete_btn_copy")

    def select_done_btn(self):
        """
        done button from print preview screen
        """
        self.driver.click("done_btn")

    def capture_crop_image(self):
        """
        Capture image for Crop icon om DS screen.
        This function is main use for screen comparison before and after choose layout type to make sure choose successfully
        """
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("ds_layout_image"))

    def click_print_settings_more_btn(self):
        """
        Click on More Options button on Print Preview screen
        """
        self.driver.click("print_more_options")
     
class IOSPreview(Preview):
    platform = "ios"

    # Preview Page
    DELETE_PAGE_ICON = "delete_page_icon"

    # Bottom Navbar buttons for Preview Landing page (MAC)
    SHARE_BTN = "preview_share_btn"
    SAVE_BTN = "preview_save_btn"

    # Share and Save page
    SHARE_SAVE_TITLE = "share_save_title_str"
    FILE_NAME_TITLE = "file_name_title"
    FILE_SETTINGS_TITLE = "file_settings_title"
    FORMAT = "file_type"
    FILE_SIZE = "file_size"
    SHARE_SETTINGS_TIP = "share_settings_tip"
    SHARE_SAVE_BTN = "action_btn"
    IMAGE_PNG = "image_png"
    IMAGE_TIF = "image_tif"
    IMAGE_HEIF = "image_heif"
    LANGUAGE_OPTION = "language_option"
    CONTINUE_BUTTON = "continue_btn"

    # Share and Save page (MAC)
    SHARE_TITLE = "share_title"

    # Dynamic locators
    DYNAMIC_PREVIEW_BUTTON = "dynamic_button"
    DYNAMIC_TEXT = "dynamic_text"

    # print settings screen
    PRINT_SETTING_OPTIONS = "print_setting_options"
    PRINT_COPY = "print_copy_txt"

    # print settings Paper size options
    PAPER = "paper_txt"
    PAPER_SIZE_5x7 = "paper_size_5x7"
    PAPER_SIZE_4x6 = "paper_size_4x6"
    PAPER_SIZE_4x5 = "paper_size_4x5"
    PAPER_SIZE_4x12 = "paper_size_4x12"
    PAPER_SIZE_8x10 = "paper_size_8x10"
    PAPER_SIZE_LETTER = "paper_size_letter"
    PAPER_SIZE_A4 = "paper_size_a4"
    PAPER_SIZE_LEGAL = "paper_size_legal"

    # Print Setting Color Options
    COLOR_OPTION_TITLE_TEXT = "color_title_txt"
    BACK_ONLY_OPTION = "black_only_option_txt"
    GRAYSCALE_OPTION = "grayscale_option_txt"
    COLOR_OPTION = "color_option_txt"


    # Print Setting Print Quality Options
    PRINT_QUALITY = "print_quality_txt"
    PRINT_QUALITY_DRAFT_OPTION = "draft_option"
    PRINT_QUALITY_NORMAL_OPTION = "normal_option"
    PRINT_QUALITY_BEST_OPTION = "best_option"

    # Print Setting Page Range Options
    PAGE_RANGE = "page_range_txt"
    SELECT_ALL_OPTION = "select_all_txt"
    DESELECT_ALL_OPTION = "deselect_all_txt"
    MANUAL_INPUT_OPTION = "manual_input_txt"

    # Print Setting two sided Options
    TWO_SIDED = "two_sided_txt"
    TWO_SIDED_LONG_EDGE_OPTION = "2_sided_long_edge_option"
    TWO_SIDED_SHORT_EDGE_OPTION = "2_sided_short_edge_option"
    TWO_SIDED_OFF_OPTION = "2_sided_off_option"

    # Print Setting Orientation Options
    ORIENTATION_OPTION = "orientation_option"
    ORIENTATION_LANDSCAPE_OPTION = "orientation_landscape_option"
    ORIENTATION_PORTRAIT_OPTION = "orientation_portrait_option"

    PR_SCREEN_OPTIONS_UI = "page_range_options"
    COPIES_MINUS_BTN = "copies_minus_btn"
    COPIES_PLUS_BTN = "copies_plus_btn"
    RE_PRINT_BTN = "re_print_btn"
    YES_BTN = "yes_btn"
    NO_BTN = "no_btn"
    CANCEL_JOB_POP_UP_TITLE = "print_job_cancel_pop_up_title"
    CANCEL_JOB_POP_DES = "print_job_cancel_pop_up_txt"

    CANCEL_JOB_ELEMENTS = [
        CANCEL_JOB_POP_UP_TITLE,
        CANCEL_JOB_POP_DES,
        YES_BTN,
        NO_BTN
    ]
    
    # Transform screen
    TF_COLLECTION_VIEW = "transform_collection_view"
    TRANSFORM_RESIZE_BTN = "resize_and_move_btn_txt"
    CANCEL_BUTTON = "tf_cancel_btn"
    DONE_BUTTON = "tf_done_btn"

    PRINT_SETTINGS_UI_ELEMENTS = [
        PRINT_COPY,
        COPIES_MINUS_BTN,
        COPIES_PLUS_BTN,
        PAPER,
        COLOR_OPTION_TITLE_TEXT,
        PAGE_RANGE,
        PRINT_QUALITY,
        TWO_SIDED,
        Preview.PRINT_BTN
    ]

    PREVIEW_TOOLBAR_ICONS = [
        Preview.PRINT_BTN,
        SHARE_SAVE_TITLE,
        Preview.SHORTCUTS_BTN,
        Preview.FAX_BTN
    ]

    PREVIEW_BUTTON_NAMES = [
        Preview.PRINT_BTN,
        SHARE_SAVE_BTN,
        Preview.SHORTCUTS_BTN,
        Preview.FAX_BTN,
        Preview.ADD_BTN,
    ]

    PRINT_PREVIEW_UI_ELEMENTS = [
        Preview.BACK_BUTTON,
        Preview.PRINT_PREVIEW_TITLE,
        Preview.PREVIEW_IMAGE,
        Preview.PRINTER_NAME,
        Preview.PRINT_BTN
    ]

    PREVIEW_UI_ELEMENTS = [
        Preview.BACK_BUTTON,
        Preview.PREVIEW_TITLE,
        Preview.PREVIEW_IMAGE,
        SHARE_SAVE_TITLE,
        Preview.SHORTCUTS_BTN,
        Preview.REORDER_BTN
    ]

    TRANSFORM_SCREEN_UI_ELEMENTS = [
        TRANSFORM_RESIZE_BTN,
        Preview.TRANSFORM_ROTATE_BTN
    ]

    SHARE_PREVIEW_UI_ELEMENTS = [
        SHARE_SAVE_TITLE,
        Preview.BACK_BUTTON,
        Preview.FILE_NAME_FIELD,
        FILE_NAME_TITLE,
        FILE_SETTINGS_TITLE,
        FORMAT,
        FILE_SIZE,
        SHARE_SETTINGS_TIP,
        SHARE_SAVE_BTN
    ]

    def __init__(self, driver):
        super().__init__(driver)
        # iOS doesnt have str ids for languages so need to create maps manually
        self.LANGUAGE_MAP = {'en': 'English', 'en_US': 'English (US)', 'en_UK': 'English (UK)', 'ar': 'الشرق الأوسط', 'bg': 'Български', 
            'cs': 'Čeština', 'da': 'Dansk', 'de': 'Deutsch', 'el': 'Ελληνικά', 'es': 'Español', 'fi': 'Suomi', 'fr': 'Français', 
            'hr': 'Hrvatski', 'he': 'עברית', 'hu': 'Magyar', 'id': 'Indonesia', 'it': 'Italiano', 'ja': '日本語', 'ko': '한국어', 
            'no': 'Norsk', 'nl': 'Nederlands', 'pl': 'Polski', 'pt': 'Português', 'pt_BR': 'Português Brasileiro', 'ro': 'Română', 
            'ru': 'Русский', 'sk': 'Slovenčina', 'sl': 'Slovenščina', 'tr': 'Türkçe', 'zh_CN': '简体中文', 'zh_TW': '繁體中文', 
            'et': 'Eesti', 'ga': 'Gaeilge', 'lv': 'Latviešu', 'lt': 'Lietuvių k.', 'de_LU': 'Lëtzebuergesch', 'mt': 'Malti', 
            'mi': 'Māori', 'is': 'Íslenska', 'ca': 'català', 'sv': 'Svensk'}
        self.LOCALE_MAP = {lang: locale for locale, lang in self.LANGUAGE_MAP.items()}

    def verify_title(self, title, timeout=10, invisible=False, raise_e=True, use_str_id=True):
        if pytest.platform == "MAC":
            use_str_id = False
        self.dismiss_feedback_popup()
        if title == self.PRINT_PREVIEW_TITLE:
            while self.verify_print_preview_coachmark():
                if pytest.platform == "MAC":
                    self.focus_on_hpsmart_window_mac()
                else:
                    self.driver.click_by_coordinates(area='bl')
                    time.sleep(2)
        return super().verify_title(title=title, timeout=timeout, invisible=invisible, raise_e=raise_e, use_str_id=use_str_id)

    def verify_button(self, button_name, timeout=30, displayed=True):
        if pytest.platform == "MAC":
            return self.driver.wait_for_object(button_name)
        else:
            return self.driver.wait_for_object(self.DYNAMIC_PREVIEW_BUTTON, format_specifier=[self.get_text_from_str_id(button_name)], timeout=timeout, displayed=displayed, raise_e=False)

    def is_button_enabled(self, button_name):
        return self.driver.is_enable(self.DYNAMIC_PREVIEW_BUTTON, format_specifier=[self.get_text_from_str_id(button_name)])
    
    def select_button(self, button):
        """
        Click on a XCUIElementTypeButton on the page
        :param button: name attribute of the element
        :return:
        """
        if button not in self.PREVIEW_BUTTON_NAMES:
            raise InvalidElementNameException("Object: " + button + " not a valid button name")
        self.driver.scroll(button, timeout=15, click_obj=True)

    def select_done(self):
        self.driver.click(self.DONE_BUTTON)
        
    # ----------------------------------- Redaction/Text Extract Continue Screen - Action Methods ------------------------------------
    def select_continue(self):
        """
        Selects the continue button on the initial redaction screen.
        """
        self.driver.click("continue_btn")

    # ---------------------------------- Action(Share/Save/Convert to Text) Screen - Action Methods ----------------------------------
    def rename_file(self, file_name):
        """
        Sets the file name text
        """
        self.driver.click(self.FILE_NAME_FIELD)
        self.driver.click("clear_file_name_btn", raise_e=False)
        self.driver.send_keys(self.FILE_NAME_FIELD, file_name, press_enter=True if pytest.platform == "IOS" else False)
    
    def select_file_types_dropdown(self):
        self.driver.click("file_type_dropdown")

    def select_navigate_back_on_file_type_screen(self):
        self.driver.click("file_type_back_arrow")
    
    def select_file_type(self, file_type=None):
        """
        Selects the specified file type. If file_type is None only opens the file type menu.
        :param file_type: The file type to select.
        """
        self.dismiss_file_types_coachmark(timeout=3)
        if not self.driver.wait_for_object("file_type_menu_title", raise_e=False):
            self.driver.click("file_type_dropdown")
        if file_type:
            self.driver.click(file_type)
            self.select_navigate_back_on_file_type_screen()
            return True

    def toggle_share_as_original_btn(self, uncheck=False):
        self.driver.check_box("share_as_original_toggle_btn", uncheck=uncheck)

    def verify_language_selected(self, language="default language", raise_e=True):
        obj = self.driver.wait_for_object("dynamic_text", format_specifier=[language], timeout=5)
        return self.driver.wait_for_object("blue_checkmark", invisible=True, root_obj=obj, raise_e=raise_e)
    
    def verify_file_type_selected(self, option, raise_e=False):
        return self.driver.wait_for_object(self.FORMAT, format_specifier=[option], raise_e=raise_e)
    
    def verify_file_saved_pop_up(self, raise_e=True):
        time.sleep(1)
        return self.driver.wait_for_object("file_saved_popup_title", timeout=20, raise_e=raise_e)
    
    def dismiss_file_saved_popup(self):
        """
        Dismiss the "Your file has been saved!" popup
        """
        self.driver.click("file_saved_popup_ok_btn")

    def click_go_to_home_button(self):
        """
        Dismiss the "Your file has been saved!" popup by clicking on "Go to Home" button
        """
        self.driver.click("go_home_btn")
    
    def dismiss_file_types_coachmark(self, timeout=10):
        """
        Dismisses the "New file types available..." popup
        """
        if self.driver.wait_for_object("new_file_types_coachmark", timeout=timeout, displayed=False, raise_e=False):
            self.driver.click_by_coordinates(area='bl')

    def select_preview_pan_view(self, open=True):
        if open:
            self.driver.wdvr.execute_script("mobile: swipe", {"direction": "up", "element": self.driver.wait_for_object("print_preview_pan_view")})
        else:
            self.driver.wdvr.execute_script("mobile: swipe", {"direction": "down", "element": self.driver.wait_for_object("print_preview_pan_view")})

    def select_cancel(self, timeout=10):
        self.driver.click(self.CANCEL_BUTTON, timeout=timeout)

    def verify_pages_selected(self, page_no):
        return self.driver.wait_for_object("page_selected_image", format_specifier=[page_no], raise_e=False)
    
    def verify_print_preview_coachmark(self, raise_e=False):
        return self.driver.wait_for_object("print_preview_coachmark", displayed=False, raise_e=raise_e)
    
    def dismiss_print_preview_coachmark(self):
        if self.verify_print_preview_coachmark():
            self.driver.click_by_coordinates(area='bl')
            time.sleep(2)
    
    def verify_printer_name_displayed(self, printer_name, timeout=25, displayed=False, delay=0):
        time.sleep(delay)
        if displayed_printer_name := self.driver.get_attribute(self.PRINTER_NAME, "label", timeout=timeout, displayed=displayed, raise_e=False):
            return displayed_printer_name in printer_name
        return False
    
    def select_no_thanks_btn(self):
        self.driver.click("feedback_no_thanks_btn")

    def dismiss_feedback_popup(self, timeout=5):
        if self.driver.wait_for_object("feedback_popup_title", timeout=timeout, raise_e=False):
            self.select_no_thanks_btn()

    def select_transform_options(self, tf_option1, tf_option_select=None, use_str_id=False):
        self.driver.click(tf_option1)
        if tf_option1 == self.PREVIEW_IMAGE:
            self.verify_title(self.TRANSFORM_TITLE, use_str_id=False)
        elif tf_option1 == self.TRANSFORM_ROTATE_BTN:
            self.verify_title(tf_option1)
        else:
            self.verify_title(tf_option1, invisible=True, use_str_id=False)
        if tf_option_select is not None:
            self.driver.click(self.DYNAMIC_TEXT, format_specifier=[tf_option_select])
        
    def verify_re_print_btn(self, timeout=60):
        timeout = time.time() + timeout
        while time.time() < timeout:
            self.dismiss_feedback_popup()
            if self.driver.wait_for_object(self.RE_PRINT_BTN, raise_e=False):
                logging.info("Re-Print button displayed")
                break
            else:
                time.sleep(5)
        return self.driver.wait_for_object(self.RE_PRINT_BTN, timeout=3)
    
    def verify_printing_status_btn_changes(self, multi_print=False, timeout=60):
        if multi_print:
            self.driver.wait_for_object("multi_page_printing_txt", timeout=timeout)
        else:
            self.driver.wait_for_object("printing_btn_txt", raise_e=False)
        self.driver.wait_for_object("printing_msg_txt", raise_e=False)
        self.driver.wait_for_object(self.CANCEL_BUTTON, raise_e=False)
        self.driver.wait_for_object("print_job_sent_btn", raise_e=False, timeout=timeout)
    
    # Print job completion varies on printer and hence need extended timeout to validate
    def verify_job_sent_and_reprint_buttons_on_print_preview(self, timeout=60):
        self.dismiss_feedback_popup()
        self.driver.wait_for_object("printing_btn_txt", raise_e=False)
        self.driver.wait_for_object("print_job_sent_btn", raise_e=False)
        self.verify_re_print_btn(timeout=timeout)

    def go_to_print_preview_pan_view(self, print_size=Preview.DOCUMENT_SIZE_8x11, pan_view=True):
        self.dismiss_feedback_popup()
        self.select_print_size(btn=print_size, raise_e=False) # find size which is letter by default on ios
        self.verify_title(self.PREVIEW_TITLE)
        self.select_bottom_nav_btn(self.PRINT_PREVIEW_BTN)
        self.verify_title(self.PRINT_PREVIEW_TITLE)
        if pan_view:
            self.select_print_preview_pan_option_screen()

    def select_print_preview_pan_option_screen(self):
        """
        Swipe Print Preview option screen
        """
        if pytest.platform == "IOS":
            self.driver.swipe("print_preview_pan_view", per_offset=0.35)
        else:
            self.driver.click_using_frame("print_preview_pan_view")
    
    # Page range screen
    def verify_print_preview_ui_elements(self, printer_name):
        self.dismiss_print_preview_coachmark()
        for element in self.PRINT_PREVIEW_UI_ELEMENTS:
            if element == self.PRINTER_NAME:
                option_displayed = printer_name[:15] in self.driver.get_attribute(element, "label")
            else:
                option_displayed = self.driver.wait_for_object(element, timeout=20, raise_e=False)
            if not option_displayed:
                raise Exception(element + " - not displayed/not applicable")
    
    # Reorder screen
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
    
    def verify_delete_page_x_icon(self):
        """
        :return: True if x button is present else False
        """
        return self.driver.find_object(self.DELETE_PAGE_ICON, multiple=True, raise_e=False)
    
    def select_delete_page_icon(self):
        self.driver.click(self.DELETE_PAGE_ICON)
    
    def verify_delete_button(self):
        self.driver.click(self.DELETE_PAGE_ICON)
        delete_button = self.driver.wait_for_object("delete_btn", raise_e=False)
        self.driver.click_by_coordinates(area="bl")
        return delete_button
    
    def select_delete_pages_in_current_job(self, no_of_pages_to_delete=2):
        """
        Click on "X" icon on Preview screen
        End of flow: Scan screen
        Device: Phone
        """
        try:
            for page in range(no_of_pages_to_delete):
                self.driver.click(self.DELETE_PAGE_ICON)
                self.driver.click("delete_btn")
                if self.driver.wait_for_object("delete_popup_msg", timeout=3, raise_e=False):
                    self.driver.click("delete_btn")
        except TimeoutException:
            logging.info("we don't have {} many pages to delete on preview screen:".format(no_of_pages_to_delete))

    def verify_default_option_selected(self, option_name):
        return self.driver.wait_for_object("option_selected_image", format_specifier=[option_name], invisible=True, raise_e=False)

    def select_add_page(self):
        """
        Click on Add Page icon button on Preview screen
        """
        self.driver.click(self.ADD_BTN, timeout=15)
    
    def select_exit_popup_home_btn(self, timeout=10, raise_e=True):
        self.driver.click("exit_popup_home_btn", timeout=timeout, raise_e=raise_e)
    
    def go_home_from_preview_screen(self):
        """
        Go back to home from preview screen
        """
        self.dismiss_feedback_popup()
        self.driver.click("back_arrow_btn")
        self.verify_exit_popup()
        self.select_exit_popup_home_btn()

    def verify_no_printer_on_printer_preview_screen(self):
        """
        Verify Choose your Printer item displays on Print Preview screen when no printer is selected
        """
        self.driver.wait_for_object("choose_your_printer_option")

    def select_choose_your_printer(self):
        """
        Click on "Choose your printer" option from Print review screen
        """
        self.driver.click("choose_your_printer_option")

    def verify_paper_screen(self):
        """
        Verify currently screen is Paper screen
        - Title
        - Paper ready to use section
        - Additional Paper Options section
        """
        self.driver.wait_for_object(self.PAPER, timeout=15)
        self.driver.wait_for_object("paper_ready_to_use_txt")
        self.driver.wait_for_object("additional_paper_options_txt")
    
    def verify_preview_screen(self):
        """
        Verifies the preview landing page
        """
        self.dismiss_feedback_popup()
        self.verify_title(self.PREVIEW_TITLE, timeout=30)
        return self.driver.wait_for_object("bottom_navbar")
    
    def select_edit(self, change_check=None):
        """
        Click on Edit button
        """
        self.dismiss_feedback_popup()
        if self.driver.wait_for_object(self.EDIT_BTN, raise_e=False):
            self.driver.click(self.EDIT_BTN)
        else:
            self.select_preview_image(change_check=change_check)
    
    def select_save_to_hp_smart_btn(self):
        self.driver.click("save_hp_smart_btn", timeout=25)
    
    def verify_id_card_front_screen(self, timeout=10):
        self.driver.wait_for_object("id_card_front", timeout=timeout)
    
    def verify_rotate_right_icon(self, timeout=10):
        return self.driver.wait_for_object("rotate_right_icon", timeout=timeout)

    def select_rotate_right_icon(self, timeout=10):
        self.driver.click("rotate_right_icon", timeout=timeout)
    
    def verify_id_card_back_screen(self, timeout=10):
        self.driver.wait_for_object("id_card_back", timeout=timeout)
    
    def verify_rotate_upsidedown_icon(self, timeout=10):
        return self.driver.wait_for_object("rotate_upsidedown_icon", timeout=timeout)
    
    def select_rotate_upsidedown_icon(self, timeout=10):
        self.driver.click("rotate_upsidedown_icon", timeout=timeout)
    
    def verify_zoomed_mode(self):
        self.driver.wait_for_object("zoomed_mode")
    
    def verify_toolbar_icons(self):
        """
        verifies the icons at the bottom of the preview screen:
            Print
            Share/Save
            Smart Tasks
            Fax
        """
        for icon in self.PREVIEW_TOOLBAR_ICONS:
            self.driver.wait_for_object(icon)
    
    def select_auto_rotate_delete_btn(self):
        self.driver.click("delete_btn")
    
    def verify_rotate_screen_tray_options(self):
        """
        Verifies the rotate screen tray options in the bottom when multiple images
        are added and at least one of them is selected (delete button won't be displayed if only one image is added)
        """
        self.driver.wait_for_object("delete_btn")
        self.verify_rotate_btn()
    
    def reorder_image(self, to_move, destination):
        """
        Moves an image to the specified index
        :param to_move: The image index, indexed at 1
        :param destination: The index to move the image to, indexed at 1
        """
        self.driver.drag_and_drop(self.driver.wait_for_object("reorder_img", format_specifier=[to_move]), self.driver.wait_for_object("reorder_img", format_specifier=[destination]))
    
    def verify_elements_on_print_preview_slider(self):
        for element in self.PRINT_SETTINGS_UI_ELEMENTS:
            self.driver.wait_for_object(element)
    
    # ------------------------------------------ Dynamic Studio Screen - Action Methods -------------------------------------------
    def select_printer_title(self, printer_name):
        self.driver.click("printer_object_title", format_specifier=[printer_name])

    def click_right_arrow_btn(self):
        """
        CLick on right arrow btn on the screen if we have multiple images selected
        """
        self.driver.click("right_arrow_btn")

    def verify_left_arrow_btn(self):
        """
        Verify the left arrow btn on the screen if we have multiple images selected
        """
        self.driver.wait_for_object("left_arrow_btn", displayed=False)

    def verify_right_arrow_btn(self):
        """
        Verify the right arrow btn on the screen if we have multiple images selected
        """
        self.driver.wait_for_object("right_arrow_btn", displayed=False)

    # ------------------------------------------ Print Preview Section -------------------------------------------
    def get_page_range(self, displayed=False):
        """
        Get page range value on Print Preview screen
        """
        page_range = self.driver.get_attribute("page_range_displayed_txt", "name", displayed=displayed)
        return page_range.encode("ascii", "ignore").decode()

    def select_or_unselect_pages(self, page_no):
        """
        Select or unselect the page on Page Range screen
        :param page_no:
        """
        for page in page_no:
            self.driver.click("page_no_txt", format_specifier=[page])

    def check_manual_input_pop_up_msg(self, input_page_range=False):
        if self.driver.wait_for_object("in_app_alert", raise_e=False):
            if input_page_range:
                return self.driver.wait_for_object("manual_input_pop_up_msg", raise_e=False)
            else:
                return self.driver.wait_for_object("manual_input_pop_up_warning_msg", raise_e=False)
        else:
            return False

    def change_print_copies(self, copies_btn, no_of_copies=1):
        for _ in range(no_of_copies):
            self.driver.click(copies_btn)

    def get_copies_btn_enabled_status(self, copies_btn):
        return self.driver.get_attribute(copies_btn, "enabled")

    def get_no_of_copies(self):
        if self.driver.wait_for_object("print_multiple_copies_txt", raise_e=False):
            copies_label = self.driver.get_attribute("print_multiple_copies_txt", attribute="label")
            copies_label = copies_label.split()
            count = list(copies_label[1])
            copies_count = int(count[1])
        else:
            copies_count = 1
        return copies_count

    def enter_page_range(self, page_nos):
        """
        Enter page range number on Manual Input screen
        """
        self.driver.click("clear_text_btn", raise_e=False)
        self.driver.send_keys("page_range_input_txt_field", page_nos)

    def select_paper_size_dropdown(self):
        """
        Click on Paper Size dropdown button on Print Preview screen
        """
        self.driver.scroll("paper_txt", click_obj=True)

    def verify_paper_size_option(self, paper_size_option, invisible=False, raise_e=True):
        """
       Verify the paper size options on the paper size list screen
        """
        if pytest.platform == "MAC":
            return self.driver.wait_for_object(paper_size_option, invisible=invisible, raise_e=raise_e)
        else:
            return self.driver.wait_for_object("visible_dynamic_text", format_specifier=[self.driver.return_str_id_value(paper_size_option)], invisible=invisible, raise_e=raise_e)

    def select_paper_size_option(self, paper_size_option):
        """
        Click on Paper Size dropdown button on Print Preview screen, and select different options from the list.
        """
        if pytest.platform == "MAC":
            self.driver.click(paper_size_option)
        else:
            self.driver.click("visible_dynamic_text", format_specifier=[self.driver.return_str_id_value(paper_size_option)])

    def select_color_mode_option(self, color_option):
        """
        Click on Color Options button, and select different color option from the list
        """
        self.driver.scroll("color_title_txt", click_obj=True)
        self.driver.click("visible_dynamic_text", format_specifier=[self.driver.return_str_id_value(color_option)])

    def get_color_selected_value(self):
        """
        Get the Color option value
        """
        return self.driver.get_attribute("color_option_value", "name")

    def select_orientation_option(self, orientation_option):
        """
        Click on Orientation button, and select different options
        """
        self.driver.scroll("orientation_option", click_obj=True)
        self.driver.click("visible_dynamic_text", format_specifier=[self.driver.return_str_id_value(orientation_option)])

    def verify_2_sided_option(self, invisible=False, raise_e=True):
        """
        verify 2 Sided item on the Print Preview screen
        """
        self.driver.scroll("table_value", direction="down", click_obj=False, check_end=True)
        return self.driver.wait_for_object("two_sided_txt", invisible=invisible, raise_e=raise_e)

    def select_2_sided_option(self, duplex_option):
        """
        Click on 2 Sided dropdown button, and select duplex option
        """
        self.driver.scroll("two_sided_txt", click_obj=True)
        self.driver.click("visible_dynamic_text", format_specifier=[self.driver.return_str_id_value(duplex_option)])

    def get_2_sided_selected_value(self):
        """
        Get the 2 Sided option value
        """
        return self.driver.get_attribute("2_sided_option_value", "name")

    def select_print_quality_option(self, print_quality_option):
        """
        Click on Print Quality dropdown button on Print Preview screen, and select different options from the list.
        """
        self.driver.scroll("print_quality_txt", click_obj=True)
        self.driver.click("visible_dynamic_text", format_specifier=[self.driver.return_str_id_value(print_quality_option)])

    def get_print_quality_selected_value(self):
        """
        Get the Print Quality option value
        """
        return self.driver.get_attribute("print_quality_option_value", "name")

    def select_page_range_option(self):
        """
        Click on Page Range button from Print Preview screen
        """
        self.driver.scroll("page_range_txt", click_obj=True)

    def get_page_range_selected_value(self):
        """
        Get the Page Range value from Print Preview screen
        """
        return self.driver.get_attribute("page_range_option_value", "name")

    def select_select_all_btn(self):
        """
        Click on Select All button on Page Range screen
        """
        self.driver.click("select_all_txt")

    def select_deselect_all_btn(self):
        """
        Click on Deselect All button on Page Range screen
        """
        self.driver.click("deselect_all_txt")

    def select_manual_input_btn(self):
        """
        Click on Manual Input button on Page Range screen
        """
        self.driver.click("manual_input_txt")

    def verify_page_range_screen(self):
        """
        Verify Page Range screen
        """
        self.driver.wait_for_object("page_range_txt")
        self.driver.wait_for_object("select_all_txt")
        self.driver.wait_for_object("deselect_all_txt")

    def select_print_preview_share_btn(self):
        """
        Click on Share button from Print Preview screen
        """
        self.driver.click("print_preview_share_btn")

    # ------------------------------------------ Transform Section -------------------------------------------

    def verify_transform_screen(self):
        """
        Verify currently screen is transform screen
        - Title
        - Cancel button
        - Done button
        """
        self.driver.wait_for_object(self.TRANSFORM_TITLE)
        self.driver.wait_for_object(self.CANCEL_BUTTON)
        self.driver.wait_for_object(self.DONE_BUTTON)

    def verify_resize_move_screen(self):
        """
        Verify currently screen is Resize and Move screen
        - Title
        - Cancel button
        - Done button
        """
        self.driver.wait_for_object(self.TRANSFORM_RESIZE_BTN)
        self.driver.wait_for_object(self.CANCEL_BUTTON)
        self.driver.wait_for_object(self.DONE_BUTTON)

    def verify_rotate_screen(self):
        """
        Verify currently screen is Rotate screen
        - Title
        - Cancel button
        - Done button
        """
        self.driver.wait_for_object("rotate_image_btn")
        self.driver.wait_for_object(self.CANCEL_BUTTON)
        self.driver.wait_for_object(self.DONE_BUTTON)

    def select_resize_move_btn(self):
        """
        Click on Resize & Move button on Transform screen
        """
        self.driver.click(self.TRANSFORM_RESIZE_BTN)

    def select_resize_move_manual_option(self):
        """
        Click on Manual button on Resize & Move screen
        """
        self.driver.click("resize_and_move_manual_option")

    def select_resize_move_original_size_option(self):
        """
       Click on Origin Size button on Resize & Move screen
        """
        self.driver.click("resize_and_move_original_size_option")

    def select_resize_move_fit_to_page_option(self):
        """
        Click on Fit to Page button on Resize & Move screen
        """
        self.driver.click("resize_and_move_fit_to_page_option")

    def select_resize_move_fill_page_option(self):
        """
        Click on Fill Page button on Resize & Move screen
        """
        self.driver.click("resize_and_move_fill_page_option")

    def manual_resize_image(self, direction="left", per_offset=0.55):
        """
        User can resize the image by direction manually
        """
        self.driver.swipe("preview_img", direction=direction, per_offset=per_offset)

    def select_rotate_left_option(self):
        """
        Click on Left option on Rotate screen
        """
        self.driver.click("rotate_left_option")

    def select_rotate_right_option(self):
        """
        Click on Right option on Rotate screen
        """
        self.driver.click("rotate_right_option")

    def select_rotate_flip_h_option(self):
        """
        Click on Flip H option on Rotate screen
        """
        self.driver.click("rotate_flip_h_option")

    def select_rotate_flip_v_option(self):
        """
        Click on Flip V option on Rotate screen
        """
        self.driver.click("rotate_flip_v_option")

    # ------------------------------------------ Shortcuts Section -------------------------------------------
    def select_activity_center_button_on_popup(self, timeout=30):
        """
        Click on Activity Center button on the "Your File is processing"
        popup after starting a shortcut
        """
        self.driver.click("go_to_activity_center_btn", timeout=timeout)
    
    def expand_shortcuts_pan_view_btn(self):
        self.driver.click("shortcuts_pan_view_expand_btn")
    
    def select_finish_shortcut_btn(self):
        self.driver.click("finish_shortcut_btn")

    def verify_file_type_option_in_file_type_screen(self, option):
        """
        verify File type option on file type screen
        """
        return self.driver.wait_for_object("selected_file_type_option", format_specifier=[option], timeout=10)

    def select_file_type_option_in_file_type_screen(self, option="image_jpg"):
        """
        verify File type option on file type screen
        """
        self.driver.click(option)

    def verify_rotate_options_on_print_screen(self):
        """
        verify Rotate screen
        """
        self.driver.wait_for_object("rotate_left_option")
        self.driver.wait_for_object("rotate_right_option")
        self.driver.wait_for_object("rotate_flip_h_option")
        self.driver.wait_for_object("rotate_flip_v_option")