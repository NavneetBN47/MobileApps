from selenium.common.exceptions import NoSuchElementException, TimeoutException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging
import time
from SAF.decorator.saf_decorator import screenshot_capture


class MissingCameraModeException(Exception):
    pass

class CameraScan(SmartFlow):
    flow_name = "camera_scan"

    # Change checks for clicking shutter button
    PHOTO_CHANGE_CHECK = {"wait_obj": "adjust_next_btn", "invisible": False, "timeout": 20}
    DOCUMENT_CHANGE_CHECK = {"wait_obj": "adjust_next_btn", "invisible": False, "timeout": 20}
    MULTI_ITEM_CHANGE_CHECK = {"wait_obj": "nav_btns_layout", "invisible": False, "flow_change": "preview", "timeout": 20}
    COPY_CHANGE_CHECK = {"wait_obj": "digital_copy_title", "invisible": False, "flow_change": "digital_copy", "timeout": 30}
    ID_CARD_CHANGE_CHECK = [
        {"wait_obj": "id_back_status_txt", "invisible": False, "timeout": 20},
        {"wait_obj": "id_preview_front_title_txt", "invisible": False, "timeout": 20}
    ]

    CAPTURE_CHANGE_CHECKS = {
        "photo": PHOTO_CHANGE_CHECK,
        "document": DOCUMENT_CHANGE_CHECK,
        "multi_item": MULTI_ITEM_CHANGE_CHECK,
        "copy": COPY_CHANGE_CHECK,
        "id_card": ID_CARD_CHANGE_CHECK,
        "batch": None,
        "book": None
    }

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_capture_mode(self, mode, timeout=30):
        """
        Select a capture mode
        :param mode: The desired capture mode. Use prefixes of "*_mode_btn" locators. 
            Possible Values: "photo", "document", "id_card", "book", "multi_item", "batch"
        """
        end_time = time.time() + timeout
        mode_btn = mode + "_mode_btn"
        # all basic modes always visible for basic/ucde users
        self.driver.wait_for_object("scan_mode_recycler")
        if self.driver.session_data["hpid_type"] == "hp+" and self.driver.find_object(mode_btn, raise_e=False) is False:
            self.driver.swipe("scan_mode_recycler", direction="right")
            while self.driver.find_object(mode_btn, raise_e=False) is False:
                if time.time() > end_time:
                    raise TimeoutException('Could not locate "{}" in {} seconds'.format(mode_btn, timeout))
                if self.driver.get_attribute("mode_btn", "selected") == "true":  # reached end of mode recycler
                    raise MissingCameraModeException('Could not locate "{}"'.format(mode_btn))
                # clicking mode_btns is inconsistent for some devices. Must drag left most mode button to center(selected mode button)
                visible_modes = self.driver.find_object("mode_btn", multiple=True)
                self.driver.drag_and_drop(visible_modes[0], [e for e in visible_modes if e.get_attribute("selected") == "true"][0])
                time.sleep(1)  # delay to allow recycler to settle
        if self.driver.get_attribute(mode_btn, "selected") != "true":
            # clicking mode_btns is inconsistent for some devices. Must drag left most mode button to center(selected mode button)
            self.driver.drag_and_drop(self.driver.find_object(mode_btn), [e for e in self.driver.find_object("mode_btn", multiple=True) if e.get_attribute("selected") == "true"][0])
        return True

    def toggle_capture_mode(self, manual=True):
        """
        Toogle Capture Mode: It is for BATCH mode
        :param manual: True -> disable
                       False -> enable
        """
        desired_state = "false" if manual else "true"
        if desired_state != self.driver.get_attribute("auto_btn", "selected"):
            self.driver.click("auto_btn")

    def capture_photo(self, mode="document", number_pages=1, is_permission=True):
        """
        Captures images at the camera_scan screen
        :param mode: The camera scan mode to use. Possible values: "photo", "document", "id_card", "book", "multi_item", "batch", "copy"
        :param number_pages: The number of pages to capture, only applies to "batch" and "book" mode
        :param is_permission: Check for/handle permission screen
        """
        if mode not in self.CAPTURE_CHANGE_CHECKS:
            raise ValueError('{} is not a valid mode, mode must be one of ["photo","document","id_card","book","multi_item","batch"]'.format(mode))
        if is_permission:
            self.grant_permissions()
        if number_pages > 1 and mode not in ["batch", "book"]:
            logging.warning("number_pages > 1 is not valid for mode {}".format(mode))
            number_pages = 1
        if mode == "id_card":
            number_pages = 2
        if mode != "copy":
            self.select_capture_mode(mode)
        for i in range(number_pages):
            change_check = self.CAPTURE_CHANGE_CHECKS[mode]
            if isinstance(change_check, list):
                change_check = change_check[i]
            self.driver.click("shutter_btn", change_check=change_check)
            time.sleep(1)
            if change_check is None:
                self.driver.wait_for_object("progress_icon", invisible=True, timeout=30)
        if mode in ["batch", "book"]:
            self.click_done()

    def grant_permissions(self):
        """
        Handles the capture no access and system permission popup if capture no access screen is present
        Returns true if permissions needed to be granted
        """
        if self.verify_capture_no_access_screen(raise_e=False):
            self.select_camera_access_allow()
            self.check_run_time_permission()
            return True
        return False

    def click_shutter(self, wait=True, change_check=None):
        """
        Clicks the shutter button to take a picture
        :param wait: Wait for capture to complete
        :param change_check: The change_check to use when clicking the shutter button. Recommended to use change_check from CAPTURE_CHANGE_CHECKS class constant
        """
        self.driver.click("shutter_btn", change_check={"wait_obj": "progress_icon", "invisible": False} if change_check is None else change_check)
        if wait:
            time.sleep(1)
            self.driver.wait_for_object("progress_icon", invisible=True, timeout=15)

    def click_done(self):
        """
        Click on Done button after capturing photos in batch mode
        """
        self.driver.click("done_btn")

    def select_camera_access_allow(self):
        """
        Click on Allow Access button on No Camera Access
        """
        self.driver.wait_for_object("allow_access_btn")
        self.driver.click("allow_access_btn")
    
    def verify_camera_access_allow_txt(self):
        """
        Verify that the Allow Access button is displayed
        """
        return self.driver.wait_for_object("allow_access_btn")
    
    def select_camera_permission_deny_btn(self, timeout=10):
        """
        Click on DENY button on Camera permission access screen
        """
        self.driver.wait_for_object("camera_permission_access_deny_btn",timeout=timeout).click()

    def click_camera_access_allow(self):
        """
        Click on Allow Access button on No Camera Access
        """
        self.driver.click("allow_access_btn")

    def select_camera_permission_allow_btn(self, timeout=20):
        """
        Click on ALLOW button on Camera permission access screen
        """
        self.driver.click("camera_permission_access_allow_btn", timeout=timeout)

    def dismiss_tips_camera_capture_popup(self):
        """
        Dismiss 'Tips for Camera Capture' popup if it displays
        Note: Add 20 seconds to timeout because of loading process
        """
        try:
            self.driver.wait_for_object("tips_capture_popup", timeout=20)
            self.driver.click("tips_capture_popup_ok_btn", change_check={"wait_obj": "tips_capture_popup_ok_btn", "invisible": True})
        except (TimeoutException):
            logging.info("'Tips for Camera Capture' is NOT displayed")

    def select_adjust_next_btn(self):
        """
        Click on Next button
        """
        self.driver.click("adjust_next_btn", change_check={"wait_obj": "adjust_next_btn", "invisible": True}, timeout=10, retry=6)
        self.verify_invisible_crop_enhance_popup()

    def select_adjust_full_option_btn(self):
        """
        Click on full option on Adjust Boundaries screen
        """
        self.driver.wait_for_object("adjust_full_screen_btn")
        self.driver.click("adjust_full_screen_btn")

    def select_x_button(self, timeout=5):
        """
        Click on X button on capture screen
        """
        self.driver.click("x_button", timeout=timeout)

    def select_back_button(self):
        """
        Click the back button. Replaces x button if a capture has already taken place.
        """
        self.driver.click("back_btn")

    def select_settings_button(self):
        """
        Click on Settings button on capture screen
        """
        self.driver.click("settings_button")
    
    def click_photo_mode_btn(self):
        """
        Click on Photo mode button
        """
        self.driver.click("photo_mode_btn")

    def click_batch_mode_btn(self):
        """
        Click on Batch mode button
        """
        self.driver.click("batch_mode_btn")

    def click_document_mode_btn(self):
        """
        Click on Document mode button
        """
        self.driver.click("document_mode_btn")
    
    # --------------------------- Preferences(Gear Icon) ------------------------------- #
    def select_preferences_icon(self):
        """
        Click the gear icon on the top right of camera scan screen
        """
        self.driver.click("settings_button")

    def toggle_preferences_switch(self, preference, on):
        """
        Toggles a setting on the preferences screen to the desired state
        :param preference: The preference to toggle, use * piece of "*_setting" locators. 
            Possible values: "auto_enhancements", "auto_heal", "auto_orientation", "flatten_book_pages"
        :param on: If True toggle preference on, if False toggle off
        """
        if preference == "auto_heal" and on and self.driver.get_attribute("settings_switch", "checked", format_specifier=[self.driver.return_str_id_value("auto_enhancements_setting")]) == "false":
            logging.warning("Cannot toggle Auto-Heal on when Auto-Enhancements is off")
            return False
        desired_state = "true" if on else "false"
        str_id = self.driver.return_str_id_value(preference + "_setting")
        if self.driver.get_attribute("settings_switch", "checked", format_specifier=[str_id]) != desired_state:
            logging.info("Toggling {} to on: {}".format(preference, on))
            self.driver.click("settings_switch", format_specifier=[str_id])
        else:
            logging.info("{} is already toggled on: {}".format(preference, on))
        return True

    # ------------------------------ ID Scan Preview ----------------------------------- #
    def select_id_next_btn(self):
        """Selects the next button on the ID Card Front/Back preview screen"""
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
        """Returns screenshot of id card preview asbase64"""
        return self.driver.screenshot_element("id_preview_img")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_capture_screen(self):
        """
        Verify that current screen is capture screen via:
            - Camera shutter button
            - Camera mode button
        """
        self.driver.wait_for_object("mode_btn")
        self.driver.wait_for_object("shutter_btn")
            
    @screenshot_capture(file_name="camera_screen.png")
    def verify_capture_no_access_screen(self, raise_e=True):
        """
        Verify current screen is capture screen with No Access message via:
            - No Camera message
            - Allow Access button
        :parameter: ga is True or False
        """
        return self.driver.wait_for_object("no_camera_access_title", raise_e=raise_e)

    def verify_camera_permission_access_screen(self):
        """
        Verify current screen is camera access screen with:
            - Allow HP Smart to take pictures and record video
            - Allow button
            - Deny button
        """
        self.driver.wait_for_object("camera_permission_access_popup")
        self.driver.wait_for_object("camera_permission_access_allow_btn")
        self.driver.wait_for_object("camera_permission_access_deny_btn")

    def verify_camera_adjust_screen(self, timeout=20):
        """
        Verify that current screen is adjust screen:
            - Next button   (add 20 seconds to timeout because of loading process after capturing a photo
            - Full screen icon button
        """
        self.driver.wait_for_object("adjust_next_btn", timeout=timeout)
        self.driver.wait_for_object("adjust_full_screen_btn", timeout=timeout)

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

    def verify_invisible_crop_enhance_popup(self):
        """
        Verify that Crop and Enhance popup invisible
        """
        self.driver.wait_for_object("crop_enhance_msg", invisible=True, timeout=30)

    def verify_slider_button_on_capture_screen(self, capture_mode):
        """
        Verify slider menu buttons on capture screen
        :param capture_mode: The capture mode to verify. Possible Values: "photo", "document", "id_card", "book", "multi_item", "batch"
        """
        self.driver.scroll(capture_mode + "_mode_btn", direction="right", scroll_object=self.driver.wait_for_object("scan_mode_recycler"), check_end=False)

    def verify_top_bar_menu_on_capture_screen(self, invisible=True):
        """
        Verify the top bar menu of capture screen through:
        - X button
        - Flash button
        - Settings button
        - Auto button for Batch mode only
        """
        self.driver.wait_for_object("x_button")
        self.driver.wait_for_object("flash_button")
        self.driver.wait_for_object("settings_button")
        self.driver.wait_for_object("auto_btn", invisible=invisible)

    def verify_preference_screen(self):
        """
        Verify that current screen is Preference screen via:
            - Auto-Enhancements
            - Auto- Orientation
        """
        self.driver.wait_for_object("auto_enhancements_setting")
        self.driver.wait_for_object("auto_orientation_setting")

    def verify_bubble_msg(self, msg):
        """
        Verify help bubble is displayed above camera mode slider
        :param msg: The message to verify. Use prefixes of "*_status_txt" locators. 
            Possible Values: "id_back", "id_front", "processing", "center", "center_multiple"
        """
        msg = msg if msg.endswith("_status_txt") else msg + "_status_txt"
        self.driver.wait_for_object("camera_bottom_status_message", format_specifier=[self.driver.return_str_id_value(msg)])
    
    def verify_camera_bottom_status_message(self,timeout=10):
        """
        Verify camera bottom status message
        """
        self.driver.wait_for_object("camera_bottom_status_message", timeout=timeout)

    def verify_rotate_button(self):
        """
        Verify roatate button on preview screen located on right bottom corner of scanned Image
        """
        self.driver.wait_for_object("rotate_image_btn")

    def verify_capture_camera_scan_message(self, raise_e=True):
        """
        Verify Tap here to catpure a camera scan coarchmark message
        """
        return self.driver.wait_for_object("capture_camera_scan_txt", raise_e=raise_e)
    
    def get_capture_mode_text(self,timeout=10):
        """
        Get the text of the current capture mode
        """
        self.driver.wait_for_object("capture_mode", timeout=timeout)
        return self.driver.get_text("capture_mode")

    def get_camera_scan_flash_mode(self,timeout=10):
        """
        Get the text of the current camera scan flash mode
        """
        self.driver.wait_for_object("camera_scan_flash_mode", timeout=timeout)
        return self.driver.get_attribute("camera_scan_flash_mode", "content-desc")

    def click_camera_scan_flash_mode(self,timeout=10):
        """
        Click on the camera scan flash mode button
        """
        self.driver.wait_for_object("camera_scan_flash_mode", timeout=timeout).click()

    def verify_no_camera_access_title(self, timeout=10):
        """
        Verify the no camera access title
        """
        self.driver.wait_for_object("no_camera_access_title", timeout=timeout)

    def get_coarchmark_titles(self, timeout=10, raise_e=True):
        """
        Get the text of the coarchmark titles
        """
        self.driver.wait_for_object("coarchmark_titles", timeout=timeout, raise_e=raise_e)
        return self.driver.get_text("coarchmark_titles")

    def get_coarchmark_status(self, timeout=10, raise_e=True):
        """
        Get the text of the coarchmark status
        """
        self.driver.wait_for_object("coarchmark_status", timeout=timeout, raise_e=raise_e)
        return self.driver.get_text("coarchmark_status")

    def click_coarchmark_next_btn(self, timeout=10, raise_e=True):
        """
        Click on the next button on the coarchmark screen
        """
        self.driver.wait_for_object("coarchmark_next_btn", timeout=timeout, raise_e=raise_e).click()

    def click_coarchmark_back_btn(self, timeout=10, raise_e=True):
        """
        Click on the back button on the coarchmark screen
        """
        self.driver.wait_for_object("coarchmark_back_btn", timeout=timeout, raise_e=raise_e).click()

    def click_coarchmark_close_btn(self, timeout=10, raise_e=True):
        """
        Click on the close button on the coarchmark screen
        """
        self.driver.wait_for_object("coarchmark_close_btn", timeout=timeout, raise_e=raise_e).click()

    def click_camera_scan_source(self, timeout=10, raise_e=True):
        """
        Click on the camera scan source button
        """
        self.driver.wait_for_object("camera_scan_source", timeout=timeout, raise_e=raise_e).click()

    def verify_camera_scan_capture_mode(self, timeout=10, raise_e=True):
        """
        Verify the camera scan capture mode
        """
        self.driver.wait_for_object("capture_mode", timeout=timeout, raise_e=raise_e)
        return self.driver.get_text("capture_mode")

    def verify_auto_is_selected(self, timeout=20):
        """
        Verify the auto is selected
        """
        return self.driver.get_attribute("auto_btn", "selected", timeout=timeout)

    def verify_is_auto_crop_selected_after_scan(self, timeout=10):
        """
        Verify the Auto option is selected
        """
        self.driver.wait_for_object("auto_crop_option_selected", timeout=timeout)
        return self.driver.get_attribute("auto_option_selected","selected")

    def click_full_crop_option(self, timeout=10):
        """
        Click on the full crop option
        """
        self.driver.wait_for_object("full_crop_option_selected", timeout=timeout).click()

    def verify_is_camera_source_selected(self, timeout=10):
        """
        Verify the camera source is selected
        """
        self.driver.wait_for_object("source_camera_scan_area", timeout=timeout)
        return self.driver.get_attribute("source_camera_scan_area","selected")

    def verify_source_files_and_photos(self, timeout=3):
        """
        Verify the source files and photos
        """
        return self.driver.wait_for_object("source_files_and_photos", timeout=timeout)

    def verify_source_camera(self, timeout=3):
        """
        Verify the source camera
        """
        return self.driver.wait_for_object("source_camera", timeout=timeout)

    def click_source_camera(self, timeout=3):
        """
        Click on the source camera
        """
        self.driver.click("source_camera", timeout=timeout)

    def verify_source_camera_printer(self, timeout=3):
        """
        Verify the source camera printer
        """
        return self.driver.wait_for_object("source_camera_printer", timeout=timeout)

    def is_source_camera_scan_area_enabled(self, timeout=10):
        """
        Verify the camera scan area is enabled
        """
        self.driver.wait_for_object("source_camera_scan_area", timeout=timeout)
        return self.driver.find_object("source_camera_scan_area").is_enabled()

    def verify_scan_btn(self, timeout=3):
        """
        Verify the scan button is displayed
        """
        return self.driver.wait_for_object("scan_btn", timeout=timeout)

    def verify_photos_pdfs_btn(self, timeout=3):
        """
        Verify the photos and pdfs button is displayed
        """
        return self.driver.wait_for_object("photos_pdfs_btn", timeout=timeout)

    def click_files_and_photos(self, timeout=3):
        """
        Click on the source files and photos
        """
        self.driver.click("files_and_photos_btn", timeout=timeout)

    def verify_select_scan_source_screen(self, timeout=10, raise_e=True):
        """
        Verify that current screen is select scan source screen via:
            - Camera Scan Source
            - Files and Photos
            - Printer
        :param timeout: The timeout to wait for the screen to load
        :param raise_e: If True, raise an exception if the screen is not found
        """
        return self.driver.wait_for_object("select_scan_source_screen", timeout=timeout, raise_e=raise_e)
    
    def click_camera_scan_source_btn(self, timeout=10, raise_e=True):
        """
        Click on the camera scan source button
        :param timeout: The timeout to wait for the button to be clickable
        :param raise_e: If True, raise an exception if the button is not found
        """
        self.driver.wait_for_object("camera_scan_source", timeout=timeout, raise_e=raise_e).click()
    
    def click_photos_pdfs_btn(self):
        """
        Click on the photos and pdfs button
        """
        self.driver.click("photos_pdfs_btn")

    def click_auto_capture_image(self, timeout=10):
        """
        Click auto capture image
        """
        self.driver.click("auto_capture_image_selected", timeout=timeout)
    
    def verify_auto_capture_image(self, timeout=10):
        """
        Verify auto capture image is selected
        """
        if self.driver.wait_for_object("auto_capture_image_selected", timeout=timeout):
            return True
    
    def click_scan_btn(self):
        """
        Click on the scan button
        """
        self.driver.click("scan_btn")
    
    def click_capture_mode(self):
        """
        Click on the capture mode button
        """
        self.driver.click("capture_mode")

    # *********************************************************************************
    #                                IS FLOWS                                         *
    # *********************************************************************************
    def is_camera_screen(self):
        """
        Verify that current screen is camera screen via shuttle button
        :return: True if it is camera screen. Otherwise, False
        """
        try:
            self.verify_capture_screen()
            return True
        except TimeoutException:
            logging.info("Current screen is not Camera screen")
            return False
