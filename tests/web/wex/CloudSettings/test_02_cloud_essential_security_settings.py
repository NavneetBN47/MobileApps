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
# Generate Service Access Code Password
service_access_code_password = random.randint(10000000,99999999)

class Test_02_Workforce_Essential_Security_CloudSettings(object):

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

    def test_01_verify_require_https_redirect_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Require HTTPS Redirect Status
        require_https_redirect_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/systemConfig"
        response = get_cloud_api_response(self.stack,require_https_redirect_uri)
        require_https_redirect_status = response.json()["state"]["reported"]["cdmData"]["httpsRedirectionEnabled"]

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Require HTTPS Redirect",setting_card="https-redirect",settings_value=require_https_redirect_status,category_type="Security")

        self.printers.dismiss_toast()

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Require HTTPS Redirect")

    def test_02_verify_auto_firmware_update_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Auto Firmware Update Status
        auto_firmware_update_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/firmwareUpdate/autoUpdate/configuration"
        response = get_cloud_api_response(self.stack,auto_firmware_update_uri)
        auto_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["scheduleEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Auto Firmware Update",setting_card="auto-fw-update",settings_value=auto_firmware_update_status,category_type="Firmware")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Auto Firmware Update")

    def test_03_verify_file_system_access_protocol_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get File System Access Protocols API Status
        file_system_access_protocol_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/print/configuration"
        response = get_cloud_api_response(self.stack,file_system_access_protocol_uri)
        ps_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["psFileSystemAccessEnabled"]
        pjl_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["pjlFileSystemAccessEnabled"]

        all_file_system_protocol_setting_status = list((ps_file_system_access_enabled_status,pjl_file_system_access_enabled_status))

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="File System Access Protocols",setting_card="fs-access-protocol",settings_value=all_file_system_protocol_setting_status,category_type="File System")
        
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("File System Access Protocols")

    def test_04_verify_pjl_access_commands_setting_in_device_specific_policy(self):
        #              
        device_cloud_id = self.printers.get_device_cloud_id()
 
         # Verify PJL Access Commands API Status
        pjl_access_commands_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/print/configuration"
        response = get_cloud_api_response(self.stack,pjl_access_commands_uri)
        pjl_access_commands_status = response.json()["state"]["reported"]["cdmData"]["pjlDeviceAccessCommandsEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Printer Job Language (PJL) Access Commands",setting_card="pjl-command",settings_value= pjl_access_commands_status,category_type="Security")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Printer Job Language (PJL) Access Commands")

    def test_05_verify_check_for_latest_firmware_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Check for Latest Firmware",setting_card="check-latest",category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Check for Latest Firmware")

    # Both SNMP V1/V2 and V3 merged into single test case as SNMP settings
    def test_06_verify_snmpv1v2_read_only_and_snmpv3_enable_settings_in_device_specific_policy(self):
        # Randam numbers
        username = "User"+str(random.randint(1,99))
        min_password_length = 8
        snmpv3_max_attempts = random.randint(5,30)
        snmpv3_reset_attempts_after_sec = random.randint(1,100)
        lockout_duration_min = random.randint(5,1000)
 
        snmp_satus = list((username,min_password_length,snmpv3_max_attempts,snmpv3_reset_attempts_after_sec,lockout_duration_min))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="SNMP",setting_card="snmp",settings_value= snmp_satus,category_type="Security")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Disable both SNMP v1/V2 and V3 settings in Device-specific Policy tab
        self.printers.update_snmpv1v2_and_v3_setting_attributes_as_disable(setting_card="snmp")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Update SNMP V1/V2 setting value as read and write and leave SNMPV3 in disable state.
        self.printers.update_snmpv1v2_and_v3_setting_attributes_as_read_write_and_disable(setting_card="snmp")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("SNMP")

    def test_07_verify_telnet_config_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Telnet API Status
        network_telnet_config_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/jetdirectServices"
        response = get_cloud_api_response(self.stack,network_telnet_config_uri)
        telnet_config_status = response.json()["state"]["reported"]["cdmData"]["telnetEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Telnet",setting_card="telnet",settings_value= telnet_config_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Telnet")

    def test_08_verify_service_access_code_settings_in_device_specific_policy(self):
        #      
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Service Access Code",setting_card="svc-access-code",settings_value=service_access_code_password,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.    
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Service Access Code")

    # As of now PJL password setting is not supported, hence this test case is skipped.
    @pytest.mark.skip
    def test_09_verify_printer_job_language_password_setting_in_security_widget_properties_tab(self):
        #             
        # Generate Random Password
        password = "12345"+str(random.randint(1,9))

        device_cloud_id = self.printers.get_device_cloud_id()

        # Get PJL Password Setting API Status
        pjl_password_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/print/configuration"
        response = get_cloud_api_response(self.stack,pjl_password_uri)
        pjl_password_status = response.json()["state"]["reported"]["cdmData"]["pjlPasswordConfigured"]

        # Navigating to Properties Tab to edit the PJL Password setting
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_security_accordion()

        # Update Settings in Properties Tab
        if pjl_password_status == "false":
            self.printers.click_printer_device_details_device_property_card("pjl-password")
            self.printers.get_printer_device_details_device_property_value("pjl-password") == "Not Configured"
            self.printers.click_printer_device_details_device_property_edit_button("pjl-password")
            self.printers.enter_properties_tab_pjl_password_textbox_value(password)
            self.printers.enter_properties_tab_pjl_confirm_password_textbox_value(password)
            self.printers.click_edit_setting_popup_save_button()

            # Get PJL Password Updated API Status
            response = get_cloud_api_response(self.stack,pjl_password_uri)
            password == response.json()["state"]["desired"]["cdmData"]["pjlPassword"]

            self.printers.verify_pjl_password_configuration_update_in_properties_tab(self.serial_number)
        else:
            self.printers.click_printer_device_details_device_property_card("pjl-password")
            self.printers.get_printer_device_details_device_property_value("pjl-password") == "Configured"

    def test_10_verify_embedded_web_server_password_setting_in_device_specific_policy(self):
        #            
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Embedded Web Server (EWS) Admin Password Setting API Status
        ews_password_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/authenticationAgents/deviceAdmin"
        response = get_cloud_api_response(self.stack,ews_password_uri)
        ews_password_status = response.json()["state"]["reported"]["cdmData"]["passwordSet"]

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Embedded Web Server (EWS) Admin Password",setting_card="ews-password",settings_value= ews_password_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Embedded Web Server (EWS) Admin Password")