import logging
import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow


class Home(SmartFlow):
    flow_name = "home"
    NAV_PRINTER_SCAN_BTN = "nav_printer_scan_btn"
    NAV_CAMERA_SCAN_BTN = "nav_camera_scan_btn"
    NAV_VIEW_PRINT_BTN = "nav_view_print_btn"
    NAV_APP_SETTINGS_BTN = "nav_app_settings"
    NAV_CREATE_ACCOUNT_BTN = "nav_create_account"
    NAV_SIGN_IN_BTN = "sign_in_btn"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_tile_by_name(self, tile_name, is_permission=True, check_printer=False):
        """
        Description: Click on tile icon button via tile's name
        :param tile_name: tile name on screen. Using constant variable from flow_container -> TILE_NAMES to get strings
        :param is_permission: True/False ->
        """
        self.__scroll_to_top_home_screen(check_printer=check_printer)
        self.driver.scroll("tile_title", direction="down", format_specifier=[tile_name], timeout=20, check_end=False, full_object=True)
        # swipe again if tile_title's bottom edge is below the bottom navbar
        title_rect = self.driver.wait_for_object("tile_title", format_specifier=[tile_name]).rect
        if title_rect["y"] + title_rect["height"] > self.driver.wait_for_object("bottom_navbar").rect["y"]:
            self.driver.swipe(direction="down", per_offset=0.7)
        self.driver.click("tile_title", format_specifier=[tile_name], change_check={"wait_obj": "notification_btn", "invisible": True})
        if is_permission:
            self.check_run_time_permission()

    def select_personalize_tiles(self):
        """
        Click on Personalize Tiles button
        """
        self.driver.scroll("personalize_tile_btn", timeout=20, click_obj=True, full_object=True)

    def select_notifications_icon(self):
        """
        Select notification bell icon on Home screen
        Steps:
            - Click on notification bell icon button
        End of flow: Notifications detail screen
        """
        self.driver.click("notification_btn")

    def select_bottom_nav_btn(self, btn, is_permission=True):
        """
        Click on a bottom navigation btn
        :param btn: constant class:
                NAV_PRINTER_SCAN_BTN
                NAV_CAMERA_SCAN_BTN
                NAV_VIEW_PRINT_BTN
                NAV_APP_SETTINGS_BTN
                NAV_CREATE_ACCOUNT_BTN
                NAV_SIGN_IN_BTN
        :param is_permission:
        """
        self.driver.click(btn, change_check={"wait_obj":"notification_btn", "invisible": True})
        if is_permission and btn != self.NAV_APP_SETTINGS_BTN:
            self.check_run_time_permission()

    def select_feature_popup_close(self):
        """
        Click on 'x' button on "Print anywhere, anytime!" popup
        """
        self.driver.click("feature_popup_close_btn")

    def select_deny_confirmation_popup_allow(self):
        """
        Click on ALLOW button on Deny Confirmation popup
        """
        self.driver.click("deny_permission_confirmation_popup_allow_btn")

    def select_deny_confirmation_popup_deny(self):
        """
        Click on Deny button on Deny Confirmation popup
        """
        self.driver.click("deny_permission_confirmation_popup_deny_btn")

    def select_deny_confirmation_popup_go_back(self):
        """
        Click on Go Back button on Deny Confirmation popup
        """
        self.driver.click("deny_permission_confirmation_popup_go_back_btn")

    def select_deny_confirmation_go_back_deny_btn(self):
        """
        Click on DENY button on permission confirmation popup screen
        """
        self.driver.click("deny_permission_confirm_go_back_deny_btn")

    def dismiss_feature_unavailable_popup(self, is_checked=True):
        """
        Verify Feature Unavailable popup with:
           - Title
           - Message
        Then click OK button to dismiss feature unavailable popup
        :param is_checked:
        """
        if is_checked:
            self.driver.wait_for_object("feature_unavailable_title")
            self.driver.wait_for_object("feature_unavailable_popup_msg")
        self.driver.click("feature_unavailable_popup_btn")

    def dismiss_photomyne_awareness_popup(self):
        """
        Click on No Thanks button on Photomyne enable awareness screen
        """
        self.driver.click("photomyne_no_thanks_btn")

    def dismiss_print_anywhere_popup(self):
        """
        Click on x icon button to close print anywherepopup if it display
        """
        if self.driver.wait_for_object("print_anywhere_popup_optimize_printers_btn", timeout=15, raise_e=False):
            self.driver.click("print_anywhere_popup_close_btn")
            
    # ----------------      More Options buttons        ------------------------
    def select_more_options(self):
        """
        Click on 3 dots icon button on Home screen
        Note: based on manufacture of device, the value for this str_id of this element is mis-matched
        End of flow: popup of More Option
        """
        self.driver.wait_for_object("nav_btns_layout", timeout=10)
        layout = self.driver.find_object("nav_btns_layout")
        try:
            self.driver.find_object("more_options_btn", index=-1, root_obj=layout).click()
        except NoSuchElementException:
            logging.info("Failed to click on more option button. Click again 1 time")
            self.driver.find_object("more_options_btn", index=-1, root_obj=layout).click()

    def select_more_options_help_center(self):
        """
        Select Help Center in More Options menu on Home screen
        Steps:
            - Click on 3 dots icon button
            - Click on Help Center
        End of flow: Help Center screen
        """
        self.select_more_options()
        self.driver.wait_for_object("more_option_help_center")
        self.driver.click("more_option_help_center")

    def select_more_options_about(self):
        """
        Select About in More Options menu on Home screen
        Steps:
            - Click on 3 dots icon button
            - CLick on About button
        End of flow: About screen
        """
        self.select_more_options()
        self.driver.wait_for_object("more_options_about_btn", timeout=5)
        self.driver.click("more_options_about_btn")

    def select_more_options_app_settings(self):
        """
        Select App Settings in More Options menu on Home screen
        Steps:
            - Click on 3 dots icon button
            - Click on App Settings button
        End of flow: App Settings
        """
        self.select_more_options()
        self.driver.wait_for_object("more_options_app_settings_btn", timeout=5)
        self.driver.click("more_options_app_settings_btn")

    def select_more_options_debug_settings(self):
        """
        Click on Debug Settings button in More Option menu
        Steps:
            - Click on 3 dots icon button
            - Click on Debug Settings button
        End of flow: Settings
        """
        self.select_more_options()
        self.driver.wait_for_object("more_options_debug_settings", timeout=5)
        self.driver.click("more_options_debug_settings")

    # ----------------      Printers area        ------------------------
    def load_printer_selection(self):
        """
        Load to Printer Selection screen via:
            - Scroll up to top of Home screen
            - Click on Select a Printer text if no printer is connected
              or click on Printer Found Image (layout) -> Click on Select Different Printer button
        End of flow: Printer Selection screen
        """
        try:
            self.select_nav_add_icon()
        except (TimeoutException, NoSuchElementException):
            self.select_big_add_icon()

    def load_printer_info(self):
        """
        Precondition: A target printer is selected.
        Load to My Printer Info screen via:
            - Click on connected printer image
        End of flow: My Printer screen
        """
        self.__scroll_to_top_home_screen()
        self.driver.click("printer_found_layout", change_check={"wait_obj": "printer_found_layout", "invisible": True})

    def select_set_up(self):
        """
        Click on Set Up button
        :param raise_e: raise TimeoutException if it is not existed for clicking
        """
        self.__scroll_to_top_home_screen()
        self.driver.click("set_up_btn", change_check={"wait_obj": "set_up_btn", "invisible": True})

    def long_press_printer(self):
        """
        Long press printer icon on Home screen
        """
        self.__scroll_to_top_home_screen()
        self.driver.long_press("printer_info_left_area")

    def select_printer_information(self):
        """
        Click on Printer Information button
        """
        self.driver.click("printer_info_btn")

    def select_forget_this_printer(self, is_remote_printer=False):
        """
        Click on Forget This Printer button
        """
        change_check = {"wait_obj": "forget_this_printer_btn", "invisible": True} if not is_remote_printer else False
        self.driver.click("forget_this_printer_btn",change_check=change_check)
        if is_remote_printer:
            self.verify_hide_this_printer_popup()
            self.driver.click("forget_this_printer_btn",change_check={"wait_obj": "forget_this_printer_btn", "invisible": True})
        if "active_printer_serial" in self.driver.session_data["smart_state"]:
            del self.driver.session_data["smart_state"]["active_printer_serial"]

    def select_estimated_supply_levels(self):
        """
        Click on Estimated Supply Levels on Home screen
        """
        self.driver.click("printer_supply_lv")

    def select_ok_button(self):
        """
        Click on OK button on change printer certificate screen
        """
        self.driver.click("ok_btn")

    def remove_loaded_printers(self, timeout=40):
        """
        Removes printers from home printer carousel until no printer remain
        1. Scroll to top of home screen
        2. While carousel counter text is visible
         - If on first item in carousel swipe right(first item is always the add printer button)
         - else long press printer in carousel and select Hide printer
        """
        end_time = time.time() + timeout
        self.__scroll_to_top_home_screen()
        carousel_counter = self.driver.find_object("printer_carousel_counter_txt", raise_e=False)
        while carousel_counter:
            if time.time() > end_time:
                raise TimeoutException("Printer removal timed out.")
            if carousel_counter.text.strip().split(" ")[0] == "1":
                self.driver.swipe(swipe_object="printer_info_container", direction="right", swipe_duration=300)
            else:
                self.driver.long_press("printer_info_left_area")
                self.driver.click("forget_this_printer_btn", delay=0.5)
            time.sleep(0.5)
            carousel_counter = self.driver.find_object("printer_carousel_counter_txt", raise_e=False)
        if "active_printer_serial" in self.driver.session_data["smart_state"]:
            del self.driver.session_data["smart_state"]["active_printer_serial"]

    # ----------------      TILES      ------------------------
    def get_tile_titles(self):
        """
        Get all title of visible tiles
        :return: list of title of tiles
        """
        self.__scroll_to_top_home_screen()
        self.driver.wait_for_object("tile_frame")
        tile_names = []
        timeout = time.time() + 60
        while time.time() < timeout:
            tiles = self.driver.find_object("tile_title", multiple=True)
            for each in tiles:
                title = each.text
                if title not in tile_names:
                    tile_names.append(title)
                    logging.info("Tile Name: {}".format(title))
            if self.driver.wait_for_object("personalize_tile_btn", timeout=5, raise_e=False):
                break
            else:
                self.driver.swipe(direction="down", check_end=False)
        return tile_names

    def select_big_add_icon(self):
        """
        Click on big "+" button on Home screen
        """
        self.__scroll_to_top_home_screen()
        self.driver.wait_for_object("add_printer_btn", timeout=10)
        self.driver.click("add_printer_btn", change_check={"wait_obj": "add_printer_btn", "invisible": True})

    def select_nav_add_icon(self):
        """
        Click on "+" button on the top of navigation
        """
        try:
            self.driver.click("add_printer_nav_btn", change_check={"wait_obj": "add_printer_nav_btn", "invisible": True})
        except (NoSuchElementException, StaleElementReferenceException):
            logging.info("Failed to click on add printer button. Click again 1 time")
            self.driver.click("add_printer_nav_btn", change_check={"wait_obj": "add_printer_nav_btn", "invisible": True})

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_home_nav(self, timeout=10, raise_e=True):
        """
        Verify navigation bar on Home screen
            - Notification button
        Device: Phone
        """
        return self.driver.wait_for_object("splash_item", timeout=timeout/2, raise_e=raise_e, invisible=True) is not False and \
                self.driver.wait_for_object("notification_btn", timeout=timeout/2, raise_e=raise_e) is not False
            
    def verify_home_nav_add_printer_icon(self, invisible=False):
        """
        Check add icon on navigation bar
        """
        self.driver.wait_for_object("add_printer_nav_btn", timeout=10, invisible=invisible)

    def verify_nav_logo(self, timeout=20):
        """
        Verifies the navbar logo that appears on the top navbar for hp+ and ucde accounts. When image appears non-basic(hp+/ucde) hpid entitlements have been applied.
        """
        self.driver.wait_for_object("nav_logo_img", timeout=timeout)

    def verify_add_new_printer(self, invisible=False):
        """
        Verify:
            + "Add Your First Printer" txt
        Note: It is displayed at first time launch and disappear after selecting a printer
        """
        self.__scroll_to_top_home_screen()
        self.driver.wait_for_object("add_first_printer_txt", invisible=invisible)

    def verify_ready_printer_status(self, raise_e=True):
        """
        Check whether printer is ready for testing
        """
        return self.driver.wait_for_object("printer_connected_status", raise_e=raise_e)

    def verify_unavailable_printer_status(self, raise_e=True):
        """
        Verify Printer status is unavailable
        """
        return self.driver.wait_for_object("printer_unavailable_status", raise_e=raise_e)

    def verify_home_no_printer_connected(self):
        """
        Verify that there is no printer connected via:
            - Error message "Not connected to a printer"
        """
        self.__scroll_to_top_home_screen()
        self.driver.wait_for_object("add_printer_btn")

    def verify_loaded_printer(self, raise_e=True):
        """
        Verify that a printer is loaded via:
            - printer's supply display (take longer time than other elements of printer)
            - selected printer's ip matched target printer's ip if printer_ip is not empty
        :param printer_ip: printer's ip address
        """
        try:
            # Make sure current screen is always on top of Home screen
            self.__scroll_to_top_home_screen()
            if not self.driver.wait_for_object("printer_process_icon", invisible=True, timeout=20, raise_e=False):
                self.driver.swipe(direction="up")           # refresh screen
                self.driver.wait_for_object("printer_process_icon", invisible=True, timeout=20)
            if not self.driver.wait_for_object("printer_supply_lv", timeout=15, raise_e=False):
                self.driver.wait_for_object("set_up_btn")
            return True
        except (TimeoutException, NoSuchElementException)as ex:
            if raise_e:
                raise ex
            return False

    def verify_tile(self, tile_name, invisible=False, raise_e = True):
        """
        Verifying visible tile on Home screen
        :param tile_name: tile name on screen. Using constant variable from flow_container -> TILE_NAMES to get strings
        :param ga:
        """
        self.__scroll_to_top_home_screen()
        error_msg = ""
        try:
            self.driver.scroll("tile_title", direction="down", format_specifier=[tile_name], timeout=30,
                               check_end=False)
            self.driver.wait_for_object("tile_title", format_specifier=[tile_name])
            if invisible:
                error_msg = u"{} displayed on screen".format(tile_name)
        except NoSuchElementException as ex:
            if not invisible:
                error_msg = ex.msg
        if error_msg:
            if raise_e:
                raise NoSuchElementException (error_msg)
            else:
                return False
        return True

    def verify_more_options(self):
        """
        Verify the contents of More option button (three dots) on Home screen via buttons:
            - Help Center
            - App Settings
            - About
            - Debug Settings
        :return:
        """
        self.driver.wait_for_object("more_option_help_center")
        self.driver.wait_for_object("more_options_app_settings_btn")
        self.driver.wait_for_object("more_options_about_btn")
        self.driver.wait_for_object("more_options_debug_settings")

    def verify_feature_popup(self, raise_e=True):
        """
        Verify current popup is for a feature (Print Anywhere, Smart Task, etc...) depend on connected printer
        :param raise_e:
        """
        return self.driver.wait_for_object("feature_popup_close_btn", timeout=5, raise_e=raise_e) and \
               self.driver.wait_for_object("feature_popup_get_started_btn", timeout=5, raise_e=raise_e)

    def verify_deny_confirmation_popup(self):
        """
        Verify current popup is confirmation for deny permission
        """
        self.driver.wait_for_object("deny_permission_confirmation_popup_deny_btn", timeout=5)
        self.driver.wait_for_object("deny_permission_confirmation_popup_go_back_btn", timeout=5)

    def verify_do_not_ask_checkbox(self):
        """
        Verify "Don't ask again" checkbox on permission popup screen
        """
        if int (self.driver.driver_info["platformVersion"].split(".")[0]) <= 9:
            self.driver.wait_for_object("deny_permission_confirm_popup_do_not_ask_checkbox", timeout=15)
        else:
            self.driver.wait_for_object("deny_do_not_again_btn", timeout=15)

    def verify_notification_screen(self):
        """
        Verify notification screen
        """
        self.driver.wait_for_object("notification_title")

    def verify_setup_btn(self, invisible=True, raise_e=True):
        """
        After selecting printer, verify setup button invisible or not
        :return:
        """
        return self.driver.wait_for_object("set_up_btn", timeout=30, invisible=invisible, raise_e=raise_e)

    def verify_photomyne_awareness_popup(self, raise_e=True):
        """
        Verify current popup is for Photomyne awarenemss with below item:
         - Message "By tapping Try Photomyne, you will be taken to the Photomyne application....."
         - No Thanks button
        :param raise_e:
        """
        return self.driver.wait_for_object("photomyne_enable_popup_msg", timeout=10, raise_e=raise_e) and \
               self.driver.wait_for_object("photomyne_no_thanks_btn", timeout=10, raise_e=raise_e)

    def verify_printer_model_name(self, bonjour_name, invisible=True, raise_e=True, timeout=10):
        """
        Verify Printer bonjour name is on Printer section
        """
        return self.driver.wait_for_object("printer_model_name_text", format_specifier=[bonjour_name],invisible=invisible, raise_e=raise_e, timeout=timeout)
    
    def verify_long_press_printer_popup(self):
        """
        Verify carousel popup with:
         - Printer Information
         - FORGET This Printer
        """
        self.driver.wait_for_object("forget_this_printer_btn")
        self.driver.wait_for_object("printer_info_btn")
    
    def verify_supply_status_screen(self):
        """
        Verify Supply Status screen via:
         - Title: Supply Status
        """
        return self.driver.wait_for_object("supply_status", timeout=15, raise_e=False) is not False

    def verify_bottom_nav_btn(self, btn, invisible=False, timeout=10, raise_e=True):
        """
        Verify invisible/visble bottom navigation button
        :param btn: use class constant variable:
                    NAV_PRINTER_SCAN_BTN
                    NAV_CAMERA_SCAN_BTN
                    NAV_VIEW_PRINT_BTN
                    NAV_APP_SETTINGS_BTN
                    NAV_CREATE_ACCOUNT_BTN
        :param invisible: visible/invisble
        """
        return self.driver.wait_for_object(btn, invisible=invisible, timeout=timeout, raise_e=raise_e)

    def verify_hp_logo(self, timeout=5):
        """
        Verify HP logo in top-left corner of screen. This function is for Basic account or Home screen without HPID login
        """
        return self.driver.wait_for_object("hp_logo",timeout=timeout)

    def verify_do_more_hp_smart(self, timeout=10):
        """
        Verify Do More with HP Smart on Home screen.
        """
        self.driver.wait_for_object("do_more_with_hp_smart", timeout=timeout)

    def verify_change_printer_certificate_popup(self, raise_e=True):
        """
        After selecting printer, verify setup button invisible or not
        :return:
        """
        return self.driver.wait_for_object("change_printer_certificate_text", raise_e=raise_e)

    def verify_hide_this_printer_popup(self):
        """
        Verify Hide this printer? popup through:
        - Title
        - Hide Printer button
        - Go to Dashboard button
        - Cancel button
        """
        self.driver.wait_for_object("hide_this_printer_title")
        self.driver.wait_for_object("hide_printer_btn")
        self.driver.wait_for_object("go_to_dashboard_btn")
        self.driver.wait_for_object("cancel_btn")

    def click_cancel_btn(self):
        """
        Click on Cancel button exit scan preview screen
        """
        self.driver.click("cancel_btn")

    def verify_personalize_tile_btn(self):
        """
        Verify the personalize button on the Home screen
        """
        self.driver.scroll("personalize_tile_btn")

    def verify_printable_sign_in_screen(self, timeout=10):
        """
        Verify Printables sign in screen:
        """
        self.driver.wait_for_object("printable_sign_in_title", timeout=timeout)
        self.driver.wait_for_object("printable_sign_in_yes_btn")
        self.driver.wait_for_object("printable_sign_in_cancel_btn")
    
    def click_continue_as_guest(self, timeout=10, raise_e=True):
        """
        Click on Continue as guest button
        """
        self.driver.wait_for_object("hpx_ows_continue_btn", timeout=timeout, raise_e=raise_e)
        self.driver.click("hpx_ows_continue_btn",raise_e=raise_e)
    
    def click_sign_in(self, timeout=20):
        """
        Click on Sign in button
        """
        self.driver.wait_for_object("hpx_ows_sign_in_btn", timeout=timeout)
        self.driver.click("hpx_ows_sign_in_btn")
    
    def verify_sign_in_btn(self, timeout=10):
        """
        Verify Sign in screen:
        """
        return self.driver.wait_for_object("hpx_ows_sign_in_btn", timeout=timeout)

    # ***********************************************************************************************
    #                                      PRIVATE FUNCTIONS                                        *
    # ***********************************************************************************************
    def __scroll_to_top_home_screen(self, check_printer=False):
        """
        At Home screen, scroll to top of Home screen.
        If check printer, make sure that printer is connected successfully in 3 times
        End of flow: Home screen
        """
        self.driver.scroll("printer_info_container", "up", check_end=False, full_object=False)
        if check_printer:
            for _ in range(3):
                if self.driver.wait_for_object("printer_supply_lv", timeout=30, raise_e=False):
                    return True
                else:
                    continue
            raise TimeoutException("Printer is not connected")        