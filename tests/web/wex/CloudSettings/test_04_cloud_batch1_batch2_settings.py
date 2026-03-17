import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

#Generate random device properties values
device_name="device_name"+str(random.randint(1,99))

class Test_04_Workforce_Batch1Batch2_CloudSettings(object):

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
        self.cloud_settings_device_serial_number = self.account["cloud_settings_batch3_serial_number"]

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

    # Cloud Batch 1 Settings

    def test_01_verify_device_name_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Device Name",setting_card="device-name",settings_value=device_name,category_type="Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Verify the device name in device details properties tab
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.click_printer_device_details_device_property_card("device-name")
        assert device_name == self.printers.get_printer_device_details_device_property_value("device-name")

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Device Name")

    def test_02_verify_web_scan_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
        
        # Get Network Web scan API Status
        airprint_scan_and_secure_scan_config_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/networkScanServices"
        response = get_cloud_api_response(self.stack,airprint_scan_and_secure_scan_config_uri)
        airprint_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCL"]
        airprint_secure_scan_status = response.json()["state"]["reported"]["cdmData"]["scanServices"]["eSCL"]["eSCLSecure"]
        all_scan_and_secure_status = list((airprint_scan_status,airprint_secure_scan_status))
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Web Scan",setting_card="web-scan",settings_value= all_scan_and_secure_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Web Scan")

    def test_03_verify_time_services_settings_in_device_specific_policy(self):
        #
        #Generate random ip address
        time_services_ip_address="15.40.45."+str(random.randint(1,99))
        local_port=random.randint(1100,1900)
        synchronize_time=random.randint(1,168)

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Time Services API Status
        time_services_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/clock/configuration"
        response = get_cloud_api_response(self.stack,time_services_uri)
        time_services_system_time_sync = response.json()["state"]["reported"]["cdmData"]["systemTimeSync"]

        time_services_status = list((time_services_system_time_sync,time_services_ip_address,local_port,synchronize_time))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Time Services",setting_card="time-services",settings_value=time_services_status,category_type="Embedded Web Server")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Time Services")

    def test_04_verify_save_to_sharepoint_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Save To SharePoint API Status
        save_to_sharepoint_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/scan/destinationConfig"
        response = get_cloud_api_response(self.stack,save_to_sharepoint_uri)
        save_to_sharepoint_status = response.json()["state"]["reported"]["cdmData"]["sharePointEnabled"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Save to SharePoint",setting_card="save-to-share-point",settings_value=save_to_sharepoint_status,category_type="Digital Sending")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Save to SharePoint")
 
    def test_05_verify_send_to_email_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Send to Email API Status
        send_to_email_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/scan/destinationConfig"
        response = get_cloud_api_response(self.stack,send_to_email_uri)
        send_to_email_status = response.json()["state"]["reported"]["cdmData"]["emailEnabled"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Send to Email",setting_card="save-to-email",settings_value=send_to_email_status,category_type="Digital Sending")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Send to Email")

    def test_06_verify_save_to_network_folder_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Save To Network Folder API Status
        save_to_network_folder_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/scan/destinationConfig"
        response = get_cloud_api_response(self.stack,save_to_network_folder_uri)
        save_to_network_folder_status = response.json()["state"]["reported"]["cdmData"]["folderEnabled"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Save To Network Folder",setting_card="save-to-network-folder",settings_value=save_to_network_folder_status,category_type="Digital Sending")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Save To Network Folder")

    # Cloud Batch 2 Settings

    def test_07_verify_email_address_or_email_settings_in_device_specific_policy(self):
        #
        # Generate random values
        default_from_email = "test"+str(random.randint(1,9))+"@hp.com"
        default_display_name = "Auto Test"+str(random.randint(1,9))
        email_subject_name = "Sample Email Testing"+str(random.randint(1,9))
        email_body_message = "Auto Test Sanity"+str(random.randint(1,9))
       
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Email Address or Email Settings API Status
        email_address_message_settings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/scanEmail"
        response = get_cloud_api_response(self.stack,email_address_message_settings_uri)
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

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Email Address / Message Settings",setting_card="email-message",settings_value=email_address_message_settings_status,category_type="Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email Address / Message Settings")