import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "WEX"
import random
from MobileApps.libs.flows.web.wex.wex_api_utility import *

#Generate random proxy name
proxy_name = "autoproxy_"+str(random.randint(1000,9999))

class Test_05_Workforce_Devices_Print_Proxies(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_proxies(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.print_proxies.verify_print_proxies_table_data_load()

    def test_01_verify_print_proxies_contextual_footer_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128855
        self.print_proxies.click_print_proxies_checkbox()
        self.print_proxies.verify_contextual_footer()
        self.print_proxies.verify_contextual_footer_cancel_button()
        self.print_proxies.verify_contextual_footer_selected_item_label()
        self.print_proxies.verify_contextual_footer_select_action_dropdown()
        self.print_proxies.verify_contextual_footer_continue_button()
        self.print_proxies.click_contextual_footer_cancel_button()
        self.print_proxies.verify_contextual_footer_is_not_displayed()

    def test_02_verify_print_proxies_contextual_footer_select_action_dropdown_options(self):
        #
        expected_options= ["Edit", "Remove"]
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_checkbox()
        self.print_proxies.verify_contextual_footer()
        self.print_proxies.click_contextual_footer_select_action_dropdown()
        assert expected_options == self.print_proxies.get_contextual_footer_select_action_dropdown_options()

    def test_03_verify_proxies_table_sort_by_connectivity_column(self):
        #
        # Verify the default table state (not sorted by connectivity status)
        self.print_proxies.verify_print_proxies_table_data_load()

        # Verify the sort change by connectivity status (Offline, Online)
        self.print_proxies.click_table_header_by_name("connectivity_status")
        self.print_proxies.verify_table_sort("connectivity_status", ["Offline", "Online"])

        # Verify the sort change by connectivity status (Online, Offline)
        self.print_proxies.click_table_header_by_name("connectivity_status")
        self.print_proxies.verify_table_sort("connectivity_status", ["Online", "Offline"])

    def test_04_verify_proxies_table_sort_by_device_name_column(self):
        #
        # Verify the default table sort by device name (not sorted by default)
        self.print_proxies.verify_print_proxies_table_data_load()
        initial_proxy_names = self.print_proxies.get_all_proxy_names()
        self.print_proxies.verify_proxies_table_sort("proxy_name", initial_proxy_names)

        # Verify the sort change by device name (ascending order on first click)
        self.print_proxies.click_table_header_by_name("proxy_name")
        self.print_proxies.verify_proxies_table_sort("proxy_name", sorted(initial_proxy_names))

        # Verify the sort change by device name (descending order on second click)
        self.print_proxies.click_table_header_by_name("proxy_name")
        self.print_proxies.verify_proxies_table_sort("proxy_name", sorted(initial_proxy_names, reverse=True))

    def test_05_verify_proxies_table_sort_by_devices_count_column(self):
        #
        # Verify the default table sort by devices count (not sorted by default)
        self.print_proxies.verify_print_proxies_table_data_load()
        initial_devices_count = self.print_proxies.get_all_proxy_devices_count()
        self.print_proxies.verify_proxies_table_sort("proxy_devices_count", initial_devices_count)

        # Verify the sort change by devices count (ascending order on first click)
        self.print_proxies.click_table_header_by_name("proxy_devices_count")
        self.print_proxies.verify_proxies_table_sort("proxy_devices_count", sorted(initial_devices_count))

        # Verify the sort change by devices count (descending order on second click)
        self.print_proxies.click_table_header_by_name("proxy_devices_count")
        self.print_proxies.verify_proxies_table_sort("proxy_devices_count", sorted(initial_devices_count, reverse=True))

    def test_06_verify_proxies_table_sort_by_last_updated_date_and_time_column(self):
        #
        # Verify the default table sort by last updated date and time (not sorted by default)
        self.print_proxies.verify_print_proxies_table_data_load()

        # Verify the sort change by last updated date and time (ascending order on first click)
        self.print_proxies.click_table_header_by_name("last_updated")
        sorted_last_updated_date = self.print_proxies.get_all_last_updated_date_and_time()
        assert self.print_proxies.verify_proxies_date_added_is_sorted(sorted_last_updated_date, "ascending"), "The 'last updated' column is not sorted in ascending order after clicking the header."

        # Verify the sort change by last updated date and time (descending order on second click)
        self.print_proxies.click_table_header_by_name("last_updated")
        sorted_last_updated_date = self.print_proxies.get_all_last_updated_date_and_time()
        assert self.print_proxies.verify_proxies_date_added_is_sorted(sorted_last_updated_date, "descending"), "The 'last updated' column is not sorted in descending order after clicking the header again."

    def test_07_verify_proxies_table_sort_by_hostname_column(self):
        #
        # Verify the default table sort by host names (not sorted by default)
        self.print_proxies.verify_print_proxies_table_data_load()
        initial_host_names = self.print_proxies.get_all_host_names()
        self.print_proxies.verify_proxies_table_sort("host_name", initial_host_names)

        # Verify the sort change by host names (ascending order on first click)
        self.print_proxies.click_table_header_by_name("host_name")
        self.print_proxies.verify_proxies_table_sort("host_name", sorted(initial_host_names))

        # Verify the sort change by host names (descending order on second click)
        self.print_proxies.click_table_header_by_name("host_name")
        self.print_proxies.verify_proxies_table_sort("host_name", sorted(initial_host_names, reverse=True))

    def test_08_verify_proxies_table_sort_by_proxy_description_column(self):
        #
        # Verify the default table sort by descriptions (not sorted by default)
        self.print_proxies.verify_print_proxies_table_data_load()
        initial_proxy_descriptions = self.print_proxies.get_all_proxy_descriptions()
        self.print_proxies.verify_proxies_table_sort("proxy_description", initial_proxy_descriptions)

        # Verify the sort change by descriptions (ascending order on first click)
        self.print_proxies.click_table_header_by_name("proxy_description")
        self.print_proxies.verify_proxies_table_sort("proxy_description", sorted(initial_proxy_descriptions))

        # Verify the sort change by descriptions (descending order on second click)
        self.print_proxies.click_table_header_by_name("proxy_description")
        self.print_proxies.verify_proxies_table_sort("proxy_description", sorted(initial_proxy_descriptions, reverse=True))

    def test_09_verify_default_and_changed_proxies_table_sort_by_date_added_column(self):
        #
        # Verify the default table sorted by date added (sorted by default in descending order)
        self.print_proxies.verify_print_proxies_table_data_load()
        initial_proxies_date_added = self.print_proxies.get_all_proxies_date_added()
        # Check if the date added is sorted in descending order by default
        assert self.print_proxies.verify_proxies_date_added_is_sorted(initial_proxies_date_added, "descending"), "The 'date added' column is not sorted in descending order by default."

        # Verify the sort change by date added (ascending order on first click)
        self.print_proxies.click_table_header_by_name("proxy_date_added")
        sorted_proxies_date_added = self.print_proxies.get_all_proxies_date_added()
        assert self.print_proxies.verify_proxies_date_added_is_sorted(sorted_proxies_date_added, "ascending"), "The 'date added' column is not sorted in ascending order after clicking the header."
    
    # def test_10_verify_add_printers_popup_view_instructions_page(self):
    #     #
    #     self.print_proxies.click_print_proxies_download_button()
    #     self.print_proxies.verify_add_printers_popup_view_instructions_link()
    #     self.print_proxies.click_add_printers_popup_view_instructions_link()
    #     self.print_proxies.verify_new_tab_opened()
    #     self.print_proxies.verify_view_instructions_newtab_url()