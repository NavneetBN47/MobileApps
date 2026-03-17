import pytest
import random
import logging
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate random device properties values
asset_number=random.randint(100,999)

class Test_03_WEX_Fleet_Management_Devices_Printer_Details(object):

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
        self.printer_serial_number = self.account["printer_serial_number"]

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
        self.printers.search_printers(self.printer_serial_number)
        return self.printers.verify_devices_printers_table_loaded()
    
    def test_01_verify_printer_details_properties_tab_options_expand_and_collapsed(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        # Verifying Copier widget expand and collapsed
        self.printers.verify_copier_accordion()
        self.printers.click_copier_accordion()
        self.printers.verify_copier_accordion_expanded()
        self.printers.click_copier_accordion()
        # Verifying Device widget expand and collapsed
        self.printers.verify_device_accordion() 
        self.printers.click_device_accordion()
        self.printers.verify_device_accordion_expanded() 
        self.printers.click_device_accordion()
        # Verifying EWS widget expand and collapsed
        self.printers.verify_ews_accordion()
        self.printers.click_ews_accordion()
        self.printers.verify_ews_accordion_expanded()
        self.printers.click_ews_accordion()
        # Verifying Network widget expand and collapsed
        self.printers.verify_network_accordion()
        self.printers.click_network_accordion()
        self.printers.verify_network_accordion_expanded()
        self.printers.click_network_accordion()
        # Verifying Security widget expand and collapsed
        self.printers.verify_security_accordion()
        self.printers.click_security_accordion()
        self.printers.verify_security_accordion_expanded()
        self.printers.click_security_accordion()
        # Verifying Supplies widget expand and collapsed
        self.printers.verify_supplies_accordion()
        self.printers.click_supplies_accordion()
        self.printers.verify_supplies_accordion_expanded()
        self.printers.click_supplies_accordion()
        # # Verifying Solutions widget expand and collapsed
        # self.printers.verify_solutions_accordion()
        # self.printers.click_solutions_accordion()
        # self.printers.verify_solutions_accordion_expanded()
        # self.printers.click_solutions_accordion()
        # Verifying Digital Sending widget expand and collapsed
        self.printers.verify_digital_sending_accordion()
        self.printers.click_digital_sending_accordion()
        self.printers.verify_digital_sending_accordion_expanded()
        self.printers.click_digital_sending_accordion()
        # Verifying Web Services widget expand and collapsed
        self.printers.verify_web_services_accordion()
        self.printers.click_web_services_accordion()
        self.printers.verify_web_services_accordion_expanded()
        self.printers.click_web_services_accordion()
        # Verifying Wireless widget expand and collapsed
        self.printers.verify_wireless_accordian()
        self.printers.click_wireless_accordion()
        self.printers.verify_wireless_accordion_expanded()
        self.printers.click_wireless_accordion()

    def test_02_verify_printers_details_page_anchor_list_functionality(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_anchor_list()
        anchor_list=self.printers.get_anchor_list_items()
        for anchor in anchor_list:
            self.printers.click_anchor_list_item(anchor)
            self.printers.verify_anchor_list_item_highlighted(anchor)
    
    def test_03_verify_printers_details_page_tab_is_highlighted(self):
        #
        self.printers.click_first_entry_link()
        self.printers.verify_devices_printers_details_page_details_breadcrumb()
        self.printers.click_printers_details_overview_tab()
        self.printers.verify_printer_details_tab_highlighted("Overview")
        self.printers.click_printers_details_page_properties_tab()
        self.printers.verify_printer_details_tab_highlighted("Properties")
        self.printers.click_printers_details_page_policies_tab()
        self.printers.verify_printer_details_tab_highlighted("Policies")
        self.printers.click_printers_details_page_hp_secure_fleet_manager_tab()
        self.printers.verify_printer_details_tab_highlighted("HP Secure Fleet Manager")
        self.printers.click_printers_details_page_hp_sds_event_log_tab()
        self.printers.verify_printer_details_tab_highlighted("Event Log")
    
    def test_04_verify_printers_details_page_properties_tab_anchor_list_functionality(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.verify_printers_details_properties_tab_anchor_list()
        properties_anchor_list=self.printers.get_printers_details_properties_tab_anchor_list_items()
        for property_anchor in properties_anchor_list:
            self.printers.click_printer_details_properties_tab_anchor_list_item(property_anchor)
            self.printers.verify_printer_details_properties_tab_anchor_list_item_highlighted(property_anchor)
        
    def test_05_verify_printers_details_page_policies_tab_anchor_list_functionality(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_policies_tab()
        self.printers.verify_printers_details_policies_tab_anchor_list()
        policies_anchor_list=self.printers.get_printers_details_policies_tab_anchor_list_items()
        for policy_anchor in policies_anchor_list:
            self.printers.click_printer_details_policies_tab_anchor_list_item(policy_anchor)
            sleep(5)
            self.printers.verify_printer_details_policies_tab_anchor_list_item_highlighted(policy_anchor)
    
    def test_06_verify_copier_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_copier_accordion()
        self.printers.verify_copier_accordion_expanded()
        expected_settings_list_in_copier_widgets = ["Color Copy Mode", "Copy Job Build", "Color Copy Mode with Auto", "Copy Background Cleanup", "Copy Contrast",
                                                    "Copy Darkness", "Copy Optimize Text/Picture", "Copy Paper Tray Selection", "Copy Sharpness", "Copy Stamps"]

        # Retrieve all settings in Copier widget
        actual_settings_list_in_copier_widgets = self.printers.get_property_tab_copier_category_setting_list_items()

        # Verify that the actual settings are present in the expected settings list
        assert all(item in expected_settings_list_in_copier_widgets for item in actual_settings_list_in_copier_widgets), "Not all actual settings are present in the expected settings list"

        # Verify the count of settings in Copier widget
        assert len(expected_settings_list_in_copier_widgets) >= len(actual_settings_list_in_copier_widgets), "The expected settings list is shorter than the actual settings list"

    def test_07_verify_device_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.verify_device_accordion_expanded()
        expected_settings_list_in_device_widgets = ["Asset Number","AutoSend", "Company Name", "Contact Person", "Control Panel Language", "Date/Time Format", "Default Media Size", 
                                                  "Default Media Type", "Device Location", "Device Name", "Duplex Binding", "Home Screen Customization - FutureSmart", "Manual Feed Prompt", 
                                                  "Online Solutions", "Outgoing Servers", "Override A4/Letter","Size / Type Prompt", "Sleep Delay", "Sleep Schedule", "Sleep Settings", 
                                                  "Time Zone/Daylight Saving", "Tray 1 Mode / Manual Feed", "Tray Administration", "Use Requested Tray", "Retain Temporary Print Jobs After Reboot",
                                                  "Temporary Job Storage Limit", "Display Network Address"]

        # Retrieve all settings in Device widget
        actual_settings_list_in_device_widgets = self.printers.get_property_tab_device_category_setting_list_items()

        # Verify that the actual settings are present in the expected settings list
        assert all(item in expected_settings_list_in_device_widgets for item in actual_settings_list_in_device_widgets), "Not all actual settings are present in the expected settings list"

        # Verify the count of settings in Device widget
        assert len(expected_settings_list_in_device_widgets) >= len(actual_settings_list_in_device_widgets), "The expected settings list is shorter than the actual settings list"

    def test_08_verify_embedded_web_server_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_ews_accordion()
        self.printers.verify_ews_accordion_expanded()
        expected_settings_list_in_ews_widgets = ["Embedded Web Server Language Settings", "Time Services"]
        # Retrieve all settings in EWS widget
        actual_settings_list_in_ews_widgets = self.printers.get_property_tab_ews_category_setting_list_items()

        # Verify that the actual settings are present in the expected settings list
        assert all(item in expected_settings_list_in_ews_widgets for item in actual_settings_list_in_ews_widgets), "Not all actual settings are present in the expected settings list"

        # Verify the count of settings in EWS widget
        assert len(expected_settings_list_in_ews_widgets) >= len(actual_settings_list_in_ews_widgets), "The expected settings list is shorter than the actual settings list"
        
    def test_09_verify_network_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_network_accordion()
        self.printers.verify_network_accordion_expanded()
        expected_settings_list_in_network_widgets = ["AirPrint Fax", "AirPrint Scan (eSCL/Webscan)", "AirPrint Secure Scan", "Bluetooth Low Energy (BLE)", 
                                                   "Configuration Precedence", "DHCPv4 FQDN compliance with RFC 4702", "DNS Server", "EWS Config", 
                                                   "FTP Printing", "IPv4 Information", "IPv6 Information", "Link Setting", "Upload CA Certificate", "Upload ID Certificate",
                                                   "Support Contact", "System Contact", "System Location", "Web Scan", "FIPS 140 Compliance Library", 
                                                   "TCP/IP Configuration Method"]

        # Retrieve all settings in Network widget
        actual_settings_list_in_network_widgets = self.printers.get_property_tab_network_category_setting_list_items()

        # Verify that the expected sublist is present in the actual list
        assert all(item in expected_settings_list_in_network_widgets for item in actual_settings_list_in_network_widgets), "Not all actual settings are present in the expected settings list"

        # Verify the count of settings in Network widget
        assert len(expected_settings_list_in_network_widgets) >= len(actual_settings_list_in_network_widgets), "The expected settings list is shorter than the actual settings list"

    def test_10_verify_security_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_security_accordion()
        self.printers.verify_security_accordion_expanded()
        expected_settings_list_in_security_widgets = ["802.1x Authentication", "802.1x Authentication(Wired)", "802.1x Authentication(Wireless)", "Access Control for Device Functions - FutureSmart 4", "Bootloader Password", 
                                                      "Cross-Origin Resource Sharing (CORS)", "Device Announcement Agent", "Digital Sending Service", "Embedded Web Server (EWS) Admin Password",
                                                      "Host USB Plug and Play", "HP Jetdirect XML Services", "LDAP Sign in Setup", "Printer Job Language (PJL) Password", "Remote Configuration Password",
                                                      "Restrict Color", "Service Access Code", "SNMP", "SNMPv1/v2", "SNMPv3", "SMB/CIFS (Shared Folder)", "Stored Data PIN Protection"]

        # Retrieve all settings in Security widget
        actual_settings_list_in_security_widgets = self.printers.get_property_tab_security_category_setting_list_items()

        # Verify that the expected sublist is present in the actual list        
        assert all(item in expected_settings_list_in_security_widgets for item in actual_settings_list_in_security_widgets), "Not all actual settings are present in the expected settings list"

        # Verify the count of settings in Security widget
        assert len(expected_settings_list_in_security_widgets) >= len(actual_settings_list_in_security_widgets), "The expected settings list is shorter than the actual settings list"

    def test_11_verify_supplies_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_supplies_accordion()
        self.printers.verify_supplies_accordion_expanded()
        expected_settings_list_in_supplies_widgets = ["Cartridge", "Cartridge Policy", "Cartridge Protection", "Cartridge Threshold - Black", "Cartridge Threshold - Cyan", "Cartridge Threshold - Magenta", "Cartridge Threshold - Yellow",
                                                      "Cartridge Very Low Action - Black", "Cartridge Very Low Action - Color", "Drum Threshold - Black", "Drum Threshold - Cyan", "Drum Threshold - Magenta", "Drum Threshold - Yellow",
                                                      "Toner Collection Unit Very Full Action", "Delay Very Low Message", "Fuser Kit Very Low Action", "Supply Low Alerts"]
        # Retrieve all settings in Supplies widget
        actual_settings_list_in_supplies_widgets = self.printers.get_property_tab_supplies_category_setting_list_items()

        # Verify that the expected sublist is present in the actual list
        assert all(item in expected_settings_list_in_supplies_widgets for item in actual_settings_list_in_supplies_widgets), "Not all actual settings are present in the expected settings list"

        # Verify the count of settings in Supplies widget
        assert len(expected_settings_list_in_supplies_widgets) >= len(actual_settings_list_in_supplies_widgets), "The expected settings list is shorter than the actual settings list"

    #Solution category is not available in the current version of WEX
    # def test_12_verify_solutions_category_settings_list_in_properties_tab(self):
    #     #
    #     self.printers.click_first_entry_link()
    #     self.printers.click_printers_details_page_properties_tab()
    #     self.printers.click_solutions_accordion()
    #     self.printers.verify_solutions_accordion_expanded()
    #     expected_settings_list_in_solutions_widgets = ["App Deployment"]
    #     # Retrieve all settings in p widget
    #     actual_settings_list_in_solutions_widgets = self.printers.get_property_tab_solutions_category_setting_list_items()

    #     # Verify that the expected sublist is present in the actual list
    #     assert all(item in expected_settings_list_in_solutions_widgets for item in actual_settings_list_in_solutions_widgets), "Not all actual settings are present in the expected settings list"

    #     # Verify the count of settings in Solutions widget
    #     assert len(expected_settings_list_in_solutions_widgets) >= len(actual_settings_list_in_solutions_widgets), "The expected settings list is shorter than the actual settings list"

    def test_13_verify_digital_sending_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_digital_sending_accordion()
        self.printers.verify_digital_sending_accordion_expanded()
        expected_settings_list_in_digital_sending_widgets = ["Email Address/Message Settings", "Email Scan Settings", "Network Folder Notification Settings",
                                                             "Network Folder File Settings", "Save to Network Folder","Save to SharePoint","Send to Email",
                                                             "Email File Settings", "Allow Access to LDAP Address Book", "Email Notification Settings"]

        # Retrieve all settings in Digital Sending widget
        actual_settings_list_in_digital_sending_widgets = self.printers.get_property_tab_digital_sending_category_setting_list_items()

        # Verify that the expected sublist is present in the actual list
        assert all(item in expected_settings_list_in_digital_sending_widgets for item in actual_settings_list_in_digital_sending_widgets), "Not all expected settings are present in the actual settings list"

        # Verify the count of settings in Digital Sending widget
        assert len(expected_settings_list_in_digital_sending_widgets) >= len(actual_settings_list_in_digital_sending_widgets), "The expected settings list is shorter than the actual settings list"

    def test_14_verify_web_services_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_web_services_accordion()
        self.printers.verify_web_services_accordion_expanded()
        expected_settings_list_in_web_services_widgets = ["HP Web Services", "Proxy Server", "Smart Cloud Print"]
        # Retrieve all settings in Web Services widget
        actual_settings_list_in_web_services_widgets = self.printers.get_property_tab_web_services_category_setting_list_items()

        # Verify that the expected sublist is present in the actual list
        assert all(item in expected_settings_list_in_web_services_widgets for item in actual_settings_list_in_web_services_widgets), "Not all expected settings are present in the actual settings list"

        # Verify the count of settings in Web Services widget
        assert len(expected_settings_list_in_web_services_widgets) >= len(actual_settings_list_in_web_services_widgets), "The expected settings list is shorter than the actual settings list"

    def test_15_verify_wireless_category_settings_list_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_wireless_accordion()
        self.printers.verify_wireless_accordion_expanded()
        expected_settings_list_in_wireless_widgets = ["Wi-Fi Direct"]
        # Retrieve all settings in Wireless widget
        actual_settings_list_in_wireless_widgets = self.printers.get_property_tab_wireless_category_setting_list_items()

        # Verify that the expected sublist is present in the actual list
        assert all(item in expected_settings_list_in_wireless_widgets for item in actual_settings_list_in_wireless_widgets), "Not all expected settings are present in the actual settings list"

        # Verify the count of settings in Wireless widget
        assert len(expected_settings_list_in_wireless_widgets) >= len(actual_settings_list_in_wireless_widgets), "The expected settings list is shorter than the actual settings list"

    def test_16_verify_show_editable_items_only_functionality_in_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.verify_printers_details_properties_tab_anchor_list()
        initial_anchor_list = self.printers.get_printers_details_properties_tab_anchor_list_items()

        # Verify the updated anchor list is different from the initial anchor list
        self.printers.click_show_editable_items_only_radio_button()

        updated_anchor_list = self.printers.get_printers_details_properties_tab_anchor_list_items()

        assert initial_anchor_list != updated_anchor_list

        # Verify the length of the updated anchor list
        assert len(updated_anchor_list) != len(initial_anchor_list)

    # def test_17_verify_editable_settings_in_device_category_from_properties_tab(self):
    #     #
    #     self.printers.click_first_entry_link()
    #     self.printers.click_printers_details_page_properties_tab()
    #     self.printers.verify_printers_details_properties_tab_anchor_list()
    #     self.printers.click_show_editable_items_only_radio_button()

    #     self.printers.click_device_accordion()
    #     actual_setting = self.printers.get_property_tab_device_category_setting_list_items()

    #     self.printers.verify_edit_button_from_settings_list_in_properties_tab("outgoing-servers")

    @pytest.mark.skip(reason="Skipping temporarily")
    def test_18_verify_editable_settings_in_network_category_from_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_show_editable_items_only_radio_button()

        self.printers.click_network_accordion()
        actual_setting = self.printers.get_property_tab_network_category_setting_list_items()

        self.printers.verify_edit_button_from_settings_list_in_properties_tab("ca-certificate")
        self.printers.verify_edit_button_from_settings_list_in_properties_tab("id-certificate")

    def test_19_verify_editable_settings_in_security_category_from_properties_tab(self):
        #
        self.printers.click_first_entry_link()
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_show_editable_items_only_radio_button()

        self.printers.click_security_accordion()
        actual_setting = self.printers.get_property_tab_security_category_setting_list_items()

        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("dot1x-authentication")
        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("ews-password")
        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("ldap-signin-setup")
        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("service-access-code")
        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("snmp-v1-v2")
        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("snmp-v3")
        # self.printers.verify_edit_button_from_settings_list_in_properties_tab("pjl-password")
        self.printers.verify_edit_button_from_settings_list_in_properties_tab("bootloader-password")

    #Solution category is not available in the current version of WEX
    # def test_20_verify_editable_settings_in_solutions_category_from_properties_tab(self):
    #     #
    #     self.printers.click_first_entry_link()
    #     self.printers.click_printers_details_page_properties_tab()
    #     self.printers.click_show_editable_items_only_radio_button()

    #     self.printers.click_solutions_accordion()
    #     actual_setting = self.printers.get_property_tab_solutions_category_setting_list_items()

    #     self.printers.verify_edit_button_from_settings_list_in_properties_tab("web-app-deployment")

    def test_21_verify_compliance_status_widget_run_now_button_functionality(self):
        #
        self.printers.click_search_clear_button()
        self.printers.search_printers(self.printer_serial_number)
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        self.printers.verify_printers_details_policies_tab_compliance_status_widget_title()
        sleep(7)
        if self.printers.verify_compliance_status_widget_run_now_button_is_enabled():
            self.printers.click_compliance_status_widget_run_now_button()
            self.printers.check_policy_started_to_check_compliance_bottom_toast()
            self.printers.dismiss_toast()
        else:
            if self.printers.verify_compliance_status_widget_no_items_found_message():
                self.printers.add_settings_in_device_specific_policy_tab(setting_name="Asset Number",setting_card="asset-number",settings_value=asset_number,category_type="Devices")
                self.printers.verify_compliance_status_widget_run_now_button_is_enabled()
                self.printers.click_compliance_status_widget_run_now_button()
                self.printers.check_policy_started_to_check_compliance_bottom_toast()
                self.printers.dismiss_toast()

                self.printers.remove_settings_in_device_specific_policy_tab("Asset Number")