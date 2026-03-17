import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

class Test_09_Copier_Embedded_Categories_Proxies_Settings(object):

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
    
    def test_01_verify_copy_background_cleanup_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()  
 
        # Verify Copy Background Cleanup uri API Status
        copy_background_cleanup_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_api_response(self.stack,copy_background_cleanup_uri)
        copy_background_cleanup_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["backgroundCleanup"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Background Cleanup", setting_card="copy-bg-cleanup", settings_value=copy_background_cleanup_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Background Cleanup")
   
    def test_02_verify_copy_contrast_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Copy Contrast uri API Status
        copy_contrast_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_api_response(self.stack,copy_contrast_uri)
        copy_contrast_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["contrast"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Contrast", setting_card="copy-contrast", settings_value=copy_contrast_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Contrast")
 
    def test_03_verify_copy_darkness_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Copy Darkness uri API Status
        copy_darkness_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_api_response(self.stack,copy_darkness_uri)
        copy_darkness_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["exposure"]
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Darkness", setting_card="copy-darkness", settings_value=copy_darkness_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Darkness")
 
    def test_04_verify_copy_optimize_text_or_picture_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Copy Optimize Text/Picture uri API Status
        copy_optimize_text_or_picture_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_api_response(self.stack,copy_optimize_text_or_picture_uri)
        copy_optimize_text_or_picture_status = response.json()["state"]["reported"]["cdmData"]["src"]["scan"]["contentType"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Optimize Text/Picture", setting_card="copy-optimize", settings_value=copy_optimize_text_or_picture_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Optimize Text/Picture")
   
    def test_05_verify_copy_paper_tray_selection_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Copy Paper Tray Selection uri API Status
        copy_paper_tray_selection_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_api_response(self.stack,copy_paper_tray_selection_uri)
        copy_paper_tray_selection_status = response.json()["state"]["reported"]["cdmData"]["dest"]["print"]["mediaSource"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Paper Tray Selection", setting_card="copy-tray", settings_value=copy_paper_tray_selection_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Paper Tray Selection")
 
    def test_06_verify_copy_sharpness_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Copy Sharpness uri API Status
        copy_sharpness_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_api_response(self.stack,copy_sharpness_uri)
        copy_sharpness_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["sharpness"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Sharpness", setting_card="copy-sharpness", settings_value=copy_sharpness_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
         
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Sharpness")

    def test_07_verify_embedded_web_server_language_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Embedded Web Server language API Status
        ews_language_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/ews"
        response = get_api_response(self.stack,ews_language_uri)
        selected_language = response.json()["state"]["reported"]["cdmData"]["selectedLanguage"]
        language_source_status = response.json()["state"]["reported"]["cdmData"]["languageSource"]
        language_source_and_language = list((selected_language, language_source_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Embedded Web Server Language Settings",setting_card="ews-language",settings_value=language_source_and_language,category_type="Embedded Web Server")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Embedded Web Server Language Settings")

    def test_08_verify_time_services_settings_in_device_specific_policy(self):
        #
        #Generate random ip address
        time_services_ip_address="15.40.45."+str(random.randint(1,99))
        local_port=random.randint(1100,1900)
        synchronize_time=random.randint(1,168)

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Time Services API Status
        time_services_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/clock"
        response = get_api_response(self.stack,time_services_uri)
        time_services_system_time_sync = response.json()["state"]["reported"]["cdmData"]["systemTimeSync"]

        time_services_status = list((time_services_system_time_sync,time_services_ip_address,local_port,synchronize_time))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Time Services",setting_card="time-services",settings_value=time_services_status,category_type="Embedded Web Server")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Time Services")