from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import MobileApps.resources.const.windows.const as w_const
from time import sleep
import re
import pytest

class SignInRequiredException(Exception):
    pass


class Home(GothamFlow):
    flow_name = "home"

    PRINTABLE_URL = ["printables"]

 
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    # ---------------- navigation pane ---------------- #
    def select_menu_btn(self):
        """
        Click on Menu button
        """
        self.driver.click("left_menu_btn")

    def menu_expansion(self, expand=True, raise_e=True):
        """
        Verify the status of expansion of the menu pane and have the corresponding action
        @param expand:
            True: have the menu pane expanded
            False: have the menu pane collapsed
        """
        if (expand and self.navbar_menu_expand() is False) or \
            (expand is False and self.navbar_menu_expand() is True):
            self.select_menu_btn()

    def select_my_hp_account_btn(self):
        """
        Click on HP account button
        """
        self.verify_my_hp_account_btn()
        self.driver.click("left_menu_my_hp_account_btn")

    def select_sign_in_btn(self):
        """
        Click on Sign in button
        """
        self.select_my_hp_account_btn()
        self.verify_fly_out_sign_in_page()
        self.driver.click("left_flyout_sign_in_btn")

    def select_create_account_btn(self):
        """
        Click on Create Account button
        """

        self.select_my_hp_account_btn()
        self.verify_fly_out_sign_in_page()
        self.driver.click("left_flyout_create_account_btn")

    def select_manage_hp_account_btn(self):
        """
        Click on Manage HP Account button
        """
        self.select_my_hp_account_btn()
        self.verify_fly_out_my_account_page()
        self.driver.click("left_flyout_manage_hp_account_btn")

    def select_home_btn(self):
        """
        Click on Home button
        """
        self.menu_expansion(expand=True)
        self.verify_home_btn().click()

    def select_activity_btn(self):
        """
        Click on Bell icon while signed in
        """
        self.menu_expansion(expand=True)
        self.verify_activity_btn().click()

    def select_left_add_printer_btn(self):
        """
        Click Add printer button on navigation pane.
        ? if there's one want to test the big btn        
        """
        self.menu_expansion(expand=True)
        self.verify_left_add_printer_btn().click()

    def select_diagnose_and_fix_btn(self):
        """
        Click on Diagnose and Fix button
        """
        self.driver.click("left_diagnose_and_fix_btn")

    def select_diagnose_and_fix_start_btn(self):
        """
        Click on Diagnose and Fix Start button
        """
        self.verify_diagnose_and_fix_screen().click()

    def select_app_settings_btn(self):
        """
        Click on App settings button
        """
        self.menu_expansion(expand=True)
        # self.verify_app_settings()
        self.driver.click("left_app_settings_btn")

    def select_personalize_tiles_listview(self):
        self.driver.click("personalize_titles_listview")

    def select_pin_hp_smart_to_start_listview(self):
        self.driver.click("pin_hp_smart_to_start_listview")

    def select_send_feedback_listview(self):
        self.driver.click("send_feedback_listview")

    def select_privacy_settings_listview(self):
        self.driver.click("privacy_settings_listview")

    def select_about_listview(self):
        self.driver.click("about_listview")

    def select_notification_settings_listview(self):
        # Only exist when an account is signed in
        self.verify_notification_settings_listview()
        self.driver.click("notification_settings_listview")

    def select_sign_out_listview(self):
        # Only exist when an account is signed in
        self.verify_sign_out_listview()
        self.driver.click("sign_out_app_settings_listview")

    def enable_logging(self):
        self.select_app_settings_btn()
        self.select_about_listview()
        for _ in range(10):
            self.driver.click("hp_image")
        self.driver.check_box("enable_logging_toggle")
        self.driver.click("save_settings_btn")
        self.driver.wait_for_object("saveed_dialog_close_btn").click()
        self.select_navbar_back_btn(return_home=False)
        self.driver.wait_for_object("hp_image")
        self.select_navbar_back_btn()

    def click_coach_mark_text(self):
        self.driver.click("coach_mark_text")

    def hover_hamburger_icon(self):
        self.driver.hover("left_menu_btn")
    
    def hover_home_icon(self):
        self.driver.hover("left_menu_home_btn")

    def hover_activity_icon(self, expand=False):
        if not expand:
            self.driver.hover("left_activity_btn")
        else:
            self.driver.hover("left_activity_btn", x_offset=0.2, y_offset=0.5)

    def hover_add_setup_printer_icon(self):
        self.driver.hover("left_add_printer_btn")
        
    def hover_diagnose_and_fix_icon(self, expand=False):
        if not expand:
            self.driver.hover("left_diagnose_and_fix_btn")
        else:
            self.driver.hover("left_diagnose_and_fix_btn", x_offset=0.3, y_offset=0.5)
        
    def hover_app_settings_icon(self, expand=False):
        if not expand:
            self.driver.hover("left_app_settings_btn")
        else:
            self.driver.hover("left_app_settings_btn", x_offset=0.3, y_offset=0.5)

    def click_shortcuts_listview(self):
        self.driver.click("shortcuts_listview")

    def click_activity_title(self):
        self.driver.click("activity_title")
    
    def hover_activity_item(self, item):
        self.driver.hover(item)

    def click_print_listview(self):
        self.driver.click("print_listview")

    def click_text_files_listview(self):
        self.driver.click("text_file_list_view")

    def click_mobile_fax_listview(self):
        self.driver.click("mobile_fax_listview")

    def click_supplies_listview(self):
        self.driver.click("supplies_listview")

    def click_account_listview(self):
        self.driver.click("account_listview")

    def go_to_reset_device_screen(self):
        self.select_app_settings_btn()
        self.select_about_listview()
        el = self.driver.wait_for_object("hp_image")
        # self.driver.action_chains.key_down(Keys.SHIFT).key_down(Keys.CONTROL).context_click(el).key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
        self.driver.long_press_keys(Keys.CONTROL)
        self.driver.long_press_keys(Keys.SHIFT)
        self.driver.click_by_coordinates(el, right_click=True)
        self.driver.long_press_keys(Keys.CONTROL, down=False)
        self.driver.long_press_keys(Keys.SHIFT, down=False)

    def enter_reset_code(self, code):
        """
        Input reset code 
        """
        self.driver.click("reset_code_edit")
        self.driver.send_keys("reset_code_edit", code)

    def click_reset_device_btn(self):
        self.driver.click("reset_device_btn")

    def click_exception_msg_dialog_ok_btn(self):
        self.driver.click("exception_msg_dialog_ok_btn")

    # ---------------- navigation pane ---------------- #
 
    # ---------------- printer card ---------------- #
    def click_carousel_add_printer_btn(self):
        self.driver.click("carousel_add_printer_btn")

    def click_carousel_printer_status_icon(self):
        self.driver.click("carousel_printer_status_icon", change_check={"wait_obj": "carousel_printer_status_icon", "invisible": True})

    def hover_carousel_printer_status_icon(self):
        self.driver.hover("carousel_printer_status_icon")
        
    def click_carousel_printer_status_text(self):
        self.driver.click("carousel_printer_status_text", change_check={"wait_obj": "carousel_printer_status_text", "invisible": True})

    def click_get_support_btn(self):
        self.driver.click("get_support_btn")

    def click_carousel_estimated_supply_levels(self, raise_e=True):
        return self.driver.click("carousel_estimated_supply_image", change_check={"wait_obj": "carousel_estimated_supply_image", "invisible": True}, raise_e=raise_e)

    def hover_carousel_estimated_supply_image(self):
        self.driver.hover("carousel_estimated_supply_image")
        
    def right_click_printer_carousel(self):
        el = self.driver.find_object("carousel_printer_model_name_text")
        self.driver.click_by_coordinates(el, right_click=True)
        sleep(5)
        if self.verify_hide_printer_list_item_load(raise_e=False) is False:
            el = self.driver.find_object("carousel_printer_image")
            self.driver.click_by_coordinates(el, right_click=True)

    def click_previous_device_btn(self):
        self.driver.click("previous_device_btn")

    def click_next_device_btn(self):
        self.driver.click("next_device_btn")

    def click_add_new_printer_link(self):
        self.driver.click("add_new_printer_link")

    def click_printer_image(self):
        self.driver.click("carousel_printer_image", change_check={"wait_obj": "carousel_printer_image", "invisible": True})

    def click_hide_printer_list_item(self):
        self.driver.click("hide_printer_list_item")

    def click_hide_this_printer_dialog_cancel_btn(self):
        self.driver.click("hide_this_printer_dialog_cancel_btn")

    def click_hide_this_printer_dialog_hide_printer_btn(self):
        self.driver.click("hide_this_printer_dialog_hide_printer_btn")

    def click_hide_this_printer_dialog_go_to_dashboard_btn(self):
        self.driver.click("hide_this_printer_dialog_go_to_dashboard_btn")

    def click_finish_setup_btn(self):
        self.driver.click("carousel_finish_setup_btn")
    # ---------------- printer card ---------------- #
    def click_security_badge_icon(self):
        self.driver.click("security_badge_icon")
    # ---------------- tiles container ---------------- #
    def get_main_page_tile_name(self, name):
        return self.driver.get_attribute(name, attribute="Name")

    def get_main_page_tile_index(self, i):
        return self.driver.get_attribute('dynamic_tile_option', format_specifier=[i], attribute="Name", raise_e=False)
    
    def select_each_tile(self, each_tile):
        self.driver.click(each_tile)

    def select_get_supplies_tile(self):
        self.driver.click("get_supplies_tile")

    def select_scan_tile(self):
        self.driver.click("scan_tile", timeout=10, change_check={"wait_obj": "scan_tile", "invisible": True})

    def select_shortcuts_tile(self):
        self.driver.click("shortcuts_tile", timeout=10, change_check={"wait_obj": "shortcuts_tile", "invisible": True})

    def select_printables_tile(self):
        self.driver.click("printables_tile")

    def select_print_documents_tile(self):
        self.driver.click("print_documents_tile")

    def select_mobile_fax_tile(self):
        self.driver.click("mobile_fax_tile", change_check={"wait_obj": "mobile_fax_tile", "invisible": True})

    def select_help_and_support_tile(self):
        self.driver.click("help_and_support_tile", change_check={"wait_obj": "help_and_support_tile", "invisible": True})

    def select_print_photos_tile(self):
        self.driver.click("print_photos_tile")

    def select_printer_settings_tile(self, change_check=None, retry=3):
        self.driver.click("printer_settings_tile", change_check=change_check, retry=retry)

    def select_cloud_scans_tile(self):
        self.driver.click("cloud_scans_tile")
    
    def select_device_function_dialog_ok_btn(self):
        self.driver.click("device_function_dialog_ok_btn")

    def select_install_printer_btn(self):
        """
        Click Install Printer button on Install to Print dialog
        """
        self.driver.click("install_printer_btn")

    def select_i_will_do_this_later_btn(self):
        """
        Click I'll do this later button on Install to Print dialog
        """
        self.driver.click("i_will_do_this_later_btn")

    def select_success_printer_installed_ok_btn(self):
        """
        Click OK button on Success! Printer Installed dialog
        """
        self.driver.click("success_printer_installed_dialog_ok_btn")

    def select_printer_driver_installed_failed_later_btn(self):
        """
        Click I'll do this later button on Printer Driver installed failed dialog
        """
        self.driver.click("printer_driver_installed_failed_later_btn")

    def select_printer_driver_installed_failed_printers_scanners_btn(self):
        """
        Click Printers & Scanners button on Printer Driver installed failed dialog
        """
        self.driver.click("printer_driver_installed_failed_printers_scanners_btn")

    def select_printer_driver_installed_failed_close_btn(self):
        """
        Click Close button on Printer Driver installed failed dialog
        """
        self.driver.click("printer_driver_installed_failed_close_btn")

    def select_welcome_back_continue_btn(self):
        """
        Click on Continue button on Welcome Back dialog
        """
        self.driver.click("welcome_back_continue_btn")

    def select_an_organization_list_item(self, index):
        """
        Select organization Listitem
        """
        self.driver.click("select_an_organization_list_item", format_specifier=[index])

    def select_skip_btn(self):
        # Choose a printer dialog
        self.driver.click("skip_btn", change_check={"wait_obj": "skip_btn", "invisible": True})

    def select_navbar_back_btn(self, return_home=True, check_kibana=False):
        """
        The back button in activity, device picker, app settings, scan result
        Land on home page
        """
        if check_kibana:
            self.driver.click("device_picker_back_btn", timeout=20)
        else:
            self.driver.click("navbar_back_btn", timeout=20)
        if return_home:
            self.verify_home_screen()

    def click_cec_engagement_close_btn(self, raise_e=True):
        """
        Click on Close button for CEC engagement
        """
        return self.driver.click("cec_engagement_close_btn", raise_e=raise_e)

    def select_not_now_skip_btn(self):
        """
        Click on "Not Now" button on "Upgrade to the new HP App" Popup
        """
        self.driver.wait_for_object("not_now_skip_btn")
        self.driver.click("not_now_skip_btn") 

    # ---------------- tiles container ---------------- #

    # ---------------- Printer Anywhere ---------------- #
    def select_paw_optimize_printers_btn(self):
        self.driver.click("paw_optimize_printers_btn")

    def select_paw_x_btn(self):
        self.driver.click("paw_x_btn")

    def select_paw_learn_more_btn(self):
        self.driver.click("paw_learn_more_btn")

    # ---------------- Get Support ---------------- #
    def click_diagnose_and_fix_link(self):
        self.driver.click("diagnose_and_fix_link")

    def click_get_more_help_link(self):
        self.driver.click("get_more_help_link")

    # ---------------- Smart Driver ---------------- #
    def click_smart_driver_x_btn(self):
        self.driver.click("smart_driver_x_btn")

    def click_install_smart_printing_driver_btn(self):
        self.driver.click("smart_driver_next_btn")

    # ---------------- job count ---------------- #
    def get_value_of_potg_job_count_number(self):
        return self.driver.get_attribute("job_count_num", attribute="Name")
    
    # ---------------- Choose a printer dialog ---------------- #
    def click_dynamic_printer_name_locator(self, keyword):
        self.driver.click("dynamic_printer_name_locator", format_specifier=[keyword])

    # ---------------- Introducing Print Anywhere ---------------- #
    def click_print_anywhere_dialog_x_btn(self):
        self.driver.click("print_anywhere_dialog_x_btn")

    # ---------------- Firmware Update Available screen ---------------- #
    def click_firmware_update_available_screen_yes_btn(self):
        self.driver.click("firmware_update_available_screen_yes_btn")
    
    def click_firmware_update_available_screen_no_btn(self):
        self.driver.click("firmware_update_available_screen_no_btn")

    # ---------------- Private Pickup File(s) ---------------- #
    def click_job_count_text(self):
        self.driver.click("job_count_text")

    def get_job_count_num(self):
        return int(self.driver.get_attribute("job_count_text", attribute="Name"))

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_home_screen(self, raise_e=True, timeout=25):
        """
        Verify the current screen is home screen
        """
        return self.verify_menu_btn(raise_e=raise_e, timeout=timeout) and \
               self.verify_scan_tile(raise_e=raise_e, timeout=timeout)
    
    def verify_cec_banner(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("cec_title", timeout=timeout, raise_e=raise_e)

    def verify_cec_engagement_list_items(self):
        self.driver.wait_for_object("cec_engagement_tile_1")
        self.driver.wait_for_object("cec_engagement_tile_2")
        self.driver.wait_for_object("cec_engagement_tile_3")
        self.driver.wait_for_object("cec_engagement_tile_4", invisible=True)

    def verify_welcome_back_dialog(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("welcome_back_org_list", raise_e=raise_e, timeout=timeout)

    def verify_skip_btn(self, raise_e=True, timeout=10):
        # Choose a printer dialog may pop up
        return self.driver.wait_for_object("skip_btn", raise_e=raise_e, timeout=timeout)

    def verify_navbar_back_btn(self, raise_e=True):
        """
        The back button in all app settings page and device picker
        Land on home page
        """
        return self.driver.wait_for_object("navbar_back_btn", raise_e=raise_e)

    def verify_navbar_back_btn_is_disabled(self):
        """
        The back button is display but can not to click
        """
        assert self.driver.get_attribute("navbar_back_btn", attribute="IsEnabled").lower() == "false"

    def verify_org_ltem_is_selected(self, index):
        assert self.driver.get_attribute("select_an_organization_list_item", format_specifier=[index], attribute="SelectionItem.IsSelected").lower() == "true"

    def verify_shell_title_bar_removed(self):
        """
        Verify the Shell title bar is removed from Main UI
        """
        assert self.driver.wait_for_object("navbar_back_btn", raise_e=False) is False
        assert self.driver.wait_for_object("shell_title_bar_exit_setup", raise_e=False) is False
    
    def verify_no_new_update_available_text(self):
        """
        Verify "New Update Available" modal does not show
        """
        assert self.driver.wait_for_object("new_update_available_text", raise_e=False) is False

    def verify_not_now(self, raise_e=True):
        """
        Verify "Not now" button on the "Upgrade to the new HP App" popup
        """
        return self.driver.wait_for_object("not_now_skip_btn",raise_e=raise_e)

    # ---------------- navigation pane ---------------- #
    def verify_navigation_pane_split_view(self, login=False, printer=False):
        """
        Verify Navigation Pane split view (Login or not, printer added or not)
        """
        self.verify_menu_btn()
        self.verify_home_btn()
        if login:
            self.verify_activity_btn()
        else:
            assert self.verify_activity_btn(raise_e=False) is False
        self.verify_left_add_printer_btn()
        if printer:
            self.verify_diagnose_and_fix_btn()
        else:
            assert self.verify_diagnose_and_fix_btn(raise_e=False) is False
        self.verify_app_settings()

    def verify_menu_btn(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("left_menu_btn", timeout=timeout, raise_e=raise_e)
        
    def verify_coach_mark_for_portal(self, timeout=20, raise_e=True):
        """
        Verify Coach Mark for Portal shows after sign in a UCDE or HP+ account.
        """
        return self.driver.wait_for_object("coach_mark_text", timeout=timeout, raise_e=raise_e)

    def verify_my_hp_account_btn(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("left_menu_my_hp_account_btn", timeout=timeout, raise_e=raise_e)

    def get_text_of_left_menu_my_hp_account_btn(self):
        """
        Verify the name for the left menu my hp account after sign in account.
        """
        return self.driver.get_attribute("left_menu_my_hp_account_btn", "Name")

    def verify_fly_out_sign_in_page(self, timeout=10, raise_e=True):
        """
        Verify the current screen is fly out sign in page while app does not sign in.
        """
        return self.driver.wait_for_object("left_flyout_sign_in_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("left_flyout_create_account_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("left_flyout_manage_hp_account_btn", timeout=timeout, invisible=True, raise_e=raise_e)

    def verify_fly_out_my_account_page(self, timeout=10, raise_e=True):
        """
        Verify the current screen is fly out My Account page after sign in account.
        """
        return self.driver.wait_for_object("left_flyout_manage_hp_account_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("left_flyout_account_name", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("left_flyout_sign_in_btn", timeout=timeout, invisible=True, raise_e=raise_e) and \
                self.driver.wait_for_object("left_flyout_create_account_btn", timeout=timeout, invisible=True, raise_e=raise_e)


    def verify_home_btn(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("left_menu_home_btn", timeout=timeout, raise_e=raise_e)

    def verify_activity_btn(self, raise_e=True):
        return self.driver.wait_for_object("left_activity_btn", raise_e=raise_e)

    def verify_left_add_printer_btn(self, raise_e=True):
        """
        Verify Add / Setup a Printer button shows on navigation pane. 
        """
        return self.driver.wait_for_object("left_add_printer_btn", raise_e=raise_e)

    def verify_diagnose_and_fix_btn(self, raise_e=True):
        return self.driver.wait_for_object("left_diagnose_and_fix_btn", raise_e=raise_e)

    def verify_diagnose_and_fix_screen(self):
        """
        Verify the current screen is Diagnose and fix page after click diagnose and fix btn.
        """
        return self.driver.wait_for_object("diagnose_and_fix_start_btn")

    def verify_app_settings(self, raise_e=True):
        return self.driver.wait_for_object("left_app_settings_btn", raise_e=raise_e)

    def verify_app_settings_pane(self):
        """
        Verify the current screen is App Settings pane afetr click App Settings button.
        """
        self.verify_personalize_tiles_listview()
        self.verify_pin_hp_smart_to_start_listview()
        self.verify_send_feedback_listview()
        self.verify_privacy_settings_listview()
        self.verify_about_listview()

    def verify_app_settings_items_by_index(self, item_index):
        return self.driver.wait_for_object("dynamic_app_settings_items_locator", format_specifier=[item_index])

    def verify_personalize_tiles_listview(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("personalize_titles_listview", raise_e=raise_e, timeout=timeout)

    def verify_pin_hp_smart_to_start_listview(self):
        self.driver.wait_for_object("pin_hp_smart_to_start_listview")

    def verify_send_feedback_listview(self):
        self.driver.wait_for_object("send_feedback_listview")

    def verify_privacy_settings_listview(self):
        return self.driver.wait_for_object("privacy_settings_listview")

    def verify_about_listview(self):
        self.driver.wait_for_object("about_listview")

    def verify_sign_out_listview(self, raise_e=True):
        # Only exist when an account is signed in
        return self.driver.wait_for_object("sign_out_app_settings_listview", raise_e=raise_e)
    
    def verify_activity_pane(self, add_printer=True):
        """
        Verify the current screen is activity screen after click Activity btn on navigation pane.
        Verify the Print option is not available when no printer is added on the Main UI.
        """
        if add_printer:
            self.verify_print_listview()
        self.verify_shortcuts_listview()
        self.verify_mobile_fax_listview()
        self.verify_supplies_listview()
        self.verify_account_listview()

    def verify_print_listview(self):
        self.driver.wait_for_object("print_listview")

    def verify_shortcuts_listview(self):
        self.driver.wait_for_object("shortcuts_listview")

    def verify_text_files_listview(self):
        self.driver.wait_for_object("text_file_list_view")

    def verify_mobile_fax_listview(self):
        self.driver.wait_for_object("mobile_fax_listview")

    def verify_supplies_listview(self):
        self.driver.wait_for_object("supplies_listview")

    def verify_account_listview(self):
        self.driver.wait_for_object("account_listview")

    def verify_home_tooltip(self, raise_e=True):
        return self.driver.wait_for_object("home_tooltip", raise_e=raise_e)
        
    def verify_activity_tooltip(self, raise_e=True):
        return self.driver.wait_for_object("activity_tooltip", raise_e=raise_e)
        
    def verify_add_setup_printer_tooltip(self, raise_e=True):
        return self.driver.wait_for_object("add_setup_printer_tooltip", raise_e=raise_e)
        
    def verify_diagnose_and_fix_tooltip(self, raise_e=True):
        return self.driver.wait_for_object("diagnose_and_fix_tooltip", raise_e=raise_e)
        
    def verify_app_settings_tooltip(self, raise_e=True):
        return self.driver.wait_for_object("app_settings_tooltip", raise_e=raise_e)
    
    # ---------------- navigation pane ---------------- #
    
    # ---------------- printer card ---------------- #
    def verify_setup_or_add_printer_card(self):
        self.verify_carousel_add_printer_title()
        self.verify_carousel_add_printer_image()
        self.verify_carousel_add_printer_body()
        self.verify_carousel_add_printer_btn()
        assert self.verify_carousel_add_printer_title().text == self.get_text_from_str_id("carousel_add_printer_title")
        assert self.verify_carousel_add_printer_body().text == self.get_text_from_str_id("carousel_add_printer_body").replace("<Bold>", "").replace("</Bold>", "")
        assert self.verify_carousel_add_printer_btn().text == self.get_text_from_str_id("carousel_add_printer_btn")
    
    def verify_printer_add_to_carousel(self, setup_btn=False):
        self.verify_home_screen()
        self.verify_carousel_printer_image()
        self.verify_carousel_printer_status_text(timeout=120)
        if setup_btn:
            self.verify_carousel_finish_setup_btn()
        else:
            assert self.verify_carousel_finish_setup_btn(raise_e=False) is False

    def verify_carousel_add_printer_title(self, raise_e=True):
        return self.driver.wait_for_object("carousel_add_printer_title", raise_e=raise_e)

    def verify_carousel_add_printer_image(self, raise_e=True):
        return self.driver.wait_for_object("carousel_add_printer_image", raise_e=raise_e)

    def verify_carousel_add_printer_body(self, raise_e=True):
        return self.driver.wait_for_object("carousel_add_printer_body", raise_e=raise_e)

    def verify_carousel_add_printer_btn(self, raise_e=True):
        return self.driver.wait_for_object("carousel_add_printer_btn", raise_e=raise_e)

    def verify_printer_still_displays(self):
        assert self.driver.wait_for_object("carousel_printer_image")

    def verify_carousel_printer_image(self, timeout=25, raise_e=True):
        return self.driver.wait_for_object("carousel_printer_image", timeout=timeout, raise_e=raise_e)

    def verify_carousel_printer_status_text(self, index=0, timeout=30, raise_e=True):
        return self.driver.wait_for_object("carousel_printer_status_text", index=index, timeout=timeout, raise_e=raise_e)

    def verify_carousel_printer_security_text(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("carousel_printer_security_text", timeout=timeout, raise_e=raise_e)

    def verify_carousel_estimated_supply_text(self, raise_e=True):
        return self.driver.wait_for_object("carousel_estimated_supply_text", raise_e=raise_e)
    
    def verify_carousel_estimated_supply_image(self, timeout=30, invisible=False, raise_e=True):
        return self.driver.wait_for_object("carousel_estimated_supply_image", timeout=timeout, invisible=invisible, raise_e=raise_e)
    
    def verify_get_support_btn(self, timeout=90, invisible=False, raise_e=True):
        return self.driver.wait_for_object("get_support_btn", timeout=timeout, invisible=invisible, raise_e=raise_e)

    def verify_carousel_finish_setup_btn(self, invisible=False, raise_e=True):
        return self.driver.wait_for_object("carousel_finish_setup_btn", invisible=invisible, raise_e=raise_e)

    def verify_carousel_finish_setup_subtitle(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("carousel_finish_setup_subtitle", timeout=timeout, raise_e=raise_e)

    def get_carousel_printer_model_name(self, index=0):
        self.driver.wait_for_object("carousel_printer_model_name_text")
        return self.driver.get_text("carousel_printer_model_name_text", index=index)

    def get_carousel_printer_status_text(self, index=0):
        return self.driver.get_text("carousel_printer_status_text", index=index)

    def verify_carousel_printer_offline_status(self, timeout=25, invisible=False, raise_e=True):
        return self.driver.wait_for_object("carousel_printer_offline_status", timeout=timeout, invisible=invisible, raise_e=raise_e)
    
    def verify_carousel_printer_status(self, status, timeout=25, invisible=False, raise_e=True):
        return self.driver.wait_for_object("carousel_printer_status", format_specifier=[status], timeout=timeout, invisible=invisible, raise_e=raise_e)
    
    def verify_previous_device_btn_enabled_status(self):
        """
        Verify Previous Device button (left arrow) displays on Printer carousel.
        """
        return self.driver.wait_for_object("previous_device_btn").get_attribute("IsEnabled").lower()

    def verify_next_device_btn_enabled_status(self):
        """
        Verify Next Device button (right arrow) displays on Printer carousel.
        """
        return self.driver.wait_for_object("next_device_btn").get_attribute("IsEnabled").lower()

    def verify_add_new_printer_link(self, raise_e=True):
        """
        Verify Add new printer link displays under Printer carousel.
        """
        return self.driver.wait_for_object("add_new_printer_link", raise_e=raise_e)

    def verify_pagination_text(self, raise_e=True):
        """
        Verify Pagination text (x of x printers.) displays under Printer carousel.
        """
        return self.driver.wait_for_object("pagination_text", raise_e=raise_e)

    def verify_hide_printer_list_item_load(self, raise_e=True):
        """
        Verify Hide Printer list item shows after right click printer carousel
        """
        return self.driver.wait_for_object("hide_printer_list_item", raise_e=raise_e)

    def verify_hide_this_printer_dialog_load(self, owner=False, raise_e=True):
        """
        Verify Hide this printer dialog load after clicking Hide printer list item
        """
        if not owner:
            return self.driver.wait_for_object("hide_this_printer_dialog_cancel_btn", raise_e=raise_e) and \
                self.driver.wait_for_object("hide_this_printer_dialog_hide_printer_btn", raise_e=raise_e)
        else:
            return self.driver.wait_for_object("hide_this_printer_dialog_cancel_btn", raise_e=raise_e) and \
                self.driver.wait_for_object("hide_this_printer_dialog_hide_printer_btn", raise_e=raise_e) and \
                self.driver.wait_for_object("hide_this_printer_dialog_go_to_dashboard_btn", raise_e=raise_e)

    def verify_security_not_monitroed_display(self):
        self.driver.wait_for_object("not_monitored_text", timeout=30)

    def verify_security_monitroed_display(self):
        self.driver.wait_for_object("security_monitored_text", timeout=30)

    def verify_carousel_printer_security_text_not_display(self):
        assert self.driver.wait_for_object("carousel_printer_security_text", timeout=30, raise_e=False) is False
    # ---------------- printer card ---------------- #

    # -------------- tiles container --------------- #
    def verify_main_page_tiles(self):
        self.verify_get_supplies_tile()
        self.verify_scan_tile()
        self.verify_shortcuts_tile()
        self.verify_printables_tile()
        self.verify_print_documents_tile()
        self.verify_mobile_fax_tile()
        self.verify_help_and_support_tile()
        self.verify_print_photos_tile()
        self.verify_printer_settings_tile()

    def verify_main_page_each_tile(self, name, raise_e=True):
        return self.driver.wait_for_object(name, raise_e=raise_e)

    def verify_play_learn_tile_not_exist(self):  
        assert self.driver.wait_for_object("play_learn_tile", raise_e=False) is False

    def verify_cloud_scans_tile(self, timeout=30, raise_e=True):  
        return self.driver.wait_for_object("cloud_scans_tile", timeout=timeout, raise_e=raise_e)

    def verify_get_supplies_tile(self):
        return self.driver.wait_for_object("get_supplies_tile")

    def verify_scan_tile(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("scan_tile", timeout=timeout, raise_e=raise_e)

    def verify_shortcuts_tile(self, invisible=False):
        return self.driver.wait_for_object("shortcuts_tile", invisible=invisible)

    def verify_printables_tile(self):
        return self.driver.wait_for_object("printables_tile")

    def verify_print_documents_tile(self):
        return self.driver.wait_for_object("print_documents_tile")

    def verify_mobile_fax_tile(self, invisible=False, raise_e=True):
        return self.driver.wait_for_object("mobile_fax_tile", invisible=invisible, raise_e=raise_e)

    def verify_help_and_support_tile(self):
        return self.driver.wait_for_object("help_and_support_tile")

    def verify_print_photos_tile(self):
        return self.driver.wait_for_object("print_photos_tile")

    def verify_printer_settings_tile(self):
        return self.driver.wait_for_object("printer_settings_tile")

    def verify_instant_ink_tile_image(self):
        self.driver.wait_for_object("instant_ink_tile_image")

    def verify_tile_by_index(self, tile_index):
        return self.driver.wait_for_object("dynamic_tile_locator", format_specifier=[tile_index])

    def verify_device_function_dialog(self):
        # Dialog shows after clicking tiles without a selected printer.
        # "To use this feature, first select a printer" dialog.
        self.driver.wait_for_object("device_function_dialog_message")
        self.driver.wait_for_object("device_function_dialog_ok_btn")

    def verify_help_and_support_page(self, timeout=20):
        self.driver.wait_for_object("help_and_support_page_chat_bot", timeout=timeout)

    def verify_install_to_print_dialog(self, raise_e=True):
        return self.driver.wait_for_object("install_to_print_title", timeout=20, raise_e=raise_e) and \
            self.driver.wait_for_object("install_to_print_content_1", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("install_to_print_content_2", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("i_will_do_this_later_btn", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("install_printer_btn", timeout=2, raise_e=raise_e)    

    def verify_installing_printer_dialog(self, raise_e=True):
        return self.driver.wait_for_object("installing_printer_dialog_title", raise_e=raise_e) and \
            self.driver.wait_for_object("installing_printer_dialog_content", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("installing_printer_dialog_process_ring", timeout=2, raise_e=raise_e)

    def verify_success_printer_installed_dialog(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("success_printer_installed_dialog_title", timeout=timeout, raise_e=raise_e) and \
            self.driver.wait_for_object("success_printer_installed_dialog_ok_btn", timeout=2, raise_e=raise_e)

    def verify_printer_driver_installed_failed_dialog(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("printer_driver_installed_failed_title", raise_e=raise_e, timeout=timeout) and \
            self.driver.wait_for_object("launch_sub_number", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("launch_sub_title", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("launch_sub_desc", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("launch_sub_image", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("select_sub_number", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("select_sub_title", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("select_sub_desc", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("select_sub_image", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("add_sub_number", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("add_sub_title", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("add_sub_image", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("add_note_text", timeout=2, raise_e=raise_e) and \
            self.driver.wait_for_object("printer_driver_installed_failed_printers_scanners_btn", timeout=2, raise_e=raise_e)
    
    def verify_printer_driver_installed_failed_later_btn(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("printer_driver_installed_failed_later_btn", timeout=timeout, raise_e=raise_e)

    def verify_printer_driver_installed_failed_close_btn(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("printer_driver_installed_failed_close_btn", timeout=timeout, raise_e=raise_e)

    def verify_mobile_fax_tile_not_show(self):
        if self.driver.wait_for_object("mobile_fax_tile", raise_e=False):
            raise NoSuchElementException("Mobile Fax tile displays")
        return True

    def verify_exception_msg_dialog(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("exception_msg_text", timeout=timeout, raise_e=raise_e)
    
    def verify_printer_rejected_dialog(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("printer_rejected_dialog_text", timeout=timeout, raise_e=raise_e)
    
    # -------------- tiles container --------------- #

    # ---------------- Firmware Update Available screen ---------------- #
    def verify_firmware_update_available_screen(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("firmware_update_available_screen_title", timeout=timeout, raise_e=raise_e)

    # ***********************************************************************************************
    #                                      STATUS FLOWS                                             *
    # ***********************************************************************************************
    def verify_logged_in(self, timeout=10, raise_e=False):
        self.select_my_hp_account_btn()
        logged_in = not self.verify_fly_out_sign_in_page(timeout=timeout, raise_e=False)
        if logged_in is True:
            self.select_navbar_back_btn()
        else:
            self.select_my_hp_account_btn()
            self.verify_home_screen()
        return logged_in

    def navbar_menu_expand(self, raise_e=True):
        """
        See whether menu bar is expanded or not
        @return:
            True: expanded
            False: collapsed
        """
        pane = self.driver.wait_for_object("left_side_menu_pane", timeout=25)

        if pane.get_attribute("Window.IsModal") == "true":
            return True
        elif pane.get_attribute("Window.IsModal") == "false":
            return False
        else:
            raise NoSuchAttributeException("Can't find IsModal in Home Nav Pane")

    def add_usetanancylogin_msg(self):
        app_name = eval("w_const.PACKAGE_NAME." + pytest.default_info)
        if (fh := self.driver.ssh.remote_open(r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name), mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            data = re.sub("</Misc>", "<CustomFeatures>UseTenancyLogin</CustomFeatures></Misc>", data)
            fh = self.driver.ssh.remote_open(r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name), mode="w")
            fh.write(data)
            fh.close()
            sleep(1)
            self.driver.restart_app()
    
    # ---------------- Printer Anywhere ---------------- #
    def verify_print_anywhere_dialog(self, shared_account=False, raise_e=True):
        if shared_account:
            return self.driver.wait_for_object("paw_x_btn", timeout=25, raise_e=raise_e) and \
            self.driver.wait_for_object("paw_learn_more_btn", raise_e=raise_e)
        else:
            return self.driver.wait_for_object("paw_x_btn", timeout=25, raise_e=raise_e) and \
            self.driver.wait_for_object("paw_optimize_printers_btn", raise_e=raise_e)

    def verify_paw_updating_settings_text(self):
        self.driver.wait_for_object("paw_updating_settings_text")

    # ---------------- Get Support ---------------- #
    def verify_connect_to_your_printer_screen(self):
        self.driver.wait_for_object("get_support_page_title")
        self.driver.wait_for_object("get_support_page_step_1")
        self.driver.wait_for_object("get_support_page_step_1_desc")
        self.driver.wait_for_object("get_support_page_step_2")
        self.driver.wait_for_object("get_support_page_step_2_desc")
        self.driver.wait_for_object("get_support_page_step_3")
        self.driver.wait_for_object("get_support_page_step_3_desc")
        self.driver.wait_for_object("still_having_problem_text")
        self.driver.wait_for_object("diagnose_and_fix_link")
        self.driver.wait_for_object("get_more_help_link")

    # ---------------- Smart Driver ---------------- #
    def verify_smart_driver_dialog(self, raise_e=True):
        return self.driver.wait_for_object("smart_driver_x_btn", timeout=25, raise_e=raise_e) and \
            self.driver.wait_for_object("smart_driver_next_btn", raise_e=raise_e)

        # ---------------- main tiles ---------------- #
    def capture_main_tiles_img(self):
        """
        Returns screenshot of id card preview asbase64
        """
        return self.driver.screenshot_element("tiles_pane")
    
    # ---------------- Choose a printer dialog ---------------- #
    def verify_choose_a_printer_dialog(self):
        self.driver.wait_for_object("choose_a_printer_tile")
        self.driver.wait_for_object("choose_a_printer_text_1")
        self.driver.wait_for_object("choose_a_printer_text_2")
        self.driver.wait_for_object("choose_a_printer_text_3")
        self.driver.wait_for_object("skip_btn")

    # ---------------- Private Pickup File(s) ---------------- #
    def verify_job_count_info(self, raise_e=True, timeout=25):
        return self.driver.wait_for_object("job_count_text", raise_e=raise_e, timeout=timeout) and\
        self.driver.wait_for_object("private_pickup_file_text", raise_e=raise_e, timeout=timeout)
 