import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_03_02_Workforce_Batch0_CloudSettings(object):

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

    def test_01_verify_direct_connect_ports_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Direct Connect Ports Status
        security_direct_connect_ports_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/usb"
        response = get_cloud_api_response(self.stack,security_direct_connect_ports_uri)
        direct_connect_ports_status = response.json()["state"]["reported"]["cdmData"]["enabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Direct Connect Ports",setting_card="dc-ports",settings_value=direct_connect_ports_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Direct Connect Ports")

    def test_02_verify_file_erase_mode_settings_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify File Erase Mode API Status
        file_erase_mode_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/storageDevices/configuration"
        response = get_cloud_api_response(self.stack,file_erase_mode_uri)
        file_erase_mode_status = response.json()["state"]["reported"]["cdmData"]["fileEraseMode"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="File Erase Mode",setting_card="file-erase",settings_value=file_erase_mode_status,category_type="File System")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("File Erase Mode")

    def test_03_verify_retain_print_jobs_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Retain Print Jobs API Status
        retain_print_jobs_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/storeJobManagement/configuration"
        response = get_cloud_api_response(self.stack,retain_print_jobs_uri)   
        stored_jobs_enabled_status = response.json()["state"]["reported"]["cdmData"]["storeJobEnabled"]
        temporary_stored_job_status = response.json()["state"]["reported"]["cdmData"]["temporaryJobRetentionInMinutes"]
        # standard_stored_job_status = response.json()["state"]["reported"]["cdmData"]["standardJobRetentionInMinutes"] # Standard Job Retention is not developed yet, So commenting this line
 
        retain_print_jobs_status = list((stored_jobs_enabled_status,temporary_stored_job_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Retain Print Jobs",setting_card="retain-jobs",settings_value= retain_print_jobs_status,category_type="Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Retain Print Jobs")

    def test_04_verify_control_panel_timeout_setting_in_device_specific_policy(self):
        #
        # Generate random number
        generate_timeout_value=random.randint(10,30)

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Control Panel Timeout",setting_card="ctrl-panel-timeout",settings_value=generate_timeout_value,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Control Panel Timeout")

    def test_05_verify_host_usb_plug_and_play_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Host USB Plug and Play Status
        security_host_usb_plug_and_play_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/usbHost/configuration"
        response = get_cloud_api_response(self.stack,security_host_usb_plug_and_play_uri)
        plug_and_play_status = response.json()["state"]["reported"]["cdmData"]["plugAndPlayEnabled"]
        print_from_usb_status = response.json()["state"]["reported"]["cdmData"]["printFromUsbEnabled"]
        scan_to_usb_status = response.json()["state"]["reported"]["cdmData"]["scanToUsbEnabled"]

        all_plug_and_play_status = list((plug_and_play_status,print_from_usb_status,scan_to_usb_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Host USB Plug and Play",setting_card="host-usb-pnp",settings_value=all_plug_and_play_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Host USB Plug and Play")

    def test_06_verify_secure_boot_presence_settings_in_device_specific_policy(self):
        #
        # Adding Secure Boot Presence in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Secure Boot Presence",setting_card="secure-boot-presence",category_type="Security")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Secure Boot Presence")

    def test_07_verify_intrusion_detection_presence_settings_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Intrusion Detection Presence",setting_card="intrusion-detect-presence",category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Intrusion Detection Presence")

    def test_08_verify_whitelisting_presence_settings_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Whitelisting Presence",setting_card="whitelist-presence",category_type="Security")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Whitelisting Presence")

    def test_09_verify_postscript_security_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get PostScript Security Status
        security_postscript_security_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/print/pdlConfiguration"
        response = get_cloud_api_response(self.stack,security_postscript_security_uri)
        postscript_security_status = response.json()["state"]["reported"]["cdmData"]["pclAndPostScript"]["postScriptSecurityEnabled"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="PostScript Security",setting_card="ps-security",settings_value=postscript_security_status,category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("PostScript Security")

    def test_10_verify_fax_receive_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        email_address = "autotest" + str(random.randint(1, 9)) + "@testmail.com"
        rings_to_answer_status = random.randint(1,6)

        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Fax Receive API Status
        fax_receive_enable_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/faxReceive/configuration"
        response = get_cloud_api_response(self.stack,fax_receive_enable_uri)
        fax_receive_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveEnabled"]
        fax_receive_method_status = response.json()["state"]["reported"]["cdmData"]["faxReceiveMethod"]

        # Verify Fax Receive Set Common Job Status
        fax_receive_set_common_job_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/jobTicket/configuration/defaults/receiveFax"
        response = get_cloud_api_response(self.stack,fax_receive_set_common_job_uri)
        paper_selection_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["imageModifications"]["outputCanvasMediaId"]
        notification_condition_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationCondition"]
        notification_mode_status = response.json()["state"]["reported"]["cdmData"]["pipelineOptions"]["notification"]["notificationMode"]

        # Verify Fax Receive Set Internal Modem API Status
        fax_receive_set_internal_modem_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/faxModem/configuration"
        response = get_cloud_api_response(self.stack,fax_receive_set_internal_modem_uri)
        ringer_volume_status = response.json()["state"]["reported"]["cdmData"]["analogFaxReceiveSettings"]["ringerVolume"]

        all_fax_receive_settings_status = list((fax_receive_status,paper_selection_status,notification_condition_status,notification_mode_status,email_address,fax_receive_method_status,ringer_volume_status,rings_to_answer_status))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Fax Receive Settings",setting_card="fax-receive",settings_value=all_fax_receive_settings_status,category_type="Fax")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Fax Receive Settings")