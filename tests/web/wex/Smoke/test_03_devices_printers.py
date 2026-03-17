import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_03_Workforce_Devices_Printers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.serial_number = request.config.getoption("--proxy-device")
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
            self.serial_number = self.account["ldk_printer_serial_number"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        # self.printers.click_printers_group("All")
        return self.printers.verify_devices_printers_table_loaded()
    
    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Passed", "High Risk", "Medium Risk", "Low Risk", "Not Assessed"])
    def test_01_verify_printers_filter_functionality_by_security_assessment(self,filter_name):
        #        
        self.printers.verify_printers_filter_button()  
        self.printers.click_printers_filter_button()
        self.printers.select_printers_filter(filter_name)
        self.printers.verify_filter_in_printers_table_for_security_assessment_column(filter_name)
        self.printers.click_printers_filter_side_bar_close_button()
        self.printers.verify_printers_filter_side_bar_security_assessment_status_tags(filter_name)
        self.printers.click_printers_filter_side_bar_security_assessment_status_tag_close_tag()

    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Error", "Warning", "Ready", "Unknown"])
    def test_02_verify_printers_filter_functionality_by_device_status(self,filter_name):
        #        
        self.printers.verify_printers_filter_button()  
        self.printers.click_printers_filter_button()
        self.printers.select_printers_filter(filter_name)
        self.printers.verify_filter_in_printers_table_for_device_status_column(filter_name)
        self.printers.click_printers_filter_side_bar_close_button()
        self.printers.verify_printers_filter_side_bar_device_status_column_status_tags(filter_name)
        self.printers.click_printers_filter_side_bar_device_status_column_status_tag_close_tag()

    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Compliant", "Noncompliant", "Not Assessed"])
    def test_03_verify_printers_filter_functionality_by_policy_compliance(self,filter_name):
        #        
        self.printers.verify_printers_filter_button()  
        self.printers.click_printers_filter_button()
        self.printers.select_printers_compliance_filter_option(filter_name)
        self.printers.verify_filter_in_printers_table_for_policy_compliance_column(filter_name)
        self.printers.click_printers_filter_side_bar_close_button()
        self.printers.verify_printers_filter_side_bar_policy_compliance_status_tags(filter_name)
        self.printers.click_printers_filter_side_bar_policy_compliance_status_tag_close_tag()