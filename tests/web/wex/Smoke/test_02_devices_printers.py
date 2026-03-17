import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_02_Workforce_Devices_Printers(object):

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
    def test_01_verify_devices_printers_page_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128846
        expected_table_headers = ['Serial Number', 'Model Name', 'Connectivity', 'Connectivity Types', 'Status', 'Status Updated', 'Group',
                                 'Policies', 'Policy Date Run', 'Security Assessment', 'Policy Compliance', 'Firmware Version', 'Device Location',
                                 'Wired (Hostname)', 'Date Added', 'Wired (IPv4 Address)', 'Device Name', 'Asset Number', 'Manufacturer',
                                 'Contact Person', 'Company Name', 'Control Panel Language', 'Wired (IPv6 Address)', 'Wired (MAC Address)', 
                                 'Wireless (IPv4 Address)', 'Wireless (IPv6 Address)', 'Wireless (MAC Address)','Wireless (Hostname)',
                                 'Wi-Fi Direct (IPv4 Address)','Wi-Fi Direct (IPv6 Address)', 'Wi-Fi Direct (MAC Address)',
                                 'Wi-Fi Direct (Hostname)', 'Apps', 'Last Synced']

        self.printers.verify_devices_printers_page_devices_breadcrumb()
        self.printers.verify_printers_search_txtbox()
        self.printers.verify_printers_export_all_btn()
        self.printers.verify_printers_add_btn()
        self.printers.verify_column_option_settings_gear_button()
        self.printers.verify_groups_side_bar_collapse_btn()
        self.printers.verify_page_size_btn()
        self.printers.verify_page_nav()
        assert expected_table_headers == self.printers.verify_printers_table_headers()

    @pytest.mark.sanity
    def test_02_verify_printers_page_breadcrumb_and_url(self):
        #
        # Verify the breadcrumb  on the printers page
        self.printers.verify_devices_printers_page_devices_breadcrumb()

        # Verify the printers page URL
        self.printers.verify_devices_printers_page_url(self.stack)

    @pytest.mark.sanity
    def test_03_verify_printers_search_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128849
        self.printers.search_printers("HP ")
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_search_results_with_model_name("HP")

    @pytest.mark.sanity
    def test_04_verify_error_case_search(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128849
        self.printers.search_printers("InvalidData")
        self.printers.verify_no_items_found()

    @pytest.mark.sanity
    def test_05_verify_search_printer_by_partial_serial_number(self):
        partial_serial_number = self.serial_number[:5]
        self.printers.search_printers(partial_serial_number)
        sleep(5)  # Wait for search results to load
        self.printers.verify_search_results_with_serial_number(self.serial_number)

    @pytest.mark.sanity
    def test_06_verify_search_with_invalid_serial_number(self):
        invalid_serial_number = "INVALIDSER"
        self.printers.search_printers(invalid_serial_number)
        self.printers.verify_no_items_found()

    @pytest.mark.sanity
    def test_07_verify_pagination(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128853
        self.printers.verify_all_page_size_options([5, 25, 50, 100, 500])
        self.printers.verify_table_displaying_correctly(5, page=1)
        self.printers.verify_table_displaying_correctly(25, page=1)
        self.printers.verify_table_displaying_correctly(50, page=1)
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.verify_table_displaying_correctly(500, page=1)

    @pytest.mark.sanity
    def test_08_verify_column_option_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128869
        expected_options= ["Serial Number", "Model Name", "Connectivity", "Connectivity Types", "Status", "Status Updated", "Group", "Policies",
                          "Policy Date Run", "Security Assessment", "Policy Compliance", "Firmware Version", "Device Location", "Wired (Hostname)",
                          "Date Added", "Wired (IPv4 Address)", "Device Name", "Asset Number", "Manufacturer", "Contact Person", "Company Name",
                          "Control Panel Language", "Wired (IPv6 Address)","Wired (MAC Address)", "Wireless (IPv4 Address)", "Wireless (IPv6 Address)",
                          "Wireless (MAC Address)","Wireless (Hostname)", "Wi-Fi Direct (IPv4 Address)", "Wi-Fi Direct (IPv6 Address)", 
                          "Wi-Fi Direct (MAC Address)", "Wi-Fi Direct (Hostname)", "Apps", "Last Synced"]

        self.printers.click_printers_column_option_settings_gear_button()
        self.printers.verify_column_options_popup_title()
        self.printers.verify_column_options_popup_reset_to_default_button()
        self.printers.verify_column_options_popup_cancel_button()
        self.printers.verify_column_options_popup_save_button()
        assert expected_options == self.printers.get_column_options_popup_options()

    @pytest.mark.sanity
    def test_09_verify_column_option_popup_save_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128869
        self.printers.click_printers_column_option_settings_gear_button()
        self.printers.click_column_option("Connectivity")
        self.printers.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_printers_table_column("Connectivity",displayed=False)

        # Reverting the Column option changes
        self.printers.click_printers_column_option_settings_gear_button()
        self.printers.click_column_option("Connectivity")
        self.printers.click_column_options_popup_save_button()
        self.printers.verify_printers_table_column("Connectivity")

    @pytest.mark.sanity
    def test_10_verify_column_option_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128869
        self.printers.click_printers_column_option_settings_gear_button()
        self.printers.click_column_option("Connectivity")
        self.printers.click_column_options_popup_cancel_button()

        # Verify Customers table Domain Column
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_printers_table_column("Connectivity")

    @pytest.mark.sanity
    def test_11_verify_printers_filter_side_bar_ui(self):
        # 
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_printers_filter_button()  
        self.printers.click_printers_filter_button()
        self.printers.verify_printers_filter_side_bar_title()
        self.printers.verify_printers_filter_side_bar_description()
        self.printers.verify_printers_filter_side_bar_search_box()
        self.printers.verify_printers_filter_side_bar_connectivity_label()
        self.printers.click_printers_filter_side_bar_close_button()
        self.printers.verify_printers_filter_side_bar_title(displayed=False)

    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Online", "Offline"])
    def test_12_verify_printers_filter_functionality(self,filter_name):
        #        
        self.printers.verify_printers_filter_button()  
        self.printers.click_printers_filter_button()
        self.printers.select_printers_filter(filter_name)
        self.printers.verify_filter_in_printers_table(filter_name)
        self.printers.click_printers_filter_side_bar_close_button()
        self.printers.verify_printers_filter_side_bar_connectivity_status_tags(filter_name)
        self.printers.click_printers_filter_side_bar_connectivity_status_tag_close_tag()
    
    @pytest.mark.sanity
    def test_13_verify_filter_connectivity_status_clear_all_tag(self):
        #
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_printers_filter_button()  
        self.printers.click_printers_filter_button()
        self.printers.select_printers_filter("Online")
        self.printers.select_printers_filter("Offline")
        self.printers.click_printers_filter_side_bar_close_button()
        self.printers.verify_printers_filter_side_bar_connectivity_status_clear_all_tag()
        self.printers.click_printers_filter_side_bar_connectivity_status_clear_all_tag()
        self.printers.verify_printers_filter_side_bar_connectivity_online_tag_is_not_displayed()
        self.printers.verify_printers_filter_side_bar_connectivity_offline_tag_is_not_displayed()

    def test_14_verify_applying_filter_resets_to_first_page(self):
        #
        # Execute this testcase only if table has more than 5 printers
        total_printers = self.printers.get_printers_table_count()
        if total_printers <= 5:
            pytest.skip("Not enough printers to test pagination and filter on second page (need more than 5).")

        # Go to page 2
        self.printers.verify_table_displaying_correctly(5, page=1)
        self.printers.select_page(2)
        assert self.printers.get_current_page() == 2  # Verify on page 2

        # Apply filter (e.g., "Online")
        self.printers.click_printers_filter_button()
        self.printers.select_printers_filter("Online")
        self.printers.click_printers_filter_side_bar_close_button()

        # Check displayed results and page reset
        assert self.printers.get_current_page() == 1  # Page should reset to 1
        self.printers.verify_filter_in_printers_table("Online")
        self.printers.verify_devices_printers_table_loaded()

    def test_15_verify_all_printers_display_valid_serial_number(self):
        """
        Verify that all printers displayed in the table have valid serial numbers.
        """
        # Retrieve all serial numbers displayed in the printers table
        serial_numbers = self.printers.get_all_printers_serial_number()
        assert serial_numbers, "No printers found in the table."

        for sn in serial_numbers:
            assert isinstance(sn, str) and len(sn) == 10 and sn.isalnum(), f"Invalid serial number: {sn}"
            assert isinstance(sn, str) and len(sn) > 0, f"Invalid serial number: {sn}"