import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "WEX"

class Test_04_Workforce_Devices_PendingPrinters(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.pending_printers = self.fc.fd["devices_pendingprinters"]
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
        self.pending_printers.verify_devices_pending_printers_button()
        self.pending_printers.click_devices_pending_printers_button()
        return self.pending_printers.verify_devices_pending_printers_table_loaded()
    
    def test_01_verify_pending_printers_table_sort_by_serial_number_column(self):
        #
        initial_serial_numbers = self.pending_printers.get_all_pending_printers_serial_number()

        # Verify descending order sort
        self.pending_printers.click_table_header_by_name("pending_printers_serial_number")
        self.pending_printers.verify_printers_table_sort("pending_printers_serial_number", sorted(initial_serial_numbers, reverse=True))

        # Verify ascending order sort
        self.pending_printers.click_table_header_by_name("pending_printers_serial_number")
        self.pending_printers.verify_printers_table_sort("pending_printers_serial_number", sorted(initial_serial_numbers))

    def test_02_verify_pending_printers_table_sort_by_product_number_column(self):
        #
        initial_product_numbers = self.pending_printers.get_all_pending_printers_product_number()

        # Verify descending order sort
        self.pending_printers.click_table_header_by_name("pending_printers_product_number")
        self.pending_printers.verify_printers_table_sort("pending_printers_product_number", sorted(initial_product_numbers, reverse=True))

        # Verify ascending order sort
        self.pending_printers.click_table_header_by_name("pending_printers_product_number")
        self.pending_printers.verify_printers_table_sort("pending_printers_product_number", sorted(initial_product_numbers))

    def test_03_verify_pending_printers_table_sort_by_status_column(self):
        #
        initial_statuses = self.pending_printers.get_all_pending_printers_status()

        # Verify ascending order sort
        self.pending_printers.click_table_header_by_name("pending_printers_status")
        self.pending_printers.verify_printers_table_sort("pending_printers_status", sorted(initial_statuses))

        # Verify descending order sort
        self.pending_printers.click_table_header_by_name("pending_printers_status")
        self.pending_printers.verify_printers_table_sort("pending_printers_status", sorted(initial_statuses, reverse=True))

    def test_04_verify_default_and_changed_printers_table_sort_by_date_added_column(self):
        #
        # Verify the default table sorted by date added (sorted by default in descending order)
        initial_dates_added = self.pending_printers.get_all_pending_printers_date_added()

        # Check if the date added is sorted in descending order by default
        assert self.pending_printers.verify_printers_date_added_is_sorted(initial_dates_added, "ascending"), \
            "The 'date added' column is not sorted in ascending order by default."

        # Verify the sort change by date added (ascending order on first click)
        self.pending_printers.click_table_header_by_name("pending_printers_date_added")
        sorted_dates_added = self.pending_printers.get_all_pending_printers_date_added()
        assert self.pending_printers.verify_printers_date_added_is_sorted(sorted_dates_added, "descending"), \
            "The 'date added' column is not sorted in descending order after clicking the header."

        # Verify the sort change back to descending order on second click
        self.pending_printers.click_table_header_by_name("pending_printers_date_added")
        sorted_dates_added = self.pending_printers.get_all_pending_printers_date_added()
        assert self.pending_printers.verify_printers_date_added_is_sorted(sorted_dates_added, "ascending"), \
            "The 'date added' column is not sorted in ascending order after clicking the header again."
    
    def test_05_verify_pending_printers_refresh_button(self):
        #
        # Click checkboxes to select devices
        all_printers = self.pending_printers.get_all_pending_printers_serial_number()
        self.pending_printers.click_pending_printers_checkbox()
        selected_devices_count = self.pending_printers.get_pending_printers_no_of_items_selected_label_count()

        # Verify selected devices count is greater than 0
        assert selected_devices_count > 0, "No devices were selected before refresh."

        # Click refresh button
        self.pending_printers.click_pending_printers_refresh_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

        # Assert selected devices count is 0 after refresh - verify label is not displayed
        self.pending_printers.verify_pending_printers_no_of_items_selected_label(displayed=False)

        # Assert all printers are loaded after refresh
        assert all_printers == self.pending_printers.get_all_pending_printers_serial_number(), "Printers list is not loaded correctly after clicking the refresh button."

    def test_06_verify_action_needed_card_printers_count_and_status(self):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_pending_printers_status_overview_card()

        # Expand the status overview card if not already expanded
        if not self.pending_printers.verify_pending_printers_status_overview_card_expanded():
            self.pending_printers.click_pending_printers_status_overview_card_expand_button()

        # Capture the printers count from the "Action Needed" card
        action_needed_count = self.pending_printers.get_pending_printers_action_needed_card_printers_count()
        assert action_needed_count is not None, "Failed to retrieve 'Action Needed' card printers count."

        table_count = self.pending_printers.get_pending_printers_table_status_count("Action needed")
        assert table_count is not None, "Failed to retrieve 'Action needed' status count from the table."
        
        # Cross-verify the count in the table matches the count from the card
        assert action_needed_count == table_count, \
            f"Action Needed card count from status overview ({action_needed_count}) does not match the count of 'Action needed' table printer status ({table_count})."

    def test_07_verify_error_card_printers_count_and_status(self):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_pending_printers_status_overview_card()

        # Expand the status overview card if not already expanded
        if not self.pending_printers.verify_pending_printers_status_overview_card_expanded():
            self.pending_printers.click_pending_printers_status_overview_card_expand_button()
        
        # Capture the printers count from the "Error" card
        error_count = self.pending_printers.get_pending_printers_error_card_printers_count()
        assert error_count is not None, "Failed to retrieve 'Error' card printers count."

        table_count = self.pending_printers.get_pending_printers_table_status_count("Error")
        assert table_count is not None, "Failed to retrieve 'Error' status count from the table."

        # Cross-verify the count in the table matches the count from the card
        assert error_count == table_count, \
            f"Error card count from status overview ({error_count}) does not match the count of 'Error' table printer status ({table_count})."
        
    def test_08_verify_connected_card_printers_count_and_status(self):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_pending_printers_status_overview_card()

        # Expand the status overview card if not already expanded
        if not self.pending_printers.verify_pending_printers_status_overview_card_expanded():
            self.pending_printers.click_pending_printers_status_overview_card_expand_button()

        # Capture the printers count from the "Connected" card
        connected_count = self.pending_printers.get_pending_printers_connected_card_printers_count()
        assert connected_count is not None, "Failed to retrieve 'Connected' card printers count."

        table_count = self.pending_printers.get_pending_printers_table_status_count("Connected")
        assert table_count is not None, "Failed to retrieve 'Connected' status count from the table."
        
        # Cross-verify the count in the table matches the count from the card
        assert connected_count == table_count, \
            f"Connected card count from status overview ({connected_count}) does not match the count of 'Connected' table printer status ({table_count})."
    
    def test_09_verify_pending_printers_delete_button_popup_ui(self):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.click_pending_printers_checkbox()
        self.pending_printers.verify_pending_printers_delete_button_status("enabled")
        self.pending_printers.click_pending_printers_delete_button()

        # Verify the delete confirmation popup UI elements
        self.pending_printers.verify_delete_confirmation_popup()
        self.pending_printers.verify_delete_confirmation_popup_title()
        self.pending_printers.verify_delete_confirmation_popup_message()
        self.pending_printers.verify_delete_confirmation_popup_cancel_button()
        self.pending_printers.verify_delete_confirmation_popup_delete_button()
        self.pending_printers.verify_delete_confirmation_popup_close_button()
        self.pending_printers.click_delete_confirmation_popup_close_button()
        self.pending_printers.verify_delete_confirmation_popup(displayed=False)