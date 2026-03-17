import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

class Test_04_Network_Category02_Proxies_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.serial_number = request.config.getoption("--proxy-device")
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]
        self.emulator_serial_number = self.account["emulator_settings_serial_number"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        if self.emulator_serial_number != "":
            self.serial_number = self.emulator_serial_number
        self.printers.search_printers(self.serial_number)
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        return self.printers.click_printers_details_page_policies_tab()

    def test_01_verify_wins_port_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        network_wins_port_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/nameResolverServices"
        response = get_api_response(self.stack,network_wins_port_uri)
        wins_port_status = response.json()["state"]["reported"]["cdmData"]["wins"]["winsPort"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="WINS Port",setting_card="wins-port",settings_value= wins_port_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("WINS Port")

    def test_02_verify_wins_registration_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Wins Registration API Status
        network_wins_registration_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/nameResolverServices"
        response = get_api_response(self.stack,network_wins_registration_uri)
        wins_reg_status = response.json()["state"]["reported"]["cdmData"]["wins"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="WINS Registration",setting_card="wins-registration",settings_value= wins_reg_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("WINS Registration")

    def test_03_verify_ws_discovery_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network WS-Discovery API Status
        network_ws_discovery_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/discoveryServices"
        response = get_api_response(self.stack,network_ws_discovery_uri)
        ws_discovery_status = response.json()["state"]["reported"]["cdmData"]["wsDiscovery"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Web Services Discovery",setting_card="ws-discovery",settings_value= ws_discovery_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Web Services Discovery")

    def test_04_verify_web_services_print_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network WS-Print API Status
        network_ws_print_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,network_ws_print_uri)
        web_services_status = response.json()["state"]["reported"]["cdmData"]["wsPrint"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Web Services Print",setting_card="ws-print",settings_value= web_services_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Web Services Print") 

    def test_05_verify_airprint_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

         # Get AirPrint API Status
        airprint_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,airprint_uri)
        airprint_status = response.json()["state"]["reported"]["cdmData"]["airPrint"]["enabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="AirPrint",setting_card="airprint",settings_value= airprint_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("AirPrint")   

    # AirPrint Fax or IPP Fax Out
    def test_06_verify_airprint_fax_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get AirPrint Fax API Status
        airprint_fax_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/fax/sendConfiguration"
        response = get_api_response(self.stack,airprint_fax_uri)
        airprint_fax_status = response.json()["state"]["reported"]["cdmData"]["ippFaxEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="AirPrint Fax",setting_card="airprint-fax",settings_value= airprint_fax_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("AirPrint Fax")

    def test_07_verify_tftp_configuration_file_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network TFTP Configuration File API Status
        network_tftp_config_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/jetdirectServices"
        response = get_api_response(self.stack,network_tftp_config_uri)
        tftp_config_status = response.json()["state"]["reported"]["cdmData"]["tftpEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="TFTP Configuration File",setting_card="tftp-cfg",settings_value= tftp_config_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("TFTP Configuration File")

    def test_08_verify_telnet_config_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Telnet API Status
        network_telnet_config_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/jetdirectServices"
        response = get_api_response(self.stack,network_telnet_config_uri)
        telnet_config_status = response.json()["state"]["reported"]["cdmData"]["telnetEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Telnet",setting_card="telnet",settings_value= telnet_config_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Telnet")

    def test_09_verify_ip_hostname_setting_in_overview_tab(self):
        #
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.search_printers(self.serial_number)
        printer_ip_hostname = self.printers.get_printers_ip_hostname_info()
        self.printers.click_first_entry_link()
        # Verify the ip hostname in device details overview tab
        self.printers.click_printers_details_overview_tab()
        assert printer_ip_hostname == self.printers.get_general_information_section_overview_tab_hostname()

    def test_10_verify_ipv4_address_setting_in_overview_tab(self):
        #
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.search_printers(self.serial_number)
        printer_ipv4_address = self.printers.get_printers_ipv4_address_info()
        self.printers.click_first_entry_link()
        # Verify the ip hostname in device details overview tab
        self.printers.click_printers_details_overview_tab()
        assert printer_ipv4_address == self.printers.get_general_information_section_overview_tab_ipv4_address()

    def test_11_verify_hp_jetadvantage_more_apps_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        #Verify HP JetAdvantage (More Apps) API Status 
        hp_jetadvantage_more_apps_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_api_response(self.stack,hp_jetadvantage_more_apps_uri)
        hp_jetadvantage = response.json()["state"]["reported"]["cdmData"]["webServices"]["hpJetAdvantage"]
        hp_jetadvantage_accountcreation = response.json()["state"]["reported"]["cdmData"]["webServices"]["accountCreation"]
        all_hp_jet_advantage_status = list((hp_jetadvantage, hp_jetadvantage_accountcreation))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="HP JetAdvantage (More Apps)",setting_card="hp-jet-adv",settings_value=all_hp_jet_advantage_status,category_type="Web Services")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("HP JetAdvantage (More Apps)")

    def test_12_verify_show_date_and_time_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Show Date and Time API Status
        show_date_and_time_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/controlpanel"
        response = get_api_response(self.stack,show_date_and_time_uri)
        show_date_and_time_status = response.json()["state"]["reported"]["cdmData"]["displayDateAndTime"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Show Date and Time",setting_card="show-date-time",settings_value=show_date_and_time_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Show Date and Time")