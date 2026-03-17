import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
import random
from time import sleep

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))

class Test_11_Workforce_Remediations_Print_Policies(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.policies = self.fc.fd["fleet_management_policies"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_remediations_button_is_expanded() is False:
            self.home.click_sidemenu_remediations_dropdown_button()
        self.home.click_remediations_policies_dropdown_option()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.verify_remediations_printer_policies_tab()
        self.policies.click_remediations_printer_policies_button()
        return self.policies.verify_fleet_management_policies_breadcrumb()

    @pytest.mark.sanity
    def test_01_verify_create_policy_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636150773
        self.policies.click_create_policy_button()
        self.policies.click_create_policy_next_button()

        self.policies.enter_policy_name(policy_name)
        self.policies.select_policy_settings_type("Skip Template")
        self.policies.click_create_policy_next_button()
        
        self.policies.search_create_policy_settings("AirPrint")
        self.policies.click_select_policy_settings_checkbox()
        self.policies.click_create_policy_next_button()

        self.policies.click_create_policy_create_button()
        self.policies.verify_policy_created_successfully_popup_title()
        self.policies.verify_policy_created_successfully_popup_description()
        self.policies.verify_policy_created_successfully_popup_policy_name(policy_name)
        self.policies.verify_policy_created_successfully_popup_done_button()
        self.policies.click_create_policy_done_button()
        self.policies.verify_table_policy_by_name(policy_name, policy_search=True, policy_status= "Active")
    
    def test_02_verify_operation_failed_popup_ui(self):
        #
        self.policies.search_policy("Do Not Delete")
        sleep(3) # Adding sleep to wait for the table to load
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        sleep(3) # Adding sleep to wait for the dropdown options to load
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()

        # Update Policy Name
        sleep(3) # Adding sleep to wait for the Edit page to load
        self.policies.update_policy_name(policy_name)
        self.policies.click_policy_save_button()
        self.policies.click_confirm_policy_save_button()

        # Verify Operation Failed Popup UI
        self.policies.verify_operation_failed_popup()
        self.policies.verify_operation_failed_popup_title()
        self.policies.verify_operation_failed_popup_description()
        self.policies.verify_operation_failed_popup_ok_button()
        self.policies.click_operation_failed_popup_ok_button()
        # Verify the popup is dismissed after clicking OK button
        self.policies.verify_operation_failed_popup(displayed=False)
        # Verify Edit Policy UI
        self.policies.verify_edit_policy_policy_name_text_field()
        self.policies.verify_edit_policy_note_text_field()

    @pytest.mark.sanity
    def test_03_verify_policies_search_functionality(self):
        #
        self.policies.verify_table_policy_by_name(policy_name, policy_search=True)

    @pytest.mark.sanity
    def test_04_verify_policies_invalid_search_functionality(self):
        #
        self.policies.search_policy("invalidpolicy")
        self.policies.verify_no_items_found()

    @pytest.mark.sanity
    @pytest.mark.parametrize("status", ["Assigned", "Unassigned"])
    def test_05_verify_policies_search_functionality_with_status(self, status):
        self.policies.verify_table_policy_by_status(status, status_search=True)

    @pytest.mark.sanity
    def test_06_verify_policies_search_functionality_with_category(self):
        self.policies.verify_table_policy_by_category("Security", category_search=True)
    
    @pytest.mark.sanity
    def test_07_verify_policies_search_functionality_with_modified_by(self):
        self.policies.verify_table_policy_by_modified_by("Print", modified_by_search=True)

    @pytest.mark.sanity
    def test_08_verify_copy_to_same_location_policy_functionality(self):
        #
        self.policies.search_policy(policy_name)
        policy_setings_names = self.policies.get_policy_settings_names()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("clone")
        self.policies.click_contextual_footer_continue_button()
        self.policies.check_toast_successful_message("Policy has been cloned.")
        self.policies.dismiss_toast()
        self.policies.verify_table_policy_by_name(policy_name+" (1)", policy_search=True)
        assert policy_setings_names == self.policies.get_policy_settings_names()

        # Removing the Cloned Policy
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.search_policy(policy_name+" (1)")
        self.policies.click_policy_checkbox()
        sleep(3)
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("remove")
        self.policies.click_contextual_footer_continue_button()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")
        self.policies.search_policy(policy_name+" (1)")
        self.policies.verify_no_items_found()

    def test_09_verify_export_button_functionality_in_policies_tab(self):
        #
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("export")
        self.policies.click_contextual_footer_continue_button()
        self.policies.verify_contextual_footer(displayed=False)

    @pytest.mark.sanity
    def test_10_verify_policy_name_edit_functionality(self):
        #
        self.policies.search_policy(policy_name)
        sleep(5) # Adding sleep to wait for the table to load
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()

        # Update Policy Name
        sleep(3) # Adding sleep to wait for the Edit page to load
        self.policies.update_policy_name("update_"+policy_name)
        self.policies.click_policy_save_button()
        self.policies.click_confirm_policy_save_button()
        self.policies.check_toast_successful_message("Policy has been saved successfully.")
        self.policies.verify_table_policy_by_name("update_"+policy_name, policy_search=True)

    @pytest.mark.sanity
    def test_11_verify_remove_policy_functionality(self):
        #
        self.policies.search_policy("update_"+policy_name)
        sleep(5) # Adding sleep to wait for the table to load
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("remove")
        self.policies.click_contextual_footer_continue_button()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")
        self.policies.search_policy("update_"+policy_name)
        self.policies.verify_no_items_found()

    @pytest.mark.sanity
    def test_12_verify_policy_details(self):
        # 
        policy_settings = "Manual Feed Prompt"
        self.policies.create_policy(policy_name,policy_settings)
        self.policies.search_policy(policy_name)
        actual_policy_settings = self.policies.get_policy_settings_names()
        self.policies.verify_policy_details_card()
        self.policies.click_policy_details_card()
        self.policies.verify_policy_details_card(expanded=False)
        self.policies.verify_policy_details_card_policy_name(policy_name)
        self.policies.verify_policy_details_card_edit_button()
        self.policies.click_policy_details_card_more_button()
        self.policies.verify_policy_details_card_remove_option() 
        assert policy_settings == actual_policy_settings[0]

    @pytest.mark.sanity
    def test_13_verify_policy_details_remove_policy_functionality(self):
        #
        self.policies.search_policy(policy_name)
        self.policies.click_first_entry_link()
        self.policies.click_policy_details_card_more_button()
        self.policies.click_policy_details_card_remove_option()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")
        self.policies.search_policy(policy_name) 
        self.policies.verify_no_items_found()