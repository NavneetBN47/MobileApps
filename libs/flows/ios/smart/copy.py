from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Copy(SmartFlow):
    flow_name = "copy"

    START_BLACK_BTN = "start_black_button"
    START_COLOR_BTN = "start_color_button"
    ADD_PAGES_BTN = "add_pages_button"
    COPY_PREVIEW_EXIT_POPUP = "copy_preview_exit_popup"

    COPY_PREVIEW_ELEMENTS = [
        START_BLACK_BTN,
        START_COLOR_BTN,
        ADD_PAGES_BTN,
    ]

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def select_object_size(self, object_size):
        """
        selects the object size for digital copy: we have 6 available options defined in const file
        :param object_size:
        """
        self.driver.click("object_size_btn")
        self.driver.click(object_size)

    def verify_copy_tile_screen(self):
        """
        verify copy tile screen
        """
        self.driver.wait_for_object("object_size_btn")

    def select_flash_button(self):
        """
        clicks the flash button to change the flash mode: ga is dynamic,
        developers need to set the variables to know current flash mode
        """
        self.driver.click("flash_button")

    def select_capture_button(self):
        """
        clicks the capture button to capture the object:
        capture the ga for copy type and also input size from object size selection:
        """
        self.driver.click("capture_button")

    def verify_manual_enabled(self):
        """
        verify manual button enabled
        """
        self.driver.click("manual_enabled")

    def select_add_more_pages(self):
        """
        it will click the small plus button on right corner of preview
        so we will add more copies to same JOB:
        GA added:
        """
        self.driver.click("add_pages_button")

    def select_number_of_copies(self, change_copies=1):
        """
        selects the number of copies from small tray table:
        """
        self.driver.click("copies_tray_button")
        self.driver.scroll("copies_table", format_specifier=[change_copies], check_end=False, click_obj=True)

    # TODO: taking time to select, try to minimize execution time, so commented temporarily
    # tile_switches = self.driver.find_object("chane_copies_val_2", multiple=True)
    # logging.info("Number of UIAELEMENTS: {}".format(len(tile_switches)))
    # print("1")
    # for tile_switch in tile_switches:
    #     switch_name = tile_switch.get_attribute("name")
    #     tile_switch_value = tile_switch.get_attribute("value")
    #     if tile_switch_value == change_copies:
    #         logging.info("Enabling [{}]. Clicking toggle!".format(switch_name))
    #         tile_switch.click()
    #         break
    # self.driver.scroll(str(change_copies), scroll_object="copies_table")

    def select_resize_in_digital_copy(self, resize):
        """
        selects the resize option: from available:: defined in const file
        """
        self.driver.click("resize_tray_button")
        self.driver.click(resize)

    def verify_start_color(self, timeout=20, raise_e=True):
        """
        clicks the start color button: it adds the GA for three things
            1) no of copies 2) resize type 3) color or black
        """
        return self.driver.wait_for_object("start_color_button", timeout=timeout, raise_e=raise_e)

    def select_start_color(self):
        """
        clicks the start color button: it adds the GA for three things
            1) no of copies 2) resize type 3) color or black
        """
        self.driver.click("start_color_button")
    
    def verify_start_black(self, raise_e=True):
        """
        clicks the start black button: it adds the GA for three things
            1) no of copies 2) resize type 3) color or black
        """
        return self.driver.wait_for_object("start_black_button", raise_e=raise_e)

    def select_start_black(self):
        """
        clicks the start black button: it adds the GA for three things
            1) no of copies 2) resize type 3) color or black
        """
        self.driver.click("start_black_button")

    def select_enable_access_to_camera_link_text(self):
        """
        clicks on enable access to camera button on the camera not allowed screen, to go manual settings page
        """
        self.driver.click("enable_access_to_camera_link_txt")

    def enable_camera_access_toggle_in_settings(self):
        """
        clicks the toggle on in settings page to enable access to camera:
        """
        self.driver.click("toggle_on_camera_access_system_ui")

    def select_settings_back_button(self):
        """
        clicks the settings button to go back to hp smart app from manual settings page:
            some times we may require in future:
        """
        self.driver.click("settings_back_btn")

    def select_x_to_close(self):
        """
            clicks the X button on copy screen to close current and go back to home with out taking capture
        """
        self.driver.click("x_btn_on_copy")

    def select_auto_capture(self):
        """
        Select Auto option on camera screen to capture automatically: we have manual and auto button
        """
        self.driver.click("auto_btn")

    def select_manual_button(self):
        """
        Select manual option on camera screen to capture automatically: we have manual and auto button
        """
        self.driver.click("Manual_btn")

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_copy_screen(self):
        """
        Verifies the copy screen with flash button:
        """
        self.driver.wait_for_object("capture_button")

    def select_copy_scanned_pages(self):
        """
        select the copy screen with flash button:
        """
        self.driver.wait_for_object("scanned_pages")
        self.driver.click("scanned_pages")

    def verify_copy_preview_screen(self):
        """
        verifies the preview screen after capture:
        """
        self.driver.wait_for_object("Digital_copy_preview_title")

    def verify_enable_access_to_camera_screen(self):
        """
        Verify the camera not allowed screen: will find the enable access to camera link to go manual settings page
        """
        self.driver.wait_for_object("enable_access_to_camera_link_txt")
    
    def select_ok_btn(self):
        """
        Click on OK button on pop-up
        """
        if self.driver.wait_for_object("_shared_str_ok", raise_e=False):
            self.driver.click("_shared_str_ok")

    def verify_copy_preview_screen_exit_popup(self):
        self.driver.wait_for_object("copy_preview_exit_popup")
        self.driver.wait_for_object("copy_preview_popup")

    def verify_manual_button(self):
        """
        Verify manual option on camera screen to capture automatically: we have manual and auto button
        """
        if self.driver.wait_for_object("manual_enabled"):
            return True
        else:
            return False
        
    def verify_auto_button(self):
        """
        Verify Auto option on camera screen to capture automatically: we have manual and auto button
        """
        if self.driver.wait_for_object("auto_enabled"):
            return True
        else:
            return False
 
    def select_resize_and_verify_options(self):
        """
        Click on resize button and verify the resize options are displayed
        """
        self.driver.click("resize_tray_button")
        self.driver.wait_for_object("_shared_original_size")
        self.driver.wait_for_object("_shared_fit_to_page")
        self.driver.wait_for_object("_shared_fill_page")