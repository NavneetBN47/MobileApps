import logging
import pytest
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from SAF.misc import saf_misc

class Scan(SmartFlow):
    flow_name = "scan"

    PAGE_SIZE = "page_size"
    PAPER_SIZE_TABLE_VIEW = "area_size_options"
    PAPER_SIZES = ["_const_paper_size_a4_option", "_const_paper_size_4x6_option", "_const_paper_size_5x7_option",
                   "_const_paper_size_3_5x5_option", "_const_paper_size_letter_option"]

    INPUT_SOURCE = "input_source"
    QUALITY = "quality"
    COLOR = "color"

    ADJUST_SCAN_COACH_MARK = "adjust_scan_coach_mark"
    ADJUST_SCAN_CAPTURE_COACH_MARK = "adjust_scan_capture_coachmark"
    START_SCAN_COACHMARK = "start_scan_coachmark"
    SCAN_SOURCE_COACHMARK = "scan_source_coachmark"

    AUTO_ENHANCEMENT = "auto_enhancements"
    AUTO_ORIENTATION = "auto_orientation"
    AUTO_ENHANCEMENT_SWITCH = "auto_enhancements_switch"
    AUTO_ORIENTATION_SWITCH = "auto_orientation_switch"
    AUTO_HEAL_SWITCH = "auto_heal"
    FLATTEN_PAGES_SWITCH = "flatten_pages"

    AUTOMATIC_INPUT = "_const_input_src_automatic_btn"
    SCANNER_GLASS = "_const_input_src_scanner_glass_btn"
    DOCUMENT_FEEDER = "_const_input_src_doc_feeder_btn"
    DOCUMENT_FEEDER_2_SIDED = "_const_input_src_doc_feeder_2_sided_btn"

    SCAN_COACH_MARKS = [
        ADJUST_SCAN_CAPTURE_COACH_MARK,
        START_SCAN_COACHMARK,
        SCAN_SOURCE_COACHMARK
    ]

    SCAN_SETTINGS = [
        PAGE_SIZE,
        QUALITY,
        COLOR,
        INPUT_SOURCE
    ]

    INPUT_SOURCES = [
        AUTOMATIC_INPUT,
        SCANNER_GLASS,
        DOCUMENT_FEEDER
    ]
    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Action Flows                                                        #
    #                                                                                                                      #
    ########################################################################################################################

    def select_scanner_if_first_time_popup_visible(self):
        """
        :return:
        """
        try:
            self.driver.wait_for_object("scanner_popup_btn")
            self.driver.click("scanner_popup_btn")
        except TimeoutException:
            logging.info("Current Screen did NOT contain the first time scanner or camera popup")

    def select_scan_settings_wheel(self):
        """
        Click on Scan Settings

        End of flow: Scan Settings screen

        Device: Phone
        """
        self.driver.click("setting_btn", timeout=30)

    def select_page_size_menu(self):
        self.driver.click(self.PAGE_SIZE)
    
    def select_scan_size(self, size="letter"):
        self.driver.click(f"_const_paper_size_{size}_option")
    
    def select_input_source(self, raise_e=False):
        if raise_e:
            self.driver.click(self.INPUT_SOURCE)
        else:
            if not self.driver.click(self.INPUT_SOURCE, raise_e=False):
                pytest.skip("Input source not available for this printer")
    
    def select_input_source_option(self, option):
        self.driver.click(option)
    
    def select_scan_settings_by_type_and_value(self, settings_option_type, settings_option_value=""):
        """
        Select scan settings by setting option and the item of that option

        End of flow: Scan screen

        Device: Phone
        """
        try:
            self.driver.click(settings_option_type)
            if settings_option_type == self.SCAN_SETTINGS.INPUT_SOURCE:
                self.driver.wait_for_object("input_src_title")
            if settings_option_type == self.SCAN_SETTINGS.QUALITY:
                self.driver.wait_for_object("quality_title")
            if settings_option_type == self.SCAN_SETTINGS.COLOR:
                self.driver.wait_for_object("color_title")
            self.driver.click(settings_option_value)
            self.select_navigate_back()
            self.verify_scan_settings_screen()
        except (NoSuchElementException, TimeoutException):
            logging.info("This settings_option is not exists !!" + settings_option_type)

    def get_area_size(self):
        """
       Get scan area size on Scan screen

       Device: Phone
       """
        area_size = self.driver.get_attribute("area_size", "text")
        if area_size == 'Letter - 8.5x11 in':
            area_size = '215.9x279.4mm'
        return str(area_size)

    def select_scan_job_button(self, verify_messages=True, change_check={"wait_obj": "cancel_scan_btn"}, scan_timeout=20):
        """
        Click Scan button on Scan screen
        Device: Phone
        """
        if self.verify_second_close_btn():
            self.select_second_close_btn()
        sleep(1)
        self.driver.click("scan_btn", change_check=change_check, timeout=scan_timeout)
        if verify_messages:
            if not self.driver.wait_for_object("scanning_finished_msg", timeout=scan_timeout, interval=0.2, raise_e=False) and not self.driver.wait_for_object("adjust_boundaries_title", raise_e=False):
                raise TimeoutException(f"Still scanning after timeout of {scan_timeout}")

    def select_cancel_scanning_job(self):
        """
        Click Scan button on Scan screen to cancel scanning
        Device: Phone
        """
        self.driver.click("cancel_scan_btn")

    def select_preview_on_scanner_screen(self):
        """
        Click on Preview button on Scan screen

        End of flow: Scan screen

        Device: Phone
        """
        self.driver.click("preview_btn")

    def select_source_button(self):
        """
        :return:
        """
        self.driver.click("source_btn")

    def get_number_of_available_sources(self):
        """
        Returns the numbers of available sources to choose from on the sources popover
        """
        return len(self.driver.find_object("source_btn_options", multiple=True))
    
    def select_no_button_to_scanner_screen(self):
        """
        Click on No button on navigate back popup, to return for scanner screen or camera screen
        """
        self.driver.click("add_page_no_btn")

    def select_camera_if_first_time_popup_visible(self):
        """

        :return:
        """

        try:
            self.driver.wait_for_object("camera_popup_btn")
            self.driver.click("camera_popup_btn")
        except TimeoutException:
            logging.warning("Current Screen did NOT contain the scanner or camera popup")

    def customize_scan_using_elements(self, source, destination="scanner_screen_message"):
        """
        Customize scan with source and destination
        :param source: Knob of the selection border to drag
        :param destination: The desired destination object to drag the knob to
                            By Default it is the center of the message in the middle of the screen
        """
        self.driver.drag_and_drop(self.driver.wait_for_object(source), self.driver.wait_for_object(destination))
    
    def screenshot_img_inside_selection_border(self):
        self.driver.wait_for_object("selection_border")
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("selection_border"))
    
    ########################################################################################################################
    #                                                                                                                      #
    #                                             Verification Flows                                                       #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_scanner_screen(self, raise_e=True):
        """
        verifies the scan screen after selection in scanner or camera first time dialog popup:
        :return:
        """
        if self.driver.wait_for_object("preview_btn", timeout=90, raise_e=raise_e) == False:
            return False
        return True

    def verify_document_feeder_empty_message(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("document_feeder_empty_message", timeout=timeout, raise_e=raise_e)
    
    def verify_scan_settings_screen(self):
        """
        Verify Scan Settings Navigation bar:
            - Done button (phone only)
            - Scan Settings title

        Note: for tablet, there are 2 texts for "Scan Settings"

        Device: phone and tablet
        """
        self.driver.wait_for_object("scan_settings_title", timeout=30)

    def verify_scanning_screen(self):
        """
         verifies the scanning screen undergoing by using the same scan button(in red color):
        :return:
        """
        self.driver.wait_for_object("cancel_scan_btn")

    def verify_scan_not_available(self):
        """
        Verify if the Scan feature is available
        :return:
        """
        return self.driver.wait_for_object("scan_not_available", raise_e=False, timeout=5)

    def verify_scanner_or_camera_popup_displayed(self, popup=True):
        """
        Verify Scanner and Camera options pop-up displayed or not

        Device: Phone
        """

        popup_displayed = self.driver.wait_for_object("scan_images_or_slash_documents_popup_msg", timeout=10,
                                                      raise_e=False)
        if popup_displayed == popup:
            return True
        else:
            return False

    def verify_x_button_on_scan_screen(self):
        """
        :return:
        """
        self.driver.wait_for_object("close_btn")

    def verify_area_size_field(self):
        """
        :return:
        """
        self.driver.wait_for_object("area_size")

    def verify_area_size_options(self):
        """
        :return:
        """
        self.driver.wait_for_object("area_size_options")

    def verify_down_arrow_icon(self):
        """
        :return:
        """
        self.driver.wait_for_object("down_arrow_icon")

    def verify_scan_setting_wheel(self):
        """
        :return:
        """
        self.driver.wait_for_object("setting_btn")

    def verify_preview_button_on_scan_screen(self, raise_e=True):
        """
        :return:
        """
        return self.driver.wait_for_object("preview_btn", timeout=10, raise_e=raise_e)

    def verify_preview_not_supported_message(self):
        return self.driver.wait_for_object("preview_not_supported_message")
    
    def verify_batch_scan_message(self, raise_e=True):
        return self.driver.wait_for_object("batch_message_after_scan", raise_e=raise_e)
    
    def verify_scan_button(self):
        """
        :return:
        """
        self.driver.wait_for_object("scan_btn", timeout=30)

    def verify_source_button(self):
        self.driver.wait_for_object("source_btn")

    def select_files_photos_option(self):
        self.driver.click("files_and_photos_btn")

    def select_camera_option(self):
        self.driver.click("camera_btn")

    def change_scan_settings_and_save(self, settings_option_type, settings_option_value):
        self.select_scan_settings_wheel()
        self.verify_scan_settings_screen()
        self.driver.click(settings_option_type)
        self.driver.click(settings_option_value)
        self.select_navigate_back()
        self.verify_scan_settings_screen()
        self.select_done()

    def verify_scan_source_btn(self, printer_name, timeout=10, raise_e=True):
        printer_name = self.format_printer_name_for_scanner_source(printer_name)
        return self.driver.wait_for_object("scanner_btn", timeout=timeout, format_specifier=[printer_name], raise_e=raise_e)

    def verify_source_all_options(self, printer_name):
        """
        :return:
        """
        printer_name = self.format_printer_name_for_scanner_source(printer_name)
        self.driver.wait_for_object("files_and_photos_btn")
        self.driver.wait_for_object("scanner_btn", format_specifier=[printer_name])
        self.driver.wait_for_object("camera_btn")

    def verify_source_options_for_printer_without_scanner(self):
        """
        verify only camera and files and photos are available as sources
        """
        self.driver.wait_for_object("files_and_photos_btn")
        self.driver.wait_for_object("camera_btn")

    def verify_input_source_options(self):
        for source in self.INPUT_SOURCES:
            if source == self.DOCUMENT_FEEDER:
                if not self.driver.wait_for_object(source, raise_e=False):
                    pytest.skip("Document feeder not available for this printer")
            else:
                self.driver.wait_for_object(source)
    
    def verify_scan_settings_type_and_options(self, scan_setting_type, scan_setting_options, raise_e=False):
        """
            scan_setting_type: Scan settings ex: Input Type, Quality
            scan_setting_options: option in each Scan Settings ex: Input Type contains JPG, PDF
            Select scan_setting_type and verify options listed
         """
        if self.driver.wait_for_object(scan_setting_type, raise_e=raise_e):
            self.driver.click(scan_setting_type)
            options = [a for a in dir(scan_setting_options) if not a.startswith("__")]
            for option in options:
                if self.driver.wait_for_object(getattr(scan_setting_options, option), raise_e=raise_e):
                    logging.warning(scan_setting_type + " option " + option + "not found/not applicable to connected "
                                                                              "printer")
            self.select_navigate_back()
        else:
            logging.warning(scan_setting_type + " Not applicable/displayed for the connected printer")

    def verify_navigate_back_popup(self):
        """
        this popup will return to home screen or scanner screen
        """
        self.driver.wait_for_object("navigate_bck_popup")

    def verify_top_left_knob_on_scan_screen(self):
        """
         verifies the top left knob
        :return:
        """
        self.driver.wait_for_object("top_left_knob")

    def verify_page_size_options(self):
        for option in self.PAPER_SIZES:
            self.driver.wait_for_object(option)
    
    def verify_document_feeder_scan(self):
        if not self.verify_document_feeder_empty_message(timeout=3, raise_e=False) and not self.driver.wait_for_object("adjust_boundaries_title", raise_e=False):
            raise TimeoutException("Document feeder scan not started")
    
    ########################################################################################################################
    #                                                                                                                      #
    #                               //  SCAN //                                                                            #
    #                                                                                                                      #
    ########################################################################################################################

    def select_scan_job_with_cancel_for_ga(self):

        self.select_scan_job_button(verify_messages=False)
        self.verify_scanning_screen()
        self.select_cancel_scanning_job()
        self.verify_scanner_screen()

    def select_scan_job(self):
        self.select_scan_job_button(verify_messages=False)
        self.verify_scanning_screen()

    def verify_scan_screen_ui_elements(self):
        """
        :return:
        """
        self.verify_x_button_on_scan_screen()
        self.verify_area_size_field()
        self.verify_scan_setting_wheel()
        self.verify_preview_button_on_scan_screen()
        self.verify_scan_button()
        self.verify_source_button()

    def verify_scanning_messages(self, timeout=10, raise_e=False):
        """
         Verify messages displayed while scanning a job
        :return:
        """
        if not self.driver.wait_for_object("scanning_msg", raise_e=raise_e):
            logging.info("Scanning.. msg not displayed")
        if not self.driver.wait_for_object("scanning_finished_msg", timeout=timeout, raise_e=raise_e):
            logging.info("Scanning Finished msg not displayed")

    def verify_scan_canceling_msg(self):
        if self.driver.wait_for_object("scanning_canceling_msg", raise_e=False):
            logging.info("Scanning canceled & canceling.. msg displayed")

    def verify_scan_coach_mark_pop_up(self, raise_e=False):
        return self.driver.wait_for_object("scan_coach_mark_pop_up", raise_e=raise_e)

    def verify_coachmark_on_scan_page(self, coachmark_no, raise_e=False):
        """        
        ADJUST_SCAN_COACH_MARK
        SCAN_COACH_MARK_1,
        SCAN_COACH_MARK_2
        """
        return self.driver.wait_for_object(coachmark_no, raise_e=raise_e)

    def select_next_on_coachmark(self):
        self.driver.click("next_btn")

    def click_close_button_on_scan_screen(self):
        """
        click close button on scan screen:
        """
        self.driver.click("close_btn")

class MacScan(Scan):
    #########################################################################################################################
    #                                                                                                                       #
    #                                 SCAN TOP NAVBAR                                                                       #
    #   Handling Buttons that only show up on scan screen for mac but are displayed on the preview screen for ios/android   #
    #########################################################################################################################
    SHARE_BTN = "scan_share_btn"
    SAVE_BTN = "scan_save_btn"
    ########################################################################################################################
    #                                  Verification Functions                                                              #
    ########################################################################################################################

    def verify_top_navbar_button_and_click(self, element, format_specifier=[], click=True, scroll=False, delay=0, raise_e=False):
        """
        Use to click on the Scan screen top navigation bar buttons:
            - Share
            - Save
            - Print
            - Shortcuts
            - Mobile Fax
            - Back
            - New Scan
        """
        self.exit_full_screen_mode()
        return self.verify_an_element_and_click(element, format_specifier=format_specifier, click=click, scroll=scroll, delay=delay, raise_e=raise_e)

    def verify_scanner_busy_popup(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("scanner_busy_popup_title", timeout=timeout, raise_e=raise_e)
    
    ########################################################################################################################
    #                                  Action Functions                                                                    #
    ########################################################################################################################

    def dismiss_scanner_busy_popup(self):
        self.driver.click("scanner_busy_popup_ok_btn")
    
    def select_scan_job_button(self, verify_messages=True, scan_timeout=20):
        self.driver.click("scan_btn", change_check={"wait_obj": "scanning_msg"}, timeout=20)
        if self.verify_scanner_busy_popup(timeout=3, raise_e=False):
            self.dismiss_scanner_busy_popup()
            pytest.skip("Scanner is busy")
        if verify_messages:
            if not self.driver.wait_for_object("scan_processing_message", timeout=scan_timeout, interval=0.2, raise_e=False) and\
               not self.driver.wait_for_object("add_scan_btn"):
                raise TimeoutException(f"Still scanning after timeout of {scan_timeout}")
    
    def select_scan_job(self):
        self.select_scan_job_button(verify_messages=True)