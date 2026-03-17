import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ecp.ecp_api_utility import *
import random
pytest.app_info = "ECP"

#Generate test policy name
policy_name="auto_dsp"+str(random.randint(100,999))

#Generate test group name
group_name="auto_dsg"+str(random.randint(100,999))

# Cloud device serial number
serial_number = "MXBCG771QW"

# App Deployment Device serial number
app_deployment_serial_num = "CITRNEAPP1"

#Generate random device properties values
device_name="device_name"+str(random.randint(1,99))
company_name="company_name"+str(random.randint(1,99))

class Test_12_ECP_Cloud_Device_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_devices(self):
        #Generate test group name
        self.temp_group_name="auto_device_group"+str(random.randint(1000,9999))
        #Generate test policy name
        self.temp_policy_name="auto_policy_name"+str(random.randint(100,999))
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.click_devices_group_all_option("All")
        self.devices.verify_device_page()
        self.devices.create_group_with_one_device(self.temp_group_name,serial_number)
        return self.devices.verify_device_page()
    
    def test_01_verify_control_panel_language_policy_setting(self):
        # 
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Devices Control Panel Language
        device_control_panel_language_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/controlPanel/configuration"
        response = get_api_response(self.stack,device_control_panel_language_uri)
        current_language_status = response.json()["state"]["reported"]["cdmData"]["currentLanguage"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Control Panel Language",modify_settings="ctrl-panel-language",settings_status=current_language_status,category_type="Devices")

         #  Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name) 

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Verify Devices Control Panel Language
        response = get_api_response(self.stack,device_control_panel_language_uri)
        assert current_language_status != response.json()["state"]["reported"]["cdmData"]["currentLanguage"]
        
        # Reverting devices settings changes
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.search_policy(self.temp_policy_name)
        self.endpoint_security.click_first_entry_link()            
        self.endpoint_security.click_policy_details_card_edit_button()
        self.endpoint_security.click_create_policy_policy_settings_card("ctrl-panel-language")
        self.endpoint_security.select_control_panel_language("English")
        self.endpoint_security.click_policy_settings_save_button()
        self.endpoint_security.click_confirm_policy_save_button()
        self.endpoint_security.check_toast_successful_message("Policy has been saved successfully.")

        # Verify Devices Control Panel Language
        response = get_api_response(self.stack,device_control_panel_language_uri)
        assert "en" == response.json()["state"]["desired"]["cdmData"]["currentLanguage"]

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_03_verify_company_name_policy_setting(self):
        # 
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Company Name",modify_settings="company-name",settings_status=company_name,category_type="Devices")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Verify the contact person in device details properties tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("company-name")
        assert company_name == self.devices.get_device_details_device_property_value("company-name")

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_04_verify_device_name_policy_setting(self):
        # 
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Device Name",modify_settings="device-name",settings_status=device_name,category_type="Devices")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Verify the contact person in device details properties tab
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(serial_number)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.click_device_accordion()
        self.devices.click_device_details_device_property_card("device-name")
        assert device_name == self.devices.get_device_details_device_property_value("device-name")

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_05_verify_WS_Discovery_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Web Services Discovery Status
        network_ws_discovery_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/discoveryServices"
        response = get_api_response(self.stack,network_ws_discovery_uri)
        ws_discovery_status = response.json()["state"]["reported"]["cdmData"]["wsDiscovery"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Web Services Discovery (WS-Discovery)",modify_settings="ws-discovery",settings_status=ws_discovery_status,category_type="Network")

        #  Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_06_verify_bonjour_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Bonjour Status
        network_bonjour_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/discoveryServices"
        response = get_api_response(self.stack,network_bonjour_uri)
        bonjour_status = response.json()["state"]["reported"]["cdmData"]["bonjour"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Bonjour",modify_settings="bonjour",settings_status=bonjour_status,category_type="Network")

        # Add the policy to the device group  
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)  

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_07_verify_service_location_protocol_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify SLP Status
        network_slp_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/discoveryServices"
        response = get_api_response(self.stack,network_slp_uri)
        slp_status = response.json()["state"]["reported"]["cdmData"]["slp"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Service Location Protocol (SLP)",modify_settings="slp",settings_status=slp_status,category_type="Network")

        #  Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_08_verify_airprint_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify AirPrint Status
        network_airprint_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_airprint_uri)
        airprint_status = response.json()["state"]["reported"]["cdmData"]["airPrint"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="AirPrint",modify_settings="airprint",settings_status=airprint_status,category_type="Network")
        
        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_09_verify_internet_print_protocol_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get IPP Status
        network_ipp_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_ipp_uri)
        ipp_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ipp"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Internet Print Protocol (IPP)",modify_settings="ipp",settings_status=ipp_status,category_type="Network")
        
        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_10_verify_secure_internet_print_protocol_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get IPP Secure Status
        network_ipp_secure_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_ipp_secure_uri)
        ipp_secure_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["ippSecure"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Secure Internet Print Protocol (IPPS)",modify_settings="ipps",settings_status=ipp_secure_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_11_verify_line_printer_daemon_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get LPD/LPR Status
        network_lpd_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_lpd_uri)
        lpd_status = response.json()["state"]["reported"]["cdmData"]["lpdPrint"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Line Printer Daemon / Line Printer Remote (LPD/LPR)",modify_settings="lpd-lpr",settings_status=lpd_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_12_verify_standard_tcp_printing_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get TCP/IP Printing Status
        network_tcp_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_tcp_uri)
        tcp_status = response.json()["state"]["reported"]["cdmData"]["port9100"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Standard TCP/IP Printing (P9100)",modify_settings="tcpip-print",settings_status=tcp_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_13_verify_ws_print_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get WS-Print Status
        network_ws_print_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_ws_print_uri)
        ws_print_status = response.json()["state"]["reported"]["cdmData"]["wsPrint"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Web Services Print (WS-Print)",modify_settings="ws-print",settings_status=ws_print_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_14_verify_wins_port_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get WINS Port Status
        network_wins_port_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/nameResolverServices"
        response = get_api_response(self.stack,network_wins_port_uri)
        wins_port_status = response.json()["state"]["reported"]["cdmData"]["wins"]["winsPort"]

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="WINS Port",modify_settings="wins-port",settings_status=wins_port_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)
        
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)
        
    def test_15_verify_wins_registration_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get WINS Registration Status
        network_wins_registration_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/nameResolverServices"
        response = get_api_response(self.stack,network_wins_registration_uri)
        wins_registration_status = response.json()["state"]["reported"]["cdmData"]["wins"]["enabled"]

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="WINS Registration",modify_settings="wins-registration",settings_status=wins_registration_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_16_verify_llmnr_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get LLMNR Status
        network_llmnr_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/nameResolverServices"
        response = get_api_response(self.stack,network_llmnr_uri)
        llmnr_status = response.json()["state"]["reported"]["cdmData"]["llmnr"]["enabled"]

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Link-Local Multicast Name Resolution Protocol (LLMNR)",modify_settings="llmnr",settings_status=llmnr_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_17_verify_airprint_fax_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get AirPrint Fax Status
        network_airprint_fax_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/fax/sendConfiguration"
        response = get_api_response(self.stack,network_airprint_fax_uri)
        airprint_fax_status = response.json()["state"]["reported"]["cdmData"]["ippFaxEnabled"]

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="AirPrint Fax",modify_settings="airprint-fax",settings_status=airprint_fax_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_18_verify_airprint_scan_and_secure_scan_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get AirPrint Scan/AirPrint Secure Scan Status
        network_airprint_scan_and_secure_scan_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/networkScanServices"
        response = get_api_response(self.stack,network_airprint_scan_and_secure_scan_uri)
        airprint_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCL"]
        airprint_secure_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCLSecure"]
        all_scan_and_secure_status = list((airprint_scan_status,airprint_secure_scan_status))

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="AirPrint Scan/AirPrint Secure Scan",modify_settings="airprint-scan-secure-scan",settings_status=all_scan_and_secure_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_19_verify_dhcp_v4_compliance_policy_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get DHCPv4 FQDN compliance with RFC 4702 Status
        network_dhcp_v4_compliance_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,network_dhcp_v4_compliance_uri)
        dhcp_v4_compliance_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["address"]["dhcpFqdnRfc4702Compliance"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="DHCPv4 FQDN compliance with RFC 4702",modify_settings="dhcp-v4-compliance",settings_status=dhcp_v4_compliance_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_20_verify_ipv4_multicast_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get IPv4 Multicast Status
        network_ipv4_multicast_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,network_ipv4_multicast_uri)
        ipv4_multicast_status = response.json()["state"]["reported"]["cdmData"]["ipv4"]["multicastEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="IPv4 Multicast",modify_settings="ipv4-multicast",settings_status=ipv4_multicast_status,category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_21_verify_postscript_security_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get PostScript Security Status
        security_postscript_security_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/print/pdlConfiguration"
        response = get_api_response(self.stack,security_postscript_security_uri)
        postscript_security_status = response.json()["state"]["reported"]["cdmData"]["pclAndPostScript"]["postScriptSecurityEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="PostScript Security",modify_settings="ps-security",settings_status=postscript_security_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_22_verify_csrf_prevention_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Cross-Site Request Forgery (CSRF) Prevention Status
        security_csrf_prevention_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/systemConfig"
        response = get_api_response(self.stack,security_csrf_prevention_uri)
        csrf_prevention_status = response.json()["state"]["reported"]["cdmData"]["csrfPreventionEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Cross-Site Request Forgery (CSRF) Prevention",modify_settings="csrf-prevention",settings_status=csrf_prevention_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_23_verify_verify_certificate_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Verify Certificate for IPP/IPPS Pull Printing Status
        security_verify_certificate_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,security_verify_certificate_uri)
        verify_certificate_status = response.json()["state"]["reported"]["cdmData"]["ipp"]["enableCertificateValidation"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Verify Certificate for IPP/IPPS Pull Printing",modify_settings="verify-certificate",settings_status=verify_certificate_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_24_verify_pjl_access_commands_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Printer Job Language (PJL) Access Commands Status
        security_pjl_access_commands_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/print/configuration"
        response = get_api_response(self.stack,security_pjl_access_commands_uri)
        pjl_access_commands_status = response.json()["state"]["reported"]["cdmData"]["pjlDeviceAccessCommandsEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Printer Job Language (PJL) Access Commands",modify_settings="pjl-command",settings_status=pjl_access_commands_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_25_verify_service_access_code_setting(self):
        #
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Service Access Code",modify_settings="svc-access-code")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_26_verify_secure_boot_presence_setting(self):
        #
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Secure Boot Presence",modify_settings="secure-boot-presence")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_27_verify_intrusion_detection_presence_setting(self):
        #
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Intrusion Detection Presence",modify_settings="intrusion-detect-presence")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_28_verify_whitelisting_presence_setting(self):
        #
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Whitelisting Presence",modify_settings="whitelist-presence")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_29_verify_remote_firmware_update_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Printer Firmware Update (send as Printjob) Status
        security_remote_firmware_update_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/firmwareUpdate/configuration"
        response = get_api_response(self.stack,security_remote_firmware_update_uri)
        remote_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["pjlUpdateEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Printer Firmware Update (send as Printjob)",modify_settings="remote-fw-update",settings_status=remote_firmware_update_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_30_verify_auto_firmware_update_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Auto Firmware Update Status
        firmware_auto_firmware_update_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/firmwareUpdate/autoUpdate/configuration"
        response = get_api_response(self.stack,firmware_auto_firmware_update_uri)
        auto_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["scheduleEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Auto Firmware Update",modify_settings="auto-fw-update",settings_status=auto_firmware_update_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_31_verify_direct_connect_ports_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Direct Connect Ports Status
        security_direct_connect_ports_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/ioConfig/adapterConfigs/usb"
        response = get_api_response(self.stack,security_direct_connect_ports_uri)
        direct_connect_ports_status = response.json()["state"]["reported"]["cdmData"]["enabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Direct Connect Ports",modify_settings="dc-ports",settings_status=direct_connect_ports_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)
        
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_32_verify_require_https_redirect_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Require HTTPS Redirect Status
        security_require_https_redirect_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/systemConfig"
        response = get_api_response(self.stack,security_require_https_redirect_uri)
        require_https_redirect_status = response.json()["state"]["reported"]["cdmData"]["httpsRedirectionEnabled"]
        
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Require HTTPS Redirect",modify_settings="https-redirect",settings_status=require_https_redirect_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_33_verify_embedded_web_server_access_setting(self):
        #
        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Embedded Web Server Access",modify_settings="ews-access")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        if self.endpoint_security.get_device_detail_policy_tab_compliance_status() != "Compliant":
            if self.endpoint_security.get_policies_compliance_status_widget_compliance_status_reason() != "Unsupported":
                self.home.click_policies_menu_btn()
                self.endpoint_security.click_policies_tab()
                self.endpoint_security.search_policy(self.temp_policy_name)
                self.endpoint_security.click_policy_checkbox()
                self.endpoint_security.click_contextual_footer_select_action_dropdown()
                self.endpoint_security.select_action_dropdown_option("edit")
                self.endpoint_security.click_contextual_footer_continue_button()
                self.endpoint_security.click_create_policy_policy_settings_card("ews-access")
                self.endpoint_security.click_set_options_settings_checkbox("ews-access")
                self.endpoint_security.click_policy_save_button()
                self.endpoint_security.click_confirm_policy_save_button()
                self.endpoint_security.click_are_you_sure_popup_save_button()
                self.home.click_devices_menu_btn()
                self.devices.navigating_to_device_details_tab(self.temp_group_name)
                assert self.endpoint_security.get_device_detail_policy_tab_compliance_status() == "Compliant"
        
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)
    
    def test_34_verify_control_panel_timeout_setting(self): 
        #
        # Generate random number
        generate_timeout_value=random.randint(10,30)
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Control Panel Timeout Status
        control_panel_timeout_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/power/configuration"
        response = get_api_response(self.stack,control_panel_timeout_uri)
        control_panel_timeout_status = response.json()["state"]["reported"]["cdmData"]["inactivityTimeout"]

        # Creating the Policy  
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Control Panel Timeout",modify_settings="ctrl-panel-timeout",settings_status=generate_timeout_value)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_35_verify_disk_encryption_status_setting(self):
        #
        # Creating the Policy  
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Disk Encryption Status",modify_settings="disk-encryption")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        if self.endpoint_security.get_device_detail_policy_tab_compliance_status() != "Compliant":
            if self.endpoint_security.get_policies_compliance_status_widget_compliance_status_reason() != "Unsupported":
                self.home.click_policies_menu_btn()
                self.endpoint_security.click_policies_tab()
                self.endpoint_security.search_policy(self.temp_policy_name)
                self.endpoint_security.click_policy_checkbox()
                self.endpoint_security.click_contextual_footer_select_action_dropdown()
                self.endpoint_security.select_action_dropdown_option("edit")
                self.endpoint_security.click_contextual_footer_continue_button()
                self.endpoint_security.click_create_policy_policy_settings_card("disk-encryption")
                self.endpoint_security.click_set_options_settings_checkbox("disk-encryption")
                self.endpoint_security.click_policy_save_button()
                self.endpoint_security.click_confirm_policy_save_button()
                self.endpoint_security.click_are_you_sure_popup_save_button()
                self.home.click_devices_menu_btn()
                self.devices.navigating_to_device_details_tab(self.temp_group_name)
                assert self.endpoint_security.get_device_detail_policy_tab_compliance_status() == "Compliant"
       
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_36_verify_snmp_v1v2_settings(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get SNMPv1/v2 Status
        security_snmp_v1v2_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/snmpconfig"
        response = get_api_response(self.stack,security_snmp_v1v2_uri)
        snmp_v1v2_status = response.json()["state"]["reported"]["cdmData"]["snmpV1V2Config"]["accessOption"]
       
        # Navigating to Properties Tab to edit the SNMP V1/V2 setting
        self.devices.click_device_details_properties_tab()
        self.devices.click_security_accordion()
        self.devices.verify_security_snmp_v1_v2_properties_tab_setting_title()
        self.devices.click_device_details_device_property_card("snmp-v1-v2")

        # Update Settings in Properties Tab
        if snmp_v1v2_status == "readWrite":
            self.devices.get_device_details_device_property_value("snmp-v1-v2-read-write-access") == "Read and Write Enabled"
            self.devices.click_edit_button_from_settings_list_in_properties_tab("snmp-v1-v2")
            self.endpoint_security.click_snmp_v1v2_read_only_radio_btn()
            self.devices.click_edit_setting_popup_save_button()

            # Get SNMPv1/v2 Updated API Status
            response = get_api_response(self.stack,security_snmp_v1v2_uri)
            assert "readOnly" == response.json()["state"]["desired"]["cdmData"]["snmpV1V2Config"]["accessOption"]

            self.devices.verify_snmp_v1v2_read_only_update_status_in_properties_tab() 
        else:
            self.devices.get_device_details_device_property_value("snmp-v1-v2-read-write-access") == "Read Only Enabled"
            self.devices.click_edit_button_from_settings_list_in_properties_tab("snmp-v1-v2")
            self.endpoint_security.click_snmp_v1v2_read_write_radio_btn()
            self.devices.enter_snmp_v1v2_read_community_name_password_textbox("1")
            self.devices.enter_snmp_v1v2_read_community_name_confirm_password_textbox("1")
            self.devices.enter_snmp_v1v2_read_write_community_name_password_textbox("1")
            self.devices.enter_snmp_v1v2_read_write_community_name_confirm_password_textbox("1")
            self.devices.click_edit_setting_popup_save_button()

            # Get SNMPv1/v2 Updated API Status
            response = get_api_response(self.stack,security_snmp_v1v2_uri)
            snmp_v1v2_status != response.json()["state"]["desired"]["cdmData"]["snmpV1V2Config"]["accessOption"]

            self.devices.verify_snmp_v1v2_read_and_write_update_status_in_properties_tab()

        # Clean up the device group
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_37_verify_snmp_v3_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get SNMPv3 Status
        security_snmp_v3_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/snmpconfig"
        response = get_api_response(self.stack,security_snmp_v3_uri)
        snmp_v3_status = response.json()["state"]["reported"]["cdmData"]["snmpV3Config"]["enabled"]
       
        # Navigating to Properties Tab to edit the SNMP V3 setting
        self.devices.click_device_details_properties_tab()
        self.devices.click_security_accordion()
        self.devices.verify_security_snmp_v3_properties_tab_setting_title()
        self.devices.click_device_details_device_property_card("snmp-v3")

        # Update Settings in Properties Tab
        if snmp_v3_status == "false":
            self.devices.get_device_details_device_property_value("snmp-v3-enabled") == "Disabled"
            self.devices.click_edit_button_from_settings_list_in_properties_tab("snmp-v3")
            self.endpoint_security.click_snmp_v3_option()
            self.devices.enter_snmp_v3_username_textbox("SNMP_Auto")
            self.devices.update_snmp_v3_authentication_passphase("Test123$")
            self.devices.click_edit_setting_popup_save_button()
        
            # Get SNMPv3 Updated API Status
            response = get_api_response(self.stack,security_snmp_v3_uri)
            snmp_v3_status != response.json()["state"]["desired"]["cdmData"]["snmpV3Config"]["enabled"]
            self.devices.verify_snmp_v3_enabled_status_in_properties_tab()
        else:
            self.devices.get_device_details_device_property_value("snmp-v3-enabled") == "Enabled"
            self.devices.click_edit_button_from_settings_list_in_properties_tab("snmp-v3")
            self.endpoint_security.click_snmp_v3_option()
            self.devices.click_edit_setting_popup_save_button()

            # Get SNMPv3 Updated API Status
            response = get_api_response(self.stack,security_snmp_v3_uri)
            snmp_v3_status != response.json()["state"]["reported"]["cdmData"]["snmpV3Config"]["enabled"]
            self.devices.verify_snmp_v3_disabled_status_in_properties_tab()

        # Clean up the device group
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_38_verify_host_usb_plug_and_play_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Host USB Plug and Play Status
        security_host_usb_plug_and_play_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/usbHost/configuration"
        response = get_api_response(self.stack,security_host_usb_plug_and_play_uri)
        plug_and_play_status = response.json()["state"]["reported"]["cdmData"]["plugAndPlayEnabled"]
        print_from_usb_status = response.json()["state"]["reported"]["cdmData"]["printFromUsbEnabled"]
        scan_to_usb_status = response.json()["state"]["reported"]["cdmData"]["scanToUsbEnabled"]
        all_plug_and_play_status = list((plug_and_play_status,print_from_usb_status,scan_to_usb_status))
       
        # Creating the Policy  
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Host USB Plug and Play",modify_settings="host-usb-pnp",settings_status=all_plug_and_play_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_39_verify_file_system_access_protocol_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get File System Access Protocol Status
        file_system_access_protocol_setting_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/print/configuration"
        response = get_api_response(self.stack,file_system_access_protocol_setting_uri)
        ps_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["psFileSystemAccessEnabled"]
        pjl_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["pjlDeviceAccessCommandsEnabled"]

        all_file_system_access_protocol_setting_status = list((ps_file_system_access_enabled_status,pjl_file_system_access_enabled_status))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="File System Access Protocols",modify_settings="fs-access-protocol",settings_status=all_file_system_access_protocol_setting_status,category_type="File System")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_40_verify_ews_information_protection_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Information Tab Status
        information_tab_setting_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/ews/configuration"
        response = get_api_response(self.stack,information_tab_setting_uri)
        information_tab_status = response.json()["state"]["reported"]["cdmData"]["informationTabAccess"]
        display_job_log_status = response.json()["state"]["reported"]["cdmData"]["displayJobLogOnInformationTab"]
        display_print_job_log_status = response.json()["state"]["reported"]["cdmData"]["displayPrintPageOnInformationTab"]
        all_information_tab_setting_status = list((information_tab_status,display_job_log_status,display_print_job_log_status))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_information_tab_setting_policy(self.temp_policy_name,policy_settings="EWS Information Protection",modify_settings="info-tab",settings_status=all_information_tab_setting_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_41_verify_printer_job_language_password_setting(self): 
        #
        # Generate Random Password
        password = "12345"+str(random.randint(1,9))

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get PJL Password Setting API Status
        pjl_password_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/print/configuration"
        response = get_api_response(self.stack,pjl_password_uri)
        pjl_password_status = response.json()["state"]["reported"]["cdmData"]["pjlPasswordConfigured"]

        # Navigating to Properties Tab to edit the Authentication 802.1x setting
        self.devices.click_device_details_properties_tab()
        self.devices.click_security_accordion()
        self.devices.verify_security_pjl_password_properties_tab_setting_title()

        # Update Settings in Properties Tab
        if pjl_password_status == "false":
            self.devices.click_device_details_device_property_card("pjl-password")
            self.devices.get_device_details_device_property_value("pjl-password") == "Not Configured"
            self.devices.click_edit_button_from_settings_list_in_properties_tab("pjl-password")
            self.devices.enter_properties_tab_pjl_password_textbox_value(password)
            self.devices.enter_properties_tab_pjl_confirm_password_textbox_value(password)
            self.devices.click_edit_setting_popup_save_button()

            # Get PJL Password Updated API Status
            response = get_api_response(self.stack,pjl_password_uri)
            password == response.json()["state"]["desired"]["cdmData"]["pjlPassword"]

            self.devices.verify_pjl_password_configuration_update_in_properties_tab()
        else:
            self.devices.click_device_details_device_property_card("pjl-password")
            self.devices.get_device_details_device_property_value("pjl-password") == "Configured"

        # Clean up the device group
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_42_verify_save_to_network_folder_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Save To Network Folder Status
        save_to_network_folder_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/scan/destinationConfig"
        response = get_api_response(self.stack,save_to_network_folder_uri)
        save_to_network_folder_status = response.json()["state"]["reported"]["cdmData"]["folderEnabled"]

        # Creating the Policy  
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Save To Network Folder",modify_settings="save-to-network-folder",settings_status=save_to_network_folder_status,category_type="Digital Sending")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)
   
    def test_43_verify_save_to_sharepoint_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Save To SharePoint Status
        save_to_sharepoint_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/scan/destinationConfig"
        response = get_api_response(self.stack,save_to_sharepoint_uri)
        save_to_sharepoint_status = response.json()["state"]["reported"]["cdmData"]["sharePointEnabled"]

        # Creating the Policy  
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Save To SharePoint",modify_settings="save-to-share-point",settings_status=save_to_sharepoint_status,category_type="Digital Sending")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_44_verify_send_to_email_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Send To Email Status
        send_to_email_setting_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/scan/destinationConfig"
        response = get_api_response(self.stack, send_to_email_setting_uri)
        send_to_email_status = response.json()["state"]["reported"]["cdmData"]["emailEnabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Send To Email", modify_settings="save-to-email", settings_status=send_to_email_status,category_type="Digital Sending")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_45_verify_time_services_setting(self):
        #
        #Generate random service and port address
        time_services_address="ntp.pool.org"
        local_port=random.randint(1100,1900)
        synchronize_time=random.randint(1,168)

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Time Services Status
        embedded_time_services_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/clock/configuration"
        response = get_api_response(self.stack,embedded_time_services_uri)
        time_services_system_time_sync = response.json()["state"]["reported"]["cdmData"]["systemTimeSync"]

        time_services_status = list((time_services_system_time_sync,time_services_address,local_port,synchronize_time))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Time Services", modify_settings="time-services", settings_status=time_services_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    @pytest.mark.skip #This Setting is deffered from Batch 0 Settings
    def test_46_verify_web_encryption_settings_or_active_ciphers(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Web Encryption Settings or Active Ciphers Status
        web_encryption_settings_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/tlsConfig/configuration"
        response = get_api_response(self.stack,web_encryption_settings_uri)
        tls_minimum_protocol_version = response.json()["state"]["reported"]["cdmData"]["minProtocolVersion"]
        tls_maximum_protocol_version = response.json()["state"]["reported"]["cdmData"]["maxProtocolVersion"]

        web_encryption_status = list((tls_minimum_protocol_version,tls_maximum_protocol_version))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Web Encryption Settings or Active Ciphers", modify_settings="web-encryption", settings_status=web_encryption_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_47_verify_file_system_file_erase_mode_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get File Erase Mode Status
        file_erase_mode_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/storageDevices/configuration"
        response = get_api_response(self.stack,file_erase_mode_uri)
        file_erase_mode_status = response.json()["state"]["reported"]["cdmData"]["fileEraseMode"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="File Erase Mode", modify_settings="file-erase", settings_status=file_erase_mode_status,category_type="File System")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_48_verify_retain_print_jobs_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Retain Print Jobs Status
        retain_print_jobs_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/storeJobManagement/configuration"
        response = get_api_response(self.stack,retain_print_jobs_uri)
        stored_jobs_enabled_status = response.json()["state"]["reported"]["cdmData"]["storeJobEnabled"]
        temporary_stored_job_status = response.json()["state"]["reported"]["cdmData"]["temporaryJobRetentionInMinutes"]
        standard_stored_job_status = response.json()["state"]["reported"]["cdmData"]["standardJobRetentionInMinutes"]

        retain_print_jobs_status = list((stored_jobs_enabled_status,temporary_stored_job_status,standard_stored_job_status))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Retain Print Jobs", modify_settings="retain-jobs", settings_status=retain_print_jobs_status,category_type="Devices")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_49_fax_receive_settings(self):
        #
        # Generate random rings to answer value
        rings_to_answer_status = random.randint(1,6)

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Fax Receive Settings
        fax_receive_settings_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/faxReceive/configuration"
        response = get_api_response(self.stack,fax_receive_settings_uri)
        fax_receive_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveEnabled"]
        fax_receive_method_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveMethod"]

        # Verify Fax Receive Set Internal Modem settings Status
        fax_receive_set_internal_modem_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/faxModem/configuration"
        response = get_api_response(self.stack,fax_receive_set_internal_modem_uri)
        ringer_volume_status = response.json()["state"]["reported"]["cdmData"]["analogFaxReceiveSettings"]["ringerVolume"]

        all_fax_receive_settings_status = list((fax_receive_status,fax_receive_method_status,ringer_volume_status,rings_to_answer_status))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Fax Receive Settings", modify_settings="fax-receive", settings_status=all_fax_receive_settings_status,category_type="Fax")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_50_verify_email_address_settings(self):
        #
        # Generate random values 
        default_from_email = "autotest"+str(random.randint(1,9))+"@hp.com"
        default_display_name = "Auto Test"+str(random.randint(1,9))
        email_subject_name = "Sample Email Testing"+str(random.randint(1,9))
        email_body_message = "Auto Test Sanity"+str(random.randint(1,9))

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Email Address / Message Settings
        email_address_message_settings_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/jobTicket/configuration/defaults/scanEmail"
    
        response = get_api_response(self.stack,email_address_message_settings_uri)

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

        email_address_message_settings_status = list((address_filed_restrictions,default_from_value,default_from_email,default_display_name,default_from_user_editable,to_sign_in_required,user_editable_to,cc_sign_in_required,user_ediatable_cc,
                                                      bcc_sign_in_required,user_editable_bcc,email_subject_name,user_editable_subject,email_body_message,user_editable_body,allow_invaild_email_address,email_message_user_editable,encrypt_email_user_editable))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Email Address / Message Settings", modify_settings="email-message", settings_status=email_address_message_settings_status,category_type="Digital Sending")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_51_verify_telnet_settings(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Telnet Settings
        telnet_settings_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/jetdirectServices"
        response = get_api_response(self.stack,telnet_settings_uri)
        telnet_status = response.json()["state"]["reported"]["cdmData"]["telnetEnabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Telnet", modify_settings="telnet", settings_status=telnet_status, category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_52_tftp_configuration_file_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get TFTP Configuration File Settings
        tftp_configuration_file_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/jetdirectServices"
        response = get_api_response(self.stack,tftp_configuration_file_uri)
        tftp_status = response.json()["state"]["reported"]["cdmData"]["tftpEnabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="TFTP Configuration File", modify_settings="tftp-cfg", settings_status=tftp_status, category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)
        
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_53_hp_jetdirect_xml_services_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get HP JetDirect XML Services Settings
        hp_jetdirect_xml_services_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/jetdirectServices"
        response = get_api_response(self.stack,hp_jetdirect_xml_services_uri)
        hp_jetdirect_xml_status = response.json()["state"]["reported"]["cdmData"]["xdmEnabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="HP Jetdirect XML Services", modify_settings="jd-xml-svc", settings_status=hp_jetdirect_xml_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)
        
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)
     
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    # Commenting the below testcases, as app deployement testcases moved to test_13_cloud_device_app_deployment_setting.py file
    # def test_54_verify_app_deployment_ui_policy_setting(self):
    #     #
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.click_policies_tab()                                                    
    #     self.endpoint_security.verify_table_loaded()
    #     self.endpoint_security.create_policy_for_app_deployment(self.temp_policy_name,policy_settings="App Deployment",modify_settings="app-deployment",category_type="Solutions")
 
    #     # Veriying the table is loaded or not
    #     self.endpoint_security.verify_table_loaded()
   
    # def test_55_verify_app_deployment_setting_for_printer_on_agent_app(self):
    #     #
    #     self.devices.delete_group(self.temp_group_name)
    #     self.devices.verify_device_page()
    #     self.devices.create_group_with_one_device(self.temp_group_name,app_deployment_serial_num)
       
    #     # Creating the Policy
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.click_policies_tab()
    #     self.endpoint_security.verify_table_loaded()
    #     self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="App Deployment",modify_settings="app-deployment",category_type="Solutions")
 
    #     # Add the policy to the device group
    #     self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)
   
    #     # Verify the compliance status of that device.
    #     self.home.click_devices_menu_btn()
    #     self.devices.navigating_to_device_details_tab(self.temp_group_name)
    #     self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)
 
    #     # Uninstalling the Printer On Agent App
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.click_policies_tab()
    #     self.endpoint_security.search_policy(self.temp_policy_name)
    #     self.endpoint_security.click_policy_checkbox()
    #     self.endpoint_security.click_contextual_footer_select_action_dropdown()
    #     self.endpoint_security.select_action_dropdown_option("edit")
    #     self.endpoint_security.click_contextual_footer_continue_button()
    #     self.endpoint_security.click_create_policy_policy_settings_card("app-deployment")
    #     self.endpoint_security.uninstal_added_app_in_app_deployment_settings()
    #     self.endpoint_security.click_policy_save_button()

    #     # Verify the compliance status of that device.
    #     self.home.click_devices_menu_btn()
    #     self.devices.navigating_to_device_details_tab(self.temp_group_name)
    #     self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)
    
    #     # Clean up the policy and device group
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
    #     self.home.click_devices_menu_btn()
    #     self.devices.delete_group(self.temp_group_name)

    # def test_56_verify_app_deployment_setting_for_regus_plugin_app(self):
    #     #
    #     self.devices.delete_group(self.temp_group_name)
    #     self.devices.verify_device_page()
    #     self.devices.create_group_with_one_device(self.temp_group_name,app_deployment_serial_num)

    #     # Creating the Policy
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.click_policies_tab()
    #     self.endpoint_security.verify_table_loaded()
    #     self.endpoint_security.create_policy_for_app_deployment_with_regus_plugin(self.temp_policy_name,policy_settings="App Deployment",modify_settings="app-deployment")

    #     # Add the policy to the device group
    #     self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

    #     # Verify the compliance status of that device.
    #     self.home.click_devices_menu_btn()
    #     self.devices.navigating_to_device_details_tab(self.temp_group_name)
    #     self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

    #     # Uninstalling the Regus Plugin App
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.click_policies_tab()
    #     self.endpoint_security.search_policy(self.temp_policy_name)
    #     self.endpoint_security.click_policy_checkbox()
    #     self.endpoint_security.click_contextual_footer_select_action_dropdown()
    #     self.endpoint_security.select_action_dropdown_option("edit")
    #     self.endpoint_security.click_contextual_footer_continue_button()
    #     self.endpoint_security.click_create_policy_policy_settings_card("app-deployment")
    #     self.endpoint_security.uninstal_added_app_in_app_deployment_settings()
    #     self.endpoint_security.click_policy_save_button()

    #     # Verify the compliance status of that device.
    #     self.home.click_devices_menu_btn()
    #     self.devices.navigating_to_device_details_tab(self.temp_group_name)
    #     self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

    #     # Clean up the policy and device group
    #     self.home.click_policies_menu_btn()
    #     self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
    #     self.home.click_devices_menu_btn()
    #     self.devices.delete_group(self.temp_group_name)

    def test_57_verify_printer_firmware_sha1_code_signing_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Printer Firmware SHA1 Code Signing Settings
        legacy_firmware_update_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/firmwareUpdate/configuration"
        response = get_api_response(self.stack,legacy_firmware_update_uri)
        legacy_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["sha1ValidationEnabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Printer Firmware SHA1 Code Signing", modify_settings="legacy-fw-update", settings_status=legacy_firmware_update_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)
        
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)
       
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_58_verify_add_web_services_settings_smart_cloud_print_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Smart Cloud Print Settings
        smart_cloud_print_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/legacyAttributes"
        response = get_api_response(self.stack,smart_cloud_print_uri)
        smart_cloud_print_status = response.json()["state"]["reported"]["cdmData"]["webServices"]["cloudPrint"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Smart Cloud Print", modify_settings="smart-cloud-print", settings_status=smart_cloud_print_status, category_type="Web Services")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)
        
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)
     
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)
    
    def test_59_verify_add_network_ftp_print_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get FTP Print Settings
        network_ftp_print_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/network/printServices"
        response = get_api_response(self.stack,network_ftp_print_uri)
        ftp_print_status = response.json()["state"]["reported"]["cdmData"]["ftpPrint"]["enabled"]

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="FTP Print", modify_settings="ftp-print", settings_status=ftp_print_status, category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)
        
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)
        
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_60_verify_sleep_settings(self):
        #
        #Generate Random Values 
        sleep_mode_values=random.randint(0,43)
        auto_off_after_sleep_values=random.randint(15,59)

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Sleep Settings Setting API Status
        sleep_settings_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/power/sleepConfiguration"
        response = get_api_response(self.stack, sleep_settings_uri)
        #sleep_auto_off_timer_status=response.json()["state"]["reported"]["cdmData"]["sleepAutoOffTimerEnabled"] # Auto Timer attribute was removed from application
        auto_on_events_status=response.json()["state"]["reported"]["cdmData"]["autoOnEvents"]

        all_sleep_settings_status =list((sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values))

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Sleep Settings", modify_settings="sleep-settings", settings_status=all_sleep_settings_status, category_type="Devices")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name, self.temp_policy_name)
        
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_61_verify_bootloader_password_setting_from_properties_tab(self):
        random_password = "430"+str(random.randint(1,9))

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Bootloader Password Setting API Status
        bootloader_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/bootloader"
        response = get_api_response(self.stack, bootloader_uri)
        bootloader_password_status = response.json()["state"]["reported"]["cdmData"]["passwordSet"]

        # Get Bootloader Password Setting UI Status
        self.devices.click_device_details_properties_tab()
        self.devices.click_security_accordion()
        self.devices.click_device_details_device_property_card("bootloader-password")
        if self.devices.get_device_details_device_property_value("bootloader-password") == "Configured":
            bootloader_password_status == "true"

        # Updating the new Password
        self.devices.click_edit_button_from_settings_list_in_properties_tab("bootloader-password")
        self.devices.enter_bootloader_current_password("1234")
        self.devices.enter_bootloader_new_password(random_password)
        self.devices.enter_bootloader_confirm_password(random_password)
        self.devices.click_edit_setting_popup_save_button()

        # Get Bootloader new password API Status
        bootloader_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/bootloader"
        response = get_api_response(self.stack, bootloader_uri)
        assert random_password == response.json()["state"]["desired"]["cdmData"]["proposedPassword"]

    def test_62_verify_cross_origin_resource_sharing_setting(self):
        random_site_name = "www.autotest"+str(random.randint(1,9))+".com"
        random_site_name_2 = "www.test"+str(random.randint(1,9))+".com"

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Cross-Origin Resource Sharing (CORS) Status
        cross_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/systemConfig"
        response = get_api_response(self.stack,cross_uri)
        cross_enable_status = response.json()["state"]["reported"]["cdmData"]["corsEnabled"]
        cross_setting_status = list((cross_enable_status,random_site_name,random_site_name_2))

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Cross-Origin Resource Sharing (CORS)",modify_settings="cors",settings_status=cross_setting_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_63_verify_printer_firmware_update_setting(self):
        #
        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name, policy_settings="Printer Firmware Update (send as Printjob)", modify_settings="remote-fw-update")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Revert the setting and verify the remediation status
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.search_policy(self.temp_policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_create_policy_policy_settings_card("remote-fw-update")
        self.endpoint_security.click_printer_firmware_sha1_code_signing_checkbox()
        self.endpoint_security.click_policy_save_button()
        self.endpoint_security.click_confirm_policy_save_button()
        self.endpoint_security.click_are_you_sure_popup_save_button()

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_64_verify_configuration_precedence_setting(self):
        #
        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Verify Configuration Precedence API Status
        configuration_precedence_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v2/"+device_cloud_id+"/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,configuration_precedence_uri)

        # Convert the Response object to a Python dictionary using .json()
        response_data = response.json()

        # Accessing the first item from the ipConfigPrecedence and extracting the precedence and method
        ip_config = response_data["state"]["reported"]["cdmData"]["ipConfigPrecedence"]

        # Accessing the first entry in the list (index 0)
        configuration_precedence = ip_config[0]["precedence"]
        configuration_method = ip_config[0]["method"]

        configuration_precedence_status =list((configuration_precedence,configuration_method))

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Configuration Precedence",modify_settings="configuration-precedence",settings_status=configuration_precedence_status, category_type="Network")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)

    def test_65_verify_restrict_color_setting(self):
        #
        application_name = "HP Smart"+str(random.randint(1,9))

        self.devices.click_first_entry_link()
        device_cloud_id = self.devices.get_device_cloud_id()

        # Get Restrict Color Setting API Status
        restrict_color_uri = "https://devices."+self.stack+"-us1.api.ws-hp.com/devices/v1/"+device_cloud_id+"/security/legacyAttributes"
        response = get_api_response(self.stack,restrict_color_uri)
        color_settings = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["restrictColor"]
        restrict_by_user_permissions = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingPermissionSets"]
        restrict_by_application = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingApplicationSettings"]
        default_permission = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["allowColorAndQuality"]

        restrict_color_status = list((color_settings,restrict_by_user_permissions,restrict_by_application,default_permission,application_name))

        # Creating the Policy   
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(self.temp_policy_name,policy_settings="Restrict Color",modify_settings="restrict-color",settings_status=restrict_color_status)

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(self.temp_group_name,self.temp_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(self.temp_group_name)
        self.endpoint_security.verify_policies_compliance_status(serial_number)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(self.temp_group_name, self.temp_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(self.temp_group_name)