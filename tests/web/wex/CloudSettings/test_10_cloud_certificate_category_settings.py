import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const
 
class Test_10_Cloud_Certificate_Category_Settings(object):
 
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
 
    def test_01_verify_identity_certificate_in_device_specific_policy(self):
        #
        # Generate random organization and location for the certificate settings
        organization_name = "Org" + str(random.randint(10, 99))
        organization_unit = "Unit" + str(random.randint(10, 99))
        city_name = "City" + str(random.randint(10, 99))
        state_name = "State" + str(random.randint(10, 99))
        upn_username = "upn_user" + str(random.randint(10, 99))
        upn_domain = "domain"+str(random.randint(1,9))+".com"
        est_connector_url = "https://ao-tlspd.dev.ven-eco.com"
        est_connector_port = "50443"
        est_server_username = "hp-est-2"
        est_server_password = "N-mP-Gc8_ktsZx-EK6m"
        arbitrary_label = "hp-est-2"
        certificate_renewal_threshold = random.randint(1, 3500)
 
        device_cloud_id = self.printers.get_device_cloud_id()  
 
        # Verify Identity Certificate uri API Status
        identity_certificate_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/certificate/certificateSigningRequest"
        response = get_cloud_api_response(self.stack,identity_certificate_uri)
        identity_certificate = response.json()["state"]["reported"]["cdmData"]["certificateAttributes"]
 
        identity_certificate_status = list((organization_name, organization_unit, city_name, state_name, upn_username, upn_domain, est_connector_url, est_connector_port,
                                        est_server_username, est_server_password, arbitrary_label, certificate_renewal_threshold))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Identity Certificate", setting_card="identity-certificate", settings_value=identity_certificate_status, category_type="Certificate")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
   
        # Update IP address as common name in identity certificate setting
        self.printers.update_ip_address_as_common_name_in_identity_certificate_setting(setting_card="identity-certificate")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Identity Certificate")