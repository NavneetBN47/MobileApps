import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_05_Workforce_Batch3_CloudSettings(object):

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

    def test_01_verify_outgoing_server_settings_in_device_specific_policy(self):
        #
        server_name = "smtp"+str(random.randint(1,9))+".com"
        port_number = "22"+str(random.randint(11, 99))
        user_name = "user"+str(random.randint(1,9))
        password = "Testing@2904"
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Outgoing Server Settings API Status
        # outgoing_server_settings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/email/defaultSmtpServers"
        # response = get_cloud_api_response(self.stack,outgoing_server_settings_uri)
        # outgoing_server_sign_in = response.json()["state"]["reported"]["cdmData"]["servers"]["serverRequireAuthentication"]
 
        outgoing_server_status = list((server_name, port_number, user_name, password))
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Outgoing Servers",setting_card="outgoing-servers",settings_value= outgoing_server_status, category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Outgoing Servers")

    def test_02_verify_stored_data_pin_protection_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Stored Data PIN Protection API Status
        stored_data_pin_protection_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/storeJobManagement/configuration"
        response = get_cloud_api_response(self.stack,stored_data_pin_protection_uri)

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

    def test_03_verify_control_panel_language_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Control Panel Language API Status
        control_panel_language_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/controlPanel/configuration"
        response = get_cloud_api_response(self.stack,control_panel_language_uri)

        current_language_status = response.json()["state"]["reported"]["cdmData"]["currentLanguage"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Control Panel Language",setting_card="ctrl-panel-language",settings_value=current_language_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Control Panel Language")

    def test_04_verify_duplex_binding_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Duplex Binding API Status
        duplex_binding_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/print"
        response = get_cloud_api_response(self.stack,duplex_binding_uri)

        duplex_binding_status = response.json()["state"]["reported"]["cdmData"]["dest"]["print"]["duplexBinding"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Duplex Binding",setting_card="duplex-binding",settings_value=duplex_binding_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Duplex Binding")
