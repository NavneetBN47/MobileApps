import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_07_Security_Category02_Proxies_Settings(object):

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

    def test_01_verify_device_announcement_agent_settings_in_device_specific_policy(self):
        #
        #Generate random ip address
        test_ip_address="15.45.68."+str(random.randint(1,99))

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Web Services Smart Cloud Print API Status
        device_announcement_agent_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/deviceAnnouncement"
        response = get_api_response(self.stack,device_announcement_agent_uri)
        announcement_status = response.json()["state"]["reported"]["cdmData"]["announcementEnabled"]
        server_auth_status = response.json()["state"]["reported"]["cdmData"]["serverAuthEnabled"]
        
        all_device_announcement_agent_status = list((announcement_status,test_ip_address,server_auth_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Device Announcement Agent",setting_card="device-announcement",settings_value=all_device_announcement_agent_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Device Announcement Agent")

    def test_02_verify_printer_firmware_sha1_code_signing_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Fax Settings PC Fax send API Status
        legacy_firmware_update_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/firmwareUpdate"

        response = get_api_response(self.stack,legacy_firmware_update_uri)
        legacy_firmware_update_uri_status = response.json()["state"]["reported"]["cdmData"]["sha1ValidationEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "Printer Firmware SHA1 Code Signing",setting_card= "legacy-fw-update",settings_value= legacy_firmware_update_uri_status,category_type= "Security")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Printer Firmware SHA1 Code Signing")

    def test_03_verify_restrict_color_setting_in_device_specific_policy(self):
        #
        # Generate random application name
        application_name = "HP Smart"+str(random.randint(1,9))
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Restrict Color API Status
        restrict_color_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_api_response(self.stack,restrict_color_uri)
        color_settings = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["restrictColor"]
        restrict_by_user_permissions = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingPermissionSets"]
        restrict_by_application = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingApplicationSettings"]
        default_permission = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["allowColorAndQuality"]
 
        restrict_color_status = list((color_settings,restrict_by_user_permissions,restrict_by_application,default_permission,application_name))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Restrict Color",setting_card="restrict-color",settings_value= restrict_color_status,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Restrict Color")

    def test_04_verify_digital_sending_service_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Show Date and Time API Status
        digital_sending_service_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_api_response(self.stack,digital_sending_service_uri)
        allow_use_of_digital_send = response.json()["state"]["reported"]["cdmData"]["security"]["digitalSendingService"]["allowUse"]
        allow_transfer_to_digital_send = response.json()["state"]["reported"]["cdmData"]["security"]["digitalSendingService"]["allowTransfer"]

        digital_sending_service_status = list((allow_use_of_digital_send,allow_transfer_to_digital_send))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Digital Sending Service",setting_card="digital-sending",settings_value=digital_sending_service_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Digital Sending Service")

    def test_05_verify_display_color_usage_job_log_page_on_information_tab_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Display Color Usage Job Log uri API Status
        display_color_usage_job_log_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/ews"
        response = get_api_response(self.stack,display_color_usage_job_log_uri)
        display_color_usage_job_log_status = response.json()["state"]["reported"]["cdmData"]["displayColorUsageTab"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Display Color Usage Job Log Page on Information Tab",setting_card="color-usage-log",settings_value=display_color_usage_job_log_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Display Color Usage Job Log Page on Information Tab")

    def test_06_verify_embedded_web_server_access_setting_in_device_specific_policy(self):
        #
        # Adding Setting in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Embedded Web Server Access",setting_card="ews-access",category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.navigating_to_device_page_from_printers_details_tab(self.serial_number)
        if self.printers.get_policies_device_list_compliance_status() != "Compliant":
            if self.printers.get_policies_compliance_status_widget_compliance_status_reason() != "Unsupported":
                self.printers.click_printers_details_policies_tab_edit_button()
                self.printers.click_device_specific_policy_next_button()
                self.printers.click_device_specific_policy_settings_card("ews-access")
                self.printers.click_set_options_settings_checkbox("ews-access")
                self.printers.click_device_specific_policy_create_button()
                self.printers.click_change_not_recommended_popup_confirm_button()
                self.printers.dismiss_toast()
                assert self.printers.get_policies_device_list_compliance_status() == "Compliant"

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Embedded Web Server Access")

    def test_07_verify_disk_encryption_status_setting_in_device_specific_policy(self):
        #
        # Adding Setting in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Disk Encryption Status",setting_card="disk-encryption",category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.navigating_to_device_page_from_printers_details_tab(self.serial_number)
        if self.printers.get_policies_device_list_compliance_status() != "Compliant":
            if self.printers.get_policies_compliance_status_widget_compliance_status_reason() != "Unsupported":
                self.printers.click_printers_details_policies_tab_edit_button()
                self.printers.click_device_specific_policy_next_button()
                self.printers.click_device_specific_policy_settings_card("disk-encryption")
                self.printers.click_disk_encryption_inactive_status()
                self.printers.click_device_specific_policy_create_button()
                self.printers.click_change_not_recommended_popup_confirm_button()
                self.printers.dismiss_toast()
                assert self.printers.get_policies_device_list_compliance_status() == "Compliant"

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Disk Encryption Status")

    # LDAP Sign in Setup
    def test_08_verify_ldap_enable_and_use_mfp_user_credential_server_authentication_setting_in_device_specific_policy(self):
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
        
    def test_09_verify_ldap_enable_and_use_ldap_admin_credentials_authentication_setting_in_device_specific_policy(self):
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

    def test_10_verify_802_1x_authentication_wired_setting_in_properties_tab(self):
        #
        #Generate random username, password and server ID
        username = "NIP95E6C"+str(random.randint(1,9))
        server_name = "Autoserver"+str(random.randint(1,99))
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify 802.1x Authentication API Status
        authentication_802_1x_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_api_response(self.stack,authentication_802_1x_uri)
        
        require_exact_match = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["exactServerIdMatch"]
        eap_tls_configure = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["eapTlsEnabled"]
        block_network = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["blockNetworkOnAuthFailure"]
        # reauthenticate_on_apply = response.json()["state"]["reported"]["cdmData"]["ethConfig"]["dot1xAuthConfig"]["reauthenticate"]
 
        settings_value = list((username,server_name,require_exact_match,eap_tls_configure,block_network))

        # Add Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="802.1x Authentication (Wired)",setting_card="802-1x-auth",settings_value=settings_value,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("802.1x Authentication (Wired)")

    def test_11_verify_stored_data_pin_protection_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
    
        # Get Stored Data PIN Protection API Status
        stored_data_pin_protection_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/storeJobManagement"
        response = get_api_response(self.stack,stored_data_pin_protection_uri)

        four_digit_pin = response.json()["state"]["reported"]["cdmData"]["requireFourDigitPin"]
        pin_required_to_store_a_scan = response.json()["state"]["reported"]["cdmData"]["requireScanJobPinProtection"]
        pin_requireded_driver_stored_jobs = response.json()["state"]["reported"]["cdmData"]["requirePrintJobPinProtection"]
        cancel_pin_jobs = response.json()["state"]["reported"]["cdmData"]["cancelJobsWithoutPinProtection"]

        stored_data_pin_protection_status = list((four_digit_pin, pin_required_to_store_a_scan, pin_requireded_driver_stored_jobs, cancel_pin_jobs))  
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Stored Data PIN Protection",setting_card="pin-protection",settings_value=stored_data_pin_protection_status,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Stored Data PIN Protection")