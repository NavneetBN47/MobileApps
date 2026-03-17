import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ecp.ecp_api_utility import *
import random
from time import sleep
pytest.app_info = "ECP"

# App Deployment Device serial number
app_deployment_serial_num = "MNSTNHMS01"

#Generate test group name
app_group_name="auto_device_group"+str(random.randint(1000,9999))
        
#Generate test policy name
app_policy_name="auto_policy_name"+str(random.randint(100,999))

class Test_13_ECP_Cloud_Device_App_Deployement_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_devices(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        # self.devices.click_devices_group_all_option("All")
        return self.devices.verify_device_page()
        
    def test_01_verify_app_deployment_ui_policy_setting(self):
        #
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()                                                    
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy_for_app_deployment(app_policy_name,policy_settings="App Deployment",modify_settings="app-deployment",category_type="Solutions")
 
        # Veriying the table is loaded or not
        self.endpoint_security.verify_table_loaded()
    
    def test_02_verify_app_deployment_setting_for_printer_on_agent_app(self):
        #
        self.devices.create_group_with_one_device(app_group_name,app_deployment_serial_num)
        self.devices.verify_device_page()

        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy(app_policy_name,policy_settings="App Deployment",modify_settings="app-deployment",category_type="Solutions")
 
        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(app_group_name,app_policy_name)
   
        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(app_group_name)
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)
 
        # Uninstalling the Printer On Agent App
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.search_policy(app_policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_create_policy_policy_settings_card("app-deployment")
        self.endpoint_security.uninstal_added_app_in_app_deployment_settings()
        self.endpoint_security.click_policy_save_button()

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(app_group_name)
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)
    
        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(app_group_name, app_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(app_group_name)

    def test_03_verify_app_deployment_setting_for_regus_plugin_app(self):
        #
        self.devices.create_group_with_one_device(app_group_name,app_deployment_serial_num)
        self.devices.verify_device_page()
        
        # Creating the Policy
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.create_policy_for_app_deployment_with_regus_plugin(app_policy_name,policy_settings="App Deployment",modify_settings="app-deployment")

        # Add the policy to the device group
        self.endpoint_security.add_policy_to_device_group(app_group_name,app_policy_name)

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(app_group_name)
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Uninstalling the Regus Plugin App
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.search_policy(app_policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_create_policy_policy_settings_card("app-deployment")
        self.endpoint_security.uninstal_added_app_in_app_deployment_settings()
        self.endpoint_security.click_policy_save_button()

        # Verify the compliance status of that device.
        self.home.click_devices_menu_btn()
        self.devices.navigating_to_device_details_tab(app_group_name)
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Clean up the policy and device group
        self.home.click_policies_menu_btn()
        self.endpoint_security.unassign_policy_from_group(app_group_name, app_policy_name)
        self.home.click_devices_menu_btn()
        self.devices.delete_group(app_group_name)

    def test_04_verify_app_deployment_setting_for_hp_for_sharepoint_online_app_in_device_specific_policy_tab(self):
        # Search the device and navigate to Device details - Device Specific Policy tab
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_details_policy_widget_expand_button()
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("App Deployment")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()

        # Add the policy in Device Specific Policy tab
        self.endpoint_security.add_hp_for_sharepoint_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        sleep(7)
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)
        
        # Uninstalling the Regus Plugin App from Device Specific Policy tab
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_next_button()
        sleep(5)  # Wait for UI to load
        self.endpoint_security.uninstal_added_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

        # verify the compliance of that device after the device specific policy is applied.
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        sleep(7)
        self.devices.click_device_details_policy_widget_expand_button()
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("App Deployment")

    def test_05_verify_hp_for_box_and_hp_for_clio_app_settings_in_device_specific_policy_tab(self):
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_details_policy_widget_expand_button()
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("App Deployment")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()

        # Add the policy in Device Specific Policy tab
        self.endpoint_security.add_hp_for_box_and_hp_for_clio_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

         # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Uninstalling the Regus Plugin App from Device Specific Policy tab
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_next_button()
        sleep(5)  # Wait for UI to load
        self.endpoint_security.uninstal_added_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

        # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("App Deployment")

    def test_06_verify_hp_for_dropbox_app_settings_in_device_specific_policy_tab(self):
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_details_policy_widget_expand_button()
        sleep(5)
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("App Deployment")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()

        # Add the policy in Device Specific Policy tab
        self.endpoint_security.add_hp_for_dropbox_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

         # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("App Deployment")

    # Hp for Google Drive, HP for OneDrive, HP for OneDrive Business apps
    def test_07_verify_hp_for_google_drive_hp_for_onedrive_and_hp_for_onedrive_business_app_settings_in_device_specific_policy_tab(self):
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_details_policy_widget_expand_button()
        sleep(5)
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("App Deployment")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()

        # Add the policy in Device Specific Policy tab
        self.endpoint_security.add_hp_for_google_drive_hp_for_onedrive_and_hp_for_onedrive_business_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

         # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("App Deployment")

    # HP for Universal Print, HP Mail Flow apps
    def test_08_verify_hp_for_universal_print_and_hp_mail_flow_app_settings_in_device_specific_policy_tab(self):
        self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_details_policy_widget_expand_button()
        sleep(5)
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("App Deployment")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()

        # Add the policy in Device Specific Policy tab
        self.endpoint_security.add_hp_for_universal_print_and_hp_mail_flow_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()

         # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("App Deployment")

    # HP for Dropbox, Lite Survey, LRS Authenticator
    def test_09_verify_hp_for_dropbox_lite_survey_and_lrs_authenticator_app_settings_in_device_specific_policy_tab(self):
        # self.devices.verify_device_page()
        self.devices.search_device(app_deployment_serial_num)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_details_policy_widget_expand_button()
        sleep(5)
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("App Deployment")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()

        # Add the policy in Device Specific Policy tab
        self.endpoint_security.add_hp_for_dropbox_lite_survey_and_lrs_authenticator_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()
        self.devices.dismiss_toast()

         # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Uninstall the apps from Device Specific Policy tab
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_next_button()
        sleep(5)  # Wait for UI to load
        self.endpoint_security.uninstal_added_app_in_app_deployment_settings(modify_setting="app-deployment")
        self.devices.click_device_specific_policy_create_button()
        self.devices.click_change_not_recommended_popup_confirm_button()    

         # verify the compliance of that device after the device specific policy is applied.
        self.endpoint_security.verify_policies_compliance_status_for_app_deployment_setting(app_deployment_serial_num)

        # Remove the device specific policy
        self.devices.remove_settings_in_device_specific_policy_tab("App Deployment")