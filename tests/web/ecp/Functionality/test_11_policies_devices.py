import time
import pytest
from SAF.misc import saf_misc
import random
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "ECP"

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))
test_policy_name="auto_policy_test"+str(random.randint(100,999))

#Generate test group name
group_name="auto_group"+str(random.randint(100,999))
@pytest.mark.skip
class Test_11_ECP_Policies_Devices(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.devices = self.fc.fd["devices"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        self.customer = self.account["customer"]
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_policies_devices(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.click_devices_group_all_option("All")
        return self.devices.verify_device_page()
        # Commenting because policy devices has been removed from the UI 
        # self.home.click_policies_menu_btn()
        # self.endpoint_security.click_policies_devices_tab()

    def test_01_verify_devices_policy_status_when_no_policy_assigned(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274733
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274749

        #Create a group in devices page 
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.devices.click_devices_create_group_button()
        self.devices.enter_group_name(group_name)
        # self.devices.select_parent_group() # Commenting as it's removed from the UI
        self.devices.click_create_group_popup_create_button()
        
        # Verify the newly created group is displayed in Groups section
        self.devices.verify_group_name(group_name)
        
        # Close the toast notification if any
        self.devices.dismiss_toast()
        time.sleep(5)
        
        #Move an online device to the newly created group
        # self.devices.search_online_device("HP ")
        self.devices.verify_and_click_online_printer()
        # self.devices.click_devices_checkbox()
        self.devices.click_contextual_footer_select_action_dropdown()
        self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
        self.devices.click_contextual_footer_continue_button()
        self.devices.select_group(group_name)
        self.devices.click_move_to_group_popup_move_button()

        #Verify any device specific policy is assigned to the device
        self.devices.click_devices_group(group_name)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()

        #Verify and remove if any specific policy is assigned to the device
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.remove_existing_device_specific_policy()
        
        assert self.devices.device_specific_policy_card_empty() == True

        #Policies- Assignments tab: verify and remove if policies is assigned to 'All groups'
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        time.sleep(5) #Adding time to load the page

        if self.endpoint_security.verify_no_policy_is_assigned_to_all_groups() is False:
            self.endpoint_security.remove_assigned_policies_from_all_groups()

        assert self.endpoint_security.verify_no_policy_is_assigned_to_all_groups() == True

        #Policies- Devices tab : Verify policy name column as empty
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        # self.endpoint_security.click_policies_devices_tab()
        # self.endpoint_security.verify_policies_devices_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_policies_column_options_gear_button()
        
        # Selecting Polices, Polices Compliance, Policy Last Run to check status
        self.endpoint_security.select_polices_column_option()
        self.endpoint_security.select_polices_compliance_option()
        self.endpoint_security.select_polices_last_run_option()
        self.endpoint_security.click_column_options_popup_save_button()
        self.devices.click_group_side_bar_collapse_btn()
        device_list_policy_info = self.endpoint_security.get_device_page_policy_list()
        assert "--" == device_list_policy_info

        device_list_compliance_status =  self.endpoint_security.get_device_page_compliance_status()
        self.endpoint_security.verify_policies_device_list_compliance_status_when_no_policy_assigned(device_list_compliance_status)
                
        #Verify policy name column as empty in Device details page
        self.endpoint_security.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        device_list_policy_info = self.endpoint_security.get_device_detail_policy_tab_policy_name()
        
        assert "--" == device_list_policy_info
        device_list_compliance_status = self.endpoint_security.get_device_detail_policy_tab_compliance_status()
        self.endpoint_security.verify_policies_device_list_compliance_status_when_no_policy_assigned(device_list_compliance_status)

        # Revertig the column options to default options
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.endpoint_security.reverting_to_default_column_options()
        # self.endpoint_security.verify_policies_device_details_compliance_policy_status(device_list_compliance_status)
        # self.endpoint_security.verify_compliance_status_empty_in_policies_devices_details_page()
    
    def test_02_verify_devices_policy_status_when_only_device_specific_policy_assigned(self):
        #
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()

        #Verify any device specific policy is assigned to the device
        self.devices.click_devices_group(group_name)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
    
        #Verify and add if no specific policy is assigned to the device
        if self.devices.device_specific_policy_card_empty() is True:
            self.devices.click_device_specific_policy_edit_button()
            self.devices.verify_edit_device_policy_settings_title()
            self.devices.search_policy_settings("https")
            self.devices.click_device_specific_policy_checkbox()
            self.devices.click_device_specific_policy_next_button()
            self.devices.click_device_specific_policy_create_button()
            #self.devices.check_bottom_toast_policy_create_success_msg("Device-Specific Policy has been created successfully.")
            self.endpoint_security.dismiss_toast_successful_message()
            self.devices.click_device_details_policy_widget_expand_button()
            self.devices.verify_device_specific_policy_setting_added("https")

        #Policies- Assignments tab: verify and remove if policies is assigned to 'All groups'
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        time.sleep(5)

        if self.endpoint_security.verify_no_policy_is_assigned_to_all_groups() is False:
            self.endpoint_security.remove_assigned_policies_from_all_groups()

        assert self.endpoint_security.verify_no_policy_is_assigned_to_all_groups() == True

        #Policies- Devices tab : Verify policy name column has device specific policy
        # self.endpoint_security.click_policies_devices_tab()
        # self.endpoint_security.verify_policies_devices_page()
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.select_polices_column_option()
        self.endpoint_security.select_polices_compliance_option()
        self.endpoint_security.select_polices_last_run_option()
        self.endpoint_security.click_column_options_popup_save_button()
        self.devices.click_group_side_bar_collapse_btn()

        device_list_policy_info = self.endpoint_security.get_device_page_policy_list()
        assert "Device-specific policy" == device_list_policy_info
        device_list_compliance_status =  self.endpoint_security.get_device_page_compliance_status()
        self.endpoint_security.verify_policies_device_list_compliance_status(device_list_compliance_status)

        #Verify policy status in Device details page whether it's Non-compliant or Compliant
        self.endpoint_security.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.endpoint_security.verify_policies_device_details_policy_name("Device-specific policy")
        self.endpoint_security.verify_policies_device_details_compliance_policy_status(device_list_compliance_status)
        # self.endpoint_security.verify_policies_device_details_compliance_total_policy_settings("1")
        
        #Verify Policy setting status in Policy priority dropdown
        self.endpoint_security.verify_policies_device_details_assigned_policy_priority_1_expanded()
        self.endpoint_security.click_policies_device_details_assigned_policy_priority_1_expanded()
        self.endpoint_security.verify_policies_device_details_assigned_policy_setting_name("https")
        self.endpoint_security.click_policies_device_details_high_priority_policy_settings_button()
        self.endpoint_security.verify_policies_device_details_high_priority_policy_warning_icon(device_list_compliance_status,"https")
        self.endpoint_security.verify_policies_device_details_high_priority_policy_warning_message("Noncompliant policy setting",device_list_compliance_status)
        self.endpoint_security.click_device_details_policy_tab_policy_widget()
        self.endpoint_security.verify_policies_device_details_collapsed()

        #removing the added device specific policy 
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        # Revertig the column options to default options
        self.endpoint_security.reverting_to_default_column_options()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.devices.click_devices_group(group_name)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policy_widget_expand_button()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()
        self.devices.click_device_specific_policy_remove_button()
        self.endpoint_security.check_toast_successful_msg("Device-Specific Policy has been removed.")
        self.devices.click_device_details_policy_widget_expand_button()
        assert self.devices.device_specific_policy_card_empty() == True

    def test_03_verify_device_status_when_effective_policy_is_non_compliant(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274731

        #Policies-Policies tab: Create a policy in Policies tab
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.click_create_policy_button()

        self.endpoint_security.enter_policy_name(test_policy_name)
        self.endpoint_security.select_policy_settings_type("Skip Template")
        self.endpoint_security.click_create_policy_next_button()
        
        self.endpoint_security.search_create_policy_settings("https")
        self.endpoint_security.click_select_policy_settings_checkbox()
        self.endpoint_security.click_create_policy_next_button()

        self.endpoint_security.click_create_policy_create_button()
        self.endpoint_security.click_create_policy_done_button()
        self.endpoint_security.verify_table_policy_by_name(test_policy_name, policy_search=True)

        #Policies-Assignments tab:Assign the created policy to the created group in Assignments tab
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_assignments_add_policy_button()

        self.endpoint_security.search_add_policy(test_policy_name)
        self.endpoint_security.click_add_policies_checkbox()
        self.endpoint_security.click_add_policy_button()
        
        self.endpoint_security.click_assess_and_remediate_dropdown_option("Assess Only")
        self.endpoint_security.click_assignments_action_button()
        self.endpoint_security.dismiss_toast_successful_message()
        #self.endpoint_security.check_toast_successful_message("Policy assigned successfully.")

        #Verify policy status in Device list whether it's Non-compliant
        # self.endpoint_security.click_policies_devices_tab()
        # self.endpoint_security.verify_policies_devices_page()
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.select_polices_column_option()
        self.endpoint_security.select_polices_compliance_option()
        self.endpoint_security.select_polices_last_run_option()
        self.endpoint_security.click_column_options_popup_save_button()
        self.devices.click_group_side_bar_collapse_btn()
        
        device_list_policy_info = self.endpoint_security.get_device_page_policy_list()
        assert test_policy_name == device_list_policy_info
        device_list_compliance_status =  self.endpoint_security.get_device_page_compliance_status()
        self.endpoint_security.verify_policies_device_list_compliance_status(device_list_compliance_status)

        ##verify policy status in Device details page whether it's Non-compliant
        self.endpoint_security.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.endpoint_security.verify_policies_device_details_policy_name(test_policy_name)
        self.endpoint_security.verify_policies_device_details_compliance_policy_status(device_list_compliance_status)
        # self.endpoint_security.verify_policies_device_details_compliance_total_policy_settings("1")

        # #Verify non-compliant policy details in device details page
        self.endpoint_security.verify_policies_device_details_assigned_policy_name(test_policy_name)
        self.endpoint_security.verify_policies_device_details_assigned_policy_compliance_status(device_list_compliance_status)
        self.endpoint_security.click_policies_device_details_assigned_policy_priority_button()
        self.endpoint_security.verify_policies_device_details_assigned_policy_priority_2_expanded()
        self.endpoint_security.verify_policies_device_details_assigned_policy_setting_name("https")
        self.endpoint_security.click_policies_device_details_high_priority_policy_settings_button()
        self.endpoint_security.verify_policies_device_details_high_priority_policy_warning_icon(device_list_compliance_status,"https")
        self.endpoint_security.verify_policies_device_details_high_priority_policy_warning_message("Noncompliant policy setting",device_list_compliance_status)
        self.endpoint_security.click_policies_device_details_assigned_policy_priority_button()
        self.endpoint_security.verify_policies_device_details_assigned_policy_priority_2_expanded(expanded=False)

        # Revertig the column options to default options
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.endpoint_security.reverting_to_default_column_options()

    def test_04_verify_device_status_when_two_policies_with_same_settings_are_added(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274732

        #Policies-Policies tab: Create another policy in Policies tab
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.click_create_policy_button()

        self.endpoint_security.enter_policy_name(policy_name)
        self.endpoint_security.select_policy_settings_type("Skip Template")
        self.endpoint_security.click_create_policy_next_button()
        
        self.endpoint_security.search_create_policy_settings("https")
        self.endpoint_security.click_select_policy_settings_checkbox()
        self.endpoint_security.click_create_policy_next_button()

        self.endpoint_security.click_create_policy_create_button()
        self.endpoint_security.click_create_policy_done_button()
        self.endpoint_security.verify_table_policy_by_name(policy_name, policy_search=True)

        #Policies-Assignments tab:Assign the created policy to the created group in Assignments tab
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_assignments_add_policy_button()

        self.endpoint_security.search_add_policy(policy_name)
        self.endpoint_security.click_add_policies_checkbox()
        self.endpoint_security.click_add_policy_button()
        
        self.endpoint_security.click_assess_and_remediate_dropdown_option("Assess Only")
        self.endpoint_security.click_assignments_action_button()
        self.endpoint_security.dismiss_toast_successful_message()
        #self.endpoint_security.check_toast_successful_message("Changes saved successfully.")

        #get low priority and high priority policy status
        low_priority_policy = self.endpoint_security.get_low_priority_policy_name()
        high_priority_policy = self.endpoint_security.get_high_priority_policy_name()

        #Verify policy status in Device list whether it's Non-compliant
        # self.endpoint_security.click_policies_devices_tab()
        # self.endpoint_security.verify_policies_devices_page()
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.select_polices_column_option()
        self.endpoint_security.select_polices_compliance_option()
        self.endpoint_security.select_polices_last_run_option()
        self.endpoint_security.click_column_options_popup_save_button()
        
        device_list_policy_info = self.endpoint_security.get_device_page_policy_list()
        assert (high_priority_policy) +" & 1 more" == device_list_policy_info
        device_list_compliance_status =  self.endpoint_security.get_policies_device_list_compliance_status()
        self.endpoint_security.verify_policies_device_list_compliance_status(device_list_compliance_status)

        #Verify assigned policy status details in Device details page 
        self.endpoint_security.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        assigned_policy_names = (high_priority_policy)+", "+(low_priority_policy)
        assert assigned_policy_names ==  self.endpoint_security.get_policies_device_details_policy_names()
        self.endpoint_security.verify_policies_device_details_compliance_policy_status(device_list_compliance_status)
        # self.endpoint_security.verify_policies_device_details_compliance_total_policy_settings("1")

        #Verify low priority policy setting has warning message in device details page
        self.endpoint_security.verify_policies_device_details_low_priority_policy_name(low_priority_policy)
        self.endpoint_security.verify_policies_device_details_low_priority_policy_overridden_status("Overridden")
        self.endpoint_security.click_policies_device_details_low_priority_policy_button()
        self.endpoint_security.click_policies_device_details_low_priority_policy_settings_button()
        self.endpoint_security.verify_policies_device_details_low_priority_policy_warning_icon()
        self.endpoint_security.verify_policies_device_details_low_priority_policy_warning_message("Inactive policy setting")
        self.endpoint_security.click_policies_device_details_low_priority_policy_button() 

    def test_05_verify_devices_and_policies_unassign_functionality(self):

        #Unassign the created policy from created group in Assignments tab
        self.home.click_policies_menu_btn()      
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_assignments_delete_policy_button()
        self.endpoint_security.click_assignments_delete_policy_button()
        self.endpoint_security.click_assignments_action_button()
        self.endpoint_security.check_toast_successful_message("Policy unassigned successfully.")
        self.endpoint_security.dismiss_toast()

        #Policies-Policy tab: Remove the created policy from Policy tab
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()

        #removing both created policies
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()

        self.endpoint_security.search_policy(test_policy_name)
        self.endpoint_security.click_policy_checkbox()

        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("remove")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_remove_policy_popup_remove_button()
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.verify_no_items_found()

        self.endpoint_security.search_policy(test_policy_name)
        self.endpoint_security.verify_no_items_found()
    
        #Devices: Remove the assigned device from created group       
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
    
        #Devices: Delete the created group from devices list
        self.devices.click_devices_edit_group_button()
        self.devices.select_group(group_name)
        self.devices.click_edit_group_popup_delete_button()
        self.devices.click_delete_group_popup_delete_button()
        self.devices.click_edit_group_popup_close_button()

        # verify the deleted group name, should not display under Groups
        self.devices.verify_group_name(group_name,displayed=False)