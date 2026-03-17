import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class OptionNotFound(Exception):
    pass

class StringComparisonException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class Home(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "home"

    ############################ Main Menu verifys ############################
    def verify_user_icon(self, timeout=3, raise_e=True):
        return self.driver.wait_for_object("user_icon_top_right", timeout=timeout, raise_e=raise_e)

    def verify_logout_menu_item(self):
        return self.driver.wait_for_object("user_icon_menu_log_out_item")

    def verify_home_menu_btn(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("home_menu_btn", timeout=timeout, raise_e=raise_e)
        
    def verify_users_menu_btn(self):
        return self.driver.wait_for_object("users_menu_btn")

    def verify_devices_menu_btn(self):
        return self.driver.wait_for_object("devices_menu_btn")

    def verify_solutions_menu_expand_btn(self):
        return self.driver.wait_for_object("solutions_menu_expand_btn")

    def verify_account_menu_btn(self, displayed=True):
        return self.driver.wait_for_object("account_menu_btn", invisible=not displayed)

    def verify_reports_menu_btn(self):
        return self.driver.wait_for_object("reports_menu_btn")

    def verify_support_menu_btn(self):
        return self.driver.wait_for_object("support_menu_btn")

    def verify_customers_menu_btn(self):
        return self.driver.wait_for_object("customers_menu_btn")

    def verify_policies_menu_btn(self):
        return self.driver.wait_for_object("policies_menu_btn")

    def verify_solutions_menu_btn(self):
        return self.driver.wait_for_object("solutions_menu_btn")

    def verify_proxies_menu_btn(self):
        return self.driver.wait_for_object("proxies_menu_btn")

    def verify_command_center_header(self, timeout=10):
        return self.driver.verify_object_string("command_center_header", timeout=timeout)

    def verify_home_breadcrumb(self):
        return self.driver.verify_object_string("home_breadcrumb")

    def verify_my_organization_menu_btn(self):
        return self.driver.wait_for_object("my_organization_menu_btn")

    def verify_unassigned_devices_menu_btn(self):
        return self.driver.wait_for_object("unassigned_devices_menu_btn")

    def verify_dashboard_menu_btn(self):
        return self.driver.wait_for_object("dashboard_menu_btn")

    def verify_tasks_menu_btn(self):
        return self.driver.wait_for_object("tasks_menu_btn")

    ############################ Main Menu Clicks ############################
    def click_access_denied_login_btn(self, timeout=3, raise_e=False):
        return self.driver.click("_shared_access_denied_login_btn", timeout=timeout, raise_e=raise_e)

    def click_home_menu_btn(self):
        return self.driver.click("home_menu_btn")

    def click_dashboard_menu_btn(self):
        return self.driver.click("dashboard_menu_btn")

    def click_users_menu_btn(self):
        return self.driver.click("users_menu_btn")

    def click_solutions_menu_expand_btn(self):
        return self.driver.click("solutions_menu_expand_btn")

    def click_devices_menu_btn(self):
        return self.driver.click("devices_menu_btn")

    def click_account_menu_btn(self):
        return self.driver.click("account_menu_btn")

    def click_reports_menu_btn(self):
        return self.driver.click("reports_menu_btn")

    def click_support_menu_btn(self):
        return self.driver.click("support_menu_btn")

    def click_customers_menu_btn(self):
        return self.driver.click("customers_menu_btn")

    def click_policies_menu_btn(self):
        return self.driver.click("policies_menu_btn")
    
    def click_proxies_menu_btn(self):
        return self.driver.click("proxies_menu_btn")

    def click_user_icon_top_right(self):
        return self.driver.click("user_icon_top_right")

    def click_user_icon_menu_account_profile_item(self):
        return self.driver.click("user_icon_menu_account_profile_item")

    def click_solutions_menu_btn(self):
        return self.driver.click("solutions_menu_btn")

    ############################ Sub Menu verifys ############################
    def verify_security_sub_menu_btn(self):
        return self.driver.wait_for_object("security_sub_menu_btn")

    def verify_notification_settings_sub_menu_btn(self):
        return self.driver.wait_for_object("notification_settings_sub_menu_btn")

    def verify_privacy_settings_sub_menu_btn(self):
        return self.driver.wait_for_object("privacy_settings_sub_menu_btn")

    ############################ Sub Menu Clicks ############################
    def click_security_sub_menu_btn(self):
        return self.driver.click("security_sub_menu_btn")

    def click_hp_room_sub_menu_btn(self):
        return self.driver.click("hp_room_sub_menu_btn")

    def click_account_profile_sub_menu_btn(self):
        return self.driver.click("account_profile_sub_menu_btn")

    def click_notification_settings_sub_menu_btn(self):
        return self.driver.click("notification_settings_sub_menu_btn")

    def click_privacy_settings_sub_menu_btn(self):
        return self.driver.click("privacy_settings_sub_menu_btn")

    ############################ Home Page MFE Verify ############################

    def verify_notification_mfe_card(self):
        return self.driver.wait_for_object("noti_mfe_card", timeout=20)

    def verify_notification_mfe_filter_dropdown(self):
        return self.driver.wait_for_object("noti_filter_by_dropdown")

    def verify_notification_mfe_filter_options(self, option):
        all_options = self.driver.find_object("noti_filter_by_dropdown_option", multiple=True)
        for option in all_options:
            if option.text == option:
                return True
        raise OptionNotFound("Cannot find option: " + option)

    def verify_devices_widget(self):
        return self.driver.wait_for_object("devices_widget",timeout=20)

    def verify_es_mfe(self):
        return self.driver.wait_for_object("es_mfe_view_details_btn")

    def verify_device_offline_widget(self):
        return self.driver.wait_for_object("device_offline_widget", timeout=30)

    ############################ Home Page MFE Clicks ############################

    def click_notification_mfe_filter_dropdown(self):
        return self.driver.click("noti_filter_by_dropdown")

    def click_status_total_online_device_btn(self):
        return self.driver.click("status_mfe_total_online_devices_btn", timeout=30)

    def click_status_total_users_btn(self):
        return self.driver.click("status_mfe_total_users_btn")

    def click_es_view_details_btn(self):
        return self.driver.click("es_mfe_view_details_btn")

    def click_users_widget_total_end_users_btn(self):
        return self.driver.click("users_widget_total_end_users_btn")
        
    ############################ Flows ############################

    def logout(self):
        #This needs to be run twice for some reason 
        for _ in range(2):
            if self.verify_user_icon(raise_e=False) is not False:
                self.click_user_icon_top_right()
                self.verify_logout_menu_item()
                self.driver.click("user_icon_menu_log_out_item")
        return True

    def get_user_icon_initial(self):
        return self.driver.wait_for_object("user_icon_top_right_txt").text


    #################################### Status Widget ##################################################

    def verify_devices_widget_title(self, timeout=20):
        #Verify status widget card/section title
        expected_title ="Devices"
        actual_title = self.driver.wait_for_object("devices_widget_title",timeout=timeout).text
        if expected_title == actual_title.split(" ")[0]:
            return True
        else:
            raise StringComparisonException("Devices widget title does not match: "+actual_title)

    def verify_devices_widget_total_devices_header(self):
        return self.driver.verify_object_string("devices_widget_total_devices_header")

    def verify_devices_widget_online_device(self):
        return self.driver.verify_object_string("devices_widget_online")

    def verify_devices_widget_offline_device(self):
        return self.driver.verify_object_string("devices_widget_offline")

    def verify_devices_widget_ready_status_devices(self):
        return self.driver.verify_object_string("devices_widget_ready")
 
    def verify_devices_widget_warning_status_devices(self):
        return self.driver.verify_object_string("devices_widget_warning")
 
    def verify_devices_widget_error_status_devices(self):
        return self.driver.verify_object_string("devices_widget_error")
    
    def verify_users_widget(self):
        return self.driver.wait_for_object("users_widget",timeout=20)

    def verify_users_widget_admin(self):
        return self.driver.verify_object_string("users_widget_admin")
    
    def verify_status_widget_users_status_header(self):
        return self.driver.verify_object_string("status_widget_total_users_status_header")

    def verify_status_widget_active_users(self):
        return self.driver.verify_object_string("status_widget_status_content_item_active")

    def verify_status_widget_pending_users(self):
        return self.driver.verify_object_string("status_widget_status_content_item_pending")

    def verify_status_widget_expired_users(self):
        return self.driver.verify_object_string("status_widget_status_content_item_expired")

    def get_devices_widget_total_device_count(self):
        device_widget_title_and_count = self.driver.wait_for_object("devices_widget_title").text
        split_count_value = device_widget_title_and_count.split("(")[1]
        return int(split_count_value.split(")")[0])
       
    def get_devices_widget_online_device_count(self):
        total_online_devices_count = (self.driver.wait_for_object("devices_online_count").text)
        return int(total_online_devices_count.split("/")[0])
 
    def get_devices_widget_offline_device_count(self):
        offline_count_element = self.driver.wait_for_object("devices_offline_count",timeout=30)
        total_offline_devices_count = offline_count_element.text
        return int(total_offline_devices_count.split("/")[0])
 
    def get_status_widget_total_user_count(self):
        self.get_devices_widget_total_device_count()
        total_users_count = int(self.driver.find_object("status_widget_users_total_count").text)
        return total_users_count

    def get_status_widget_enduser_user_count(self):
        total_expired_users = int(self.driver.find_object("status_widget_end_users_total_count").text)
        return total_expired_users
        
    def get_status_widget_active_user_count(self):
        total_active_users = int(self.driver.find_object("status_users_active_count").text)
        return total_active_users

    def get_status_widget_pending_user_count(self):
        total_pending_users = int(self.driver.find_object("status_users_pending_count").text)
        return total_pending_users

    def get_status_widget_expired_user_count(self):
        total_expired_users = int(self.driver.find_object("status_users_expired_count").text)
        return total_expired_users

    def wait_for_status_widget_count_load(self, format_specifier): 
        for _ in range(6):
            try:
                int(self.driver.wait_for_object("device_widget_devices_total_count").text)
            except ValueError:
                logging.debug("The count hasn't loaded yet")
                sleep(5)

    #################################### Solution Entitled Widget ##################################################

    def verify_solution_entitled_widget(self):
        return self.driver.wait_for_object("solution_entitled_widget",timeout=20)

    def verify_solution_entitled_widget_title(self):
        return self.driver.verify_object_string("solution_entitled_widget_title")

    def verify_solution_entitled_view_details_button(self):
        return self.driver.wait_for_object("solution_entitled_view_details_btn")

    def click_solution_entitled_view_details_button(self):
        return self.driver.click("solution_entitled_view_details_btn")

    def verify_solution_entitled_hp_secure_fleet_manager(self):
        return self.driver.verify_object_string("solution_entitled_hp_secure_fleet_manager_label")

    def get_solution_entitled_device_count(self):
        entitled_device_count = int(self.driver.find_object("solution_entitled_device_count").text)
        return entitled_device_count

    #################################### HP Secure Fleet Manager Widget ##################################################

    def verify_hp_secure_fleet_manager_widget_title(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_widget_title",timeout=20)

    def verify_hp_secure_fleet_manager_view_details_button(self):
        return self.driver.wait_for_object("hp_secure_fleet_manager_view_details_btn")

    def click_hp_secure_fleet_manager_view_details_button(self):
        return self.driver.click("hp_secure_fleet_manager_view_details_btn", timeout=30)

    def get_hp_secure_fleet_manager_device_count(self):
        sleep(5) # Adding wait for the count to load
        entitled_device_count = int(self.driver.find_object("hp_secure_fleet_manager_device_count").text)
        return entitled_device_count
        
    #################################### IT Admin ##################################################

    def verify_customer_selector_displayed(self, displayed=True):
        return self.driver.wait_for_object("choose_customer_link", invisible=not displayed)

    def click_support_center_button(self):
        return self.driver.click("support_center_btn",timeout=10)

    def verify_support_and_resources_title(self):
        return self.driver.verify_object_string("support_and_resources_title")

    def verify_support_center_options(self,option_name):
        support_option = self.driver.find_object("support_center_options",multiple=True)
        for option in support_option:
            if option_name in option.text:
                return True
        raise OptionNotFound("Support Option: "+option_name+"is not avaialble in support center")

    def verify_support_center_option_count(self,option_count):
        assert option_count == len(self.driver.find_object("support_center_options", multiple = True))

    def verify_my_organization_link_displayed(self, displayed=True):
        return self.driver.wait_for_object("avatar_my_organization_link", invisible=not displayed)

    def verify_customer_menu_displayed(self,displayed=True):
        return self.driver.wait_for_object("customers_menu_btn", invisible=not displayed)

    #################################### Bell Notification ##################################################

    def click_notification_bell_button(self):
        return self.driver.click("bell_notification_button")

    def verify_notifications_popup(self):
        return self.driver.wait_for_object("bell_notification_popup")

    def verify_notifications_title(self):
        return self.driver.verify_object_string("bell_notification_title")

    #################################### Avatar Menu Organization ##################################################

    def verify_organization_count(self):
        assert len(self.driver.find_object("avatar_menu_org_selector",multiple=True)) > 0

    #################################### Device Offline widget ##################################################

    def verify_device_offline_widget_title(self):
        expected_title ="Devices Offline"
        actual_title = self.driver.wait_for_object("device_offline_widget_title").text
        if expected_title == actual_title.split("(")[0]:
            return True
        else:
            raise StringComparisonException("Devices offline widget title does not match with: "+actual_title)

    def get_device_offline_widget_offline_devices_count(self):
        title_with_count= self.driver.wait_for_object("device_offline_widget_title").text
        split_text_value = title_with_count.split("(")
        return int(split_text_value[1].split(")")[0])
    
    def verify_device_offline_widget_no_offline_devices_warnign_icon(self):
        return self.driver.wait_for_object("device_offline_widget_no_offline_devices_warnign_icon")

    def verify_device_offline_widget_no_offline_devices_warnign_message(self):
        return self.driver.verify_object_string("device_offline_widget_no_offline_devices_warning_message")
    
    def verify_device_offline_widget_view_details_button(self):
        return self.driver.verify_object_string("device_offline_widget_view_details_btn")
    
    def click_device_offline_widget_view_details_button(self):
        return self.driver.click("device_offline_widget_view_details_btn")
    
    def verify_device_offline_widget_view_details_button_disabled(self):
        if self.driver.find_object("device_offline_widget_view_details_btn").is_enabled():
            raise UnexpectedItemPresentException("Save button is enabled")
        return True 

    #################################### ECP Footer ##################################################

    def verify_ecp_footer_copyright(self):
        return self.driver.verify_object_string("ecp_footer_copyright_lbl")

    def verify_ecp_footer_terms_of_service(self):
        self.driver.verify_object_string("ecp_footer_terms_of_service_link")
        self.driver.click("ecp_footer_terms_of_service_link")
        return self.driver.wait_for_new_window()

    def verify_ecp_footer_privacy_statement(self):
        self.driver.verify_object_string("ecp_footer_privacy_statement_link")
        self.driver.click("ecp_footer_privacy_statement_link")
        return self.driver.wait_for_new_window()

    #################################### Customer Selector ##################################################

    def choose_customer(self,customer_name=None):
        self.driver.click("choose_customer_link")
        if customer_name!=None:
            self.driver.send_keys("choose_customer_search_txt", customer_name)
        self.driver.click("select_customer")
        return self.driver.click("choose_btn")

    def verify_customer_selected(self,timeout=20):
        cust_val=self.driver.wait_for_object("choose_customer_link", timeout=timeout).text
        if cust_val == "Choose Customer":
            return False
        return True 
    
    #################################### Notification Settings ##################################################

    def click_notification_popup_three_dot_menu_button(self):
        return self.driver.click("bell_notification_menu_button")
   
    def verify_notification_settings_option(self):
        return self.driver.verify_object_string("notification_settings_option")

    def click_notification_settings_option(self):
        return self.driver.click("notification_settings_option")

    def verify_notification_settings_all_notification_title(self):
        return self.driver.verify_object_string("notification_settings_all_title")
   
    def verify_notification_settings_description(self):
        return self.driver.verify_object_string("notification_settings_desc")
   
    def verify_notification_settings_email_notification_checkbox_label(self):
        return self.driver.verify_object_string("notification_settings_email_notification_checkbox_label")
   
    def verify_notification_settings_email_notification_checkbox(self):
        return self.driver.wait_for_object("notification_settings_email_notification_checkbox")

    def click_notification_settings_email_notification_checkbox(self):
        return self.driver.click("notification_settings_email_notification_checkbox")

    def verify_notification_settings_contextual_footer_is_displayed(self):
        self.driver.wait_for_object("notification_settings_contextual_footer")

    def verify_notification_settings_contextual_footer_is_not_displayed(self):
        self.driver.wait_for_object("notification_settings_contextual_footer", invisible=True)

    def verify_notification_settings_save_button(self):
        return self.driver.verify_object_string("notification_settings_tab_save_button")
   
    def click_notification_settings_save_button(self):
        return self.driver.click("notification_settings_tab_save_button")
   
    def verify_notification_settings_cancel_button(self):
        return self.driver.verify_object_string("notification_settings_tab_cancel_button")

    def click_notification_settings_cancel_button(self):
        return self.driver.click("notification_settings_tab_cancel_button")

    def verify_notification_settings_reset_to_default_button(self):
        return self.driver.verify_object_string("notification_settings_reset_to_default_button")
   
    def click_notification_settings_reset_to_default_button(self):
        return self.driver.click("notification_settings_reset_to_default_button")

    def verify_notification_settings_reset_to_default_popup_desc(self):
        return self.driver.verify_object_string("notification_settings_reset_to_default_popup_desc")

    def verify_notification_settings_reset_to_default_popup_cancel_button(self):
        return self.driver.verify_object_string("notification_settings_reset_to_default_popup_cancel_button")

    def click_notification_settings_reset_to_default_popup_cancel_button(self):
        return self.driver.click("notification_settings_reset_to_default_popup_cancel_button")

    def verify_notification_settings_reset_to_default_popup_reset_button(self):
        return self.driver.verify_object_string("notification_settings_reset_to_default_popup_reset_button")

    def click_notification_settings_reset_to_default_popup_reset_button(self):
        return self.driver.click("notification_settings_reset_to_default_popup_reset_button")
   
    def get_notification_settings_email_checkbox_status(self):
        checkbox = self.driver.wait_for_object("notification_settings_email_notification_checkbox")
        return checkbox.is_selected()
    
#################################### Device Policy Status Widget #############################################

    def verify_device_policy_status_widget(self):
        return self.driver.wait_for_object("device_policy_status_widget",timeout=20)

    def verify_device_policy_status_widget_title(self):
        expected_title ="Device Policy Status"
        actual_title = self.driver.wait_for_object("device_policy_status_widget_title").text
        if expected_title == actual_title.split("(")[0]:
            return True
        else:
            raise StringComparisonException("Device Policy Status widget title does not match with: "+actual_title)

    def verify_device_policy_status_view_details_button(self):
        return self.driver.wait_for_object("device_policy_status_view_details_btn")

    def click_device_policy_status_view_details_button(self):
        return self.driver.click("device_policy_status_view_details_btn")