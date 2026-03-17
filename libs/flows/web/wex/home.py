from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep 
import logging

class UnexpectedItemPresentException(Exception):
    pass

class Home(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "home"

   ############################ Main Menu verifys ############################

    def verify_sidemenu_home_btn(self):
        return self.driver.wait_for_object("home_menu_btn", raise_e=False, timeout=20)
    
    def verify_sidemenu_analytics_button(self):
        return self.driver.wait_for_object("sidemenu_analytics_button", raise_e=False, timeout=20)
        
    def verify_sidemenu_devices_button(self):
        return self.driver.wait_for_object("sidemenu_devices_button", raise_e=False, timeout=20)
    
    def verify_sidemenu_remediations_button(self):
        return self.driver.wait_for_object("sidemenu_remediations_button", raise_e=False, timeout=20)
        
    def verify_sidemenu_pulses_button(self):
        return self.driver.wait_for_object("sidemenu_pulses_button", raise_e=False, timeout=20)
        
    def verify_sidemenu_labs_button(self):
        return self.driver.wait_for_object("sidemenu_labs_button", raise_e=False, timeout=20)

    def verify_sidemenu_alerts_button(self):
        return self.driver.wait_for_object("sidemenu_alerts_button", raise_e=False, timeout=20)
    
    def verify_sidemenu_active_alerts_button(self):
        return self.driver.wait_for_object("sidemenu_active_alerts_button", raise_e=False, timeout=20)
    
    def verify_sidemenu_alerts_management_button(self):
        return self.driver.wait_for_object("sidemenu_alerts_management_button", raise_e=False, timeout=20)

    def verify_sidemenu_scripts_button(self):
        return self.driver.wait_for_object("sidemenu_scripts_button", raise_e=False, timeout=20)
    
    def verify_sidemenu_groups_button(self):
        return self.driver.wait_for_object("sidemenu_groups_button", raise_e=False, timeout=20)
    
    def verify_sidemenu_remediations_policies_button(self):
        return self.driver.wait_for_object("sidemenu_remediations_policies_button", raise_e=False, timeout=20)
    
    def verify_sidemenu_remediations_secrets_button(self):
        return self.driver.wait_for_object("sidemenu_remediations_secrets_button", raise_e=False, timeout=20)

    def verify_sidemenu_accounts_button(self):
        return self.driver.wait_for_object("sidemenu_accounts_button", raise_e=False, timeout=20)

    def verify_sidemenu_integrations_button(self):
        return self.driver.wait_for_object("sidemenu_integrations_button", raise_e=False, timeout=20)

    def verify_sidemenu_remediations_activity_button(self):
        return self.driver.wait_for_object("sidemenu_remediations_activity_button", raise_e=False, timeout=20)

    def verify_sidemenu_remediations_scripts_button(self):
        return self.driver.wait_for_object("sidemenu_remediations_scripts_button", raise_e=False, timeout=20)  
    
    def verify_home_menu_btn(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("home_menu_btn", timeout=timeout, raise_e=raise_e)

    def verify_side_menu_expand_button_is_displayed(self):
        return self.driver.wait_for_object("side_menu_expand_button",raise_e=False)
    
    def verify_home_page_title(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("home_breadcrumb",timeout=timeout, raise_e=raise_e)
        
    def verify_side_menu_modules_title(self):
        return self.driver.wait_for_object("side_menu_modules_title")

    def verify_modules_fleet_management_button(self):
        return self.driver.wait_for_object("modules_fleet_management_button")
    
    def verify_modules_fleet_management_button_is_expanded(self):
        return self.driver.wait_for_object("modules_fleet_management_expanded",raise_e=False)

    def click_sidemenu_analytics_button(self):
        return self.driver.click("sidemenu_analytics_button",timeout=30)        
    
    def verify_sidemenu_devices_button_is_expanded(self):
        return self.driver.wait_for_object("sidemenu_devices_dropdown_option_expanded",raise_e=False)

    def verify_sidemenu_remediations_button_is_expanded(self):
        return self.driver.wait_for_object("sidemenu_remediations_dropdown_option_expanded",raise_e=False)

    def verify_fleet_management_print_proxies_button(self):
        return self.driver.wait_for_object("fleet_management_print_proxies_button",timeout=30)

    def verify_fleet_management_policies_button(self):
        return self.driver.wait_for_object("fleet_management_policies_button",timeout=30)
    
    def verify_avatar_icon(self, timeout=3, raise_e=True):
        return self.driver.wait_for_object("avatar_icon_top_right", timeout=timeout, raise_e=raise_e)
    
    def verify_avatar_user_profile_card(self):
        return self.driver.wait_for_object("avatar_user_profile_card")
    
    def verify_user_profile_logout_button(self):
        return self.driver.wait_for_object("avatar_user_profile_card_logout_button")

    def verify_fleet_management_breadcrumb(self):
        sleep(3)
        return self.driver.verify_object_string("fleet_management_breadcrumb",timeout=40) # Dashboard page is taking a while to load sometimes, so we increase the timeout

    def verify_sidemenu_devices_view_pcs_button(self):
        return self.driver.wait_for_object("sidemenu_devices_view_pcs_button", raise_e=False)
   
    def verify_sidemenu_devices_view_virtual_machines_button(self):
        return self.driver.wait_for_object("sidemenu_devices_view_virtual_machines_button", raise_e=False)
   
    def verify_sidemenu_devices_view_physical_assets_button(self):
        return self.driver.wait_for_object("sidemenu_devices_view_physical_assets_button", raise_e=False)
   
    def verify_sidemenu_devices_view_printers_button(self):
        return self.driver.wait_for_object("sidemenu_devices_view_printers_button", raise_e=False)
    
    def verify_sidemenu_settings_button(self):
        return self.driver.wait_for_object("sidemenu_settings_button",raise_e=False, timeout=30)
 
    def click_sidemenu_home_btn(self):
        return self.driver.click("home_menu_btn", timeout=30)
 
    def click_sidemenu_devices_view_pcs_button(self):
        return self.driver.click("sidemenu_devices_view_pcs_button",timeout=30)
   
    def click_sidemenu_devices_view_virtual_machines_button(self):
        return self.driver.click("sidemenu_devices_view_virtual_machines_button",timeout=30)
   
    def click_sidemenu_devices_view_physical_assets_button(self):
        return self.driver.click("sidemenu_devices_view_physical_assets_button",timeout=30)
   
    def click_sidemenu_devices_view_printers_button(self):
        return self.driver.click("sidemenu_devices_view_printers_button",timeout=30)
    
    def click_sidemenu_settings_button(self):
        return self.driver.click("sidemenu_settings_button",timeout=30)
    
    def click_sidemenu_accounts_button(self):
        return self.driver.click("sidemenu_accounts_button",timeout=30)

    def click_sidemenu_pulses_button(self):
        return self.driver.click("sidemenu_pulses_button",timeout=30)

    def click_sidemenu_integrations_button(self):
        return self.driver.click("sidemenu_integrations_button",timeout=30)

    def click_sidemenu_scripts_button(self):
        return self.driver.click("sidemenu_scripts_button")
    
    def click_sidemenu_alerts_button(self):
        return self.driver.click("sidemenu_alerts_button")

    def click_sidemenu_labs_button(self):
        return self.driver.click("sidemenu_labs_button")
    
    def click_sidemenu_active_alerts_button(self):
        return self.driver.click("sidemenu_active_alerts_button", timeout=30)

    def click_sidemenu_alerts_management_button(self):
        return self.driver.click("sidemenu_alerts_management_button", timeout=30)

    ############################ Main Menu Clicks ############################

    def click_home_menu_btn(self):
        return self.driver.click("home_menu_btn")
    
    def click_side_menu_expand_button(self):
        return self.driver.click("side_menu_close_button")
    
    def click_side_menu_collapse_button(self):
        return self.driver.click("side_menu_expand_button")

    def click_modules_fleet_management_button(self):
        return self.driver.click("modules_fleet_management_button",timeout=30)
    
    def click_modules_fleet_management_expand_button(self):
        return self.driver.click("modules_fleet_management_expand_button",timeout=30)

    def click_sidemenu_devices_printers_dropdown_option(self):
        return self.driver.click("sidemenu_devices_printers_dropdown_option",timeout=40)

    def click_sidemenu_devices_button(self):
        return self.driver.click("sidemenu_devices_button", timeout=30)
    
    def click_sidemenu_devices_dropdown_button(self):
        return self.driver.click("sidemenu_devices_dropdown_button", timeout=30)

    def click_sidemenu_remediations_button(self):
        return self.driver.click("sidemenu_remediations_button",timeout=30)
    
    def click_sidemenu_remediations_dropdown_button(self):
        return self.driver.click("sidemenu_remediations_dropdown_button",timeout=30)

    def click_sidemenu_groups_button(self):
        return self.driver.click("sidemenu_groups_button",timeout=30)

    def click_sidemenu_remediations_policies_button(self):
        return self.driver.click("sidemenu_remediations_policies_button",timeout=30)

    def click_sidemenu_remediations_secrets_button(self):
        return self.driver.click("sidemenu_remediations_secrets_button",timeout=30)

    def click_sidemenu_remediations_activity_button(self):
        return self.driver.click("sidemenu_remediations_activity_button",timeout=30)

    def click_sidemenu_remediations_scripts_button(self):
        return self.driver.click("sidemenu_remediations_scripts_button",timeout=30)
    
    def click_remediations_policies_dropdown_option(self):
        return self.driver.click("remediations_policies_dropdown_option",timeout=30)
    
    def click_fleet_management_print_proxies_button(self):
        return self.driver.click("fleet_management_print_proxies_button",timeout=30)

    def click_fleet_management_policies_button(self):
        return self.driver.click("fleet_management_policies_button",timeout=30)

    def click_fleet_management_dashboard_button(self):
        return self.driver.click("fleet_management_dashboard_button",timeout=30)
    
    def click_avatar_icon_top_right(self):
        return self.driver.click("avatar_icon_top_right")

    def logout(self):
            if self.verify_avatar_icon(raise_e=False):
                self.click_avatar_icon_top_right()
                self.verify_avatar_user_profile_card()
                self.verify_user_profile_logout_button()
                self.driver.click("avatar_user_profile_card_logout_button")
                return True

    def click_fleet_management_breadcrumb(self):
        return self.driver.click("fleet_management_breadcrumb")

    def verify_sidemenu_devices_dropdown_list(self):
        return self.driver.wait_for_object("sidemenu_devices_dropdown_list")
    
    def get_sidemenu_devices_options_list_items(self):
        actual_options = []
        all_options = self.driver.find_object("sidemenu_devices_dropdown_list_items",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def verify_sidemenu_remediations_dropdown_list(self):
        return self.driver.wait_for_object("sidemenu_remediations_dropdown_list")

    def get_sidemenu_remediations_options_list_items(self):
        actual_options = []
        all_options = self.driver.find_object("sidemenu_remediations_dropdown_list_items",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options
    
    def click_sidemenu_devices_dropdown_list_printers_button(self):
        return self.driver.click("sidemenu_devices_dropdown_list_printers_button",timeout=30)

    def click_sidemenu_remediations_dropdown_list_policies_button(self):
        return self.driver.click("sidemenu_remediations_dropdown_list_policies_button",timeout=30)

    ############################ Home - Fleet Inventory Widget ############################  
     
    def verify_home_fleet_inventory_widget(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("home_fleet_inventory_widget", timeout=30))

    def verify_home_fleet_inventory_widget_is_displayed(self):
        return self.driver.wait_for_object("home_fleet_inventory_widget", raise_e=False, timeout=20)

    def verify_fleet_inventory_widget_title(self):
        return self.driver.verify_object_string("fleet_inventory_widget_title")

    def verify_fleet_inventory_pcs_button(self):
        return self.driver.wait_for_object("fleet_inventory_pcs_button", raise_e=False)

    def verify_fleet_inventory_pcs_icon(self):
        return self.driver.wait_for_object("fleet_inventory_pcs_icon")
    
    def verify_fleet_inventory_pcs_title(self):
        return self.driver.verify_object_string("fleet_inventory_pcs_title")
    
    def verify_fleet_inventory_pcs_count(self):
        return self.driver.wait_for_object("fleet_inventory_pcs_count")

    def verify_fleet_inventory_printers_button(self):
        return self.driver.wait_for_object("fleet_inventory_printers_button", raise_e=False)
    
    def verify_fleet_inventory_printers_icon(self):
        return self.driver.wait_for_object("fleet_inventory_printers_icon")
    
    def verify_fleet_inventory_printers_title(self):
        return self.driver.verify_object_string("fleet_inventory_printers_title")
    
    def verify_fleet_inventory_printers_count(self):
        return self.driver.wait_for_object("fleet_inventory_printers_count")

    def verify_fleet_inventory_virtual_machines_button(self):
        return self.driver.wait_for_object("fleet_inventory_virtual_machines_button", raise_e=False)
    
    def verify_fleet_inventory_virtual_machines_icon(self):
        return self.driver.wait_for_object("fleet_inventory_virtual_machines_icon")

    def verify_fleet_inventory_virtual_machines_title(self):
        return self.driver.verify_object_string("fleet_inventory_virtual_machines_title")
    
    def verify_fleet_inventory_virtual_machines_count(self):
        return self.driver.wait_for_object("fleet_inventory_virtual_machines_count")

    def verify_fleet_inventory_video_endpoints_button(self):
        return self.driver.wait_for_object("fleet_inventory_video_endpoints_button", raise_e=False)

    def verify_fleet_inventory_video_endpoints_icon(self):
        return self.driver.wait_for_object("fleet_inventory_video_endpoints_icon")

    def verify_fleet_inventory_video_endpoints_title(self):
        return self.driver.verify_object_string("fleet_inventory_video_endpoints_title")

    def verify_fleet_inventory_video_endpoints_add_on_btn(self):
        return self.driver.wait_for_object("fleet_inventory_video_endpoints_add_on_btn")
    
    def get_fleet_inventory_video_endpoints(self):
        return self.driver.get_text("fleet_inventory_video_endpoints_add_on_btn")

    def verify_fleet_inventory_telephones_button(self):
        return self.driver.wait_for_object("fleet_inventory_telephones_button", raise_e=False)
    
    def verify_fleet_inventory_telephones_icon(self):
        return self.driver.wait_for_object("fleet_inventory_telephones_icon")

    def verify_fleet_inventory_telephones_title(self):
        return self.driver.verify_object_string("fleet_inventory_telephones_title")

    def verify_fleet_inventory_telephones_add_on_btn(self):
        return self.driver.wait_for_object("fleet_inventory_telephones_add_on_btn")
    
    def get_fleet_inventory_telephones(self):
        return self.driver.get_text("fleet_inventory_telephones_add_on_btn")

    ######################################## Home - View Alerts Widget ########################################

    def verify_home_view_alerts_widget(self):
        return self.driver.wait_for_object("home_view_alerts_widget", raise_e=False, timeout=20)
    
    def verify_home_view_full_list_of_alerts_widget(self):
        return self.driver.wait_for_object("home_view_full_list_of_alerts_widget", raise_e=False, timeout=20)
    
    def get_home_view_full_list_of_alerts_widget_text(self):
        return self.driver.wait_for_object("home_view_full_list_of_alerts_widget", raise_e=False, timeout=20).text
    
    def click_home_view_full_list_of_alerts_widget(self):
        return self.driver.click("home_view_full_list_of_alerts_widget", timeout=30)
    
    def get_drill_down_to_alerts_widget(self):
        return self.driver.wait_for_object("active_alerts_page_breadcrumb", raise_e=False, timeout=20).text

    ############################ Home - Fleet Inventory Widget Printers Chart ############################

    def click_fleet_inventory_printers_button(self):
        return self.driver.click("fleet_inventory_printers_button",timeout=20)
    
    def verify_fleet_inventory_card_printers_chart_chart(self):
        return self.driver.wait_for_object("fleet_inventory_card_printers_chart_chart",timeout=30)
    
    def verify_fleet_inventory_card_printers_chart_count(self):
        return self.driver.wait_for_object("fleet_inventory_card_printers_chart_count")
    
    def verify_fleet_inventory_card_printers_chart_online_button(self):
        return self.driver.wait_for_object("fleet_inventory_card_printers_chart_online_button",timeout=30)
    
    def verify_fleet_inventory_card_printers_chart_offline_button(self):
        return self.driver.wait_for_object("fleet_inventory_card_printers_chart_offline_button")
    
    def get_fleet_inventory_printers_count(self):
        count = self.driver.get_text("fleet_inventory_printers_count")
        return int(count)
    
    def get_fleet_inventory_card_printers_chart_count(self):
        count = self.driver.get_text("fleet_inventory_card_printers_chart_count")
        return int(count)
    
    def click_fleet_inventory_printers_count(self):
        return self.driver.click("fleet_inventory_printers_count",timeout=30)
    
    def verify_fleet_inventory_card_printers_chart_online_button_is_enabled(self):
        sleep(3)
        online_button = self.driver.get_attribute("fleet_inventory_card_printers_chart_online_button", "aria-pressed", raise_e=False)
        if online_button == "true":
            return True
        else:
            print("Printer Inventory graph online button is disabled")
            return False
    
    def verify_fleet_inventory_card_printers_chart_offline_button_is_enabled(self):
        sleep(3)
        offline_button = self.driver.get_attribute("fleet_inventory_card_printers_chart_offline_button", "aria-pressed", raise_e=False)
        if offline_button == "true":
            return True
        else:
            print("Printer Inventory graph offline button is disabled")
            return False
    
    def click_fleet_inventory_card_printers_chart_offline_button(self):
        return self.driver.click("fleet_inventory_card_printers_chart_offline_button",timeout=30)

    def click_fleet_inventory_card_printers_chart_online_button(self):
        return self.driver.click("fleet_inventory_card_printers_chart_online_button",timeout=30)

    def get_fleet_inventory_card_printers_chart_online_button_count(self):
        online_button_label = self.driver.get_attribute("fleet_inventory_card_printers_chart_online_graph", "aria-label")
        if "Online printers:" in online_button_label:
            count = online_button_label.split(":")[1].strip().split()[0]
            return int(count)
        else:
            raise UnexpectedItemPresentException(f"Unexpected label format: '{online_button_label}'")

    def get_fleet_inventory_card_printers_chart_offline_button_count(self):
        offline_button_label = self.driver.get_attribute("fleet_inventory_card_printers_chart_offline_graph", "aria-label", raise_e=False)
        if "Offline printers:" in offline_button_label:
            count = offline_button_label.split(":")[1].strip().split()[0]
            return int(count)
        else:
            raise UnexpectedItemPresentException(f"Unexpected label format: '{offline_button_label}'")

    def click_fleet_inventory_card_printers_chart_online_chart(self):
        return self.driver.click("fleet_inventory_card_printers_chart_online_graph",timeout=30)
    
    def click_fleet_inventory_card_printers_chart_offline_chart(self):
        return self.driver.click("fleet_inventory_card_printers_chart_offline_graph",timeout=30)

    def verify_fleet_inventory_card_printers_chart_offline_graph(self):
        return self.driver.wait_for_object("fleet_inventory_card_printers_chart_offline_graph",timeout=30)

    def verify_fleet_inventory_card_printers_chart_view_list_of_printers_button(self):
        return self.driver.wait_for_object("fleet_inventory_card_printers_chart_view_list_of_printers_button",timeout=30)
    
    def verify_fleet_inventory_card_printers_chart_printers_by_connectivity_label(self):
        return self.driver.verify_object_string("fleet_inventory_card_printers_chart_printers_by_connectivity_label")
    
    def click_fleet_inventory_card_printers_chart_view_list_of_printers_button(self):
        return self.driver.click("fleet_inventory_card_printers_chart_view_list_of_printers_button",timeout=30)

    ###################################### Analytics Page ######################################

    def click_analytics_fleet_management_button(self):
        return self.driver.click("analytics_fleet_management_button",timeout=30)

    ############################# Experience Score Widget #############################

    def verify_experience_score_widget(self):
        return self.driver.wait_for_object("home_experience_score_widget", raise_e=False, timeout=20)
    
    def verify_experience_score_widget_overall_score(self):
        return self.driver.wait_for_object("experience_score_widget_overall_score", raise_e=False)
    
    def verify_experience_score_widget_sentiment(self):
        return self.driver.wait_for_object("experience_score_widget_sentiment", raise_e=False)
    
    def verify_experience_score_widget_system_health(self):
        return self.driver.wait_for_object("experience_score_widget_system_health", raise_e=False)
    
    def verify_experience_score_widget_os_performance(self):
        return self.driver.wait_for_object("experience_score_widget_os_performance", raise_e=False)
    
    def verify_experience_score_widget_network_health(self):
        return self.driver.wait_for_object("experience_score_widget_network_health", raise_e=False)
    
    def verify_experience_score_widget_security(self):
        return self.driver.wait_for_object("experience_score_widget_security", raise_e=False)

    def verify_experience_score_widget_applications(self):
        return self.driver.wait_for_object("experience_score_widget_applications", raise_e=False)

    def verify_experience_score_widget_collaboration(self):
        return self.driver.wait_for_object("experience_score_widget_collaboration", raise_e=False)

    def verify_experience_score_widget_drill_down_overall_score(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_overall_score", raise_e=False)
    
    def verify_experience_score_widget_drill_down_system_health(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_system_health", raise_e=False)
    
    def verify_experience_score_widget_drill_down_os_performance(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_os_performance", raise_e=False)
    
    def verify_experience_score_widget_drill_down_security(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_security", raise_e=False)
    
    def verify_experience_score_widget_drill_down_sentiment(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_sentiment", raise_e=False)
    
    def verify_experience_score_widget_drill_down_network_health(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_network_health", raise_e=False)
    
    def verify_experience_score_widget_drill_down_applications(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_applications", raise_e=False)
    
    def verify_experience_score_widget_drill_down_collaboration(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_collaboration", raise_e=False)
    
    def get_experience_score_widget_drill_down_sentiment(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_sentiment").text
    
    def get_experience_score_widget_drill_down_network_health(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_network_health").text
    
    def get_experience_score_widget_drill_down_applications(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_applications").text
    
    def get_experience_score_widget_drill_down_collaboration(self):
        return self.driver.wait_for_object("experience_score_widget_drill_down_collaboration").text
    
    def click_experience_score_widget_overall_score(self):
        return self.driver.click("experience_score_widget_overall_score",timeout=30, raise_e=False)
   
    def get_analytics_experience_score_page(self):
        return self.driver.wait_for_object("analytics_experience_score_page_breadcrumb", timeout=30, raise_e=False).text
   
    def click_experience_score_widget_system_health(self):
        return self.driver.click("experience_score_widget_system_health", raise_e=False)
   
    def click_experience_score_widget_os_performance(self):
        return self.driver.click("experience_score_widget_os_performance", raise_e=False)
   
    def click_experience_score_widget_security(self):
        return self.driver.click("experience_score_widget_security", raise_e=False)
 
    def click_experience_score_widget_sentiment(self):
        return self.driver.click("experience_score_widget_sentiment", raise_e=False)
   
    def click_experience_score_widget_network_health(self):
        return self.driver.click("experience_score_widget_network_health", raise_e=False)
   
    def click_experience_score_widget_applications(self):
        return self.driver.click("experience_score_widget_applications", raise_e=False)
   
    def click_experience_score_widget_collaboration(self):
        return self.driver.click("experience_score_widget_collaboration", raise_e=False)

    ######################################## Experience Overtime Widget  #########################################
    
    def verify_experience_overtime_widget(self):
        return self.driver.wait_for_object("home_experience_overtime_widget", raise_e=False)

    def verify_experience_overtime_widget_days_filter(self):
        return self.driver.wait_for_object("experience_overtime_widget_days_filter", raise_e=False)
    
    def click_experience_overtime_widget_days_filter(self):
        return self.driver.click("experience_overtime_widget_days_filter", raise_e=False)
    
    def get_experience_overtime_widget_days_filter_options(self):
        actual_options = []
        all_options = self.driver.find_object("experience_overtime_widget_days_filter_options", multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    def click_experience_overtime_widget_days_filter_option(self, option):
        if option == "Last 30 days":
            self.driver.click("experience_overtime_widget_days_filter_option_30_days", raise_e=False)
        elif option == "Last 60 days":
            self.driver.click("experience_overtime_widget_days_filter_option_60_days", raise_e=False)
        elif option == "Last 90 days":
            self.driver.click("experience_overtime_widget_days_filter_option_90_days", raise_e=False)
    
    def verify_experience_overtime_widget_days_filter_selected_option(self, option):
        selected_option = self.driver.wait_for_object("experience_overtime_widget_days_filter_selected_option",raise_e=False).text
        if selected_option == option:
            return True
        else:
            print(f"Selected option '{selected_option}' does not match expected option '{option}'.")
            return False

    def verify_experience_overtime_chart(self):
        return self.driver.wait_for_object("experience_overtime_chart", raise_e=False, timeout=30)
    
    ######################################## Apps with Most Crashes Widget  #########################################

    def verify_apps_with_most_crashes_widget(self):
        return self.driver.wait_for_object("home_apps_with_most_crashes_widget", raise_e=False, timeout=30)

    ############################################ Onboarding Notifications ############################################

    def verify_onboarding_notifications_button(self):
        return self.driver.wait_for_object("onboarding_notifications_button", raise_e=False)
    
    def click_onboarding_notifications_button(self):
        sleep(3)
        return self.driver.js_click("onboarding_notifications_button", raise_e=False)
    
    def verify_onboarding_notifications_popup(self):
        return self.driver.wait_for_object("onboarding_notifications_popup", raise_e=False)

    def verify_onboarding_notifications_first_steps_title(self):
        return self.driver.wait_for_object("onboarding_notifications_first_steps_title", raise_e=False).text
    
    def verify_add_device_notification_button(self):
        return self.driver.wait_for_object("add_device_notification_button", raise_e=False)
    
    def verify_invite_team_notification_button(self):
        return self.driver.wait_for_object("invite_team_notification_button", raise_e=False)
    
    def verify_complete_your_profile_notification_button(self):
        return self.driver.wait_for_object("complete_your_profile_notification_button", raise_e=False)
    
    def verify_explore_integrations_notification_button(self):
        return self.driver.wait_for_object("explore_integrations_notification_button", raise_e=False)
    
    def verify_onboarding_notifications_discover_more_title(self):
        return self.driver.wait_for_object("onboarding_notifications_discover_more_title", raise_e=False).text
    
    def verify_improve_experience_score_notification_button(self):
        return self.driver.wait_for_object("improve_experience_score_notification_button", raise_e=False)
    
    def verify_gather_employee_feedback_notification_button(self):
        return self.driver.wait_for_object("gather_employee_feedback_notification_button", raise_e=False)
    
    def verify_get_help_and_provide_feedback_notification_button(self):
        return self.driver.wait_for_object("get_help_and_provide_feedback_notification_button", raise_e=False)
    
    def verify_stay_up_to_date_alerts_button(self):
        return self.driver.wait_for_object("stay_up_to_date_alerts_button", raise_e=False)
    
    def verify_troubleshoot_device_issues_button(self):
        return self.driver.wait_for_object("troubleshoot_device_issues_button", raise_e=False)
    
    def verify_add_a_script_button(self):
        return self.driver.wait_for_object("add_a_script_button", raise_e=False)
    
    def verify_understand_workforce_sentiment_notification_button(self):
        return self.driver.wait_for_object("understand_workforce_sentiment_notification_button", raise_e=False)
    
    def click_add_device_notification_button(self):
        return self.driver.click("add_device_notification_button", raise_e=False)
    
    def click_invite_team_notification_button(self):
        return self.driver.click("invite_team_notification_button", raise_e=False)
    
    def click_complete_your_profile_notification_button(self):
        return self.driver.click("complete_your_profile_notification_button", raise_e=False)
    
    def click_explore_integrations_notification_button(self):
        return self.driver.js_click("explore_integrations_notification_button")
    
    def click_improve_experience_score_notification_button(self):
        return self.driver.click("improve_experience_score_notification_button", raise_e=False)
    
    def click_gather_employee_feedback_notification_button(self):
        return self.driver.click("gather_employee_feedback_notification_button", raise_e=False)
    
    def click_get_help_and_provide_feedback_notification_button(self):
        return self.driver.click("get_help_and_provide_feedback_notification_button", raise_e=False)

    def verify_add_device_notification_alert_message_title(self):
        return self.driver.wait_for_object("add_device_notification_alert_message_title", raise_e=False).text
    
    def verify_add_device_notification_alert_message1(self):
        return self.driver.wait_for_object("add_device_notification_alert_message1", raise_e=False).text
    
    def verify_add_device_notification_alert_message2(self):
        return self.driver.wait_for_object("add_device_notification_alert_message2", raise_e=False).text
    
    def verify_add_device_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("add_device_notification_alert_message_close_button", raise_e=False)
    
    def click_add_device_notification_alert_message_close_button(self):
        return self.driver.click("add_device_notification_alert_message_close_button", raise_e=False)

    def verify_add_device_notification_alert_message_popup(self):
        return self.driver.wait_for_object("add_device_notification_alert_message_popup", raise_e=False)

    def verify_invite_team_notification_alert_message_title(self):
        return self.driver.wait_for_object("invite_team_notification_alert_message_title", raise_e=False).text
    
    def verify_invite_team_notification_alert_message1(self):
        return self.driver.wait_for_object("invite_team_notification_alert_message1", raise_e=False).text
    
    def verify_invite_team_notification_alert_message2(self):
        return self.driver.wait_for_object("invite_team_notification_alert_message2", raise_e=False).text
    
    def verify_invite_team_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("invite_team_notification_alert_message_close_button", raise_e=False)
    
    def click_invite_team_notification_alert_message_close_button(self):
        return self.driver.click("invite_team_notification_alert_message_close_button", raise_e=False)
    
    def verify_invite_team_notification_alert_message_popup(self):
        return self.driver.wait_for_object("invite_team_notification_alert_message_popup", raise_e=False)

    def verify_complete_your_profile_notification_alert_message_title(self):
        return self.driver.wait_for_object("complete_your_profile_notification_alert_message_title", raise_e=False).text
    
    def verify_complete_your_profile_notification_alert_message(self):
        return self.driver.wait_for_object("complete_your_profile_notification_alert_message", raise_e=False).text
    
    def verify_complete_your_profile_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("complete_your_profile_notification_alert_message_close_button", raise_e=False)
    
    def click_complete_your_profile_notification_alert_message_close_button(self):
        return self.driver.click("complete_your_profile_notification_alert_message_close_button", raise_e=False)
    
    def verify_complete_your_profile_notification_alert_message_popup(self):
        return self.driver.wait_for_object("complete_your_profile_notification_alert_message_popup", raise_e=False)
    
    def verify_explore_integrations_notification_alert_message_title(self):
        return self.driver.wait_for_object("explore_integrations_notification_alert_message_title").text
    
    def verify_explore_integrations_notification_alert_message1(self):
        return self.driver.wait_for_object("explore_integrations_notification_alert_message1", raise_e=False).text
    
    def verify_explore_integrations_notification_alert_message2(self):
        return self.driver.wait_for_object("explore_integrations_notification_alert_message2", raise_e=False).text
    
    def verify_explore_integrations_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("explore_integrations_notification_alert_message_close_button", raise_e=False)
    
    def click_explore_integrations_notification_alert_message_close_button(self):
        return self.driver.click("explore_integrations_notification_alert_message_close_button", raise_e=False)
    
    def verify_explore_integrations_notification_alert_message_popup(self):
        return self.driver.wait_for_object("explore_integrations_notification_alert_message_popup", raise_e=False)

    def verify_improve_experience_score_notification_alert_message_title(self):
        return self.driver.wait_for_object("improve_experience_score_notification_alert_message_title", raise_e=False).text
    
    def verify_improve_experience_score_notification_alert_message1(self):
        return self.driver.wait_for_object("improve_experience_score_notification_alert_message1", raise_e=False).text
    
    def verify_improve_experience_score_notification_alert_message2(self):
        return self.driver.wait_for_object("improve_experience_score_notification_alert_message2", raise_e=False).text
    
    def verify_improve_experience_score_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("improve_experience_score_notification_alert_message_close_button", raise_e=False)
    
    def click_improve_experience_score_notification_alert_message_close_button(self):
        return self.driver.click("improve_experience_score_notification_alert_message_close_button", raise_e=False)
    
    def verify_improve_experience_score_notification_alert_message_popup(self):
        return self.driver.wait_for_object("improve_experience_score_notification_alert_message_popup", raise_e=False)
    
    def verify_gather_employee_feedback_notification_alert_message_title(self):
        return self.driver.wait_for_object("gather_employee_feedback_notification_alert_message_title", raise_e=False).text
    
    def verify_gather_employee_feedback_notification_alert_message1(self):
        return self.driver.wait_for_object("gather_employee_feedback_notification_alert_message1", raise_e=False).text
    
    def verify_gather_employee_feedback_notification_alert_message2(self):
        return self.driver.wait_for_object("gather_employee_feedback_notification_alert_message2", raise_e=False).text
    
    def verify_gather_employee_feedback_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("gather_employee_feedback_notification_alert_message_close_button", raise_e=False)
    
    def click_gather_employee_feedback_notification_alert_message_close_button(self):
        return self.driver.click("gather_employee_feedback_notification_alert_message_close_button", raise_e=False)
    
    def verify_gather_employee_feedback_notification_alert_message_popup(self):
        return self.driver.wait_for_object("gather_employee_feedback_notification_alert_message_popup", raise_e=False)

    def verify_get_help_and_provide_feedback_notification_alert_message_title(self):
        return self.driver.wait_for_object("get_help_and_provide_feedback_notification_alert_message_title", raise_e=False).text
    
    def verify_get_help_and_provide_feedback_notification_alert_message1(self):
        return self.driver.wait_for_object("get_help_and_provide_feedback_notification_alert_message1", raise_e=False).text
    
    def verify_get_help_and_provide_feedback_notification_alert_message2(self):
        return self.driver.wait_for_object("get_help_and_provide_feedback_notification_alert_message2", raise_e=False).text
    
    def click_stay_up_to_date_alerts_button(self):
        return self.driver.click("stay_up_to_date_alerts_button", raise_e=False)
    
    def verify_stay_up_to_date_alerts_notification_alert_message_title(self):
        return self.driver.wait_for_object("stay_up_to_date_alerts_notification_alert_message_title", raise_e=False).text
    
    def verify_stay_up_to_date_alerts_notification_alert_message1(self):
        return self.driver.wait_for_object("stay_up_to_date_alerts_notification_alert_message1", raise_e=False).text
    
    def verify_stay_up_to_date_alerts_notification_alert_message2(self):
        return self.driver.wait_for_object("stay_up_to_date_alerts_notification_alert_message2", raise_e=False).text
    
    def verify_stay_up_to_date_alerts_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("stay_up_to_date_alerts_notification_alert_message_close_button", raise_e=False)
    
    def click_stay_up_to_date_alerts_notification_alert_message_close_button(self):
        return self.driver.click("stay_up_to_date_alerts_notification_alert_message_close_button", timeout=30, raise_e=False)

    def verify_stay_up_to_date_alerts_notification_alert_message_popup(self):
        return self.driver.wait_for_object("stay_up_to_date_alerts_notification_alert_message_popup", raise_e=False)

    def click_troubleshoot_device_issues_button(self):
        return self.driver.click("troubleshoot_device_issues_button", raise_e=False, timeout=20)
    
    def verify_troubleshoot_device_issues_notification_alert_message_title(self):
        return self.driver.wait_for_object("troubleshoot_device_issues_notification_alert_message_title", raise_e=False).text
    
    def verify_troubleshoot_device_issues_notification_alert_message1(self):
        return self.driver.wait_for_object("troubleshoot_device_issues_notification_alert_message1", raise_e=False).text
    
    def verify_troubleshoot_device_issues_notification_alert_message2(self):
        return self.driver.wait_for_object("troubleshoot_device_issues_notification_alert_message2", raise_e=False).text
    
    def verify_troubleshoot_device_issues_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("troubleshoot_device_issues_notification_alert_message_close_button", raise_e=False)
    
    def click_troubleshoot_device_issues_notification_alert_message_close_button(self):
        return self.driver.click("troubleshoot_device_issues_notification_alert_message_close_button", timeout=20)

    def verify_troubleshoot_device_issues_notification_alert_message_popup(self):
        return self.driver.wait_for_object("troubleshoot_device_issues_notification_alert_message_popup", raise_e=False)

    def click_add_a_script_button(self):
        return self.driver.click("add_a_script_button", raise_e=False, timeout=20)
    
    def verify_add_a_script_notification_alert_message_title(self):
        return self.driver.wait_for_object("add_a_script_notification_alert_message_title", raise_e=False).text
    
    def verify_add_a_script_notification_alert_message1(self):
        return self.driver.wait_for_object("add_a_script_notification_alert_message1", raise_e=False).text
    
    def verify_add_a_script_notification_alert_message2(self):
        return self.driver.wait_for_object("add_a_script_notification_alert_message2", raise_e=False).text
    
    def verify_add_a_script_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("add_a_script_notification_alert_message_close_button", raise_e=False)
    
    def click_add_a_script_notification_alert_message_close_button(self):
        return self.driver.click("add_a_script_notification_alert_message_close_button", raise_e=False)
    
    def verify_add_a_script_notification_alert_message_popup(self):
        return self.driver.wait_for_object("add_a_script_notification_alert_message_popup", raise_e=False)
    
    def click_understand_workforce_sentiment_notification_button(self):
        return self.driver.click("understand_workforce_sentiment_notification_button", raise_e=False, timeout=20)
    
    def verify_understand_workforce_sentiment_notification_alert_message_title(self):
        return self.driver.wait_for_object("understand_workforce_sentiment_notification_alert_message_title", raise_e=False).text
    
    def verify_understand_workforce_sentiment_notification_alert_message1(self):
        return self.driver.wait_for_object("understand_workforce_sentiment_notification_alert_message1", raise_e=False).text
    
    def verify_understand_workforce_sentiment_notification_alert_message2(self):
        return self.driver.wait_for_object("understand_workforce_sentiment_notification_alert_message2", raise_e=False).text
    
    def verify_understand_workforce_sentiment_notification_alert_message_close_button(self):
        return self.driver.wait_for_object("understand_workforce_sentiment_notification_alert_message_close_button", raise_e=False)

    def click_understand_workforce_sentiment_notification_alert_message_close_button(self):
        return self.driver.click("understand_workforce_sentiment_notification_alert_message_close_button", raise_e=False)
    
    def verify_understand_workforce_sentiment_notification_alert_message_popup(self):
        return self.driver.wait_for_object("understand_workforce_sentiment_notification_alert_message_popup", raise_e=False)

    ############################################## Notifications Center ##############################################

    def verify_notification_bell_button(self):
        return self.driver.wait_for_object("notification_bell_button", raise_e=False, timeout=20)
    
    def click_notification_center_bell_button(self):
        return self.driver.click("notification_bell_button", raise_e=False, timeout=20)
    
    def verify_notifications_center_popup(self):
        return self.driver.wait_for_object("notifications_center_popup", raise_e=False, timeout=20)
    
    def get_notification_center_popup_title(self):
        return self.driver.wait_for_object("notifications_center_popup_title", raise_e=False, timeout=20).text
    
    def verify_notification_center_alerts_section(self):
        return self.driver.wait_for_object("notifications_center_alerts_section", raise_e=False, timeout=20)
    
    def verify_notification_center_notifications_section(self):
        return self.driver.wait_for_object("notifications_center_notifications_section", raise_e=False, timeout=20)

    def click_notification_center_notifications_section(self):
        return self.driver.click("notifications_center_notifications_section", raise_e=False, timeout=20)

    def verify_notification_center_alerts_message(self):
        return self.driver.wait_for_object("notifications_center_alerts_message", raise_e=False, timeout=20)
    
    def verify_notification_center_notifications_message(self):
        return self.driver.wait_for_object("notifications_center_notifications_message", raise_e=False, timeout=20)