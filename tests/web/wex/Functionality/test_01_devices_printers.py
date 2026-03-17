import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_01_Workforce_Devices_Printers(object):

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
        self.printers.click_printers_group("All")
        return self.printers.verify_devices_printers_table_loaded()
    
    def test_01_verify_export_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128873
        self.printers.export_devices()

    def test_02_verify_export_devices_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128873
        self.printers.click_printers_export_all_btn()
        self.printers.verify_export_devices_popup_title()
        self.printers.verify_export_devices_popup_description()
        self.printers.verify_export_devices_popup_select_file_type_dropdown()
        self.printers.verify_export_devices_popup_cancel_button()
        self.printers.verify_export_devices_popup_export_button()
        self.printers.click_export_devices_popup_cancel_button()

    def test_03_verify_export_devices_popup_select_file_type_dropdown_option(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128873
        file_type_option=["XLSX","CSV"]
        self.printers.click_printers_export_all_btn()
        self.printers.click_export_devices_popup_select_file_type_dropdown()
        sleep(3)  # Adding sleep to allow dropdown options to load properly
        assert file_type_option == self.printers.get_select_file_type_dropdown_options()

    def test_04_verify_printers_floating_menu_options(self):
        #
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()

        self.printers.click_printers_checkbox()

        self.printers.verify_printers_add_btn()
        self.printers.verify_printers_export_all_btn()
        self.printers.verify_move_to_group_button()
        self.printers.verify_configure_printers_button()
        self.printers.verify_download_app_configuration_button()

    def test_05_verify_add_printers_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128872
        self.printers.click_printers_add_btn()
        self.printers.verify_add_printers_popup_title()
        self.printers.verify_add_printers_popup_description()
        self.printers.verify_add_printers_popup_close_button()
        self.printers.verify_add_printers_popup_cancel_button()
        self.printers.verify_add_printers_popup_cloud_connect_button()
        self.printers.verify_add_printers_popup_print_fleet_proxy_connect_button()

        self.printers.verify_add_printers_popup_cloud_connect_button_name()
        self.printers.verify_add_printers_popup_cloud_connect_button_description()

        self.printers.verify_add_printers_popup_print_fleet_proxy_connect_button_name()
        self.printers.verify_add_printers_popup_print_fleet_proxy_connect_button_description()

        self.printers.click_add_printers_popup_close_button()
        self.printers.verify_devices_printers_table_loaded()

    def test_06_verify_add_printers_enter_manually_popup_ui(self):
        #
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.verify_add_printers_enter_manually_popup_title()
        self.printers.verify_add_printers_enter_manually_popup_description()
        self.printers.verify_add_printers_cloud_connect_enter_manually_btn_title()
        self.printers.verify_add_printers_cloud_connect_enter_manually_btn_desc()
        self.printers.verify_add_printers_cloud_connect_enter_manually_btn()
        self.printers.verify_add_printers_enter_manually_popup_close_button()
        self.printers.verify_add_printers_enter_manually_popup_cancel_button()

        # Add Printers - Enter Manually Popup "Back" button functioanlity
        self.printers.click_add_printers_print_fleet_proxy_popup_back_button()
        self.printers.verify_add_printers_popup_description()

        # Add Printers - Enter Manually Popup "Close" button functioanlity
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.click_add_printers_enter_manually_popup_close_button()
        self.printers.verify_devices_printers_table_loaded()

        # Add Printers - Enter Manually Popup "Cancel" button functioanlity
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.click_add_printers_enter_manually_popup_cancel_button()
        self.printers.verify_devices_printers_table_loaded()

    def test_07_verify_add_printers_enter_manually_printers_details_popup_ui(self):
        #
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.click_add_printers_cloud_connect_enter_manually_btn()
        self.printers.verify_add_printers_enter_manually_popup_title()
        self.printers.verify_add_printers_enter_manually_popup_printer_details_desc()
        self.printers.verify_add_printers_printer1_field_name_title()
        self.printers.verify_add_printers_printer1_field_serial_number_label()
        self.printers.verify_add_printers_printer1_field_serial_number_textbox()
        self.printers.verify_add_printers_printer1_field_product_number_label()
        self.printers.verify_add_printers_printer1_field_product_number_textbox()
        self.printers.verify_add_printers_printer1_field_delete_btn("disabled")
        self.printers.verify_add_another_printer_link()

        self.printers.verify_add_printers_enter_manually_details_popup_back_button()
        self.printers.verify_add_printers_enter_manually_details_popup_close_button()
        self.printers.verify_add_printers_enter_manually_details_popup_submit_button()
        self.printers.verify_add_printers_enter_manually_details_popup_cancel_button()

        # Add Printers - Cloud Connect Printers Details Popup "Back" button functioanlity
        self.printers.click_add_printers_enter_manually_details_popup_back_button()
        self.printers.verify_add_printers_enter_manually_popup_description()

        # Add Printers - Cloud Connect Printers Details Popup "Close" button functioanlity
        self.printers.click_add_printers_cloud_connect_enter_manually_btn()
        self.printers.click_add_printers_enter_manually_details_popup_close_button()
        self.printers.verify_devices_printers_table_loaded()

        # Add Printers - Cloud Connect Printers Details Popup "Cancel" button functioanlity without entering any serial or product number values
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.click_add_printers_cloud_connect_enter_manually_btn()
        self.printers.click_add_printers_enter_manually_details_popup_cancel_button()
        self.printers.verify_devices_printers_table_loaded()

    def test_08_verify_add_printer_functionality_multiple_printers_fields_ui(self):
        #
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.click_add_printers_cloud_connect_enter_manually_btn()
        self.printers.click_add_another_printer_link()

        self.printers.verify_add_printers_printer2_field()
        self.printers.verify_add_printers_printer2_field_name_title()
        self.printers.verify_add_printers_printer2_field_serial_number_label()
        self.printers.verify_add_printers_printer2_field_serial_number_textbox()
        self.printers.verify_add_printers_printer2_field_product_number_label()
        self.printers.verify_add_printers_printer2_field_product_number_textbox()
        self.printers.verify_add_printers_printer2_field_delete_btn("enabled")

        self.printers.click_add_printers_printer2_field_delete_btn()
        self.printers.verify_add_printers_printer2_field(displayed=False)

    def test_09_verify_add_printers_discard_changes_popup_ui(self):
        #
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_cloud_connect_button()
        self.printers.click_add_printers_cloud_connect_enter_manually_btn()
        self.printers.enter_add_printers_printer1_field_serial_number("1234567890")
        self.printers.enter_add_printers_printer1_field_product_number("123456")
        self.printers.click_add_printers_enter_manually_details_popup_cancel_button()

        # Discard Changes Popup UI
        self.printers.verify_add_printers_discard_changes_popup_title()
        self.printers.verify_add_printers_discard_changes_popup_description()
        self.printers.verify_add_printers_discard_changes_popup_close_button()
        self.printers.verify_add_printers_discard_changes_popup_go_back_button()
        self.printers.verify_add_printers_discard_changes_popup_discard_button()
        self.printers.click_add_printers_discard_changes_popup_go_back_button()

        # Verify the changes are not discarded
        self.printers.verify_add_printers_enter_manually_popup_title()
        assert self.printers.get_add_printers_printer1_field_serial_number() == "1234567890", \
            "The serial number field is not retaining the entered value after clicking 'Go Back' button."
        assert self.printers.get_add_printers_printer1_field_product_number() == "123456", \
            "The product number field is not retaining the entered value after clicking 'Go Back' button."

    def test_10_verify_add_printers_connect_through_print_fleet_proxy_popup_ui(self):
        #
        self.printers.click_printers_add_btn()
        self.printers.click_add_printers_popup_print_fleet_proxy_connect_button()
        self.printers.verify_add_printers_print_fleet_proxy_popup_title()
        self.printers.verify_add_printers_print_fleet_proxy_popup_description()
        self.printers.verify_add_printers_print_fleet_proxy_label()
        self.printers.verify_add_printers_print_fleet_proxy_version()
        self.printers.verify_add_printers_print_fleet_proxy_download_link()
        self.printers.verify_add_printers_print_fleet_proxy_done_button()

        # Verify Back button functionality in Print Fleet Proxy Popup
        self.printers.click_add_printers_print_fleet_proxy_popup_back_button()
        self.printers.verify_add_printers_popup_title()

        # verify Done button functionality in Print Fleet Proxy Popup
        self.printers.click_add_printers_popup_print_fleet_proxy_connect_button()
        self.printers.click_add_printers_print_fleet_proxy_done_button()
        self.printers.verify_devices_printers_table_loaded()   
    
    @pytest.mark.skip(reason="Skipping test case temporarily")
    def test_11_verify_configure_device_show_selected_items_toggle_button_functionality(self):
        #
        self.printers.click_printers_checkbox()
        self.printers.click_configure_printers_button()

        # Verify Configure Device Pop-up
        self.printers.verify_configure_device_popup_title()

        # Verify and toggle the 'Show Selected Items Only' button
        self.printers.verify_configure_device_popup_show_selected_items_only_toggle_button()
        self.printers.click_configure_device_popup_show_selected_items_only_toggle_button()
        self.printers.verify_configure_device_popup_show_selected_items_only_toggle_button_status("enabled")
        self.printers.verify_configure_device_popup_no_settings_selected_msg()
        self.printers.verify_configure_device_popup_configure_button(disabled=True)
        self.printers.click_configure_device_popup_show_selected_items_only_toggle_button()
        self.printers.verify_configure_device_popup_show_selected_items_only_toggle_button_status("disabled")

        # Enable device category settings 
        self.printers.search_configure_device_popup_category_setting("Proxy")
        self.printers.verify_configure_device_popup_category_option_displayed("Web Services")
        self.printers.select_configure_device_popup_device_category_outgoing_servers_setting()
        self.printers.click_configure_device_popup_search_txtbox_clear_button()

        # Verify the 'Show Selected Items Only' button functionality after enabling a setting
        self.printers.click_configure_device_popup_show_selected_items_only_toggle_button()
        self.printers.verify_configure_device_popup_show_selected_items_only_toggle_button_status("enabled")
        self.printers.verify_configure_device_popup_category_option_displayed("Web Services")
        self.printers.verify_configure_device_popup_configure_button(disabled=False)
        
    def test_12_verify_configure_device_popup_search_functionality(self):
        #
        self.printers.click_printers_checkbox()
        self.printers.click_configure_printers_button()

        # Verify Configure Device Pop-up
        self.printers.verify_configure_device_popup_title()

        # Verify the search functionality
        self.printers.verify_configure_device_popup_search_txtbox()
        self.printers.search_configure_device_popup_device_settings("Password")
        self.printers.verify_configure_device_popup_search_results("Password")
        self.printers.click_configure_device_popup_search_txtbox_clear_button()

        self.printers.search_configure_device_popup_device_settings("Noresult")
        self.printers.verify_configure_device_popup_no_settings_found_message("All")
        self.printers.click_configure_device_popup_search_txtbox_clear_button()

    def test_13_verify_no_settings_found_message_based_on_category_selection(self):
        #
        self.printers.click_printers_checkbox()
        self.printers.click_configure_printers_button()

        # Verify Configure Device Pop-up
        self.printers.verify_configure_device_popup_title()

        # Retrieve all available category names dynamically
        category_names = self.printers.get_configure_device_popup_category_options()

        # Iterate over each category name and verify the no settings found message
        for category_name in category_names:
            self.printers.select_configure_device_popup_category_option(category_name)
            self.printers.search_configure_device_popup_device_settings("Noresult")
            self.printers.verify_configure_device_popup_no_settings_found_message(category_name)
            self.printers.click_configure_device_popup_search_in_all_button()
            self.printers.verify_configure_device_popup_no_settings_found_message("All")
            self.printers.click_configure_device_popup_search_txtbox_clear_button()