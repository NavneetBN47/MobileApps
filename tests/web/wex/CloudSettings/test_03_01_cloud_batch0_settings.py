import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

#Generate random device properties values
device_name="device_name"+str(random.randint(1,99))
support_contact="support_user"+str(random.randint(1,99))
system_location="system_location"+str(random.randint(1,99))
system_contact="system_contact"+str(random.randint(1,99))
asset_number=random.randint(100,999)
company_name="company"+str(random.randint(1,99))
contact_person="user"+str(random.randint(1,99))
device_location="location"+str(random.randint(1,99))

class Test_03_01_Workforce_Batch0_CloudSettings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.pending_printers = self.fc.fd["devices_pendingprinters"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]
        self.cloud_settings_device_serial_number = self.account["cloud_settings_serial_number"]

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
        if self.cloud_settings_device_serial_number != "":
            self.serial_number = self.cloud_settings_device_serial_number
        self.printers.search_printers(self.serial_number)
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        return self.printers.click_printers_details_page_policies_tab()

    # Cloud Batch 0 Settings

    def test_01_verify_add_network_settings_slp_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network SLP API Status
        network_slp_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/discoveryServices"
        response = get_cloud_api_response(self.stack,network_slp_uri)
        slp_status = response.json()["state"]["reported"]["cdmData"]["slp"]["enabled"]
    
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="SLP",setting_card="slp",settings_value=slp_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("SLP")

    def test_02_verify_ipv4_multicast_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        #Get IPV4 Multicast Settings Setting API Status
        ipv4_multicast_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_cloud_api_response(self.stack, ipv4_multicast_uri)
        ipv4_multicast_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["multicastEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="IPv4 Multicast",setting_card="ipv4-multicast",settings_value= ipv4_multicast_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("IPv4 Multicast")

    def test_03_verify_add_network_settings_llmnr_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Link-Local Multicast Name Resolution Protocol (LLMNR) API Status
        network_llmnr_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/nameResolverServices"
        response = get_cloud_api_response(self.stack,network_llmnr_uri)
        llmnr_status = response.json()["state"]["reported"]["cdmData"]["llmnr"]["enabled"]
    
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="LLMNR",setting_card="llmnr",settings_value=llmnr_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("LLMNR")

    def test_04_verify_ws_discovery_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network WS-Discovery API Status
        network_ws_discovery_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/discoveryServices"
        response = get_cloud_api_response(self.stack,network_ws_discovery_uri)
        ws_discovery_status = response.json()["state"]["reported"]["cdmData"]["wsDiscovery"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Web Services Discovery",setting_card="ws-discovery",settings_value= ws_discovery_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Web Services Discovery")

    def test_05_verify_bonjour_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Bonjour API Status
        network_bonjour_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/discoveryServices"
        response = get_cloud_api_response(self.stack,network_bonjour_uri)
        bonjour_status = response.json()["state"]["reported"]["cdmData"]["bonjour"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Bonjour",setting_card="bonjour",settings_value= bonjour_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Bonjour")

    def test_06_verify_add_network_settings_9100_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Standard TCP/IP Printing (P9100) API Status
        network_9100_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,network_9100_uri)
        tcpipprint_status = response.json()["state"]["reported"]["cdmData"]["port9100"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="9100",setting_card="tcpip-print",settings_value=tcpipprint_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("9100")

    def test_07_verify_airprint_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

         # Get AirPrint API Status
        airprint_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,airprint_uri)
        airprint_status = response.json()["state"]["reported"]["cdmData"]["airPrint"]["enabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="AirPrint",setting_card="airprint",settings_value= airprint_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("AirPrint")

    def test_08_verify_add_network_settings_lpd_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network LPD API Status
        network_lpd_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,network_lpd_uri)
        lpd_status = response.json()["state"]["reported"]["cdmData"]["lpdPrint"]["enabled"]
    
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Line Printer Daemon",setting_card="lpd-lpr",settings_value=lpd_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Line Printer Daemon")

    def test_09_verify_ipp_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Internet Print Protocol (IPP) API Status
        network_ipp_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,network_ipp_uri)
        ipp_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ipp"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="(IPP)",setting_card="ipp",settings_value= ipp_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("(IPP)")

    def test_10_verify_ipps_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Secure Internet Print Protocol (IPPS) API Status
        network_ipps_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,network_ipps_uri)
        ipps_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ippSecure"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Secure Internet Print Protocol",setting_card="ipps",settings_value= ipps_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Secure Internet Print Protocol")

    def test_11_verify_certificate_for_ipp_ipps_pull_printings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        #Verify Verify Certificate for IPP/IPPS Pull Printing API Status 
        verify_certificate_for_ipp_ipps_pull_printings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,verify_certificate_for_ipp_ipps_pull_printings_uri)
        verify_certificate_for_ipp_ipps_pull_printings_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["enableCertificateValidation"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Verify Certificate for IPP/IPPS Pull Printing",setting_card="verify-certificate",settings_value=verify_certificate_for_ipp_ipps_pull_printings_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Verify Certificate for IPP/IPPS Pull Printing")

    def test_12_verify_web_services_print_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network WS-Print API Status
        network_ws_print_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,network_ws_print_uri)
        web_services_status = response.json()["state"]["reported"]["cdmData"]["wsPrint"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Web Services Print",setting_card="ws-print",settings_value= web_services_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Web Services Print")