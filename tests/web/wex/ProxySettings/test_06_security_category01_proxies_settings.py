import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

#Generate random device properties values
company_name="company"+str(random.randint(1,99))

class Test_06_Security_Category01_Proxies_Settings(object):

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
        self.security_category_proxy_serial_number = self.account["security_category_proxy_serial_number"]

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
        if self.security_category_proxy_serial_number != "":
            self.serial_number = self.security_category_proxy_serial_number
        self.printers.search_printers(self.serial_number)
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        return self.printers.click_printers_details_page_policies_tab()

    def test_01_verify_require_https_redirect_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Require HTTPS Redirect Status
        require_https_redirect_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/systemConfig"
        response = get_api_response(self.stack,require_https_redirect_uri)
        require_https_redirect_status = response.json()["state"]["reported"]["cdmData"]["httpsRedirectionEnabled"]

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Require HTTPS Redirect",setting_card="https-redirect",settings_value=require_https_redirect_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # # Verify Assessment status
        # self.printers.click_printers_details_page_hp_secure_fleet_manager_tab()
        # self.printers.verify_assessment_status_report(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Require HTTPS Redirect")

    def test_02_verify_pjl_access_commands_settings_in_device_specific_policy(self):
        #              
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify PJL Access Commands API Status
        pjl_access_commands_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/print"
        response = get_api_response(self.stack,pjl_access_commands_uri)
        pjl_access_commands_status = response.json()["state"]["reported"]["cdmData"]["pjlDeviceAccessCommandsEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Printer Job Language (PJL) Access Commands",setting_card="pjl-command",settings_value= pjl_access_commands_status,category_type="Security")
       
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Printer Job Language (PJL) Access Commands")

    def test_03_verify_snmpv1v2_read_only_and_snmpv3_enable_settings_in_device_specific_policy(self):
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

    def test_04_verify_printer_firmware_update_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Printer Firmware Update (send as Printjob)",setting_card="remote-fw-update",category_type="Security")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Revert the setting and verify the remediation status
        self.printers.click_printers_details_policies_tab_edit_button()
        self.printers.click_device_specific_policy_next_button()
        self.printers.click_device_specific_policy_settings_card("remote-fw-update")
        self.printers.click_printer_firmware_update_checkbox()
        self.printers.click_device_specific_policy_create_button()
        self.printers.click_change_not_recommended_popup_confirm_button()

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Printer Firmware Update (send as Printjob)")

    def test_05_verify_check_for_latest_firmware_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Check for Latest Firmware",setting_card="check-latest",category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Check for Latest Firmware")

    def test_06_xml_services_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network XML Services API Status
        network_xml_services_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/jetdirectServices"
        response = get_api_response(self.stack,network_xml_services_uri)
        xml_services_status = response.json()["state"]["reported"]["cdmData"]["xdmEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="HP Jetdirect XML Services",setting_card="jd-xml-svc",settings_value= xml_services_status,category_type="Security")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("HP Jetdirect XML Services")

    def test_07_verify_host_usb_plug_and_play_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Host USB Plug and Play Status
        security_host_usb_plug_and_play_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/usbHost"
        response = get_api_response(self.stack,security_host_usb_plug_and_play_uri)
        plug_and_play_status = response.json()["state"]["reported"]["cdmData"]["plugAndPlayEnabled"]
        print_from_usb_status = response.json()["state"]["reported"]["cdmData"]["printFromUsbEnabled"]
        scan_to_usb_status = response.json()["state"]["reported"]["cdmData"]["scanToUsbEnabled"]

        all_plug_and_play_status = list((plug_and_play_status,print_from_usb_status,scan_to_usb_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Host USB Plug and Play",setting_card="host-usb-pnp",settings_value=all_plug_and_play_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Host USB Plug and Play")

    def test_08_verify_service_access_code_settings_in_device_specific_policy(self):
        #  
        # Generate Service Access Code Password
        service_access_code_password = random.randint(10000000,99999999)
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Service Access Code API/Configuration Status
        service_access_code_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/serviceUserConfig"
        response = get_api_response(self.stack,service_access_code_uri)
        service_access_code_status = response.json()["state"]["reported"]["cdmData"]["passwordConfiguredByUser"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Service Access Code",setting_card="svc-access-code",settings_value=service_access_code_password,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.    
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Navigating to Properties Tab to verify the configuration status
        response = get_api_response(self.stack,service_access_code_uri)
        assert service_access_code_status == "true"
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_security_accordion()
        self.printers.click_printer_device_details_device_property_card("service-access-code")
        self.printers.get_printer_device_details_device_property_value("svc-access-code") == "Configured"
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Service Access Code")

    def test_09_verify_cross_origin_resource_sharing_in_device_specific_policy(self):
        #
        site_name = "auto" +str(random.randint(1,9)) + "." +"com"

        device_cloud_id = self.printers.get_device_cloud_id()
    
        #Get Cross-Origin Resource Sharing (CORS) Setting API Status
        cors_setting_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/systemConfig"
        response = get_api_response(self.stack,cors_setting_uri)
        cors_setting_checkbox = response.json()["state"]["reported"]["cdmData"]["corsEnabled"]

        cors_setting_status = list((cors_setting_checkbox,site_name))

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Cross-Origin Resource Sharing (CORS)",setting_card="cors",settings_value= cors_setting_status, category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)    

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Cross-Origin Resource Sharing (CORS)")

    def test_10_verify_bootloader_password_setting_from_properties_tab(self):
        random_password = "430"+str(random.randint(1,9))

        device_cloud_id = self.printers.get_device_cloud_id()
    
        # Get Bootloader Password Setting API Status
        bootloader_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/bootloader"
        response = get_api_response(self.stack, bootloader_uri)
        bootloader_password_status = response.json()["state"]["reported"]["cdmData"]["passwordSet"]
        # Only proceed if password is not already set
        if bootloader_password_status != "true":

            # Get Bootloader Password Setting UI Status
            self.printers.click_printers_details_page_properties_tab()
            self.printers.click_security_accordion()
            self.printers.click_printer_device_details_device_property_card("bootloader-password")
            assert self.printers.get_printer_device_details_device_property_value("bootloader-password") == "Not Configured"
            
            # Updating the Password from Dvice - Specific Policy tab
            self.printers.click_printers_details_page_policies_tab()
            self.printers.add_settings_in_device_specific_policy_tab(setting_name="Bootloader Password",setting_card="bootloader-password",settings_value= random_password,category_type="Security")
    
            # verify the compliance of that device after the device specific policy is applied.
            self.printers.verify_policies_compliance_status(self.serial_number)
    
            # Remove the device specific policy
            self.printers.remove_settings_in_device_specific_policy_tab("Bootloader Password")

        else:
            # Verify current status in Properties Tab
            self.printers.click_printers_details_page_policies_tab()
            self.printers.click_printers_details_page_properties_tab()
            self.printers.click_security_accordion()
            self.printers.click_printer_device_details_device_property_card("bootloader-password")
            self.printers.get_printer_device_details_device_property_value("bootloader-password") == "Configured"
        
    def test_11_verify_smb_or_cifs_shared_folder_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify SMB/CIFS (Shared Folder) API Status
        smb_or_cifs_shared_folder_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/networkFolder/configuration"
        response = get_api_response(self.stack,smb_or_cifs_shared_folder_uri)
        smb_v1 = response.json()["state"]["reported"]["cdmData"]["smbVersion1Enabled"]
        smb_v2 = response.json()["state"]["reported"]["cdmData"]["smbVersion2Enabled"]
        smb_v3 = response.json()["state"]["reported"]["cdmData"]["smbVersion3Enabled"]
        smb_or_cifs_shared_folder_status = list((smb_v1,smb_v2,smb_v3))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="SMB/CIFS (Shared Folder)",setting_card="smb-cifs",settings_value=smb_or_cifs_shared_folder_status,category_type="Security")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("SMB/CIFS (Shared Folder)")