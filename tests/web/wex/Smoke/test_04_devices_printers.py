import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_04_Workforce_Devices_Printers(object):

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
    def test_01_verify_default_and_changed_printers_table_sort_by_date_added_column(self):
        #
        # Verify the default table sorted by date added (sorted by default in descending order)
        self.printers.verify_devices_printers_table_loaded()
        initial_printers_date_added = self.printers.get_all_printers_date_added()
 
        # Check if the date added is sorted in descending order by default
        assert self.printers.verify_printers_date_added_is_sorted(initial_printers_date_added, "descending"), "The 'date added' column is not sorted in descending order by default."
 
        # Verify the sort change by date added (ascending order on first click)
        self.printers.click_table_header_by_name("printers_date_added")
        sorted_printers_date_added = self.printers.get_all_printers_date_added()
        assert self.printers.verify_printers_date_added_is_sorted(sorted_printers_date_added, "ascending"), "The 'date added' column is not sorted in ascending order after clicking the header."
   
    @pytest.mark.sanity
    def test_02_verify_printers_table_sort_by_serial_number_column(self):
        #
        # Verify the default table sort by serial number (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_serial_number = self.printers.get_all_printers_serial_number()
        self.printers.verify_printers_table_sort("printers_serial_number", initial_serial_number)
 
        # Verify the sort change by device name (ascending order on first click)
        self.printers.click_table_header_by_name("printers_serial_number")
        self.printers.verify_printers_table_sort("printers_serial_number", sorted(initial_serial_number))
 
        # Verify the sort change by device name (descending order on second click)
        self.printers.click_table_header_by_name("printers_serial_number")
        self.printers.verify_printers_table_sort("printers_serial_number", sorted(initial_serial_number, reverse=True))

    @pytest.mark.sanity
    def test_03_verify_printers_table_sort_by_model_name_column(self):
        #
        # Verify the default table sort by model name (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_model_name = self.printers.get_all_printers_model_name()
        self.printers.verify_printers_table_sort("printers_model_name", initial_model_name)
 
        # Verify the sort change by model name (ascending order on first click)
        self.printers.click_table_header_by_name("printers_model_name")
        self.printers.verify_printers_table_sort("printers_model_name", sorted(initial_model_name))
 
        # Verify the sort change by model name (descending order on second click)
        self.printers.click_table_header_by_name("printers_model_name")
        self.printers.verify_printers_table_sort("printers_model_name", sorted(initial_model_name, reverse=True))
   
    @pytest.mark.sanity
    def test_04_verify_printers_table_sort_by_assessment_column(self):
        #
        # Verify the default table sort by assessment (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_assessment = self.printers.get_all_printers_assessment()
 
        # Verify the sort change by assessment (descending order on first click - High risk to Passed)
        self.printers.click_table_header_by_name("printer_assessment_status")
        descending_assessment = self.printers.get_all_printers_assessment()
        expected_descending = sorted(initial_assessment, key=self.printers.assessment_sort_key)
        self.printers.verify_printers_assessment_table_sort("printer_assessment_status", expected_descending)
 
        # Verify the sort change by assessment (ascending order on second click - Passed to High risk)
        self.printers.click_table_header_by_name("printer_assessment_status")
        ascending_assessment = self.printers.get_all_printers_assessment()
        expected_ascending = sorted(initial_assessment, key=self.printers.assessment_sort_key, reverse=True)
        self.printers.verify_printers_assessment_table_sort("printer_assessment_status", expected_ascending)
   
    @pytest.mark.sanity
    def test_05_verify_printers_table_sort_by_policies_column(self):
        #
        # Verify the default table sort by policies (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_policies = self.printers.get_all_printers_policies()
 
        # Verify the sort change by policies (ascending order on first click)
        self.printers.click_table_header_by_name("printers_policies")
        self.printers.verify_printers_table_sort("printers_policies", sorted(initial_policies))
 
        # Verify the sort change by policies (descending order on second click)
        self.printers.click_table_header_by_name("printers_policies")
        self.printers.verify_printers_table_sort("printers_policies", sorted(initial_policies, reverse=True))
 
    @pytest.mark.sanity
    def test_06_verify_printers_table_sort_by_policy_compliance_column(self):
        #
        # Verify the default table sort by policy compliance (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_policy_compliance = self.printers.get_all_printers_policy_compliance()
        self.printers.verify_printers_table_sort("printers_policy_compliance", initial_policy_compliance)
 
        # Verify the sort change by policy compliance (ascending order on first click)
        self.printers.click_table_header_by_name("printers_policy_compliance")
        self.printers.verify_printers_table_sort("printers_policy_compliance", sorted(initial_policy_compliance))
 
        # Verify the sort change by policy compliance (descending order on second click)
        self.printers.click_table_header_by_name("printers_policy_compliance")
        self.printers.verify_printers_table_sort("printers_policy_compliance", sorted(initial_policy_compliance, reverse=True))
   
    @pytest.mark.sanity
    def test_07_verify_printers_table_sort_by_policy_date_run_column(self):
        #
        # Verify the default table sort by Policy Date Run (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_policy_date_run = self.printers.get_all_printers_policy_date_run()
 
        # Verify the sort change by Policy Date Run (ascending order on first click - oldest to newest)
        self.printers.click_table_header_by_name("printers_policy_date_run")
        ascending_policy_date_run = self.printers.get_all_printers_policy_date_run()
        assert self.printers.verify_printers_policy_date_run_is_sorted(ascending_policy_date_run, "ascending"), "Policy Date Run column is not sorted in ascending order after first click."
 
        # Verify the sort change by Policy Date Run (descending order on second click - newest to oldest)
        self.printers.click_table_header_by_name("printers_policy_date_run")
        descending_policy_date_run = self.printers.get_all_printers_policy_date_run()
        assert self.printers.verify_printers_policy_date_run_is_sorted(descending_policy_date_run, "descending"), "Policy Date Run column is not sorted in descending order after second click."
   
    @pytest.mark.sanity
    def test_08_verify_printers_table_sort_by_connectivity_column(self):
        #
        # Verify the default table sort by connectivity (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_connectivity = self.printers.get_all_printers_connectivity_status()
        self.printers.verify_printers_table_sort("printer_connectivity", initial_connectivity)
 
        # Verify the sort change by connectivity (ascending order on first click)
        self.printers.click_table_header_by_name("printer_connectivity")
        self.printers.verify_printers_table_sort("printer_connectivity", sorted(initial_connectivity))
 
        # Verify the sort change by connectivity (descending order on second click)
        self.printers.click_table_header_by_name("printer_connectivity")
        self.printers.verify_printers_table_sort("printer_connectivity", sorted(initial_connectivity, reverse=True))
   
    @pytest.mark.sanity
    def test_09_verify_printers_table_sort_by_device_name_column(self):
        #
        # Verify the default table sort by device name (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_device_name = self.printers.get_all_printers_device_name()
        self.printers.verify_printers_table_sort("printers_device_name", initial_device_name)
 
        # Verify the sort change by device name (ascending order on first click)
        self.printers.click_table_header_by_name("printers_device_name")
        self.printers.verify_printers_table_sort("printers_device_name", sorted(initial_device_name))
 
        # Verify the sort change by device name (descending order on second click)
        self.printers.click_table_header_by_name("printers_device_name")
        self.printers.verify_printers_table_sort("printers_device_name", sorted(initial_device_name, reverse=True))
   
    @pytest.mark.sanity
    def test_10_verify_printers_table_sort_by_group_column(self):
        #
        # Verify the default table sort by group (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_group = self.printers.get_all_printers_group()
        self.printers.verify_printers_table_sort("printers_group", initial_group)
 
        # Verify the sort change by group (ascending order on first click)
        self.printers.click_table_header_by_name("printers_group")
        self.printers.verify_printers_table_sort("printers_group", sorted(initial_group))
 
        # Verify the sort change by group (descending order on second click)
        self.printers.click_table_header_by_name("printers_group")
        self.printers.verify_printers_table_sort("printers_group", sorted(initial_group, reverse=True))
 
    @pytest.mark.skip
    def test_11_verify_printers_table_sort_by_wired_ipv4_address_column(self):
        #
        # Verify the default table sort by wired ipv4 address (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        # self.printers.enable_printers_table_column()
        initial_wired_ipv4_address = self.printers.get_all_printers_wired_ipv4_address()
        self.printers.verify_printers_table_sort("printers_wiredipv4", initial_wired_ipv4_address)
 
        # Verify the sort change by wired ipv4 address (ascending order on first click)
        self.printers.click_table_header_by_name("printers_wiredipv4")
        self.printers.verify_printers_table_sort("printers_wiredipv4", sorted(initial_wired_ipv4_address))
 
        # Verify the sort change by wired ipv4 address (descending order on second click)
        self.printers.click_table_header_by_name("printers_wiredipv4")
        self.printers.verify_printers_table_sort("printers_wiredipv4", sorted(initial_wired_ipv4_address, reverse=True))
        self.printers.disable_printers_table_column()

    @pytest.mark.sanity
    def test_12_verify_printers_table_sort_by_company_name_column(self):
        #
        # Verify the default table sort by company name (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_company_name = self.printers.get_all_printers_company_name()
        self.printers.verify_printers_table_sort("printers_company_name", initial_company_name)
 
        # Verify the sort change by company name (ascending order on first click)
        self.printers.click_table_header_by_name("printers_company_name")
        self.printers.verify_printers_table_sort("printers_company_name", sorted(initial_company_name))
 
        # Verify the sort change by company name (descending order on second click)
        self.printers.click_table_header_by_name("printers_company_name")
        self.printers.verify_printers_table_sort("printers_company_name", sorted(initial_company_name, reverse=True))

    @pytest.mark.sanity
    def test_13_verify_printers_table_sort_by_contact_person_column(self):
        #
        # Verify the default table sort by contact person (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_contact_person = self.printers.get_all_printers_contact_person()
        self.printers.verify_printers_table_sort("printers_contact_person", initial_contact_person)
 
        # Verify the sort change by contact person (ascending order on first click)
        self.printers.click_table_header_by_name("printers_contact_person")
        self.printers.verify_printers_table_sort("printers_contact_person", sorted(initial_contact_person))
 
        # Verify the sort change by contact person (descending order on second click)
        self.printers.click_table_header_by_name("printers_contact_person")
        self.printers.verify_printers_table_sort("printers_contact_person", sorted(initial_contact_person, reverse=True))

    @pytest.mark.sanity
    def test_14_verify_printers_table_sort_by_control_panel_language_column(self):
        #
        # Verify the default table sort by control panel language (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_control_panel_language = self.printers.get_all_printers_control_panel_language()
        self.printers.verify_printers_table_sort("printers_control_panel_language", initial_control_panel_language)
 
        # Verify the sort change by control panel language (ascending order on first click)
        self.printers.click_table_header_by_name("printers_control_panel_language")
        self.printers.verify_printers_table_sort("printers_control_panel_language", sorted(initial_control_panel_language))
 
        # Verify the sort change by control panel language (descending order on second click)
        self.printers.click_table_header_by_name("printers_control_panel_language")
        self.printers.verify_printers_table_sort("printers_control_panel_language", sorted(initial_control_panel_language, reverse=True))
    
    @pytest.mark.sanity
    def test_15_verify_printers_table_sort_by_manufacturer_column(self):
        #
        # Verify the default table sort by manufacturer (not sorted by default)
        self.printers.verify_devices_printers_table_loaded()
        initial_manufacturer = self.printers.get_all_printers_manufacturer()
        self.printers.verify_printers_table_sort("printers_manufacturer", initial_manufacturer)
 
        # Verify the sort change by manufacturer (ascending order on first click)
        self.printers.click_table_header_by_name("printers_manufacturer")
        self.printers.verify_printers_table_sort("printers_manufacturer", sorted(initial_manufacturer))
 
        # Verify the sort change by manufacturer (descending order on second click)
        self.printers.click_table_header_by_name("printers_manufacturer")
        self.printers.verify_printers_table_sort("printers_manufacturer", sorted(initial_manufacturer, reverse=True))