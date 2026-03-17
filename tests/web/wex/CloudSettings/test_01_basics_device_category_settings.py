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

class Test_01_Workforce_Basics_Device_Category_CloudSettings(object):

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

    def test_01_verify_asset_number_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Asset Number",setting_card="asset-number",settings_value=asset_number,category_type="Devices")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Verify the asset number in device details overview tab
        self.printers.click_printers_details_overview_tab()
        assert str(asset_number) == self.printers.get_general_information_section_overview_tab_asset_number()
 
        # Verify the asset number in device details properties tab
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.click_printer_device_details_device_property_card("asset-number")
        assert str(asset_number) == self.printers.get_printer_device_details_device_property_value("asset-number")
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Asset Number")
 
    def test_02_verify_company_name_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Company Name",setting_card="company-name",settings_value=company_name,category_type="Devices")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Verify the company name in device details properties tab
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.click_printer_device_details_device_property_card("company-name")
        assert company_name == self.printers.get_printer_device_details_device_property_value("company-name")
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Company Name")
   
    def test_03_verify_contact_person_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Contact Person",setting_card="contact-person",settings_value=contact_person,category_type="Devices")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Verify the contact person in device details properties tab
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.click_printer_device_details_device_property_card("contact-person")
        assert contact_person == self.printers.get_printer_device_details_device_property_value("contact-person")
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Contact Person")
 
    def test_04_verify_device_location_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Device Location",setting_card="device-location",settings_value=device_location,category_type="Devices")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Verify the device location in device details properties tab
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.click_printer_device_details_device_property_card("device-location")
        assert device_location == self.printers.get_printer_device_details_device_property_value("device-location")
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Device Location")

    def test_05_verify_use_requested_tray_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Use Requested Tray API Status
        use_requested_tray_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling/configuration"
        response = get_cloud_api_response(self.stack,use_requested_tray_uri)
        use_requested_tray_status = response.json()["state"]["reported"]["cdmData"]["useRequestedTray"]
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Use Requested Tray",setting_card="use-requested-tray",settings_value= use_requested_tray_status,category_type="Devices")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Use Requested Tray")
 
    def test_06_verify_override_a4_letter_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Override a4 letter API Status
        override_letter_a4_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling/configuration"
        response = get_cloud_api_response(self.stack,override_letter_a4_uri)
        override_letter_a4_status = response.json()["state"]["reported"]["cdmData"]["a4LetterOverrideEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Override A4/Letter",setting_card="override-letter-a4",settings_value=override_letter_a4_status,category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Override A4/Letter")
 
    def test_07_manual_feed_prompt_setting_in_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Manual Feed Prompt API Status
        manual_feed_prompt_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling/configuration"
        response = get_cloud_api_response(self.stack,manual_feed_prompt_uri)
        manual_feed_prompt_status = response.json()["state"]["reported"]["cdmData"]["manualFeedprompt"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Manual Feed Prompt",setting_card="manual-feed-prompt",settings_value=manual_feed_prompt_status,category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Manual Feed Prompt")

    def test_08_verify_size_type_prompt_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Size Type Prompt API Status
        size_type_prompt_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling/configuration"
        response = get_cloud_api_response(self.stack,size_type_prompt_uri)
        size_type_prompt_status = response.json()["state"]["reported"]["cdmData"]["sizeTypeEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Size / Type Prompt",setting_card="size-type-prompt",settings_value=size_type_prompt_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Size / Type Prompt")
 
    def test_09_verify_support_contact_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Support Contact",setting_card="support-contact",settings_value=support_contact,category_type="Network")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Support Contact")
 
    def test_10_verify_system_location_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="System Location",setting_card="system-location",settings_value=system_location,category_type="Network")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("System Location")
 
    def test_11_verify_system_contact_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="System Contact",setting_card="system-contact",settings_value=system_contact,category_type="Network")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("System Contact")