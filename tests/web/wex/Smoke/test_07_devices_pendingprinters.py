import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "WEX"

class Test_07_Workforce_Devices_PendingPrinters(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.pending_printers = self.fc.fd["devices_pendingprinters"]
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
        self.pending_printers.verify_devices_pending_printers_button()
        self.pending_printers.click_devices_pending_printers_button()
        return self.pending_printers.verify_devices_pending_printers_table_loaded()

    @pytest.mark.sanity
    def test_01_verify_pending_printers_screen_ui_contents(self):
        #
        expected_table_headers = ["Serial number", "Product number", "Status", "Date Added"]
        self.pending_printers.verify_pending_printers_search_textbox()
        self.pending_printers.verify_pending_printers_add_printers_button()
        self.pending_printers.verify_pending_printers_refresh_button()
        self.pending_printers.verify_pending_printers_gear_button()
        self.pending_printers.verify_pending_printers_filter_button()
        self.pending_printers.verify_page_size_btn()
        self.pending_printers.verify_page_nav()       
        self.pending_printers.verify_pending_printers_status_overview_card()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

        self.pending_printers.verify_pending_printers_delete_button(displayed=False)
        self.pending_printers.verify_pending_printers_no_of_items_selected_label(displayed=False)
        self.pending_printers.verify_pending_printers_select_all_button(displayed=False)

        self.pending_printers.click_pending_printers_checkbox()
        self.pending_printers.verify_pending_printers_delete_button(displayed=True)
        self.pending_printers.verify_pending_printers_no_of_items_selected_label(displayed=True)
        self.pending_printers.verify_pending_printers_select_all_button(displayed=True)
        assert expected_table_headers == self.pending_printers.verify_devices_pending_printers_table_headers()
    
    def test_02_verify_pending_printers_status_overview_card(self):
        #
        self.pending_printers.verify_pending_printers_status_overview_card()
        if self.pending_printers.verify_pending_printers_status_overview_card_expanded() is False:
            self.pending_printers.click_pending_printers_status_overview_card_expand_button()
        self.pending_printers.verify_pending_printers_status_overview_card_title()
        self.pending_printers.verify_pending_printers_status_overview_card_description()
        self.pending_printers.verify_pending_printers_status_overview_action_needed_card()
        self.pending_printers.verify_pending_printers_status_overview_error_card()
        self.pending_printers.verify_pending_printers_status_overview_connected_card()

        # Verify the status overview - action needed card
        self.pending_printers.verify_pending_printers_action_needed_card_label()
        # self.pending_printers.verify_pending_printers_action_needed_card_label_icon()
        self.pending_printers.verify_pending_printers_action_needed_card_title()
        self.pending_printers.verify_pending_printers_action_needed_card_description()
        self.pending_printers.verify_pending_printers_action_needed_card_printers_count()

        # Verify the status overview - error card
        self.pending_printers.verify_pending_printers_error_card_label()
        # self.pending_printers.verify_pending_printers_error_card_label_icon()
        self.pending_printers.verify_pending_printers_error_card_title()
        self.pending_printers.verify_pending_printers_error_card_description()
        self.pending_printers.verify_pending_printers_error_card_printers_count()

        # Verify the status overview - connected card
        self.pending_printers.verify_pending_printers_connected_card_label()
        # self.pending_printers.verify_pending_printers_connected_card_label_icon()
        self.pending_printers.verify_pending_printers_connected_card_title()
        self.pending_printers.verify_pending_printers_connected_card_description()
        self.pending_printers.verify_pending_printers_connected_card_printers_count()

    @pytest.mark.sanity
    def test_03_verify_pending_printers_table_search_functionality(self):
        #
        initial_serial_numbers = self.pending_printers.get_all_pending_printers_serial_number()
        initial_product_numbers = self.pending_printers.get_all_pending_printers_product_number()

        # Verify search by serial number
        search_serial_number = initial_serial_numbers[0]
        self.pending_printers.search_pending_printers(search_serial_number)
        self.pending_printers.verify_search_results_by_serial_number(search_serial_number)
        self.pending_printers.clear_pending_printers_search_results_box()

        # Verify search by product number
        search_product_number = initial_product_numbers[0]
        self.pending_printers.search_pending_printers(search_product_number)
        self.pending_printers.verify_search_results_by_product_number(search_product_number)
        self.pending_printers.clear_pending_printers_search_results_box()
        
        # Verify search by status
        search_status = self.pending_printers.get_all_pending_printers_status()[0]
        self.pending_printers.search_pending_printers(search_status)
        self.pending_printers.verify_search_results_by_status(search_status)
        self.pending_printers.clear_pending_printers_search_results_box()

        # Verify search by date added
        search_date_added = self.pending_printers.get_all_pending_printers_date_added()[0]
        self.pending_printers.search_pending_printers(search_date_added)
        self.pending_printers.verify_search_results_by_date_added(search_date_added)

    @pytest.mark.sanity
    def test_04_verify_error_case_search(self):
        # 
        self.pending_printers.search_pending_printers("%$iNVALID")
        self.pending_printers.verify_no_items_found()

    def test_05_verify_pending_printers_table_delete_button(self):
        #
        initial_serial_numbers = self.pending_printers.get_all_pending_printers_serial_number()
        self.pending_printers.verify_pending_printers_delete_button(displayed=False)
        self.pending_printers.click_pending_printers_checkbox()
        self.pending_printers.verify_pending_printers_delete_button(displayed=True)
        self.pending_printers.click_pending_printers_delete_button()

        self.pending_printers.verify_delete_confirmation_popup()
        self.pending_printers.click_delete_confirmation_popup_cancel_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        assert initial_serial_numbers == self.pending_printers.get_all_pending_printers_serial_number()
    
    def test_06_verify_pending_printers_no_of_items_selected_label(self):
        #
        # Verify the label text not displayed when no items are selected
        self.pending_printers.verify_pending_printers_no_of_items_selected_label(displayed=False)

        # Verify the label text when one item is selected
        self.pending_printers.click_pending_printers_checkbox()
        assert self.pending_printers.get_pending_printers_no_of_items_selected_label_count() == 1, "Selected items count is not 1 when one item is selected."

        # Verify the label text when all items are selected
        self.pending_printers.click_pending_printers_select_all_button()
        self.pending_printers.select_page_size("500")
        total_count = self.pending_printers.get_total_printers_items_count()
        assert self.pending_printers.get_pending_printers_no_of_items_selected_label_count() == total_count, "Selected items count is not equal to total items when all items are selected."

    def test_07_verify_pending_printers_select_all_button(self):
        #
        # Verify the select all button functionality
        self.pending_printers.verify_pending_printers_select_all_button(displayed=False)
        self.pending_printers.click_pending_printers_checkbox()
        self.pending_printers.verify_pending_printers_select_all_button(displayed=True)
        sleep(5)
        self.pending_printers.click_pending_printers_select_all_button()
        selected_count = self.pending_printers.get_pending_printers_no_of_items_selected_label_count()
        self.pending_printers.select_page_size("500")
        total_count = self.pending_printers.get_total_printers_items_count()
        assert selected_count == total_count, "Not all items are selected after clicking 'Select All' button."

        # Verify the unselect all button functionality
        self.pending_printers.click_pending_printers_unselect_all_button()
        self.pending_printers.verify_pending_printers_select_all_button(displayed=False)
        self.pending_printers.verify_pending_printers_no_of_items_selected_label(displayed=False)

    @pytest.mark.sanity
    def test_08_verify_pending_printers_column_option_popup_ui(self):
        #
        # Verify the gear button functionality
        self.pending_printers.click_pending_printers_gear_button()
        self.pending_printers.verify_column_options_popup_title()
        self.pending_printers.verify_column_options_popup_reset_to_default_button()
        self.pending_printers.verify_column_options_popup_cancel_button()
        self.pending_printers.verify_column_options_popup_save_button()

        # Verify the column options in the popup
        expected_options = ["Serial number", "Product number", "Status", "Date Added"]
        assert expected_options == self.pending_printers.get_column_options_popup_options()
    
    @pytest.mark.sanity
    def test_09_verify_pending_printers_column_option_save_functionality(self):
        #
        # Verify the save button functionality in the gear button popup
        self.pending_printers.click_pending_printers_gear_button()
        self.pending_printers.click_column_option("Product number")
        self.pending_printers.click_column_options_popup_save_button()

        # Verify the table reflects the changes
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_printers_table_column("Product number", displayed=False)

        # Revert the changes
        self.pending_printers.click_pending_printers_gear_button()
        self.pending_printers.click_column_option("Product number")
        self.pending_printers.click_column_options_popup_save_button()
        self.pending_printers.verify_printers_table_column("Product number")

    @pytest.mark.sanity
    def test_10_verify_pending_printers_column_option_cancel_functionality(self):
        #
        # Verify the cancel button functionality in the gear button popup
        self.pending_printers.click_pending_printers_gear_button()
        self.pending_printers.click_column_option("Product number")
        self.pending_printers.click_column_options_popup_cancel_button()

        # Verify the table does not reflect the changes
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_printers_table_column("Product Number")

    def test_11_verify_pagination(self):
        # 
        self.pending_printers.verify_all_page_size_options([5, 25, 50, 100, 500])
        self.pending_printers.verify_table_displaying_correctly(5, page=1)
        self.pending_printers.verify_table_displaying_correctly(25, page=1)
        self.pending_printers.verify_table_displaying_correctly(50, page=1)
        self.pending_printers.verify_table_displaying_correctly(100, page=1)
        self.pending_printers.verify_table_displaying_correctly(500, page=1)

    @pytest.mark.sanity
    def test_12_verify_pending_printers_filter_side_bar_ui(self):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_pending_printers_filter_button()
        self.pending_printers.click_pending_printers_filter_button()
        self.pending_printers.verify_pending_printers_filter_side_bar_title()
        self.pending_printers.verify_pending_printers_filter_side_bar_status_label()
        self.pending_printers.verify_pending_printers_filter_side_bar_clear_all_button_status("disabled")
        self.pending_printers.verify_pending_printers_filter_side_bar_done_button()
        self.pending_printers.click_pending_printers_filter_side_bar_done_button()
        self.pending_printers.verify_pending_printers_filter_side_bar_title(displayed=False)

    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Action needed", "Error", "Connected"])
    def test_13_verify_pending_printers_filter_functionality(self,filter_name):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_pending_printers_filter_button()
        self.pending_printers.click_pending_printers_filter_button()
        self.pending_printers.select_pending_printers_filter(filter_name)
        self.pending_printers.click_pending_printers_filter_side_bar_done_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_filter_in_pending_printers_table(filter_name)
    
    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Action needed", "Error", "Connected"])
    def test_14_verify_pending_printers_filter_count(self,filter_name):
        #
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.verify_pending_printers_filter_button()
        self.pending_printers.click_pending_printers_filter_button()
        self.pending_printers.select_pending_printers_filter(filter_name)
        sleep(5) #sleep added to wait for the filter count to update in the sidebar before fetching the count
        filter_popup_count = self.pending_printers.get_pending_printers_filter_count_in_filter_sidebar(filter_name)
        self.pending_printers.click_pending_printers_filter_side_bar_done_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

        self.pending_printers.verify_filter_in_pending_printers_table(filter_name)
        self.pending_printers.select_page_size("500")

        table_count = self.pending_printers.get_total_printers_items_count()
        assert filter_popup_count == table_count, f"Filter count in popup ({filter_popup_count}) does not match table count ({table_count})."

        #revert the changes
        self.pending_printers.click_pending_printers_filter_button()
        self.pending_printers.select_pending_printers_filter(filter_name)
        self.pending_printers.click_pending_printers_filter_side_bar_done_button()

    @pytest.mark.sanity
    def test_15_verify_pending_printers_filter_clear_all_button_functionality(self):
        #
        sleep(5)
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.select_page_size("500")
        table_count = self.pending_printers.get_total_printers_items_count()
        self.pending_printers.verify_pending_printers_filter_button()
        self.pending_printers.click_pending_printers_filter_button()

        # Verify the "Clear All" button is initially disabled
        self.pending_printers.verify_pending_printers_filter_side_bar_clear_all_button_status("disabled")

        # Select multiple filters
        self.pending_printers.select_pending_printers_filter("Action needed")
        self.pending_printers.select_pending_printers_filter("Error")
        self.pending_printers.verify_pending_printers_filter_side_bar_clear_all_button_status("enabled")

        # Click the "Clear All" button and verify its functionality
        self.pending_printers.click_pending_printers_filter_side_bar_clear_all_button()
        self.pending_printers.verify_pending_printers_filter_side_bar_clear_all_button_status("disabled")

        # Close the filter sidebar
        self.pending_printers.click_pending_printers_filter_side_bar_done_button()
        self.pending_printers.verify_pending_printers_filter_side_bar_title(displayed=False)
        self.pending_printers.select_page_size("500")
        assert table_count == self.pending_printers.get_total_printers_items_count(), "Table count does not match after clearing filters."