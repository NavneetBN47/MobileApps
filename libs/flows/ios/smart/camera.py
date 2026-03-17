import logging
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from MobileApps.resources.const.ios.const import FLASH_MODE

class Camera(SmartFlow):
    flow_name = "camera"

    OPTION_FILES = "files_and_photos_str"
    OPTION_CAMERA = "camera_str"
    OPTION_SCANNER = "scanner_str"

    POPUP_UNSAVED_PAGES = "unsaved_pages_popup"
    POPUP_EXIT_WITHOUT_SAVING = "exit_without_saving_popup"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def select_camera_option_to_scan(self):
        """
            selects the camera option on scan screen:its on scan screen not from first time popup with scanner or camera
        :return:
        """
        self.driver.click("camera_btn")

    def select_allow_access_to_camera_on_popup(self, allow_access=True):
        """
            verifies the allow access to camera popup is present/not,if present based on param value it gives the access
        :param allow_access: True default, if you want to check no access screen , allow_access = False:
        :return:
        """
        try:
            if self.driver.wait_for_object("allow_camera_access_popup", timeout=20):
                if allow_access:
                    self.driver.click("allow_ok")
                else:
                    self.driver.click("dont_allow")
        except TimeoutException:
            logging.info("Current Screen did NOT contain the Allow access camera pop up")

    def verify_allow_access_to_camera_popup(self):
        """
        verify the allow access to camera popup
        """
        self.driver.wait_for_object("allow_camera_access_popup")

    def select_capture_btn(self):
        """
        Selects the camera button
        :return:
        """
        self.driver.click("capture_btn")

    def select_adjust_boundaries_next(self, timeout=10):
        """
        Select the next button on the adjust boundaries screen
        """
        self.driver.click("next_btn", timeout=timeout)
    
    def select_adjust_boundaries_full(self):
        """
        Selects the full button on the adjust boundaries screen
        """
        self.driver.click("full_boundary_btn")

    def select_manual_option(self):
        """
        Select Manual option on camera screen
        """
        if not self.verify_manual_capture_mode():
            self.select_auto_btn()

    def select_auto_option(self):
        if not self.verify_auto_capture_mode():
            self.select_auto_btn()

    def select_auto_btn(self):
        self.driver.click("auto_btn")

    def select_gear_setting_btn(self):
        self.driver.click("scan_setting_gear")

    def select_allow_access_to_unsaved_pages_popup(self, allow_save=True):
        if self.driver.wait_for_object("unsaved_pages_popup"):
            if allow_save:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_yes")])
            else:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_no")])

    def select_exit_without_saving_popup(self, allow_save=True):
        if self.driver.wait_for_object("exit_without_saving_popup"):
            if allow_save:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_yes")])
            else:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_no")])

    def select_camera_enabled(self):
        if self.driver.get_attribute(obj_name="camera_toggle_btn", attribute="value") == u'0':
            self.driver.click("camera_toggle_btn")

    def select_flash_mode(self, mode, cycle_attempts=2):
        clicks = 0
        while self.driver.wait_for_object(mode, raise_e=False) is False:
            self.driver.click("flash_btn")
            time.sleep(2)
            clicks += 1
            if clicks//len([attr for attr in dir(FLASH_MODE) if not attr.startswith("__")]) >= cycle_attempts:
                break

    def select_enable_access_to_camera_link(self):
        self.driver.click("enable_access_to_camera_text")

    def select_return_to_hp_smart_btn(self):
        self.driver.wait_for_object("return_to_hp_smart_btn")

    def select_return_to_hp_smart(self):
        self.driver.click("return")

    def select_return_to_hp_smart_r(self):
        self.driver.click("return_a")

    def select_return_to_hp_smart_b(self):
        self.driver.click("return_b")

    def select_return_to_hp_smart_c(self):
        self.driver.click("return_c")

    def select_auto_enhancements(self):
        self.driver.click("auto_enhancements")

    def select_auto_heal(self):
        self.driver.click("auto_heal")

    def select_auto_orientation(self):
        self.driver.click("auto_orientation")

    def select_auto_image_collection_view(self):
        """
        clicks the image collection icon that appears on top right of the Camera screen during auto capture
        :return:
        """
        self.driver.click("auto_image_collection_view", timeout=10, interval=1)

    def select_source_button(self, timeout=10):
        """

        :return:
        """
        self.driver.click("source_btn", timeout=timeout)

    def clear_tips_pop_up(self):
        """
        After launching camera, close the tips and tricks pop up notification if it's present
        """
        if self.driver.wait_for_object("close_tips_pop_up", raise_e=False, timeout=3):
            self.driver.click("close_tips_pop_up")

    def select_files_and_photos_option(self):
        """
        After selecting source option select the Files and Photos option
        """
        self.driver.click("files_and_photos_source_option")

    def return_number_of_images(self):
        """
        verifies the number of images captured
        :param no_of_images: default value is 2
        :return:
        """
        return int(self.driver.get_attribute("auto_image_collection_view", "value"))

    def select_source_option(self, option, printer_name=None):
        if option == self.OPTION_SCANNER:
            if not printer_name:
                raise ValueError("printer_name is required for scanner option")
            printer_name = self.format_printer_name_for_scanner_source(printer_name)
            self.driver.click(self.OPTION_SCANNER, format_specifier=[printer_name])
        else:
            self.driver.click(option)

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_adjust_boundaries_nav(self):
        """
        Verify Adjust Boundaries naviagation bar:

            - Adjust Boundaries title

        Device: Phone
        """
        self.driver.wait_for_object("adjust_boundaries_title")

    def verify_full_boundary_btn(self):
        """
        Verify full boundary button
        """
        self.driver.wait_for_object("full_boundary_btn")

    def verify_auto_boundary_btn(self):
        """
        Verify auto boundary button
        """
        self.driver.wait_for_object("auto_boundary_btn")

    def verify_allow_access_to_camera_text(self):
        """
        Verify text for allow access to the camera
        """
        self.driver.wait_for_object("allow_access_to_camera_text")

    def verify_enable_access_to_camera_link(self):
        """
        Verify the link to enable camera access
        """
        self.driver.wait_for_object("enable_access_to_camera_text")

    def verify_aio_needs_access_to_camera_text(self):
        """
        Verify text
        """
        self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[
            self.get_text_from_str_id("aio_needs_access_to_camera_text").replace("%@", self.get_ios_device_type())])

    def verify_camera_screen(self, timeout=20, raise_e=True):
        """
        determines which type is selected and counts it
        :return: strings for AUTO or MANUAL
        """
        return self.driver.wait_for_object("capture_btn", timeout=timeout, raise_e=raise_e)

    def verify_camera_btn(self):
        self.driver.wait_for_object("capture_btn")

    def verify_auto_btn(self):
        self.driver.wait_for_object("auto_btn")

    def verify_manual_btn(self):
        self.driver.wait_for_object("manual_btn")

    def verify_auto_capture_mode(self):
        '''
            auto capture mode is enabled if auto_btn have a value attribute equal to 1
        '''
        return self.driver.get_attribute("auto_btn", "value") == "1"

    def verify_manual_capture_mode(self):
        '''
            "Auto" button is disabled if auto_btn does not have a value attribute (default)
        '''
        return self.driver.get_attribute("auto_btn", "value") is None

    def verify_flash_btn(self):
        self.driver.wait_for_object("flash_btn")

    def verify_flash_mode_state(self, mode):
        if mode == FLASH_MODE.FLASH_OFF:
            if not self.driver.wait_for_object("default_flash_off", raise_e=False):
                logging.info("Flash not in given {} mode".format(mode))
        elif not self.driver.wait_for_object(mode, raise_e=False):
            logging.info("Flash not in given {} mode".format(mode))

    def verify_auto_enhancements(self):
        self.driver.wait_for_object("auto_enhancements")

    def verify_auto_heal(self):
        self.driver.wait_for_object("auto_heal")

    def verify_auto_orientation(self):
        self.driver.wait_for_object("auto_orientation")

    def verify_back_button(self):
        self.driver.wait_for_object("back_btn")

    def verify_adjust_boundaries_next_button(self):
        self.driver.wait_for_object("next_btn")

    def verify_allow_hp_smart_to_access_camera_screen(self):
        self.driver.wait_for_object("allow_hp_smart_access_camera")

    def verify_camera_adjust_text_to_capture_image(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("camera_adjust_text", timeout=timeout, raise_e=raise_e)

    def verify_source_button(self):
        self.driver.wait_for_object("source_btn")

    def verify_source_options(self, scanner=False, printer_name=None):
        if scanner:
            self.driver.wait_for_object(self.OPTION_SCANNER, format_specifier=[printer_name])
        self.driver.wait_for_object(self.OPTION_FILES)
        self.driver.wait_for_object(self.OPTION_CAMERA)

    def return_capture_image(self):
        return saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())

    def capture_multiple_photos_by_auto_mode(self, no_of_images=2, timeout=30, device_name=None):
        # multiple photos will take longer than 10 sec
        timeout = time.time() + timeout
        while time.time() < timeout:
            try:
                try:
                    captured_images = self.driver.get_attribute(obj_name="auto_image_collection_view", attribute='value')
                except TimeoutException:
                    if not device_name:
                        raise TimeoutException("Images are not being captured! Camera is either blocked by something or can't detect the paper for some reason!")
                    else:
                        raise TimeoutException(f"Images are not being captured! Check {device_name}'s camera or the paper in front of it!")
                if int(captured_images) >= no_of_images:
                    logging.info("no of pages {}".format(int(captured_images)))
                    self.select_auto_btn()
                    self.driver.click("auto_image_collection_view", delay=5)
                    break
                else:
                    time.sleep(5)
            except (NoSuchElementException, ValueError):
                continue

    def verify_popup_message(self, popup_title):
        self.driver.wait_for_object(popup_title)
        self.driver.wait_for_object("_shared_no")
        self.driver.wait_for_object("_shared_yes")

    def verify_capture_preference_screen(self, raise_e=True):
        return self.driver.wait_for_object("capture_preference", raise_e=raise_e)

    def verify_adjust_scan_coach_mark(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("adjust_scan_coach_mark", timeout=timeout, raise_e=raise_e)

    def verify_preset_coach_mark(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("camera_preset_coach_mark", timeout=timeout, raise_e=raise_e)

    def verify_capture_coach_mark(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("camera_capture_coach_mark", timeout=timeout, raise_e=raise_e)

    def verify_source_coach_mark(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("camera_source_coach_mark", timeout=timeout, raise_e=raise_e)

    def verify_gear_setting_btn(self):
        self.driver.wait_for_object("scan_setting_gear")

    def verify_id_front(self):
        self.driver.wait_for_object("id_front")
    
    def verify_id_back(self):
        self.driver.wait_for_object("id_back")

########################################################################################################################
#                                                                                                                      #
#                                                  Functionality Related sets
#                                                                                                                      #
########################################################################################################################

    def capture_manual_photo_by_camera(self, mode=FLASH_MODE.FLASH_OFF):
        """
        manual capture and skips adjust boundary screen
        :return:
        """
        if self.verify_second_close_btn():
            self.select_second_close_btn()
        self.select_manual_option()
        self.select_flash_mode(mode)
        self.select_capture_btn()
        time.sleep(1)
        self.verify_adjust_boundaries_nav()
        self.select_adjust_boundaries_next()

    def verify_top_bar(self):
        self.verify_close()
        self.verify_flash_mode_state(FLASH_MODE.FLASH_OFF)
        self.verify_gear_setting_btn()

    def verify_bottom_bar(self, acc_type="normal"):
        self.verify_source_button()
        self.verify_preset_sliders(acc_type=acc_type)
        self.verify_camera_btn()

    def verify_camera_ui_elements(self, acc_type="normal"):
        self.verify_top_bar()
        self.verify_camera_adjust_text_to_capture_image()
        self.verify_bottom_bar(acc_type=acc_type)

    def verify_camera_ui_elements_for_copy_functionality(self):
        self.verify_camera_btn()
        self.verify_auto_btn()
        self.verify_manual_btn()
        self.verify_flash_mode_state(FLASH_MODE.FLASH_OFF)
        self.verify_close()

    def verify_adjust_boundaries_ui_elements(self):
        self.verify_adjust_boundaries_nav()
        self.verify_adjust_boundaries_next_button()
        self.verify_back_button()
        self.verify_auto_boundary_btn()
        self.verify_full_boundary_btn()

    def verify_allow_access_to_camera_ui_elements(self):
        self.verify_close()
        self.verify_aio_needs_access_to_camera_text()
        self.verify_enable_access_to_camera_link()
        self.verify_allow_access_to_camera_text()

    def verify_capture_preference_options(self):
        self.verify_auto_enhancements()
        # self.verify_auto_heal()
        self.verify_auto_orientation()

    def verify_preset_default_capture_mode(self):
        self.verify_preset_mode(self.PHOTO)
        self.verify_manual_capture_mode()
        self.verify_preset_mode(self.BATCH)
        self.verify_auto_capture_mode()
        self.verify_preset_mode(self.DOCUMENT)
        self.verify_manual_capture_mode()

    def capture_id_card_by_camera(self):
        self.verify_camera_screen()
        self.select_preset_mode(self.ID_CARD)
        self.verify_id_front()
        self.select_capture_btn()
        self.verify_id_back()
        self.select_capture_btn()

    def verify_source_menu_ui(self):
        """
        Verify the source menu on the camera screen
        """
        self.driver.wait_for_object("files_and_photos_source_option")
        self.driver.wait_for_object("source_camera")

    def verify_default_capture_mode(self, capture_mode="Manual"):
        """
        Verify default capture mode
        """
        if capture_mode== "Auto":
            self.verify_auto_capture_mode()
        elif capture_mode== "Manual":
            self.verify_manual_capture_mode()

    def verify_batch_ui(self, single_element=None):
        """
        Verify batch mode UI
        """
        if single_element == True:
            return self.driver.wait_for_object("search_text", timeout=10)
        else:
            return (
                self.driver.wait_for_object("search_text", timeout=10),
                self.driver.wait_for_object("scanning_text", timeout=10),
                self.driver.wait_for_object("processing_text", timeout=10)
            )

    def select_and_verify_flash_mode(self, mode=FLASH_MODE.FLASH_OFF):
        """
        Selects the flash mode and verifies it
        """
        self.select_flash_mode(mode)
        self.verify_flash_mode_state(mode)

    def verify_source_menu_ui(self):
        """
        Verify the source menu on the camera screen
        """
        self.driver.wait_for_object("files_and_photos_source_option")
        self.driver.wait_for_object("source_camera")

    def verify_camera_source_mode_selected(self):
        """
        Verify the camera source mode
        """
        self.driver.wait_for_object("source_camera")

    def click_images_on_camera_scan_batch_mode(self):
        """
        Verify the camera source mode
        """
        self.driver.click("batch_scan_image")
    
    def verify_and_select_flash_mode(self, desired_mode, max_attempts=4):
        """
        Selects the flash mode
        """
        for _ in range(max_attempts):
            if self.driver.wait_for_object(desired_mode, raise_e=False):
                return  # Desired mode is active; stop here
            self.driver.click("flash_btn")  # Cycle to the next mode

    def select_close_x_btn(self):
        """
        Selects the close button on the camera screen
        """
        self.driver.click("hpx_close_x_btn")