import logging
from time import sleep
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
from SAF.decorator.saf_decorator import screenshot_compare
from selenium.webdriver.common.action_chains import ActionChains
from SAF.decorator.saf_decorator import string_validation


class OptionNotFound(SMBFlow):
    pass

class StringComparisonException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class Home(SMBFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for SMB
    """
    flow_name = "home"
    hp_official_site_url = "https://www.hp.com/us-en/home.html"
    hp_official_support_url = "https://support.hp.com/us-en"
    hp_smart_admin_terms_of_use_url = "https://www.hpsmart.com/admin-tou"
    hp_privacy_central_url = "https://www.hp.com/us-en/privacy/privacy-central.html"
    personal_data_rights_notice_url  = "https://www.hp.com/us-en/personal-data-rights.html"

    def handle_smb_dashboard_overlay(self, timeout=15):
        """
        This intro overlay is only shown when user creates a account for the first time.
        """
        if self.driver.wait_for_object("tutorial_overlay_modal", timeout=timeout, raise_e=False):
            for i in range(1,3):
                self.driver.click("tutorial_overlay_modal_step_{}_next_btn".format(i))
            self.driver.click("tutorial_overlay_modal_get_started_btn")
        if self.driver.wait_for_object("new_printer_added_modal", raise_e=False):
            self.driver.click("new_printer_added_modal_dashboard_home_btn")

    def verify_tutorial_overlay_modal(self, raise_e=True):
        return self.driver.wait_for_object("tutorial_overlay_modal", raise_e=raise_e, timeout=10)

    def verify_new_printer_added_modal(self, raise_e=True):
        return self.driver.wait_for_object("new_printer_added_modal", raise_e=raise_e, timeout=10)
    
    def verify_printer_email_alerts_overlay(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("printer_email_alerts_overlay", timeout=timeout, raise_e=raise_e)
    
    def handle_printer_email_alerts_overlay(self, timeout=15):
        if self.driver.wait_for_object("printer_email_alerts_overlay", timeout=timeout, raise_e=False):
            self.driver.click("printer_email_alerts_overlay_not_now_btn")
    
    ############################ Main Menu verifys ############################
    def verify_smb_home_title_bar(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("shell_title_bar", timeout=timeout, raise_e=raise_e)

    def get_smb_home_title(self):
        return self.driver.wait_for_object("shell_title_bar").text

    def verify_user_icon(self, timeout=3, raise_e=True):
        return self.driver.wait_for_object("user_icon_top_right", timeout=timeout, raise_e=raise_e)

    def verify_logout_menu_item(self):
        return self.driver.wait_for_object("user_icon_menu_log_out_item")

    def verify_home_menu_btn(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("home_menu_btn", timeout=timeout, raise_e=raise_e)
        
    def verify_users_menu_btn(self):
        return self.driver.wait_for_object("users_menu_btn")

    def verify_printers_menu_btn(self): 
        return self.driver.wait_for_object("printers_menu_btn")

    def verify_solutions_menu_btn(self,timeout=30):
        return self.driver.wait_for_object("solutions_menu_btn", timeout=timeout)

    def verify_solutions_menu_btn_displayed(self,displayed=True):
        return self.driver.wait_for_object("solutions_menu_btn", invisible=not displayed)

    def verify_sustainability_menu_btn(self, timeout=20):
        return self.driver.wait_for_object("sustainability_menu_btn", timeout=timeout)
    
    def verify_sustainability_menu_btn_displayed(self,displayed=True):
        return self.driver.wait_for_object("sustainability_menu_btn", invisible=not displayed)

    def verify_account_menu_btn(self):
        return self.driver.wait_for_object("account_menu_btn")

    def verify_hpinstantink_menu_btn(self):
        return self.driver.wait_for_object("hpinstantink_menu_btn")

    def verify_help_center_menu(self):
        return self.driver.wait_for_object("help_center_menu")
    
    def get_home_menu_btn_text(self):
        self.driver.wait_for_object("home_menu_btn",timeout=30)
        return self.driver.get_text("home_menu_btn")

    def get_users_menu_btn_text(self):
        return self.driver.get_text("users_menu_btn")

    def get_printers_menu_btn_text(self): 
        return self.driver.get_text("printers_menu_btn")

    def get_solutions_menu_btn_text(self):
        self.driver.wait_for_object("solutions_menu_btn",timeout=30)
        return self.driver.get_text("solutions_menu_btn")
 
    def get_sustainability_menu_btn_text(self):
        return self.driver.get_text("sustainability_menu_btn")

    def get_account_menu_btn_text(self):
        return self.driver.get_text("account_menu_btn")

    def get_hpinstantink_menu_btn_text(self):
        return self.driver.get_text("hpinstantink_menu_btn")

    def get_help_center_menu_text(self):
        return self.driver.get_text("help_center_menu")
    
    ############################ Sub Menu Actions ############################

    def check_organization_name_profile_container(self, company_name):
        """
        Check of the given organization name is showing in the top right corner drop menu section in smb dashboard.
        """
        if company_name not in self.driver.wait_for_object("profile_menu_conatiner").text:
            raise AssertionError("organization name not in smb dashboard profile section")

    def click_organization_selector(self):
        """
        Change organization. This click method just clicks on second organization name in user icon profile drop menu conatiner.
        """
        return self.driver.click("organization_selector")

    ############################ Main Menu Clicks ############################
    
    def click_home_menu_btn(self):
        return self.driver.click("home_menu_btn",timeout=20)

    def click_users_menu_btn(self):
        return self.driver.click("users_menu_btn", timeout=30)

    def click_solutions_menu_btn(self):
        return self.driver.click("solutions_menu_btn", timeout=30)

    def click_printers_menu_btn(self):
        return self.driver.click("printers_menu_btn", timeout=30)

    def click_account_menu_btn(self):
        return self.driver.click("account_menu_btn",timeout=20)

    def click_hpinstantink_menu_btn(self):
        return self.driver.click("hpinstantink_menu_btn",timeout=20)
    
    def click_sustainability_menu_btn(self, timeout=20):
        return self.driver.click("sustainability_menu_btn", timeout=timeout)
    
    def click_help_center_menu_btn(self):
        return self.driver.click("help_center_menu",timeout=30)

 ############################ Home Page Status widget Clicks ############################

    def click_status_total_printer_btn(self):
        return self.driver.click("status_mfe_total_printer_btn",timeout=20)

    def click_status_total_users_btn(self):
        return self.driver.click("status_mfe_total_users_btn",timeout=20)

    def verify_status_total_users_btn(self):
        return self.driver.wait_for_object("status_mfe_total_users_btn",timeout=20)   

    def click_user_icon_top_right(self):
        return self.driver.js_click("user_icon_top_right")

    def click_user_icon_menu_account_profile_item(self):
        return self.driver.click("user_icon_menu_account_profile_item")

 ############################ Sub Menu verifys ############################

    def verify_notification_settings_sub_menu_btn(self):
        return self.driver.wait_for_object("notification_settings_sub_menu_btn")

    def verify_privacy_settings_sub_menu_btn(self):
        return self.driver.wait_for_object("privacy_settings_sub_menu_btn")
   
    def verify_user_icon_top_right_profile(self):
        return self.driver.wait_for_object("user_icon_top_right",timeout=20)

 ############################ Sub Menu Clicks ############################
   
    def click_account_profile_sub_menu_btn(self):
        return self.driver.click("account_profile_sub_menu_btn")

    def click_notification_settings_sub_menu_btn(self):
        return self.driver.click("notification_bell_btn")

 ############################ Home Page Notification Verify ############################

    def verify_notification_bell_icon(self):
        return self.driver.wait_for_object("notification_bell_btn", timeout=10)  

    def verify_notification_mfe_title(self):
        return self.driver.wait_for_object("noti_mfe_card_tite")    
 ############################ Status Widget - Home Page  ############################       

    @string_validation("status_header_title")
    def verify_status_widget_title(self):
        #Verify status widget card/section title
        return self.driver.wait_for_object("status_header_title", timeout=20)
        
    def verify_status_total_printer_btn(self):
        return self.driver.wait_for_object("status_mfe_total_printer_btn", timeout=20)

    @string_validation("status_header_devices_totalPrinters")
    def verify_status_widget_printer_status_header(self):
        return self.driver.wait_for_object("status_header_devices_totalPrinters")
    
    @string_validation("status_header_devices_connected")
    def verify_status_widget_connected_printer(self, timeout=10):
        return self.driver.wait_for_object("status_header_devices_connected", timeout=timeout)
       
    @string_validation("status_header_devices_notConnected")   
    def verify_status_widget_not_connected_printer(self):
        return self.driver.wait_for_object("status_header_devices_notConnected")

    @string_validation("status_header_users_total")
    def verify_status_widget_users_status_header(self):
        return self.driver.wait_for_object("status_header_users_total")

    @string_validation("status_header_users_active")
    def verify_status_widget_active_users(self):
        return self.driver.wait_for_object("status_header_users_active")
        
    @string_validation("status_header_users_pending")
    def verify_status_widget_pending_users(self):
        return self.driver.wait_for_object("status_header_users_pending")
        
    @string_validation("status_header_users_expired")
    def verify_status_widget_expired_users(self):
        return self.driver.wait_for_object("status_header_users_expired")
        
    def get_status_widget_total_printer_count(self): 
        return int(self.driver.wait_for_object("status_widget_total_count").text)
        
    def get_status_widget_connected_printer_count(self):
        return int(self.driver.wait_for_object("status_printer_connected_count").text)

    def get_status_widget_not_connected_printer_count(self):
        return int(self.driver.wait_for_object("status_printer_notconnected_count").text)

    def get_status_widget_total_user_count(self): 
        return int(self.driver.wait_for_object("status_widget_total_user_count").text)
        
    def get_status_widget_active_user_count(self):
        return int(self.driver.wait_for_object("status_users_active_count").text)

    def get_status_widget_pending_user_count(self):
        return int(self.driver.wait_for_object("status_users_pending_count").text)

    def get_status_widget_expired_user_count(self):
        return int(self.driver.wait_for_object("status_users_expired_count").text)
    
     ############################ Top Right  Corner Menu ############################

    def get_emailid_user_icon(self):
        return self.driver.get_text("user_icon_top_right_email")
        
    def get_user_icon_initial(self):
        return self.driver.wait_for_object("user_icon_top_right_txt").text
    
    def click_user_icon_top_right_txt(self):
        """ 
        Performing this click will open Users account drop down menu
        """
        self.driver.click("user_icon_top_right_txt")   

    def verify_profile_menu_conatiner(self):
        self.driver.wait_for_object("profile_menu_conatiner")
    
    def verify_emailid_user_icon(self):
        return self.driver.wait_for_object("user_icon_top_right_email", timeout=10)
     
    ############################ Flows ############################

    def logout(self):
        #This needs to be run twice for some reason 
        for _ in range(2):
            if self.verify_user_icon(raise_e=False) is not False:
                self.click_user_icon_top_right()
                self.verify_logout_menu_item()
                self.driver.click("user_icon_menu_log_out_item")
        return True
############################ Home Page Printer widget ############################

    def verify_printer_widget_section(self):
      return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_widget_section", timeout=20))

    def verify_printer_widget_title(self):
        return self.driver.wait_for_object("printer_widget_printer_title")

    def verify_printer_location(self):
        if self.driver.find_object("printer_widget_printer_location",raise_e=True):
            logging.info("Printer location field not available for Printer")
        else:
            return self.driver.wait_for_object("printer_widget_printer_location") 

    def verify_printer_status(self):
        return self.driver.wait_for_object("printer_widget_printer_status")

    def get_printer_name(self, timeout=10):
        return self.driver.wait_for_object("printer_widget_printer_name", timeout=timeout).text
    
    def get_printer_location(self):
        if self.driver.find_object("printer_widget_printer_location",raise_e=True):
            logging.info("Printer location field not available for Printer")
        else:
            return self.driver.wait_for_object("printer_widget_printer_location").text

    def get_printer_status(self):
        return self.driver.get_text("printer_widget_printer_status")

    def click_printer_widget_view_all_link(self):
        return self.driver.click("printer_widget_view_all_link_button", timeout=20)

    def get_printer_widget_printer_total_count(self):
        total_count = self.driver.wait_for_object("printer_widget_printer_total_count").text
        return int(total_count.replace("(","").replace(")",""))

    def get_printer_widget_no_of_printers_count(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_widget_printer_total_count", timeout=20))
        return len(self.driver.find_object("printer_widget_printer_total_count",multiple=True)) 

    def verify_printer_widget_printer_is_displayed(self):
        return self.driver.wait_for_object("printer_widget_printer_list",raise_e=False)

    def get_printer_widget_empty_text(self):
        return self.driver.wait_for_object("printer_widget_no_printers").text

    def get_printer_widget_list_of_printers(self):
        return len(self.driver.find_object("printer_widget_printers_list",multiple=True))
       
 ############################ Home Page Usage widget ############################
        
    def verify_printer_usage_widget_fixed_days(self):
        return self.driver.verify_object_string("printer_usage_widget_telementry_days_label")
        
    def get_printer_usage_widget_color_label(self):
        actual_value = self.driver.wait_for_object("printer_usage_widget_printed_color_label").text
        printer_color_label=(actual_value.split(" ")[0]).replace(" ","")
        return printer_color_label

    def verify_printer_usage_widget_toggle_color_button_default(self):
        toggle_button = self.driver.wait_for_object("printer_usage_widget_toogle_color_button")
        if toggle_button.is_enabled():
            return True
        else:
            raise UnexpectedItemPresentException("printer usage widget color toggle button is not selected by default")

    def get_printer_usage_widget_black_white_label(self):
        actual_value = self.driver.wait_for_object("printer_usage_widget_printed_black_white_label").text
        printer_black_white_label=(actual_value.split("(")[0]).strip()
        return printer_black_white_label
        
    def verify_printer_usage_widget_toggle_color_button_default(self):
        toggle_button = self.driver.wait_for_object("printer_usage_widget_toogle_color_button")
        if toggle_button.is_enabled():
            return True
        else:
            raise UnexpectedItemPresentException("printer usage widget color toggle button is not selected by default")

    def click_printer_usage_sides_toggle_button(self):
        return self.driver.click("printer_usage_widget_toogle_sides_button",timeout=20)

    def verify_printer_usage_widget_single_sided_label(self):
        actual_value = self.driver.wait_for_object("printer_usage_widget_single_sided_label").text
        printer_single_sided_label=(actual_value.split("(")[0]).strip()
        return printer_single_sided_label
        
    def verify_printer_usage_widget_double_sided_label(self):
        actual_value = self.driver.wait_for_object("printer_usage_widget_double_sided_label").text
        printer_single_double_label=(actual_value.split("(")[0]).strip()
        return printer_single_double_label
       
    def get_printer_usage_widget_dropdown_print(self):
        dropdown_option_print = (self.driver.wait_for_object("printer_usage_widget_dropdown_print").text).strip()
        return dropdown_option_print

    def verify_printer_usage_widget_dropdown_print(self):
        return self.driver.verify_object_string("printer_usage_widget_dropdown_print_label")

    @string_validation("dashboard_cardAnalytics_disclaimerText")
    def verify_printer_usage_description(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_disclaimerText")

    def get_printer_usage_widget_printed_pages(self):
        printed_pages = (self.driver.wait_for_object("printer_usage_widget_printed_pages_label").text).strip()
        return printed_pages

    def verify_printer_usage_widget_printed_pages_text(self):
        return self.driver.verify_object_string("printer_usage_widget_printed_pages_text")

    def click_printer_usage_print_sides_button(self):
        return self.driver.click("printer_usage_print_sides_button")

    def click_printer_device_status_icon(self):
        self.driver.click("printer_device_status_icon")
    
    def verify_printer_usage_widget_total_print_count(self):
        return self.driver.wait_for_object("printer_usage_widget_total_printed_pages_count")

    def get_printer_usage_widget_single_sided_label(self):
        actual_value = self.driver.wait_for_object("printer_usage_widget_single_sided_label").text
        if "Single-sided" in actual_value:
            return True
        else:
            raise UnexpectedItemPresentException("text mismatches actual value:"+ actual_value)
		
    def get_printer_usage_widget_double_sided_label(self):
        actual_value = self.driver.wait_for_object("printer_usage_widget_double_sided_label").text
        if "Double-sided" in actual_value:
            return True
        else:
            raise UnexpectedItemPresentException("text mismatches actual value:"+ actual_value)

    def verify_printer_usage_widget_total_printed_pages_count(self):
        return self.driver.wait_for_object("printer_usage_widget_sides_total_print_count")

    def click_printer_usage_select_dropdown(self):
        return self.driver.click("printer_usage_option_dropdown", timeout=30)

    def verify_printer_usage_fax_pages_received_text(self):
        return self.driver.verify_object_string("printer_usage_fax_pages_received_text")
    
    def verify_printer_usage_fax_pages_sent_text(self):
        return self.driver.verify_object_string("printer_usage_fax_pages_sent_text")

    def verify_printer_usage_fax_pages_archived_only_text(self):
        actual_value = self.driver.wait_for_object("printer_usage_fax_pages_archived_only_text").text
        printer_usage_fax_pages_archived_label=(actual_value.split("(")[0]).strip()
        return printer_usage_fax_pages_archived_label

    def verify_printer_usage_fax_pages_text(self):
        return self.driver.verify_object_string("printer_usage_fax_pages_text")

    def verify_printer_usage_pages_scanned_text(self):
        return self.driver.verify_object_string("printer_usage_pages_scanned_text")

    def verify_printer_usage_scanned_pages_text(self):
        return self.driver.verify_object_string("printer_usage_scanned_pages_text")
    
    def usage_select_dropdown_option(self,option):
        return self.driver.click("usage_select_dropdown_scan",format_specifier=[option])

    def verify_usage_select_dropdown(self):
        return self.driver.wait_for_object("printer_usage_option_dropdown")

    @string_validation("dashboard_cardAnalytics_headerNew2")
    def verify_printer_usage_widget_label(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_headerNew2",timeout=20)

    def verify_printer_usage_widget_help_icon(self):
        return self.driver.wait_for_object("printer_usage_widget_help_icon")

    def verify_printer_usage_widget_view_details_button(self):
        return self.driver.wait_for_object("printer_usage_widget_view_details_button")

    @string_validation("dashboard_cardAnalytics_subtitleText_printPageNew")
    def verify_printer_usage_widget_total_pages_printed_label(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_subtitleText_printPageNew",timeout=20)

    def verify_printer_usage_widget_total_pages_printed_count(self):
        return self.driver.wait_for_object("usage_widget_total_pages_printed_count",timeout=20)

    def verify_printer_usage_data_select_previous_year_button(self):
        return self.driver.wait_for_object("usage_data_select_previous_year_button",timeout=20)

    def verify_printer_usage_data_select_next_year_button(self):
        return self.driver.wait_for_object("usage_data_select_next_year_button",timeout=20)

    def verify_printer_usage_data_select_year_value(self):
        return self.driver.wait_for_object("usage_data_select_year_value",timeout=20)

    @string_validation("dashboard_cardAnalytics_select_print")
    def verify_usage_widget_toggle_print_button(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_select_print",timeout=20)

    @string_validation("dashboard_cardAnalytics_printedPages")
    def verify_printed_usage_data_highcharts_axis_printed_pages_title(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_printedPages",timeout=20)
  
    @string_validation("dashboard_cardAnalytics_color_blackWhite")
    def verify_printed_usage_data_highcharts_black_and_white_button(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_color_blackWhite",timeout=20)

    @string_validation("dashboard_cardAnalytics_color_color")
    def verify_printed_usage_data_highcharts_color_button(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_color_color",timeout=20)

    @string_validation("dashboard_cardAnalytics_average_usage")
    def verify_printed_usage_data_highcharts_average_use_button(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_average_usage",timeout=20)

    def get_printed_usage_data_highcharts_xaxis_labels_options(self):
        actual_options = []
        all_options = self.driver.find_object("printed_usage_data_highcharts_xaxis_labels_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def verify_usage_widget_toggle_scan_button_is_displayed(self):
        if self.driver.find_object("usage_widget_toggle_scan_button", raise_e=False) is not False:
            return True
        else:
            logging.info("Scan toggle button is not available.")
            return False

    def verify_usage_widget_toggle_scan_button(self):
        return self.driver.wait_for_object("usage_widget_toggle_scan_button",timeout=20)

    def click_usage_widget_toggle_scan_button(self):
        return self.driver.click("usage_widget_toggle_scan_button",timeout=20)

    @string_validation("dashboard_cardAnalytics_subtitleText_scanNew")
    def verify_printer_usage_widget_total_pages_scanned_label(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_subtitleText_scanNew",timeout=20)

    def verify_printer_usage_widget_total_pages_scanned_count(self):
        return self.driver.wait_for_object("usage_widget_total_pages_scanned_count",timeout=20)

    @string_validation("dashboard_cardAnalytics_scan_pagesScanned")
    def verify_scanned_usage_data_highcharts_axis_scanned_pages_title(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_scan_pagesScanned",timeout=20)
  
    @string_validation("dashboard_cardAnalytics_select_scans")
    def verify_scanned_usage_data_highcharts_scans_button(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_select_scans",timeout=20)

    @string_validation("dashboard_cardAnalytics_average_usage")
    def verify_scanned_usage_data_highcharts_average_use_button(self):
        return self.driver.wait_for_object("dashboard_cardAnalytics_average_usage",timeout=20)

    def get_scanned_usage_data_highcharts_xaxis_labels_options(self):
        actual_options = []
        all_options = self.driver.find_object("scanned_usage_data_highcharts_xaxis_labels_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def add_both_color_black_and_white(self):
        actual_count = self.driver.wait_for_object("printer_usage_widget_printed_color_label").text
        Printed_color_pages_count=int((actual_count.split("(")[1]).replace(")",""))
        actual_value = self.driver.wait_for_object("printer_usage_widget_printed_black_white_label").text
        printer_black_white_pages_count=int((actual_value.split("(")[1]).replace(")",""))
        return (Printed_color_pages_count + printer_black_white_pages_count)
    
    def get_total_pages_in_usage_print_color_toggle(self):
        return int(self.driver.wait_for_object("printer_usage_widget_total_printed_pages_count").text)

    def add_both_single_and_double_sided_pages(self):
        actual_count = self.driver.wait_for_object("printer_usage_widget_single_sided_label").text
        printer_single_sided_label=int(actual_count.split("(")[1].replace(")",""))
        actual_value = self.driver.wait_for_object("printer_usage_widget_double_sided_label").text
        printer_double_sided_label=int(actual_value.split("(")[1].replace(")",""))
        return (printer_single_sided_label + printer_double_sided_label)
    
    def get_total_pages_in_usage_print_sides_toggle(self):
        return int(self.driver.wait_for_object("printer_usage_widget_sides_total_print_count").text)

############################ HP Smart Pro Widget - Home Page  ############################   

    @string_validation("dashboard_hpPlus_hpSmartPro_header")
    def verify_hp_smart_pro_widget_title(self, timeout=20):
        #Verify HP smart pro widget card/section title
        return self.driver.wait_for_object("dashboard_hpPlus_hpSmartPro_header")

    def verify_smart_pro_widget(self):
        return self.driver.wait_for_object("dashboard_hpPlus_hpSmartPro_header",raise_e=False, timeout=40)

    def verify_hp_smart_pro_page_title(self):
        #Verify Users page/section title
        return self.driver.wait_for_object("hp_smart_pro_title", timeout=20)

    def get_status_solution_page(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("hp_smart_pro_status"))
        return self.driver.get_text("hp_smart_pro_status")

    def get_status_description_solution_page(self):
        return (self.driver.wait_for_object("hp_smart_pro_status_description").text).replace(".","")

    def get_smart_pro_widget_description(self):
        return (self.driver.wait_for_object("smart_pro_widget_desc").text).split(".")[0]

    @string_validation("dashboard_hpPlus_hpSmartPro_action")
    def verify_smart_pro_discover_link(self):
        return self.driver.wait_for_object("dashboard_hpPlus_hpSmartPro_action") 

    def click_smart_pro_discover_link(self):
        return self.driver.click("dashboard_hpPlus_hpSmartPro_action",timeout=30)        

############################ Home Page Smart Notification widget ############################    
   
    def verify_smart_notification_widget_title(self):
        return self.driver.wait_for_object("smart_notification_widget_title",timeout=30)

    def get_smart_notification_widget_title(self):
        title = self.driver.wait_for_object("smart_notification_widget_title").text
        return (title.split("(")[0]).strip() 
        
    def get_smart_notification_widget_notification_count(self):
        sleep(3)
        notification_count = self.driver.wait_for_object("smart_notification_widget_title_count", timeout=20).text
        return int((notification_count.split("(")[1]).replace(")",""))      

    def get_smart_notification_widget_list_of_notifications(self):
        return len(self.driver.find_object("smart_notification_widget_total_count",multiple=True))       

    @string_validation("notification_smartNotification_noDataAvailable")
    def verify_smart_notification_widget_empty_text(self):
        return self.driver.wait_for_object("notification_smartNotification_noDataAvailable",timeout=20)

#################### Home Page HP+ widget #########################

    def get_hp_plus_printer_widget_smart_security_printer_total_count(self):
        return int(self.driver.wait_for_object("hp_plus_printer_widget_smart_security_printer_total_count").text)

    def get_hp_plus_printer_widget_print_anywhere_printer_total_count(self):
        return int(self.driver.wait_for_object("hp_plus_printer_widget_print_anywhere_printer_total_count").text)
        
    @string_validation("dashboard_hpPlus_smartSecurity_status_secured")
    def verify_hp_plus_smart_security_secured_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_smartSecurity_status_secured",timeout=20)

    @string_validation("dashboard_hpPlus_smartSecurity_status_needsAttention")
    def verify_hp_plus_smart_security_needs_attention_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_smartSecurity_status_needsAttention")

    @string_validation("dashboard_hpPlus_smartSecurity_status_unmonitored")
    def verify_hp_plus_smart_security_unmonitored_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_smartSecurity_status_unmonitored")

    @string_validation("dashboard_hpPlus_smartSecurity_status_noDataAvailable")
    def verify_hp_plus_smart_security_needs_no_data_available_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_smartSecurity_status_noDataAvailable")

    @string_validation("dashboard_hpPlus_printAnywhere_status_enable")
    def verify_hp_plus_print_anywhere_enabled_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_printAnywhere_status_enable")

    @string_validation("dashboard_hpPlus_printAnywhere_status_disabled")
    def verify_hp_plus_print_anywhere_disabled_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_printAnywhere_status_disabled")

    @string_validation("dashboard_hpPlus_smartSecurity_header")
    def verify_smart_security_label(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("dashboard_hpPlus_smartSecurity_header", timeout=30))

    @string_validation("dashboard_hpPlus_printAnywhere_header")
    def verify_print_anywhere_label(self):
        return self.driver.wait_for_object("dashboard_hpPlus_printAnywhere_header")

    @string_validation("dashboard_hpPlus_forestFirst_header")
    def verify_forest_first_label(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("dashboard_hpPlus_forestFirst_header", timeout=30))

    def get_forest_first_description(self):
        return (self.driver.wait_for_object("hp_plus_forest_first_description").text).rsplit(' ',3)[0]

    @string_validation("dashboard_hpPlus_forestFirst_link")
    def verify_learn_more_text(self):
        return self.driver.wait_for_object("dashboard_hpPlus_forestFirst_link")

    def click_on_learn_more_hyperlink(self):
        return self.driver.click("hp_plus_forest_first_learn_more_link", timeout=30)

    def verify_learn_more_sustainability_label(self):
        return self.driver.verify_object_string("hp_plus_forest_first_learn_more_hyperlink", timeout=30)

    @string_validation("dashboard_hpPlus_header")
    def verify_hp_plus_widget_title(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("dashboard_hpPlus_header", timeout=20))

    def get_hp_plus_widget_printer_total_count(self):
        return int((self.driver.wait_for_object("hp_plus_widget_printer_total_count").text).split(" ")[0].replace("(",""))

    def click_account_profile_button(self):
        return self.driver.click("account_profile_button" , timeout=30)

    def get_welcome_text_first_name(self):
        return ((self.driver.wait_for_object("welcome_message").text).split(",")[1]).replace("!","").strip()

    def get_first_name_in_account_profile(self):
        self.driver.wait_for_object("personal_tab_first_name", timeout=30)
        return self.driver.get_text("personal_tab_first_name")

    def get_welcome_text(self):
        return (self.driver.wait_for_object("welcome_message").text)

    def verify_home_dashboard_welcome_text(self):
        return self.driver.wait_for_object("welcome_message", timeout=60)

    def click_organization_tab(self):
        return self.driver.click("organization_tab")

    def get_organization_name_in_account_profile(self):
        return self.driver.get_text("organization_name")

    def click_avatar_button(self):
        return self.driver.click("avatar_button", timeout=30)

    def get_organization_id(self):
        return self.driver.get_text("organization_id") 

    def get_last_four_digit_of_uid(self):
        uid = self.driver.get_text("uid")
        return uid[-4:]

    def verify_notification_bell_icon(self):
        return self.driver.wait_for_object("notification_bell_icon")

    def click_notification_bell_icon(self):
        return self.driver.click("notification_bell_icon", timeout=20)

    def verify_all_notification_text(self):
        return (self.driver.wait_for_object("all_notification_text").text).split(" ")[1]

    def get_notification_popup_text(self):
        return self.driver.wait_for_object("all_notifications_text", timeout=30).text

    def verify_notification_popup(self):
        return self.driver.wait_for_object("notification_popup", timeout=20)

    @string_validation("notification_bellNotification_noNewNotification")
    def verify_notification_popup_no_new_notification_text(self):
        return self.driver.wait_for_object("notification_bellNotification_noNewNotification", timeout=30)

    def get_notifications_count(self):
        notification_count = self.driver.wait_for_object("all_notifications_count", timeout=20).text
        return int((notification_count.split("(")[1]).replace(")",""))

    def get_notifications_count_from_notification_list(self):
        return len(self.driver.find_object("all_notifications_counts", multiple = True))

    def verify_notification_popup_ellipsis_button(self):
        return self.driver.wait_for_object("notification_popup_ellipsis_button",timeout=20)
	  
    def click_notification_popup_ellipsis_button(self):
        return self.driver.js_click("notification_popup_ellipsis_button")
	  
    def get_notification_popup_ellipsis_dropdown_options(self):
        actual_options = []
        all_options = self.driver.find_object("notification_popup_ellipsis_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def verify_bell_notification_message_icon(self):
        return self.driver.wait_for_object("bell_notification_message_icon",timeout=20)

    def verify_new_notification_printer_detail_and_location(self):
        return self.driver.wait_for_object("new_notification_printer_detail_and_location",timeout=20)

    def verify_new_notification_arrived_date_and_time(self):
        return self.driver.wait_for_object("new_notification_arrived_date_and_time",timeout=20)

    def get_mark_all_notification_read_option_status(self):
        mark_all_read_option = self.driver.get_attribute("notification_markAsReadAll","tabindex")
        if mark_all_read_option == "0":
            return True
        else:
            return False
    
    def get_mark_read_option_status_for_single_message(self):
        mark_read_option = self.driver.get_attribute("notification_markAsRead","tabindex")
        if mark_read_option == "0":
            return True
        else:
            return False

    def verify_mark_all_read_option_status(self,status):
        mark_all_read_option = self.driver.get_attribute("notification_markAsReadAll","tabindex")
        if mark_all_read_option == 0:
            mark_all_read_option = "enabled"
        else:
            mark_all_read_option = "disabled"

        if mark_all_read_option != status:
            raise UnexpectedItemPresentException("mark all read option button mismatches, it is "+mark_all_read_option)
        else:
            return True

    @string_validation("notification_markAsReadAll")
    def click_mark_all_read_option_status(self):
        return self.driver.click("notification_markAsReadAll")

    @string_validation("notification_removeAll")
    def click_remove_all_notification_button(self):
        return self.driver.click("notification_removeAll")

    def verify_notification_unread_red_dot_status(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("bell_notification_red_dot",timeout=timeout, raise_e=raise_e)

    def click_mark_read_option_for_single_notification(self):
        return self.driver.click("notification_markAsRead")

    @string_validation("notification_remove")
    def click_remove_option_for_single_notification(self):
        return self.driver.click("notification_remove")
    
    def click_single_notification_action_btn(self):
        return self.driver.click("bell_notification_action_btn")
    
    def bell_notification_mouse_hover(self):
        ac = ActionChains(self.wdvr)
        self.driver.wait_for_object("bell_notification_message", timeout=10)
        obj = self.driver.find_object("bell_notification_message")
        ac.move_to_element(obj).perform()
        return True  

    def verify_organization_count(self):
        organization_name = []
        actual_org_name = self.driver.find_object("avatar_menu_org_names",multiple=True)
        for name in actual_org_name:
            logging.info(name.text)
            organization_name.append(name.text)
        return organization_name
      
    def change_organization_name(self):
        if len(self.driver.find_object("avatar_menu_org_names",multiple=True)) > 0:
            #select second organization name
            organization_name = self.driver.get_text("organization_name_selection",format_specifier=[1])
            self.driver.click("organization_name_selection",format_specifier=[1])
            
            #after selection, verify selected organization name moved to first 
            self.verify_home_menu_btn()
            #sleep used as Home screen takes time to load
            sleep(10)
            self.click_avatar_button()
            selected_organization_name = self.driver.get_text("organization_name_selection",format_specifier=[0])
            assert organization_name == selected_organization_name

    def usage_select_dropdown_option(self,option):
        return self.driver.click("usage_select_dropdown_scan",format_specifier=[option])

    def smart_notification_mouse_hover(self):
        ac = ActionChains(self.wdvr)
        self.driver.wait_for_object("smart_notification_generated_date_and_time", timeout=10)
        obj = self.driver.find_object("smart_notification_generated_date_and_time")
        ac.move_to_element(obj).perform()
        return True

    def click_smart_notification_action_button(self):
        self.driver.wait_for_object("smart_notification_action_btn")
        return self.driver.click("smart_notification_action_btn")

    @string_validation("notification_smartNotification_dismiss")
    def click_smart_notification_dismiss_button(self):
        return self.driver.click("notification_smartNotification_dismiss")

    def verify_smart_notification_printer_detail_and_location(self):
        return self.driver.wait_for_object("smart_notification_printer_detail_and_location", timeout=20)

    def verify_smart_notification_generated_date_and_time(self):
        return self.driver.wait_for_object("smart_notification_generated_date_and_time",timeout=20)

    def verify_footer_copyright_information(self):
        return self.driver.verify_object_string("footer_copyright_information",timeout=20)

    def verify_footer_component_hp_com(self):
        return self.driver.verify_object_string("footer_component_hp_com",timeout=20)

    @string_validation("footer_hpSupport")
    def verify_footer_component_hp_support(self):
        return self.driver.wait_for_object("footer_hpSupport",timeout=20)

    @string_validation("footer_hpTermsOfUse")
    def verify_footer_component_hp_smart_admin_terms_of_use(self):
        return self.driver.wait_for_object("footer_hpTermsOfUse",timeout=20)

    @string_validation("footer_hpPrivacy")
    def verify_footer_component_hp_privacy(self):
        return self.driver.wait_for_object("footer_hpPrivacy",timeout=20)

    @string_validation("footer_personalDataRightsNotice")
    def verify_footer_component_personal_data_rights_notice(self):
        return self.driver.wait_for_object("footer_personalDataRightsNotice",timeout=20)
    
    def click_footer_component_hp_com(self):
        return self.driver.click("footer_component_hp_com",timeout=20)

    def click_footer_component_hp_support(self):
        return self.driver.click("footer_hpSupport",timeout=20)

    def click_footer_component_hp_smart_admin_terms_of_use(self):
        return self.driver.click("footer_hpTermsOfUse",timeout=20)

    def click_footer_component_hp_privacy(self):
        return self.driver.click("footer_hpPrivacy",timeout=20)

    def click_footer_component_personal_data_rights_notice(self):
        return self.driver.click("footer_personalDataRightsNotice",timeout=20)

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()

    def verify_hp_official_site_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.hp_official_site_url
    
    def verify_hp_official_support_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.hp_official_support_url
    
    def verify_hp_smart_admin_terms_of_use_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.hp_smart_admin_terms_of_use_url
    
    def verify_hp_privacy_central_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.hp_privacy_central_url

    def verify_personal_data_rights_notice_url(self):
        #Verifying if the url matches
        return self.driver.wdvr.current_url == self.personal_data_rights_notice_url