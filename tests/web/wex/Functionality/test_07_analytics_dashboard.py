import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from time import sleep
import random

new_dashboard_name= "auto_test"+str(random.randint(1,1000))
 
class Test_07_Workforce_Analytics_Dashboard(object):
 
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.policies = self.fc.fd["fleet_management_policies"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        self.home.click_sidemenu_analytics_button()
        self.home.click_analytics_fleet_management_button()
        return self.home.verify_fleet_management_breadcrumb()

    def test_01_verify_new_dashboard_functionality(self):
        #
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_analytics_new_dashboard_button()
        self.dashboard.click_new_dashboard_print_widget_from_select_widgets()

        self.dashboard.select_printer_fleet_compliance_widget()
        self.dashboard.select_printer_fleet_security_widget()
        self.dashboard.select_printer_inventory_widget()

        self.dashboard.select_analytics_new_dashboard_widgets_create_btn()
        self.dashboard.verify_analytics_new_dashboard_created_toast_message()

        assert self.dashboard.verify_printer_fleet_security_widget()
        assert self.dashboard.verify_printer_fleet_compliance_widget()
        assert self.dashboard.verify_printer_inventory_card()

        # Verify the dashboard name - Edit functionality
        self.dashboard.click_analytics_new_dashboard_edit_btn()
        self.dashboard.edit_analytics_new_dashboard_name("update_"+new_dashboard_name)
        self.dashboard.click_analytics_new_dashboard_save_btn()
        self.dashboard.verify_analytics_new_dashboard_created_toast_message()

        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytics_newly_created_dashboard("update_"+new_dashboard_name)

        #revert the name change 
        self.dashboard.click_created_analytic_dashboard("update_"+new_dashboard_name)
        self.dashboard.click_analytics_new_dashboard_edit_btn()
        self.dashboard.edit_analytics_new_dashboard_name(new_dashboard_name)
        self.dashboard.click_analytics_new_dashboard_save_btn()
        self.dashboard.verify_analytics_new_dashboard_created_toast_message()
        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytics_newly_created_dashboard(new_dashboard_name)
   
    def test_02_verify_new_dashboard_export_functionality(self):
        #
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard(new_dashboard_name)
        self.dashboard.click_created_dashboard_export_btn()
        self.dashboard.click_created_dashboard_export_xlsx_btn()
        self.dashboard.verify_xlsx_file_downloaded_popup_msg()
       
    def test_03_verify_new_dashboard_duplicate_functionality(self):
        #
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard(new_dashboard_name)
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_duplicate_dashboard_btn()
        self.dashboard.verify_analytic_dashboard_duplicate_popup_msg()
        self.dashboard.verify_analytic_dashboard_copy_analytic_dashboard_name(new_dashboard_name)

        #Verify the copied/duplicate dashboard name 
        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytic_dashboard_created_copy_analytic_dashboard(new_dashboard_name)

        #Delete the copied/duplicate dashboard
        self.dashboard.click_analytic_dashboard_created_copy_analytic_dashboard(new_dashboard_name)
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_delete_dashboard_btn()
        self.dashboard.click_analytic_dashboard_delete_btn()
        self.dashboard.verify_analytic_dashboard_deleted_popup_msg()
 
    def test_04_verify_new_dashboard_edit_functionality(self):
        #
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard(new_dashboard_name)
        self.dashboard.click_analytic_dashboard_expand_btn()

        self.dashboard.click_analytic_dashboard_edit_dashboard_btn()
        self.dashboard.click_new_dashboard_print_widget_from_select_widgets()
        #Remove the Fleet Compliance and Security widgets
        self.dashboard.select_printer_fleet_compliance_widget()
        self.dashboard.select_printer_fleet_security_widget()
        self.dashboard.select_compliance_security_inventory_save_btn()
        self.dashboard.verify_analytic_dashboard_dashboard_updated_popup_msg()

        #Verify the removed widgets
        self.dashboard.verify_printer_fleet_security_widget(displayed=False)
        self.dashboard.verify_printer_fleet_compliance_widget_is_displayed(displayed=False)
        self.dashboard.verify_printer_inventory_card()

    def test_05_verify_new_dashboard_delete_functionality(self):
        #
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard(new_dashboard_name)
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_delete_dashboard_btn()
        self.dashboard.click_analytic_dashboard_delete_btn()
        self.dashboard.verify_analytic_dashboard_deleted_popup_msg()

        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytics_newly_created_dashboard(new_dashboard_name, displayed=False)
    
    def test_06_verify_edit_duplicate_delete_functionality_for_fleet_management_dashboard(self):
        #
        #Verify Fleet Management Dashboard
        assert "Fleet Management" == self.dashboard.get_analytics_fleet_management_dashboard_page_breadcrumb()
        assert "Fleet Management" == self.dashboard.get_analytics_fleet_management_dashboard_page_title()

        # Verify the dashboard name - Edit functionality
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_edit_dashboard_btn()
        self.dashboard.click_analytics_fleet_management_dashboard_pc_widget_from_select_widgets()
        #Remove the Printer Management widgets
        self.dashboard.select_fleet_inventory_widget()
        self.dashboard.click_select_widgets_save_btn()
        self.dashboard.verify_analytic_dashboard_dashboard_updated_popup_msg()

        # Verify the dashboard name - Edit functionality
        self.dashboard.click_analytics_new_dashboard_edit_btn()
        self.dashboard.edit_analytics_new_dashboard_name("update_"+new_dashboard_name)
        self.dashboard.click_analytics_new_dashboard_save_btn()
        self.dashboard.verify_analytics_new_dashboard_created_toast_message()

        #Verify the dashboard name and widget in Edit functionality
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard("update_"+new_dashboard_name)
        self.dashboard.verify_fleet_inventory_widget_is_displayed(displayed=True)

        #Verify the dashboard - Duplicate functionality
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_duplicate_dashboard_btn()
        self.dashboard.verify_analytic_dashboard_duplicate_popup_msg()
        self.dashboard.verify_fleet_inventory_widget_is_displayed(displayed=True)
        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytics_newly_created_dashboard("copy-update_"+new_dashboard_name)

        # Verify the dashboard name - Delete functionality
        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard("copy-update_"+new_dashboard_name)
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_delete_dashboard_btn()
        self.dashboard.click_analytic_dashboard_delete_btn()
        self.dashboard.verify_analytic_dashboard_deleted_popup_msg()
        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytics_newly_created_dashboard("copy-update_"+new_dashboard_name, displayed=False)

        self.home.click_sidemenu_analytics_button()
        self.dashboard.click_created_analytic_dashboard("update_"+new_dashboard_name)
        self.dashboard.click_analytic_dashboard_expand_btn()
        self.dashboard.click_analytic_dashboard_delete_dashboard_btn()
        self.dashboard.click_analytic_dashboard_delete_btn()
        self.dashboard.verify_analytic_dashboard_deleted_popup_msg()
        self.home.click_sidemenu_analytics_button()
        self.dashboard.verify_analytics_newly_created_dashboard("update_"+new_dashboard_name, displayed=False)