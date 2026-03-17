import logging
import pytest
from abc import ABCMeta
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from MobileApps.libs.flows.ios.ios_flow import IOSFlow
from MobileApps.resources.const.ios.const import BUNDLE_ID


class SmartFlow(IOSFlow):
    __metaclass__ = ABCMeta
    project = "smart"

    # preset sliders of Camera and scan flow
    PHOTO = "photo_mode"
    DOCUMENT = "document_mode"        
    ID_CARD = "id_card"
    MULTI_ITEM = "multi_item_mode"
    BATCH = "batch_mode"
    BOOK = "book_mode"
    TEXT_EXTRACT = "text_extract"
    SIGN_IN_BTN = "_shared_sign_in"
    SIGN_OUT_BTN = "_shared_sign_out"

    def __init__(self, driver):
        super(SmartFlow, self).__init__(driver)
        self.load_smart_app_shared_ui()

    def load_smart_app_shared_ui(self):
        ui_map = self.load_ui_map(system="IOS", project="smart", flow_name="shared_obj")
        self.driver.load_ui_map("smart", "shared_obj", ui_map)
        return True

    def get_ios_device_type(self):
        return "iPhone" if "iphone" in self.driver.driver_info['deviceName'].lower() else 'iPad'

    def verify_rootbar_home_icon(self, raise_e=True):
        return self.driver.wait_for_object("home_icon_on_rootbar", raise_e=raise_e)

    def verify_rootbar_documents_icon(self, raise_e=True, invisible=False):
        return self.driver.wait_for_object("files_and_photos_icon_rootbar", raise_e=raise_e, invisible=invisible)

    def verify_rootbar_scan_icon(self, raise_e=True, invisible=False):
        return self.driver.wait_for_object("scan_icon_on_rootbar", raise_e=raise_e, invisible=invisible)

    def verify_rootbar_app_settings(self):
        return self.driver.wait_for_object("settings_icon_on_rootbar")

    def verify_rootbar_account_icon(self):
        return self.driver.wait_for_object("_shared_account")

    def verify_rootbar_create_account_icon(self):
        return self.driver.wait_for_object("_shared_create_account")

    def verify_rootbar_sign_in(self):
        return self.driver.wait_for_object("_shared_sign_in")
    
    def verify_rootbar_view_and_print_icon(self, raise_e=True, invisible=False):
        return self.driver.wait_for_object("view_and_print_icon_on_rootbar", raise_e=raise_e, invisible=invisible)

    def verify_bottom_navigation_bar(self):
        return self.driver.wait_for_object("bottom_rootbar")

    def verify_bottom_navigation_bar_icons(self, signed_in=True, already_signed_in=False):
        self.verify_rootbar_home_icon()
        self.verify_rootbar_app_settings()
        if signed_in:
            self.verify_rootbar_documents_icon()
            self.verify_rootbar_scan_icon()
            self.verify_rootbar_account_icon()
        elif not already_signed_in:
            self.verify_rootbar_create_account_icon()
            self.verify_rootbar_sign_in()
        else:
            self.verify_rootbar_scan_icon()
            self.verify_rootbar_view_and_print_icon()
            self.verify_rootbar_sign_in()

    def verify_back_arrow_btn(self):
        return self.driver.wait_for_object("_shared_back_arrow_btn")

    def verify_cancel(self, raise_e=True, invisible=False):
        return self.driver.wait_for_object("_shared_cancel", raise_e=raise_e, invisible=invisible)

    def verify_allow_while_using_app(self, raise_e=True):
        return self.driver.wait_for_object("_shared_allow_while_using_app", timeout=10, raise_e=raise_e)

    def verify_allow_once(self, raise_e=True):
        return self.driver.wait_for_object("_shared_allow_once", timeout=3, raise_e=raise_e)

    def verify_dont_allow(self, raise_e=True):
        return self.driver.wait_for_object("_shared_dont_allow", timeout=3, raise_e=raise_e)

    def verify_ok(self, raise_e=True):
        return self.driver.wait_for_object("_shared_str_ok", timeout=3, raise_e=raise_e)

    def verify_close(self, raise_e=True):
        return self.driver.wait_for_object("_shared_close", raise_e=raise_e)

    def handle_location_popup(self, selection="allow", raise_e=True):
        if self.verify_allow_while_using_app(raise_e=raise_e) is not False:
            buttons = {
                "allow": self.verify_allow_while_using_app,
                "once": self.verify_allow_once,
                "dont_allow": self.verify_dont_allow
                }
            buttons[selection]().click()

    def verify_bluetooth_popup(self, raise_e=True):
        return self.driver.wait_for_object("bluetooth_alert", timeout=5, raise_e=raise_e)

    def verify_bluetooth_popup_ui(self, raise_e=True):
        return [
            self.driver.wait_for_object("bluetooth_alert", raise_e=raise_e),
            self.driver.wait_for_object("bluetooth_alert_text", raise_e=raise_e),
            self.verify_ok(raise_e=raise_e),
            self.verify_dont_allow(raise_e=raise_e)
        ]

    def handle_bluetooth_popup(self, allow=True):
        if allow:
            btn_to_click = "_shared_str_ok" if int(self.driver.platform_version.split(".")[0]) == 16 else "allow_btn"
            self.driver.click(btn_to_click)
        else:
            self.driver.click("_shared_dont_allow")

    def verify_no_internet_popup(self):
        self.driver.wait_for_object("_shared_str_check_internet")
        self.driver.wait_for_object("_shared_str_no_internet")

    def handle_no_internet_popup(self, try_again=True):
        if try_again:
            self.driver.click("_shared_try_again")
        else:
            self.driver.click("_shared_cancel")

    def get_options_listed(self, option, format_specifier=[]):
        options = []
        options_list = self.driver.find_object(option, format_specifier=format_specifier, multiple=True)
        if len(options_list) < 1:
            raise NoSuchElementException(option + "not displayed")
        for i in range(len(options_list)):
            option_name = options_list[i].get_attribute("name")
            options.append(option_name.encode("ascii", "ignore").decode())
        logging.debug(options)
        return options

    def verify_an_element_and_click(self, element, format_specifier=[], click=True, scroll=False, delay=0, raise_e=False):
        if scroll:
            element_displayed = self.driver.scroll(element, format_specifier=format_specifier, raise_e=raise_e)
        else:
            element_displayed = self.driver.wait_for_object(element, format_specifier=format_specifier, raise_e=raise_e)
        if element_displayed and click:
            self.driver.click(element, format_specifier=format_specifier, delay=delay, raise_e=raise_e)
        return element_displayed

    def verify_static_text(self, text_option, raise_e=False):
        return self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[text_option], raise_e=raise_e)

    def select_static_text(self, text):
        self.driver.click("_shared_visible_dynamic_text", format_specifier=[text])

    def verify_array_of_elements(self, array_elements, direction="down", scroll_object=None):
        element_missing = []
        for element in array_elements:
            if not self.driver.wait_for_object(element, raise_e=False):
                if not self.driver.scroll(element, direction=direction, scroll_object=scroll_object, raise_e=False):
                    element_missing.append(element)
        if element_missing:
            raise NoSuchElementException("Following options {}:not displayed".format(element_missing))

    def select_navigate_back(self, index=0, delay=None):
        self.driver.click("_shared_back_arrow_btn", index=index, delay=delay)

    def select_files_and_photos_rootbar_element(self, delay: int):
        self.driver.click("files_and_photos_icon_rootbar", delay=delay)
        
    def select_next(self):
        self.driver.click("next_btn")

    def select_cancel(self, timeout=10):
        self.driver.click("_shared_cancel", timeout=timeout)

    def select_close(self):
        self.driver.click("_shared_close")

    def select_done(self, raise_e=True):
        self.driver.click("_shared_done", raise_e=raise_e)

    def select_ok(self):
        self.driver.click("_shared_str_ok")

    def select_continue(self, timeout=10):
        self.driver.click("_shared_continue_btn", timeout=timeout)

    def verify_continue_popup(self, raise_e=False):
        return self.driver.wait_for_object("_shared_continue_btn", raise_e=raise_e)

    def select_yes(self):
        self.driver.click("_shared_yes")

    def select_no_option(self):
        self.driver.click("_shared_no")

    def verify_no_search_results(self):
        self.driver.wait_for_object("_shared_no_search_results", displayed=False)

    def allow_notifications_popup(self, timeout=5, allow=True, raise_e=True):
        """
        Check if the current screen contains the notification popup
        :return:
        """
        if self.driver.wait_for_object("notifications_alert", timeout=timeout, raise_e=raise_e) is not False:
            self.driver.performance.stop_timer("hpid_login")
            if allow:
                self.driver.click("allow_btn")
            else:
                self.driver.click("do_not_allow_access_btn")

    def verify_adjust_scan_coach_mark(self, raise_e=False):
        return self.driver.wait_for_object("adjust_scan_coach_mark", timeout=5, raise_e=raise_e)

    def select_second_close_btn(self):
        self.driver.click("_shared_close", index=1)

    def verify_second_close_btn(self, timeout=5, raise_e=False):
        return self.driver.wait_for_object("_shared_close", index=1, timeout=timeout, raise_e=raise_e)
    
    def select_gear_setting_btn(self):
        self.driver.click("scan_setting_gear")
        
    def select_on_my_iphone(self):
        return self.driver.click("on_my_iphone")
    
    def rename_file(self, obj, file_name):
        self.driver.click("_shared_clear_text_btn")
        return self.driver.send_keys(obj, file_name)

    def verify_sign_in_btn(self, raise_e=True):
        return self.driver.wait_for_object("_shared_sign_in", raise_e=raise_e)
    
    def verify_sign_out_btn(self, raise_e=True):
        return self.driver.wait_for_object("_shared_sign_out", raise_e=raise_e)

    def verify_create_account_btn(self, raise_e=True):
        return self.driver.wait_for_object("_shared_create_account", raise_e=raise_e)

    def select_sign_in_btn(self):
        return self.driver.click("_shared_sign_in")
    
    def select_sign_out_btn(self):
        return self.driver.click("_shared_sign_out")

    def select_create_account_btn(self):
        return self.driver.click("_shared_create_account")

    def select_rootbar_view_and_print_icon(self):
        return self.driver.click("view_and_print_icon_on_rootbar")

    def dismiss_feedback_pop_up(self):
        if self.driver.wait_for_object("feedback_alert_title", raise_e=False, timeout=3):
            self.driver.click("_Shared_no_thanks_btn")
            logging.info("Selected No Thanks on Feedback pop_up")

    def select_preset_mode(self, mode):
        self.verify_preset_mode(mode)
        if not self.driver.click(mode, change_check={"cc_type": "wait_for_attribute", "wait_obj": mode, "wait_attribute": "rect", "interval": 2, "retry": 5}, raise_e=False):
            logging.info("Scan preset mode not changed, currently set to {}".format(mode))
    
    def verify_preset_mode(self, mode, raise_e=True):
        '''
            capture modes in camera and scan
            DOCUMENT: document_mode
            BATCH: batch_mode
            PHOTO: photo_mode
            TEXT_EXTRACT: text_extract
            MULTI_ITEM: multi_item_mode
            BOOK: book_mode
            ID_CARD: id_card
        '''
        if not self.driver.wait_for_object(mode, raise_e=False):
            if pytest.platform == "IOS":
                # scroll all the way to the left, multiple swipes, each takes 10s to load
                self.driver.scroll(self.BATCH, scroll_object="preset_collection_view", 
                    direction="left", check_end=False, timeout=60, raise_e=True)
                # scroll to the right to find element, multiple swipes, each takes 10s to load
                self.driver.scroll(mode, scroll_object="preset_collection_view", 
                    direction="right", check_end=False, timeout=60, raise_e=raise_e)
            else:
                self.driver.scroll(mode, scroll_object="preset_collection_view", 
                    direction="down", timeout=60, raise_e=raise_e)
        return self.driver.wait_for_object(mode, raise_e=raise_e)
    
    def verify_preset_sliders(self, acc_type="normal"):
        self.verify_preset_mode(self.DOCUMENT)
        self.verify_preset_mode(self.PHOTO)
        self.verify_preset_mode(self.BATCH)
        if acc_type == "hpplus":
            self.verify_preset_mode(self.MULTI_ITEM)
            self.verify_preset_mode(self.BOOK)
            self.verify_preset_mode(self.ID_CARD)
            self.verify_preset_mode(self.TEXT_EXTRACT)
    
    def verify_sign_out_confirmation_popup(self, raise_e=True):
        self.driver.wait_for_object("sign_out_confirm_title", raise_e=raise_e)
        self.driver.wait_for_object("sign_out_confirm_msg", raise_e=raise_e)
        self.driver.wait_for_object("save_username_for_easy_signin", raise_e=raise_e)
        self.verify_sign_out_btn(raise_e=raise_e)
        self.verify_cancel(raise_e=raise_e)
    
    def verify_sign_out_on_popup(self, raise_e):
        return self.driver.wait_for_object("pop_up_sign_out_btn", raise_e=raise_e)
    
    def select_sign_out_on_popup(self):
        self.driver.click("pop_up_sign_out_btn")
    
    def dismiss_sign_out_popup(self, signout=True):
        if signout:
            self.select_sign_out_on_popup()
        else:
            self.select_cancel()
    
    def format_printer_name_for_scanner_source(self, printer_name):
        return printer_name[:25]

    def verify_is_toggled(self, switch_name, is_toggled=True, toggle_on_after_check=True, raise_e=True):
        """
        :param switch_name: switch name
        :param is_toggled: Checks if :switch_name: is toggled on
        :param toggle_on_after_check: toggle the switch on after checking the switch status
        :return:
        """
        if not raise_e:
            if toggle_on_after_check:
                self.driver.check_box(switch_name)
            else:
                self.driver.check_box(switch_name, uncheck=True)
            return
        if is_toggled:
            assert self.driver.get_attribute(switch_name, "value") == "1", f"Switch {switch_name} is not toggled"
        else:
            assert self.driver.get_attribute(switch_name, "value") == "0", f"Switch {switch_name} is toggled"
        if toggle_on_after_check:
            self.driver.check_box(switch_name)
        else:
            self.driver.check_box(switch_name, uncheck=True)
    
########################################################################################################################
#                                                                                                                      #
#                                                  Mac Functions                                                       #
#                                                                                                                      #
########################################################################################################################

    def focus_on_hpsmart_window_mac(self, timeout=10):
        """
        Focus on HP Smart window on mac if another window is on top of it
        """
        self.driver.click("hpsmart_window", timeout=timeout)

    def click_hpsmart_preferences_btn(self, timeout=10):
        """
        Click on Preferences button in the HP Smart menu on mac
        """
        self.driver.hover((0, 0))
        self.driver.click("hpsmart_prefrences_btn", timeout=timeout)
    
    def click_stacks_dropdown_menu(self, timeout=10):
        """
        Click on Stacks dropdown menu on mac under HP Smart Preferences > General on mac
        """
        self.driver.click("stacks_dropdown_menu", timeout=timeout)

    def select_stack_option_from_dropdown_menu(self, stack_option):
        """
        Select an option from Stacks dropdown menu on mac
        """
        stacks = {"pie": "PIE1", "stage": "Stage1", "production": "Production"}
        self.driver.click("stack_option_from_dropdown", format_specifier=[stacks[stack_option]])

    def enter_full_screen_mode(self):
        """
        Enter full screen mode on mac
        """
        if self.driver.wait_for_object("_is_fullscreen", timeout=3, raise_e=False):
            return
        self.driver.click("_shared_fullscreen_btn")
    
    def exit_full_screen_mode(self):
        """
        Exit full screen mode on mac
        """
        if not self.driver.wait_for_object("_is_fullscreen", timeout=3, raise_e=False):
            return
        self.driver.hover((0, 0))
        self.driver.click("_shared_fullscreen_btn")
    
    def select_hpx_settings_tab(self):
        """
        Select HPX Settings tab on mac
        """
        self.driver.click("hpx_settings_tab")
    
    def toggle_hpx_enable_web_mfe_checkbox(self, enable=True):
        """
        Toggle HPX Enable Web MFE checkbox on mac
        """
        is_enabled = True if self.driver.get_attribute("hpx_enable_web_mfe_checkbox", "value") == '1' else False
        if enable != is_enabled:
            self.driver.click("hpx_enable_web_mfe_checkbox")