import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_03_03_Workforce_Batch0_CloudSettings(object):

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

    def test_01_verify_disk_encryption_status_setting_in_device_specific_policy(self):
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

    def test_02_verify_wins_port_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        network_wins_port_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/nameResolverServices"
        response = get_cloud_api_response(self.stack,network_wins_port_uri)
        wins_port_status = response.json()["state"]["reported"]["cdmData"]["wins"]["winsPort"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="WINS Port",setting_card="wins-port",settings_value= wins_port_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("WINS Port")

    def test_03_verify_wins_registration_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network Wins Registration API Status
        network_wins_registration_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/nameResolverServices"
        response = get_cloud_api_response(self.stack,network_wins_registration_uri)
        wins_reg_status = response.json()["state"]["reported"]["cdmData"]["wins"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="WINS Registration",setting_card="wins-registration",settings_value= wins_reg_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("WINS Registration")

    def test_04_verify_csrf_prevention_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Cross-Site Request Forgery (CSRF) Prevention Status
        security_csrf_prevention_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/systemConfig"
        response = get_cloud_api_response(self.stack,security_csrf_prevention_uri)
        csrf_prevention_status = response.json()["state"]["reported"]["cdmData"]["csrfPreventionEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Cross-Site Request Forgery (CSRF) Prevention",setting_card="csrf-prevention",settings_value=csrf_prevention_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Cross-Site Request Forgery (CSRF) Prevention")

    def test_05_verify_embedded_web_server_access_setting_in_device_specific_policy(self):
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

    def test_06_verify_ews_information_protection_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Information Tab Status
        information_tab_setting_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/ews/configuration"
        response = get_cloud_api_response(self.stack,information_tab_setting_uri)
        information_tab_status = response.json()["state"]["reported"]["cdmData"]["informationTabAccess"]
        display_job_log_status = response.json()["state"]["reported"]["cdmData"]["displayJobLogOnInformationTab"]
        display_print_job_log_status = response.json()["state"]["reported"]["cdmData"]["displayPrintPageOnInformationTab"]

        all_information_tab_setting_status = list((information_tab_status,display_job_log_status,display_print_job_log_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="EWS Information Protection",setting_card="info-tab",settings_value=all_information_tab_setting_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("EWS Information Protection")

    def test_07_verify_tftp_configuration_file_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network TFTP Configuration File API Status
        network_tftp_config_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/jetdirectServices"
        response = get_cloud_api_response(self.stack,network_tftp_config_uri)
        tftp_config_status = response.json()["state"]["reported"]["cdmData"]["tftpEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="TFTP Configuration File",setting_card="tftp-cfg",settings_value= tftp_config_status,category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("TFTP Configuration File")

    def test_08_verify_printer_firmware_sha1_code_signing_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Fax Settings PC Fax send API Status
        legacy_firmware_update_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/firmwareUpdate/configuration"

        response = get_cloud_api_response(self.stack,legacy_firmware_update_uri)
        legacy_firmware_update_uri_status = response.json()["state"]["reported"]["cdmData"]["sha1ValidationEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "Printer Firmware SHA1 Code Signing",setting_card= "legacy-fw-update",settings_value= legacy_firmware_update_uri_status,category_type= "Security")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Printer Firmware SHA1 Code Signing")

    def test_09_xml_services_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Network XML Services API Status
        network_xml_services_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/network/jetdirectServices"
        response = get_cloud_api_response(self.stack,network_xml_services_uri)
        xml_services_status = response.json()["state"]["reported"]["cdmData"]["xdmEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="HP Jetdirect XML Services",setting_card="jd-xml-svc",settings_value= xml_services_status,category_type="Security")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("HP Jetdirect XML Services")

    @pytest.mark.parametrize("setting_name, setting_card, max_tls_radio, min_tls_radio, cipher_checkboxes", [
    ("Web Encryption Settings or Active Ciphers", "web-encryption", "web_encryption_max_tls_1_3_radio_button", "web_encryption_min_tls_1_1_radio_button", [
        "web_encryption_AES128_SHA_cipher_checkbox",
        "web_encryption_ECDHE_ECDSA_AES128_SHA_cipher_checkbox",
        "web_encryption_TLS_AES_128_GCM_SHA256_cipher_checkbox"
    ]),
    ("Web Encryption Settings or Active Ciphers", "web-encryption", "web_encryption_max_tls_1_2_radio_button", "web_encryption_min_tls_1_1_radio_button", [
        "web_encryption_AES128_SHA_cipher_checkbox", "web_encryption_ECDHE_ECDSA_AES128_SHA_cipher_checkbox", 
        "web_encryption_TLS_AES_128_GCM_SHA256_cipher_checkbox", "web_encryption_TLS_AES_128_CCM_SHA256_cipher_checkbox"
    ]),
    ("Web Encryption Settings or Active Ciphers", "web-encryption", "web_encryption_max_tls_1_3_radio_button", "web_encryption_min_tls_1_0_radio_button", [
        "web_encryption_ECDHE_RSA_AES256_SHA_cipher_checkbox", "web_encryption_ECDHE_ECDSA_AES128_SHA_cipher_checkbox",
        "web_encryption_TLS_AES_128_GCM_SHA256_cipher_checkbox"
    ]),
    ("Web Encryption Settings or Active Ciphers", "web-encryption", "web_encryption_max_tls_1_2_radio_button", "web_encryption_min_tls_1_2_radio_button", [
        "web_encryption_ECDHE_RSA_AES256_SHA_cipher_checkbox", "web_encryption_ECDHE_ECDSA_AES128_SHA_cipher_checkbox",
        "web_encryption_TLS_AES_128_GCM_SHA256_cipher_checkbox"
    ]),
    ("Web Encryption Settings or Active Ciphers", "web-encryption", "web_encryption_max_tls_1_2_radio_button", "web_encryption_min_tls_1_0_radio_button", [
        "web_encryption_AES128_SHA_cipher_checkbox", "web_encryption_ECDHE_ECDSA_AES128_SHA_cipher_checkbox", 
        "web_encryption_TLS_AES_128_GCM_SHA256_cipher_checkbox", "web_encryption_TLS_AES_128_CCM_SHA256_cipher_checkbox"
    ])])

    def test_10_verify_web_encryption_settings_in_device_specific_policy(self, setting_name, setting_card, max_tls_radio, min_tls_radio, cipher_checkboxes):
        #
        self.printers.add_settings_in_device_specific_policy_tab(setting_name=setting_name,setting_card=setting_card,max_tls_radio=max_tls_radio,min_tls_radio=min_tls_radio,cipher_checkboxes=cipher_checkboxes)
        
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab(setting_name)