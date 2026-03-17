import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

class Test_03_Network_Category01_Proxies_Settings(object):

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

    def test_01_verify_web_scan_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
        
        # Get Network airprint scan and secure scan API Status
        airprint_scan_and_secure_scan_config_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/networkScanServices"
        response = get_api_response(self.stack,airprint_scan_and_secure_scan_config_uri)
        airprint_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCL"]
        airprint_secure_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCLSecure"]
        all_scan_and_secure_status = list((airprint_scan_status,airprint_secure_scan_status))
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Web Scan",setting_card="web-scan",settings_value= all_scan_and_secure_status, category_type="Network")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Web Scan")

    def test_02_verify_bonjour_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Bonjour API Status
        network_bonjour_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/discoveryServices"
        response = get_api_response(self.stack,network_bonjour_uri)
        bonjour_status = response.json()["state"]["reported"]["cdmData"]["bonjour"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Bonjour",setting_card="bonjour",settings_value= bonjour_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Bonjour")

    def test_03_verify_ipp_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Internet Print Protocol (IPP) API Status
        network_ipp_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,network_ipp_uri)
        ipp_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ipp"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="(IPP)",setting_card="ipp",settings_value= ipp_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("(IPP)")

    def test_04_verify_ipps_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Secure Internet Print Protocol (IPPS) API Status
        network_ipps_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,network_ipps_uri)
        ipps_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ippSecure"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Secure Internet Print Protocol",setting_card="ipps",settings_value= ipps_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Secure Internet Print Protocol")

    def test_05_verify_add_network_settings_lpd_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network LPD API Status
        network_lpd_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,network_lpd_uri)
        lpd_status = response.json()["state"]["reported"]["cdmData"]["lpdPrint"]["enabled"]
    
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Line Printer Daemon",setting_card="lpd-lpr",settings_value=lpd_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Line Printer Daemon")

    def test_06_verify_add_network_settings_llmnr_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Link-Local Multicast Name Resolution Protocol (LLMNR) API Status
        network_llmnr_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/nameResolverServices"
        response = get_api_response(self.stack,network_llmnr_uri)
        llmnr_status = response.json()["state"]["reported"]["cdmData"]["llmnr"]["enabled"]
    
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="LLMNR",setting_card="llmnr",settings_value=llmnr_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("LLMNR")
    
    def test_07_verify_add_network_settings_slp_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network SLP API Status
        network_slp_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/discoveryServices"
        response = get_api_response(self.stack,network_slp_uri)
        slp_status = response.json()["state"]["reported"]["cdmData"]["slp"]["enabled"]
    
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="SLP",setting_card="slp",settings_value=slp_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("SLP")

    def test_08_verify_add_network_settings_9100_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Standard TCP/IP Printing (P9100) API Status
        network_9100_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,network_9100_uri)
        tcpipprint_status = response.json()["state"]["reported"]["cdmData"]["port9100"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="9100",setting_card="tcpip-print",settings_value=tcpipprint_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("9100")

    