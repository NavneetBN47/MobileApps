import pytest
import random
import logging
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate random device properties values
asset_number=random.randint(100,999)

class Test_06_Workforce_Devices_Printer_Details(object):

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
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
            self.serial_number = self.account["ldk_printer_details_serial_number"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]
            self.serial_number = self.account["printer_serial_number"]

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
        sleep(5)
        self.printers.search_printers(self.serial_number)
        return self.printers.verify_devices_printers_table_loaded()

    @pytest.mark.sanity
    def test_01_verify_printers_details_page_navigation(self):
        # 
        self.printers.verify_devices_printers_table_loaded()
        entry_detail = self.printers.get_printers_detail_info()[0]  # Get first entry from table
        self.printers.click_first_entry_link()
        self.printers.verify_devices_printers_details_page_devices_breadcrumb()
        details_page_info = self.printers.verify_printers_details_info()
        
        # Compare only the common keys between table and details page
        for key in details_page_info.keys():
            if key in entry_detail:
                assert entry_detail[key] == details_page_info[key], f"Mismatch for {key}: table='{entry_detail[key]}' vs details='{details_page_info[key]}'"

    def test_02_verify_printers_details_page_breadcrumb_and_its_navigation(self):
        #
        self.printers.click_first_entry_link()
        # Verify the breadcrumb  on the printers details page
        self.printers.verify_devices_printers_details_page_devices_breadcrumb()

        # Verify the printers page URL
        self.printers.verify_devices_printers_details_page_url(self.stack)

        # Verify the navigation to the devices page from the printers details page.
        self.printers.click_devices_printers_details_page_devices_breadcrumb()
        self.printers.verify_devices_printers_table_loaded()

    @pytest.mark.sanity
    def test_03_verify_printers_details_page_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_devices_printers_details_page_details_breadcrumb()
        self.printers.verify_printers_details_page_printer_details_info_section()
        self.printers.verify_printers_details_info_section_supplies_chart()
        self.printers.verify_printers_details_page_overview_tab()
        self.printers.verify_printers_details_page_properties_tab()
        self.printers.verify_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.verify_printers_details_page_anchor_list()

    @pytest.mark.sanity
    def test_04_verify_printers_details_page_printer_info_section_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_info_section_printer_title()
        self.printers.verify_printer_details_info_section_expand_button()
        self.printers.verify_printers_details_page_printer_type_label()
        self.printers.verify_printers_details_info_section_printer_image()
        self.printers.verify_printers_details_info_section_printer_friendly_name()
        self.printers.verify_printers_details_info_section_printer_location()
        # self.printers.verify_printers_details_info_section_printer_status_title()
        # self.printers.verify_printers_details_info_section_printer_status()
        self.printers.verify_printers_details_info_section_printer_status_updated_title()
        self.printers.verify_printers_details_info_section_printer_status_updated_date_and_time()
        self.printers.verify_printers_details_info_section_printer_connectivity_title()
        self.printers.verify_printers_details_info_section_printer_connectivity_status()
        # self.printers.verify_printers_details_info_section_printer_status_message_title()
        # self.printers.verify_printers_details_info_section_printer_status_message()

    @pytest.mark.sanity
    def test_05_verify_printers_details_info_section_supplies_chart_ui(self):
        #
        self.printers.click_first_entry_link()
        if self.printers.verify_printers_details_info_section_supplies_chart() is True:
            # self.printers.verify_printers_details_supplies_chart_start_scroll_button()
            self.printers.verify_printers_details_supply_chart_ink_cartridges_tab()
            self.printers.verify_printers_details_supply_chart_printhead_tab()
            self.printers.verify_printers_details_supply_chart_media_tab()
            self.printers.verify_printers_details_supply_chart_other_supplies_tab()
            # self.printers.verify_printers_details_supplies_chart_end_scroll_button()
            self.printers.verify_printers_details_supplies_chart_estimated_supplies_label()
            self.printers.verify_printers_details_supplies_chart_ink_cartridges_chart()
    
    @pytest.mark.sanity
    def test_06_verify_printer_details_properties_tab_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.verify_devices_printers_details_page_properties_tab_url(self.stack)
        self.printers.verify_copier_accordion()
        self.printers.verify_device_accordion()
        self.printers.verify_digital_sending_accordion()
        self.printers.verify_ews_accordion()
        self.printers.verify_network_accordion()
        self.printers.verify_security_accordion()
        self.printers.verify_supplies_accordion()
        # self.printers.verify_solutions_accordion()
        self.printers.verify_web_services_accordion()
        self.printers.verify_wireless_accordian()

    @pytest.mark.sanity
    def test_07_verify_printer_details_hp_secure_fleet_manager_tab_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.click_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.verify_devices_printers_details_page_hp_secure_fleet_manager_tab_url(self.stack)
        self.printers.verify_hp_secure_fleet_manager_widget_reports_dropdown()
        self.printers.verify_hp_secure_fleet_manager_tab_export_as_pdf_button()
        self.printers.verify_hp_secure_fleet_manager_tab_no_reports_selected_icon()
        self.printers.verify_hp_secure_fleet_manager_tab_no_reports_selected_message()
        self.printers.verify_hp_secure_fleet_manager_tab_note_message()
    
    @pytest.mark.sanity
    def test_08_verify_printer_details_overview_tab_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_overview_tab()
        self.printers.verify_printer_details_general_information_section()
        self.printers.verify_printer_details_connectivity_type_section()
        self.printers.verify_printer_details_general_information_section_title()
        self.printers.verify_printer_details_connectivity_type_section_title()
        self.printers.verify_printer_details_general_information_section_expanded()
        self.printers.verify_printer_details_connectivity_type_section_expanded()

    @pytest.mark.sanity
    def test_09_verify_printer_details_overview_tab_general_information_section_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printer_details_general_information_section()
        self.printers.verify_general_information_section_asset_number_title()
        self.printers.verify_general_information_section_asset_number()
        self.printers.verify_general_information_section_device_group_title()
        self.printers.verify_general_information_section_device_group()
        self.printers.verify_general_information_section_date_added_title()
        self.printers.verify_general_information_section_date_added()
        self.printers.verify_general_information_section_firmware_version_title()
        self.printers.verify_general_information_section_firmware_version()
        self.printers.verify_general_information_section_serial_number_title()
        self.printers.verify_general_information_section_serial_number()

    @pytest.mark.sanity
    def test_10_verify_printer_details_connectivity_type_section(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printer_details_connectivity_type_section()
        self.printers.verify_printer_details_connectivity_type_section_title()
        if self.printers.verify_printer_details_connectivity_type_section_expanded() is False:
            self.printers.click_printer_details_connectivity_type_section()
 
        self.printers.verify_connectivity_type_section_printer_connectivity_name()
        self.printers.verify_connectivity_type_section_printer_connectivity_description()
       
        printer_type = self.printers.get_connectivity_type_section_printer_connectivity_type()
        if printer_type != "Cloud":
            self.printers.verify_connectivity_type_section_printer_connectivity_status()
            self.printers.click_connectivity_type_section_proxy_view_details_link()
            self.print_proxies.verify_print_proxies_table_data_load()
            self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
    
    @pytest.mark.sanity
    @pytest.mark.parametrize('report_name', ["assessment", "remediation"])
    def test_11_verify_fleet_manager_tab_export_reports(self, report_name):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.click_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.select_report(report_name)
        self.printers.verify_device_report_type(report_name)
        self.printers.verify_device_report_description()
        self.printers.click_hp_secure_fleet_manager_tab_export_as_pdf_button()

    @pytest.mark.sanity
    def test_12_verify_fleet_manager_policies_tab_general_information_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        self.printers.verify_devices_printers_details_page_policies_tab_url(self.stack)

        # Verify Policies - Compliance Status Widget UI
        self.printers.verify_printers_details_policies_tab_compliance_status_widget()
        self.printers.verify_printers_details_policies_tab_compliance_status_widget_title()
        self.printers.verify_compliance_status_widget_run_now_button()
        self.printers.verify_compliance_status_widget_expanded()
        self.printers.click_compliance_status_widget()
        self.printers.verify_compliance_status_widget_collapsed()

        # Verify Policies - Policy Status Widget UI
        self.printers.verify_printers_details_policies_tab_policy_widget()
        self.printers.verify_printers_details_policies_tab_edit_button()
        self.printers.verify_printers_details_policies_tab_policy_widget_collapsed()
        self.printers.click_policy_widget()
        sleep(5)
        self.printers.verify_printers_details_policies_tab_policy_widget_expand_button()

    @pytest.mark.sanity
    def test_13_verify_printer_details_hp_sds_event_log_tab_ui(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_hp_sds_event_log_tab()
        self.printers.verify_devices_printers_details_page_hp_sds_event_log_tab_url(self.stack)
        self.printers.verify_hp_sds_event_log_tab_event_log_title()
        self.printers.verify_hp_sds_event_log_tab_event_log_description()

    @pytest.mark.sanity
    @pytest.mark.parametrize('report_name', ["assessment", "remediation"])
    def test_14_verify_fleet_manager_tab_report_content_can_be_expanded_and_collapsed(self,report_name):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.click_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.select_report(report_name)
        self.printers.verify_report_content_expanded()
        self.printers.click_report_content()
        self.printers.verify_report_content_collapsed()
        self.printers.click_report_content()
        self.printers.verify_report_content_expanded()