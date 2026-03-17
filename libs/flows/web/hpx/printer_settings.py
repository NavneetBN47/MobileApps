import time
import re
import pytest
import logging
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from selenium.common.exceptions import NoSuchElementException


class PrinterSettings(HPXFlow):
    flow_name = "printer_settings"

    PRINTER_STATUS = "printer_status_opt"
    SUPPLY_STATUS = "supply_status_opt"
    PRINTER_INFO = "printer_information_opt"
    NETWORK_INFO = "network_information_opt"
    PRINTER_REPORTS = "printer_reports_opt"
    PRINT_QUALITY = "print_quality_tools_opt"

    STATUS = "print_status_report_option"
    DEMO = "demo_page_option"
    DIAGNOSTIC = "print_diagnostic_info_option"
    NETWORK = "network_configuration_report_option"
    WIRELESS = "sub_wireless_network_test_report_option"
    QUALITY = "print_quality_report_option"
    WEB = "web_access_test_report_option"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_top_back_arrow(self):
        self.driver.click("top_back_arrow", change_check={"wait_obj": "top_back_arrow", "invisible": True}, retry=2, delay=1)

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

    def click_sign_in_link(self):
        self.driver.click("sign_in_text")

    # ****************Hide Printer********************
    def select_hide_printer_item(self):
        self.driver.swipe("hide_printer_opt")
        self.driver.click("hide_printer_opt")

    def select_hide_this_printer_btn(self):
        self.driver.click("hide_this_printer_btn")

    # ****************Print Reports********************
    def select_printer_reports(self):
        if self.driver.click("printer_reports_opt", change_check={"wait_obj": "report_title"}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("printer_reports_opt", timeout=2)
            el.send_keys(Keys.ENTER)

    def select_report_opt(self, opt, raise_e=True):
        if opt == 'STATUS':
            opt = "print_status_report_option"
        elif opt == 'DIAGNOSTIC':
            opt = "print_diagnostic_info_option"
        elif opt == 'NETWORK':
            opt = "network_configuration_report_option"
        elif opt == 'WIRELESS':
            opt = "wireless_network_test_report_option"
        elif opt == 'QUALITY':
            opt = "print_quality_report_option"
        elif opt == 'WEB':
            opt = "web_access_test_report_option"
        elif opt == 'DEMO':
            opt = "demo_page_option"
        result = self.driver.click(opt, raise_e=False)
        if result is False:
            if raise_e:
                pytest.skip(f"Skip this test as {opt} report option is not available")
            else:
                return False
        return result

    def click_report_print_btn(self):
        self.driver.swipe(distance=8)
        if self.driver.click("report_print_btn", change_check={"wait_obj": "dialog_cancel_btn"}, retry=2, delay=1,  raise_e=False) is False:
            el = self.driver.wait_for_object("report_print_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_report_ok_btn(self, raise_e=True):
        return self.driver.click("report_ok_btn", raise_e=raise_e)

    def click_retry_btn(self):
        self.driver.click("retry_btn")
    
    def hover_reports_item(self, item):
        self.driver.hover(item)

    def click_dialog_cancel_btn(self, raise_e=True):
        return self.driver.click("dialog_cancel_btn", displayed=False, raise_e=raise_e)

    def click_dialog_cancel_print_btn(self):
        self.driver.click("cancel_print_btn")

    # ****************Print Quality Tools********************
    def select_print_quality_tools(self, retry=3):
        self.driver.click("print_quality_tools_opt", retry=retry, delay=1)

    def click_align_arrow(self, retry=3):
        self.driver.click("align_arrow",  retry=retry, delay=1)

    def click_clean_arrow(self, retry=3):
        self.driver.click("clean_arrow",  retry=retry, delay=1)

    def click_print_alignment_page_btn(self):
        self.driver.click("print_alignment_page_btn")

    def click_align_skip_btn(self):
        self.driver.click("align_skip_btn")

    def click_quality_cancel_btn(self):
        self.driver.click("quality_cancel_btn", timeout=10)

    def click_view_all_arrow(self):
        self.driver.click("view_all_arrow")

    def select_exit_setup_arrow(self):
        self.driver.click("exit_setup_arrow")

    def click_align_scan_page_btn(self):
        self.driver.click("align_scan_page_btn")

    def click_clean_again_btn(self):
        self.driver.click("clean_again_btn")

    def click_cleaning_done_btn(self):
        self.driver.click("cleaning_done_btn")

    def click_done_btn_on_alignment_dialog(self):
        self.driver.click("align_printheads_finished_done_btn")
    
    # ****************Printer Information********************
    def swipe_to_end(self, timeout=30):
        """
        Click ip address to swipe down on Printer info page"""
        element=self.driver.wait_for_object("ip_address_title", timeout=timeout)
        element.click()
        element.send_keys(Keys.END, Keys.END)
        
    def select_printer_information(self):
        self.driver.click("printer_information_opt")

    def get_printer_infor_status(self, timeout=10):
        return self.driver.get_attribute("printer_info_status_value", attribute="Name", timeout=timeout)

    def click_status_circle_btn(self, timeout=10):
        self.driver.click("status_circle_btn", timeout=timeout)

    def click_country_dropdown(self):
        self.driver.click("country_region_box")

    def select_USA_country(self):
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="down", distance=8)
        self.driver.click("USA")

    def select_English_language(self):
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="up", distance=8)
        self.driver.click("English")

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
        self.driver.send_keys("pin_num_box", pin_num)
  
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

    def click_back_btn_on_dialog(self):
        """
        Unable to align dialog/semi-align printer.
        """
        self.driver.click("back_btn_on_dialog")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_top_back_text(self):
        assert self.driver.get_attribute("top_back_text", attribute="Name") == "Back"

    def verify_progress_bar(self, timeout=30):
        time.sleep(5)
        self.driver.wait_for_object("progressbar", timeout=timeout, invisible=True)

    def verify_status_tile(self, is_remote=False):
        self.driver.wait_for_object("status_group")
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

    def verify_advanced_settings_under_setting_section(self):
        """
        Verify Advanced Settings below Settings section.
        """
        act_advanced = self.driver.get_attribute("advanced_settings", attribute="Name")
        print(f"act_advanced: {act_advanced}")
        assert act_advanced.lower() == "advanced settings"
        # assert self.driver.get_attribute("advanced_settings", attribute="Name").lower() == "Advanced Settings"

    def verify_reports_under_tools_section(self):
        """
        Verify Advanced Settings below Settings section.
        """
        act_printer = self.driver.get_attribute("printer_reports", attribute="Name")
        act_quality = self.driver.get_attribute("printer_quality_reports", attribute="Name")
        print(f"act_printer: {act_printer}")
        print(f"act_quality: {act_quality}")
        assert act_printer.lower() == "printer reports"
        assert act_quality.lower() == "print quality tools"
        # assert self.driver.get_attribute("printer_reports", attribute="Name").lower() == "printer reports"
        # assert self.driver.get_attribute("printer_quality_reports", attribute="Name").lower() == "print quality reports"

    def verify_status_under_status_section(self):
        """
        Verify Printer Status and Supply status under Status section.
        """
        act_printer_status = self.driver.get_attribute("printer_status", attribute="Name")
        assert act_printer_status.lower() == "printer status"
        act_supply_status = self.driver.get_attribute("supply_status", attribute="Name", raise_e=False)
        if not act_supply_status:
            return None  # No supply status option present in STG build.
        else:
            assert act_supply_status.lower() == "supply status"

    def verify_tools_tile(self):
        self.driver.wait_for_object("tools_group")
        self.driver.wait_for_object("printer_reports_opt")
        self.driver.wait_for_object("print_quality_tools_opt")
        # self.driver.wait_for_object("see_what_printing_opt", format_specifier=['See What\'s Printing'])

    def verify_manage_tile(self):
        self.driver.wait_for_object("manage_group")
        self.driver.wait_for_object("print_from_other_devices_opt")
        self.driver.wait_for_object("hide_printer_opt", displayed=False)

    def verify_print_anywhere_option_is_hidden(self):
        assert self.driver.wait_for_object("print_anywhere_opt", raise_e=False) is False

    def verify_advanced_settings_item(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("advanced_settings_opt", timeout=timeout, raise_e=raise_e)

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
    
    def verify_printer_reports_is_disable(self, invisible=False):
        self.driver.click("printer_reports_opt")
        self.driver.wait_for_object("name_title", invisible=invisible)

    def verify_printer_quality_tools_is_disable(self, invisible=False):
        self.driver.click("print_quality_tools_opt")
        self.driver.wait_for_object("name_title", invisible=invisible)

    def verify_network_information_is_disable(self, invisible=False):
        self.driver.click("network_information_opt")
        self.driver.wait_for_object("name_title", invisible=invisible)

    # ****************Network Information********************
    def verify_network_information_opt(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("network_information_opt", timeout=timeout, raise_e=raise_e)

    def verify_advanced_settings_is_disable(self):
        self.driver.click("advanced_settings_opt")
        self.driver.wait_for_object("name_title")

    def verify_all_the_opt_not_available_in_tools_tile(self):
        assert self.driver.get_attribute("printer_reports_opt", attribute="SelectionItem.IsSelected").lower() == "false"
        assert self.driver.get_attribute("print_quality_tools_opt", attribute="SelectionItem.IsSelected").lower() == "false"
        # assert self.driver.get_attribute("see_what_printing_opt", format_specifier=['See What\'s Printing'], attribute="SelectionItem.IsSelected").lower() == "false"
    
    def verify_shortcuts_item(self, invisible=True):
        self.driver.wait_for_object("shortcuts_item_opt", invisible=invisible)

    def verify_security_status_opt(self):
        self.driver.wait_for_object("security_status_opt")

    def verify_security_status_opt_is_hidden(self):
        assert self.driver.wait_for_object("security_status_opt", raise_e=False) is False

    # ****************Print Reports********************
    def verify_print_status_unknown_dialog(self, timeout=3, raise_e=True):
        return self.driver.wait_for_object("printer_status_unknown_text", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", timeout=timeout, raise_e=raise_e)

    def verify_report_printing_dialog(self, opt, timeout=25, raise_e=True):
        if opt == 'STATUS':
            text = "Printing Printer Status Report"
        elif opt == 'DIAGNOSTIC':
            text = "Printing Print Diagnostic Report"
        elif opt == 'NETWORK':
            text = "Printing Network Configuration Report"
        elif opt == 'WIRELESS':
            text = "Printing Wireless Network Test Report"
        elif opt == 'QUALITY':
            text = "Printing Print Quality Report"
        elif opt == 'WEB':
            text = "Printing Web Access Test Report"
        elif opt == 'DEMO':
            text = "Printing Demo Page"
        return self.driver.wait_for_object("dialog_cancel_btn", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("dynamic_text", format_specifier=[text], timeout=2, raise_e=raise_e)

    def verify_report_printing_dialog_dismiss(self, timeout=60, raise_e=True):
        return self.driver.wait_for_object("dialog_cancel_btn", invisible=True, timeout=timeout, raise_e=raise_e)
    
    def verify_printing_is_completed_dialog(self, opt, timeout=60, raise_e=True):
        if opt == 'STATUS':
            text = "Printer Status Report"
        elif opt == 'DIAGNOSTIC':
            text = "Print Diagnostic Report"
        elif opt == 'NETWORK':
            text = "Network Configuration Report"
        elif opt == 'WIRELESS':
            text = "Wireless Network Test Report"
        elif opt == 'QUALITY':
            text = "Print Quality Report"
        elif opt == 'WEB':
            text = "Web Access Test Report"
        elif opt == 'DEMO':
            text = "Demo Page"
        return self.driver.wait_for_object("report_ok_btn", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("printing_is_title", raise_e=raise_e, timeout=2) and\
        self.driver.wait_for_object("dynamic_text", format_specifier=[text], timeout=2, raise_e=raise_e) 
        
    def get_report_item_num(self):
        for i in range(1, 8):
            if i == 5:
                self.driver.swipe(distance=8)
            if self.driver.wait_for_object("dynamic_report_list_item", format_specifier=[i], timeout=2, raise_e=False) is False:
                return i-1
            
    def verify_printer_reports_page(self):
        item_list = []
        self.driver.wait_for_object("report_title", timeout=20)

        if self.driver.wait_for_object("print_status_report_option", timeout=2, raise_e=False):
            self.driver.wait_for_object("sub_print_status_report_option", timeout=2)
            item_list.append('STATUS')
        if self.driver.wait_for_object("print_diagnostic_info_option", timeout=2, raise_e=False):
            self.driver.wait_for_object("sub_print_diagnostic_info_option", timeout=2)
            item_list.append('DIAGNOSTIC')
        if self.driver.wait_for_object("network_configuration_report_option", timeout=2, raise_e=False):
           self.driver.wait_for_object("sub_network_configuration_report_option")
           item_list.append('NETWORK')
        if self.driver.wait_for_object("wireless_network_test_report_option", timeout=2, raise_e=False):
           self.driver.wait_for_object("sub_wireless_network_test_report_option", timeout=2)
           item_list.append('WIRELESS')
        if self.driver.wait_for_object("demo_page_option", timeout=2, raise_e=False):
           self.driver.wait_for_object("sub_demo_page_option", timeout=2)
           item_list.append('DEMO')
        if self.driver.wait_for_object("print_quality_report_option", timeout=2, raise_e=False):
            self.driver.wait_for_object("sub_print_quality_report_option", timeout=2)
            item_list.append('QUALITY')
        self.driver.swipe(distance=16)
        if self.driver.wait_for_object("web_access_test_report_option", timeout=2, raise_e=False):
            self.driver.wait_for_object("sub_web_access_test_report_option", timeout=2)
            item_list.append('WEB')
        self.driver.wait_for_object("report_print_btn", timeout=2)
        logging.info("report item: {}".format(item_list))
        return item_list
        
    def verify_this_feature_is_not_available_screen(self, raise_e=False):
        return self.driver.wait_for_object("this_feature_is_not_available_text", raise_e=raise_e)

    def get_printer_reports_items(self, item):
        return self.driver.wait_for_object(item, timeout=2, raise_e=False)

    def verify_printer_reports_available(self, raise_e=False):
        return self.driver.wait_for_object("report_print_name", raise_e=raise_e, timeout=10)
          
    def verify_door_open_dialog(self, raise_e=True):
        return self.driver.wait_for_object("door_open_title", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", raise_e=raise_e)
    
    def verify_door_open_dismiss(self):
        self.driver.wait_for_object("door_open_title", raise_e=False, invisible=True)

    def verify_unable_to_connect_dialog(self, raise_e=True):
        return self.driver.wait_for_object("unable_to_connect_title", raise_e=raise_e) and\
        self.driver.wait_for_object("check_printer_connection_text", raise_e=raise_e) and\
        self.driver.wait_for_object("retry_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e)

    # ****************Print Quality Tools********************
    def verify_print_quality_tools_page(self, check_detail=False):
        self.driver.wait_for_object("print_quality_tools_title")
        if check_detail:
            self.verify_align_printheads_part()
            self.verify_clean_printheads_part()
            self.verify_view_all_part()

    def verify_align_printheads_part(self, raise_e=True):
        return self.driver.wait_for_object("align_printheads_title_text", raise_e=raise_e) and\
        self.driver.wait_for_object("align_printheads_sub_text", raise_e=raise_e) and\
        self.driver.wait_for_object("align_arrow", raise_e=raise_e)

    def verify_clean_printheads_part(self, raise_e=True):
        return self.driver.wait_for_object("clean_printheads_title_text", raise_e=raise_e) and\
        self.driver.wait_for_object("clean_printheads_sub_text", raise_e=raise_e) and\
        self.driver.wait_for_object("clean_arrow", raise_e=raise_e)

    def verify_view_all_part(self, raise_e=True):
        return self.driver.wait_for_object("view_all_title_text", raise_e=raise_e) and\
        self.driver.wait_for_object("view_all_arrow", raise_e=raise_e)

    def verify_align_printheads_dialog(self, raise_e=True):
        return self.driver.wait_for_object("align_printheads_title", raise_e=raise_e) and\
        self.driver.wait_for_object("print_alignment_page_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("align_skip_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", raise_e=raise_e)
    
    def verify_alignment_dialog(self, raise_e=True):
        """
        Align printheads with an auto alignment printer.
        """
        return self.driver.wait_for_object("alignment_title", raise_e=raise_e) and\
        self.driver.wait_for_object("alignment_text", raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", raise_e=raise_e)

    def verify_align_printheads_finished_dialog(self, timeout=50, raise_e=False):
        """
        Align printheads with an auto alignment printer.
        """
        return self.driver.wait_for_object("align_printheads_finished_text", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("align_printheads_finished_done_btn", timeout=timeout, raise_e=raise_e)

    def verify_align_printheads_printing_dialog(self, timeout=50, raise_e=True):
        return self.driver.wait_for_object("align_printheads_title", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("progress_bar", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", timeout=timeout, raise_e=raise_e)

    def verify_align_printheads_scanning_dialog(self, timeout=50, raise_e=True):
        return self.driver.wait_for_object("align_printheads_title", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("progress_bar", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", timeout=timeout, raise_e=raise_e)

    def verify_align_printheads_place_dialog(self, raise_e=True):
        return self.driver.wait_for_object("align_printheads_title", raise_e=raise_e) and\
        self.driver.wait_for_object("align_scan_page_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", raise_e=raise_e)

    def verify_cleaning_dialog(self, raise_e=True):
        return self.driver.wait_for_object("cleaning_title", raise_e=raise_e) and\
        self.driver.wait_for_object("progress_bar", raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", raise_e=raise_e)

    def verify_cleaning_dialog_dismiss(self, timeout=40):
        self.driver.wait_for_object("cleaning_title", timeout=timeout, invisible=True)

    def verify_printing_dialog_dismiss(self, timeout=30):
        self.driver.wait_for_object("printing_title", timeout=timeout, invisible=True)

    def verify_cleaning_complete_dialog_dismiss(self, raise_e=False, invisible=True):
        self.driver.wait_for_object("cleaning_complete_title", raise_e=raise_e, invisible=invisible)

    def verify_printing_dialog(self, timeout=30, interval=0.5, raise_e=True):
        return self.driver.wait_for_object("printing_title", timeout=timeout, interval=interval, raise_e=raise_e) and\
        self.driver.wait_for_object("progress_bar", timeout=timeout, interval=interval, raise_e=raise_e) and\
        self.driver.wait_for_object("quality_cancel_btn", timeout=timeout, interval=interval, raise_e=raise_e)

    def verify_cleaning_complete_dialog(self, raise_e=True):
        return self.driver.wait_for_object("cleaning_complete_title", raise_e=raise_e) and\
        self.driver.wait_for_object("additional_cleaning_text", raise_e=raise_e) and\
        self.driver.wait_for_object("cleaning_done_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("clean_again_btn", raise_e=raise_e)

    def verify_unable_to_align_dialog(self, appear_time=30, raise_e=False):
        return self.driver.wait_for_object("unable_to_align_title", timeout=appear_time, raise_e=raise_e) and\
        self.driver.wait_for_object("unable_to_align_text", timeout=appear_time, raise_e=raise_e) and\
        self.driver.wait_for_object("back_btn_on_dialog", timeout=appear_time, raise_e=raise_e)

    # ***************Supply Status********************
    def verify_supply_status_page(self, timeout=20, raise_e=False):
        if self.driver.wait_for_object("i_accept_btn", timeout=timeout, raise_e=False):
            self.driver.click("i_accept_btn", change_check={"wait_obj": "i_accept_btn", "invisible": True}, timeout=timeout, raise_e=raise_e)
        return self.driver.wait_for_object("get_supplies_for_text", timeout=2, raise_e=raise_e) or \
        self.driver.wait_for_object("supply_printer_image", timeout=2, raise_e=raise_e)

    def verify_lets_finish_setting_up_page(self, timeout=20, raise_e=False):
        if self.driver.wait_for_object("i_accept_btn", timeout=2, raise_e=False):
            self.driver.click("i_accept_btn", change_check={"wait_obj": "i_accept_btn", "invisible": True}, timeout=timeout, raise_e=raise_e)
        return self.driver.wait_for_object("supply_status_sign_in_btn", timeout=2, raise_e=raise_e)

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
    
    def verify_model_name_title(self, raise_e=False):
        if self.driver.wait_for_object("model_name_title", timeout=25, raise_e=raise_e):
            return True
        else:
            return False
    
    # ****************Network Information******************** 
    def verify_network_info_simple_page(self):
        self.driver.wait_for_object("network_info_title") 

    def verify_ip_text(self, timeout=30):
        """
        Verify IP address text is displayed on Network Information page.
        """
        self.driver.wait_for_object("ip_address_title", timeout=timeout) 

    def verify_network_info_page(self, ip):
        """
        The simulated printer information just has SN/IP address/Model name info.
        """
        self.driver.wait_for_object("network_info_title")
        self.driver.wait_for_object("wireless_text")
        self.driver.get_attribute("wireless_detail_text", attribute="Name")
        self.driver.wait_for_object("wireless_status_text") 
        self.driver.get_attribute("wireless_status_detail_text", attribute="Name")
        # self.driver.wait_for_object("bonjour_name_text")
        # bon_detail_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Bonjour Name'], attribute="Name")
        # assert bon_detail_text == bon_name
        self.driver.wait_for_object("ip_address_text")
        ip_detail_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['IP Address'], attribute="Name") 
        assert ip_detail_text == ip 
        self.driver.wait_for_object("mac_address_text")
        element = self.driver.wait_for_object("host_name_text")
        element.click()
        element.send_keys(Keys.END, Keys.END)
        # host_detail_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Host Name'], attribute="Name")
        # assert host_detail_text == host_name             
        if self.driver.wait_for_object("bluetooth_low_energy_title", raise_e=False):
            assert self.driver.get_attribute("bluetooth_status_text_1", attribute="Name") == "Status"
            bluetooth_text = self.driver.get_attribute("bluetooth_status_text_2", attribute="Name")
            if not bluetooth_text in ["On", "Off"]:
                raise NoSuchElementException("Bluetooth Low Energy Status shows incorrect")       
        assert self.driver.wait_for_object("wifi_direct_text", raise_e=False) is False
        

        # if is_dune:
        #     wireless_detail_text == "Off"
        #     wireless_status_detail_text == "Not connected"
        #     self.driver.wait_for_object("ethernet_title")
        #     assert self.driver.get_attribute("ethernet_status_text_1", attribute="Name") == "Status"
        #     assert self.driver.get_attribute("ethernet_status_text_2", attribute="Name") == "Connected"   
        # else:
        #     wireless_detail_text == "On"
        #     wireless_status_detail_text == "Connected"
        #     self.driver.wait_for_object("network_name_text")
        #     # ssid_text = self.driver.get_attribute("get_dynamic_text", format_specifier=['Network Name (SSID)'], attribute="Name")
        #     # assert ssid_text == ssid  
      
        if self.driver.wait_for_object("ethernet_title", raise_e=False):
                assert self.driver.get_attribute("ethernet_status_text_1", attribute="Name") == "Status"
                ethernet_text = self.driver.get_attribute("ethernet_status_text_2", attribute="Name")
                if not ethernet_text in ["Supported", "Not supported", "Not connected", "Connected"]:
                    raise NoSuchElementException("Ethernet Status shows incorrect")
                
    def verify_network_info_page_not_show(self, raise_e=True):
        return self.driver.wait_for_object("network_info_title", raise_e=raise_e)
    
   # ****************Printer Information********************
    def verify_submit_btn_status(self, enable=True):
        """
        Verify submit button on PIN/Password dialog is enable after input value.
        """
        button = self.driver.wait_for_object("sign_in_submit_btn")
        if enable:
            assert button.get_attribute("IsEnabled").lower() == "true"
        else:
            assert button.get_attribute("IsEnabled").lower() == "false"

    def verify_country_result(self):
        """
        verify the result before and after changeing the options.
        """
        return self.driver.get_attribute("country_result", attribute='Name')

    def verify_language_result(self):
        """
        verify the result before and after changeing the options.
        """
        return self.driver.get_attribute("language_result", attribute='Name')
    
    def verify_printer_information_opt(self, timeout=30, raise_e=True):
        self.driver.wait_for_object("printer_information_opt", timeout=timeout, raise_e=raise_e)

    def verify_option_under_information_section(self):
        """
        Verify Printer Information and Network Information options under Information section.
        """
        act_printer = self.driver.get_attribute("printer_information", attribute="Name")
        act_network = self.driver.get_attribute("network_information", attribute="Name")
        print(f"ACT printer info: {act_printer}")
        print(f"ACT network info: {act_network}")
        assert act_printer.lower() == "printer information"
        assert act_network.lower() == "network information"
        # assert self.driver.get_attribute("printer_information", attribute="Name").lower() == "printer information"
        # assert self.driver.get_attribute("network_information", attribute="Name").lower() == "network information"

    def verify_printer_info_simple_page(self, timeout=25, raise_e=True):
        return self.driver.wait_for_object("left_list", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("printer_info_title", raise_e=raise_e)
    
    def verify_quick_reference_btn(self, raise_e=True):
        return self.driver.wait_for_object("quick_reference_btn", raise_e=raise_e)

    def verify_status_text(self, status, timeout=3, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[status], timeout=timeout, raise_e=raise_e)
    
    def verify_installation_status_text(self):
        return self.driver.get_attribute("get_dynamic_text", format_specifier=['Installation Status'], attribute="Name")

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

    def verify_printer_info_page_with_offline_printer(self, host_name, model_name):
        self.driver.wait_for_object("name_title")
        name_info = self.driver.get_attribute("get_dynamic_text", format_specifier=['Printer Name'], attribute="Name")
        if '(' in name_info:
            assert host_name in name_info
        self.driver.wait_for_object("status_title")
        assert self.driver.get_attribute("get_dynamic_text", format_specifier=['Status'], attribute="Name")  == 'Printer offline' 
        self.driver.wait_for_object("status_circle_btn", timeout=25)
        self.driver.wait_for_object("model_name_title", timeout=25)
        model_name = re.search(r"\d+", model_name).group()
        actual_model = self.driver.get_attribute("get_dynamic_text", format_specifier=['Model Name'], attribute="Name")
        assert model_name in actual_model
        installation = self.verify_installation_status_text()
        assert installation in ['Installed', 'Not installed']
        self.driver.wait_for_object("connection_type_title")
        self.driver.wait_for_object("network_text")
        self.driver.wait_for_object("connection_status_title")

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

    def verify_country_region_part(self):
        self.driver.wait_for_object("country_region_title")

    def verify_country_select_item(self, cou='United States', timeout=2, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[cou], timeout=timeout, raise_e=raise_e)

    def verify_language_part(self):
        self.driver.wait_for_object("language_title")

    def verify_language_select_item(self, lan='English', timeout=2, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[lan], timeout=timeout, raise_e=raise_e)

    def verify_set_country_or_language_dialog(self, timeout=2, raise_e=True):
        return self.driver.wait_for_object("cancel_btn", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("save_btn", timeout=timeout, raise_e=raise_e)

    def verify_unable_to_set_printer_dialog(self, timeout=90):
        self.driver.wait_for_object("unable_to_set_printer_dialog", timeout=timeout)

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

    def verify_ews_page(self, timeout=60, raise_e=True):
        if self.driver.wait_for_object("continuing_to_your_printer_title", timeout=timeout, raise_e=False):
            self.driver.click("the_pin_ok_btn")
        if self.driver.wait_for_object("privacy_error_screen", raise_e=False):
            self.driver.click("advanced_btn")
            self.driver.click("continue_to_ip_link")
        self.driver.wait_for_object("ews_home_title",timeout=timeout, raise_e=raise_e)

    def verify_general_title_not_show(self, timeout=30, invisible=True):
        self.driver.wait_for_object("general_title", timeout=timeout, invisible=invisible)

    def verify_tile_are_locked(self):
        self.driver.wait_for_object("locked_image")

    def verify_log_in_with_pin_dialog(self, invisible=False, raise_e=True):
        """
        This dialog box is about the need to enter a password/pin.
        Find the printer PIN dialog.
        """
        return self.driver.wait_for_object("submit_btn", invisible=invisible, raise_e=raise_e) and \
        self.driver.wait_for_object("sign_in_cancel_btn", invisible=invisible, raise_e=raise_e)
   
    def verify_incorrect_pin_text_display(self):
        self.driver.wait_for_object("incorrect_pin_text")

    def verify_sign_in_text_display(self):
        self.driver.wait_for_object("sign_in_text")

    def verify_sign_out_text_display(self, timeout=30):
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="up", distance=4)
        self.driver.wait_for_object("sign_out_text", timeout=timeout)

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

    def verify_ews_session_locked(self):
        """
        input several times with incorrect pin/password, the session will be locked and can't input pin in a moment.
        """
        self.driver.wait_for_object("session_locked")

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
    
    def get_feature_screen_text(self):
        return self.driver.get_attribute("this_feature_is_not_available_text", attribute="Name")

