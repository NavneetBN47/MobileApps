import logging
import time
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Home(SmartFlow):
    flow_name = "home"

    ACCOUNT_BTN = "account_btn"
    SIGN_IN_BTN = "signin_btn"
    SIGN_OUT_BTN = "sign_out_btn"
    SUPPLIES_BTN = "supplies_btn"
    SHORTCUTS_BTN = "shortcuts_btn"
    NO_PRINT_ACTIVITY_TITLE = "no_printer_activity_title"
    MOBILE_FAX_BTN = "mobile_fax_btn"
    TOGGLE_MENU = "toggle_menu"
    VIEW_NOTIFICATIONS_TITLE = "view_notifications_title"
    VIEW_NOTIFICATIONS_LINK = "view_notifications_link"
    ACTIVITY_TABS = [MOBILE_FAX_BTN, SUPPLIES_BTN, ACCOUNT_BTN, SHORTCUTS_BTN]
    

    ########################################################################################################################
    #                                                                                                                      #
    #                                              ACTION  FLOWS                                                           #
    #                                                                                                                      #
    ########################################################################################################################

    def select_get_started_by_adding_a_printer(self, handle_popup=True):
        """
        clicks  add printer sign on home page
        :return:
        """
        if self.verify_add_your_first_printer(raise_e=False) is not False:
            self.select_add_your_first_printer()
        else:
            self.allow_notifications_popup(raise_e=False)
            self.select_printer_plus_button_from_topbar()
        # iOS 13 bluetooth security update
        if handle_popup:
            if self.verify_bluetooth_popup(raise_e=False):
                self.handle_bluetooth_popup()
            # Handle Bluetooth setup pop-up when bluetooth is off
            if self.verify_close(raise_e=False) is not False:
                self.select_close()
                logging.info("Bluetooth is off")

    def select_printer_plus_button_from_topbar(self):
        """
        clicks the small + symbol on the top bar of home page:
            its located right most corner on the home page. but it will display after a printer selection atleast once
        :return:
        """
        self.driver.wait_for_object("add_new_printer_from_top_bar")
        self.driver.click("add_new_printer_from_top_bar")

    def select_notification_bell(self):
        """

        :return:
        """
        self.driver.wait_for_object("notification_bell_btn")
        self.driver.click("notification_bell_btn")
    
    def select_toggle_menu(self):
        self.driver.click(self.TOGGLE_MENU)

    def long_press_on_printer(self):
        """
        it clicks long press on the printer in carousel to bring printer menu live:
            printer menu has options: printer details:
                                      forget this printer:
        :return:
        """
        self.driver.wait_for_object("printer_image", timeout=20)
        self.driver.long_press("printer_image")

    def select_personalize_btn(self):
        """
        selects the Personalize button
        """
        self.driver.scroll("personalize_btn", click_obj=True)

    def verify_tile_displayed(self, tile_name):
        return self.driver.scroll(tile_name, direction="down", scroll_object="tile_collection_view", raise_e=False)

    def select_tile_by_name(self, tile_name, change_check=None):
        """
        clicks on the given tile name:
            tile_name is a shared_obj locator available in shared_obj ui map:
        """
        if not self.driver.click(tile_name, change_check=change_check, raise_e=False):
            self.driver.scroll(tile_name, direction="down", scroll_object="tile_collection_view", click_obj=True)

    def select_different_printer(self):
        """
        From Home screen, go to Printers screen via:
            - Click on Printer button on navigation bar of Home screen
            - CLick on 'Select a Different Printer' button
        End of flow: Printers screen
        """
        self.driver.click("select_printer_btn")

    def select_printer_info(self):
        """
        From Home screen, go to Printers screen via:
            - Click on Printer button on navigation bar of Home screen
            - CLick on 'See my Printer Information' button
        End of flow: Printer Information
        """
        self.driver.click("printer_info_btn")

    def select_carousel(self):
        self.driver.click("device_carousel_collection_view")

    def scroll_to_carousel(self):
        self.driver.scroll("device_carousel_collection_view", direction="up", timeout=20, check_end=False, full_object=True)

    def select_printer_information_from_menu(self):
        """
        From Home screen, go to Printers screen via:
            - Click on Printer button on navigation bar of Home screen
            - CLick on 'See My Printer Information' button
        End of flow: Printers screen
        """

        self.driver.click("printer_information_btn")

    def select_forget_printer_from_menu(self):
        """

        :return:
        """
        self.driver.click("forget_this_printer_btn")
    
    def select_hide_printer_from_menu(self):
        """

        :return:
        """
        self.driver.click("hide_printer_btn")

    def select_forget_printer_cancel_btn(self):
        """

        :return:
        """
        self.driver.click("forget_printer_cancel_btn")

    def select_photos(self):
        self.driver.click("photos_btn")

    def select_forget_printer_forget_btn(self):
        self.driver.click("forget_printer_forget_btn")

    def select_hide_printer_confirmation_btn(self):
        self.driver.click("hide_printer_confirmation_btn")

    def click_on_printer_icon(self):
        """
        clicks on the printer icon in the Printer Overview to open/close the printer options menu
        :return:
        """
        self.driver.scroll("printer_image", direction="up", click_obj=True)
    
    def select_estimated_supply_levels(self, raise_e=True):
        """
        Click on Estimated Supply Levels item on Home screen
        :return:
        """
        self.driver.click("estimated_supply_level_item", raise_e=raise_e)

    def select_arrow_back_to_home(self, raise_e=True):
        """
        Method used to click back to home arrow while being on
        web page after estimated supply levels were tapped.
        :return:
        """
        self.driver.click("arrow_back_to_home", raise_e=raise_e)
        
    def close_privacy_web_alert_dialog(self, timeout=10, raise_e=False):
        """
        Method used to close the privacy web dialog after estimated
        supply level was selected.
        """
        self.driver.click("close_privacy_popup", timeout=timeout, raise_e=raise_e)


    def select_notifications(self):
        """
        Click on Notifications button on Home navigation bar

        End of flows: Notifications screen

        """
        self.driver.click("notification_bell_btn")

    def select_my_printer(self):
        self.driver.click("more_btn")

    def swipe_carousel(self, direction="left"):
        self.driver.swipe("device_carousel_collection_view", direction=direction)

    ####################################################################################################################
    #                                              BOTTOM ACTION BAR                                                   #
    ####################################################################################################################
    def select_home_icon(self):
        """
        Click on 'Home' icon on bottom action bar
        """
        self.verify_rootbar_home_icon().click()

    def select_documents_icon(self):
        """
        Click on 'View and Print' icon on bottom action bar
        """
        self.verify_rootbar_documents_icon().click()

    def select_scan_icon(self):
        """
        Click on 'Scan' icon on bottom action bar
        """
        self.verify_rootbar_scan_icon().click()

    def select_app_settings(self):
        """
        Click on 'Settings' icon on bottom action bar
        """
        self.verify_rootbar_app_settings().click()

    def select_account_icon(self):
        """
        Click on 'Account' icon on bottom action bar
        """
        self.verify_rootbar_account_icon().click()

    def dismiss_tap_account_coachmark(self):
        if self.driver.wait_for_object("tap_account_coachmark", displayed=False, raise_e=False):
            self.driver.click_by_coordinates(area='bl')

    def select_sign_in_icon(self):	
        self.driver.click(self.SIGN_IN_BTN)

    def select_create_account_icon(self, timeout=10):
        self.driver.click("create_account_icon", timeout=timeout)	

    def select_settings_icon(self):
        self.driver.click("settings_opt")

    ########################################################################################################################
    #                                                                                                                      #
    #                                              VERIFICATION  FLOWS                                                     #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_printer_menu_screen(self, raise_e=True):
        """
            verifies the small printer menu daillog as a screen after long press on printer:
                verifying using printer table view (small box)
        :return:
        """
        return self.driver.wait_for_object("printer_menu_table_view", interval=5, raise_e=raise_e)

    def verify_empty_carousel(self):
        self.verify_add_your_first_printer()

    def verify_notification_bell(self):
        """
        verifies the notification bell
        :return:
        """
        self.driver.wait_for_object("notification_bell_btn")

    def verify_hp_smart_nav_bar(self):
        self.driver.wait_for_object("top_navigation_bar_name")
    
    def verify_add_printer_nav_bar(self, raise_e=True):
        """
        Method used to verify the top navigation bar add printer(+) icon.
        :return: bool
        """
        return self.driver.wait_for_object("add_printer_nav_bar", raise_e=raise_e)
    
    def select_add_printer_nav_bar(self, raise_e=True):
        """
        Method used to select the top navigation bar add printer(+) icon.
        """
        return self.driver.click("add_printer_nav_bar", raise_e=raise_e)

    def verify_loaded_printer(self, printer_name, raise_e=True):
        """
        Verify that a printer is loaded via:
            - Left side: printer name
            - Right side: Estimated Cartridge Levels displays or Get Support button
        """
        self.verify_printer_name(printer_name)
        if not self.driver.wait_for_object("estimate_cartridge_levels_text_btn", raise_e=False):
            self.driver.wait_for_object("get_support_btn", raise_e=raise_e)

    def verify_printer_name(self, printer_name, raise_e=True):
        return self.driver.wait_for_object("printer_name_txt", format_specifier=[printer_name], raise_e=raise_e)
    
    def verify_printer_information_screen(self):
        self.driver.wait_for_object("printer_information_title", timeout=10)

    def verify_forget_printer_popup(self):
        """
        :return:
        """
        self.driver.wait_for_object("forget_printer_forget_btn")
    
    def verify_hide_printer_popup(self):
        """
        :return:
        """
        self.driver.wait_for_object("hide_this_printer_popup")

    def verify_forget_printer_cancel_popup(self):
        """
        :return:
        """
        self.driver.wait_for_object("forget_printer_cancel_btn")

    def verify_estimated_cartridge_levels(self, timeout=20, raise_e=True):
        """
        verifies the estimated cartridge levels text
        :return:
        """
        return self.driver.wait_for_object("estimated_supply_level_item", timeout=timeout, raise_e=raise_e)

    def get_printer_name_from_device_carousel(self, printer_cell="DeviceCarouselInfo-1"):
        printer_name = None
        if self.driver.wait_for_object("device_name_in_carousel", format_specifier=[printer_cell],
                                       raise_e=False) is not False:
            printer_name = self.driver.get_attribute("device_name_in_carousel", attribute='value',
                                                     format_specifier=[printer_cell])
        return printer_name
    
    def verify_printer_count(self, selected=1, total=1):
        """
            showing number of printers under carousel, formatted as: x of y printer
        """
        count_msg = "{} of {} printer".format(selected, total)
        self.driver.wait_for_object("printer_count", format_specifier=[count_msg])

    def verify_printer_not_connected_popup(self):
        """
        verifies that the printer not connected popup is displayed after clicking a grayed out tile
        :return:
        """
        self.driver.wait_for_object("printer_not_connected_txt")

    def verify_home_tile(self, raise_e=False):
        # close promotion banner pop-up
        if self.driver.wait_for_object("promotion_banner_pop_up", timeout=5, raise_e=False):
            self.driver.click("promotion_banner_pop_up")
            if self.driver.wait_for_object("_shared_cancel", timeout=3, raise_e=False):
                self.driver.click("_shared_cancel")
            else:
                self.driver.click("_shared_back_arrow_btn")
        if self.driver.wait_for_object("_Shared_no_thanks_btn", timeout=3, raise_e=False):
            self.select_no_thanks()
        self.close_smart_task_awareness_popup()
        self.close_print_anywhere_pop_up()
        self.dismiss_feedback_pop_up()

        return self.driver.wait_for_object("tile_collection_view", raise_e=raise_e)

    def verify_tap_here_to_start(self, raise_e=False):
        """
        WAC popup on home screen
        """
        return self.driver.wait_for_object("tap_here_to_start", timeout=2, raise_e=raise_e)

    def verify_home(self, raise_e=True):
        """
        Verifies home screen via:
        1. Tile collection
        2. Bottom navigation bar: home icon is active
        """
        self.allow_notifications_popup(timeout=10, raise_e=False)
        if self.verify_tap_account_coachmark_popup(raise_e=False):
            self.dismiss_tap_account_coachmark()
        self.driver.wait_for_object("tile_collection_view", raise_e=False)
        if self.verify_rootbar_home_icon(raise_e=False):
            result = self.driver.get_attribute("home_icon_on_rootbar", "value") == '1'
            return result
        else:
            if raise_e:
                raise NoSuchElementException("Home not Displayed")
            else:
                return False

    def verify_add_your_first_printer(self, raise_e=True):
        """
        Add Your First printer card
        """
        return self.driver.find_object("add_your_first_printer", raise_e=raise_e)

    def verify_add_printer_on_carousel(self, invisible=False, raise_e=True):
        """
        Add printer card for when a printer exists on carousel
        """
        return self.driver.wait_for_object("add_printer_img_txt", invisible=invisible, raise_e=raise_e)

    def select_add_your_first_printer(self):
        self.verify_add_your_first_printer().click()

    def verify_printer_added(self):
        return self.driver.scroll("printer_image", direction="up", timeout=5, raise_e=False)

    # GA tiles showing and tile count
    def check_tile_show_and_count(self):

        counted_tile_list = []

        tiles = self.get_all_tiles()
        for tile in tiles:
            name = tile.text
            if name is None:
                continue
            if name in counted_tile_list:
                continue

            logging.debug("Tile Name: {}".format(name))
            self.driver.scroll("tile_title", format_specifier=[name], direction="down",
                               scroll_object="tile_collection_view")

            if name == "Personalize":
                excluded_tile = name
                logging.debug("List Size: {}".format(excluded_tile))
            else:
                self.driver.wait_for_object("tile_title", format_specifier=[name], timeout=30, interval=1)
                counted_tile_list.append(name)

        logging.debug("List Size: {}".format(len(counted_tile_list)))
        self.driver.wait_for_object("tile_collection_view")
        self.driver.scroll("device_info_section", direction="up")

    def get_all_tiles(self):
        return self.driver.find_object("tile_frame", multiple=True,
                                       root_obj=self.driver.find_object("tile_collection_view"))

    def get_all_tiles_titles(self):
        tiles = self.get_all_tiles()
        tiles_titles = []
        for tile in tiles:
            if not tile.text or tile.text in tiles_titles:
                continue
            else:
                tiles_titles.append(tile.text)
        return tiles_titles
    
    # TODO: this method need to refactor more when method used in execution
    def select_printer_from_carousel(self, printer_name):

        self.driver.wait_for_object("tile_collection_view")

        self.driver.scroll("device_info_section", direction="up")
        # self.driver.swipe("tile_collection_view", "up") # TODO: keep swipe if device carousel changes again

        timeout = time.time() + 120
        direction = 'left'
        last_tested_printer = ''
        carousel_cv = self.driver.find_object("device_carousel_collection_view")

        while time.time() < timeout:
            self.driver.wait_for_object("printer_name_txt")
            pn = self.driver.find_object("printer_name_txt")
            current_printer = pn.get_attribute("value")
            if last_tested_printer == current_printer:
                direction = 'left' if direction == 'right' else 'right'

            if printer_name in current_printer:
                logging.info("Found Printer on carousel")
                break

            self.driver.swipe(carousel_cv, direction="left") if direction == 'left' \
                else self.driver.swipe(carousel_cv, direction="right")

    def verify_is_printer_unavailable(self, printer_name, raise_e=True):
        """
        Checks if the printer in the carousel is Unavailable
        """
        return self.driver.wait_for_object("printer_status_txt", displayed=True, raise_e=raise_e, format_specifier=[printer_name])

    def verify_your_privacy_title(self, timeout=30, raise_e=True):
        """
        Method used to verify "Your Privacy" title after popup.
        """
        return self.driver.wait_for_object("your_privacy_title", timeout=timeout, raise_e=raise_e)
    
    def available_printers_in_carousel(self, printer_name=''):

        self.driver.wait_for_object("tile_collection_view")
        self.driver.scroll("device_info_section", direction="up")
        self.driver.wait_for_object("device_carousel_collection_view")

        required_printer = printer_name

        timeout = time.time() + 180
        while time.time() < timeout:
            r_objects = self.driver.find_object('device_carousel_collection_view', multiple=True)
            for obj in r_objects:

                found = False
                current_printer_name = self.driver.find_object("printer_name_txt").get_attribute('value')

                if current_printer_name == required_printer:
                    obj.click()
                    found = True

                if not found:
                    self.driver.swipe(swipe_object="device_carousel_collection_view", check_end=False)
                else:
                    break

    def verify_smart_task_awareness_popup(self, timeout=5, raise_e=False):
        return self.driver.wait_for_object("smart_task_awareness_popup", timeout=timeout, raise_e=raise_e)

    def close_smart_task_awareness_popup(self):
        # TODO: remove this location & notificaiton popup once AIOI-11099 & 10937 is resolved
        self.allow_notifications_popup(raise_e=False)
        if self.verify_allow_while_using_app(raise_e=False):
            self.handle_location_popup()
        if self.verify_smart_task_awareness_popup():
            self.driver.click("smart_task_pop_up_close_btn")
        else:
            logging.info("smart task awareness popup not displayed")

    def close_print_anywhere_pop_up(self):
        self.allow_notifications_popup(raise_e=False)
        if self.driver.wait_for_object("print_anywhere_anytime_popup", timeout=3, raise_e=False) is not False:
            self.driver.click("print_anywhere_anytime_pop_up_close_btn")
            logging.info("Print anywhere popup displayed")

    def close_organize_documents_pop_up(self, timeout=3):
        if self.driver.wait_for_object("organize_documents_pop_up", timeout=timeout, raise_e=False):
            self.select_close()

    def close_use_bluetooth_pop_up(self):
        """
        Dismiss Use bluetooth popup if shows on Home Screen
        :return:
        """
        self.allow_notifications_popup(raise_e=False)
        if self.driver.wait_for_object("use_bluetooth_popup", raise_e=False) is not False:
            self.driver.click("_shared_str_ok")

    def select_tap_here_to_start(self, timeout=60):
        self.driver.wait_for_object("tap_here_to_start", timeout=timeout).click()

    def remove_hide_second_printer(self, printer_img="second_printer_img"):
        try:
            self.remove_printer(printer_img)
        except NoSuchElementException:
            self.hide_printer(printer_img)

    def remove_printer(self, printer_img="printer_image"):
        self.printer_menu_display(printer_img)
        self.select_forget_printer_from_menu()
        self.verify_forget_printer_popup()
        self.select_forget_printer_forget_btn()
    
    def hide_printer(self, printer_img="printer_image"):
        self.printer_menu_display(printer_img)
        self.select_hide_printer_from_menu()
        self.verify_hide_printer_popup()
        self.select_hide_printer_confirmation_btn()

    def select_estimated_supply_levels(self):
        """
        Click on Estimated Supply Levels item on Home screen
        :return:
        """
        self.driver.click("estimated_supply_level_item")

    def printer_menu_display(self, printer_img="printer_image"):
        if self.verify_printer_menu_screen(raise_e=False) is False:
            self.driver.wait_for_object(printer_img)
            self.driver.long_press(printer_img)
            self.verify_printer_menu_screen()

    def verify_feature_unavailable_popup(self, message: str, raise_e: bool=True) -> bool:
        """
        :param message: ui map obj key for the popup error message
        """
        if not self.driver.wait_for_object("feature_unavailable", raise_e=raise_e):
            return False
        self.driver.wait_for_object("_shared_str_ok", raise_e=raise_e)
        self.driver.wait_for_object(message, raise_e=raise_e)
        return True

    def verify_limited_access_popup(self):
        self.driver.wait_for_object("limited_access")
        self.driver.wait_for_object("limited_access_no_printer")
        self.driver.wait_for_object("_shared_continue_btn")
        self.driver.wait_for_object("_shared_cancel")

    def verify_printer_dropdown_options(self, owner=False):
        self.driver.long_press("printer_image")
        self.verify_printer_menu_screen()
        if not owner:
            self.driver.wait_for_object("hide_printer_btn")
        else:
            self.driver.wait_for_object("forget_this_printer_btn")
        self.driver.wait_for_object("printer_information_btn")

    def verify_tap_account_coachmark_popup(self, raise_e=True):
        return self.driver.wait_for_object("tap_account_coachmark", displayed=False, raise_e=raise_e)

    def verify_print_anywhere_popup(self):
        self.driver.wait_for_object("print_anywhere_anytime_popup")
    
    def verify_create_account_icon(self, raise_e=True):
        return self.driver.wait_for_object('create_account_icon', raise_e=raise_e)

    def verify_sign_in_icon(self, raise_e=True):
        return self.driver.wait_for_object("signin_btn", raise_e=raise_e)

    def verify_printer_on_home_screen(self, invisible):
        """
        Verify if the printer added to home screen
        """
        self.driver.wait_for_object("printer_image", invisible=invisible)
        
    def verify_printer_icon(self):
        """
        Method used to verify if the printer icon is present
        on home screen.
        :return:
        """
        self.driver.wait_for_object("printer_image")
        
    def verify_alert_status_icon(self, timeout=10):
        """
        Method used to verify if the alert status icon is present
        on home screen.
        :return:
        """
        self.driver.wait_for_object("alert_status_icon", timeout=timeout)
        
    def verify_alert_status_icon_text(self, raise_e=True):
        """
        Method used to verify if the alert status text is present
        on home screen.
        :return:
        """
        return self.driver.wait_for_object("alert_status_text", format_specifier=["Ready"], raise_e=raise_e)
        
    def verify_arrow_back_to_home(self, raise_e=True):
        """
        Method used to verify the presence of the back to home arrow
        on the opened website after ink estimated supply button was tapped on home
        screen
        return: 
        """
        return self.driver.wait_for_object("arrow_back_to_home", raise_e=raise_e)
    
    def verify_finish_setup_warning(self, raise_e=True, timeout=10):
        """
        Method used to verify if finish printer setup warning is present
        for selected printer
        """
        return self.driver.wait_for_object("finish_setup_warning", raise_e=raise_e, timeout=timeout)
    
    def select_no_thanks(self):
        self.driver.click("_Shared_no_thanks_btn")

    def verify_notification_screen(self):
        """
        Verify notification screen
        """
        self.driver.wait_for_object("notification_title")

    def verify_toggle_menu(self, timeout=10, invisible=False):
        """
        Verify toggle menu is present
        """
        self.driver.wait_for_object("toggle_menu", timeout=timeout, invisible=invisible)

    def verify_limited_access_screen(self):
        """
        Verify Limited Access screen
        - Title
        """
        self.driver.wait_for_object("limited_access_title")
    

    ########################################################################################################################
    #                                             HPX MFE Actions                                                            #
    ########################################################################################################################
    def dismiss_hpx_whats_new_popup(self, raise_e=True, timeout=10):
        """
        Dismiss HPX Whats New Popup
        """
        if self.driver.wait_for_object("hpx_whats_new_popup_skip", raise_e=raise_e, timeout=timeout):
            self.driver.click("hpx_whats_new_popup_skip")
    
    def click_notification_btn(self):
        """
        Click on Notification Button
        """
        self.driver.click("hpx_notification_btn")

    def verify_notification_btn(self):
        """
        Verify on Notification Button
        """
        self.driver.wait_for_object("hpx_notification_btn")
    
    def click_profile_btn(self):
        """
        Click on Profile Button in the Home Screen
        """
        self.driver.click("hpx_profile_btn")
    
    def click_avatar_btn(self, timeout=10):
        """
        Click on Avatar Button in the Home Screen
        """
        self.driver.wait_for_object("hpx_avatar_btn", timeout=timeout).click()
    
    def click_sign_btn_hpx(self):
        """
        Click on Sign In Button in the Home Screen
        """
        self.driver.click("hpx_home_sign_btn")
    
    def get_lets_get_started_text(self, timeout=10):
        """
        Get the Get Started Text
        """
        self.driver.wait_for_object("lets_get_started_txt", timeout=timeout)
        return self.driver.get_text("lets_get_started_txt")
    
    def get_add_your_first_printer_text(self, timeout=10):
        """
        Get the Add Your First Printer Text
        """
        self.driver.wait_for_object("hpx_add_your_first_device_txt", timeout=timeout)
        return self.driver.get_text("hpx_add_your_first_device_txt")
    
    def get_hpx_whats_new_popup_title(self, timeout=10):
        """
        Get the HPX Whats New Title
        """
        self.driver.wait_for_object("hpx_whats_new_popup_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_title")
    
    def get_hpx_whats_new_popup_sub_title(self, timeout=10):
        """
        Get the HPX Whats New Subtexts
        """
        self.driver.wait_for_object("hpx_whats_new_popup_sub_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_sub_title")
    
    def verify_hpx_whats_new_popup(self, timeout=10):
        """
        Verify HPX Whats New Popup
        """
        self.driver.wait_for_object("hpx_whats_new_popup_title", timeout=timeout)
        self.driver.wait_for_object("hpx_whats_new_popup_sub_title", timeout=timeout)
    
    def verify_hpx_whats_new_popup_second_screen(self, timeout=10):
        """
        Verify HPX Whats New Popup Second Screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_title", timeout=timeout)
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_sub_title", timeout=timeout)
    
    def get_hpx_whats_new_popup_second_screen_title(self,timeout=10):
        """
        Get the HPX Whats New Popup Second Screen Title
        """
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_second_screen_title")
    
    def get_hpx_whats_new_popup_second_screen_sub_title(self,timeout=10):
        """
        Get the HPX Whats New Popup Second Screen Subtitle
        """
        self.driver.wait_for_object("hpx_whats_new_popup_second_screen_sub_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_second_screen_sub_title")
    
    def verify_hpx_whats_new_popup_third_screen(self, timeout=10):
        """
        Verify HPX Whats New Popup Third Screen
        """
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_title", timeout=timeout)
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_sub_title", timeout=timeout)
    
    def get_hpx_whats_new_popup_third_screen_title(self,timeout=10):
        """
        Get the HPX Whats New Popup Third Screen Title
        """
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_third_screen_title")
    
    def get_hpx_whats_new_popup_third_screen_sub_title(self,timeout=10):
        """
        Get the HPX Whats New Popup Third Screen Subtitle
        """
        self.driver.wait_for_object("hpx_whats_new_popup_third_screen_sub_title", timeout=timeout)
        return self.driver.get_text("hpx_whats_new_popup_third_screen_sub_title")
    
    def click_hpx_whats_new_popup_next_btn(self, timeout=10):
        """
        Click on HPX Whats New Popup Next Button
        """
        self.driver.click("hpx_whats_new_popup_next_btn", timeout=timeout)
    
    def click_hpx_whats_new_popup_back_btn(self, timeout=10):
        """
        Click on HPX Whats New Popup Back Button
        """
        self.driver.click("hpx_whats_new_popup_back_btn", timeout=timeout)
    
    def click_hpx_whats_new_popup_done_btn(self, timeout=10):
        """
        Click on HPX Whats New Popup Done Button
        """
        self.driver.click("hpx_whats_new_popup_done_btn", timeout=timeout)
    
    def verify_hpx_home(self, timeout=10):
        """
        Verify HPX Home Screen
        """
        assert self.driver.wait_for_object("hpx_printer_add_btn", timeout=timeout)
        assert self.driver.wait_for_object("hpx_avatar_btn", timeout=timeout)
    
    def click_hpx_add_printer_btn(self, timeout=10):
        """
        Click on HPX Add Printer Button
        """
        self.driver.click("hpx_printer_add_btn")
    
    def click_to_view_device_page_from_home(self, timeout=10):
        """
        Method used to click the device page
        """
        self.driver.wait_for_object("device_page_ios", timeout=timeout)
        self.driver.click("device_page_ios")

    def click_hpx_devices_btn(self, timeout=10):
        """
        Click on HPX devices back Button
        """
        self.driver.click("back_btn_ios")

    def verify_device_details_page(self, timeout=10):
        """
        verify device details page
        """
        self.driver.wait_for_object("back_btn_ios")

    def click_hpx_support_btn(self, timeout=10):
        """
        Click on HPX Support Button
        """
        self.driver.click("hpx_support_side_flyoutscreen_btn", timeout=timeout)

    def verify_hpx_subscription_btn(self, raise_e=True):
        """
        Verify HPX Subscription Button
        """
        return self.driver.wait_for_object("hpx_subscription_btn", raise_e=raise_e)

class MacHome(Home):

    def swipe_carousel(self, direction="left"):
        frame = self.driver.get_attribute("device_carousel_collection_view", "frame")
        self.driver.swipe(x=frame["x"] + frame["width"] / 2, y=frame["y"] + frame["height"] / 2, direction=direction)

    def verify_home(self, raise_e=True):
        """
        Verifies home screen via:
        1. Tile collection
        2. Bottom navigation bar: home icon is active
        """
        self.enter_full_screen_mode()
        self.driver.wait_for_object("tile_collection_view", raise_e=False)
        if self.verify_rootbar_home_icon(raise_e=False):
            result = self.driver.get_attribute("home_icon_on_rootbar", "value") == '1'
            if self.verify_hp_diagnose_and_fix_popup(raise_e=False):
                self.driver.click("hp_diagnose_and_fix_dont_allow_btn")
            return result
        else:
            if raise_e:
                raise NoSuchElementException("Home not Displayed")
            else:
                return False

    def dismiss_tap_account_coachmark(self):
        if self.driver.wait_for_object("tap_account_coachmark", timeout=5, displayed=False, raise_e=False):
            self.focus_on_hpsmart_window_mac()
    
    def verify_session_expired_popup(self, timeout=10, raise_e=False):
        """
        Method used to verify the session expired popup
        """
        return self.driver.wait_for_object("session_expired_title", timeout=timeout, raise_e=raise_e)
    
    def verify_hp_diagnose_and_fix_popup(self, timeout=10, raise_e=False):
        """
        Method used to verify the hp diagnose and fix popup
        """
        return self.driver.wait_for_object("hp_diagnose_and_fix_title", timeout=timeout, raise_e=raise_e)
    
    def verify_alert_status_icon_text(self, raise_e=True):
        """
        Method used to verify if the alert status text is present
        on home screen.
        :return:
        """
        try:
            assert self.driver.wait_for_object("alert_status_text", format_specifier=["Ready"], raise_e=False) or \
                self.driver.wait_for_object("alert_status_text", format_specifier=["HP Cartridges"], raise_e=False)
            return True
        except AssertionError:
            if raise_e:
                raise AssertionError("Alert status text not displayed")
            return False

    def select_session_expired_cancel_btn(self):
        """
        Method used to select the session expired cancel button
        """
        self.driver.click("session_expired_cancel_btn")
    
    def verify_printer_dropdown_options(self, owner=False):
        self.driver.right_click("printer_image")
        self.verify_printer_menu_screen()
        if not owner:
            self.driver.wait_for_object("hide_printer_btn")
        else:
            self.driver.wait_for_object("forget_this_printer_btn")
        self.driver.wait_for_object("printer_information_btn")
    
    def verify_home_screen_with_hpx_mfe_enabled(self):
        """
        Currently the only elements showing in the page source are:
            - Privacy
            - Terms of use
            - 2024 HP
        """
        self.driver.wait_for_object("hpx_privacy_text")
        self.driver.wait_for_object("hpx_terms_of_use_text")
        self.driver.wait_for_object("hpx_2024_hp_text")