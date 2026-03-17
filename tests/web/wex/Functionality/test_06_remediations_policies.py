import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
import random
from time import sleep

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))

class Test_06_Workforce_Remediations_Print_Policies(object):

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
        # self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        return self.policies.verify_fleet_management_policies_breadcrumb()

    def test_01_verify_policies_contextual_footer(self):
        #
        self.policies.click_policy_checkbox()
        self.policies.verify_contextual_footer()
        self.policies.verify_contextual_footer_cancel_button()
        self.policies.verify_contextual_footer_selected_item_label()
        self.policies.verify_contextual_footer_select_action_dropdown()
        self.policies.verify_contextual_footer_continue_button()

    def test_02_verify_policies_contextual_footer_select_action_dropdown_options(self):
        #
        expected_option=["Copy to Same Location","Edit","Export","Remove"]
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        assert expected_option == self.policies.get_contextual_footer_select_action_dropdown_options()

    def test_03_verify_policies_contextual_footer_cancel_button_functionality(self):
        #
        self.policies.click_policy_checkbox()
        self.policies.verify_contextual_footer()
        self.policies.click_contextual_footer_cancel_button()
        self.policies.verify_contextual_footer(displayed=False)

    def test_04_verify_table_sort(self):
        #
        self.policies.verify_policies_tab_table_data_load()
        self.policies.verify_table_sort("status", ["Assigned", "Unassigned"])

    def test_05_verify_sort_change(self):
        #
        self.policies.verify_policies_tab_table_data_load()
        self.policies.click_table_header_by_name("status")
        self.policies.verify_table_sort("status", ["Unassigned", "Assigned"])
    
    def test_06_verify_policies_table_sort_by_policy_name_column(self):
        #
        # Verify the default table sort by Policy Name (not sorted by default)
        self.policies.verify_policies_tab_table_data_load()
        initial_policy_name = self.policies.get_all_policy_table_policy_names()
 
        # Verify the sort change by device name (ascending order on first click)
        self.policies.click_table_header_by_name("policy_name")
        self.policies.verify_printers_table_sort("policy_name", sorted(initial_policy_name))
 
        # Verify the sort change by device name (descending order on second click)
        self.policies.click_table_header_by_name("policy_name")
        self.policies.verify_printers_table_sort("policy_name", sorted(initial_policy_name, reverse=True))
    
    def test_07_verify_policies_table_sort_by_status_column(self):
        #
        # Verify the default table sort by Status (not sorted by default)
        self.policies.verify_policies_tab_table_data_load()
        initial_status = self.policies.get_all_status()
        #verify sorted by default by status with assigned first and unassigned second
        self.policies.verify_printers_table_sort("status", initial_status)

        # Verify the sort change by device name (descending order on second click)
        self.policies.click_table_header_by_name("status")
        self.policies.verify_printers_table_sort("status", sorted(initial_status, reverse=True))
    
    def test_08_verify_policies_table_sort_by_modified_by_column(self):
        #
        # Verify the default table sort by modified by (not sorted by default)
        self.policies.verify_policies_tab_table_data_load()
        initial_modified_by = self.policies.get_all_modified_by()
 
        # Verify the sort change by device name (ascending order on first click)
        self.policies.click_table_header_by_name("modified_by")
        self.policies.verify_printers_table_sort("modified_by", sorted(initial_modified_by))
 
        # Verify the sort change by device name (descending order on second click)
        self.policies.click_table_header_by_name("modified_by")
        self.policies.verify_printers_table_sort("modified_by", sorted(initial_modified_by, reverse=True))
    
    def test_09_verify_policies_table_sort_by_last_modified_column(self):
        #
        # Verify the default table sort by Last modified (not sorted by default)
        self.policies.verify_policies_tab_table_data_load()
        initial_last_modified = self.policies.get_all_last_modified()
 
        # Verify the sort change by Last modified (descending order on first click)
        self.policies.click_table_header_by_name("last_modified")
        descending_last_modified = self.policies.get_all_last_modified()
        self.policies.verify_policies_last_modified_column_is_sorted(descending_last_modified, order="descending")
 
        # Verify the sort change by Last modified (ascending order on second click)
        self.policies.click_table_header_by_name("last_modified")
        ascending_last_modified = self.policies.get_all_last_modified()
        self.policies.verify_policies_last_modified_column_is_sorted(ascending_last_modified, order="ascending")

    def test_10_verify_settings_not_saved_popup(self):
        # 
        self.policies.click_first_entry_link()
        self.policies.click_policy_details_card_edit_button()
    
        # Update Policy Name
        sleep(3) # Adding sleep to wait for the Edit page to load
        self.policies.update_policy_name("Policy Name")
        # self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        
        # Verify Settings Not Saved Popup
        self.policies.verify_settings_not_saved_popup()
        self.policies.verify_settings_not_saved_popup_title()
        self.policies.verify_settings_not_saved_popup_desc()
        self.policies.verify_settings_not_saved_popup_cancel_button()
        self.policies.verify_settings_not_saved_popup_leave_button()

        # Click Settings not saved Cancel Button
        self.policies.click_settings_not_saved_popup_cancel_button()

        # Verify Settings not popup is displayed
        self.policies.verify_settings_not_saved_popup(displayed=False)
        assert "Policy Name" == self.policies.get_updated_policy_name()

    def test_11_verify_settings_not_saved_popup_leave_button_functionality(self):
        # 
        self.policies.click_first_entry_link()
        self.policies.click_policy_details_card_edit_button()
    
        # Update Policy Name
        sleep(3) # Adding sleep to wait for the Edit page to load
        self.policies.update_policy_name("Policy Name")
        # self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()

        # Click Settings not saved Leave Button
        self.policies.click_settings_not_saved_popup_leave_button()

        # Verify Policies screen is displayed
        self.policies.verify_policies_tab_table_data_load()

    def test_12_verify_contextual_footer_in_edit_policy_screen(self):
        # 
        self.policies.click_first_entry_link()
        self.policies.click_policy_details_card_edit_button()
    
        # Update Policy Name
        sleep(3) # Adding sleep to wait for the Edit page to load
        self.policies.update_policy_name("Policy Name")

        # Verify Contextual footer
        self.policies.verify_contextual_footer()
        self.policies.verify_contextual_footer_cancel_button()
        self.policies.verify_contextual_footer_save_button()

        #Verify cancel button functionality in Contextual footer
        self.policies.click_contextual_footer_cancel_button()
        self.policies.verify_contextual_footer(displayed=False)
        assert "Policy Name" != self.policies.get_updated_policy_name()

    def test_13_verify_create_policy_basic_information_screen_ui(self):
        # 
        self.policies.click_create_policy_button()

        # Verify create policy basic info screen
        self.policies.verify_create_policy_popup()
        self.policies.verify_create_policy_popup_title()
        self.policies.verify_basic_info_screen_step_title()
        self.policies.verify_basic_info_screen_step_description()
        self.policies.verify_basic_info_screen_policy_name_field()
        self.policies.verify_basic_info_screen_policy_name_field_error_msg()
        self.policies.verify_basic_info_screen_policy_settings_type_error_msg()
        self.policies.verify_basic_info_screen_note_field()
        self.policies.verify_create_policy_cancel_button()
        self.policies.enter_policy_name(policy_name)

        # Click on cancel button
        self.policies.click_create_policy_cancel_button()
        self.policies.verify_create_policy_popup(displayed=False)

    def test_14_verify_create_policy_templates_and_attributes_screen_ui(self):
        #
        self.policies.click_create_policy_button()
        # self.policies.click_create_policy_next_button()
        self.policies.enter_policy_name(policy_name)
        self.policies.select_policy_settings_type("Skip Template")
        self.policies.click_create_policy_next_button()

        # Verify create policy template and attributes screen
        self.policies.verify_create_policy_popup()
        self.policies.verify_create_policy_step2_title()
        self.policies.verify_create_policy_step2_description()
        self.policies.verify_create_policy_step2_related_items()
        self.policies.verify_add_policy_popup_search_funtionality("Manual Feed Prompt")
        self.policies.verify_create_policy_next_button_status("disabled")

        # Click on cancel button
        self.policies.click_create_policy_cancel_button()
        self.policies.verify_create_policy_popup(displayed=False)

    def test_15_verify_create_policy_set_options_screen_ui(self):
        #
        self.policies.click_create_policy_button()
        self.policies.click_create_policy_next_button()
        self.policies.enter_policy_name(policy_name)
        self.policies.select_policy_settings_type("Skip Template")
        self.policies.click_create_policy_next_button()
        self.policies.search_create_policy_settings("AirPrint")
        self.policies.click_select_policy_settings_checkbox()
        self.policies.verify_create_policy_next_button_status("enabled")
        self.policies.click_create_policy_next_button()

        # Verify create policy set options screen ui
        self.policies.verify_create_policy_popup()
        self.policies.verify_create_policy_step3_title()
        self.policies.verify_create_policy_step3_description()
        self.policies.search_create_policy_settings("AirPrint")
        self.policies.verify_create_policy_cancel_button()
        self.policies.verify_create_policy_back_button()
        self.policies.verify_create_policy_create_button()

        # Click on cancel button
        self.policies.click_create_policy_cancel_button()
        self.policies.verify_create_policy_popup(displayed=False)
    
    def test_16_verify_change_not_recommended_popup_ui(self):
        #
        self.policies.create_policy(policy_name,policy_settings="Require HTTPS Redirect")
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        self.printers.click_device_specific_policy_settings_card("https-redirect")
        self.printers.click_ignore_unsupported_item_toggle()
        self.printers.click_set_options_settings_checkbox("https-redirect")
        self.policies.click_policy_save_button()

        # Verify Change Not Recommended Popup UI
        self.policies.verify_change_not_recommended_popup()
        self.policies.verify_change_not_recommended_popup_title()
        self.policies.verify_change_not_recommended_popup_desc()
        self.policies.verify_change_not_recommended_popup_desc_end_part()
        self.policies.verify_change_not_recommended_popup_cancel_button()
        self.policies.verify_change_not_recommended_popup_confirm_button()

    def test_17_verify_change_not_recommended_popup_cancel_button_functionality(self):
        #
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        self.printers.click_device_specific_policy_settings_card("https-redirect")
        self.printers.click_ignore_unsupported_item_toggle()
        self.printers.click_set_options_settings_checkbox("https-redirect")
        self.policies.click_policy_save_button()
        self.policies.verify_change_not_recommended_popup()
        self.policies.click_change_not_recommended_popup_cancel_button()
        self.policies.verify_change_not_recommended_popup(displayed=False)

    def test_18_verify_change_not_recommended_popup_confirm_button_functionality(self):
        #
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        self.printers.click_device_specific_policy_settings_card("https-redirect")
        self.printers.click_ignore_unsupported_item_toggle()
        self.printers.click_set_options_settings_checkbox("https-redirect")
        self.policies.click_policy_save_button()
        self.policies.verify_change_not_recommended_popup()
        self.policies.click_change_not_recommended_popup_confirm_button()
        self.policies.verify_are_you_sure_to_save_this_policy_popup_policy_name()
        self.policies.verify_are_you_sure_to_save_this_policy_popup_policy_name_value(policy_name)
        self.policies.click_confirm_policy_save_button()
        self.policies.check_toast_successful_message("Policy has been saved successfully.")
        self.policies.dismiss_toast()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.remove_policy(policy_name)
        self.policies.check_toast_successful_message("Policy has been removed.")

    def test_19_verify_polciy_details_search_field_default_text_based_on_category_selection(self):
        #
        self.policies.click_first_entry_link()
        self.policies.verify_policy_settings_card()

        # Verify the default search field text
        self.policies.verify_policy_details_policy_settings_search_txtbox_text("All")
        
        # Retrieve all available category names dynamically
        category_names = self.policies.get_policy_details_policy_settiings_category_options()
        
        # Iterate over each category name and verify the search field default text
        for category_name in category_names:
            self.policies.select_policy_details_policy_settiings_category_option(category_name)
            self.policies.verify_policy_details_policy_settings_search_txtbox_text(category_name)