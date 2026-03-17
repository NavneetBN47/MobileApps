import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

#Generate random device properties values
company_name="company"+str(random.randint(1,99))

class Test_08_File_System_Fax_Categories_Proxies_Settings(object):

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

    def test_01_verify_file_system_access_protocol_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get File System Access Protocols API Status
        file_system_access_protocol_uri = w_const.get_connector_deviceconfigs_v2_uri(self.stack) + f"/{device_cloud_id}/print"
        response = get_api_response(self.stack,file_system_access_protocol_uri)
        ps_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["psFileSystemAccessEnabled"]
        pjl_file_system_access_enabled_status = response.json()["state"]["reported"]["cdmData"]["pjlFileSystemAccessEnabled"]

        all_file_system_protocol_setting_status = list((ps_file_system_access_enabled_status,pjl_file_system_access_enabled_status))

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="File System Access Protocols",setting_card="fs-access-protocol",settings_value=all_file_system_protocol_setting_status,category_type="File System")
        
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("File System Access Protocols")

    def test_02_verify_file_erase_mode_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify File Erase Mode API Status
        file_erase_mode_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/storageDevices"
        response = get_api_response(self.stack,file_erase_mode_uri)
        file_erase_mode_status = response.json()["state"]["reported"]["cdmData"]["fileEraseMode"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="File Erase Mode",setting_card="file-erase",settings_value=file_erase_mode_status,category_type="File System")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("File Erase Mode")

    def test_03_verify_auto_firmware_update_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Auto Firmware Update Status
        auto_firmware_update_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/firmwareUpdate/autoUpdate/configuration"
        response = get_api_response(self.stack,auto_firmware_update_uri)
        auto_firmware_update_status = response.json()["state"]["reported"]["cdmData"]["scheduleEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Auto Firmware Update",setting_card="auto-fw-update",settings_value=auto_firmware_update_status,category_type="Firmware")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Auto Firmware Update")

    def test_04_verify_fax_send_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        domain_name = "auto" +str(random.randint(1,9)) + "." +"com"
        account_email_address = "autotest" + str(random.randint(1,9)) + "@testmail.com"

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify fax send settings API Status
        fax_send_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/fax/sendConfiguration"
        response = get_api_response(self.stack,fax_send_settings_uri)
        fax_send_status = response.json()["state"]["reported"]["cdmData"]["faxSendEnabled"]
        fax_send_method = response.json()["state"]["reported"]["cdmData"]["faxSendMethod"]

        # Verify fax send set common job API Status
        fax_send_set_common_job_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/scanFax"
        response = get_api_response(self.stack,fax_send_set_common_job_uri)
        background_method = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["backgroundCleanup"]
        exposure = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["exposure"]
        contrast = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["contrast"]
        sharpness = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["sharpness"]
        notification_condition = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]

        # Verify fax send set internal modem settings Status
        fax_send_set_internal_modem_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/faxModem"
        response = get_api_response(self.stack,fax_send_set_internal_modem_uri)
        error_correction_mode_status = response.json()["state"]["reported"]["cdmData"]["analogFaxOperation"]["errorCorrectionModeEnabled"]
        jbig_compression_status = response.json()["state"]["reported"]["cdmData"]["analogFaxOperation"]["compressionJBIGEnabled"]

        all_fax_send_status = list((fax_send_status,fax_send_method,domain_name,account_email_address,background_method,exposure,contrast,sharpness,
                                    notification_condition,notification_mode,email_address,error_correction_mode_status,jbig_compression_status))
        
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Fax Send Settings",setting_card="fax-send",settings_value=all_fax_send_status,category_type="Fax")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Fax Send Settings")

    def test_05_verify_fax_receive_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        rings_to_answer_status = random.randint(1,6)

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Fax Receive API Status
        fax_receive_enable_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/faxReceive"
        response = get_api_response(self.stack,fax_receive_enable_uri)
        fax_receive_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveEnabled"]
        fax_receive_method_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveMethod"]

        # Verify Fax Receive Set Common Job Status
        fax_receive_set_common_job_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/defaults/receiveFax"
        response = get_api_response(self.stack,fax_receive_set_common_job_uri)
        paper_selection_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["outputCanvasMediaId"]
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]

        # Verify Fax Receive Set Internal Modem API Status
        fax_receive_set_internal_modem_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/faxModem"
        response = get_api_response(self.stack,fax_receive_set_internal_modem_uri)
        ringer_volume_status = response.json()["state"]["reported"]["cdmData"]["analogFaxReceiveSettings"]["ringerVolume"]

        all_fax_receive_settings_status = list((fax_receive_status,paper_selection_status,notification_condition_status,notification_mode_status,email_address,fax_receive_method_status,ringer_volume_status,rings_to_answer_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Fax Receive Settings",setting_card="fax-receive",settings_value=all_fax_receive_settings_status,category_type="Fax")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Fax Receive Settings")

    def test_06_verify_fax_header_settings_in_device_specific_policy(self):
        #
        #Generate random phone number
        test_phone_number="5678"+str(random.randint(11,99))

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Fax Header Settings API Status
        fax_header_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/faxModem"
        response = get_api_response(self.stack,fax_header_uri)
        fax_header_country_status = response.json()["state"]["reported"]["cdmData"]["analogFaxSetup"]["analogFaxCountry"]

        fax_header_status = list((test_phone_number,company_name,fax_header_country_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Fax Header Settings",setting_card="fax-header",settings_value=fax_header_status,category_type="Fax")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Fax Header Settings")

    def test_07_verify_ip_fax_setting_in_device_specific_policy(self):
 
        #Generate random fax id
        fax_ip="567"+str(random.randint(11,99))
 
        all_ip_fax_settings_status = list((fax_ip,company_name))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "IP Fax Settings",setting_card= "ip-fax",settings_value= all_ip_fax_settings_status,category_type= "Fax")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("IP Fax Settings")

    def test_08_verify_add_fax_settings_pc_fax_send_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Fax Settings PC Fax send API Status
        pc_fax_send_config_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/fax/sendConfiguration"
        response = get_api_response(self.stack,pc_fax_send_config_uri)
        apc_fax_send_status = response.json()["state"]["reported"]["cdmData"]["pcFaxSendEnabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name= "PC Fax Send",setting_card= "pc-fax-send",settings_value= apc_fax_send_status,category_type= "Fax")
 
        #Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("PC Fax Send")
