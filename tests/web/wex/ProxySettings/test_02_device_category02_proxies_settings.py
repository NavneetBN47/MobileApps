import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const 

class Test_02_Device_Category02_Proxies_Settings(object):

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

    def test_01_manual_feed_prompt_setting_in_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Manual Feed Prompt API Status
        manual_feed_prompt_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling"
        response = get_api_response(self.stack,manual_feed_prompt_uri)
        manual_feed_prompt_status = response.json()["state"]["reported"]["cdmData"]["manualFeedprompt"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Manual Feed Prompt",setting_card="manual-feed-prompt",settings_value=manual_feed_prompt_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Manual Feed Prompt")

    def test_02_verify_override_a4_letter_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Override a4 letter API Status
        override_letter_a4_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling"
        response = get_api_response(self.stack,override_letter_a4_uri)
        override_letter_a4_status = response.json()["state"]["reported"]["cdmData"]["a4LetterOverrideEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Override A4/Letter",setting_card="override-letter-a4",settings_value=override_letter_a4_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Override A4/Letter")

    def test_03_verify_size_type_prompt_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Size Type Prompt API Status
        size_type_prompt_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling"
        response = get_api_response(self.stack,size_type_prompt_uri)
        size_type_prompt_status = response.json()["state"]["reported"]["cdmData"]["sizeTypeEnabled"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Size / Type Prompt",setting_card="size-type-prompt",settings_value=size_type_prompt_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Size / Type Prompt")

    def test_04_verify_tray1_mode_or_manual_feed_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get tray1 mode manual feed API Status
        tray1_mode_manual_feed_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling"
        response = get_api_response(self.stack,tray1_mode_manual_feed_uri)
        tray1_mode_manual_feed_status = response.json()["state"]["reported"]["cdmData"]["manualFeedEnable"]
        
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Tray 1 Mode / Manual Feed",setting_card="manual-feed",settings_value=tray1_mode_manual_feed_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Tray 1 Mode / Manual Feed")

    def test_05_verify_use_requested_tray_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Device use requested tray API Status
        use_requested_tray_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/mediaHandling"
        response = get_api_response(self.stack,use_requested_tray_uri)
        use_requested_tray_status = response.json()["state"]["reported"]["cdmData"]["useRequestedTray"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Use Requested Tray",setting_card="use-requested-tray",settings_value= use_requested_tray_status,category_type="Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Use Requested Tray")

    def test_06_verify_time_zone_day_light_saving_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Time Zone Day Light Saving  API Status
        time_zone_day_light_saving_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/clock"
        response = get_api_response(self.stack,time_zone_day_light_saving_uri)
        time_zone_day_light_saving_status = response.json()["state"]["reported"]["cdmData"]["timeZone"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Time Zone/Daylight Saving",setting_card="time-zone",settings_value=time_zone_day_light_saving_status,category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Time Zone/Daylight Saving")

    def test_07_verify_retain_print_job_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Retain Print Jobs API Status
        retain_print_jobs_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/storeJobManagement"
        response = get_api_response(self.stack,retain_print_jobs_uri)   
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

    def test_08_verify_online_solutions_setting_in_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Online Solutions - Show Event QR Code API Status
        show_event_qr_code_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/controlpanel"
        response = get_api_response(self.stack,show_event_qr_code_uri)
        show_event_qr_code_status = response.json()["state"]["reported"]["cdmData"]["showEventQrCode"]

        # Verify Online Solutions - Show Links in the EWS API Status
        show_support_links_uri  = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/ews"
        response = get_api_response(self.stack,show_support_links_uri)
        show_support_links_status = response.json()["state"]["reported"]["cdmData"]["showSupportLinks"]
        show_links_in_event_log_status = response.json()["state"]["reported"]["cdmData"]["showLinksInEventLog"]

        online_solutions_status = list((show_event_qr_code_status,show_support_links_status,show_links_in_event_log_status))

         # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Online Solutions",setting_card="online-solutions",settings_value= online_solutions_status,category_type="Devices")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Online Solutions")

    def test_09_verify_sleep_settings_in_device_specific_policy(self):
        #
        #Generate Random Values
        sleep_mode_values=random.randint(0,119)
        auto_off_after_sleep_values=random.randint(0,119)    
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Sleep Settings Setting API Status
        sleep_settings_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/power/sleepconfiguration"
        response = get_api_response(self.stack, sleep_settings_uri)
        sleep_auto_off_timer_status=response.json()["state"]["reported"]["cdmData"]["sleepAutoOffTimerEnabled"]
        auto_on_events_status=response.json()["state"]["reported"]["cdmData"]["autoOnEvents"]
 
        all_sleep_settings_status =list((sleep_auto_off_timer_status,sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values))
 
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Sleep Settings",setting_card="sleep-settings",settings_value=all_sleep_settings_status,category_type="Devices")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Sleep Settings")

    def test_10_verify_auto_send_settings_in_device_specific_policy(self):
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
        auto_send_uri = w_const.get_connector_deviceconfigs_v1_uri(self.stack) + f"/{device_cloud_id}/autosend"
        response = get_api_response(self.stack,auto_send_uri)
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
