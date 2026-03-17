import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_08_Workforce_Secure_Storage_CloudSettings(object):

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

    def test_01_verify_copy_background_cleanup_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()  
 
        # Verify Copy Background Cleanup uri API Status
        copy_background_cleanup_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_cloud_api_response(self.stack,copy_background_cleanup_uri)
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
        copy_contrast_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_cloud_api_response(self.stack,copy_contrast_uri)
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
        copy_darkness_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_cloud_api_response(self.stack,copy_darkness_uri)
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
        copy_optimize_text_or_picture_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_cloud_api_response(self.stack,copy_optimize_text_or_picture_uri)
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
        copy_paper_tray_selection_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_cloud_api_response(self.stack,copy_paper_tray_selection_uri)
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
        copy_sharpness_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/copy"
        response = get_cloud_api_response(self.stack,copy_sharpness_uri)
        copy_sharpness_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["sharpness"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Copy Sharpness", setting_card="copy-sharpness", settings_value=copy_sharpness_status, category_type="Copier")
 
        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
         
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Copy Sharpness")
    
    def test_07_verify_digital_sending_service_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Show Date and Time API Status
        digital_sending_service_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_cloud_api_response(self.stack,digital_sending_service_uri)
        allow_use_of_digital_send = response.json()["state"]["reported"]["cdmData"]["security"]["digitalSendingService"]["allowUse"]
        allow_transfer_to_digital_send = response.json()["state"]["reported"]["cdmData"]["security"]["digitalSendingService"]["allowTransfer"]
 
        digital_sending_service_status = list((allow_use_of_digital_send,allow_transfer_to_digital_send))
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Digital Sending Service",setting_card="digital-sending",settings_value=digital_sending_service_status,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Digital Sending Service")
 
    def test_08_verify_auto_send_settings_in_device_specific_policy(self):
        #
        #Generate random values
        days=random.randint(1,28)
        weeks=random.randint(1,4)
        months=random.randint(1,6)
        pages=random.randint(50,30000)
        https_url = "https://autotest" + str(random.randint(1, 9)) +"@testmail.com"
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Get Auto Send API Status
        auto_send_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/autosend/configuration"
        response = get_cloud_api_response(self.stack,auto_send_uri)
        auto_send_enabled_status=response.json()["state"]["reported"]["cdmData"]["autoSendEnabled"]
        auto_send_frequency_unit_status=response.json()["state"]["reported"]["cdmData"]["autoSendFrequency"]["frequencyUnit"]
        send_to_url_list_status=response.json()["state"]["reported"]["cdmData"]["sendToUrlList"]
        send_to_email_address=response.json()["state"]["reported"]["cdmData"]["sendToEmailList"]
       
        all_auto_send_status =list((auto_send_enabled_status,auto_send_frequency_unit_status,days,weeks,months,pages,send_to_url_list_status,https_url,send_to_email_address,email_address))
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="AutoSend",setting_card="auto-send",settings_value=all_auto_send_status,category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("AutoSend")
 
    def test_09_verify_add_fax_settings_pc_fax_send_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Fax Settings PC Fax send API Status
        pc_fax_send_config_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/fax/sendConfiguration"
        response = get_cloud_api_response(self.stack,pc_fax_send_config_uri)
        apc_fax_send_status = response.json()["state"]["reported"]["cdmData"]["pcFaxSendEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "PC Fax Send",setting_card= "pc-fax-send",settings_value= apc_fax_send_status,category_type= "Fax")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("PC Fax Send")
 
    def test_10_verify_email_notification_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_addresses = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        #Verify Email Notification Settings API Status
        email_notification_settings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/scanEmail"
        response = get_cloud_api_response(self.stack,email_notification_settings_uri)
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]
       
        all_email_notification_settings_status=list((notification_condition_status,notification_mode_status,email_addresses))
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Email Notification Settings",setting_card="email-notification",settings_value=all_email_notification_settings_status,category_type="Digital Sending")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Email Notification Settings")
 
    def test_11_verify_network_folder_notification_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_addresses = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        device_cloud_id = self.printers.get_device_cloud_id()
 
        #Verify Email Notification Setting API Status
        network_folder_notification_settings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/scanNetworkFolder"
       
        response = get_cloud_api_response(self.stack, network_folder_notification_settings_uri)
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]
       
        all_network_folder_notification_settings_status=list((notification_condition_status,notification_mode_status,email_addresses))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "Network Folder Notification Settings",setting_card= "network-folder-notification",settings_value= all_network_folder_notification_settings_status,category_type= "Digital Sending")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Network Folder Notification Settings")