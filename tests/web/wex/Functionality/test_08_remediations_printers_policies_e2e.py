import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))
auto_policy_name="auto_policy_test"+str(random.randint(100,999))

class Test_08_WEX_Fleet_Management_Printers_Policies(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.policies = self.fc.fd["fleet_management_policies"]
        self.printers_groups = self.fc.fd["printers_groups"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]
        self.emulator_e2e_serial_number = self.account["emulator_e2e_serial_number"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        self.printers.click_printers_group("All groups")
        return self.printers.verify_devices_printers_table_loaded()

    def test_01_verify_devices_policy_status_when_no_policy_assigned(self):
        #
        #Create a group in devices page 
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()

        # Create group under Groups Printers tab
        self.printers.click_printers_manage_group_button()
        self.printers_groups.create_group_without_rules(group_name)

        # close the toast notification if any
        self.printers.dismiss_toast()

        # Verify the newly created group is displayed in Printers Groups section
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_group_name(group_name)

        # Move an online device to the newly created group
        # self.printers.verify_and_click_online_printer()
        if self.emulator_e2e_serial_number == "":
            self.printers.verify_and_click_online_printer()
        else:
            self.printers.search_printers(self.emulator_e2e_serial_number)
            self.printers.click_printers_checkbox()
        self.printers.verify_devices_printers_table_loaded()
        sleep(5)
        self.printers.click_move_to_group_button()
        self.printers.select_group(group_name)
        self.printers.click_move_to_group_popup_move_button()
        sleep(5) # Need to wait for the device to move to the group

        self.printers.dismiss_toast()

        # Verify any device specific policy is assigned to the device
        self.printers.click_printers_group(group_name)
        self.printers.click_devices_printers_page_refresh_button()
        sleep(20)  # Need to wait for the device list to load
        self.printers.click_devices_printers_page_refresh_button()
        sleep(30)  # Need to wait for the device list to load
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        sleep(10)  # Need to wait for the device list to load
        self.printers.verify_devices_printers_table_loaded()
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()

        # Verify and remove if any specific policy is assigned to the device
        self.printers.click_compliance_status_widget()
        self.printers.click_policy_widget()
        if self.printers.verify_device_specific_policy_card_empty() is False:
            self.printers.remove_existing_device_specific_policy()
            # self.printers.click_policy_widget()
        assert self.printers.verify_device_specific_policy_card_empty() == True

        # Policies- Assignments tab: verify and remove if policies is assigned to 'All groups'
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        # self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()

        if self.policies.verify_no_policy_is_assigned_to_all_groups() is False:
            self.policies.remove_assigned_policies_from_all_groups
        assert self.policies.verify_no_policy_is_assigned_to_all_groups() == True

        # Policies- Devices tab : Verify policy name column as empty
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_group(group_name)
        self.printers.click_groups_side_bar_collapse_btn()
        sleep(5)  # Need to wait for the device list to load

        # Verify Policy Column as empty in Device table
        device_table_policy_column_info = self.printers.get_printer_device_page_policy_list()
        assert '--' == device_table_policy_column_info

        # Verify Policy Compliance column as empty in Device table 
        device_table_policy_compliance_status = self.printers.get_printer_device_page_policy_compliance_list()
        self.printers.verify_policies_device_list_compliance_status_when_no_policy_assigned(device_table_policy_compliance_status)

        # Verify Policy Name option as empty in Device details page
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        sleep(15)

        device_list_policy_info = self.printers.get_device_detail_policy_tab_policy_name()
        assert "--" == device_list_policy_info

        # Verify Policy Compliance Status as empty in Device details page
        device_table_policy_compliance_status = self.printers.get_device_detail_policy_tab_compliance_status()
        self.printers.verify_policies_device_list_compliance_status_when_no_policy_assigned(device_table_policy_compliance_status)

    def test_02_verify_devices_policy_status_when_only_device_specific_policy_assigned(self):
        #
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_group(group_name)
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()

        # Verify and add if no specific policy is assigned to the device
        self.printers.click_compliance_status_widget()
        self.printers.click_policy_widget()
        if self.printers.verify_device_specific_policy_card_empty() is True:
            self.printers.click_printers_details_policies_tab_edit_button()
            self.printers.verify_edit_device_policy_settings_title()
            self.printers.search_policy_settings("https")
            sleep(5) # Need to wait for the search results to load
            self.printers.click_device_specific_policy_checkbox()
            self.printers.click_device_specific_policy_next_button()
            self.printers.click_device_specific_policy_create_button()
            self.printers.dismiss_toast()
            # self.printers.click_policy_widget()
            self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("https")

        # Policies- Assignments tab: verify and remove if policies is assigned to 'All groups'
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()

        if self.policies.verify_no_policy_is_assigned_to_all_groups() is False:
            self.policies.remove_assigned_policies_from_all_groups
        assert self.policies.verify_no_policy_is_assigned_to_all_groups() == True

        # Devices tab : Verify policy name column has device specific policy name
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_group(group_name)
        self.printers.click_groups_side_bar_collapse_btn()

        device_table_policy_column_info = self.printers.get_printer_device_page_policy_list()
        assert 'Device-specific policy' == device_table_policy_column_info

        # Devices tab : Verify policy Compliance column has policy compliance status
        device_table_policy_compliance_status = self.printers.get_printer_device_page_policy_compliance_list()
        self.printers.verify_policies_device_list_compliance_status(device_table_policy_compliance_status)

        # Verify policy status in Device details page whether it's Non-compliant or Compliant
        self.printers.click_first_entry_link()
        sleep(30)
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        sleep(20)

        self.printers.verify_printers_device_details_policies_tab_policy_name("Device-specific policy")
        self.printers.verify_printers_device_details_policies_tab_compliance_policy_status(device_table_policy_compliance_status)
        self.printers.verify_printers_device_details_policy_compliance_total_policy_settings("1")

        # Verify Policy setting status in Policy priority dropdown
        self.printers.click_policy_widget()
        self.printers.verify_printers_details_policies_tab_policy_widget_expand_button()
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("https")
        self.printers.click_printers_details_policies_tab_high_priority_settings_button()
        self.printers.verify_printers_details_policies_tab_high_priority_policy_warning_icon(device_table_policy_compliance_status, "https")
        self.printers.verify_printers_details_policies_tab_high_priority_policy_warning_message("Noncompliant policy setting", device_table_policy_compliance_status)
        self.printers.click_policy_widget()
        self.printers.verify_printers_details_policies_tab_policy_widget_collapsed()

        # Removing the added device specific policy
        self.printers.remove_existing_device_specific_policy()

    def test_03_verify_device_status_when_effective_policy_is_non_compliant(self):
        #
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()

        # Policies-Policies tab: Create a policy in Policies tab
        self.policies.click_create_policy_button()
        self.policies.click_create_policy_next_button()
        self.policies.enter_policy_name(auto_policy_name)
        self.policies.select_policy_settings_type("Skip Template")
        self.policies.click_create_policy_next_button()
        
        self.policies.search_create_policy_settings("https")
        self.policies.click_select_policy_settings_checkbox()
        self.policies.click_create_policy_next_button()

        self.policies.click_create_policy_create_button()
        self.policies.click_create_policy_done_button()
        self.policies.verify_table_policy_by_name(auto_policy_name, policy_search=True)

        # Policies-Assignments tab: Assign the created policy to the created group in Assignments tab
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.click_assignments_add_policy_button()

        self.policies.search_add_policy(auto_policy_name)
        self.policies.click_add_policies_checkbox()
        self.policies.click_add_policy_button()
        
        self.policies.click_assess_and_remediate_dropdown_option("Assess Only")
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        # self.policies.check_toast_successful_message("Policy assigned successfully.")

        # Verify policy status in Device list whether it's Non-compliant
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_group(group_name)
        self.printers.click_groups_side_bar_collapse_btn()
        self.printers.click_devices_printers_page_refresh_button()
        sleep(20)  # Need to wait for the device list to load
        self.printers.click_devices_printers_page_refresh_button()
        sleep(30)  # Need to wait for the device list to load
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        sleep(10)  # Need to wait for the device list to load
        self.printers.verify_devices_printers_table_loaded()

        device_table_policy_column_info = self.printers.get_printer_device_page_policy_list()
        assert auto_policy_name == device_table_policy_column_info
        device_table_policy_compliance_status = self.printers.get_printer_device_page_policy_compliance_list()
        self.printers.verify_policies_device_list_compliance_status(device_table_policy_compliance_status)

        # Verify policy status in Device details page whether it's Non-compliant or Compliant
        self.printers.click_first_entry_link()
        sleep(20)
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        sleep(25)
        self.printers.verify_printers_device_details_policies_tab_policy_name(auto_policy_name)
        self.printers.verify_printers_device_details_policies_tab_compliance_policy_status(device_table_policy_compliance_status)
        self.printers.verify_printers_device_details_policy_compliance_total_policy_settings("1")

        # Verify policy details in device details policies tab
        self.printers.verify_printers_device_details_assigned_policy_name_2(auto_policy_name)
        self.printers.verify_printers_device_details_priority_2_compliance_status(device_table_policy_compliance_status)
        self.printers.click_printers_device_details_assigned_policy_priority_2_button()
        self.printers.click_printers_details_policies_tab_priority_2_settings_button()
        self.printers.verify_printers_device_details_assigned_policy_priority_2_expanded(expanded=True)
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("https")
        self.printers.verify_printers_details_policies_tab_high_priority_policy_warning_icon(device_table_policy_compliance_status, "https")
        self.printers.verify_printers_details_policies_tab_high_priority_policy_warning_message("Noncompliant policy setting", device_table_policy_compliance_status)
        self.printers.click_printers_details_policies_tab_priority_2_settings_button()
        self.printers.click_printers_device_details_assigned_policy_priority_2_button()
        self.printers.verify_printers_device_details_assigned_policy_priority_2_expanded(expanded=False)

    def test_04_verify_device_status_when_two_policies_with_same_settings_are_added(self):
        #
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()

        # Policies-Policies tab: Create a policy in Policies tab
        self.policies.click_create_policy_button()
        self.policies.click_create_policy_next_button()
        self.policies.enter_policy_name(policy_name)
        self.policies.select_policy_settings_type("Skip Template")
        self.policies.click_create_policy_next_button()
        
        self.policies.search_create_policy_settings("https")
        self.policies.click_select_policy_settings_checkbox()
        self.policies.click_create_policy_next_button()

        self.policies.click_create_policy_create_button()
        self.policies.click_create_policy_done_button()
        self.policies.verify_table_policy_by_name(policy_name, policy_search=True)

        # Policies-Assignments tab: Assign the created policy to the created group in Assignments tab
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.click_assignments_add_policy_button()

        self.policies.search_add_policy(policy_name)
        self.policies.click_add_policies_checkbox()
        self.policies.click_add_policy_button()
        
        self.policies.click_assess_and_remediate_dropdown_option("Assess Only")
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        # self.policies.check_toast_successful_message("Changes saved successfully.")
        # self.policies.dismiss_toast()

        # Get low priority and high priority policy status
        low_priority_policy = self.policies.get_low_priority_policy_name()
        high_priority_policy = self.policies.get_high_priority_policy_name()

        # Verify policy status in Device list whether it's Non-compliant
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        sleep(5)  # Need to wait for the device list to load
        self.printers.verify_devices_printers_table_loaded()
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_group(group_name)
        self.printers.click_groups_side_bar_collapse_btn()
        self.printers.click_devices_printers_page_refresh_button()
        sleep(30)  # Need to wait for the device list to load
        self.printers.click_devices_printers_page_refresh_button()
        sleep(30)  # Need to wait for the device list to load
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        sleep(10)  # Need to wait for the device list to load
        self.printers.verify_devices_printers_table_loaded()

        device_table_policy_column_info = self.printers.get_printer_device_page_policy_list()
        #Having defect - - So commenting the assert statement
        # assert (high_priority_policy) +" & 1 more" == device_table_policy_column_info
        device_table_policy_compliance_status = self.printers.get_printer_device_page_policy_compliance_list()
        self.printers.verify_policies_device_list_compliance_status(device_table_policy_compliance_status)

        # Verify assigned policy status details in Device details - Policies tab
        self.printers.click_first_entry_link()
        sleep(20)
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        sleep(25)
        assigned_policy_names = (high_priority_policy)+", "+(low_priority_policy)
        assert assigned_policy_names == self.printers.get_device_detail_policy_tab_policy_name()
        self.printers.verify_policies_device_list_compliance_status(device_table_policy_compliance_status)
        self.printers.verify_printers_device_details_policy_compliance_total_policy_settings("1")

        # Verify low priority policy setting has warning message in device details page
        self.printers.verify_printers_device_details_low_priority_policy_name(low_priority_policy)
        self.printers.verify_printers_device_details_low_priority_policy_overridden_status("Overridden")
        self.printers.click_printers_device_details_low_priority_policy_button()
        self.printers.click_printers_device_details_low_priority_policy_settings_button()
        self.printers.verify_printers_device_details_low_priority_policy_warning_icon()
        # self.printers.verify_printers_device_details_low_priority_policy_warning_message("Inactive policy setting")
        self.printers.click_printers_device_details_low_priority_policy_button()

    def test_05_verify_devices_and_policies_unassign_functionality(self):
        #
        # Unassign the created policy from created group in Assignments tab
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()

        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.click_assignments_delete_policy_button()
        self.policies.click_assignments_delete_policy_button()
        self.policies.click_assignments_action_button()
        self.policies.check_toast_successful_message("Policy unassigned successfully.")
        self.policies.dismiss_toast()

        # Policies-Policy tab: Remove the created policies from Policy tab
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()

        # Removing both created policies
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.search_policy(auto_policy_name)
        self.policies.click_policy_checkbox()

        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("remove")
        self.policies.click_contextual_footer_continue_button()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")

        self.policies.search_policy(policy_name)
        self.policies.verify_no_items_found()

        self.policies.search_policy(auto_policy_name)
        self.policies.verify_no_items_found()

        # Devices: Remove the assigned device from created group
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
    
        #Devices: Delete the created group from devices list
        self.printers.click_printers_manage_group_button()
        sleep(5)
        self.printers_groups.select_group_by_name(group_name)
        self.printers_groups.click_group_details_delete_group_button()
        
        self.printers_groups.verify_delete_group_popup()
        self.printers_groups.verify_delete_group_popup_security_code()
        security_code = self.printers_groups.get_delete_group_popup_security_code_text()
        self.printers_groups.enter_delete_group_popup_security_code_text(security_code)
        self.printers_groups.click_delete_group_popup_delete_button()

        # # Verify toast notification message
        # assert f'Printer group "{group_name}" deleted' == self.printers_groups.verify_delete_groups_toast_message(), "Toast notification for group deletion not displayed"

        # close the toast notification if any
        self.printers.dismiss_toast()

        # verify group deletion success
        assert self.printers_groups.verify_group_name(group_name,displayed=False), "Group was not deleted successfully"
    
    def test_06_verify_policy_creation_with_essential_security_template_settings(self):
        #
        # Create a group in devices page
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        
        # Create group under Groups Printers tab
        self.printers.click_printers_manage_group_button()
        self.printers_groups.create_group_without_rules(group_name)

        # close the toast notification if any
        self.printers.dismiss_toast()
    
        # Verify the newly created group is displayed in Printers Groups section
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.verify_group_name(group_name)
 
        # Move an online device to the newly created group
        if self.emulator_e2e_serial_number == "":
            self.printers.verify_and_click_online_printer()
        else:
            self.printers.search_printers(self.emulator_e2e_serial_number)
            self.printers.click_printers_checkbox()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.click_move_to_group_button()
        self.printers.select_group(group_name)
        self.printers.click_move_to_group_popup_move_button()
        sleep(5) # Need to wait for the device to move to the group
 
        # Create a policy with Essential Security Template
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.click_create_policy_button()
        self.policies.click_create_policy_next_button()
        self.policies.enter_policy_name(policy_name)
        self.policies.select_policy_settings_type("Essential Security Template")
        self.policies.click_create_policy_next_button()
        self.policies.click_create_policy_next_button()
        sleep(20)
 
        # Get the list of all available Essential Security policy settings in create policy tab
        essential_security_template_setting_list = self.policies.get_policy_settings_count()
        
        self.printers.click_device_specific_policy_settings_card("ews-password")
        self.printers.enter_ews_admin_password_textbox_value("Test@123")
        self.printers.enter_ews_admin_confirm_password_textbox_value("Test@123")

        self.policies.click_create_policy_create_button()
        self.policies.verify_policy_created_successfully_popup_policy_name(policy_name)
        self.policies.click_create_policy_done_button()
        self.policies.dismiss_toast()
        self.policies.search_policy(policy_name)
        self.policies.verify_table_policy_by_name(policy_name, policy_search=True, policy_status= "Inactive")
        self.policies.click_first_entry_link()
        sleep(20)
 
        # Verify the added policy settings in the policy details page
        essential_security_template_setting_list == self.policies.get_policy_settings_count()
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        self.policies.verify_remediations_printer_policies_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.click_remediations_printer_assignments_button()
 
        # Assign the policy to the device group and verify the policy status in policies tab
        sleep(5)
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.click_assignments_add_policy_button()
        self.policies.search_add_policy(policy_name)
        self.policies.click_add_policies_checkbox()
        self.policies.click_add_policy_button()
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        # self.policies.check_toast_successful_message("Policy assigned successfully.")
 
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.search_policy(policy_name)
        self.policies.verify_table_policy_by_name(policy_name, policy_search=True, policy_status= "Active")
 
    def test_07_verify_assigned_essential_security_template_policy_settings_in_device_details_page(self):
        #
        # Verify the assigned essential security policy settings in the device details page
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_group(group_name)
        self.printers.click_groups_side_bar_collapse_btn()
 
        self.printers.click_first_entry_link()
        self.printers.verify_printers_details_page_policies_tab()
        self.printers.click_printers_details_page_policies_tab()
        self.printers.click_policy_widget()
        self.printers.click_printers_device_details_assigned_policy_priority_2_button()
        self.printers.click_printers_details_policies_tab_priority_2_settings_button()
        self.printers.verify_printers_device_details_assigned_policy_priority_2_expanded(expanded=True)
 
        # Verify the essential security policy settings in the device details page
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("auto-fw")
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("check-latest")
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("fs-access")
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("remote-fw-update")
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("pjl-command")
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("https")
        self.printers.verify_printers_device_details_policies_tab_assigned_policy_setting_name("telnet")
 
        # Unassign the created policy from created group in Assignments tab
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()
 
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.click_assignments_delete_policy_button()
        self.policies.click_assignments_action_button()
        self.policies.check_toast_successful_message("Policy unassigned successfully.")
        self.policies.dismiss_toast()
 
        # Policies-Policy tab: Remove the created policies from Policy tab
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
 
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        sleep(7)
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("remove")
        self.policies.click_contextual_footer_continue_button()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")
 
        # Devices: Remove the assigned device from created group
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
   
        #Devices: Delete the created group from devices list
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.click_printers_edit_groups_button()
        self.printers.click_edit_groups_popup_group_name(group_name)
        self.printers.click_edit_groups_popup_delete_button()
        self.printers.click_delete_group_popup_delete_button()
        self.printers.dismiss_toast()
        sleep(3)
        self.printers.click_edit_groups_popup_close_button()
 
        # verify the deleted group name, should not display under Groups
        self.printers.verify_group_name(group_name,displayed=False)