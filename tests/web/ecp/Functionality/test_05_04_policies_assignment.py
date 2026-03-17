import pytest
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import random
from time import sleep
pytest.app_info = "ECP"

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))

#Generate test group name
group_name="auto_group"+str(random.randint(100,999))

@pytest.mark.skip
class Test_01_ES_Tasks(object):

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
        # self.customer = self.account["customer"]

    def test_01_verify_devices_policy_assign_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/636150770
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960065
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961202
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()

        #Check for Online devices in Devices list table
        # self.devices.search_online_device("Online")

        #Create a group in devices page 
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.devices.click_devices_create_group_button()
        self.devices.enter_group_name(group_name)
        # self.devices.select_parent_group() #Parent group is removed from the UI, So commenting this line
        self.devices.click_create_group_popup_create_button()
        self.devices.verify_group_name(group_name)

        # close the toast notification if any
        self.devices.dismiss_toast()

        #Move an online device to the newly created group
        # self.devices.search_online_device("HP ")
        self.devices.verify_and_click_online_printer()
        # self.devices.click_devices_checkbox()
        self.devices.click_contextual_footer_select_action_dropdown()
        self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
        self.devices.click_contextual_footer_continue_button()
        self.devices.select_group(group_name)
        self.devices.click_move_to_group_popup_move_button()

        #Policies-Policies tab: Create a policy in Policies tab
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.click_create_policy_button()

        self.endpoint_security.enter_policy_name(policy_name)
        self.endpoint_security.select_policy_settings_type("Skip Template")
        self.endpoint_security.click_create_policy_next_button()
        
        self.endpoint_security.search_create_policy_settings("LLMNR")
        self.endpoint_security.click_select_policy_settings_checkbox()
        self.endpoint_security.click_create_policy_next_button()

        self.endpoint_security.click_create_policy_create_button()
        self.endpoint_security.click_create_policy_done_button()
        self.endpoint_security.verify_table_policy_by_name(policy_name, policy_search=True)

        #Policies-Policies tab: Save created policy status
        unassigned_policy_status = self.endpoint_security.get_policy_status() 

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
        self.endpoint_security.click_create_policy_done_button()
        # self.endpoint_security.check_toast_successful_message("Policy assigned successfully.")

        #Policies-Policies tab: Check Policy status after assignment to devices
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.search_policy(policy_name)

        assert unassigned_policy_status != self.endpoint_security.get_policy_status() 
        assert group_name == self.endpoint_security.get_policies_assigned_group_name()

    def test_02_verify_devices_assessment_report(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/663732123
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()

        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_first_entry_link()
        sleep(5) # wait for the devices details page to load
        self.devices.click_device_details_hp_secure_fleet_manager_tab()

        # Select assessment report for last 1 day
        self.endpoint_security.select_report("assessment")
        self.endpoint_security.verify_details_report_loaded()

        # get the most recent report result
        initial_report_result = self.endpoint_security.get_report_result()

        # Changing the LLMNR policy settings
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_first_entry_link()            
        self.endpoint_security.click_policy_details_card_edit_button()
        self.endpoint_security.click_llmnr_policy_settings_accordion()
        self.endpoint_security.click_llmnr_settings_toggle()
        self.endpoint_security.click_policy_settings_save_button()
        self.endpoint_security.click_are_you_sure_popup_save_button()
        self.endpoint_security.check_toast_successful_message("Policy has been saved successfully.")

        # Again check for assessment report
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()  
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_first_entry_link()
        sleep(4) # wait for the report to be generated
        self.devices.click_device_details_hp_secure_fleet_manager_tab()
        self.endpoint_security.select_report("assessment")
        self.endpoint_security.verify_details_report_loaded()

        # get the most recent report result and compare with initial
        final_report_result = self.endpoint_security.get_report_result()
        assert initial_report_result != final_report_result # Remediation was taking time for LLMNR setting, so remediation result was not matching with initial result

    def test_03_verify_device_details_policy_card(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/708348784
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.devices.click_devices_group(group_name)
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.endpoint_security.verify_devices_assigned_policy(policy_name)

    @pytest.mark.skip # Solution Device tab got removed from the UI, So skipping this test case
    def test_04_verify_solutions_device_details_policies_card(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/679212092
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.click_devices_tab() 
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.verify_devices_assigned_policy(policy_name)
        self.endpoint_security.click_policy_view_details_link()
        self.endpoint_security.verify_policy_details_card_policy_name(policy_name)
    
    def test_05_verify_assignment_page_refresh_btn(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960060
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        cur_time = self.endpoint_security.get_sync_time_info()
        sleep(1)
        self.endpoint_security.click_refresh_button()
        new_time = self.endpoint_security.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time
    
    def test_06_verify_assignments_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960061
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_assignments_add_policy_button()
        self.endpoint_security.click_add_policies_checkbox()
        self.endpoint_security.click_add_policy_button()
        self.endpoint_security.verify_assignments_contextual_footer()
        self.endpoint_security.verify_assignments_contextual_footer_cancel_button()
        self.endpoint_security.verify_assignments_contextual_footer_action_button()
        self.endpoint_security.click_assignments_contextual_footer_cancel_button()
        self.endpoint_security.verify_assignments_contextual_footer_is_not_displayed()
    
    def test_07_verify_policy_name_hyperlink(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960062
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961322
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961323
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)

        #verify policy preview page
        self.endpoint_security.select_assignments_policy_name()
        assert policy_name == self.endpoint_security.get_assignments_policy_preview_name()
        self.endpoint_security.verify_assignments_policy_settings_title()
        self.endpoint_security.click_assignments_policy_setting_card()
        self.endpoint_security.verify_assignments_policy_settings_card(expanded=True)
        self.endpoint_security.click_assignments_policy_preview_close_button()
    
    def test_08_verify_change_policy_priority_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961261
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961264
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635176
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        self.endpoint_security.click_assignments_add_policy_button()
        self.endpoint_security.search_add_policy("Do Not Delete")
        self.endpoint_security.click_add_policies_checkbox()
        self.endpoint_security.click_add_policy_button()
        self.endpoint_security.click_assignments_action_button()
        self.endpoint_security.click_create_policy_done_button()
        self.endpoint_security.click_change_policy_priority_button()

        # Verify Change Priority Policy Popup
        self.endpoint_security.verify_change_policy_priority_popup()
        self.endpoint_security.verify_change_policy_priority_popup_title()
        self.endpoint_security.verify_change_policy_priority_popup_description()
        self.endpoint_security.verify_change_policy_priority_popup_reset_button()
        self.endpoint_security.verify_change_policy_priority_popup_cancel_button()
        self.endpoint_security.verify_change_policy_priority_popup_save_button()
        self.endpoint_security.verify_change_policy_priority_popup_up_arrow_button()
        self.endpoint_security.verify_change_policy_priority_popup_down_arrow_button()
        self.endpoint_security.click_change_policy_priority_cancel_button()
        self.endpoint_security.verify_change_policy_priority_popup(displayed=False)
        
    def test_09_verify_change_policy_priority_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961267
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961268
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635172
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        initial_priority_order=self.endpoint_security.get_policy_priority()
        self.endpoint_security.click_change_policy_priority_button()

        # Change policy priority
        self.endpoint_security.click_change_policy_priority_checkbox()
        self.endpoint_security.click_change_policy_priority_down_arrow()
        self.endpoint_security.click_change_policy_priority_save_button()
        self.endpoint_security.click_assignments_action_button()
        self.endpoint_security.click_create_policy_done_button()
        changed_priority_order=self.endpoint_security.get_policy_priority()
        changed_priority_order.reverse()
        assert initial_priority_order == changed_priority_order

        # Reverting the changes
        self.endpoint_security.click_change_policy_priority_button()
        self.endpoint_security.click_change_policy_priority_checkbox(1)
        self.endpoint_security.click_change_policy_priority_up_arrow()
        self.endpoint_security.click_change_policy_priority_save_button()
        self.endpoint_security.dismiss_toast()
        self.endpoint_security.click_assignments_action_button()
        self.endpoint_security.click_create_policy_done_button()
        assert initial_priority_order == self.endpoint_security.get_policy_priority()

    def test_10_verify_change_policy_priority_popup_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635175
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        initial_priority_order=self.endpoint_security.get_policy_priority()
        self.endpoint_security.click_change_policy_priority_button()

        # Change policy priority and click on cancel button
        self.endpoint_security.click_change_policy_priority_checkbox()
        self.endpoint_security.click_change_policy_priority_down_arrow()
        self.endpoint_security.click_change_policy_priority_cancel_button()
        assert initial_priority_order == self.endpoint_security.get_policy_priority()
    
    def test_11_verify_add_policy_popup_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635168
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        if self.endpoint_security.verify_policy_assignments_side_groups_btn_is_enabled() is False:
            self.endpoint_security.click_policy_assignments_side_groups_btn()
        self.endpoint_security.select_group(group_name)
        initial_priority_order=self.endpoint_security.get_policy_priority()
        self.endpoint_security.click_assignments_add_policy_button()
        self.endpoint_security.click_add_policies_checkbox()

        # Select policy in add policy popup and click on cancel button
        self.endpoint_security.click_add_policy_popup_cancel_button()
        assert initial_priority_order == self.endpoint_security.get_policy_priority()

    def test_12_verify_devices_policy_unassign_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/636150768
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960066
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        
        #Unassign the created policy from created group in Assignments tab
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
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("remove")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_remove_policy_popup_remove_button()
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.verify_no_items_found()
    
        #Devices: Remove the assigned device from created group       
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
    
        #Devices: Delete the created group from devices list
        if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.devices.click_groups_side_bar_expand_btn()
        self.devices.click_devices_edit_group_button()
        self.devices.select_group(group_name)
        self.devices.click_edit_group_popup_delete_button()
        self.devices.click_delete_group_popup_delete_button()
        self.devices.click_edit_group_popup_close_button()

        # verify the deleted group name, should not display under Groups
        self.devices.verify_group_name(group_name,displayed=False)

    def test_13_verify_policy_names_in_add_policy_popup(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635167
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        all_policy_names=self.endpoint_security.get_all_policy_names()
        self.endpoint_security.click_assignments_tab()
        self.endpoint_security.click_assignments_add_policy_button()
        assert all_policy_names == self.endpoint_security.get_all_policy_names_from_add_policy_popup()

    def test_14_verify_add_policy_popup(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635164
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635169
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        self.endpoint_security.click_assignments_add_policy_button()

        # Verify Add Policy popup
        self.endpoint_security.verify_add_policy_popup()
        self.endpoint_security.verify_add_policy_popup_title()
        self.endpoint_security.verify_add_policy_popup_description()
        self.endpoint_security.verify_add_policy_popup_search_box()
        self.endpoint_security.verify_add_policy_popup_cancel_button()
        self.endpoint_security.verify_add_policy_popup_add_button()
        self.endpoint_security.click_add_policy_popup_cancel_button()
        self.endpoint_security.verify_add_policy_popup(displayed=False)

    def test_15_verify_add_policy_popup_add_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/720635170
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_assignments_tab()
        self.endpoint_security.click_assignments_add_policy_button()
        self.endpoint_security.verify_add_policy_popup_add_button_status("disabled")
        self.endpoint_security.click_add_policies_checkbox()
        self.endpoint_security.verify_add_policy_popup_add_button_status("enabled")