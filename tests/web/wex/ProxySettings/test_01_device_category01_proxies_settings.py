import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

#Generate random device properties values
asset_number=random.randint(100,999)
company_name="company"+str(random.randint(1,99))
contact_person="user"+str(random.randint(1,99))
device_location="location"+str(random.randint(1,99))
device_name="device_name"+str(random.randint(1,99))

class Test_01_Workforce_Device_Category01_Proxies_Settings(object):

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
        self.emulator_serial_number = self.account["emulator_settings_serial_number"]

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
        if self.emulator_serial_number != "":
            self.serial_number = self.emulator_serial_number
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

    def test_05_verify_device_name_in_device_specific_policy(self):
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

    def test_06_verify_control_panel_language_policy_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Control Panel Language API Status
        control_panel_language_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/controlpanel"
        response = get_api_response(self.stack,control_panel_language_uri)
        current_language_status = response.json()["state"]["reported"]["cdmData"]["currentLanguage"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Control Panel Language",setting_card="ctrl-panel-language",settings_value= current_language_status,category_type="Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Verify updated language in device details properties tab
        self.printers.click_printers_details_page_properties_tab()
        self.printers.click_device_accordion()
        self.printers.click_printer_device_details_device_property_card("ctrl-panel-language")
        assert current_language_status != self.printers.get_printer_device_details_device_property_value("ctrl-panel-language")

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Control Panel Language")

    def test_07_verify_add_device_settings_date_and_time_format_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Web Services Smart Cloud Print API Status
        device_date_and_time_format_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/clock"
        response = get_api_response(self.stack,device_date_and_time_format_uri)
        device_date_format = response.json()["state"]["reported"]["cdmData"]["dateFormat"]
        device_time_format = response.json()["state"]["reported"]["cdmData"]["timeFormat"]
        device_date_and_time_format = list((device_date_format, device_time_format))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Date/Time Format",setting_card="date-time-format",settings_value=device_date_and_time_format,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Date/Time Format")

    def test_08_verify_energy_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Energy Settings API Status
        energy_setting_v3_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/power/configuration"
        response = get_api_response(self.stack,energy_setting_v3_uri)
        inactivityTimeout = response.json()["state"]["reported"]["cdmData"]["inactivityTimeout"]
        shutdownTimeout = response.json()["state"]["reported"]["cdmData"]["shutdownTimeout"] 

        all_energy_setting_status=list((inactivityTimeout,shutdownTimeout))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Energy Settings",setting_card="energy-settings",settings_value=all_energy_setting_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Energy Settings")

    def test_09_verify_outgoing_server_settings_in_device_specific_policy(self):
        #
        server_name = "smtp"+str(random.randint(1,9))+".com"
        port_number = "22"+str(random.randint(11, 99))
        user_name = "user"+str(random.randint(1,9))
        password = "Testing@2904"
 
        outgoing_server_status = list((server_name, port_number, user_name, password))
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Outgoing Servers",setting_card="outgoing-servers",settings_value= outgoing_server_status, category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Outgoing Servers")

    def test_10_verify_retain_temporary_print_jobs_after_reboot_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Retain Temporary Print Jobs after Reboot API Status
        retain_temporary_print_jobs_after_reboot_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/storeJobManagement"
        response = get_api_response(self.stack,retain_temporary_print_jobs_after_reboot_uri)
        retain_temporary_print_jobs_after_reboot_status = response.json()["state"]["reported"]["cdmData"]["temporaryJobRetentionPolicy"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Retain Temporary Print Jobs after Reboot",setting_card="retain-jobs-after-reboot",settings_value=retain_temporary_print_jobs_after_reboot_status,category_type="Devices")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Retain Temporary Print Jobs after Reboot")
 
    def test_11_verify_temporary_job_storage_limit_in_device_specific_policy(self):
        #
        # Generate random number for temporary job storage limit
        temporary_job_storage_limit = random.randint(1,300)
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Temporary Job Storage Limit",setting_card="job-storage-limit-temporary",settings_value=temporary_job_storage_limit,category_type="Devices")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Temporary Job Storage Limit")