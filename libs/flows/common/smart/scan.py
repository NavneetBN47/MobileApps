import sys
import logging
import time
import re

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from MobileApps.libs.flows.common.smart.smart_flow import SmartFlow
from SAF.misc import saf_misc


class MissingCaptureModeException(Exception):
    pass

class Scan(SmartFlow):
    flow_name = "scan"
    folder_name = "scan"

    # Scan Sources
    SOURCE_CAMERA_OPT = "camera_source_btn"
    SOURCE_PRINTER_SCAN_OPT = "printer_scan_source_btn"
    SOURCE_FILES_PHOTOS = "files_photo_source_btn"
    ADJUST_SETTINGS_CHECK = {"wait_obj": "scanning_adjust_settings_txt", "invisible": True, "timeout": 5}

    # Change Checks for Scan/Camera Scan capture
    PHOTO_CHANGE_CHECK = {"wait_obj": "adjust_next_btn", "invisible": False, "timeout": 30}
    DOCUMENT_CHANGE_CHECK = {"wait_obj": "adjust_next_btn", "invisible": False, "timeout": 30}
    TEXT_EXTRACT_CHANGE_CHECK = {"wait_obj": "text_extract_continue_btn", "invisible": False, "timeout": 30}
    MULTI_ITEM_CHANGE_CHECK = {"wait_obj": "nav_btns_layout", "invisible": False, "flow_change": "preview", "timeout": 30}
    COPY_CHANGE_CHECK = {"wait_obj": "digital_copy_title", "invisible": False, "flow_change": "digital_copy", "timeout": 30}
    ID_CARD_CHANGE_CHECK = [
        {"wait_obj": "id_back_scanner_msg_txt", "invisible": False, "timeout": 30},
        {"wait_obj": "id_preview_front_title_txt", "invisible": False, "timeout": 30}
    ]
    ID_CARD_CAMERA_CHANGE_CHECK = [
        {"wait_obj": "id_back_msg_txt", "invisible": False, "timeout": 20},
        {"wait_obj": "id_preview_front_title_txt", "invisible": False, "timeout": 20}
    ]

    CAPTURE_CHANGE_CHECKS = {
        "photo": PHOTO_CHANGE_CHECK,
        "document": DOCUMENT_CHANGE_CHECK,
        "text_extract":TEXT_EXTRACT_CHANGE_CHECK,
        "multi_item": MULTI_ITEM_CHANGE_CHECK,
        "id_card": ID_CARD_CHANGE_CHECK,
        "id_card_" + SOURCE_CAMERA_OPT: ID_CARD_CAMERA_CHANGE_CHECK,
        "batch": None,
        "book": None
    }

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def select_exit_btn(self):
        """
        Selects the x button on the top left to exit to home screen. If there is atleast 
        one image already captured the icon is a left arrow and will remove the most recent image.
        """
        self.driver.click("exit_btn", change_check={"wait_obj": "exit_btn", "invisible": True})

    def select_enhancements_btn(self):
        """
        Selects the gear button which opens the "Enhancements" screen
        """
        self.driver.click("gear_btn", change_check={"wait_obj": "gear_btn", "invisible": True})
    
    def start_capture(self, change_check=None, timeout=10):
        """
        Selects the capture button to initiate a scan
        :param change_check: The change check to use when selecting the capture button.
        """
        self.driver.click("capture_btn", change_check=change_check, timeout=timeout)

    def select_capture_mode(self, mode):
        """
        Select a capture mode
        :param mode: The desired capture mode. Use prefixes of "*_mode_btn" locators. 
            Possible Values: "photo", "document", "id_card", "book", "multi_item", "batch"
        """
        mode_btn = mode + "_mode_btn"
        # all basic modes always visible for basic/ucde users
        self.driver.wait_for_object("scan_mode_recycler")
        if self.driver.session_data["hpid_type"] == "hp+" and self.driver.find_object(mode_btn, raise_e=False) is False:
            self.driver.swipe("scan_mode_recycler", direction="right")
            scroll_count = 0
            while self.driver.find_object(mode_btn, raise_e=False) is False:
                assert scroll_count < 3, "Could not locate capture mode {} after 3 scrolls".format(mode)
                if self.driver.get_attribute("mode_btn", "selected") == "true":  # reached end of mode recycler
                    raise MissingCaptureModeException('Could not locate "{}"'.format(mode_btn))
                # clicking mode_btns is inconsistent for some devices. Must drag left most mode button to center(selected mode button)
                self.driver.drag_and_drop(self.driver.find_object("mode_btn", index=0), self.driver.wait_for_object("selected_mode_btn"))
                scroll_count += 1
                time.sleep(1)  # delay to allow recycler to settle
        if not self.verify_selected_capture_mode(mode=mode, raise_e=False):
            # clicking mode_btns is inconsistent for some devices. Must drag left most mode button to center(selected mode button)
            self.driver.drag_and_drop(self.driver.find_object(mode_btn), self.driver.wait_for_object("selected_mode_btn"))
        return True

    def select_preview(self, wait=True, timeout=20):
        """
        Click on Preview button
        End of flow: Scan screen
        :param wait: Wait for the preview to be captured
        :param timeout: Timeout for scan preview to complete, ignored if wait=False
        """
        self.driver.click("preview_btn")
        if wait:
            end_time = time.time() + timeout
            time.sleep(1)
            while self.driver.get_attribute("capture_btn", "selected") == "true":
                if time.time() > end_time:
                    raise TimeoutException("Scan preview was not captured within {} seconds".format(timeout))

    def select_done(self):
        """Selects the Pages Icon on the bottom right"""
        self.driver.click("pages_icon")
           
    def select_scan_settings_btn(self):
        """
        Click on Settings button on Scan Home screen
        End of flow: Scan Settings screen
        """
        self.driver.click("scan_settings_btn", change_check={"wait_obj": "scan_settings_btn", "invisible": True})

    def select_source(self, source_opt):
        """
        Selects the image source button
        :param source: The image source to select, if None only opens the source menu. 
            Possible values: "files_photo", "camera" or "scanner
        """
        self.driver.click("source_btn")
        self.driver.click(source_opt)
    
    def select_coachmark_btn(self, btn="next", change_check=None):
        """
        Click on Next button on the coachmark message
        :param btn: The coachmark button to press. Possible values are "next", "back" or "close"
        """
        self.driver.click("coachmark_{}_btn".format(btn), change_check=change_check)

    def dismiss_coachmark(self, timeout=20):
        """
        Dismiss all coarchmark message on Scan or Camera scan screen
        """
        timeout = time.time() + timeout
        while time.time() < timeout:
            if (next_btn := self.driver.wait_for_object("coachmark_next_btn", raise_e=False)) is not False:
                next_btn.click()
            else:
                return True
        raise TimeoutException("coachmark message didn't dismiss successful")

    def get_scanned_file_size(self, file_path):
        """
        Get the size of the file from device
        :return file name
        """
        try:
            contents = self.driver.wdvr.pull_file(file_path).decode('base64')
            size = sys.getsizeof(contents)
            logging.debug("Scanned File: {} has file size of: {} bytes".format(file_path, size))
            return size
        except NoSuchElementException:
            logging.debug("Can not get file. {}".format(file_path))
            return 0

    # ------------------------------ Scan Settings ------------------------------
    def select_scan_setting(self, setting, option=None):
        """
        Selects one of the settings on the scan settings screen.
        :param setting: The setting to select. Possible Values: "page_size", "source", "resolution", "color"
        :param option: See values from select_scan_settings_option. If None only loads the specified setting's screen.
        """
        self.driver.wait_for_object("scan_setting_txt")
        self.driver.click("settings_label_txt", format_specifier=[self.driver.return_str_id_value("{}_setting_txt".format(setting))], 
            change_check={"wait_obj": "settings_title_txt", "format_specifier": [self.driver.return_str_id_value("{}_setting_txt".format(setting))]})
        if option:
            self.select_scan_settings_option(option, screen=setting)
    
    def select_scan_settings_option(self, option, screen=None):
        """
        Selects one of the options for the current scan settings screen.
        :param option: The option to select based on the current scan setting screen. Possible values: "3.5x5", "4x6", "5x7", 
            "letter", "a4", "scanner", "feeder", "75_dpi", "100_dpi", "200_dpi", "300_dpi", "color", "black"
        :param screen: The screen that the option belongs to, Possible Values: "page_size", "resolution", "color", "source". If None screen is inferred based on title.
        """
        if not screen:
            screen = self.verify_scan_settings_title()
            assert screen != "scan", "Should not be at main scan settings screen"
        self.driver.click("settings_option_btn", format_specifier=[self.driver.return_str_id_value("{}_{}_txt".format(option, screen))])

    # ------------------------------ Book Capture ------------------------------
    def select_book_page_order_button(self):
        """
        Selects the book page order button
        """
        self.driver.click("book_page_order_btn")

    def select_book_page_order_switch_button(self):
        """
        Selects the book page order switch button
        NOTE: Only visible if book page order is enabled
        """
        self.driver.click("book_page_switch_btn")

    # ------------------------------ Enhancements Screen ------------------------------
    def toggle_enhancement(self, option, enable=True):
        """
        Toggles an enhancements on the enhancemnts screen(navigated to by gear icon).
        :param option: The option to toggle. Possible Values: "auto_enhancements", "auto_heal", "auto_orientation", "flatten_book_pages"
        :param enabled: Enable or disable the specified option
        """
        if option == "auto_heal" and enable and self.driver.get_attribute("settings_switch", "checked", format_specifier=[self.driver.return_str_id_value("auto_enhancements_enhancement")]) == "false":
            logging.warning("Cannot toggle Auto-Heal on when Auto-Enhancements is off")
            return False
        desired_state = "true" if enable else "false"
        str_id = self.driver.return_str_id_value(option + "_enhancement")
        if self.driver.get_attribute("enhancement_switch", "checked", format_specifier=[str_id]) != desired_state:
            logging.info("Toggling {} {}".format(option, "on" if enable else "off"))
            self.driver.click("enhancement_switch", format_specifier=[str_id])
        else:
            logging.info("{} is already toggled {}".format(option, "on" if enable else "off"))
        return True

    # ---------------------------------- Camera Only ----------------------------------
    def grant_camera_permissions(self):
        """
        Handles the No Camera Access screen when camera scan is initally opened
        """
        if self.verify_no_camera_access_screen(raise_e=False):
            self.driver.click("allow_camera_access_btn")
            return True
        return False

    def toggle_auto_mode(self, enabled=True):
        """
        Toggles auto mode on the camera capture screen
        """
        desired_state = "true" if enabled else "false"
        if self.driver.get_attribute("auto_btn", "selected") != desired_state:
            self.driver.click("auto_btn", change_check={"cc_type": "wait_for_attribute", "wait_obj": "auto_btn", "wait_attribute": "selected"})

    # ---------------------------- ID Card Preview Screen -----------------------------
    def select_id_next_btn(self):
        """
        Selects the next button on the ID Card Front/Back preview screen
        """
        self.driver.click("id_preview_next_btn")

    def select_id_page_options_btn(self, option=None):
        """
        Selects the page options button on the scan preview screen
        :param option: The page options menu button to select, if None only opens page options menu. options are "*_page_opt_btn" possible values: "edit", "replace"
        """
        self.driver.click("id_preview_page_opts_btn")
        if option is not None:
            self.driver.click("{}_page_opt_btn".format(option))

    def select_id_rotate_btn(self, verify=False):
        """
        Selects the rotate button on ID Card Front/Back preview screen
        :param verify: Verify the rotate and page options disappear during rotation and reappear after
        """
        if not verify:
            self.driver.click("id_preview_rotate_btn")
            return True
        init_elements = {k: self.driver.wait_for_object(k) for k in ["id_preview_rotate_btn", "id_preview_page_opts_btn"]}
        self.driver.click("id_preview_rotate_btn")
        assert self.driver.wait_for_object("id_preview_rotate_btn") != init_elements["id_preview_rotate_btn"], "id_preview_rotate_btn id did not change"
        assert self.driver.wait_for_object("id_preview_page_opts_btn") != init_elements["id_preview_page_opts_btn"], "id_preview_page_opts_btn id did not change"
        return True

    def capture_id_preview_img(self):
        """
        Returns screenshot of id card preview asbase64
        """
        return self.driver.screenshot_element("id_preview_img")

    # --------------------------- Adjust Boundaries Screen ----------------------------
    def select_adjust_next_btn(self, timeout=20, change_check={"wait_obj": "adjust_next_btn", "invisible": True}, raise_e=True):
        """
        Selects the next button on the adjust screen
        """
        self.driver.click("adjust_next_btn", change_check=change_check, timeout=timeout, retry=8, raise_e=raise_e)

    def select_adjust_size_option(self, option="full"):
        """
        Selects one of the options on the bottom of the adjustment screen.
        :param option: The option to select. Possible values: "auto" or "full"
        """
        self.driver.click("adjust_opt_{}_btn".format(option))

    def dismiss_camera_capture_tips_popup(self):
        """
        Dismiss 'Tips for Camera Capture' popup if it displays
        Note: Add 20 seconds to timeout because of loading process
        """
        if self.driver.wait_for_object("capture_tips_popup", raise_e=False, timeout=20) and (ok_btn := self.driver.wait_for_object("capture_tips_ok_btn", raise_e=False)):
            ok_btn.click()
        else:
            logging.info("'Tips for Camera Capture' is NOT displayed")

    
    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_scan_screen(self, source=None, invisible=False,auto_btn_invisable=False, timeout=10):
        """
        Verify that current screen is Scan screen via:
            - exit button
            - capture button
            - gear button
            - source button
            - flash button(if camera source)
            - auto button(if camera source)
            - preview button(if printer/scanner source)
            - Scan settings button(if printer/scanner source)
        :param source: The current source. Use class constants SOURCE_PRINTER_SCAN_OPT or SOURCE_CAMERA_OPT
        """
        self.driver.wait_for_object("exit_btn", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("capture_btn", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("gear_btn", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("source_btn", invisible=invisible, timeout=timeout)
        if source == self.SOURCE_PRINTER_SCAN_OPT:
            self.driver.wait_for_object("preview_btn", invisible=invisible, timeout=timeout)
            self.driver.wait_for_object("scan_settings_btn", invisible=invisible, timeout=timeout)
        elif source == self.SOURCE_CAMERA_OPT:
            self.driver.wait_for_object("flash_btn", invisible=invisible, timeout=timeout)
            self.driver.wait_for_object("auto_btn", invisible=auto_btn_invisable, timeout=timeout)

    def verify_place_content_txt(self, invisible=False):
        """
        Verifies the "Place content on the scanner..." text on scan screen
        """
        self.driver.wait_for_object("place_content_txt", invisible=invisible)

    def verify_selected_source(self):
        """
        Returns which source is currently selected. Returns False if cannot determine source.
        :param source: If source is None returns source relevant source constant else verifies that the specified source is selected.
            Use class constants SOURCE_CAMERA_OPT or SOURCE_PRINTER_SCAN_OPT. Does not check for file photos source.
        """
        if self.driver.wait_for_object("flash_btn", raise_e=False) or self.driver.wait_for_object("allow_camera_access_btn", raise_e=False):
            return self.SOURCE_CAMERA_OPT
        elif self.driver.wait_for_object("scan_settings_btn", raise_e=False):
            return self.SOURCE_PRINTER_SCAN_OPT
        return False

    def verify_adjust_screen(self, timeout=20):
        """
        Verifies the Adjust Boudnaries screen
            - Next button
            - Auto button
            - Full button
        """
        self.driver.wait_for_object("adjust_next_btn", timeout=timeout)
        self.driver.wait_for_object("adjust_opt_auto_btn", timeout=timeout)
        self.driver.wait_for_object("adjust_opt_full_btn", timeout=timeout)

    def verify_successful_scan_job(self, invisible=True, timeout=170):
        """
        Verify that a scan job is successful via invisible of Cancel button

        Note: depending on printer, scan job can take time to complete

        """
        self.driver.wait_for_object("scanning_page_msg", invisible=invisible, timeout=timeout)

    def verify_current_settings_info(self, settings_info):
        """
        Verify current setting info displays on screen
        :param settings_info: target setting info
        """
        self.driver.wait_for_object("current_settings_txt", format_specifier=[settings_info])

    def verify_scan_settings_screen(self):
        """
        Verify the "Scan Settings" screen.
         - "Scan Settings" title text
         - "Page Size" button
         - "Source" button
         - "Resolution" button
         - "Color" button
        """
        self.driver.wait_for_object("settings_title_txt", format_specifier=[self.driver.return_str_id_value("scan_setting_txt")])
        self.driver.wait_for_object("settings_label_txt", format_specifier=[self.driver.return_str_id_value("page_size_setting_txt")])
        self.driver.wait_for_object("settings_label_txt", format_specifier=[self.driver.return_str_id_value("source_setting_txt")])
        self.driver.wait_for_object("settings_label_txt", format_specifier=[self.driver.return_str_id_value("resolution_setting_txt")])
        self.driver.wait_for_object("settings_label_txt", format_specifier=[self.driver.return_str_id_value("color_setting_txt")])
    
    def verify_scan_settings_title(self, screen=None):
        """
        Gets the current scan screen based on the title text.
        :param screen: The expected screen based on title. Possible Values: "scan", "page_size", "source", "resolution", "color"
        """
        self.driver.wait_for_object("settings_title_txt")
        if screen:
            self.driver.wait_for_object("settings_title_txt", format_specifier=[self.driver.return_str_id_value(screen + "_setting_txt")])
            return True
        title_txt = self.driver.get_attribute("settings_title_txt", "text")
        for locator in ["scan_setting_txt", "page_size_setting_txt", "source_setting_txt", "resolution_setting_txt", "color_setting_txt"]:
            if self.driver.return_str_id_value(locator) == title_txt:
                return locator.replace("_setting_txt", "")
        return False

    def verify_scan_setting_options(self, screen=None, options=None):
        """ 
        Verify scan setting options on the "Page Size", "Source", "Resolution" or "Color" screen
        :param screen: Verify options based on the specified screen. Ignored if options param is not None. Possible Values: "page_size", "source", "resolution", "color"
        :param options: The option(s) to verify, list or str.Possible Values: "3.5x5", "4x6", "5x7", "letter", "a4", "scanner", "feeder", "75_dpi", "100_dpi", "200_dpi", 
            "300_dpi", "color", "black"
        NOTE: If screen and options are None options to verify are inferred based on current screen's title
        """
        options_map = {
            "page_size": ["3.5x5", "4x6", "5x7", "letter", "a4"],
            "source": ["scanner"],  # Many printers lack feeders so not verified by default
            "resolution": ["75_dpi", "100_dpi", "200_dpi", "300_dpi"],
            "color": ["color", "black"]
        }
        if screen is None:
            screen = self.verify_scan_settings_title()
            assert screen != "scan", "Should not be at main scan settings screen"
        if options is None:
            options = options_map[screen]
        elif not isinstance(options, list):
            options = [options]
        for opt_str in [self.driver.return_str_id_value("{}_{}_txt".format(opt, screen)) for opt in options]:
            logging.info("Verifying {} {} option".format(opt_str, screen))
            self.driver.wait_for_object("settings_option_btn", format_specifier=[opt_str])

    def verify_selected_scan_setting_option(self, setting, option):
        """
        Verify the selected option for a scan setting on the scan settings screen.
        :param setting: The setting to check. Possible Values: "page_size", "source", "resolution", "color"
        :param option: The expected option for the specified setting: Possible Values: "3.5x5", "4x6", "5x7", "letter", "a4", "scanner", "feeder", 
            "75_dpi", "100_dpi", "200_dpi", "300_dpi", "color", "black"
        """
        self.verify_scan_settings_title(screen="scan")
        expected_opt_str = self.driver.return_str_id_value("{}_{}_txt".format(option, setting))
        selected_opt_str = self.driver.get_attribute("selected_setting_option_txt", "text", format_specifier=[self.driver.return_str_id_value("{}_setting_txt".format(setting))])
        assert selected_opt_str == expected_opt_str, "Current {} option {} does not match expected option {}".format(setting, selected_opt_str, expected_opt_str)

    def verify_enhancements_screen(self, advanced=False):
        """
        Verify Enhancement screen which opens froms the gear icon on the scan screen.
         - Title
         - Auto-Orientation
         - Auto-Enhancements
         - Auto-Heal for hp+
         - Flatten Book Pages for hp+
        :param advanced: Verify the advanced(hp+) enhancements
        """
        self.driver.wait_for_object("preferences_title")
        self.driver.wait_for_object("auto_enhancements_enhancement")
        self.driver.wait_for_object("auto_orientation_enhancement")
        if advanced:
            self.driver.wait_for_object("flatten_book_pages_enhancement")
            self.driver.wait_for_object("auto_heal_enhancement")
    
    def verify_enhancement_state(self, option, enabled):
        """
        Verify the state of an enhancement setting
        :param option: The enhancement to check. Possible Values: "auto_enhancements", "auto_heal", "auto_orientation", "flatten_book_pages"
        :param enabled: The enhancement switch's state
        """
        desired_state = "true" if enabled else "false"
        assert self.driver.get_attribute("enhancement_switch", "checked", format_specifier=[self.driver.return_str_id_value(option + "_enhancement")]) \
             == desired_state, "Expected {} enhancment to be enabled: {}".format(option, enabled)

    def verify_capture_modes(self, advanced=False):
        """
        Verify Capture modes on scan home screen.
         - Batch mode
         - Photo mode
         - Document mode
         - Multi-Item mode (HP+ account visible, Basic account invisible)
         - Book mode (HP+ account visible, Basic account invisible)
         - ID Card mode (HP+ account visible, Basic account invisible)
        :param advanced: Should verify the advanced(hp+) capture modes, id_card, book and multi_item
        """
        self.driver.wait_for_object("photo_mode_btn")
        self.driver.wait_for_object("document_mode_btn")
        self.driver.wait_for_object("batch_mode_btn")
        if not advanced:
            return True
        adv_modes = ["multi_item_mode_btn", "id_card_mode_btn", "book_mode_btn"]
        for mode in adv_modes:
            if not self.driver.wait_for_object(mode, raise_e=False):
                visible_modes = self.driver.find_object("mode_btn", multiple=True)
                self.driver.drag_and_drop(visible_modes[-1], [e for e in visible_modes if e.get_attribute("selected") == "true"][0])
                self.driver.wait_for_object(mode)
        return True

    def verify_selected_capture_mode(self, mode="document", raise_e=True):
        """
        Verify the specified mode is selected
        :param mode: Mode to verify is selected. Possible Values: "photo", "document", "batch", "id_card", "book", "multi_item"
        """
        return self.driver.find_object("selected_mode_btn", format_specifier=[self.driver.return_str_id_value(mode + "_mode_btn")], raise_e=raise_e)

    def verify_no_camera_access_screen(self, raise_e=True):	
        """	
        Verify camera scan screen with no access message:	
            - No camera access text	
            - Allow access button	
        """	
        return self.driver.wait_for_object("no_camera_access_txt", raise_e=raise_e) and self.driver.wait_for_object("allow_camera_access_btn", raise_e=raise_e)	

    def verify_id_preview_screen(self, side):
        """
        Verifies the ID Card preview screen
         - title text
         - rotate button
         - page options(...) button
         - next button
        :param side: Verify the id card front or back preview screen. Possible Values: "front", "back"
        """
        self.driver.wait_for_object("id_preview_{}_title_txt".format(side))
        self.driver.wait_for_object("id_preview_rotate_btn")
        self.driver.wait_for_object("id_preview_page_opts_btn")
        self.driver.wait_for_object("id_preview_next_btn")

    def verify_coachmark(self, coach_num=None, invisible=False):
        """
        Verifies that a coachmark is displayed.
         - close(x) button
         - status text
         - body text
         - next/done button
         - back button
        :param coach_num: The number of the coachmark to verify, 1-4.
        """
        coachmarks_strs = [
            "scanning_adjust_settings_txt",
            "scanning_adjust_capture_settings_txt",
            "tap_to_start_scan_txt",
            "change_the_source_txt"
        ]
        self.driver.wait_for_object("coachmark_close_btn", invisible=invisible)
        self.driver.wait_for_object("coachmark_status_txt", invisible=invisible)
        self.driver.wait_for_object("coachmark_next_btn", invisible=invisible)
        if not coach_num:
            return True
        self.driver.wait_for_object(coachmarks_strs[coach_num - 1], invisible=invisible)
        if 1 < coach_num < 4:  # back button doesnt appear on first and last coachmarks
            self.driver.wait_for_object("coachmark_back_btn", invisible=invisible)
        return True

    def verify_bubble_msg(self, message=None, invisible=False, interval=3, timeout=10, raise_e=True):
        """
        Verify the bubble message above the scan mode recycler.
        :param message: The message to verify. Use "*_msg_txt" str_id locators
        """
        format_specifier = []
        if message:
            format_specifier = [self.driver.return_str_id_value(message if message.endswith("_msg_txt") else message + "_msg_txt") ]
        self.driver.wait_for_object("bubble_msg", format_specifier=format_specifier, invisible=invisible, interval=interval, timeout=timeout, raise_e=raise_e)

    def verify_book_page_order_button(self, screenshot=False):
        """
        Verify the book page order button
        :param screenshot: Return a screenshot of the button
        """
        self.driver.wait_for_object("book_page_order_btn")
        if screenshot:
            return saf_misc.load_image_from_base64(self.driver.screenshot_element("book_page_order_btn"))
        return True

    def verify_book_page_switch_button(self, invisible=False, screenshot=False):
        """
        Verify the book page switch
        :param screenshot: Return a screenshot of the button
        """
        self.driver.wait_for_object("book_page_switch_btn", invisible=invisible)
        if invisible and screenshot:
            logging.warning("Cannot screenshot invisible element")
        elif screenshot:
            return saf_misc.load_image_from_base64(self.driver.screenshot_element("book_page_switch_btn"))
        return True

    def verify_adjust_settings_message(self, raise_e=True):
        """
        Verify Adjust Settings coarchmark message
        """
        return self.driver.wait_for_object("scanning_adjust_settings_txt", raise_e=raise_e)

    def verify_scan_adjust_capture_settings_message(self, raise_e=True):
        """
        Verify Adjust capture Settings coarchmark message
        """
        return self.driver.wait_for_object("scanning_adjust_capture_settings_txt", raise_e=raise_e)
    
    def verify_scan_select_preset_message(self, raise_e=True):
        """
        Verify scan select the preset coarchmark message
        """
        return self.driver.wait_for_object("scanning_select_preset_txt", raise_e=raise_e)
    
    def verify_tap_to_start_scan_message(self, raise_e=True):
        """
        Verify tap tap to start scan message
        """
        return self.driver.wait_for_object("tap_to_start_scan_txt", raise_e=raise_e)
    def verify_tap_to_change_the_source_message(self, raise_e=True):
        """
        Verify Scan tap to change the source of your scan message
        """
        return self.driver.wait_for_object("change_the_source_txt", raise_e=raise_e)
    
    def verify_scan_error_popup(self, raise_e=True):
        """
        Verify Scan error popup:
            - Scan error title
        """
        return self.driver.wait_for_object("scan_error_title", timeout=15, raise_e=raise_e)

    # --------------------------- Adjust Boundaries Screen ----------------------------
    def verify_text_extract_title(self):
        """
        Verify title is Text Extract
        """
        self.driver.wait_for_object("text_extract_title_txt")

    def select_text_extract_continue_btn(self):
        """
        Press continue button to extract text
        """
        self.driver.wait_for_object("text_extract_continue_btn")
        self.driver.click("text_extract_continue_btn")

    def verify_extracting_text_title(self):
        """
        Verify Extracting Text Dialog showing
        Note: This function is not used. The dialog goes away
              before it can be tested.
        """
        self.driver.wait_for_object("extracting_text_title")

    def verify_text_extract_language(self,language):
        """
        verify the language used for extracting text
        """
        self.driver.wait_for_object('text_extract_language',format_specifier=[language])        

    def select_copy_to_clipboard_btn(self):
        """
        press copy all button
        Note: this function is not being used
        """
        self.driver.click("copy_to_clipboard_btn")

    def long_press_text_extract_edit_text(self):
        """
        Long press on Text Extract edit area
        Note: this function is not being used
        """
        self.driver.long_press("text_extract_edit_text")

class AndroidScan(Scan):
    platform = "android"

    def select_capture_mode(self, mode):
        if self.driver.session_data["smart_state"].get("capture_mode", "document") != mode:
            super().select_capture_mode(mode)
            self.driver.session_data["smart_state"]["capture_mode"] = mode
    def dismiss_coachmark(self, timeout=20, screen=None):
            """
            Dismisses the coachmark on the scan screen
            :param timeout: Timeout in seconds for dismissing the coachmark
            :param screen: The screen that the coachmark belongs to. Used to update smart_state for faster execution
                Possible values: "camera" or "scanner"
            """
            state_name = None
            if screen:
                if screen not in ["camera", "scanner"]:
                    raise ValueError(f'screen param must be "camera" or "scanner". "{screen}" is invalid.')
                state_name = screen + "_coachmark_dismissed"
            if state_name and self.driver.session_data["smart_state"].get(state_name, False):
                return True
            to_return = super().dismiss_coachmark(timeout=timeout)
            if state_name and to_return:
                self.driver.session_data["smart_state"][state_name] = True
            return to_return

    def verify_capture_button(self, is_selected=None, timeout=30):
        """
        Verifies the capture button
        :param is_selected: True to verify selected == True False to verify selected == False
        """
        if is_selected is None:
            self.driver.wait_for_object("capture_btn", timeout=timeout)
            return True
        end_time = time.time() + timeout
        selected_val = "true" if is_selected else "false"
        while self.driver.get_attribute("capture_btn", "selected") == selected_val:
            if time.time() < end_time:
                raise TimeoutException("Capture did not complete within {} seconds".format(timeout))
            time.sleep(2)
        return True

    def verify_capture_progress_icon(self, invisible=False):
        self.driver.wait_for_object("camera_progress_icon", invisible=invisible, timeout=30)

    def verify_book_page_guides(self, reordered=None, invisible=False):
        """
        Verify the book capture mode guides.
         - page 1 and 2 icons
         - page divider
        :param reordered: If True verify 2 is above 1 if False verify 1 is above 2 if None dont verify positions of 1 and 2 icons. Ignored if invisible is True.
        """
        if reordered is not None and not invisible:
            p = re.compile(r"\[(?P<left>\d+),(?P<top>\d+)\]\[(?P<right>\d+),(?P<bottom>\d+)]")
            page_one_height = int(p.match(self.driver.get_attribute("book_guide_page_one", "bounds"))["top"])
            page_two_height = int(p.match(self.driver.get_attribute("book_guide_page_two", "bounds"))["top"])
            if reordered:
                assert page_two_height < page_one_height, "Page two guide should be above page one guide for reordered: {}".format(reordered)
            else:
                assert page_two_height > page_one_height, "Page one guide should be above page two guide for reordered: {}".format(reordered)
        else:
            self.driver.wait_for_object("book_guide_page_one", invisible=invisible)
            self.driver.wait_for_object("book_guide_page_two", invisible=invisible)
        self.driver.wait_for_object("book_guide_divider", invisible=invisible)
