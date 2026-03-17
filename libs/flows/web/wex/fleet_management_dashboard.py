from MobileApps.libs.flows.web.wex.wex_flow import WEXFlow
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import logging

class UnexpectedItemPresentException(Exception):
    pass

class Dashboard(WEXFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for wex
    """
    flow_name = "fleet_management_dashboard"
 
    ############################ Main Menu verifys ############################
 
    def verify_printer_inventory_card(self, displayed=True):
        return self.driver.wait_for_object("printer_inventory_card", invisible=not displayed, timeout=30)
   
    def verify_printer_inventory_card_title(self):
        return self.driver.wait_for_object("printer_inventory_card_title")
   
    def verify_printer_inventory_card_graph_chart(self):
        try:
            return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_inventory_card_graph_chart", timeout=30))
        except (NoSuchElementException, TimeoutException):
            print("Printer Inventory graph chart not present")
            return False
   
    def verify_printer_inventory_card_online_button(self):
        return self.driver.wait_for_object("printer_inventory_card_online_button")
   
    def verify_printer_inventory_card_offline_button(self):
        return self.driver.wait_for_object("printer_inventory_card_offline_button")

    def verify_printer_inventory_card_online_button_label(self):
        online_button_label = self.driver.get_text("printer_inventory_card_online_button")
        if "Online" in online_button_label:
            return True
        else:
            print(f"Expected label 'Online', but got '{online_button_label}'")
            return False

    def verify_printer_inventory_card_offline_button_label(self):
        offline_button_label = self.driver.get_text("printer_inventory_card_offline_button")
        if "Offline" in offline_button_label:
            return True
        else:
            print(f"Expected label 'Offline', but got '{offline_button_label}'")
            return False
 
    def click_printer_inventory_card_online_button(self):
        return self.driver.click("printer_inventory_card_online_button")
   
    def click_printer_inventory_card_offline_button(self):
        return self.driver.click("printer_inventory_card_offline_button")
    
    def verify_printer_inventory_card_is_empty(self):
        return self.driver.wait_for_object("printer_inventory_card_empty")

    def verify_no_data_display_message(self):
        return self.driver.wait_for_object("no_data_display_message")

    def verify_printer_inventory_card_printers_count(self):
        return self.driver.wait_for_object("printer_inventory_card_printers_count")
    
    def verify_printer_inventory_card_printers_count_label(self):
        return self.driver.verify_object_string("printer_inventory_card_printers_count_label")
    
    def verify_printer_inventory_card_online_button_count(self):
        return self.driver.wait_for_object("printer_inventory_card_online_button_count")
    
    def verify_printer_inventory_card_offline_button_count(self):
        return self.driver.wait_for_object("printer_inventory_card_offline_button_count")

    def verify_printer_inventory_card_online_button_is_enabled(self):
        online_button = self.driver.wait_for_object("printer_inventory_card_online_button_enabled", raise_e=False)
        if online_button:
            return online_button.is_enabled()
        else:
            print("Online button is disabled")
            self.driver.wait_for_object("printer_inventory_card_online_button_disabled", timeout=30)
            return False
    
    def verify_printer_inventory_card_offline_button_is_enabled(self):
        offline_button = self.driver.wait_for_object("printer_inventory_card_offline_button_enabled", raise_e=False)
        if offline_button:
            return offline_button.is_enabled()
        else:
            print("Offline button is disabled")
            self.driver.wait_for_object("printer_inventory_card_offline_button_disabled", timeout=30)
            return False

    def get_printer_inventory_card_printers_count(self):
        return self.driver.get_text("printer_inventory_card_printers_count")
    
    def get_printer_inventory_card_online_button_count(self):
        self.verify_printer_inventory_card_online_button()
        online_button_label = self.driver.get_text("printer_inventory_card_online_button_count")
        count = online_button_label.split()[0]
        return int(count)
    
    def get_printer_inventory_card_offline_button_count(self):
        self.verify_printer_inventory_card_offline_button()
        offline_button_label = self.driver.get_text("printer_inventory_card_offline_button_count")
        count = offline_button_label.split()[0]
        return int(count)

    def verify_printer_inventory_card_more_options_button(self):
        return self.driver.wait_for_object("printer_inventory_card_more_options_button", timeout=30)
    
    def click_printer_inventory_card_more_options_button(self):
        return self.driver.click("printer_inventory_card_more_options_button", timeout=30)
    
    def get_printer_inventory_card_more_options_list_items(self):
        options = self.driver.find_object("printer_inventory_card_more_options_list_items", multiple=True)
        return [option.text for option in options]

    def verify_printer_fleet_security_widget(self, displayed=True):
        return self.driver.wait_for_object("printer_fleet_security_widget",invisible=not displayed, timeout=30)
    
    def verify_printer_fleet_security_widget_title(self):
        return self.driver.verify_object_string("printer_fleet_security_widget_title")
    
    def verify_printer_fleet_security_widget_view_details_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_fleet_security_widget_view_details_button", timeout=60))
        return self.driver.wait_for_object("printer_fleet_security_widget_view_details_button")
    
    def verify_printer_fleet_security_widget_badge_title(self):
        return self.driver.verify_object_string("printer_fleet_security_widget_badge_title", timeout=30)
    
    def verify_printer_fleet_security_widget_badge_subtitle(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_badge_subtitle")

    def get_printer_fleet_security_widget_badge_subtitle_status(self):
        return self.driver.get_text("printer_fleet_security_widget_badge_subtitle")
    
    def verify_printer_fleet_security_widget_badge_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_badge_icon")
    
    def verify_printer_fleet_security_widget_high_risk_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_security_widget_high_risk_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False

    def verify_printer_fleet_security_widget_medium_risk_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_security_widget_medium_risk_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False

    def verify_printer_fleet_security_widget_not_assessed_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_security_widget_not_assessed_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False
    
    def verify_printer_fleet_security_widget_low_risk_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_security_widget_low_risk_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False

    def verify_printer_fleet_security_widget_passed_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_security_widget_passed_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False

    def verify_printer_fleet_security_widget_high_risk_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_high_risk_status_button_count")

    def verify_printer_fleet_security_widget_medium_risk_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_medium_risk_status_button_count")

    def verify_printer_fleet_security_widget_not_assessed_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_not_assessed_status_button_count")

    def verify_printer_fleet_security_widget_low_risk_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_low_risk_status_button_count")

    def verify_printer_fleet_security_widget_passed_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_passed_status_button_count")    
    
    def verify_printer_fleet_security_widget_high_risk_status_navigation_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_high_risk_status_navigation_icon")
    
    def verify_printer_fleet_security_widget_medium_risk_status_navigation_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_medium_risk_status_navigation_icon")
    
    def verify_printer_fleet_security_widget_not_assessed_status_navigation_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_not_assessed_status_navigation_icon")
    
    def verify_printer_fleet_security_widget_low_risk_status_navigation_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_low_risk_status_navigation_icon")
    
    def verify_printer_fleet_security_widget_passed_status_navigation_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_passed_status_navigation_icon")
    
    def click_printer_fleet_security_widget_view_details_button(self):
        return self.driver.click("printer_fleet_security_widget_view_details_button",timeout=30)
    
    def get_printer_fleet_security_widget_high_risk_status_button_count(self):
        return int(self.driver.get_text("printer_fleet_security_widget_high_risk_status_button_count"))

    def click_printer_fleet_security_widget_high_risk_status_button(self):
        return self.driver.click("printer_fleet_security_widget_high_risk_status_button")
    
    def get_printer_fleet_security_widget_medium_risk_status_button_count(self):
        return int(self.driver.get_text("printer_fleet_security_widget_medium_risk_status_button_count"))
    
    def click_printer_fleet_security_widget_medium_risk_status_button(self):
        return self.driver.click("printer_fleet_security_widget_medium_risk_status_button")
   
    def get_printer_fleet_security_widget_not_assessed_status_button_count(self):
        return int(self.driver.get_text("printer_fleet_security_widget_not_assessed_status_button_count"))
    
    def click_printer_fleet_security_widget_not_assessed_status_button(self):
        return self.driver.click("printer_fleet_security_widget_not_assessed_status_button")
    
    def get_printer_fleet_security_widget_low_risk_status_button_count(self):
        return int(self.driver.get_text("printer_fleet_security_widget_low_risk_status_button_count"))
    
    def click_printer_fleet_security_widget_low_risk_status_button(self):
        return self.driver.click("printer_fleet_security_widget_low_risk_status_button")
    
    def get_printer_fleet_security_widget_passed_status_button_count(self):
        return int(self.driver.get_text("printer_fleet_security_widget_passed_status_button_count"))
    
    def click_printer_fleet_security_widget_passed_status_button(self):
        return self.driver.click("printer_fleet_security_widget_passed_status_button")

    def get_printer_fleet_security_widget_status_buttons(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_fleet_security_widget_status_buttons", timeout=30))
        options = self.driver.find_object("printer_fleet_security_widget_status_buttons", multiple=True)
        return [option.text for option in options]

    def get_printer_fleet_security_widget_status_button_count(self, status):
        count_text = self.driver.get_text("printer_fleet_security_widget_{}_status_button_count".format(status.lower().replace(" ", "_")))
        # Split the string and get the first part
        count = int(count_text.split()[0])
        return count

    def click_printer_fleet_security_widget_status_button(self, status):
        return self.driver.click("printer_fleet_security_widget_{}_status_button".format(status.lower().replace(" ", "_")))

    def verify_printer_fleet_security_widget_information_icon(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_information_icon")
    
    def click_printer_fleet_security_widget_information_icon(self):
        self.driver.wait_for_object("printer_fleet_security_widget_information_icon", timeout=30)
        return self.driver.click("printer_fleet_security_widget_information_icon",timeout=30)

    def verify_printer_fleet_security_widget_more_options_button(self):
        self.driver.wait_for_object("printer_fleet_security_widget_more_options_button", timeout=30)

    def click_printer_fleet_security_widget_more_options_button(self):
        self.driver.click("printer_fleet_security_widget_more_options_button", timeout=30)
    
    def click_printer_fleet_security_widget_about_this_widget_button(self):
        self.driver.click("printer_fleet_security_widget_about_this_widget_button", timeout=30)

    def verify_hp_secure_fleet_manager_status_information_modal(self):
        return self.driver.wait_for_object("hp_secure_fleet_manager_status_information_modal",timeout=30)
    
    def verify_hp_secure_fleet_manager_status_information_modal_title(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_title")
    
    def verify_hp_secure_fleet_manager_status_information_modal_description(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_description",timeout=30)
    
    def verify_hp_secure_fleet_manager_status_information_modal_status_description(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_status_description")
    
    def verify_hp_secure_fleet_manager_status_information_modal_high_risk_status_description(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_high_risk_status_description")
    
    def verify_hp_secure_fleet_manager_status_information_modal_medium_risk_status_description(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_medium_risk_status_description")
    
    def verify_hp_secure_fleet_manager_status_information_modal_low_risk_status_description(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_low_risk_status_description")
    
    def verify_hp_secure_fleet_manager_status_information_modal_compliant_status_description(self):
        return self.driver.verify_object_string("hp_secure_fleet_manager_status_information_modal_compliant_status_description")

    def verify_hp_secure_fleet_manager_status_information_modal_close_button(self):
        return self.driver.wait_for_object("hp_secure_fleet_manager_status_information_modal_close_button")
    
    def click_hp_secure_fleet_manager_status_information_modal_close_button(self):
        return self.driver.click("hp_secure_fleet_manager_status_information_modal_close_button")
    
    def verify_hp_secure_fleet_manager_status_information_modal_not_displayed(self):
        return self.driver.wait_for_object("hp_secure_fleet_manager_status_information_modal", timeout=10,invisible=True)

    def verify_printer_fleet_security_widget_more_options_button(self):
        return self.driver.wait_for_object("printer_fleet_security_widget_more_options_button", timeout=30)
    
    def click_printer_fleet_security_widget_more_options_button(self):
        return self.driver.click("printer_fleet_security_widget_more_options_button", timeout=30)
    
    def get_printer_fleet_security_widget_more_options_list_items(self):
        options = self.driver.find_object("printer_fleet_security_widget_more_options_list_items", multiple=True)
        return [option.text for option in options]
    
    ##########################Fleet Management Dashboard - Printer Fleet Compliance Widget ##########################

    def verify_printer_fleet_compliance_widget(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_fleet_compliance_widget", timeout=30))
        return self.driver.wait_for_object("printer_fleet_compliance_widget",timeout=30)
    
    def verify_printer_fleet_compliance_widget_is_displayed(self, displayed=True):
        return self.driver.wait_for_object("printer_fleet_compliance_widget", invisible=not displayed, timeout=30)

    def verify_printer_fleet_compliance_widget_title(self):
        return self.driver.verify_object_string("printer_fleet_compliance_widget_title")
    
    def verify_printer_fleet_compliance_widget_view_details_button(self):
        return self.driver.verify_object_string("printer_fleet_compliance_widget_view_details_button")
    
    def click_printer_fleet_compliance_widget_view_details_button(self):
        return self.driver.click("printer_fleet_compliance_widget_view_details_button", timeout=30)
    
    def verify_printer_fleet_compliance_widget_graph_chart(self):
        try:
            return self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_fleet_compliance_widget_graph_chart", timeout=30))
        except (NoSuchElementException, TimeoutException):
            print("Printer Fleet Compliance graph chart not present")
            return False
        
    def verify_printer_fleet_compliance_widget_graph_chart_printers_count(self):
        return self.driver.wait_for_object("printer_fleet_compliance_widget_graph_chart_printers_count")
    
    def verify_printer_fleet_compliance_widget_graph_chart_printers_count_label(self):
        return self.driver.verify_object_string("printer_fleet_compliance_widget_graph_chart_printers_count_label")
        
    def verify_printer_fleet_compliance_widget_compliance_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_compliance_widget_compliance_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False
    
    def verify_printer_fleet_compliance_widget_compliance_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_compliance_widget_compliance_status_button_count")
    
    def verify_printer_fleet_compliance_widget_compliance_status_button_is_enabled(self):
        compliant_button = self.driver.wait_for_object("printer_fleet_compliance_widget_compliance_status_button_enabled", raise_e=False)
        if compliant_button:
            return compliant_button.is_enabled()
        else:
            print("Compliant button is disabled")
            self.driver.wait_for_object("printer_fleet_compliance_widget_compliance_status_button_disabled", timeout=30)
            return False
    
    def click_printer_fleet_compliance_widget_compliance_status_button(self):
        return self.driver.click("printer_fleet_compliance_widget_compliance_status_button")
    
    def verify_printer_fleet_compliance_widget_non_compliant_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_compliance_widget_non_compliant_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False
    
    def verify_printer_fleet_compliance_widget_non_compliant_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_compliance_widget_non_compliant_status_button_count", timeout=30)
    
    def verify_printer_fleet_compliance_widget_non_compliant_status_button_is_enabled(self):
        non_compliant_button = self.driver.wait_for_object("printer_fleet_compliance_widget_non_compliant_status_button_enabled", raise_e=False)
        if non_compliant_button:
            return non_compliant_button.is_enabled()
        else:
            print("Non Compliant button is disabled")
            self.driver.wait_for_object("printer_fleet_compliance_widget_non_compliant_status_button_disabled", timeout=30)
            return False
    
    def click_printer_fleet_compliance_widget_non_compliant_status_button(self):
        return self.driver.click("printer_fleet_compliance_widget_non_compliant_status_button",timeout=30)
    
    def verify_printer_fleet_compliance_widget_not_assessed_status_button(self):
        button = self.driver.wait_for_object("printer_fleet_compliance_widget_not_assessed_status_button", raise_e=False)
        if button:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            return True
        return False
    
    def verify_printer_fleet_compliance_widget_not_assessed_status_button_count(self):
        return self.driver.wait_for_object("printer_fleet_compliance_widget_not_assessed_status_button_count", timeout=30)
    
    def verify_printer_fleet_compliance_widget_not_assessed_status_button_is_enabled(self):
        compliant_button = self.driver.wait_for_object("printer_fleet_compliance_widget_not_assessed_status_button_enabled", raise_e=False)
        if compliant_button:
            return compliant_button.is_enabled()
        else:
            print("Not Assessed button is disabled")
            self.driver.wait_for_object("printer_fleet_compliance_widget_not_assessed_status_button_disabled", timeout=30)
            return False
    
    def click_printer_fleet_compliance_widget_not_assessed_status_button(self):
        return self.driver.click("printer_fleet_compliance_widget_not_assessed_status_button")

    def verify_printer_fleet_compliance_widget_compliance_status_button_label(self):
        compliant_button_label = self.driver.get_text("printer_fleet_compliance_widget_compliance_status_button")
        if "Compliant" in compliant_button_label:
            return True
        else:
            print(f"Expected label 'Compliant', but got '{compliant_button_label}'")
            return False
    
    def verify_printer_fleet_compliance_widget_non_compliant_status_button_label(self):
        non_compliant_button_label = self.driver.get_text("printer_fleet_compliance_widget_non_compliant_status_button")
        if "Noncompliant" in non_compliant_button_label:
            return True
        else:
            print(f"Expected label 'Non Compliant', but got '{non_compliant_button_label}'")
            return False
    
    def verify_printer_fleet_compliance_widget_not_assessed_status_button_label(self):
        not_assessed_button_label = self.driver.get_text("printer_fleet_compliance_widget_not_assessed_status_button")
        if "Not assessed" in not_assessed_button_label:
            return True
        else:
            print(f"Expected label 'Not Assessed', but got '{not_assessed_button_label}'")
            return False
    
    def get_printer_fleet_compliance_widget_graph_chart_printers_count(self):
        return self.driver.get_text("printer_fleet_compliance_widget_graph_chart_printers_count")
    
    def get_printer_fleet_compliance_widget_compliance_status_button_count(self):
        self.verify_printer_fleet_compliance_widget_compliance_status_button()
        compliant_button_label = self.driver.get_text("printer_fleet_compliance_widget_compliance_status_button_count")
        count = compliant_button_label.split()[0]
        return int(count)

    def get_printer_fleet_compliance_widget_non_compliant_status_button_count(self):
        self.verify_printer_fleet_compliance_widget_non_compliant_status_button()
        non_compliant_button_label = self.driver.get_text("printer_fleet_compliance_widget_non_compliant_status_button_count")
        count = non_compliant_button_label.split()[0]
        return int(count)
        
    def get_printer_fleet_compliance_widget_not_assessed_status_button_count(self):
        self.verify_printer_fleet_compliance_widget_not_assessed_status_button()
        not_assessed_button_label = self.driver.get_text("printer_fleet_compliance_widget_not_assessed_status_button_count")
        count = not_assessed_button_label.split()[0]
        return int(count)
        
    def verify_printer_fleet_compliance_widget_more_options_button(self):
        return self.driver.wait_for_object("printer_fleet_compliance_widget_more_options_button", timeout=30)
    
    def click_printer_fleet_compliance_widget_more_options_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.wait_for_object("printer_fleet_compliance_widget_more_options_button", timeout=30))
        return self.driver.click("printer_fleet_compliance_widget_more_options_button", timeout=30)
    
    def get_printer_fleet_compliance_widget_more_options_list_items(self):
        options = self.driver.find_object("printer_fleet_compliance_widget_more_options_list_items", multiple=True)
        return [option.text for option in options]
    
    ################################Analytics - New Dashboard#################################

    def get_analytics_dashboards_page_breadcrumb(self):
        return self.driver.wait_for_object("analytics_dashboards_page_breadcrumb", raise_e=False).text
    
    def get_analytics_dashboards_page_header(self):
        return self.driver.wait_for_object("analytics_dashboards_page_header", raise_e=False).text
    
    def verify_analytics_dashboards_new_dashboard_button(self):
        return self.driver.wait_for_object("analytics_new_dashboard_button", raise_e=False)
    
    def verify_analytics_dashboards_experience_score_dashboard_button(self):
        return self.driver.wait_for_object("analytics_experience_score_dashboard_button", raise_e=False)
    
    def verify_analytics_dashboards_fleet_management_dashboard_button(self):
        return self.driver.wait_for_object("analytics_fleet_management_dashboard_button", raise_e=False)
    
    def verify_analytics_dashboards_employee_engagement_dashboard_button(self):
        return self.driver.wait_for_object("analytics_employee_engagement_dashboard_button", raise_e=False)
    
    def verify_analytics_dashboards_hardware_support_dashboard_button(self):
        return self.driver.wait_for_object("analytics_hardware_support_dashboard_button", raise_e=False)

    def click_analytics_new_dashboard_button(self):
        return self.driver.click("analytics_new_dashboard_button")
    
    def click_new_dashboard_print_widget_from_select_widgets(self):
        return self.driver.click("analytics_print_widget", timeout=30)

    def select_printer_fleet_compliance_widget(self):
        return self.driver.click("analytics_print_printer_fleet_compliance_widgets")
    
    def select_printer_fleet_security_widget(self):
        return self.driver.click("analytics_print_printer_fleet_security")
    
    def select_printer_inventory_widget(self):
        return self.driver.click("analytics_print_printer_inventory")

    def select_printer_management_widget(self):
        return self.driver.click("analytics_print_printer_management")
    
    def click_new_dashboard_pc_widget_from_select_widgets(self):
        return self.driver.click("analytics_pc_widget", timeout=40)

    def select_fleet_inventory_widget(self):
        return self.driver.click("analytics_fleet_inventory_widget")
    
    def verify_analytics_new_dashboard_created_toast_message(self):
        return self.driver.wait_for_object("analytics_dashboard_created_pop_up_message")
    
    def verify_compliance_security_inventory_widgets(self):
        self.driver.wait_for_object("analytics_print_printer_fleet_compliance_widgets")
        self.driver.wait_for_object("analytics_print_printer_fleet_security")
        return self.driver.wait_for_object("analytics_print_printer_inventory")
    
    def click_analytics_new_dashboard_edit_btn(self):
        return self.driver.click("analytics_edit_btn")

    def edit_analytics_new_dashboard_name(self, analytics_dashboard_name):
        self.driver.click("analytics_dashboard_name_input")
        sleep(3)
        self.driver.js_clear_text("analytics_dashboard_name_input")
        sleep(2)
        return self.driver.send_keys("analytics_dashboard_name_input", analytics_dashboard_name)
 
    def send_analytics_dashboard_name(self,analytics_dashboard_name):
        return self.driver.send_keys("analytics_dashboard_name_input",analytics_dashboard_name)
    
    def verify_new_dashboard_created_pop_up_message(self):
        return self.driver.wait_for_object("analytics_dashboard_created_pop_up_message")
    
    def verify_analytics_newly_created_dashboard(self,analytic_new_dashboard_name, displayed=True):
        return self.driver.wait_for_object("created_analytic_dashboard",format_specifier =[analytic_new_dashboard_name], invisible=not displayed, timeout=30)
    
    def select_analytics_new_dashboard_widgets_create_btn(self):
        return self.driver.click("analytics_widgets_create_btn")
    
    def click_analytics_new_dashboard_save_btn(self):
        return self.driver.click("analytics_dashboard_save_btn")
    
    def click_created_analytic_dashboard(self,analytic_new_dashboard_name):
        return self.driver.click("created_analytic_dashboard",format_specifier =[analytic_new_dashboard_name])
    
    def click_created_dashboard_export_btn(self):
        return self.driver.click("created_dashboard_export_btn", timeout=30)
    
    def click_created_dashboard_export_xlsx_btn(self):
        return self.driver.click("created_dashboard_export_xlsx_btn")
 
    def verify_xlsx_file_downloaded_popup_msg(self):
        return self.driver.wait_for_object("xlsx_file_downloaded_popup_msg",timeout=20)
 
    def click_analytic_dashboard_expand_btn(self):
        return self.driver.click("analytic_dashboard_expand_btn",timeout=30)
    
    def click_analytic_dashboard_delete_dashboard_btn(self):
        return self.driver.click("analytic_dashboard_delete_dashboard_btn")
    
    def click_analytic_dashboard_delete_btn(self):
        return self.driver.click("analytic_dashboard_delete_btn",timeout=30)
    
    def verify_analytic_dashboard_deleted_popup_msg(self):
        return self.driver.wait_for_object("analytic_dashboard_deleted_popup_msg")
    
    def click_analytic_dashboard_duplicate_dashboard_btn(self):
        return self.driver.click("analytic_dashboard_duplicate_dashboard_btn")
    
    def verify_analytic_dashboard_duplicate_popup_msg(self):
        return self.driver.wait_for_object("analytic_dashboard_duplicate_popup_msg")
    
    def verify_analytic_dashboard_copy_analytic_dashboard_name(self,analytic_new_dashboard_name):
        return self.driver.wait_for_object("analytic_dashboard_copy_analytic_dashboard_name",format_specifier =[analytic_new_dashboard_name])
 
    def verify_analytic_dashboard_created_copy_analytic_dashboard(self,analytic_new_dashboard_name):
        self.driver.wait_for_object("analytic_dashboard_copy_analytic_dashboard",format_specifier =[analytic_new_dashboard_name], timeout=30)
        return self.driver.find_object("analytic_dashboard_copy_analytic_dashboard",format_specifier =[analytic_new_dashboard_name])
    
    def click_analytic_dashboard_created_copy_analytic_dashboard(self,analytic_new_dashboard_name):
        return self.driver.click("analytic_dashboard_copy_analytic_dashboard",format_specifier =[analytic_new_dashboard_name])
    
    def click_analytic_dashboard_edit_dashboard_btn(self):
        return self.driver.click("analytic_dashboard_edit_dashboard_btn")
 
    def select_compliance_security_inventory_save_btn(self):
        return self.driver.click("analytics_save_btn")
    
    def verify_analytic_dashboard_dashboard_updated_popup_msg(self):
        return self.driver.wait_for_object("analytic_dashboard_dashboard_updated_popup_msg")

    ##########################Analytics - Fleet Management Dashboard#########################

    def click_analytics_fleet_management_dashboard_button(self):
        return self.driver.click("analytics_fleet_management_dashboard_button")
    
    def get_analytics_fleet_management_dashboard_page_breadcrumb(self):
        return self.driver.wait_for_object("fleet_management_dashboard_page_breadcrumb", raise_e=False).text
    
    def get_analytics_fleet_management_dashboard_page_title(self):
        return self.driver.wait_for_object("fleet_management_dashboard_page_title", raise_e=False).text
    
    def click_analytics_fleet_management_dashboard_print_widget_from_select_widgets(self):
        return self.driver.click("fleet_management_dashboard_print_widget")
    
    def select_printer_management_from_select_widgets(self):
        return self.driver.click("analytics_print_printer_management")
    
    def click_analytics_fleet_management_dashboard_pc_widget_from_select_widgets(self):
        return self.driver.click("fleet_management_dashboard_pc_widget",timeout=20)
    
    def click_select_widgets_save_btn(self):
        return self.driver.click("fleet_management_dashboard_select_widgets_save_btn")

    def verify_printer_management_widget_is_displayed(self, displayed=True):
        return self.driver.wait_for_object("fleet_management_dashboard_printer_management_widget", invisible=not displayed, timeout=30)
    
    def verify_fleet_inventory_widget_is_displayed(self, displayed=True):
        return self.driver.wait_for_object("fleet_management_dashboard_fleet_inventory_widget", invisible=not displayed, timeout=30)

    def click_modern_reports_tab(self):
        return self.driver.click("analytics_modern_reports_tab",timeout=30)

    def verify_modern_reports_tab(self):
        return self.driver.wait_for_object("analytics_modern_reports_tab",timeout=20, raise_e=False)
    
    def verify_windows_11_readiness_assessment_report(self):
        return self.driver.wait_for_object("analytics_windows_11_readiness_assessment_report",raise_e=False, timeout=30)

    def verify_application_experience_report(self):
        return self.driver.wait_for_object("analytics_application_experience_report", raise_e=False, timeout=30)

    def verify_application_experience_installed_app_report(self):
        return self.driver.wait_for_object("analytics_application_experience_installed_app_report", raise_e=False)

    def verify_application_experience_web_app_report(self):
        return self.driver.wait_for_object("analytics_application_experience_web_app_report", raise_e=False)
    
    def click_application_experience_installed_app_report(self):
        return self.driver.click("analytics_application_experience_installed_app_report", timeout=30)

    def click_application_experience_web_app_report(self):
        return self.driver.click("analytics_application_experience_web_app_report", timeout=30)
    
    def verify_network_health_report(self):
        return self.driver.wait_for_object("analytics_network_health_report", raise_e=False)
    
    def verify_device_utilization_report(self):
        return self.driver.wait_for_object("analytics_device_utilization_report", raise_e=False)
    
    def verify_sustainability_report(self):
        return self.driver.wait_for_object("analytics_sustainability_report", raise_e=False)
    
    def verify_bios_inventory_report(self):
        return self.driver.wait_for_object("analytics_bios_inventory_report", raise_e=False)
    
    def verify_driver_inventory_report(self):
        return self.driver.wait_for_object("analytics_driver_inventory_report", raise_e=False)
    
    def verify_hardware_inventory_report(self):
        return self.driver.wait_for_object("analytics_hardware_inventory_report", raise_e=False)
    
    def verify_application_inventory_report(self):
        return self.driver.wait_for_object("analytics_application_inventory_report", raise_e=False)

    def verify_security_report(self):
        return self.driver.wait_for_object("analytics_security_report", raise_e=False)
    
    def verify_system_health_report(self):
        return self.driver.wait_for_object("analytics_system_health_report", raise_e=False)
    
    def verify_os_performance_report(self):
        return self.driver.wait_for_object("analytics_os_performance_report", raise_e=False)
    
    def verify_blue_screen_errors_report(self):
        return self.driver.wait_for_object("analytics_blue_screen_errors_report", raise_e=False)
    
    def click_application_inventory_report(self):
        return self.driver.click("analytics_application_inventory_report",timeout=30)
    
    def click_application_experience_report(self):
        return self.driver.click("analytics_application_experience_report",timeout=30)

    def get_modern_report_breadcrumb(self):
        return self.driver.wait_for_object("analytics_modern_report_breadcrumb", raise_e=False).text
    
    def click_modern_report_expand_btn(self):
        return self.driver.click("analytics_modern_report_expand_btn",timeout=30)
    
    def verify_modern_report_duplicate_btn(self):
        return self.driver.wait_for_object("analytics_modern_report_duplicate_btn",timeout=30)
    
    def click_modern_reports_duplicate_btn(self):
        return self.driver.click("analytics_modern_report_duplicate_btn",timeout=30)
    
    def get_modern_report_duplicate_popup_msg(self):
        return self.driver.wait_for_object("analytics_modern_report_duplicate_popup_msg", raise_e=False).text
    
    def get_modern_report_duplicated_breadcrumb(self):
        sleep(3)
        return self.driver.wait_for_object("analytics_modern_report_duplicated_breadcrumb", raise_e=False,timeout=30).text
    
    def click_modern_reports_delete_report_btn(self):
        return self.driver.click("analytics_modern_report_delete_btn",timeout=30)
    
    def click_delete_reports_popup_delete_btn(self):
        self.driver.wait_for_object("analytics_delete_reports_popup_delete_btn", timeout=30)
        return self.driver.click("analytics_delete_reports_popup_delete_btn",timeout=30)
    
    def get_modern_report_deleted_popup_msg(self):
        return self.driver.wait_for_object("analytics_modern_report_deleted_popup_msg", raise_e=False).text
    
    def click_security_report(self):
        return self.driver.click("analytics_security_report",timeout=30)

    def click_system_health_report(self):
        return self.driver.click("analytics_system_health_report",timeout=30)
    
    def click_os_performance_report(self):
        return self.driver.click("analytics_os_performance_report",timeout=30)

    def click_blue_screen_errors_report(self):
        return self.driver.click("analytics_blue_screen_errors_report",timeout=30)

    def click_sustainability_report(self):
        return self.driver.click("analytics_sustainability_report",timeout=30)
    
    def click_network_health_report(self):
        return self.driver.click("analytics_network_health_report",timeout=30)

    def click_network_health_report_expand_btn(self):
        return self.driver.click("analytics_network_health_report_expand_btn",timeout=30)    
    
    def click_blue_screen_error_modern_report_expand_btn(self):
        return self.driver.click("analytics_blue_screen_error_modern_report_expand_btn",timeout=30)

    ########################################Analytics - Classic Reports#########################################

    def click_classic_reports_tab(self):
        return self.driver.js_click("analytics_classic_reports_tab")
    
    def click_first_classic_report(self):
        self.driver.wait_for_object("analytics_classic_report_first_link", timeout=40)
        return self.driver.click("analytics_classic_report_first_link",timeout=30)
    
    def verify_classic_reports_tab(self):
        return self.driver.wait_for_object("analytics_classic_reports_tab",timeout=20, raise_e=False)
    
    def get_classic_reports_tab_name(self):
        return self.driver.wait_for_object("analytics_classic_reports_tab_name", raise_e=False).text

    def verify_classic_reports_add_report_button(self):
        return self.driver.wait_for_object("classic_reports_add_report_button", raise_e=False, timeout=30)
    
    def click_classic_reports_add_report_button(self):
        return self.driver.click("classic_reports_add_report_button",timeout=30)
    
    def get_classic_reports_add_report_breadcrumb(self):
        return self.driver.wait_for_object("classic_reports_add_report_breadcrumb", raise_e=False).text
    
    def click_classic_reports_add_report_discard_btn(self):
        return self.driver.click("classic_reports_add_report_discard_btn",timeout=40)

    def click_classic_reports_analytics_breadcrumb(self):
        return self.driver.click("analytics_breadcrumb",timeout=40)
    
    def verify_classic_reports_export_report_button(self):
        return self.driver.wait_for_object("classic_reports_export_report_button", raise_e=False, timeout=30)
    
    def click_classic_reports_export_report_button(self):
        return self.driver.click("classic_reports_export_report_button",timeout=30)
    
    def verify_classic_reports_browse_tab(self):
        return self.driver.wait_for_object("classic_reports_browse_tab", raise_e=False, timeout=30)
    
    def verify_classic_reports_favorites_tab(self):
        return self.driver.wait_for_object("classic_reports_favorites_tab", raise_e=False, timeout=30)
    
    def verify_classic_reports_history_tab(self):
        return self.driver.wait_for_object("classic_reports_history_tab", raise_e=False, timeout=30)

    ########################################Analytics - Experience Score Dashboard########################################

    def click_analytics_experience_score_dashboard_button(self):
        return self.driver.click("analytics_experience_score_dashboard_button")
    
    def get_analytics_experience_score_dashboard_page_breadcrumb(self):
        return self.driver.wait_for_object("analytics_experience_score_dashboard_page_breadcrumb", raise_e=False).text
    
    def get_analytics_experience_score_dashboard_page_title(self):
        return self.driver.wait_for_object("analytics_experience_score_dashboard_page_title", raise_e=False).text

    def click_analytics_experience_score_dashboard_print_widget_from_select_widgets(self):
        return self.driver.click("experience_score_dashboard_print_widget")
    
    def click_analytics_experience_score_dashboard_pc_widget_from_select_widgets(self):
        return self.driver.click("experience_score_dashboard_pc_widget", timeout=30)

    ######################################### Analytics - Employee Engagement Dashboard #########################################

    def click_analytics_employee_engagement_dashboard_button(self):
        return self.driver.click("analytics_employee_engagement_dashboard_button")

    def get_analytics_employee_engagement_dashboard_page_breadcrumb(self):
        return self.driver.wait_for_object("analytics_employee_engagement_dashboard_page_breadcrumb", raise_e=False).text
    
    def get_analytics_employee_engagement_dashboard_page_title(self):
        return self.driver.wait_for_object("analytics_employee_engagement_dashboard_page_title", raise_e=False).text
    
    def click_analytics_employee_engagement_dashboard_pc_widget_from_select_widgets(self):
        return self.driver.click("employee_engagement_dashboard_pc_widget")