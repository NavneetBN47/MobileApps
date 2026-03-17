import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const

class Test_06_Workforce_Batch3_Amazon_CloudSettings(object):

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

    def test_01_verify_bootloader_password_setting_from_properties_tab(self):
        random_password = "430"+str(random.randint(1,9))

        device_cloud_id = self.printers.get_device_cloud_id()

        # Get Bootloader Password Setting API Status
        bootloader_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/bootloader"
        response = get_cloud_api_response(self.stack, bootloader_uri)
        bootloader_password_status = response.json()["state"]["reported"]["cdmData"]["passwordSet"]
        # Only proceed if password is not already set
        if bootloader_password_status != "true":

            # Get Bootloader Password Setting UI Status
            self.printers.click_printers_details_page_properties_tab()
            self.printers.click_security_accordion()
            self.printers.click_printer_device_details_device_property_card("bootloader-password")
            assert self.printers.get_printer_device_details_device_property_value("bootloader-password") == "Not Configured"
            
            # Updating the Password from Dvice - Specific Policy tab
            self.printers.click_printers_details_page_policies_tab()
            self.printers.add_settings_in_device_specific_policy_tab(setting_name="Bootloader Password",setting_card="bootloader-password",settings_value= random_password,category_type="Security")
    
            # verify the compliance of that device after the device specific policy is applied.
            self.printers.verify_policies_compliance_status(self.serial_number)
    
            # Remove the device specific policy
            self.printers.remove_settings_in_device_specific_policy_tab("Bootloader Password")

        else:
            # Verify current status in Properties Tab
            self.printers.click_printers_details_page_policies_tab()
            self.printers.click_printers_details_page_properties_tab()
            self.printers.click_security_accordion()
            self.printers.click_printer_device_details_device_property_card("bootloader-password")
            self.printers.get_printer_device_details_device_property_value("bootloader-password") == "Configured"

    def test_02_verify_smart_cloud_print_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Web Services Smart Cloud Print API Status
        smart_cloud_print_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_cloud_api_response(self.stack,smart_cloud_print_uri)
        smart_cloud_print_status = response.json()["state"]["reported"]["cdmData"]["webServices"]["cloudPrint"]

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Smart Cloud Print",setting_card="smart-cloud-print",settings_value=smart_cloud_print_status,category_type="Web Services")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Smart Cloud Print")

    def test_03_verify_restrict_color_setting_in_device_specific_policy(self):
        #
        # Generate random application name
        application_name = "HP Smart"+str(random.randint(1,9))
 
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Restrict Color API Status
        restrict_color_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/legacyAttributes"
        response = get_cloud_api_response(self.stack,restrict_color_uri)
        color_settings = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["restrictColor"]
        restrict_by_user_permissions = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingPermissionSets"]
        restrict_by_application = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["usingApplicationSettings"]
        default_permission = response.json()["state"]["reported"]["cdmData"]["security"]["colorAccessControl"]["customColorAccess"]["allowColorAndQuality"]
 
        restrict_color_status = list((color_settings,restrict_by_user_permissions,restrict_by_application,default_permission,application_name))
 
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Restrict Color",setting_card="restrict-color",settings_value= restrict_color_status,category_type="Security")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
 
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Restrict Color")

    #Commenting the below testcase as it is the setting turn the deivce to offline mode
    # def test_52_verify_sleep_settings_in_device_specific_policy(self):
    #     #
    #     #Generate Random Values
    #     sleep_mode_values=random.randint(0,119)
    #     auto_off_after_sleep_values=random.randint(0,119)    
 
    #     device_cloud_id = self.printers.get_device_cloud_id()
 
    #     # Verify Sleep Settings Setting API Status
    #     sleep_settings_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/power/sleepConfiguration"
    #     response = get_cloud_api_response(self.stack, sleep_settings_uri)
    #     sleep_auto_off_timer_status=response.json()["state"]["reported"]["cdmData"]["sleepAutoOffTimerEnabled"]
    #     auto_on_events_status=response.json()["state"]["reported"]["cdmData"]["autoOnEvents"]
 
    #     all_sleep_settings_status =list((sleep_auto_off_timer_status,sleep_mode_values,auto_on_events_status,auto_off_after_sleep_values))
 
    #     # Adding Settings in Device-specific Policy tab
    #     self.printers.add_settings_in_device_specific_policy_tab(setting_name="Sleep Settings",setting_card="sleep-settings",settings_value=all_sleep_settings_status,category_type="Devices")
 
    #     # verify the compliance of that device after the device specific policy is applied.
    #     self.printers.verify_policies_compliance_status(self.serial_number)
 
    #     # Remove the device specific policy
    #     self.printers.remove_settings_in_device_specific_policy_tab("Sleep Settings")

    def test_04_verify_printer_firmware_update_setting_in_device_specific_policy(self):
        #
        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Printer Firmware Update (send as Printjob)",setting_card="remote-fw-update",category_type="Security")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Revert the setting and verify the remediation status
        self.printers.click_printers_details_policies_tab_edit_button()
        self.printers.click_device_specific_policy_next_button()
        self.printers.click_device_specific_policy_settings_card("remote-fw-update")
        self.printers.click_printer_firmware_update_checkbox()
        self.printers.click_device_specific_policy_create_button()
        self.printers.click_change_not_recommended_popup_confirm_button()

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Printer Firmware Update (send as Printjob)")

    def test_05_verify_cross_origin_resource_sharing_in_device_specific_policy(self):
        #
        site_name = "auto" +str(random.randint(1,9)) + "." +"com"

        device_cloud_id = self.printers.get_device_cloud_id()

        #Get Cross-Origin Resource Sharing (CORS) Setting API Status
        cors_setting_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/security/systemConfig"
        response = get_cloud_api_response(self.stack,cors_setting_uri)
        cors_setting_checkbox = response.json()["state"]["reported"]["cdmData"]["corsEnabled"]

        cors_setting_status = list((cors_setting_checkbox,site_name))

        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Cross-Origin Resource Sharing (CORS)",setting_card="cors",settings_value= cors_setting_status, category_type="Security")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)    

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Cross-Origin Resource Sharing (CORS)")

    def test_06_verify_configuration_precedence_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()

        # Verify Configuration Precedence API Status
        configuration_precedence_uri = w_const.get_cloud_iot_base_v2_uri(self.stack) + f"/{device_cloud_id}/ioConfig/adapterConfigs/eth0"
        response = get_cloud_api_response(self.stack, configuration_precedence_uri)

        # Convert the Response object to a Python dictionary using .json()
        response_data = response.json()

        # Accessing the first item from the ipConfigPrecedence and extracting the precedence and method
        ip_config = response_data["state"]["reported"]["cdmData"]["ipConfigPrecedence"]

        # Accessing the first entry in the list (index 0)
        configuration_precedence = ip_config[0]["precedence"]
        configuration_method = ip_config[0]["method"]

        configuration_precedence_status =list((configuration_precedence,configuration_method))

        # Adding Settings in Device-specific Policy tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Configuration Precedence", setting_card="configuration-precedence", settings_value=configuration_precedence_status, category_type="Network")

        # Verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Configuration Precedence")

    def test_07_verify_ftp_print_setting_in_device_specific_policy(self):
        #
        device_cloud_id = self.printers.get_device_cloud_id()
 
        # Verify Network FTP Print API Status
        network_ftp_print_uri = w_const.get_cloud_iot_base_v1_uri(self.stack) + f"/{device_cloud_id}/network/printServices"
        response = get_cloud_api_response(self.stack,network_ftp_print_uri)
        ftp_print_status = response.json()["state"]["reported"]["cdmData"]["ftpPrint"]["enabled"]
       
        # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="FTP Print",setting_card="ftp-print",settings_value= ftp_print_status, category_type="Network")
 
        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("FTP Print")

    def test_09_home_screen_customization_future_smart(self):
        #
         # Adding Settings in Device Specific Policy Tab
        self.printers.add_settings_in_device_specific_policy_tab(setting_name="Home Screen Customization - FutureSmart",setting_card="home-screen-custom", category_type="Devices")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)

        # Revert the setting and verify the remediation status
        self.printers.update_home_screen_customization_future_smart_to_default_hp_or_samsung(setting_card="home-screen-custom")

        # verify the compliance of that device after the device specific policy is applied.
        self.printers.verify_policies_compliance_status(self.serial_number)
       
        # Remove the device specific policy
        self.printers.remove_settings_in_device_specific_policy_tab("Home Screen Customization - FutureSmart")