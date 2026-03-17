import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

#Generate random device properties values
support_contact="support_user"+str(random.randint(1,99))
system_location="system_location"+str(random.randint(1,99))
system_contact="system_contact"+str(random.randint(1,99))

class Test_05_Network_Category03_Proxies_Settings(object):

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

    def test_01_verify_support_contact_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Support Contact",setting_card="support-contact",settings_value=support_contact,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Support Contact")

    def test_02_verify_system_location_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="System Location",setting_card="system-location",settings_value=system_location,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("System Location")

    def test_03_verify_system_contact_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="System Contact",setting_card="system-contact",settings_value=system_contact,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("System Contact")
    
    def test_04_verify_ftp_print_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Network FTP Print API Status
        network_ftp_print_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_api_response(self.stack,network_ftp_print_uri)
        ftp_print_status = response.json()["state"]["reported"]["cdmData"]["ftpPrint"]["enabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="FTP Print",setting_card="ftp-print",settings_value= ftp_print_status, category_type="Network")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("FTP Print")

    def test_05_verify_ipv4_multicast_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        #Get IPV4 Multicast Settings Setting API Status
        ipv4_multicast_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack, ipv4_multicast_uri)
        ipv4_multicast_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["multicastEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="IPv4 Multicast",setting_card="ipv4-multicast",settings_value= ipv4_multicast_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # # Verify Assessment status
        # self.printers.click_printers_details_page_hp_secure_fleet_manager_tab()
        # self.printers.verify_assessment_status_report(self.serial_number)        

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("IPv4 Multicast")

    def test_06_verify_ipv6_information_setting_in_device_specific_policy(self):
        #
        domain_name = "stgtest"+str(random.randint(1,9))+".com"
        primary_dns_ipv6_server_address = "2620:0:a02:e00d:b25c:daff:fec0:"+str(random.randint(11,99))+"fe"
        secondary_dns_ipv6_server_address = "2620:0:a02:e00d:b25c:daff:fec0:"+str(random.randint(22,88))+"fe"

        device_cloud_id = self.printers.get_device_cloud_id()

        # Get IPv6 Information API Status
        ipv6_information_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,ipv6_information_uri)
        ipv6_status = response.json()["state"]["reported"]["cdmData"]["ipv6"]["enabled"]
        dhcpv6_policy_status = response.json()["state"]["reported"]["cdmData"]["ipv6"]["dhcpv6Policy"]

        ipv6_information_status = list((ipv6_status,dhcpv6_policy_status,domain_name,primary_dns_ipv6_server_address,secondary_dns_ipv6_server_address))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="IPv6 Information",setting_card="ipv6-info",settings_value=ipv6_information_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("IPv6 Information")

    def test_07_verify_tcp_or_ip_configuration_method_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get TCP/IP Configuration Method API Status
        tcpip_configuration_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,tcpip_configuration_uri)
        tcpip_configuration_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["address"]["activeConfigMethod"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="TCP/IP Configuration Method",setting_card="tcpip-config",settings_value=tcpip_configuration_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("TCP/IP Configuration Method")

    def test_08_verify_configuration_precedence_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Configuration Precedence API Status
        configuration_precedence_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack, configuration_precedence_uri)

        # Convert the Response object to a Python dictionary using .json()
        response_data = response.json()

        # Accessing the first item from the ipConfigPrecedence and extracting the precedence and method
        ip_config = response_data["state"]["reported"]["cdmData"]["ipConfigPrecedence"]

        # Accessing the first entry in the list (index 0)
        configuration_precedence = ip_config[0]["precedence"]
        configuration_method = ip_config[0]["method"]

        configuration_precedence_status =list((configuration_precedence,configuration_method))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Configuration Precedence", setting_card="configuration-precedence", settings_value=configuration_precedence_status, category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Configuration Precedence")

    def test_09_verify_fips_140_compliance_library_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify FIPS 140 Compliance Library API Status
        fips_140_compliance_library_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/tlsConfig"
        response = get_api_response(self.stack,fips_140_compliance_library_uri)
        fips_140_compliance_library_status = response.json()["state"]["reported"]["cdmData"]["fipsMode"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="FIPS 140 Compliance Library",setting_card="fips-140-compliance",settings_value=fips_140_compliance_library_status,category_type="Network")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("FIPS 140 Compliance Library")
        
    @pytest.mark.skip
    def test_10_verify_dns_server_setting_in_device_specific_policy(self):
        #
        domain_name = "stgtest"+str(random.randint(1,9))+".com"
        primary_dns_server_ip = "15.4.28."+str(random.randint(11,99))
        secondary_dns_server_ip = "15.6.28."+str(random.randint(22,88))
        
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get DNS Server API Status
        ipv6_information_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,ipv6_information_uri)
        clear_primary_dns_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["dnsServer"]["primary"]["configMethod"]
        clear_secondary_dns_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["dnsServer"]["secondary"]["configMethod"]

        dns_server_status = list((clear_primary_dns_status,primary_dns_server_ip,clear_secondary_dns_status,secondary_dns_server_ip,domain_name))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="DNS Server",setting_card="dns-server",settings_value=dns_server_status,category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("DNS Server")

    