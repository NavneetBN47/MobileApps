import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

class Test_11_Digital_Sending_Category_Proxies_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.serial_number = request.config.getoption("--proxy-device")
        self.printers = self.fc.fd["fleet_management_devices"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]

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
        self.printers.search_printers(self.serial_number)
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        return self.printers.click_printers_details_page_policies_tab()

    def test_01_verify_save_to_network_folder_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Save To Network Folder API Status
        save_to_network_folder_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/scan/destinationConfig"
        response = get_api_response(self.stack,save_to_network_folder_uri)
        save_to_network_folder_status = response.json()["state"]["reported"]["cdmData"]["folderEnabled"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Save To Network Folder",setting_card="save-to-network-folder",settings_value=save_to_network_folder_status,category_type="Digital Sending")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Save To Network Folder")
 
    def test_02_verify_save_to_sharepoint_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Save To SharePoint API Status
        save_to_sharepoint_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/scan/destinationConfig"
        response = get_api_response(self.stack,save_to_sharepoint_uri)
        save_to_sharepoint_status = response.json()["state"]["reported"]["cdmData"]["sharePointEnabled"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Save to SharePoint",setting_card="save-to-share-point",settings_value=save_to_sharepoint_status,category_type="Digital Sending")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Save to SharePoint")
 
    def test_03_verify_send_to_email_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Send to Email API Status
        send_to_email_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/scan/destinationConfig"
        response = get_api_response(self.stack,send_to_email_uri)
        send_to_email_status = response.json()["state"]["reported"]["cdmData"]["emailEnabled"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Send to Email",setting_card="save-to-email",settings_value=send_to_email_status,category_type="Digital Sending")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Send to Email")

    def test_04_verify_email_notification_settings_in_device_specific_policy(self):
        #Generate Random Values
        email_addresses = "autotest" + str(random.randint(1, 9)) + "@testmail.com"

        device_cloud_id = self.printers.get_device_cloud_id()

        #Verify Email Notification Settings API Status 
        email_notification_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanEmail"
        response = get_api_response(self.stack,email_notification_settings_uri)
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]
        
        all_email_notification_settings_status=list((notification_condition_status,notification_mode_status,email_addresses))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Email Notification Settings",setting_card="email-notification",settings_value=all_email_notification_settings_status,category_type="Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email Notification Settings")

    def test_05_verify_network_folder_notification_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_addresses = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        device_cloud_id = self.printers.get_device_cloud_id()
 
        #Verify Email Notification Setting API Status
        network_folder_notification_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanNetworkFolderConfigurationDefaults"
       
        response = get_api_response(self.stack, network_folder_notification_settings_uri)
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]
       
        all_network_folder_notification_settings_status=list((notification_condition_status,notification_mode_status,email_addresses))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "Network Folder Notification Settings",setting_card= "network-folder-notification",settings_value= all_network_folder_notification_settings_status,category_type= "Digital Sending")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Network Folder Notification Settings")

    def test_06_verify_email_scan_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Email Scan API Status
        email_scan_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanEmail"      
        response = get_api_response(self.stack, email_scan_settings_uri)
        email_scan_setting_status = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["contentType"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "Email Scan Settings", setting_card="email-scan", settings_value=email_scan_setting_status,category_type="Digital Sending")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email Scan Settings")

    def test_07_verify_email_address_or_email_settings_in_device_specific_policy(self):
        #
        # Generate random values
        default_from_email = "test"+str(random.randint(1,9))+"@hp.com"
        default_display_name = "Auto Test"+str(random.randint(1,9))
        email_subject_name = "Sample Email Testing"+str(random.randint(1,9))
        email_body_message = "Auto Test Sanity"+str(random.randint(1,9))
       
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Email Address or Email Settings API Status
        email_address_message_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanEmail"
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

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Email Address / Message Settings",setting_card="email-message",settings_value=email_address_message_settings_status,category_type="Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email Address / Message Settings")

    def test_08_verify_network_folder_file_setting_in_device_specific_policy(self):
        #
        # Generate random values
        default_file_name = "_Auto_Test_File_Name_" + str(random.randint(1, 9)) + "_"
       
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Folder File Settings or Network Folder File Settings API Status
        network_folder_file_setting_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanNetworkFolderConfigurationDefaults"
        response = get_api_response(self.stack,network_folder_file_setting_uri)

        network_folder_file_name_prefix = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["prefix"]
        user_editable = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileNameIsEditable"]
        network_folder_file_name_suffix = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["suffix"]
        default_colour_preference = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["colorMode"]
        default_output_quality = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["qualityAndFileSize"]
        default_file_type = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileType"]
        default_resolution = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["resolution"]
        grey_scale_tiff_compression_method = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["colorGrayScaleTiffCompression"]
        pdf_encryption = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["encryptPDF"]
        blank_page_suppression = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["blankPageSuppressionEnabled"]

        all_network_folder_file_settings_status = list((network_folder_file_name_prefix,default_file_name,user_editable,network_folder_file_name_suffix,default_colour_preference,default_output_quality,
                                                        default_file_type,default_resolution,grey_scale_tiff_compression_method,pdf_encryption,blank_page_suppression))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Network Folder File Settings",setting_card="network-folder-file",settings_value=all_network_folder_file_settings_status,category_type="Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Network Folder File Settings")

    def test_09_verify_email_file_setting_in_device_specific_policy(self):
        #
        # Generate random values
        default_file_name = "_Auto_Test_File_Name_" + str(random.randint(1, 9)) + "_"
       
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Email File Setting or Email File Setting API Status
        email_file_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanEmail"
        response = get_api_response(self.stack,email_file_settings_uri)

        email_file_name_prefix = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["prefix"]
        user_editable = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileNameIsEditable"]
        email_file_name_suffix = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["suffix"]
        default_colour_preference = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["colorMode"]
        default_output_quality = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["qualityAndFileSize"]
        default_file_type = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["fileType"]
        default_resolution = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["resolution"]
        black_tiff_compression_method = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["monoTiffCompression"]
        grey_scale_tiff_compression_method = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["colorGrayScaleTiffCompression"]
        pdf_encryption = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["sendFileAttributes"]["encryptPDF"]
        blank_page_suppression = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["blankPageSuppressionEnabled"]

        all_email_file_setting_status = list((email_file_name_prefix,default_file_name,user_editable,email_file_name_suffix,default_colour_preference,default_output_quality,default_file_type,default_resolution,black_tiff_compression_method,grey_scale_tiff_compression_method,pdf_encryption,blank_page_suppression))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Email File Settings",setting_card="email-file",settings_value=all_email_file_setting_status,category_type="Digital Sending")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email File Settings")

    # Allow Access to LDAP Address Book Tests
    def test_10_verify_allow_access_to_ldap_address_book_with_no_authentication_setting_in_device_specific_policy(self):
        #
        # Generate random values
        ldap_server_address = "ldapbook"+ str(random.randint(1, 9)) +".com"
        port_number = "38" + str(random.randint(10, 99))
        starting_point_directory = "DC=test" + str(random.randint(1, 9)) + ",DC=com"
        ldap_search_filter = "ldapfilter" + str(random.randint(1, 9))
        # windows_domain = "testdomain" + str(random.randint(1, 9)) + ".com"
        # username = "ldapuser" + str(random.randint(1, 9))
       
        # First scenario: No Authentication with Active Directory Default
        ldap_address_book_settings_value = list((ldap_server_address, port_number, starting_point_directory, ldap_search_filter))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Allow Access to LDAP Address Book",setting_card="ldap-ab-access",
            settings_value=ldap_address_book_settings_value, category_type="Digital Sending")
       
        # Verify the compliance of that device after the device specific policy is applied
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Second scenario: Edit settings - Disable SSL and change Windows Domain Authentication
        self.printers.update_ldap_ssl_and_change_windows_domain_authentication_settings(setting_card="ldap-ab-access")
       
        # Verify compliance after edit
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Allow Access to LDAP Address Book")
 
    def test_11_verify_allow_access_to_ldap_address_book_with_simple_authentication_setting_in_device_specific_policy(self):
        #
        # Generate random values
        ldap_server_address = "ldapbook"+ str(random.randint(1, 9)) +".com"
        port_number = "38" + str(random.randint(10, 99))
        starting_point_directory = "DC=test" + str(random.randint(1, 9)) + ",DC=com"
        match_attribute = "ldapuser"+ str(random.randint(1, 9))
        email_attribute = "user"+ str(random.randint(1, 9)) +"@hpp.com"
        fax_number_attribute = "78"+ str(random.randint(10, 99))
        ldap_search_filter = "ldapfilter" + str(random.randint(1, 9))
       
        # Enable with Simple Authentication and Custom Attributes
        allow_ldap_address_book_settings_value = list((ldap_server_address, port_number,starting_point_directory,match_attribute, email_attribute, fax_number_attribute, ldap_search_filter))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.update_allow_access_to_ldap_address_book_with_custom_attributes(setting_name="Allow Access to LDAP Address Book", setting_card="ldap-ab-access",
                                                                                    settings_value=allow_ldap_address_book_settings_value)
       
        # Verify the compliance of that device after the device specific policy is applied
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Edit settings - Disable Allow Access to LDAP Address Book
        self.printers.click_printers_details_policies_tab_edit_button()
        self.printers.click_device_specific_policy_next_button()
        self.printers.click_device_specific_policy_settings_card("ldap-ab-access")
        # Disable the feature
        self.printers.click_ldap_address_book_enable_checkbox()
        self.printers.click_device_specific_policy_create_button()
        self.printers.click_change_not_recommended_popup_confirm_button()
       
        # Verify compliance after disabling
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Allow Access to LDAP Address Book")