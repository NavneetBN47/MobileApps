import pytest
import random
import logging
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))

#Generate test group name
group_name="auto_group"+str(random.randint(100,999))

class Test_12_Workforce_Remediations_Policies_Assignment(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.policies = self.fc.fd["fleet_management_policies"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.printers_groups = self.fc.fd["printers_groups"]
        self.serial_number = request.config.getoption("--proxy-device")
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
            self.serial_number = self.account["ldk_printer_serial_number"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]
            self.emulator_serial_number = self.account["emulator_assignment_serial_number"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.verify_remediations_printer_assignments_tab()
        self.policies.click_remediations_printer_assignments_button()
        return self.policies.verify_fleet_management_policies_breadcrumb()
    
    @pytest.mark.sanity
    def test_01_verify_assignments_tab_ui(self):
        # 
        expected_table_headers = ["Policy Name", "Category", "Assess and Remediate"]
        assert expected_table_headers == self.policies.verify_assignments_tab_table_headers()

        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()

        self.policies.verify_groups_title()

    def test_02_verify_policies_assignment_breadcrumb_and_its_navigation(self):
        #
        # Verify the breadcrumb  on the policies page
        self.policies.verify_fleet_management_policies_breadcrumb()
 
        # Verify the policies page URL
        self.policies.verify_assignments_page_url(self.stack)

    @pytest.mark.sanity
    def test_03_verify_groups_side_bar_expand_collapse_functionality(self):
        # 
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.verify_groups_side_bar_collapse_btn()
        self.policies.verify_groups_title()
        
        self.policies.click_groups_side_bar_collapse_btn()
        self.policies.verify_groups_side_bar_expand_btn()
        self.policies.verify_groups_title(displayed=False)
    
    @pytest.mark.sanity
    def test_04_verify_policy_names_in_add_policy_popup(self):
        #
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.verify_table_displaying_correctly(100, page=1)  
        all_policy_names=self.policies.get_all_policy_names()

        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()        
        sleep(5)
        assert all_policy_names == self.policies.get_all_policy_names_from_add_policy_popup()

    @pytest.mark.sanity
    def test_05_verify_add_policy_popup(self):
        #
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()

        # Verify Add Policy popup
        self.policies.verify_add_policy_popup()
        self.policies.verify_add_policy_popup_title()
        self.policies.verify_add_policy_popup_description()
        self.policies.verify_add_policy_popup_search_box()
        self.policies.verify_add_policy_popup_cancel_button()
        self.policies.verify_add_policy_popup_add_button()
        self.policies.click_add_policy_popup_cancel_button()
        self.policies.verify_add_policy_popup(displayed=False)

    @pytest.mark.sanity
    def test_06_verify_add_policy_popup_add_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635170
        
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()
        # Verify Add button enabled by default when no policy is selected
        self.policies.verify_add_policy_popup_add_button_status("enabled")
        self.policies.click_add_policies_checkbox()
        self.policies.verify_add_policy_popup_add_button_status("enabled")

    def test_07_verify_devices_policy_assign_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/636150770
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960065
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961202
        
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()

        #Create a group in devices page 
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()

        self.printers.click_printers_manage_group_button()
        sleep(5)
        self.printers_groups.click_groups_printers_tab_title()
        self.printers_groups.click_groups_printers_add_group_button()

        # Enter group name and description
        self.printers_groups.enter_group_name(group_name)
        self.printers_groups.enter_group_description("Test group without rules")

        # Uncheck the 'Add group rules' checkbox if it is checked
        self.printers_groups.click_add_group_rules_checkbox()

        # Click Next to create the group
        self.printers_groups.click_add_groups_next_button()
        # # Verify toast notification message
        # assert f'Printer group {group_name} created' == self.printers_groups.verify_add_groups_toast_message(), "Toast notification for group creation not displayed"

        # close the toast notification if any
        self.printers.dismiss_toast()

        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()

        # Verify the newly created group is displayed in Groups section
        self.printers.verify_group_name(group_name)
 
        #Check for Online devices or Emulator from Printers list table
        self.printers.search_printers(self.emulator_serial_number)
        sleep(30) # Need to wait for the printer status to be updated in UI
        if self.printers.get_printer_device_page_connectivity_status() == "Online":
            printer_serial_number = self.emulator_serial_number
        else:
            printer_serial_number = self.serial_number
 
        #Move an online device to the newly created group
        self.printers.click_search_clear_button()
        self.printers.search_printers(printer_serial_number)
        self.printers.click_printers_checkbox()
        self.printers.click_move_to_group_button()
        self.printers.select_group(group_name)
        self.printers.click_move_to_group_popup_move_button()
        self.policies.dismiss_toast()

        #Policies-Policies tab: Create a policy in Policies tab
        
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.click_create_policy_button()
        self.policies.click_create_policy_next_button()

        self.policies.enter_policy_name(policy_name)
        self.policies.select_policy_settings_type("Skip Template")
        self.policies.click_create_policy_next_button()
        
        self.policies.search_create_policy_settings("Device Name")
        self.policies.click_select_policy_settings_checkbox()
        self.policies.click_create_policy_next_button()

        self.policies.click_create_policy_create_button()
        self.policies.click_create_policy_done_button()
        self.policies.verify_table_policy_by_name(policy_name, policy_search=True)

        #Policies-Policies tab: Save created policy status
        unassigned_policy_status = self.policies.get_policy_status() 

        #Policies-Assignments tab:Assign the created policy to the created group in Assignments tab
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_assignments_button()
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()

        self.policies.search_add_policy(policy_name)
        self.policies.click_add_policies_checkbox()
        self.policies.click_add_policy_button()
        
        self.policies.click_assess_and_remediate_dropdown_option("Assess Only")
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        # self.policies.check_toast_successful_message("Policy assigned successfully.")

        #Policies-Policies tab: Check Policy status after assignment to devices
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.search_policy(policy_name)

        assert unassigned_policy_status != self.policies.get_policy_status() 
        assert group_name == self.policies.get_policies_assigned_group_name()

    def test_08_verify_assignments_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960061
        
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()
        self.policies.click_add_policies_checkbox()
        self.policies.click_add_policy_button()
        # self.policies.verify_assignments_contextual_footer()
        self.policies.verify_assignments_contextual_footer_cancel_button()
        self.policies.verify_assignments_contextual_footer_action_button()
        self.policies.click_assignments_contextual_footer_cancel_button()
        self.policies.verify_assignments_contextual_footer_is_not_displayed()
    
    def test_09_verify_policy_name_hyperlink(self):
        # 
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)

        #verify policy preview page
        self.policies.select_assignments_policy_name()
        assert policy_name == self.policies.get_assignments_policy_preview_name()
        self.policies.verify_assignments_policy_settings_title()
        self.policies.click_assignments_policy_setting_card()
        self.policies.verify_assignments_policy_settings_card(expanded=True)
        self.policies.click_assignments_policy_preview_close_button()
    
    def test_10_verify_change_policy_priority_popup_ui(self):
        #        
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()
        self.policies.search_add_policy("Do Not Delete")
        sleep(5) # Need to wait for the policy to load
        self.policies.click_add_policies_checkbox()
        self.policies.click_add_policy_button()
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        sleep(5)
        self.policies.click_change_policy_priority_button()

        # Verify Change Priority Policy Popup
        self.policies.verify_change_policy_priority_popup()
        self.policies.verify_change_policy_priority_popup_title()
        self.policies.verify_change_policy_priority_popup_description()
        self.policies.verify_change_policy_priority_popup_reset_button()
        self.policies.verify_change_policy_priority_popup_cancel_button()
        self.policies.verify_change_policy_priority_popup_save_button()
        self.policies.verify_change_policy_priority_popup_up_arrow_button()
        self.policies.verify_change_policy_priority_popup_down_arrow_button()
        self.policies.click_change_policy_priority_cancel_button()
        self.policies.verify_change_policy_priority_popup(displayed=False)
        
    def test_11_verify_change_policy_priority_functionality(self):
        # 
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        initial_priority_order=self.policies.get_policy_priority()
        sleep(5)
        self.policies.click_change_policy_priority_button()

        # Change policy priority
        self.policies.click_change_policy_priority_checkbox()
        self.policies.click_change_policy_priority_down_arrow()
        self.policies.click_change_policy_priority_save_button()
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        changed_priority_order=self.policies.get_policy_priority()
        changed_priority_order.reverse()
        assert initial_priority_order == changed_priority_order

        # Reverting the changes
        sleep(5)
        self.policies.click_change_policy_priority_button()
        self.policies.click_change_policy_priority_checkbox(1)
        self.policies.click_change_policy_priority_up_arrow()
        self.policies.click_change_policy_priority_save_button()
        self.policies.dismiss_toast()
        self.policies.click_assignments_action_button()
        assert initial_priority_order == self.policies.get_policy_priority()

    def test_12_verify_change_policy_priority_popup_cancel_button_functionality(self):
        #
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        initial_priority_order=self.policies.get_policy_priority()
        self.policies.click_change_policy_priority_button()

        # Change policy priority and click on cancel button
        self.policies.click_change_policy_priority_checkbox()
        self.policies.click_change_policy_priority_down_arrow()
        self.policies.click_change_policy_priority_cancel_button()
        assert initial_priority_order == self.policies.get_policy_priority()
    
    def test_13_verify_add_policy_popup_cancel_button_functionality(self):
        #
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        initial_priority_order=self.policies.get_policy_priority()
        self.policies.verify_assignments_add_policy_button()
        self.policies.click_assignments_add_policy_button()
        self.policies.click_add_policies_checkbox()

        # Select policy in add policy popup and click on cancel button
        self.policies.click_add_policy_popup_cancel_button()
        assert initial_priority_order == self.policies.get_policy_priority()
    
    def test_14_verify_devices_policy_unassign_functionality(self):
        #
        #Unassign the created policy from created group in Assignments tab
        if self.policies.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.policies.click_groups_side_bar_expand_btn()
        self.policies.select_group(group_name)
        self.policies.click_assignments_delete_policy_button()
        self.policies.click_assignments_action_button()
        self.policies.click_create_policy_done_button()
        # self.policies.check_toast_successful_message("Policy unassigned successfully.")
        self.policies.dismiss_toast()

        #Policies-Policy tab: Remove the created policy from Policy tab
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        sleep(5)
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("remove")
        self.policies.click_contextual_footer_continue_button()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")
        self.policies.search_policy(policy_name)
        self.policies.verify_no_items_found()
    
        #Devices: Remove the assigned device from created group 

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
    
        #Devices: Delete the created group from Groups page
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()

        self.printers.click_printers_manage_group_button()
        sleep(5)
        self.printers_groups.remove_group_from_groups_page(group_name)

        # Verify toast notification message
        # assert f'Printer group "{group_name}" deleted' == self.printers_groups.verify_delete_groups_toast_message(), "Toast notification for group deletion not displayed"

        # close the toast notification if any
        self.printers.dismiss_toast()

        # verify group deletion success
        assert self.printers_groups.verify_group_name(group_name,displayed=False), "Group was not deleted successfully"