import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_15_Workforce_Devices_Printers(object):

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
    def test_01_verify_printers_configure_device_popup_ui(self):
        #
        self.printers.click_printers_checkbox()
        self.printers.click_configure_printers_button()

        # Verify Configure Device Pop-up
        self.printers.verify_configure_device_popup_title()
        self.printers.verify_configure_device_popup_description()
        self.printers.verify_configure_device_popup_cancel_button()
        self.printers.verify_configure_device_popup_configure_button(disabled=True)
        self.printers.click_configure_device_popup_cancel_button()
        self.printers.verify_devices_printers_table_loaded()

    @pytest.mark.sanity
    def test_02_verify_configure_device_popup_category_section(self):
        #
        self.printers.click_printers_checkbox()
        self.printers.click_configure_printers_button()

        self.printers.verify_configure_device_popup_title()
        self.printers.verify_configure_device_popup_category_section_title()
        self.printers.verify_configure_device_popup_all_category_option()
        self.printers.verify_configure_device_popup_all_category_expand_button()
        self.printers.verify_configure_device_popup_all_category_expanded()
        self.printers.click_configure_device_popup_all_category_expand_button()
        self.printers.verify_configure_device_popup_all_category_collapsed()

        self.printers.click_configure_device_popup_all_category_expand_button()
        category_options = self.printers.get_configure_device_popup_category_options()
        for option in category_options:
            self.printers.select_configure_device_popup_category_option(option)
            self.printers.verify_configure_device_popup_category_option_displayed(option)
    
    @pytest.mark.sanity
    def test_03_verify_search_field_default_text_based_on_category_selection(self):
        #
        self.printers.click_printers_checkbox()
        self.printers.click_configure_printers_button()

        self.printers.verify_configure_device_popup_title()

        # Verify the default search field text
        self.printers.verify_configure_device_popup_search_txtbox_text("All")
        
        # Retrieve all available category names dynamically
        category_names = self.printers.get_configure_device_popup_category_options()
        
        # Iterate over each category name and verify the search field default text
        for category_name in category_names:
            self.printers.select_configure_device_popup_category_option(category_name)
            self.printers.verify_configure_device_popup_search_txtbox_text(category_name)

    @pytest.mark.sanity
    def test_04_verfiy_printers_search_with_serial_number_functionality(self):
        #
        self.printers.search_printers(self.serial_number)
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_search_results_with_serial_number(self.serial_number)
    
    #Skipping as search functionality with assessment status is not supported - PSPECP-4802
    # @pytest.mark.sanity
    # def test_05_verfiy_printers_search_with_assessment_functionality(self):
    #     #
    #     self.printers.search_printers("Passed")
    #     self.printers.verify_devices_printers_table_loaded()
    #     self.printers.verify_search_results_with_assessment_status("Passed")
    
    @pytest.mark.sanity
    def test_06_verfiy_printers_search_with_policies_functionality(self):
        #
        self.printers.search_printers("Policy")
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_search_results_with_assigned_policies("Policy")
    
    #Skipping as search functionality with policy compliance is not supported - PSPECP-4802
    #@pytest.mark.sanity
    # def test_07_verfiy_printers_search_with_policy_compliance_functionality(self):
    #     #
    #     self.printers.search_printers("Compliant")
    #     self.printers.verify_devices_printers_table_loaded()
    #     self.printers.verify_search_results_with_policy_compliance("Compliant")
    
    #Skipping as search functionality with connectivity is not supported - PSPECP-4802 
    #@pytest.mark.sanity
    # def test_08_verfiy_printers_search_with_connectivity_functionality(self):
    #     #
    #     self.printers.search_printers("Online")
    #     self.printers.verify_devices_printers_table_loaded()
    #     self.printers.verify_search_results_with_connectivity("Online")

    @pytest.mark.sanity
    def test_09_verfiy_printers_search_with_device_name_functionality(self):
        #
        # Filtering with "device_name" in device_name cloumn is not working in UI 
        self.printers.search_printers("device_name")
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_search_results_with_device_name("device_name")
    
    #Skipping as search functionality with ipv4 address is not supported - PSPECP-4802
    #@pytest.mark.sanity
    # def test_10_verfiy_printers_search_with_ipv4_address_functionality(self):
    #     #
    #     #filtering with "ipv4_address" in Wired (IPv4 Address) cloumn is not working in UI
    #     self.printers.search_printers("15.4.")
    #     self.printers.verify_devices_printers_table_loaded()
    #     self.printers.verify_search_results_with_wiredipv4_address("15.4.")