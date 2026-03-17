import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

class Test_10_Supplies_Web_Services_Categories_Settings(object):

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

    @pytest.mark.parametrize('setting_name, setting_card', [("Cartridge Threshold - Black", "cartridge-threshold-black"), ("Cartridge Threshold - Cyan", "cartridge-threshold-cyan"),
                                                             ("Cartridge Threshold - Magenta", "cartridge-threshold-magenta"), ("Cartridge Threshold - Yellow", "cartridge-threshold-yellow")])
    def test_01_verify_supplies_category_setting(self, setting_name, setting_card):
        #
        # Generate Cartridge Threshold value
        cartridge_threshold = random.randint(1,100)

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name,setting_card,settings_value=cartridge_threshold,category_type="Supplies")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab(setting_name)

    @pytest.mark.parametrize('settings_name, setting_card', [("Cartridge Very Low Action - Black", "very-low-action-black"),("Cartridge Very Low Action - Color", "very-low-action-color")])
    def test_02_verify_cartridge_settings_in_device_specific_policy(self,settings_name,setting_card):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        #Verify Cartridge Very Low Action Black Setting API Status
        cartridge_very_low_action_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/supply/configPrivate"
        response = get_api_response(self.stack,cartridge_very_low_action_settings_uri)
        cartridge_very_low_action_black_status=response.json()["state"]["reported"]["cdmData"]["blackVeryLowAction"]
        cartridge_very_low_action_color_status=response.json()["state"]["reported"]["cdmData"]["colorVeryLowAction"]

        all_cartridge_very_low_action_status =list((cartridge_very_low_action_black_status,cartridge_very_low_action_color_status))
       
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(settings_name,setting_card,settings_value=all_cartridge_very_low_action_status,category_type="Supplies")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab(settings_name)

    def test_03_verify_proxy_server_in_device_specific_policy(self):
        #
        #Generate random ip address
        test_ip_address="auto" +str(random.randint(1,9)) + "." +"com"
        test_port_number="22"+str(random.randint(29,99))
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify proxy server API Status
        proxy_server_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/network/proxyConfig"
        response = get_api_response(self.stack,proxy_server_uri)
        proxy_server_status = response.json()["state"]["reported"]["cdmData"]["httpProxy"]["enabled"]
       
        all_proxy_server_payload = list((proxy_server_status,test_ip_address,test_port_number))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Proxy Server",setting_card="proxy-server",settings_value=all_proxy_server_payload,category_type="Web Services")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Proxy Server")

    def test_04_verify_smart_cloud_print_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Web Services Smart Cloud Print API Status
        smart_cloud_print_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_api_response(self.stack,smart_cloud_print_uri)
        smart_cloud_print_status = response.json()["state"]["reported"]["cdmData"]["webServices"]["cloudPrint"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Smart Cloud Print",setting_card="smart-cloud-print",settings_value=smart_cloud_print_status,category_type="Web Services")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Smart Cloud Print")