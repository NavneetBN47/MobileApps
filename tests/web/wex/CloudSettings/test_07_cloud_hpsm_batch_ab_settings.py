import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_07_Workforce_HPSM_Batch_AB_CloudSettings(object):

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

    def test_01_verify_online_solutions_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Online Solutions - Show Event QR Code API Status
        show_event_qr_code_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/controlPanel/configuration"
        response = get_cloud_api_response(self.stack,show_event_qr_code_uri)
        show_event_qr_code_status = response.json()["state"]["reported"]["cdmData"]["showEventQrCode"]

        # Verify Online Solutions - Show Links in the EWS API Status
        show_support_links_uri  = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/ews/configuration"
        response = get_cloud_api_response(self.stack,show_support_links_uri)
        show_support_links_status = response.json()["state"]["reported"]["cdmData"]["showSupportLinks"]
        show_links_in_event_log_status = response.json()["state"]["reported"]["cdmData"]["showLinksInEventLog"]

        online_solutions_status = list((show_event_qr_code_status,show_support_links_status,show_links_in_event_log_status))

         # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Online Solutions",setting_card="online-solutions",settings_value= online_solutions_status,category_type="Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Online Solutions")

    # HPSM Batch A & B and Catching up with FP Settings
    def test_02_verify_device_announcement_agent_settings_in_device_specific_policy(self):
        #
        #Generate random ip address
        test_ip_address="15.45.68."+str(random.randint(1,99))

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Web Services Smart Cloud Print API Status
        device_announcement_agent_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/deviceAnnouncement/configuration"
        response = get_cloud_api_response(self.stack,device_announcement_agent_uri)
        announcement_status = response.json()["state"]["reported"]["cdmData"]["announcementEnabled"]
        server_auth_status = response.json()["state"]["reported"]["cdmData"]["serverAuthEnabled"]
        
        all_device_announcement_agent_status = list((announcement_status,test_ip_address,server_auth_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Device Announcement Agent",setting_card="device-announcement",settings_value=all_device_announcement_agent_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Device Announcement Agent")

    # AirPrint Fax or IPP Fax Out
    def test_03_verify_airprint_fax_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get AirPrint Fax API Status
        airprint_fax_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/fax/sendConfiguration"
        response = get_cloud_api_response(self.stack,airprint_fax_uri)
        airprint_fax_status = response.json()["state"]["reported"]["cdmData"]["ippFaxEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="AirPrint Fax",setting_card="airprint-fax",settings_value= airprint_fax_status, category_type="Network")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("AirPrint Fax") 

    def test_04_verify_802_1x_authentication_wired_setting_in_properties_tab(self):
        #
        #Generate random username, password and server ID
        username = "NIP95E6C"+str(random.randint(1,9))
        server_name = "Autoserver"+str(random.randint(1,99))
 
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify 802.1x Authentication API Status
        authentication_802_1x_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_cloud_api_response(self.stack, authentication_802_1x_uri)
        
        require_exact_match = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["exactServerIdMatch"]
        eap_tls_configure = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["eapTlsEnabled"]
        block_network = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["blockNetworkOnAuthFailure"]
        
        settings_value = list((username,server_name,require_exact_match,eap_tls_configure,block_network))

        # Add Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="802.1x Authentication (Wired)",setting_card="802-1x-auth",settings_value=settings_value,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("802.1x Authentication (Wired)")

    def test_05_verify_802_1x_authentication_wireless_setting_in_properties_tab(self):
        #
        #Generate random username, password and server ID
        security_key = "1234567"+str(random.randint(1,9))
        username = "NIP95E6C"+str(random.randint(1,9))
        server_name = "Autoserver"+str(random.randint(1,99))
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify 802.1x Authentication API Status
        authentication_802_1x_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/wirelessConfig"
        response = get_cloud_api_response(self.stack, authentication_802_1x_uri)
        eap_tls_configure = response.json()["state"]["reported"]["cdmData"]["wlanProfile1"]["dot1xAuthConfig"]["eapTlsEnabled"]
        peap_enabled = response.json()["state"]["reported"]["cdmData"]["wlanProfile1"]["dot1xAuthConfig"]["eapPeapEnabled"]
       
        settings_value = list((username,server_name,eap_tls_configure,peap_enabled))
 
        # Add Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="802.1x Authentication (Wireless)",setting_card="802-1x-auth-wifi",settings_value=settings_value,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Update 802 authentication wireless setting WIFI protected access to personal
        self.printers.update_802_1x_authentication_wireless_wpa_personal_settings(setting_card="802-1x-auth-wifi")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("802.1x Authentication (Wireless)")

    # LDAP Sign in Setup 
    def test_06_verify_ldap_enable_and_use_mfp_user_credential_server_authentication_setting_in_device_specific_policy(self):
        # Generate random values
        ldap_server_address = "autotest"+str(random.randint(1,9))+".com"
        port_number = "22"+str(random.randint(11, 99))
        bind_prefix = str(random.randint(11, 99))
        root_name = "Test"+str(random.randint(1,9))+".com"
        match_attribute = "ldapuser"+str(random.randint(1,9))
        email_attribute = "mfpuseremail"+str(random.randint(1,9))+"@hpp.com"
        display_name_attribute = "MFPUser"+str(random.randint(1,9))
        group_attribute = "group"+str(random.randint(1,9))
        
        ldap_settings_value = list((ldap_server_address, port_number, bind_prefix, root_name, match_attribute, email_attribute, display_name_attribute, group_attribute))

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="LDAP Sign In Setup",setting_card="ldap-setup", settings_value=ldap_settings_value,category_type="Security")
        
        # Verify the compliance of that device after the device specific policy is applied
        self.printers.verify_policies_compliance_status(self.serial_number)
        
        # Edit settings - disable SSL and exact match
        self.printers.click_printers_details_policies_tab_edit_button()
        self.printers.click_device_specific_policy_next_button()
        self.printers.click_device_specific_policy_settings_card("ldap-setup")
        self.printers.click_ldap_use_ssl_checkbox()
        self.printers.click_ldap_exact_match_checkbox()
        self.printers.click_device_specific_policy_create_button()
        self.printers.click_change_not_recommended_popup_confirm_button()
        
        # Verify compliance after edit
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Disable LDAP Sign In Setup
        self.printers.click_printers_details_policies_tab_edit_button()
        self.printers.click_device_specific_policy_next_button()
        self.printers.click_device_specific_policy_settings_card("ldap-setup")
        self.printers.click_ldap_enable_checkbox()
        self.printers.click_device_specific_policy_create_button()
        self.printers.click_change_not_recommended_popup_confirm_button()

        # Verify compliance after disabling LDAP Sign In Setup
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("LDAP Sign In Setup")
        
    def test_07_verify_ldap_enable_and_use_ldap_admin_credentials_authentication_setting_in_device_specific_policy(self):
        ldap_server_address = "autotest"+str(random.randint(1,9))+".com"
        port_number = "22"+str(random.randint(11, 99))
        domain_name = "domain"+str(random.randint(1,9))+".com"
        root_name = "Test"+str(random.randint(1,9))+".com"
        match_attribute = "ldapuser"+str(random.randint(1,9))
        email_attribute = "mfpuseremail"+str(random.randint(1,9))+"@hpp.com"
        display_name_attribute = "MFPUser"+str(random.randint(1,9))
        group_attribute = "group"+str(random.randint(1,9))
        
        ldap_settings_value = list((ldap_server_address, port_number, domain_name, root_name, match_attribute, email_attribute, display_name_attribute, group_attribute))

        # Adding Settings in Device Specific Policy Tab
        self.printers.update_ldap_admin_credentials_settings(setting_name="LDAP Sign In Setup",setting_card="ldap-setup", settings_value=ldap_settings_value)
        
        # Verify the compliance of that device after the device specific policy is applied
        self.printers.verify_policies_compliance_status(self.serial_number)
        
        # Edit settings - disable SSL and exact match
        self.printers.update_ldap_use_ssl_and_exact_match_settings(setting_card="ldap-setup")
        
        # Verify compliance after edit
        self.printers.verify_policies_compliance_status(self.serial_number)
        
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("LDAP Sign In Setup")

    # Allow access to LDAP Address Book
    def test_08_verify_allow_access_to_ldap_address_book_with_no_authentication_setting_in_device_specific_policy(self):
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
 
    def test_09_verify_allow_access_to_ldap_address_book_with_simple_authentication_setting_in_device_specific_policy(self):
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

    # HPSM Settings
    def test_10_verify_email_scan_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Email Scan API Status
        email_scan_settings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/scanEmail"      
        response = get_cloud_api_response(self.stack, email_scan_settings_uri)
        email_scan_setting_status = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["contentType"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "Email Scan Settings", setting_card="email-scan", settings_value=email_scan_setting_status,category_type="Digital Sending")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email Scan Settings")
 
    def test_11_verify_retain_temporary_print_jobs_after_reboot_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Retain Temporary Print Jobs after Reboot API Status
        retain_temporary_print_jobs_after_reboot_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/storeJobManagement/configuration"
        response = get_cloud_api_response(self.stack,retain_temporary_print_jobs_after_reboot_uri)
        retain_temporary_print_jobs_after_reboot_status = response.json()["state"]["reported"]["cdmData"]["temporaryJobRetentionPolicy"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Retain Temporary Print Jobs after Reboot",setting_card="retain-jobs-after-reboot",settings_value=retain_temporary_print_jobs_after_reboot_status,category_type="Devices")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Retain Temporary Print Jobs after Reboot")
 
    def test_12_verify_smb_or_cifs_shared_folder_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify SMB/CIFS (Shared Folder) API Status
        smb_or_cifs_shared_folder_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/networkFolder/configuration"
        response = get_cloud_api_response(self.stack,smb_or_cifs_shared_folder_uri)
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
 
    def test_13_verify_fips_140_compliance_library_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify FIPS 140 Compliance Library API Status
        fips_140_compliance_library_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/tlsConfig/configuration"
        response = get_cloud_api_response(self.stack,fips_140_compliance_library_uri)
        fips_140_compliance_library_status = response.json()["state"]["reported"]["cdmData"]["fipsMode"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="FIPS 140 Compliance Library",setting_card="fips-140-compliance",settings_value=fips_140_compliance_library_status,category_type="Network")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("FIPS 140 Compliance Library")