import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ecp.ecp_api_utility import *
from time import sleep
import random
pytest.app_info = "ECP"

#Generate random device properties values
asseet_number=random.randint(100,999)
contact_person="user"+str(random.randint(1,99))
device_name="device_name"+str(random.randint(1,99))
device_location="location"+str(random.randint(1,99))
company_name="company"+str(random.randint(1,99))
support_contact="support_user"+str(random.randint(1,99))
system_location="system_location"+str(random.randint(1,99))
system_contact="system_contact"+str(random.randint(1,99))

class Test_12_ECP_Proxies_Device_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.serial_number = request.config.getoption("--proxy-device")
        self.hpid = self.fc.fd["hpid"]
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.proxies = self.fc.fd["proxies"]
        self.login_account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.login_account["fp_email"]
        self.hpid_password = self.login_account["fp_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_devices(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        return self.devices.click_first_entry_link()
    
    def test_01_verify_add_asset_number_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36095047

        self.devices.add_settings_in_device_specific_policy_tab("Asset Number",setting_card="asset-number",settings_value=asseet_number,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Verify the asset number in device details overview tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        assert str(asseet_number) == self.devices.get_device_details_overview_asset_number()

        # Verify the asset number in device details properties tab
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("asset-number")
        assert str(asseet_number) == self.devices.get_device_details_device_property_value("asset-number")

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Asset Number")

    def test_02_verify_add_contact_person_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36095049
         
        self.devices.add_settings_in_device_specific_policy_tab("Contact Person",setting_card="contact-person",settings_value=contact_person,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Verify the contact person in device details properties tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("contact-person")
        assert contact_person == self.devices.get_device_details_device_property_value("contact-person")

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Contact Person")

    def test_03_verify_add_device_name_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36095051

        self.devices.add_settings_in_device_specific_policy_tab("Device Name",setting_card="device-name",settings_value=device_name,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Verify the device name in device details properties tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("device-name")
        assert device_name == self.devices.get_device_details_device_property_value("device-name")

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Device Name")

    def test_04_verify_add_device_location_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36095050

        self.devices.add_settings_in_device_specific_policy_tab("Device Location",setting_card="device-location",settings_value=device_location,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Verify the device location in device details properties tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("device-location")
        assert device_location == self.devices.get_device_details_device_property_value("device-location")

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Device Location")

    def test_05_verify_add_company_name_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36095048

        self.devices.add_settings_in_device_specific_policy_tab("Company Name",setting_card="company-name",settings_value=company_name,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Verify the company name in device details properties tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("company-name")
        assert company_name == self.devices.get_device_details_device_property_value("company-name")

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Company Name")

    def test_06_verify_add_network_settings_wins_registration_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909624

        device_cloud_id = self.devices.get_device_cloud_id()
        
        # Verify Network Wins Registration API Status
        if self.stack == "stage":
            network_wins_registration_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/nameResolverServices"
        else:
            network_wins_registration_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/nameResolverServices"
        response = get_proxy_settings_api_response(self.stack,network_wins_registration_uri)
        wins_reg_status = response.json()["state"]["reported"]["cdmData"]["wins"]["enabled"]

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("WINS Registration","wins-registration",wins_reg_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
    
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("WINS Registration")

    def test_07_verify_add_network_settings_wins_port_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909623

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network Wins Port API Status
        if self.stack == "stage":
            network_wins_port_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/nameResolverServices"
        else:
            network_wins_port_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/nameResolverServices"
        response = get_proxy_settings_api_response(self.stack,network_wins_port_uri)
        wins_port_status = response.json()["state"]["reported"]["cdmData"]["wins"]["winsPort"]

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("WINS Port", "wins-port", wins_port_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("WINS Port")

    def test_08_verify_add_network_settings_llmnr_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909621

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network LLMNR API Status
        if self.stack == "stage":
            network_llmnr_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/nameResolverServices"
        else:
            network_llmnr_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/nameResolverServices"
        response = get_proxy_settings_api_response(self.stack,network_llmnr_uri)
        llmnr_status = response.json()["state"]["reported"]["cdmData"]["llmnr"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("LLMNR", "llmnr", llmnr_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("LLMNR")

    def test_09_verify_add_network_settings_slp_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909614

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network SLP API Status
        if self.stack == "stage":
            network_slp_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/discoveryServices"
        else:
            network_slp_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/discoveryServices"
        response = get_proxy_settings_api_response(self.stack,network_slp_uri)
        slp_status = response.json()["state"]["reported"]["cdmData"]["slp"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("SLP", "slp", slp_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("SLP")

    def test_10_verify_add_network_settings_bonjour_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909615

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network Bonjour API Status
        if self.stack == "stage":
            network_bonjour_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/discoveryServices"
        else:
            network_bonjour_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/discoveryServices"
        response = get_proxy_settings_api_response(self.stack,network_bonjour_uri)
        bonjour_status = response.json()["state"]["reported"]["cdmData"]["bonjour"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Bonjour", "bonjour", bonjour_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Bonjour")

    def test_11_verify_add_network_settings_ws_discovery_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909620

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network WS-Discovery API Status
        if self.stack == "stage":
            network_ws_discovery_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/discoveryServices"
        else:
            network_ws_discovery_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/discoveryServices"
        response = get_proxy_settings_api_response(self.stack,network_ws_discovery_uri)
        ws_discovery_status = response.json()["state"]["reported"]["cdmData"]["wsDiscovery"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Web Services Discovery", "ws-discovery", ws_discovery_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Web Services Discovery")

    def test_12_verify_add_network_settings_ipp_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909618

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network IPP API Status
        if self.stack == "stage":
            network_ipp_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            network_ipp_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,network_ipp_uri)
        ipp_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ipp"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("(IPP)", "ipp", ipp_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("(IPP)")

    def test_13_verify_add_network_settings_ipps_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909619
        
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network IPPS API Status
        if self.stack == "stage":
            network_ipps_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            network_ipps_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,network_ipps_uri)
        ipps_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ippSecure"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Secure Internet Print Protocol", "ipps", ipps_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Secure Internet Print Protocol")

    def test_14_verify_add_network_settings_9100_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909616
        
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network 9100 API Status
        if self.stack == "stage":
            network_9100_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            network_9100_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,network_9100_uri)
        tcpipprint_status = response.json()["state"]["reported"]["cdmData"]["port9100"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("9100", "tcpip-print", tcpipprint_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("9100")

    def test_15_verify_add_network_settings_lpd_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909627

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network LPD API Status
        if self.stack == "stage":
            network_lpd_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            network_lpd_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,network_lpd_uri)
        lpd_status = response.json()["state"]["reported"]["cdmData"]["lpdPrint"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Line Printer Daemon", "lpd-lpr", lpd_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Line Printer Daemon")

    def test_16_verify_add_network_settings_web_services_print_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909622
              
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network WS-Print API Status
        if self.stack == "stage":
            network_ws_print_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            network_ws_print_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,network_ws_print_uri)
        web_services_status = response.json()["state"]["reported"]["cdmData"]["wsPrint"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Web Services Print", "ws-print", web_services_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Web Services Print")

    def test_17_verify_add_network_ftp_print_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909626
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network FTP Print API Status
        if self.stack == "stage":
            network_ftp_print_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            network_ftp_print_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,network_ftp_print_uri)
        ftp_print_status = response.json()["state"]["reported"]["cdmData"]["ftpPrint"]["enabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("FTP Print", "ftp-print", ftp_print_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("FTP Print")

    def test_18_verify_add_network_settings_xml_services_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909629

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network XML Services API Status
        if self.stack == "stage":
            network_xml_services_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        else:
            network_xml_services_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        response = get_proxy_settings_api_response(self.stack,network_xml_services_uri)
        xml_services_status = response.json()["state"]["reported"]["cdmData"]["xdmEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("HP Jetdirect XML Services", "jd-xml-svc", xml_services_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("HP Jetdirect XML Services")

    def test_19_verify_add_network_settings_telnet_config_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909628
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network Telnet API Status
        if self.stack == "stage":
            network_telnet_config_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        else:
            network_telnet_config_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        response = get_proxy_settings_api_response(self.stack,network_telnet_config_uri)
        telnet_config_status = response.json()["state"]["reported"]["cdmData"]["telnetEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Telnet", "telnet", telnet_config_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Telnet")

    def test_20_verify_add_network_settings_tftp_configuration_file_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909630

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network TFTP Config API Status
        if self.stack == "stage":
            network_tftp_config_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        else:
            network_tftp_config_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        response = get_proxy_settings_api_response(self.stack,network_tftp_config_uri)
        tftp_config_status = response.json()["state"]["reported"]["cdmData"]["tftpEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("TFTP Configuration File", "tftp-cfg", tftp_config_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("TFTP Configuration File")

    def test_21_verify_add_network_settings_airprint_scan_and_secure_scan_specific_policy(self):
        #  https://hp-testrail.external.hp.com/index.php?/cases/view/36909709
               
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network airprint scan and secure scan API Status
        if self.stack == "stage":
            airprint_scan_and_secure_scan_config_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/networkScanServices"
        else:
            airprint_scan_and_secure_scan_config_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/networkScanServices"
        response = get_proxy_settings_api_response(self.stack,airprint_scan_and_secure_scan_config_uri)
        airprint_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCL"]
        airprint_secure_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCLSecure"]
        all_scan_and_secure_status = list((airprint_scan_status,airprint_secure_scan_status))
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("AirPrint Scan/AirPrint Secure Scan", "airprint-scan-secure-scan", all_scan_and_secure_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("AirPrint Scan/AirPrint Secure Scan")

    def test_22_verify_proxies_settings_toggle_functionality_end_to_end(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/37835611

        self.home.click_proxies_menu_btn()
        self.proxies.verify_page_title(page_title="Proxies")
        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.proxies_settings_search("Asset Number")
        toggle_status=self.proxies.get_proxies_settings_toggle_button_status()
        if toggle_status:
            self.proxies.click_proxies_settings_toggle_button()
            self.proxies.verify_proxies_settings_table_data_load()
            assert toggle_status != self.proxies.get_proxies_settings_toggle_button_status()
        
        # Add Asset Number setting in Device Specific Policy Tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.add_settings_in_device_specific_policy_tab("Asset Number",setting_card="asset-number",settings_value=company_name)

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Reverting the proxy settings toggle.
        self.home.click_proxies_menu_btn()
        self.proxies.verify_page_title(page_title="Proxies")
        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.proxies_settings_search("Asset Number")
        toggle_status=self.proxies.get_proxies_settings_toggle_button_status()
        if toggle_status == False:
            self.proxies.click_proxies_settings_toggle_button()
            self.proxies.verify_proxies_settings_table_data_load()
            assert toggle_status != self.proxies.get_proxies_settings_toggle_button_status()

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Asset Number")

    def test_23_verify_add_device_settings_use_requested_tray_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909530

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Device use requested tray API Status
        if self.stack == "stage":
            use_requested_tray_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        else:
            use_requested_tray_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        response = get_proxy_settings_api_response(self.stack,use_requested_tray_uri)
        use_requested_tray_status = response.json()["state"]["reported"]["cdmData"]["useRequestedTray"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Use Requested Tray", "use-requested-tray", use_requested_tray_status,"Devices")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Use Requested Tray")
    
    def test_24_verify_add_device_settings_override_a4_letter_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909573
                 
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Device override a4 letter API Status
        if self.stack == "stage":
            override_letter_a4_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        else:
            override_letter_a4_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        response = get_proxy_settings_api_response(self.stack,override_letter_a4_uri)
        override_letter_a4_status = response.json()["state"]["reported"]["cdmData"]["a4LetterOverrideEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Override A4/Letter", "override-letter-a4", override_letter_a4_status, "Devices")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Override A4/Letter")

    def test_25_verify_add_device_settings_tray1_mode_manual_feed_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909551

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Device tray1 mode manual feed API Status
        if self.stack == "stage":
            tray1_mode_manual_feed_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        else:
            tray1_mode_manual_feed_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        response = get_proxy_settings_api_response(self.stack,tray1_mode_manual_feed_uri)
        tray1_mode_manual_feed_status = response.json()["state"]["reported"]["cdmData"]["manualFeedEnable"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Tray 1 Mode / Manual Feed", "manual-feed", tray1_mode_manual_feed_status, "Devices")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
    
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Tray 1 Mode / Manual Feed")

    def test_26_verify_add_device_settings_size_type_prompt_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909574
            
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Device size type prompt API Status
        if self.stack == "stage":
            size_type_prompt_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        else:
            size_type_prompt_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        response = get_proxy_settings_api_response(self.stack,size_type_prompt_uri)
        size_type_prompt_status = response.json()["state"]["reported"]["cdmData"]["sizeTypeEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Size / Type Prompt", "size-type-prompt", size_type_prompt_status, "Devices")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Size / Type Prompt")

    def test_27_verify_add_security_settings_device_announcement_agent_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/38181972

        #Generate random ip address
        test_ip_address="15.45.68."+str(random.randint(1,99)) 
        
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Security Device Announcement Agent API Status
        if self.stack == "stage":
            device_announcement_agent_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/deviceAnnouncement"
        else:
            device_announcement_agent_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/deviceAnnouncement"
        response = get_proxy_settings_api_response(self.stack,device_announcement_agent_uri)
        announcement_status = response.json()["state"]["reported"]["cdmData"]["announcementEnabled"]
        server_auth_status = response.json()["state"]["reported"]["cdmData"]["serverAuthEnabled"]
        
        all_device_announcement_agent_status = list((announcement_status,test_ip_address,server_auth_status))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Device Announcement Agent", "device-announcement", all_device_announcement_agent_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
         
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Device Announcement Agent")

    def test_28_verify_add_web_services_settings_smart_cloud_print_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/38181983
        
        device_cloud_id = self.devices.get_device_cloud_id()
 
        # Verify Web Services Smart Cloud Print API Status
        if self.stack == "stage":
            smart_cloud_print_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        else:
            smart_cloud_print_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        response = get_proxy_settings_api_response(self.stack,smart_cloud_print_uri)
        smart_cloud_print_status = response.json()["state"]["reported"]["cdmData"]["webServices"]["cloudPrint"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Smart Cloud Print", "smart-cloud-print", smart_cloud_print_status, "Web Services")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Smart Cloud Print")

    def test_29_verify_add_device_settings_manual_feed_prompt_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909572
            
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Device Manual Feed Prompt API Status
        if self.stack == "stage":
            manual_feed_prompt_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        else:
            manual_feed_prompt_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/mediaHandling"
        response = get_proxy_settings_api_response(self.stack,manual_feed_prompt_uri)
        manual_feed_prompt_status = response.json()["state"]["reported"]["cdmData"]["manualFeedprompt"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Manual Feed Prompt", "manual-feed-prompt", manual_feed_prompt_status, "Devices")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
   
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Manual Feed Prompt")
   
    def test_30_verify_host_plug_and_play_device_specific_policy(self):
        # 
        
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Host Plug and Play API Status
        if self.stack == "stage":
            usb_plug_and_play_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/usbHost"
        else:
            usb_plug_and_play_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/usbHost"
        response = get_proxy_settings_api_response(self.stack,usb_plug_and_play_uri)
        plug_and_play_status = response.json()["state"]["reported"]["cdmData"]["plugAndPlayEnabled"]
        print_from_usb_status = response.json()["state"]["reported"]["cdmData"]["printFromUsbEnabled"]
        scan_to_usb_status = response.json()["state"]["reported"]["cdmData"]["scanToUsbEnabled"]
        all_plug_and_play_status = list((plug_and_play_status,print_from_usb_status,scan_to_usb_status))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Host USB Plug and Play", "host-usb-pnp", all_plug_and_play_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Host USB Plug and Play")

    def test_31_verify_digital_sending_service_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/38181986

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Digital Sending Service API Status
        if self.stack == "stage":
            digital_service_sending_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        else:
            digital_service_sending_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        response = get_proxy_settings_api_response(self.stack,digital_service_sending_uri)
        digital_sending_allow_use = response.json()["state"]["reported"]["cdmData"]["security"]["digitalSendingService"]["allowUse"]
        digital_sending_allow_transfer = response.json()["state"]["reported"]["cdmData"]["security"]["digitalSendingService"]["allowTransfer"]
        all_digital_sending_status = list((digital_sending_allow_use,digital_sending_allow_transfer))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Digital Sending Service", "digital-sending", all_digital_sending_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Digital Sending Service")

    def test_32_verify_pjl_access_commands_device_specific_policy(self):
        #
                
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify PJL Access Commands API Status
        if self.stack == "stage":
            pjl_access_commands_uri = "https://stratus-stg.tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/print"
        else:
            pjl_access_commands_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/print"
        response = get_proxy_settings_api_response(self.stack,pjl_access_commands_uri)
        pjl_access_commands_status = response.json()["state"]["reported"]["cdmData"]["pjlDeviceAccessCommandsEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Printer Job Language (PJL) Access Commands", "pjl-command", pjl_access_commands_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Printer Job Language (PJL) Access Commands")

    def test_33_verify_add_network_settings_airprint_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/36909617
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Network AirPrint API Status
        if self.stack == "stage":
            airprint_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        else:
            airprint_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/printServices"
        response = get_proxy_settings_api_response(self.stack,airprint_uri)
        airprint_status = response.json()["state"]["reported"]["cdmData"]["airPrint"]["enabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("AirPrint", "airprint", airprint_status, "Network")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number) 

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("AirPrint")

    def test_34_verify_hp_jet_advantage_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/38181977
               
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify HP JetAdvantage (More Apps) API Status
        if self.stack == "stage":
            hp_jet_advantage_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        else:
            hp_jet_advantage_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        response = get_proxy_settings_api_response(self.stack,hp_jet_advantage_uri)
        hp_jetadvantage = response.json()["state"]["reported"]["cdmData"]["webServices"]["hpJetAdvantage"]
        hp_jetadvantage_accountcreation = response.json()["state"]["reported"]["cdmData"]["webServices"]["accountCreation"]
        all_hp_jet_advantage_status = list((hp_jetadvantage, hp_jetadvantage_accountcreation))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("HP JetAdvantage (More Apps)", "hp-jet-adv", all_hp_jet_advantage_status, "Web Services")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("HP JetAdvantage (More Apps)")

    def test_35_verify_add_device_settings_date_and_time_format_specific_policy(self):
        # 
        
        device_cloud_id = self.devices.get_device_cloud_id()
 
        # Verify Web Services Smart Cloud Print API Status
        if self.stack == "stage":
            device_date_and_time_format_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/clock"
        else:
            device_date_and_time_format_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/clock"
        response = get_proxy_settings_api_response(self.stack,device_date_and_time_format_uri)
        device_date_format = response.json()["state"]["reported"]["cdmData"]["dateFormat"]
        device_time_format = response.json()["state"]["reported"]["cdmData"]["timeFormat"]
        device_date_and_time_format = list((device_date_format, device_time_format))
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Date/Time Format", "date-time-format", device_date_and_time_format, "Devices")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Date/Time Format")

    def test_36_verify_add_fax_settings_pc_fax_send_specific_policy(self):
        #

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Fax Settings PC Fax send API Status
        if self.stack == "stage":
            pc_fax_send_config_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/fax/sendConfiguration"
        else:
            pc_fax_send_config_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/fax/sendConfiguration"
        response = get_proxy_settings_api_response(self.stack,pc_fax_send_config_uri)
        apc_fax_send_status = response.json()["state"]["reported"]["cdmData"]["pcFaxSendEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("PC Fax Send", "pc-fax-send", apc_fax_send_status,"Fax")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("PC Fax Send")

    def test_37_verify_embedded_web_server_language_policy_setting(self):
        #

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Embedded Web Server language API Status
        if self.stack == "stage":
            embedded_web_server_language_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/ews"
        else:
            embedded_web_server_language_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/ews"
        response = get_proxy_settings_api_response(self.stack,embedded_web_server_language_uri)
        selected_language = response.json()["state"]["reported"]["cdmData"]["selectedLanguage"]
        language_source_status = response.json()["state"]["reported"]["cdmData"]["languageSource"]
        language_source_and_language = list((selected_language, language_source_status))
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Embedded Web Server Language Settings", "ews-language", language_source_and_language, "Embedded Web Server")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
            
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Embedded Web Server Language Settings")

    def test_38_verify_control_panel_language_policy_setting(self):
        # 
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Control Panel Language API Status
        if self.stack == "stage":
            control_panel_language_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/controlpanel"
        else:
            control_panel_language_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/controlpanel"
        response = get_proxy_settings_api_response(self.stack,control_panel_language_uri)
        current_language_status = response.json()["state"]["reported"]["cdmData"]["currentLanguage"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Control Panel Language", "ctrl-panel-language", current_language_status, "Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
               
        # Verify Control Panel Language API Status
        response = get_proxy_settings_api_response(self.stack,control_panel_language_uri)
        assert current_language_status != response.json()["state"]["reported"]["cdmData"]["currentLanguage"]

        # Changing Control Panel Language to English
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_next_button()
        self.devices.click_device_specific_policy_settings_card("ctrl-panel-language")
        self.devices.select_control_panel_language("English")
        self.devices.click_device_specific_policy_create_button()

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Control Panel Language")

    def test_39_verify_printer_firmware_update_remote_firmware_update_specific_policy(self):
        # 

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Remote Firmware Update API Status
        if self.stack == "stage":
            remote_firmware_update_uri = "https://stratus-stg.tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/firmwareUpdate"
        else:
            remote_firmware_update_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/firmwareUpdate"
        response = get_proxy_settings_api_response(self.stack,remote_firmware_update_uri)
        remote_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["pjlUpdateEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Remote Firmware Update (RFU)", "remote-fw-update", remote_firmware_update_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Remote Firmware Update (RFU)")

    def test_40_verify_printer_firmware_sha1_code_signing_legacy_firmware_update_specific_policy(self):
        # 

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Legacy Firmware Update UPi API Status
        if self.stack == "stage":
            legacy_firmware_update_uri = "https://stratus-stg.tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/firmwareUpdate"
        else:
            legacy_firmware_update_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/firmwareUpdate"
        response = get_proxy_settings_api_response(self.stack,legacy_firmware_update_uri)
        legacy_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["sha1ValidationEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Legacy Firmware Upgrade", "legacy-fw-update", legacy_firmware_update_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Legacy Firmware Upgrade")

    def test_41_verify_display_color_usage_job_log_page_on_information_tab_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Display Color Usage Job Log uri API Status
        if self.stack == "stage":
            display_color_usage_job_log_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/ews"
        else:
            display_color_usage_job_log_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/ews"
        response = get_proxy_settings_api_response(self.stack,display_color_usage_job_log_uri)
        display_color_usage_job_log_status = response.json()["state"]["reported"]["cdmData"]["displayColorUsageTab"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Display Color Usage Job Log Page on Information Tab", "color-usage-log", display_color_usage_job_log_status, "Security")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Display Color Usage Job Log Page on Information Tab")

    def test_42_verify_add_support_contact_device_specific_policy(self):
        # 

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Support Contact Update API Status
        if self.stack == "stage":
            support_contact_update_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/system"
        else:
            support_contact_update_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/system"
        response = get_proxy_settings_api_response(self.stack,support_contact_update_uri)
        support_contact_update_status = response.json()["state"]["reported"]["cdmData"]["supportContact"]

        self.devices.add_settings_in_device_specific_policy_tab("Support Contact",setting_card="support-contact",settings_value=support_contact, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Support Contact")

    def test_43_verify_add_system_location_device_specific_policy(self):
        # 

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify System Location API Status
        if self.stack == "stage":
            system_location_update_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        else:
            system_location_update_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        response = get_proxy_settings_api_response(self.stack,system_location_update_uri)
        system_location_update_status = response.json()["state"]["reported"]["cdmData"]["systemLocation"]

        self.devices.add_settings_in_device_specific_policy_tab("System Location",setting_card="system-location",settings_value=device_location, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("System Location")
        
    def test_44_verify_save_to_network_folder_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Save To Network Folder uri API Status
        if self.stack == "stage":
            save_to_network_folder_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/scan/destinationConfig"
        else:
            save_to_network_folder_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/scan/destinationConfig"
        response = get_proxy_settings_api_response(self.stack,save_to_network_folder_uri)
        save_to_network_folder_status = response.json()["state"]["reported"]["cdmData"]["folderEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Save To Network Folder", "save-to-network-folder", save_to_network_folder_status, "Digital Sending")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Save To Network Folder")

    def test_45_verify_save_to_sharepoint_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Save to Share Point uri API Status
        if self.stack == "stage":
            save_to_sharepoint_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/scan/destinationConfig"
        else:
            save_to_sharepoint_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/scan/destinationConfig"
        response = get_proxy_settings_api_response(self.stack,save_to_sharepoint_uri)
        save_to_sharepoint_status = response.json()["state"]["reported"]["cdmData"]["sharePointEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Save to SharePoint", "save-to-share-point", save_to_sharepoint_status, "Digital Sending")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Save to SharePoint")
    
    def test_46_verify_airprint_fax_settings(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify AirPrint Fax API Status
        if self.stack == "stage":
            airprint_fax_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/fax/sendConfiguration"
        else:
            airprint_fax_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/fax/sendConfiguration"
        response = get_proxy_settings_api_response(self.stack,airprint_fax_uri)
        airprint_fax_status = response.json()["state"]["reported"]["cdmData"]["ippFaxEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("AirPrint Fax", "airprint-fax", airprint_fax_status, "Network")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("AirPrint Fax")

    def test_47_verify_service_access_code_settings(self):
        # 
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Service Access Code", setting_card="svc-access-code", category_type="Security")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Service Access Code")

    def test_48_verify_file_erase_mode_settings(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify File Erase Mode API Status
        if self.stack == "stage":
            file_erase_mode_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/storageDevices"
        else:
            file_erase_mode_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/storageDevices"
        response = get_proxy_settings_api_response(self.stack,file_erase_mode_uri)
        file_erase_mode_status = response.json()["state"]["reported"]["cdmData"]["fileEraseMode"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("File Erase Mode", "file-erase", file_erase_mode_status, "File System")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("File Erase Mode")

    def test_49_verify_copy_paper_tray_selection_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Copy Paper Tray Selection uri API Status
        if self.stack == "stage":
            copy_paper_tray_selection_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        else:
            copy_paper_tray_selection_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        response = get_proxy_settings_api_response(self.stack,copy_paper_tray_selection_uri)
        copy_paper_tray_selection_status = response.json()["state"]["reported"]["cdmData"]["dest"]["print"]["mediaSource"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Copy Paper Tray Selection", "copy-tray", copy_paper_tray_selection_status, "Copier")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Copy Paper Tray Selection")

    def test_50_verify_copy_darkness_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Copy Darkness uri API Status
        if self.stack == "stage":
            copy_darkness_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        else:
            copy_darkness_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        response = get_proxy_settings_api_response(self.stack,copy_darkness_uri)
        copy_darkness_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["exposure"]

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Copy Darkness", "copy-darkness", copy_darkness_status, "Copier")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Copy Darkness")

    def test_51_verify_copy_sharpness_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Copy Sharpness uri API Status
        if self.stack == "stage":
            copy_sharpness_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        else:
            copy_sharpness_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        response = get_proxy_settings_api_response(self.stack,copy_sharpness_uri)
        copy_sharpness_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["sharpness"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Copy Sharpness", "copy-sharpness", copy_sharpness_status, "Copier")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Copy Sharpness")

    def test_52_verify_copy_optimize_text_or_picture_specific_policy(self):
        # 
          
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Copy Optimize Text/Picture uri API Status
        if self.stack == "stage":
            copy_optimize_text_or_picture_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        else:
            copy_optimize_text_or_picture_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        response = get_proxy_settings_api_response(self.stack,copy_optimize_text_or_picture_uri)
        copy_optimize_text_or_picture_status = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["contentType"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Copy Optimize Text/Picture", "copy-optimize", copy_optimize_text_or_picture_status, "Copier")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Copy Optimize Text/Picture")

    def test_53_verify_copy_background_cleanup_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id()    
         
        # Verify Copy Background Cleanup uri API Status
        if self.stack == "stage":
            copy_background_cleanup_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        else:
            copy_background_cleanup_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        response = get_proxy_settings_api_response(self.stack,copy_background_cleanup_uri)
        copy_background_cleanup_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["backgroundCleanup"]

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Copy Background Cleanup", "copy-bg-cleanup", copy_background_cleanup_status, "Copier")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Copy Background Cleanup")

    def test_54_verify_copy_contrast_specific_policy(self):
        #

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Copy Contrast uri API Status
        if self.stack == "stage":
            copy_contrast_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        else:
            copy_contrast_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/configuration/defaults/copy"
        response = get_proxy_settings_api_response(self.stack,copy_contrast_uri)
        copy_contrast_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["contrast"]

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Copy Contrast", "copy-contrast", copy_contrast_status, "Copier")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Copy Contrast")

    def test_55_verify_time_services_device_specific_policy(self):
        #
        #Generate random ip address
        time_services_ip_address="15.40.45."+str(random.randint(1,99))
        local_port=random.randint(1100,1900)
        synchronize_time=random.randint(1,168)

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Time Services API Status
        if self.stack == "stage":
            time_services_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/clock"
        else:
            time_services_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/clock"
        response = get_proxy_settings_api_response(self.stack,time_services_uri)
        time_services_system_time_sync = response.json()["state"]["reported"]["cdmData"]["systemTimeSync"]

        time_services_status = list((time_services_system_time_sync,time_services_ip_address,local_port,synchronize_time))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Time Services", "time-services", time_services_status, "Embedded Web Server")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Time Services")

    def test_56_verify_file_system_access_protocol_setting_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify File System Access Protocols API Status
        if self.stack == "stage":
            file_system_access_protocol_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/print"
        else:
            file_system_access_protocol_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/print"
        response = get_proxy_settings_api_response(self.stack,file_system_access_protocol_uri)
        ps_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["psFileSystemAccessEnabled"]
        pjl_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["pjlDeviceAccessCommandsEnabled"]

        all_file_system_access_protocol_setting_status = list((ps_file_system_access_enabled_status,pjl_file_system_access_enabled_status))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("File System Access Protocols", "fs-access-protocol", all_file_system_access_protocol_setting_status, "File System")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("File System Access Protocols")

    def test_57_verify_system_contact_device_specific_policy(self):
        #
        
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify System Contact API Status
        if self.stack == "stage":
            system_contact_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        else:
            system_contact_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/jetdirectServices"
        response = get_proxy_settings_api_response(self.stack,system_contact_uri)
        system_contact_status = response.json()["state"]["reported"]["cdmData"]["systemContact"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("System Contact", setting_card="system-contact",settings_value=system_contact, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Verify System Contact API Status
        response = get_proxy_settings_api_response(self.stack,system_contact_uri)
        assert system_contact_status != response.json()["state"]["reported"]["cdmData"]["systemContact"]

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("System Contact")

    def test_58_verify_send_to_email_specific_policy(self):
        # 
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify send to email uri API Status
        if self.stack == "stage":
            send_to_email_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/scan/destinationConfig"
        else:
            send_to_email_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/scan/destinationConfig"
        response = get_proxy_settings_api_response(self.stack,send_to_email_uri)
        send_to_email_status = response.json()["state"]["reported"]["cdmData"]["emailEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Send To Email", "save-to-email", send_to_email_status, "Digital Sending")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Send To Email")

    def test_59_verify_proxy_server_specific_policy(self):
        # 

        #Generate random ip address
        test_ip_address="15.45.68."+str(random.randint(11,99))
        test_port_number="22"+str(random.randint(29,99))

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify proxy server API Status
        if self.stack == "stage":
            proxy_server_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/proxyConfig"
        else:
            proxy_server_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/network/proxyConfig"
        response = get_proxy_settings_api_response(self.stack,proxy_server_uri)
        proxy_server_status = response.json()["state"]["reported"]["cdmData"]["httpProxy"]["enabled"]
        
        all_proxy_server_payload = list((proxy_server_status,test_ip_address,test_port_number))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Proxy Server", "proxy-server", all_proxy_server_payload, "Web Services")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Proxy Server")

    def test_60_verify_fax_header_setting_specific_policy(self):
        #

        #Generate random ip address
        test_phone_number="5678"+str(random.randint(11,99))
        
        device_cloud_id = self.devices.get_device_cloud_id()

         # Verify Fax Header Settings API Status
        if self.stack == "stage":
            fax_header_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxModem"
        else:
            fax_header_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxModem"
        response = get_proxy_settings_api_response(self.stack,fax_header_uri)
        fax_header_country_status = response.json()["state"]["reported"]["cdmData"]["analogFaxSetup"]["analogFaxCountry"]

        all_fax_header_status = list((test_phone_number,company_name,fax_header_country_status))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Fax Header Settings", "fax-header", all_fax_header_status, "Fax")

        # Verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Fax Header Settings")

    @pytest.mark.skip # Below test case is Skipped due to PSPECP-2664
    @pytest.mark.parametrize('settings_name', ["Cloud Logging","Config Component","Device Config","Device Groups","Device Manufacturer",
                                               "Device UUID","Device UUID Key","Display Name","Fleet Proxy","Model Number","Serial Number","Service ID"])
    def test_61_verify_necessary_settings(self,settings_name):
        #
        self.home.click_proxies_menu_btn()
        self.proxies.verify_page_title(page_title="Proxies")
        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.proxies_settings_search(settings_name)
        if self.proxies.get_proxies_settings_toggle_button_status() is not True:
            self.proxies.verify_proxies_settings_warning_icon()
        else:
            self.proxies.click_proxies_settings_toggle_button()
            self.proxies.click_functionality_may_be_lost_popup_confirm_button()
            self.proxies.verify_proxies_settings_table_data_load()
            assert False == self.proxies.get_proxies_settings_toggle_button_status()
            self.proxies.verify_proxies_settings_warning_icon()

        # Reverting the settings
        self.proxies.click_proxies_settings_toggle_button()
        self.proxies.verify_proxies_settings_table_data_load()
        assert True == self.proxies.get_proxies_settings_toggle_button_status()
        self.proxies.verify_proxies_settings_warning_icon(displayed=False)

    def test_62_verify_fax_send_settings_specific_policy(self):
        #
        #Generate Random Values
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        domain_name = "auto" +str(random.randint(1,9)) + "." +"com"
        account_email_address = "autotest" + str(random.randint(1,9)) + "@testmail.com"
        
        device_cloud_id = self.devices.get_device_cloud_id()    
         
        # Verify fax send settings API Status

        if self.stack == "stage":
            fax_send_settings_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/fax/sendConfiguration"
        else:
            fax_send_settings_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/fax/sendConfiguration"
        response = get_proxy_settings_api_response(self.stack,fax_send_settings_uri)
        fax_send_status = response.json()["state"]["reported"]["cdmData"]["faxSendEnabled"]
        fax_send_method = response.json()["state"]["reported"]["cdmData"]["faxSendMethod"]

        # Verify fax send set common job API Status

        if self.stack == "stage":
            fax_send_set_common_job_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanFax"
        else:
            fax_send_set_common_job_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanFax"
        response = get_proxy_settings_api_response(self.stack,fax_send_set_common_job_uri)
        background_method = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["backgroundCleanup"]
        exposure = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["exposure"]
        contrast = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["contrast"]
        sharpness = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["sharpness"]
        notification_condition = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]

        # Verify fax send set internal modem settings Status

        if self.stack == "stage":
            fax_send_set_internal_modem_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxModem"
        else:
            fax_send_set_internal_modem_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxModem"
        response = get_proxy_settings_api_response(self.stack,fax_send_set_internal_modem_uri)
        error_correction_mode_status = response.json()["state"]["reported"]["cdmData"]["analogFaxOperation"]["errorCorrectionModeEnabled"]
        jbig_compression_status = response.json()["state"]["reported"]["cdmData"]["analogFaxOperation"]["compressionJBIGEnabled"]

        all_fax_send_status = list((fax_send_status,fax_send_method,domain_name,account_email_address,
                                    background_method,exposure,contrast,sharpness,notification_condition,notification_mode,
                                    email_address,error_correction_mode_status,jbig_compression_status))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Fax Send Settings", "fax-send", all_fax_send_status, "Fax")

         # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Fax Send Settings")

    def test_63_verify_ip_fax_setting_in_device_specific_policy(self):

        #Generate random fax id
        fax_ip="567"+str(random.randint(11,99))

        all_ip_fax_settings_status = list((fax_ip,company_name))

        # Adding IP Fax Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("IP Fax Settings", "ip-fax", all_ip_fax_settings_status, "Fax")

        # Verify the compliance of that device after the device-specific policy is applied
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device-specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("IP Fax Settings")

    def test_64_verify_retain_print_job_in_device_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Retain Print Jobs API Status
        if self.stack == "stage":
            retain_print_jobs_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/storeJobManagement"
        else:
            retain_print_jobs_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/storeJobManagement"
        response = get_proxy_settings_api_response(self.stack,retain_print_jobs_uri)   
        stored_jobs_enabled_status = response.json()["state"]["reported"]["cdmData"]["storeJobEnabled"]
        temporary_stored_job_status = response.json()["state"]["reported"]["cdmData"]["temporaryJobRetentionInMinutes"]
        standard_stored_job_status = response.json()["state"]["reported"]["cdmData"]["standardJobRetentionInMinutes"] 

        retain_print_jobs_status = list((stored_jobs_enabled_status,temporary_stored_job_status,standard_stored_job_status))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Retain Print Jobs", "retain-jobs", retain_print_jobs_status, "Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Retain Print Jobs")

    def test_65_verify_fax_receive_setting_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        rings_to_answer_status = random.randint(1,6)
        
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Fax Receive API Status

        if self.stack == "stage":
            retain_print_jobs_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxReceive"
        else:
            retain_print_jobs_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxReceive"
        response = get_proxy_settings_api_response(self.stack,retain_print_jobs_uri)
        fax_receive_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveEnabled"]
        fax_receive_method_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveMethod"]

        # Verify Fax Receive Set Common Job Status

        if self.stack == "stage":
            retain_print_jobs_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/receiveFax"
        else:
            retain_print_jobs_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/receiveFax"
        response = get_proxy_settings_api_response(self.stack,retain_print_jobs_uri)
        paper_selection_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["outputCanvasMediaId"]
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["notification"]["notificationMode"]

        # Verify Fax Receive Set Internal Modem API Status

        if self.stack == "stage":
            fax_receive_set_internal_modem_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxModem"
        else:
            fax_receive_set_internal_modem_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/faxModem"
        response = get_proxy_settings_api_response(self.stack,fax_receive_set_internal_modem_uri)
        ringer_volume_status = response.json()["state"]["reported"]["cdmData"]["analogFaxReceiveSettings"]["ringerVolume"]
        rings_to_answer_status = response.json()["state"]["reported"]["cdmData"]["analogFaxReceiveSettings"]["ringsToAnswer"]
        all_fax_receive_settings_status = list((fax_receive_status,paper_selection_status,notification_condition_status,notification_mode_status,email_address,fax_receive_method_status,ringer_volume_status,rings_to_answer_status))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Fax Receive Settings", "fax-receive", all_fax_receive_settings_status, "Fax")

        # Verify the compliance of that device after the device-specific policy is applied
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Fax Receive Settings")

    def test_66_verify_email_address_or_email_settings_in_device_specific_policy(self):
        #
        # Generate random values 
        default_from_email = "autotest"+str(random.randint(1,9))+"@hp.com"
        default_display_name = "Auto Test"+str(random.randint(1,9))
        email_subject_name = "Sample Email Testing"+str(random.randint(1,9))
        email_body_message = "Auto Test Sanity"+str(random.randint(1,9))

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Email Address or Email Settings API Status
        if self.stack == "stage":
            email_address_message_settings_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanEmail"
        else:
            email_address_message_settings_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanEmail"

        response = get_proxy_settings_api_response(self.stack,email_address_message_settings_uri)
        address_filed_restrictions = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["addressFieldRestrictionsEnabled"]
        default_from_value = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["fromSignInRequired"]
        default_from_user_editable = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["isFromEditable"]
        to_sign_in_required = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["toListSignInRequired"]
        user_editable_to = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["toListIsEditable"]
        cc_sign_in_required = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["ccListSignInRequired"]
        user_ediatable_cc = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["ccListIsEditable"]
        bcc_sign_in_required = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["bccListSignInRequired"]
        user_editable_bcc = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["bccListIsEditable"]
        user_editable_subject = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["isSubjectEditable"]
        user_editable_body = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["isBodyEditable"]
        allow_invaild_email_address = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["allowInvalidEmailAddress"]
        email_message_user_editable = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["emailSigning"]["isEditable"]
        encrypt_email_user_editable = response.json()["state"]["reported"]["cdmData"]["dest"]["email"]["emailEncryption"]["isEditable"]

        email_address_message_settings_status = list((address_filed_restrictions,default_from_value,default_from_email,default_display_name,default_from_user_editable,to_sign_in_required,user_editable_to,cc_sign_in_required,user_ediatable_cc,bcc_sign_in_required,
                                                      user_editable_bcc,email_subject_name,user_editable_subject,email_body_message,user_editable_body,allow_invaild_email_address,email_message_user_editable,encrypt_email_user_editable))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Email Address / Message Settings", "email-message", email_address_message_settings_status, "Digital Sending")

        # Verify the compliance of that device after the device-specific policy is applied
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Email Address / Message Settings")  

    def test_67_verify_energy_settings_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id() 

        # Verify Energy Settings API Status
        if self.stack == "stage":
            energy_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/power/configuration"
        else:
            energy_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/power/configuration"
        response = get_proxy_settings_api_response(self.stack,energy_settings_uri)
        inactivityTimeout = response.json()["state"]["reported"]["cdmData"]["inactivityTimeout"]
        shutdownTimeout = response.json()["state"]["reported"]["cdmData"]["shutdownTimeout"] 

        all_energy_setting_status=list((inactivityTimeout,shutdownTimeout))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Energy Settings", "energy-settings", all_energy_setting_status,"Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Energy Settings")
    
    def test_68_verify_email_scan_settings_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id()
        
        # Verify Email Settings API Status
        if self.stack == "stage":
            email_scan_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/scanEmail"
        else:
            email_scan_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/scanEmail"
        response = get_proxy_settings_api_response(self.stack, email_scan_settings_uri)
        email_scan_setting_status = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["contentType"]

         # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Email Scan Settings", "email-scan", email_scan_setting_status,"Digital Sending")

        # Verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Energy Settings")
    
    def test_69_verify_auto_send_settings_in_device_specific_policy(self):
        #
        #Generate random values
        days=random.randint(1,28)
        weeks=random.randint(1,4)
        months=random.randint(1,6)
        pages=random.randint(50,30000)
        https_url = "https://autotest" + str(random.randint(1, 9)) +"@testmail.com"
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify AutoSend API Status
        if self.stack == "stage":
            auto_send_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/autosend"
        else:
            auto_send_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/autosend"
        response = get_proxy_settings_api_response(self.stack, auto_send_settings_uri)
        auto_send_enabled_status=response.json()["state"]["reported"]["cdmData"]["autoSendEnabled"]
        auto_send_frequency_unit_status=response.json()["state"]["reported"]["cdmData"]["autoSendFrequency"]["frequencyUnit"]
        send_to_url_list_status=response.json()["state"]["reported"]["cdmData"]["sendToUrlList"]
        send_to_email_address=response.json()["state"]["reported"]["cdmData"]["sendToEmailList"]
        
        all_auto_send_status =list((auto_send_enabled_status,auto_send_frequency_unit_status,days,weeks,months,pages,send_to_url_list_status,https_url,send_to_email_address,email_address))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("AutoSend","auto-send",all_auto_send_status,"Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("AutoSend")

    def test_70_verify_restrict_color_setting_in_device_specific_policy(self):
        #
        # Generate random application name
        name = "test"+str(random.randint(1,9))

        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Restrict Color API Status
        if self.stack == "stage":
            restrict_color_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        else:
            restrict_color_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/security/legacyAttributes"
        response = get_proxy_settings_api_response(self.stack,restrict_color_uri) 

        restrict_color = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["restrictColor"]
        restrict_by_application = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingApplicationSettings"]
        default_permission = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["allowColorAndQuality"]
        non_default_permission = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["applications"][0]["allowColorAndQuality"]

        applications = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"].get("applications", [])
        if applications:
            non_default_permission = applications[0].get("allowColorAndQuality", None)
        else:
            non_default_permission = None

        all_restrict_color_status = list((restrict_color,restrict_by_application,default_permission,name,non_default_permission))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Restrict Color", "restrict-color", all_restrict_color_status, "Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Restrict Color")

    @pytest.mark.parametrize('settings_name, setting_card', [("Cartridge Threshold - Black", "cartridge-threshold-black"), ("Cartridge Threshold - Cyan", "cartridge-threshold-cyan"),
                                                             ("Cartridge Threshold - Magenta", "cartridge-threshold-magenta"), ("Cartridge Threshold - Yellow", "cartridge-threshold-yellow")])
    def test_71_verify_supplies_category_setting(self, settings_name, setting_card):
        #
        # Generate Cartridge Threshold value
        cartridge_threshold = random.randint(1,100)

        # Adding IP Fax Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab(settings_name, setting_card , cartridge_threshold, "Supplies")

        # Verify the compliance of that device after the device-specific policy is applied
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device-specific policy
        self.devices.remove_settings_in_device_specific_policy_tab(settings_name)

    def test_72_verify_email_notification_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_addresses = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Email Notification Setting API Status
        if self.stack == "stage":
            email_notification_settings_uri = "https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/" + device_cloud_id + "/jobTicket/defaults/scanEmail"
        else:
            email_notification_settings_uri = "https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/" + device_cloud_id + "/jobTicket/defaults/scanEmail"
        response = get_proxy_settings_api_response(self.stack, email_notification_settings_uri)
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]
        
        all_email_notification_settings_status=list((notification_condition_status,notification_mode_status,email_addresses))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Email Notification Settings","email-notification",all_email_notification_settings_status,"Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Email Notification Settings")

    def test_73_verify_network_folder_notification_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_addresses = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Email Notification Setting API Status
        if self.stack == "stage":
            network_folder_notification_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanNetworkFolderConfigurationDefaults"
        else:
            network_folder_notification_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanNetworkFolderConfigurationDefaults"
        response = get_proxy_settings_api_response(self.stack, network_folder_notification_settings_uri)
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]
        
        all_network_folder_notification_settings_status=list((notification_condition_status,notification_mode_status,email_addresses))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Network Folder Notification Settings","network-folder-notification",all_network_folder_notification_settings_status,"Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Network Folder Notification Settings")

    @pytest.mark.parametrize('settings_name, setting_card', [("Cartridge Very Low Action - Black", "very-low-action-black"),("Cartridge Very Low Action - Color", "very-low-action-color")])

    def test_74_verify_cartridge_settings_in_device_specific_policy(self, settings_name, setting_card):
        #
        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Cartridge Very Low Action Black Setting API Status 
        if self.stack == "stage":
            cartridge_very_low_action_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/supply/configPrivate"
        else:
            cartridge_very_low_action_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/supply/configPrivate"
        response = get_proxy_settings_api_response(self.stack, cartridge_very_low_action_settings_uri)
        cartridge_very_low_action_black_status=response.json()["state"]["reported"]["cdmData"]["blackVeryLowAction"]
        cartridge_very_low_action_color_status=response.json()["state"]["reported"]["cdmData"]["colorVeryLowAction"]

        all_cartridge_very_low_action_status =list((cartridge_very_low_action_black_status,cartridge_very_low_action_color_status))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab(settings_name, setting_card, all_cartridge_very_low_action_status, "Supplies")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab(settings_name)

    def test_75_verify_sleep_settings_in_device_specific_policy(self):
        #
        #Generate Random Values 
        sleep_mode_values=random.randint(0,119)
        auto_off_after_sleep_values=random.randint(0,119)

        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Sleep Settings Setting API Status 
        if self.stack == "stage":
            sleep_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/power/sleepconfiguration"
        else:
            sleep_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/power/sleepconfiguration"
        response = get_proxy_settings_api_response(self.stack, sleep_settings_uri)
        sleep_auto_off_timer_status=response.json()["state"]["reported"]["cdmData"]["sleepAutoOffTimerEnabled"]
        auto_on_events_status=response.json()["state"]["reported"]["cdmData"]["autoOnEvents"]

        all_sleep_settings_status =list((sleep_auto_off_timer_status,sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Sleep Settings", "sleep-settings", all_sleep_settings_status, "Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Sleep Settings")
    
    def test_76_verify_email_file_settings_in_device_specifc_policy(self):
        #
        default_file_name = "Auto_Test" + str(random.randint(1, 9))

        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Email File Settings API Status 
        if self.stack == "stage":
            eamil_file_settings_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanEmail"
        else:
            eamil_file_settings_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanEmail"
        response = get_proxy_settings_api_response(self.stack, eamil_file_settings_uri)
        email_file_name_prefix = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["prefix"]
        user_ediatable = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileNameIsEditable"]
        email_file_name_suffix = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["suffix"]
        default_output_quality = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["qualityAndFileSize"]
        default_file_type = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileType"]
        default_resolution = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["resolution"]
        pdf_encryption = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["encryptPDF"]
        blank_page_suppression = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["blankPageSuppressionEnabled"]

        all_email_file_status =list((email_file_name_prefix,default_file_name,user_ediatable,email_file_name_suffix,default_output_quality,default_file_type,default_resolution,pdf_encryption,blank_page_suppression))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Email File Settings", "email-file", all_email_file_status, "Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Email File Settings")

    def test_77_verify_network_folder_file_setting_in_device_specific_policy(self):
        #
        #Generate Random Values 
        filename= "File"+ str(random.randint(1, 9))

        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Network Folder File Settings Setting API Status 
        if self.stack == "stage":
            network_folder_file_setting_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanEmail"
        else:
            network_folder_file_setting_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/jobTicket/defaults/scanEmail"
        response = get_proxy_settings_api_response(self.stack, network_folder_file_setting_uri)
        prefix_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["prefix"]
        user_editable_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileNameIsEditable"]
        suffix_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["suffix"]
        output_quality_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["qualityAndFileSize"]
        file_type_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileType"]    
        resoultion_status=response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["resolution"]
        pdf_encryption_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["encryptPDF"]
        blank_page_supression_status=response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["blankPageSuppressionEnabled"]

        all_network_folder_file_setting_status=list((prefix_status,filename,user_editable_status,suffix_status,output_quality_status,file_type_status,resoultion_status,pdf_encryption_status,blank_page_supression_status))
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Network Folder File Settings", "network-folder-file",all_network_folder_file_setting_status , "Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Network Folder File Settings")

    def test_78_verify_ipv4_multicast_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify IPV4 Multicast Settings Setting API Status 
        if self.stack == "stage":
            ipv4_multicast_uri ="https://stratus-stg.tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/ioConfig/adapterConfigs/eth0"
        else:
            ipv4_multicast_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"/ioConfig/adapterConfigs/eth0"
        response = get_proxy_settings_api_response(self.stack, ipv4_multicast_uri)
        ipv4_multicast_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["multicastEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("IPv4 Multicast", "ipv4-multicast", ipv4_multicast_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("IPv4 Multicast")

    def test_79_verify_show_date_and_time_setting_in_device_specific_policy(self):
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Show Date and Time",setting_card="show-date-time",category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
 
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_next_button()
        self.devices.click_device_specific_policy_settings_card("show-date-time")
        self.devices.click_set_options_settings_checkbox("show-date-time")
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Show Date and Time")
    
    def test_80_verify_time_zone_day_light_saving_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify Time Zone/Daylight Saving Setting API Status 
        if self.stack == "stage":
            time_zone_day_light_saving_uri ="https://stratus-stg.tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/clock"
        else:
            time_zone_day_light_saving_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v1/deviceconfigs/"+device_cloud_id+"/clock"
        response = get_proxy_settings_api_response(self.stack, time_zone_day_light_saving_uri)
        time_zone_day_light_saving_status = response.json()["state"]["reported"]["cdmData"]["timeZone"]

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("Time Zone/Daylight Saving", "time-zone", time_zone_day_light_saving_status, "Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number) 

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("Time Zone/Daylight Saving")
    
    def test_81_verify_ipv4_information_setting_in_device_specific_policy(self):
        #
        #Generate Standard Values 
        ip_address = "15.4.0.200"
        subnet_mask_value = "255.255.248.0"
        gateway_value = "15.4.0.1"

        device_cloud_id = self.devices.get_device_cloud_id()

        #Verify IPv4 Information Saving Setting API Status 
        if self.stack == "stage":
            ipv4_information_uri ="https://stratus-stg.tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"ioConfig/adapterConfigs/eth0"
        else:
            ipv4_information_uri ="https://stratus-"+self.stack+".tropos-rnd.com/connector/v2/deviceconfigs/"+device_cloud_id+"ioConfig/adapterConfigs/eth0"
        response = get_proxy_settings_api_response(self.stack, ipv4_information_uri)
    
        all_ipv4_information_status =list((ip_address,subnet_mask_value,gateway_value))

        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("IPv4 Information", "ipv4-info", all_ipv4_information_status, "Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("IPv4 Information")
    
    def test_82_verify_eprint_setting_in_device_specific_policy(self):
       
        # Adding Settings in Device Specific Policy Tab
        self.devices.add_settings_in_device_specific_policy_tab("ePrint Settings",setting_card="hp-web-svc",category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(self.serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status(self.serial_number)
        
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_next_button()
        self.devices.click_device_specific_policy_settings_card("hp-web-svc")
        self.devices.set_eprint_settings_option()
 
        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("ePrint Settings")