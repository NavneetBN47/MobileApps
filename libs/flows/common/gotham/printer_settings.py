import time
import re
import pytest

from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.common.exceptions import NoSuchElementException
import MobileApps.resources.const.windows.const as w_const


class PrinterSettings(GothamFlow):
    flow_name = "printer_settings"

    STATUS = "print_status_report_option"
    DEMO = "demo_page_option"
    DIAGNOSTIC = "print_diagnostic_info_option"
    NETWORK = "network_configuration_report_option"
    WIRELESS = "wireless_test_report_option"
    QUALITY = "print_quality_report_option"
    WEB = "web_access_report_option"

    PRINTER_STATUS = "printer_status_opt"
    SUPPLY_STATUS = "supply_status_opt"
    PRINTER_INFO = "printer_information_opt"
    NETWORK_INFO = "network_information_opt"
    PRINTER_REPORTS = "printer_reports_opt"
    PRINT_QUALITY = "print_quality_tools_opt"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def get_name_detail_text(self):
        return self.driver.get_attribute("printer_info_name_value", "Name")

    def get_model_name_text(self):
        return self.driver.get_attribute("printer_info_model_name_value", "Name")
    
    # ****************Printer Status********************
    def select_printer_status_item(self):
        self.driver.click("printer_status_opt", timeout=20)

    # ****************Supply Status********************
    def select_supply_status_option(self):
        self.driver.click("supply_status_opt")
    # ****************security status********************
    def select_security_status_opt(self):
        self.driver.click("security_status_opt")

    def select_smart_security_toggle(self):
        self.driver.click("smart_security_toggle")

    def select_stay_protected_btn(self):
        self.driver.click("stay_protected_btn")

    def select_remove_security_btn(self):
        self.driver.click("remove_security_btn")

    def select_get_protected_btn(self):
        self.driver.click("get_protected_btn")

    def select_close_btn(self):
        self.driver.click("close_btn")
    # ****************Advanced setting********************
    def select_advanced_settings_item(self, change_check=None, retry=3):
        self.driver.click("advanced_settings_opt", change_check=change_check, retry=retry)

    # ****************Hide Printer********************
    def select_hide_printer_item(self):
        self.driver.swipe("hide_printer_opt")
        self.driver.click("hide_printer_opt")

    def select_hide_this_printer_btn(self):
        self.driver.click("hide_this_printer_btn")

    # ****************Print Reports********************
    def select_printer_reports(self):
        self.driver.click("printer_reports_opt")

    def select_report_opt(self, name):
        self.driver.click(name)

    def click_report_print_btn(self):
        self.driver.click("report_print_btn")

    def click_report_close_btn(self):
        self.driver.click("report_close_btn")

    def click_retry_btn(self):
        self.driver.click("retry_btn")
    
    def hover_reports_item(self, item):
        self.driver.hover(item)

    # ****************Print Quality Tools********************
    def select_print_quality_tools(self):
        self.driver.click("print_quality_tools_opt")

    def click_cleaning_done_btn(self):
        self.driver.click("cleaning_done_btn")

    def click_cleaning_second_btn(self):
        self.driver.click("second_level_clean_btn")

    def click_cleaning_third_btn(self):
        self.driver.click("third_level_clean_btn")

    def click_cleaning_close_btn(self):
        self.driver.click("cleaning_close_btn")

    def click_clean_printheads_btn(self, raise_e=False):
        self.driver.click("clean_printheads_btn", timeout=20, raise_e=raise_e)

    def click_align_printheads_btn(self, raise_e=False):
        self.driver.click("align_printheads_btn", timeout=20, raise_e=raise_e)

    def click_print_alignment_page_btn(self):
        self.driver.click("print_alignment_page_btn")

    def click_print_next_btn(self):
        self.driver.click("align_next_btn", timeout=20)

    def click_scan_alignment_page_btn(self):
        self.driver.click("scan_alignment_page_btn")

    def click_scan_exit_btn(self):
        self.driver.click("align_exit_btn")

    def click_complete_close_btn(self):
        self.driver.click("complete_close_btn")

    def click_dialog_cancel_btn(self):
        self.driver.click("dialog_cancel_btn", displayed=False, timeout=10)

    def click_dialog_cancel_print_btn(self):
        self.driver.click("cancel_print_btn", timeout=10)

    def click_alignment_back_btn(self):
        self.driver.click("align_back_btn")

    def click_unable_align_back_btn(self):
        self.driver.click("unable_align_back_btn")

    # ****************Printer Information********************
    def select_printer_information(self):
        self.driver.click("printer_information_opt")

    def get_printer_infor_status(self, timeout=10):
        return self.driver.get_attribute("printer_info_status_value", attribute="Name", timeout=timeout)

    def click_status_circle_btn(self, timeout=10):
        self.driver.click("status_circle_btn", timeout=timeout)

    def click_country_dropdown(self):
        self.driver.click("country_region_box")

    def click_language_dropdown(self):
        self.driver.click("language_box")

    def click_preferences_title(self):
        self.driver.click("preferences_title")

    def click_country_region_index(self, index):
        self.driver.click("dynamic_country_region_index", format_specifier=[index])

    def get_country_region_text(self):
        return self.driver.get_attribute("dynamic_country_region_index", format_specifier=[1], attribute="Name")

    def select_country_item(self, country, raise_e=True):
        return self.driver.click("dynamic_text", format_specifier=[country], raise_e=raise_e)

    def click_language_index(self, index):
        self.driver.click("dynamic_language_index", format_specifier=[index])

    def get_language_text(self):
        return self.driver.get_attribute("dynamic_language_index", format_specifier=[1], attribute="Name")

    def select_language_item(self, language, raise_e=True):
        return self.driver.click("dynamic_text", format_specifier=[language], raise_e=raise_e)

    def click_set_cancel_btn(self):
        self.driver.click("cancel_btn")

    def click_set_save_btn(self):
        self.driver.click("save_btn")

    def edit_sign_in_password(self, password):
        self.driver.send_keys("sign_in_edit_box", password) 

    def click_sign_in_submit_btn(self):
        self.driver.click("sign_in_submit_btn")

    def click_sign_in_cancel_btn(self):
        self.driver.click("sign_in_cancel_btn")

    def click_quick_reference_btn(self):
        self.driver.click("quick_reference_btn")
    
    def get_quick_reference_text(self):
        return self.driver.get_attribute("quick_reference_btn", attribute="Name")

    def click_the_pin_ok_btn(self):
        self.driver.click("the_pin_ok_btn")

    def check_country_box_expand(self):
        return self.driver.get_attribute("country_region_box", attribute="ExpandCollapsePattern.ExpandCollapseState")

    def check_language_expand(self):
        return self.driver.get_attribute("language_box", attribute="ExpandCollapsePattern.ExpandCollapseState")

    # ****************Network Information********************
    def select_network_information(self, raise_e=True):
        return self.driver.click("network_information_opt", raise_e=raise_e)

    # ****************Print Anywhere********************
    def select_print_anywhere(self):
        self.driver.click("print_anywhere_opt")

    def click_privacy_pickup_toggle(self):
        self.driver.click("paw_private_pickup_toggle")

    def click_allow_printing_toggle(self):
        self.driver.click("paw_allow_printing_toggle")

    def select_next_button(self):
        self.driver.click("print_anywhere_next_btn")

    def select_done_button(self):
        self.driver.click("print_anywhere_next_btn")
        
    def enable_useca2(self):
        app_name = eval("w_const.PACKAGE_NAME." + pytest.default_info)
        if (fh := self.driver.ssh.remote_open(r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name), mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            data = re.sub("</Misc>", "<MiscFeatures>UseCA2</MiscFeatures></Misc>", data)
            fh = self.driver.ssh.remote_open(r"C:\Users\exec\AppData\Local\Packages\{}\LocalState\Logs\LoggingData.xml".format(app_name), mode="w")
            fh.write(data)
            fh.close()
            time.sleep(1)
            self.driver.restart_app()

    def switch_private_pickup_toggle(self, toggle):
        if self.verify_paw_private_pickup_toggle() == 0 and toggle.lower() == 'on':
            self.click_privacy_pickup_toggle()
            assert self.verify_paw_private_pickup_toggle() == 1
        elif self.verify_paw_private_pickup_toggle() == 1 and toggle.lower() == 'off':
            self.click_privacy_pickup_toggle()
            assert self.verify_paw_private_pickup_toggle() == 0

    def switch_printing_anywhere_toggle(self, toggle):
        if self.verify_paw_allow_printing_toggle() == 0 and toggle.lower() == 'on':
            self.click_allow_printing_toggle()
            assert self.verify_paw_allow_printing_toggle() == 1
        elif self.verify_paw_allow_printing_toggle() == 1 and toggle.lower() == 'off':
            self.click_allow_printing_toggle()
            assert self.verify_paw_allow_printing_toggle() == 0

    def restore_print_anywhere_toggle(self):
        self.verify_print_anywhere_option_display()
        self.select_print_anywhere()
        self.verify_print_anywhere_screen()
        self.switch_private_pickup_toggle(toggle='off')
        self.switch_printing_anywhere_toggle(toggle='on')

    # ****************Advanced settings********************
    def click_network_summary_tile(self):
        self.driver.click("network_summary_tile")

    def click_ews_home_title(self):
        self.driver.click("ews_home_title")

    def enter_pin_num(self, pin_num):
        """
        Input pin number on EWS screen
        """
        self.driver.click("pin_num_box")
        
    def click_submit_btn(self):
        self.driver.click("submit_btn")

    # ****************select each option********************
    def select_printer_settings_opt(self, each_opt):
        self.driver.click(each_opt)

    # ****************Shortcuts option********************
    def select_shortcuts_option(self):
        self.driver.click("shortcuts_item_opt")

    # ---------------- Private Pickup File(s) ---------------- #
    def click_pp_del_button(self):
        return self.driver.click("pp_del_btn", raise_e=False)

    def click_pp_del_button(self):
        return self.driver.click("pp_del_btn", raise_e=False)

    def click_dialog_del_button(self):
        self.driver.click("dialog_del_btn", raise_e=False)

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_printer_settings_page(self, timeout=25, raise_e=True):
        return self.driver.wait_for_object("left_list", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("printer_info_title", raise_e=raise_e)

    def verify_status_tile(self, is_remote=False):
        self.driver.wait_for_object("status_group")
        self.driver.wait_for_object("supply_status_opt")
        if not is_remote:
            self.driver.wait_for_object("printer_status_opt")
        else:
            self.driver.wait_for_object("security_status_opt")
            assert self.driver.wait_for_object("printer_status_opt", raise_e=False) is False

    def verify_information_tile(self , is_remote=False):
        self.driver.wait_for_object("information_group")
        self.driver.wait_for_object("printer_information_opt")
        if not is_remote:
            self.driver.wait_for_object("network_information_opt")
        else:
            assert self.driver.wait_for_object("network_information_opt", raise_e=False) is False

    def verify_settings_tile(self):
        self.driver.wait_for_object("settings_group")
        self.driver.wait_for_object("advanced_settings_opt")

    def verify_tools_tile(self):
        self.driver.wait_for_object("tools_group")
        self.driver.wait_for_object("printer_reports_opt")
        self.driver.wait_for_object("print_quality_tools_opt")
        self.driver.wait_for_object("see_what_printing_opt", format_specifier=['See What\'s Printing'])

    def verify_manage_tile(self):
        self.driver.wait_for_object("manage_group")
        self.driver.wait_for_object("print_from_other_devices_opt")
        self.driver.wait_for_object("hide_printer_opt", displayed=False)

    def verify_print_anywhere_option_is_hidden(self):
        assert self.driver.wait_for_object("print_anywhere_opt", raise_e=False) is False

    def verify_advanced_settings_item(self, raise_e=True):
        return self.driver.wait_for_object("advanced_settings_opt", raise_e=raise_e)

    def verify_hide_this_printer_screen(self):
        self.driver.wait_for_object("hide_this_printer_title")
        self.driver.wait_for_object("hide_this_printer_body")
        self.driver.wait_for_object("hide_this_printer_btn")

    def verify_advanced_settings_item_is_hidden(self):
        return self.driver.wait_for_object("advanced_settings_opt", raise_e=False) is False

    def verify_print_anywhere_option_display(self):
        self.driver.wait_for_object("print_anywhere_opt")

    def verify_printer_reports_is_hidden(self):
        assert self.driver.wait_for_object("printer_reports_opt", raise_e=False) is False

    def verify_print_quality_tools_option_is_hidden(self):
        assert self.driver.wait_for_object("print_quality_tools_opt", raise_e=False) is False

    def verify_see_what_printing_option_is_hidden(self):
        assert self.driver.wait_for_object("see_what_printing_opt", format_specifier=['See What\'s Printing'], raise_e=False) is False

    def verify_print_from_other_devices_is_hidden(self):
        assert self.driver.wait_for_object("print_from_other_devices_opt", raise_e=False) is False

    def verify_supply_status_opt_is_hidden(self):
        assert self.driver.wait_for_object("supply_status_opt", raise_e=False) is False

    def verify_network_information_not_available(self):
        assert self.driver.get_attribute("network_information_opt", attribute="SelectionItem.IsSelected").lower() == "false"

    def verify_advanced_settings_not_available(self):
        assert self.driver.get_attribute("advanced_settings_opt", attribute="SelectionItem.IsSelected").lower() == "false"

    def verify_all_the_opt_not_available_in_tools_tile(self):
        assert self.driver.get_attribute("printer_reports_opt", attribute="SelectionItem.IsSelected").lower() == "false"
        assert self.driver.get_attribute("print_quality_tools_opt", attribute="SelectionItem.IsSelected").lower() == "false"
        assert self.driver.get_attribute("see_what_printing_opt", format_specifier=['See What\'s Printing'], attribute="SelectionItem.IsSelected").lower() == "false"
    
    def verify_shortcuts_item(self, invisible=True):
        self.driver.wait_for_object("shortcuts_item_opt", invisible=invisible)

    def verify_security_status_opt(self):
        self.driver.wait_for_object("security_status_opt")

    def verify_security_status_opt_is_hidden(self):
        assert self.driver.wait_for_object("security_status_opt", raise_e=False) is False

    # ****************Print Reports********************
    def verify_print_status_unknown_dialog(self):
        self.driver.wait_for_object("fix_this_problem_text")
        self.driver.wait_for_object("dialog_cancel_btn")
        self.driver.wait_for_object("retry_btn")
    
    def verify_cancel_print_dialog(self, invisible=False, raise_e=True, timeout=15):
        return self.driver.wait_for_object("progress_bar", invisible=invisible, raise_e=raise_e, timeout=timeout) and\
        self.driver.wait_for_object("cancel_print_btn", invisible=invisible, raise_e=raise_e, timeout=timeout)

    def verify_printer_reports_page(self):
        self.driver.wait_for_object("report_title")
        self.driver.wait_for_object("report_print_btn")

    def verify_this_feature_is_not_available_screen(self, raise_e=False):
        return self.driver.wait_for_object("this_feature_is_not_available_text", raise_e=raise_e)

    def get_printer_reports_items(self, item):
        return self.driver.wait_for_object(item, timeout=2, raise_e=False)

    def verify_printer_reports_available(self, raise_e=False):
        return self.driver.wait_for_object("report_print_name", raise_e=raise_e, timeout=10)
    
    def verify_printing_is_completed_dialog(self, raise_e=True):
        return self.driver.wait_for_object("printing_is_title", raise_e=raise_e, timeout=25) and\
        self.driver.wait_for_object("report_close_btn", raise_e=raise_e)

    def verify_door_open_dialog(self, raise_e=False):
        return self.driver.wait_for_object("door_open_title", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", raise_e=raise_e)

    def verify_unable_to_connect_dialog(self, raise_e=False):
        return self.driver.wait_for_object("unable_to_connect_title", raise_e=raise_e) and\
        self.driver.wait_for_object("fix_this_problem_text", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", raise_e=raise_e)

    # ****************Print Quality Tools********************
    def verify_print_quality_tools_page(self):
        self.driver.wait_for_object("print_quality_tools_title")

    def verify_clean_printheads_part(self, raise_e=True):
        return self.driver.wait_for_object("clean_printheads_btn", raise_e=raise_e)

    def verify_align_printheads_part(self, raise_e=True):
        return self.driver.wait_for_object("align_printheads_btn", raise_e=raise_e)

    def verify_this_feature_is_not_screen(self, raise_e=False):
        return self.driver.wait_for_object("this_feature_is_not_text", raise_e=raise_e)
    
    def verify_cleaning_dialog_1(self, raise_e=True):
        return self.driver.wait_for_object("progress_bar", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("cleaning_is_in_progress_text", invisible=True, timeout=120, raise_e=raise_e)

    def verify_cleaning_dialog_2(self):
        self.driver.wait_for_object("printing_is_in_progress_text", invisible=True, timeout=30)

    def your_device_is_busy_dialog(self, raise_e=False):
        return self.driver.wait_for_object("your_device_is_busy_title", raise_e=raise_e) and\
        self.driver.wait_for_object("please_wait_for_text", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", raise_e=raise_e)
    
    def verify_second_cleaning_dialog(self):
        self.driver.wait_for_object("second_level_clean_btn", timeout=25)
        self.driver.wait_for_object("cleaning_done_btn")

    def verify_third_cleaning_dialog(self, raise_e=False):
        return self.driver.wait_for_object("third_level_clean_btn", timeout=25, raise_e=raise_e) and\
        self.driver.wait_for_object("cleaning_done_btn", raise_e=raise_e)

    def verify_cleaning_complete_dialog(self, raise_e=False):
        return self.driver.wait_for_object("cleaning_complete_title", raise_e=raise_e) and\
        self.driver.wait_for_object("cleaning_complete_body", raise_e=raise_e) and\
        self.driver.wait_for_object("complete_close_btn", raise_e=raise_e)

    def verify_printing_dialog(self, invisible=True):
        self.driver.wait_for_object("dialog_cancel_btn", displayed=False)
        self.driver.wait_for_object("printing_the_alignment_text", invisible=invisible, timeout=120)
    
    def verify_another_alignment_dialog(self, raise_e=False):
        return self.driver.wait_for_object("alignment_title", raise_e=raise_e) and\
        self.driver.wait_for_object("another_alignment_text", raise_e=raise_e) and\
        self.driver.wait_for_object("complete_close_btn", raise_e=raise_e)

    def alignment_is_not_finished_dialog(self, raise_e=False):
        return self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", raise_e=raise_e)

    def verify_print_alignment_dialog(self, raise_e=True):
        return self.driver.wait_for_object("print_alignment_page_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("align_next_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("align_back_btn", raise_e=raise_e)

    def verify_scan_alignment_dialog(self, raise_e=True):
        return self.driver.wait_for_object("align_exit_btn", raise_e=raise_e, timeout=40) and\
        self.driver.wait_for_object("scan_alignment_page_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("align_back_btn", raise_e=raise_e)

    def verify_dialog_disappear(self):
        assert self.driver.wait_for_object("progress_bar", raise_e=False, timeout=2) is False

    def verify_alignment_complete_dialog(self, raise_e=True):
        return self.driver.wait_for_object("complete_close_btn", raise_e=raise_e, timeout=5)

    def verify_unable_to_align_dialog(self, raise_e=True):
        return self.driver.wait_for_object("unable_align_back_btn", raise_e=raise_e, timeout=40)

    def verify_scanning_dialog(self, invisible=True):
        self.driver.wait_for_object("dialog_cancel_btn", displayed=False)
        self.driver.wait_for_object("scanning_title", invisible=invisible, timeout=120)

    # ***************Supply Status********************
    def verify_supply_status_page(self, timeout=25, raise_e=False):
        if self.driver.wait_for_object("i_accept_btn", timeout=timeout, raise_e=False):
            self.driver.click("i_accept_btn")
        return self.driver.wait_for_object("supply_status_page", timeout=timeout, raise_e=raise_e) or \
        self.driver.wait_for_object("try_it_free_link", timeout=timeout, raise_e=raise_e) or \
        self.driver.wait_for_object("finish_setup_link", timeout=timeout, raise_e=raise_e)

    # ***************Printer Status********************
    def verify_printer_status_page(self, is_printer_online=True, is_installed=True):
        self.driver.wait_for_object("device_image", timeout=25)
        self.driver.wait_for_object("device_state_text")
        if not is_printer_online:
            assert self.driver.get_attribute("device_state_text", attribute="Name") == "Offline"
            if is_installed:
                self.driver.wait_for_object("diagnose_fix_btn")
            else:
                assert self.driver.wait_for_object("diagnose_fix_btn", raise_e=False) is False
    
    # ****************Network Information********************    
    def verify_network_info_page(self, bon_name, ip, host_name, ssid, is_dune=False):
        self.driver.wait_for_object("wireless_title")
        self.driver.wait_for_object("wireless_text")    
        assert self.driver.get_attribute("wireless_status_text", attribute="Name") == "Status"
        wireless_detail_text = self.driver.get_attribute("wireless_detail_text", attribute="Name")
        wireless_status_detail_text = self.driver.get_attribute("wireless_status_detail_text", attribute="Name")
        self.driver.wait_for_object("bonjour_name_text")
        bon_detail_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Bonjour Name'], attribute="Name")
        assert bon_detail_text == bon_name
        self.driver.wait_for_object("ip_address_text")
        ip_detail_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['IP Address'], attribute="Name") 
        assert ip_detail_text == ip 
        self.driver.wait_for_object("mac_address_text")
        self.driver.wait_for_object("host_name_text")
        host_detail_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Host Name'], attribute="Name")
        assert host_detail_text == host_name             
        if self.driver.wait_for_object("bluetooth_low_energy_title", raise_e=False):
            assert self.driver.get_attribute("bluetooth_status_text_1", attribute="Name") == "Status"
            bluetooth_text = self.driver.get_attribute("bluetooth_status_text_2", attribute="Name")
            if not bluetooth_text in ["On", "Off"]:
                raise NoSuchElementException("Bluetooth Low Energy Status shows incorrect")       
        assert self.driver.wait_for_object("wifi_direct_text", raise_e=False) is False

        if is_dune:
            wireless_detail_text == "Off"
            wireless_status_detail_text == "Not connected"
            self.driver.wait_for_object("ethernet_title")
            assert self.driver.get_attribute("ethernet_status_text_1", attribute="Name") == "Status"
            assert self.driver.get_attribute("ethernet_status_text_2", attribute="Name") == "Connected"   
        else:
            wireless_detail_text == "On"
            wireless_status_detail_text == "Connected"
            self.driver.wait_for_object("network_name_text")
            ssid_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Network Name (SSID)'], attribute="Name")
            assert ssid_text == ssid  
      
            if self.driver.wait_for_object("ethernet_title", raise_e=False):
                assert self.driver.get_attribute("ethernet_status_text_1", attribute="Name") == "Status"
                ethernet_text = self.driver.get_attribute("ethernet_status_text_2", attribute="Name")
                if not ethernet_text in ["Supported", "Not supported", "Not connected", "Connected"]:
                    raise NoSuchElementException("Ethernet Status shows incorrect")
                 
    # ****************Printer Information********************
    def verify_quick_reference_btn(self, raise_e=True):
        return self.driver.wait_for_object("quick_reference_btn", raise_e=raise_e)

    def verify_status_text(self, status, timeout=3, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[status], timeout=timeout, raise_e=raise_e)
    
    def verify_installation_status_text(self):
        return self.driver.get_attribute("get_dynamic_text", format_specifier=['Installation Status:'], attribute="Name")

    def verify_printer_info_must_part(self, host_name, model_name, status='Ready', con_status='Active', ip=False):
        assert self.driver.get_attribute("quick_reference_btn", attribute="Name") == 'Quick Reference'
        self.driver.wait_for_object("name_title")
        name_info = self.driver.get_attribute("get_dynamic_text", format_specifier=['Name:'], attribute="Name")
        if '(' in name_info:
            assert host_name in name_info
        self.driver.wait_for_object("status_title")
        status_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Status:'], attribute="Name")        
        if status == 'Printer offline':
            assert status_text == status
        elif status != 'Finish Setup':
            assert status_text in ['HP Cartridges Installed', 'Ready', 'Printer is Asleep', status]
        self.driver.wait_for_object("status_circle_btn", timeout=25)
        self.driver.wait_for_object("model_name_title", timeout=25)
        self.driver.wait_for_object("dynamic_text", format_specifier=[model_name])
        self.driver.wait_for_object("installation_status_title")
        installation = self.verify_installation_status_text()
        assert installation in ['Installed', 'Not installed']
        self.driver.wait_for_object("connection_type_title")
        self.driver.wait_for_object("network_text")
        self.driver.wait_for_object("connection_status_title")
        self.driver.wait_for_object("dynamic_text", format_specifier=[con_status])
        if ip:
            self.driver.wait_for_object("ip_address_title", timeout=20)
            self.driver.wait_for_object("dynamic_text", format_specifier=[ip])
            
    def verify_printer_info_optional_part(self, name, num, vesion, id):
        if self.driver.wait_for_object("host_name_title", raise_e=False):
            self.driver.wait_for_object("dynamic_text", format_specifier=[name])
        if self.driver.wait_for_object("serial_number_title", raise_e=False):
            self.driver.wait_for_object("dynamic_text", format_specifier=[num])
        if self.driver.wait_for_object("service_id_title", raise_e=False):
            self.driver.wait_for_object("dynamic_text", format_specifier=[id])
        if self.driver.wait_for_object("firmware_version_title", raise_e=False):
            self.driver.wait_for_object("dynamic_text", format_specifier=[vesion])

        optional_title_list = ["mac_address_title", "product_number_title", "tp_number_title"]
        for optional_title in optional_title_list:
            if self.driver.wait_for_object(optional_title, raise_e=False):
                title_name = self.driver.get_attribute(optional_title, attribute="Name")
                self.driver.wait_for_object("dynamic_text", format_specifier=[title_name])

    def verify_preference_part(self, timeout=25):
        if self.driver.wait_for_object("preferences_title", timeout=timeout, raise_e=False):
            self.verify_preference_country_part()
            self.verify_preference_language_part()
        else:
            return False

    def verify_preference_country_part(self):
        self.driver.wait_for_object("country_region_title")
        self.driver.wait_for_object("country_region_box")

    def verify_country_select_item(self, cou='United States', timeout=2, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[cou], timeout=timeout, raise_e=raise_e)

    def verify_preference_language_part(self):
        self.driver.wait_for_object("language_title")
        self.driver.wait_for_object("language_box")
        self.driver.click("language_title")
        self.driver.swipe()
        self.driver.wait_for_object("notice_text")

    def verify_language_select_item(self, lan='English', timeout=2, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[lan], timeout=timeout, raise_e=raise_e)

    def verify_set_country_or_language_dialog(self, timeout=2, raise_e=True):
        return self.driver.wait_for_object("cancel_btn", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("save_btn", timeout=timeout, raise_e=raise_e)

    def verify_sign_in_to_dialog(self, raise_e=True):
        return self.driver.wait_for_object("sign_in_edit_box", raise_e=raise_e)

    def verify_invalid_pin_code_text(self):
        return self.driver.wait_for_object("invalid_pin_code_text", raise_e=False)

    def verify_the_pin_incorrect_dialog(self, timeout=2, raise_e=False):
        return self.driver.wait_for_object("the_pin_you_entered_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("to_protect_your_security_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("the_pin_ok_btn", timeout=timeout, raise_e=raise_e)

    def verify_printer_info_status(self, status, timeout=25, raise_e=True):
        return self.driver.wait_for_object("printer_info_status", format_specifier=[status], timeout=timeout, raise_e=raise_e)

    # ****************Privacy Preferences********************
    def verify_privacy_preferences_tile(self, raise_e=True):
        return self.driver.wait_for_object("privacy_preferences_opt", raise_e=raise_e)

    # ****************Print Anywhere********************
    def verify_print_anywhere_screen(self):
        self.driver.wait_for_object("print_anywhere_title")
        if self.driver.wait_for_object("i_accept_btn", timeout=25, raise_e=False):
            self.driver.click("i_accept_btn")
        self.driver.wait_for_object("paw_private_pickup_toggle")
        self.driver.wait_for_object("paw_allow_printing_toggle")

    def verify_how_to_use_paw_screen(self):
        self.driver.wait_for_object("print_anywhere_title")
        if self.driver.wait_for_object("i_accept_btn", timeout=20, raise_e=False):
            self.driver.click("i_accept_btn")
        self.driver.wait_for_object("print_anywhere_next_btn", timeout=20)

    def verify_how_to_use_private_pickup_screen(self):
        self.driver.wait_for_object("print_anywhere_next_btn", timeout=20)

    def verify_you_are_ready_to_paw_screen(self):
        self.driver.wait_for_object("print_anywhere_done_btn", timeout=20)

    def verify_paw_private_pickup_toggle(self):
        return int(self.driver.get_attribute("paw_private_pickup_toggle", "Toggle.ToggleState"))

    def verify_paw_allow_printing_toggle(self):
        return int(self.driver.get_attribute("paw_allow_printing_toggle", "Toggle.ToggleState"))


    # ****************Advanced settings********************
    def verify_continuing_to_your_printer_settings_dialog(self, raise_e=False):
        return self.driver.wait_for_object("continuing_to_your_printer_title", raise_e = raise_e)

    def verify_ews_page(self):
        self.driver.wait_for_object("ews_home_title")

    def verify_tile_are_locked(self):
        self.driver.wait_for_object("locked_image")

    def verify_log_in_with_pin_dialog(self, invisible=False, raise_e=True):
        return self.driver.wait_for_object("log_in_pin_dialog_title", invisible=invisible, raise_e=raise_e)
   
    def verify_incorrect_pin_text_display(self):
        self.driver.wait_for_object("incorrect_pin_text")

    def verify_sign_in_text_display(self):
        self.driver.wait_for_object("sign_in_text")

    def verify_sign_out_text_display(self):
        self.driver.wait_for_object("sign_out_text")

    # ****************security status********************
    def verify_security_status_page(self):
        self.driver.wait_for_object("smart_security_toggle", timeout=60)

    def verify_smart_security_toggle_status(self, by_default=True):
        """
        Verify "password protection" option is ON or OFF
        """
        toggle = self.driver.wait_for_object("smart_security_toggle")
        if by_default:
            assert toggle.get_attribute("Toggle.ToggleState") == "1"
        else:
            assert toggle.get_attribute("Toggle.ToggleState") == "0"

    def verify_hp_smart_security_protects_dialog(self):
        self.driver.wait_for_object("hp_smart_security_protects_title")

    def verify_security_not_monitroed_text(self):
        self.driver.wait_for_object("security_not_monitroed_title", timeout=30)

    def verify_security_monitroed_text(self):
        self.driver.wait_for_object("security_monitroed_title", timeout=30)

    # ---------------- Private Pickup File(s) ---------------- #
    def verify_private_pickup_screen(self, no_files=False):
        if self.driver.wait_for_object("i_accept_btn", timeout=25, raise_e=False):
            self.driver.click("i_accept_btn")
        self.driver.wait_for_object("private_pickup_title")
        self.driver.wait_for_object("setting_btn")

    def verify_no_files_print(self):
        return self.driver.wait_for_object("ready_to_text", raise_e=False)

    def verify_are_you_sure_dialog(self):
        self.driver.wait_for_object("dialog_del_btn")
        self.driver.wait_for_object("dialog_cancel_btn")

    def verify_are_you_sure_dialog(self):
        self.driver.wait_for_object("dialog_del_btn")
        self.driver.wait_for_object("dialog_cancel_btn")
