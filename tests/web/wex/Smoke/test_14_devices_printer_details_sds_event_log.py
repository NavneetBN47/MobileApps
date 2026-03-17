
import pytest
import logging
from time import sleep
from datetime import datetime, timedelta
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

@pytest.mark.skip
class Test_14_Workforce_Printer_Details_SDS_Event_Log(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.serial_number = request.config.getoption("--proxy-device")
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]
        self.emulator_serial_number = self.account["emulator_assignment_serial_number"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        sleep(5)
        self.printers.search_printers("SIM")
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_and_click_one_sim_printer()
        self.printers.click_printers_details_page_hp_sds_event_log_tab()       
        return self.printers.verify_sds_event_log_tab_event_log_table_loaded()

    def test_01_verify_printer_details_sds_event_log_tab_ui(self):
        #
        expected_table_headers = ["Code", "Description", "Recommended action", "Date", "Type", "Cycles", "Firmware version"]
        self.printers.verify_sds_event_log_tab_filters_button()
        self.printers.verify_sds_event_log_tab_column_options_button()
        self.printers.verify_page_size_btn()
        self.printers.verify_page_nav()
        sleep(5)
        assert expected_table_headers == self.printers.verify_sds_event_log_tab_event_log_table_headers()

    def test_02_verify_sds_event_log_table_pagination(self):
        # 
        self.printers.verify_all_page_size_options([25, 50, 100])
        self.printers.verify_table_displaying_correctly(25, page=1)
        self.printers.verify_table_displaying_correctly(50, page=1)
        self.printers.verify_table_displaying_correctly(100, page=1)

    def test_03_verify_sds_event_log_tab_column_option_popup_ui(self):
        # 
        expected_options= ['Code', 'Description', 'Recommended action', 'Date', 'Type', 'Cycles', 'Firmware version']
        self.printers.click_sds_event_log_tab_column_options_button()
        self.printers.verify_sds_event_log_tab_column_options_popup_title()
        self.printers.verify_sds_event_log_tab_column_options_popup_reset_to_default_button()
        self.printers.verify_sds_event_log_tab_column_options_popup_cancel_button()
        self.printers.verify_sds_event_log_tab_column_options_popup_save_button()
        assert expected_options == self.printers.get_sds_event_log_tab_column_options_popup_options()

    def test_04_verify_sds_event_log_tab_column_option_popup_save_button_functionality(self):
        # 
        self.printers.click_sds_event_log_tab_column_options_button()
        self.printers.click_sds_event_log_table_column_option("Code")
        self.printers.click_sds_event_log_tab_column_options_popup_save_button()

        # Verify Event log table Code Column
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_sds_event_log_table_column("Code",displayed=False)

        # Reverting the Column option changes
        self.printers.click_sds_event_log_tab_column_options_button()
        self.printers.click_sds_event_log_table_column_option("Code")
        self.printers.click_sds_event_log_tab_column_options_popup_save_button()

        # # Verify Event log table Code Column
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_sds_event_log_table_column("Code")

    def test_05_verify_sds_event_log_tab_column_option_popup_cancel_button_functionality(self):
        # 
        self.printers.click_sds_event_log_tab_column_options_button()
        self.printers.click_sds_event_log_table_column_option("Code")
        self.printers.click_sds_event_log_tab_column_options_popup_cancel_button()
        # Verify Event log table Code Column
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_sds_event_log_table_column("Code")

    def test_06_verify_sds_event_log_table_sort_by_code_column(self):
        #
        # Verify the default table sort by code (not sorted by default)
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        initial_code = self.printers.get_all_event_logs_code()
        self.printers.verify_event_log_table_sort("event_log_code", initial_code)
 
        # Verify the sort change by code(ascending order on first click)
        self.printers.click_table_header_by_name("event_log_code")
        self.printers.verify_event_log_table_sort("event_log_code", sorted(initial_code))
 
        # Verify the sort change by code(descending order on second click)
        self.printers.click_table_header_by_name("event_log_code")
        self.printers.verify_event_log_table_sort("event_log_code", sorted(initial_code, reverse=True))
    
    def test_07_verify_sds_event_log_table_sort_by_type_column(self):
        #
        # Verify the default table sort by description (not sorted by default)
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        initial_event_type = self.printers.get_all_event_logs_type()
        self.printers.verify_event_log_table_sort("event_log_type", initial_event_type)
 
        # Verify the sort change by description(ascending order on first click)
        self.printers.click_table_header_by_name("event_log_type")
        self.printers.verify_event_log_table_sort("event_log_type", sorted(initial_event_type))
 
        # Verify the sort change by description(descending order on second click)
        self.printers.click_table_header_by_name("event_log_type")
        self.printers.verify_event_log_table_sort("event_log_type", sorted(initial_event_type, reverse=True))
    
    def test_08_verify_sds_event_log_table_sort_by_cycles_column(self):
        #
        # Verify the default table sort by description (not sorted by default)
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        initial_event_type = self.printers.get_all_event_logs_cycle()
        self.printers.verify_event_log_table_sort("event_log_cycle", initial_event_type)
 
        # Verify the sort change by description(ascending order on first click)
        self.printers.click_table_header_by_name("event_log_cycle")
        self.printers.verify_event_log_table_sort("event_log_cycle", sorted(initial_event_type))
 
        # Verify the sort change by description(descending order on second click)
        self.printers.click_table_header_by_name("event_log_cycle")
        self.printers.verify_event_log_table_sort("event_log_cycle", sorted(initial_event_type, reverse=True))
    
    def test_09_verify_sds_event_log_table_sort_by_firmware_version_column(self):
        #
        # Verify the default table sort by description (not sorted by default)
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        initial_logs_firmware_version = self.printers.get_all_event_logs_firmware_version()
        self.printers.verify_event_log_table_sort("event_log_firmware_version", initial_logs_firmware_version)
 
        # Verify the sort change by description(ascending order on first click)
        self.printers.click_table_header_by_name("event_log_firmware_version")
        self.printers.verify_event_log_table_sort("event_log_firmware_version", sorted(initial_logs_firmware_version))
 
        # Verify the sort change by description (descending order on second click)
        self.printers.click_table_header_by_name("event_log_firmware_version")
        self.printers.verify_event_log_table_sort("event_log_firmware_version", sorted(initial_logs_firmware_version, reverse=True))
    
    # Date and column sort not working as expected
    # def test_10_verify_default_and_changed_sds_event_log_table_sort_by_date_column(self):
    #     #
    #     # Verify the default table sorted by date (sorted by default in ascending order)
    #     self.printers.verify_table_displaying_correctly(100, page=1)
    #     self.printers.verify_sds_event_log_tab_event_log_table_loaded()
    #     initial_logs_date = self.printers.get_all_event_logs_date()
 
    #     # # Check if the date is sorted in ascending order by default
    #     # assert self.printers.verify_event_log_date_is_sorted(initial_logs_date, "ascending"), "The 'date' column is not sorted in ascending order by default."
 
    #     # Verify the sort change by date (descending order on first click)
    #     self.printers.click_table_header_by_name("event_log_date")
    #     sorted_logs_date = self.printers.get_all_event_logs_date()
    #     assert self.printers.verify_event_log_date_is_sorted(sorted_logs_date, "descending"), "The 'date' column is not sorted in descending order after clicking the header."

    def test_11_verify_sds_event_log_tab_filters_popup_ui(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_sds_event_log_tab_filters_button()  
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.verify_event_log_filter_side_bar_title()
        self.printers.verify_event_log_filter_side_bar_clear_all_button()
        self.printers.verify_event_log_filter_side_bar_event_type_dropdown_label()
        self.printers.verify_event_log_filter_side_bar_event_type_dropdown()
        self.printers.verify_event_log_filter_side_bar_timeframe_dropdown_label()
        self.printers.verify_event_log_filter_side_bar_timeframe_dropdown()
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_event_log_filter_side_bar_title(displayed=False)

    def test_12_verify_sds_event_log_tab_filters_dropdown_options(self):
        #
        expected_event_type_options = ["All", "Error", "Warning", "Info"]
        expected_timeframe_options = ["Last 7 days", "Last 30 days", "Last 60 days", "Last 90 days", "Custom"]

        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.click_sds_event_log_tab_filters_button()

        # Verify event type dropdown options
        self.printers.click_event_log_filter_side_bar_event_type_dropdown()
        actual_event_type_options = self.printers.get_event_log_filter_side_bar_event_type_dropdown_options()
        assert expected_event_type_options == actual_event_type_options, f"Expected {expected_event_type_options}, but got {actual_event_type_options}"
        sleep(5)
        self.printers.select_event_log_filter_event_type_dropdown_options("Info")

        # Verify timeframe dropdown options
        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()
        actual_timeframe_options = self.printers.get_event_log_filter_side_bar_timeframe_dropdown_options()
        assert expected_timeframe_options == actual_timeframe_options, f"Expected {expected_timeframe_options}, but got {actual_timeframe_options}"
        sleep(5)
        self.printers.select_event_log_filter_timeframe_dropdown_options("Last 7 days")

    def test_13_verify_sds_event_log_tab_filter_clear_all_button_functionality(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_event_type_dropdown()
        # Get the initially selected event type option
        initial_event_type_option = self.printers.get_event_log_filter_side_bar_event_type_dropdown_selected_option()
        # Select a different event type option
        self.printers.select_event_log_filter_event_type_dropdown_options("Info")
        
        # Verify the event type filter option was changed
        assert initial_event_type_option != self.printers.get_event_log_filter_side_bar_event_type_dropdown_selected_option(), "The event type filter option was not changed."

        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()        
        # Get the initially selected timeframe option
        initial_timeframe_option = self.printers.get_event_log_filter_side_bar_timeframe_dropdown_selected_option()
        # Select a different timeframe option
        self.printers.select_event_log_filter_timeframe_dropdown_options("Last 7 days")
        
        # Verify the timeframe filter option was changed
        assert initial_timeframe_option != self.printers.get_event_log_filter_side_bar_timeframe_dropdown_selected_option(), "The timeframe filter option was not changed."

        # Click on the clear all button to reset the filters
        self.printers.click_event_log_filter_side_bar_clear_all_button()

        # Verify the event type filter option was reverted to the initial state
        assert initial_event_type_option == self.printers.get_event_log_filter_side_bar_event_type_dropdown_selected_option(), "The event type filter option was not reverted to the initial state."
        
        # Verify the timeframe filter option was reverted to the initial state
        assert initial_timeframe_option == self.printers.get_event_log_filter_side_bar_timeframe_dropdown_selected_option(), "The timeframe filter option was not reverted to the initial state."
    
    def test_14_verify_sds_event_log_table_info_event_guide_me_link(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_event_type_dropdown()
        self.printers.select_event_log_filter_event_type_dropdown_options("Info")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()

        # Verify that all displayed logs are of type "Info"
        event_types = self.printers.get_sds_event_log_table_all_event_logs_type()
        assert all(event_type == "info" for event_type in event_types), "Not all displayed logs are of type 'Info'"

        # Verify the Guide Me link navigation for an Info event
        self.printers.click_sds_event_log_table_first_guide_me_link()
        self.printers.verify_guide_me_link_page_loaded()

    def test_15_verify_sds_event_log_table_warning_event_guide_me_link(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_event_type_dropdown()
        self.printers.select_event_log_filter_event_type_dropdown_options("Warning")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()

        # Verify that all displayed logs are of type "Warning"
        event_types = self.printers.get_sds_event_log_table_all_event_logs_type()
        assert all(event_type == "warning" for event_type in event_types), "Not all displayed logs are of type 'Warning'"

        # Verify the Guide Me link navigation for a Warning event
        self.printers.click_sds_event_log_table_first_guide_me_link()
        self.printers.verify_guide_me_link_page_loaded()

    def test_16_verify_sds_event_log_table_error_event_guide_me_link(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_event_type_dropdown()
        self.printers.select_event_log_filter_event_type_dropdown_options("Error")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()

        # Verify that all displayed logs are of type "Error"
        event_types = self.printers.get_sds_event_log_table_all_event_logs_type()
        assert all(event_type == "error" for event_type in event_types), "Not all displayed logs are of type 'Error'"

        # Verify the Guide Me link navigation for an Error event
        self.printers.click_sds_event_log_table_first_guide_me_link()
        self.printers.verify_guide_me_link_page_loaded()

    def test_17_verify_sds_event_log_table_timeframe_last_7_days(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()
        self.printers.select_event_log_filter_timeframe_dropdown_options("Last 7 days")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
 
        # Verify that all displayed logs are within the last 7 days
        event_dates = self.printers.get_sds_event_log_table_all_event_logs_date()
        assert all(self.printers.verify_is_date_within_last_days(event_date, 7) for event_date in event_dates), "Not all displayed logs are within the last 7 days"
 
    def test_18_verify_sds_event_log_table_timeframe_last_30_days(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()
        self.printers.select_event_log_filter_timeframe_dropdown_options("Last 30 days")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
 
        # Verify that all displayed logs are within the last 30 days
        event_dates = self.printers.get_sds_event_log_table_all_event_logs_date()
        assert all(self.printers.verify_is_date_within_last_days(event_date, 30) for event_date in event_dates), "Not all displayed logs are within the last 30 days"
 
    def test_19_verify_sds_event_log_table_timeframe_last_60_days(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()
        self.printers.select_event_log_filter_timeframe_dropdown_options("Last 60 days")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
 
        # Verify that all displayed logs are within the last 60 days
        event_dates = self.printers.get_sds_event_log_table_all_event_logs_date()
        assert all(self.printers.verify_is_date_within_last_days(event_date, 60) for event_date in event_dates), "Not all displayed logs are within the last 60 days"
 
    def test_20_verify_sds_event_log_table_timeframe_last_90_days(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()
        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()
        self.printers.select_event_log_filter_timeframe_dropdown_options("Last 90 days")
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
 
        # Verify that all displayed logs are within the last 90 days
        event_dates = self.printers.get_sds_event_log_table_all_event_logs_date()
        assert all(self.printers.verify_is_date_within_last_days(event_date, 90) for event_date in event_dates), "Not all displayed logs are within the last 90 days"

    def test_21_verify_sds_event_log_table_timeframe_custom(self):
        #
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()
        self.printers.verify_table_displaying_correctly(100, page=1)
        self.printers.click_sds_event_log_tab_filters_button()

        self.printers.click_event_log_filter_side_bar_event_type_dropdown()
        self.printers.select_event_log_filter_event_type_dropdown_options("Warning")

        self.printers.click_event_log_filter_side_bar_timeframe_dropdown()
        self.printers.select_event_log_filter_timeframe_dropdown_options("Custom")

        # Set custom timeframe to include today's date
        today = datetime.now().strftime("%Y-%m-%d")
        self.printers.set_custom_timeframe(today, today)        
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()

        # Verify that all displayed logs are within today's date
        event_dates = self.printers.get_sds_event_log_table_all_event_logs_date()
        assert all(self.printers.verify_date_is_within_range(event_date, today, today) for event_date in event_dates), "Not all displayed logs are within today's date"

        # Set custom timeframe to include yesterday's date
        yesterday = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
        self.printers.set_custom_timeframe(yesterday, yesterday)
        self.printers.click_event_log_filter_side_bar_done_button()
        self.printers.verify_sds_event_log_tab_event_log_table_loaded()

        # Verify that all displayed logs are within yesterday's date
        event_dates = self.printers.get_sds_event_log_table_all_event_logs_date()
        assert all(self.printers.verify_date_is_within_range(event_date, yesterday, yesterday) for event_date in event_dates), "Not all displayed logs are within yesterday's date"