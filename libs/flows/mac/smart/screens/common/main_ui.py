# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the main UI screen.

@author: Sophia
@create_date: May 9, 2019
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class MainUI(SmartScreens):
    folder_name = "common"
    flow_name = "main_ui"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(MainUI, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("scan_tile", format_specifier=['Scan'], timeout=timeout, raise_e=raise_e)

    def wait_for_coach_mark_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Coach Mark load on main UI screen.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_coach_mark_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("coach_mark", timeout=timeout, raise_e=raise_e)

    def wait_for_add_your_first_printer_text_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait add your first printer text on main UI screen.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_add_your_first_printer_text_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("add_your_first_printer_text", timeout=timeout, raise_e=raise_e)

    def wait_for_ready_status_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_ready_status_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_status_text", format_specifier=['Ready'], timeout=timeout, raise_e=raise_e)

    def wait_for_hp_cartridges_installed_status_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_hp_cartridge_installed_status_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_status_text", format_specifier=['HP Cartridges Installed'], timeout=timeout, raise_e=raise_e)

    def wait_for_printer_offline_status_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Printer Offline status shows on main UI screen.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_printer_offline_status_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_status_text", format_specifier=['Printer offline'], timeout=timeout, raise_e=raise_e)

    def wait_for_mobile_fax_tile_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Tile load on main UI screen correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_mobile_fax_tile_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("mobile_fax_tile", format_specifier=['Mobile Fax'], timeout=timeout, raise_e=raise_e)

    def wait_for_shortcuts_tile_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Shortcuts tile load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_smart_tasks_tile_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("shortcuts_tile", format_specifier=['Shortcuts'], timeout=timeout, raise_e=raise_e)

    def wait_for_private_pickup_files_text_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Private Pickup Files text load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_private_pickup_files_text_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("private_pickup_files_text", timeout=timeout, raise_e=raise_e)

    def wait_for_estimated_supply_levels_text_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Estimated Supply levels text load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_estimated_supply_levels_text_text_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("estimated_supply_levels_text", timeout=timeout, raise_e=raise_e)

    def wait_for_printer_status_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for printer status load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_screen_load]-Wait for printer_status loading... ")

        return self.driver.wait_for_object("printer_status", timeout=timeout, raise_e=raise_e)

    def wait_for_app_windows(self, timeout=30, raise_e=True):
        '''
        This is a method to wait app windows shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_app_windows]-Wait for screen loading... ")

        return self.driver.wait_for_object("app_window", timeout=timeout, raise_e=raise_e)

    def wait_for_find_printer_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait find printer icon load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_find_printer_icon]-Wait for screen loading... ")

        return self.driver.wait_for_object("add_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_forget_printer_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait forget printer screen load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_forget_printer_btn_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("forget_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_hide_printer_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait hide_printer_btn load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_hide_printer_btn_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("hide_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_forget_this_printer_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait forget this printer button load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_forget_this_printer_btn_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("forget_this_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_left_arrow_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait left arrow icon load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_left_arrow_icon_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("left_arrow_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_allow_hp_diagnose_fix_dialog_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait allow_hp_diagnose_fix_dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_allow_hp_diagnose_fix_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("allow_hp_diagnose_fix_dialog_allow_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_choose_a_printer_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait allow_hp_diagnose_fix_dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_choose_a_printer_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("skip_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_right_arrow_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait right arrow icon load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_right_arrow_icon_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("right_arrow_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_finish_setup_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Finish Setup button load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_finish_setup_btn_display]-Wait for Finish Setup button loading... ")

        return self.driver.wait_for_object("finish_setup_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_potg_optimize_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for POTG Optimize dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_potg_optimize_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("potg_optimize_dialog_introducing_print_anywhere_text", timeout=timeout, raise_e=raise_e)

    def wait_for_potg_optimize_updating_settings_dialog(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for POTG Optimize Updating settings dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_potg_optimize_updating_settings_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("potg_optimize_dialog_updating_settings_text", timeout=timeout, raise_e=raise_e)

    def wait_for_my_account_printers_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for my_account_printers_screen load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_my_account_printers_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("my_account_printers_text", timeout=timeout, raise_e=raise_e)

    def wait_for_install_to_print_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Install to Print load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_install_to_print_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("install_to_print_dialog_the_selected_printer_text", timeout=timeout, raise_e=raise_e)

    def click_left_arrow_btn(self):
        '''
        This is a method to click left arrow button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_left_arrow_btn]-Click left arrow button... ")

        self.driver.click("left_arrow_btn", is_native_event=True)

    def click_right_arrow_btn(self):
        '''
        This is a method to click right arrow button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_right_arrow_btn]-Click right arrow button... ")

        self.driver.click("right_arrow_btn", is_native_event=True)

    def click_close_btn_on_potg_optimize_dialog(self):
        '''
        This is a method to click Close button on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_close_btn_on_potg_optimize_dialog]-Click Close button... ")

        self.driver.click("potg_optimize_dialog_close_btn", is_native_event=True)

    def click_optimize_printers_btn_on_potg_optimize_dialog(self):
        '''
        This is a method to click Optimize Printers button on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_optimize_printers_btn_on_potg_optimize_dialog]-Click Optimize Printers button... ")

        self.driver.click("potg_optimize_dialog_optimize_printers_btn", is_native_event=True)

    def click_private_pickup_files_number(self):
        '''
        This is a method to click Private Pickup Files number.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_private_pickup_files_number]-Click Private Pickup Files number... ")

        self.driver.click("private_pickup_files_number", is_native_event=True)

    def click_get_ink_tile(self):
        '''
        This is a method to click Get Ink tile or Get Supplies tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_get_ink_tile]-Click 'Get Ink Tile' or 'Get Supplies tile'... ")

        self.driver.click("get_ink_tile", is_native_event=True)  # format_specifier=['Get Ink']

    def click_get_supplies_tile_no_printer(self):
        '''
        This is a method to click Shortcuts tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_shortcuts_tile]-Click Shortcuts tile... ")

        self.driver.click("get_supplies_tile_no_printer", format_specifier=['Get Supplies'], is_native_event=True)

    def click_shortcuts_tile(self):
        '''
        This is a method to click Shortcuts tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_shortcuts_tile]-Click Shortcuts tile... ")

        self.driver.click("shortcuts_tile", format_specifier=['Shortcuts'], is_native_event=True)

    def click_scan_tile(self):
        '''
        This is a method to click scan tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_scan_tile]-Click 'Scan Tile' button... ")

        self.driver.click("scan_tile", format_specifier=['Scan'], is_native_event=True)

    def click_print_document_tile(self):
        '''
        This is a method to click print document tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_print_document_tile]-Click 'Print Document Tile' button... ")

        self.driver.click("print_document_tile", format_specifier=['Print Documents'], is_native_event=True)

    def click_print_photo_tile(self):
        '''
        This is a method to click print photo tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_print_photo_tile]-Click 'Print Photo Tile' button... ")

        self.driver.click("print_photo_tile", format_specifier=['Print Photos'], is_native_event=True)

    def click_mobile_fax_tile(self):
        '''
        This is a method to click Mobile Fax tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_mobile_fax_tile]-Click 'Mobile Fax Tile' button... ")

        self.driver.click("mobile_fax_tile", format_specifier=['Mobile Fax'], is_native_event=True)

    def click_help_center_tile(self):
        '''
        This is a method to click help_center_tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_help_center_tile]-Click 'Help Center Tile' button... ")

        self.driver.click("help_center_tile", format_specifier=['Help & Support'], is_native_event=True)

    def click_printables_tile(self):
        '''
        This is a method to click printables_tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printables_tile]-Click 'printables_tile' button... ")

        self.driver.click("printables_tile", format_specifier=['Printables'], is_native_event=True)

    def click_printer_settings_tile(self):
        '''
        This is a method to click printer_settings_tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printer_settings_tile]-Click 'Printer Settings Tile' button... ")

        self.driver.click("printer_settings_tile", format_specifier=['Printer Settings'], is_native_event=True)

    def click_printer_image(self):
        '''
        This is a method to click Printer Image on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printer_image]-Click Printer Image... ")

        self.driver.click("printer_image", is_native_event=True)

    def click_printer_status_image(self):
        '''
        This is a method to click Printer Status Image on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printer_status_image]-Click Printer Status Image... ")

        self.driver.click("printer_status_image", is_native_event=True)

    def click_allow_btn_on_allow_hp_diagnose_fix_dialog(self):
        '''
        This is a method to click allow_btne on hp_diagnose_fix_dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_allow_btn ]-Click allow_btn... ")

        self.driver.click("allow_hp_diagnose_fix_dialog_allow_btn", is_native_event=True)

    def click_add_printer_btn(self):
        '''
        This is a method to click Add printer button on Main page.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_add_printer_btn]-Click Add printer button... ")

        self.driver.click("add_printer_btn")
 
    def click_skip_icon(self):
        '''
        This is a method to click skip icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_skip_icon]-Click 'skip' icon... ")

        self.driver.click("skip_btn")

    def click_finish_setup_btn(self):
        '''
        This is a method to click Finish Setup button on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_finish_setup_btn]-Click Finish Setup button... ")

        self.driver.click("finish_setup_btn", is_native_event=True)

    def right_click_find_printer_icon(self):
        '''
        This is a method to right click find printer icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[right_click_find_printer_icon]-Click 'find_printer' icon... ")

        self.driver.context_click("add_printer_btn")

    def right_click_printer_image_by_id(self):
        '''
        This is a method to right click printer image on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[right_click_printer_image_by_id]-Click 'print_image' icon... ")

        self.driver.context_click("printer_image")

    def right_click_printer_image_by_coordinates(self):
        '''
        This is a method to select file.
        :parameter:
        :return:
        '''
        position = self.driver.get_location("printer_status")
        x_position = position['x'] - 1300
        y_position = position['y'] - 300

        sleep(2)
        self.driver.click("printer_status", is_native_event=True)
        self.driver.context_click_by_coordinates(x=x_position, y=y_position)
        return True

    def click_outside_of_forget_this_printer_btn(self):
        '''
        This is a method to click outside of Forget this printer btn on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_outside_of_forget_this_printer_btn]-Click outside of Forget this printer btn... ")

        self.driver.click("right_arrow_icon", is_native_event=True)
#         position = self.driver.get_location("printer_status")
#         x_position = position['x'] - 1400
#         y_position = position['y'] - 400
#         logging.debug(position)
# 
#         sleep(2)
#         self.driver.click_by_coordinates(x=x_position, y=y_position)
#         return True

    def click_forget_this_printer_btn(self):
        '''
        This is a method to click forget printer button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_forget_this_printer_btn]-Click 'forget_printer' btn... ")

        self.driver.click("forget_this_printer_btn")

    def click_hide_printer_btn(self):
        '''
        This is a method to click forget printer button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[hide_printer_btn]-Click Hide Printer btn... ")

        self.driver.click("hide_printer_btn")

    def click_install_to_print_dialog_i_will_do_this_later_btn(self):
        '''
        This is a method to click I'll do this later button on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_install_to_print_dialog_i_will_do_this_later_btn]-Click I'll do this later button... ")

        self.driver.click("install_to_print_dialog_i_will_do_this_later_btn")

    def click_install_to_print_dialog_install_printer_btn(self):
        '''
        This is a method to click Install printer button on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_install_to_print_dialog_install_printer_btn]-Click Install printer button... ")

        self.driver.click("install_to_print_dialog_install_printer_btn")

    def get_value_of_printer_name(self):
        '''
        This is a method to get value of printer name.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_printer_name]-Get printer name...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_printer_status(self):
        '''
        This is a method to get value of printer_status.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_printer_status]-Get printer_status...  ")

        return self.driver.get_value("printer_status")

    def get_value_of_potg_job_count_number(self):
        '''
        This is a method to get value of Job Count number for POTG.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_potg_job_count_number]-Get printer_status...  ")

        return self.driver.get_value("private_pickup_files_number")

    def get_value_of_get_ink_tile(self):
        '''
        This is a method to get value of Get Ink Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_get_ink_tile]-Get value of Get Ink Tile...  ")

        return self.driver.get_value("get_ink_tile_text")

    def get_value_of_smart_tasks_tile(self):
        '''
        This is a method to get value of Shortcuts Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_smart_tasks_tile]-Get value of Shortcuts Tile...  ")

        return self.driver.get_value("smart_tasks_tile_text")

    def get_value_of_scan_tile(self):
        '''
        This is a method to get value of Scan Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_scan_tile]-Get value of Scan Tile...  ")

        return self.driver.get_value("scan_tile_text")

    def get_value_of_print_documents_tile(self):
        '''
        This is a method to get value of Print Documents Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_print_documents_tile]-Get value of Print Documents Tile...  ")

        return self.driver.get_value("print_document_tile_text")

    def get_value_of_print_photos_tile(self):
        '''
        This is a method to get value of Print Photos Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_print_photos_tile]-Get value of Print Photos Tile...  ")

        return self.driver.get_value("print_photo_tile_text")

    def get_value_of_mobile_fax_tile(self):
        '''
        This is a method to get value of Mobile Fax Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_mobile_fax_tile]-Get value of Mobile Fax Tile...  ")

        return self.driver.get_value("mobile_fax_tile_text")

    def get_value_of_help_support_tile(self, is_malbec_taccola_vasari=False):
        '''
        This is a method to get value of Help Support Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_help_support_tile]-Get value of Help Support Tile...  ")

        if not is_malbec_taccola_vasari:
            return self.driver.get_value("help_center_tile_text")
        else:
            return self.driver.get_value("7_help_center_tile_text")

    def get_value_of_printer_settings_tile(self, is_malbec_taccola_vasari=False):
        '''
        This is a method to get value of Printer Settings Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_printer_settings_tile]-Get value of Printer Settings Tile...  ")

        if not is_malbec_taccola_vasari:
            return self.driver.get_value("printer_settings_tile_text")
        else:
            return self.driver.get_value("8_printer_settings_tile_text")

    def get_value_of_potg_optimize_dialog_introducing_print_anywhere_text(self):
        '''
        This is a method to get value of Introducing print anywhere text on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_potg_optimize_dialog_introducing_print_anywhere_text]-Get value of Introducing print anywhere text...  ")

        return self.driver.get_value("potg_optimize_dialog_introducing_print_anywhere_text")

    def get_value_of_potg_optimize_dialog_send_files_text(self):
        '''
        This is a method to get value of Send files to printer text on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_potg_optimize_dialog_send_files_text]-Get value of Send files to printer text...  ")

        return self.driver.get_value("potg_optimize_dialog_send_files_text")

    def get_value_of_potg_optimize_dialog_optimize_printers_text(self):
        '''
        This is a method to get value of Optimize printers text on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_potg_optimize_dialog_optimize_printers_text]-Get value of Optimize printers text...  ")

        return self.driver.get_value("potg_optimize_dialog_optimize_printers_text")

    def get_value_of_potg_optimize_dialog_optimize_printers_btn(self):
        '''
        This is a method to get value of Optimize printers button on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_potg_optimize_dialog_optimize_printers_btn]-Get value of Optimize printers button...  ")

        return self.driver.get_title("potg_optimize_dialog_optimize_printers_btn")

    def get_value_of_potg_optimize_dialog_updating_settings_text(self):
        '''
        This is a method to get value of Updating settings text on POTG Optimize dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_potg_optimize_dialog_updating_settings_text]-Get value of Updating settings text...  ")

        return self.driver.get_value("potg_optimize_dialog_updating_settings_text")

    def get_value_of_install_to_print_dialog_title(self):
        '''
        This is a method to get value of Install to print dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_to_print_dialog_title]-Get value of Install to print dialog title...  ")

        return self.driver.get_value("install_to_print_dialog_title")

    def get_value_of_install_to_print_dialog_the_selected_printer_text(self):
        '''
        This is a method to get value of The selected printer text on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_to_print_dialog_the_selected_printer_text]-Get value of The selected printer text...  ")

        return self.driver.get_value("install_to_print_dialog_the_selected_printer_text")

    def get_value_of_install_to_print_dialog_please_install_the_printer_text(self):
        '''
        This is a method to get value of Please install the printer text on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_to_print_dialog_please_install_the_printer_text]-Get value of Please install the printer...  ")

        return self.driver.get_value("install_to_print_dialog_please_install_the_printer_text")

    def get_value_of_install_to_print_dialog_set_as_default_printer_checkbox(self):
        '''
        This is a method to get value of Set as default printer checkbox on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_to_print_dialog_set_as_default_printer_checkbox]-Get value of Set as default printer checkbox...  ")

        return self.driver.get_title("install_to_print_dialog_set_as_default_printer_checkbox")

    def get_value_of_install_to_print_dialog_i_will_do_this_later_btn(self):
        '''
        This is a method to get value of I'll do this later button on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_to_print_dialog_the_selected_printer_text]-Get value of I'll do this later button...  ")

        return self.driver.get_title("install_to_print_dialog_i_will_do_this_later_btn")

    def get_value_of_install_to_print_dialog_install_printer_btn(self):
        '''
        This is a method to get value of Install printer button on Install to print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_install_to_print_dialog_install_printer_btn]-Get value of Install printer button...  ")

        return self.driver.get_title("install_to_print_dialog_install_printer_btn")

# -------------------------------Verification Methods--------------------------
    def verify_printer_name_main_ui(self, printer_name):
        logging.debug("[MainUIScreen]:[verify_printer_name_main_ui]-Verify printer name on the main page... ")

        assert self.get_value_of_printer_name() == printer_name

    def verify_main_ui_with_installed_printer(self, printer_info):
        logging.debug("[MainUIScreen]:[verify_main_ui_with_installed_printer]-Verify Main page with Installed printer... ")

        self.verify_printer_name_main_ui(printer_info["printerName"])

    def verify_forget_this_printer_btn_notdisplay(self, timeout=1):
        '''
        verify_forget_this_printer_btn_notdisplay
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("forget_this_printer_btn", timeout=timeout, raise_e=False)

    def verify_instant_ink_tile(self, support=True):
        '''
        check Instant Ink tile on Main UI
        :parameter:
        :return:
        '''
        if(support):
            assert self.get_value_of_get_ink_tile() == ""
        else:
            assert self.get_value_of_get_ink_tile() == "Get Supplies"

    def verify_gothamappwindow_minimized(self):
        '''
        Verify gotham app was minimized
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("scan_tile", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")
        return True

    def check_printer_added(self):
        '''
        check printer added on main ui
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("add_printer_btn", raise_e=False):
            raise UnexpectedItemPresentException("the printer will not be added")
        return True

    def verify_shortcuts_tile_hidden(self, timeout=5):
        '''
        This is a verification method to verify Shortcuts tile is hidden on Main page.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("shortcuts_tile", format_specifier=['Shortcuts'], timeout=timeout, raise_e=False)

    def verify_mobile_fax_tile_hidden(self, timeout=5):
        '''
        This is a verification method to verify Mobile Fax tile is hidden on Main page.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("mobile_fax_tile", format_specifier=['Mobile Fax'], timeout=timeout, raise_e=False)

    def verify_printer_status(self, status):
        '''
        This is a verification method to check UI strings of printer_stauts.
        :parameter:
        :return:
        '''
        assert self.get_value_of_printer_status() == status

    def verify_printer_status_is_ready(self):
        '''
        This is a verification method to check UI strings of Printer Ready status.
        :parameter:
        :return:
        '''
        self.wait_for_printer_status_load(120)
        test_strings = smart_utility.get_local_strings_from_table(screen_name='main_ui')
        assert self.get_value_of_printer_status() == test_strings['ready_text']

    def verify_printer_status_is_offline(self):
        '''
        This is a verification method to check UI strings of Printer Offline status.
        :parameter:
        :return:
        '''
        self.wait_for_printer_status_load(120)
        test_strings = smart_utility.get_local_strings_from_table(screen_name='main_ui')
        assert self.get_value_of_printer_status() == test_strings['offline_text']

    def verify_printer_status_is_not_in_offline_status(self):
        '''
        This is a verification method to check UI strings of Printer is in Non-Offline status.
        :parameter:
        :return:
        '''
        self.wait_for_printer_status_load(120)
        test_strings = smart_utility.get_local_strings_from_table(screen_name='main_ui')
        assert self.get_value_of_printer_status() != test_strings['offline_text']

    def verify_potg_optimize_dialog(self):
        '''
        This is a verification method to check UI strings of POTG Optimize dialog.
        :parameter:
        :return:
        '''
        self.wait_for_potg_optimize_dialog_load(120)

        logging.debug("Start to check UI strings of POTG Optimize dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='potg_optimize_dialog')
#         assert self.get_value_of_potg_optimize_dialog_introducing_print_anywhere_text() == test_strings['introducing_print_anywhere_and_private_pickup_text']
#         assert self.get_value_of_potg_optimize_dialog_send_files_text() == test_strings['potg_optimize_dialog_send_files_text_1']
        assert self.get_value_of_potg_optimize_dialog_introducing_print_anywhere_text() == test_strings['introducing_print_anywhere_text']
        assert self.get_value_of_potg_optimize_dialog_send_files_text() == test_strings['potg_optimize_dialog_send_files_text_2']
        assert self.get_value_of_potg_optimize_dialog_optimize_printers_text() == test_strings['potg_optimize_dialog_optimize_printers_text']
        assert self.get_value_of_potg_optimize_dialog_optimize_printers_btn() == test_strings['potg_optimize_dialog_optimize_printers_btn']

    def verify_potg_optimize_updating_settings_dialog(self):
        '''
        This is a verification method to check UI strings of POTG Optimize Updating Settings dialog.
        :parameter:
        :return:
        '''
        self.wait_for_potg_optimize_updating_settings_dialog()

        logging.debug("Start to check UI strings of POTG Optimize Updating Settings dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='potg_optimize_dialog')
#         assert self.get_value_of_potg_optimize_dialog_introducing_print_anywhere_text() == test_strings['introducing_print_anywhere_and_private_pickup_text']
#         assert self.get_value_of_potg_optimize_dialog_send_files_text() == test_strings['potg_optimize_dialog_send_files_text_1']
        assert self.get_value_of_potg_optimize_dialog_introducing_print_anywhere_text() == test_strings['introducing_print_anywhere_text']
        assert self.get_value_of_potg_optimize_dialog_send_files_text() == test_strings['potg_optimize_dialog_send_files_text_2']
        assert self.get_value_of_potg_optimize_dialog_optimize_printers_text() == test_strings['potg_optimize_dialog_optimize_printers_text']
        assert self.get_value_of_potg_optimize_dialog_updating_settings_text() == test_strings['potg_optimize_dialog_updating_settings_text']

    def verify_potg_optimize_dialog_is_not_seen(self, timeout=3):
        '''
        This is a verification method to verify POTG Optimize dialog is not seen.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("potg_optimize_dialog_introducing_print_anywhere_text", timeout=timeout, raise_e=False)

    def verify_printer_image_disappear(self):
        '''
        This is a verification method to check Horget Printer dialog dismiss after clicking hide printer button.
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("printer_image", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")

        return True

    def verify_add_your_first_printer_text(self):
        '''
        This is a verification method to check Add your first printer display after clicking hide printer button.
        :parameter:
        :return:
        '''
        self.wait_for_add_your_first_printer_text_load()
        test_strings = smart_utility.get_local_strings_from_table(screen_name='main_ui')
        assert self.driver.get_value("add_your_first_printer_text") == test_strings['add_your_first_printer_text']

    def verify_install_to_print_dialog(self):
        '''
        This is a verification method to check UI strings of Install to print dialog.
        :parameter:
        :return:
        '''
        self.wait_for_install_to_print_dialog_load(60)

        logging.debug("Start to check UI strings of Install to print dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='install_to_print_dialog')
        assert self.get_value_of_install_to_print_dialog_title() == test_strings['install_to_print_dialog_title']
        assert self.get_value_of_install_to_print_dialog_the_selected_printer_text() == test_strings['install_to_print_dialog_the_selected_printer_text']
        assert self.get_value_of_install_to_print_dialog_please_install_the_printer_text() == test_strings['install_to_print_dialog_please_install_the_printer_text']
        assert self.get_value_of_install_to_print_dialog_set_as_default_printer_checkbox() == test_strings['install_to_print_dialog_set_as_default_printer_checkbox']
        assert self.get_value_of_install_to_print_dialog_i_will_do_this_later_btn() == test_strings['install_to_print_dialog_i_will_do_this_later_btn']
        assert self.get_value_of_install_to_print_dialog_install_printer_btn() == test_strings['install_to_print_dialog_install_printer_btn']

