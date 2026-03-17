import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
import random
from time import sleep

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))

class Test_10_Workforce_Remediations_Print_Policies(object):

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
    def test_01_verify_policies_landing_page(self):
        #
        self.policies.verify_policies_tab_table_data_load() # This will raise an exception if the table is empty
        self.policies.verify_policies_tab_search_textbox()
        self.policies.verify_policies_tab_import_button()
        self.policies.verify_policies_tab_create_button()
        self.policies.verify_policies_tab_column_option_gear_btn()

    @pytest.mark.sanity
    def test_02_verify_policies_breadcrumb_and_its_navigation(self):
        #
        # Verify the breadcrumb  on the policies page
        self.policies.verify_fleet_management_policies_breadcrumb()

        # Verify the policies page URL
        self.policies.verify_policies_page_url(self.stack)

    def test_03_verify_policies_details_tab_breadcrumb_and_its_navigation(self):
        #
        self.policies.click_first_entry_link()

        # Verify the breadcrumb  on the policies details page
        self.policies.verify_fleet_management_policy_details_policies_breadcrumb
        self.policies.verify_policy_details_page_policy_detail_breadcrumb()

        # Verify the policies details page URL
        self.policies.verify_policies_details_page_url(self.stack)

        # Verify the navigation to the policies page from the policy details page.
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()

    def test_04_verify_edit_policy_tab_breadcrumb_and_its_navigation(self):
        #
        self.policies.click_first_entry_link()
        self.policies.click_policy_details_card_edit_button()

        # Verify the breadcrumb on the edit policy page
        self.policies.verify_fleet_management_policy_details_policies_breadcrumb()
        self.policies.verify_fleet_management_policy_policy_details_breadcrumb()
        self.policies.verify_edit_policies_page_breadcrumb()

        # Verify the edit policy page URL
        self.policies.verify_edit_policies_page_url(self.stack)

        # Verify the navigation to the policies details page from the edit policy page.
        self.policies.click_fleet_management_policy_policy_details_breadcrumb()
        self.policies.verify_policy_details_card()

        # Verify the navigation to the policies page from the edit policy page.
        self.policies.click_policy_details_card_edit_button()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()

    def test_05_verify_policies_pagination(self):
        #
        self.policies.verify_all_page_size_options([5, 25, 50, 100, 500])
        self.policies.verify_table_displaying_correctly(5, page=1)
        self.policies.verify_table_displaying_correctly(25, page=1)
        self.policies.verify_table_displaying_correctly(50, page=1)
        self.policies.verify_table_displaying_correctly(100, page=1)
        self.policies.verify_table_displaying_correctly(500, page=1)

    @pytest.mark.sanity
    def test_06_verify_column_option_popup_ui(self):
        #
         expected_options= ["Policy Name", "Status", "Assigned To", "Category", "Modified By", "Last Modified"]
         self.policies.click_policies_tab_column_option_gear_btn()
         self.policies.verify_column_options_popup_title()
         self.policies.verify_column_options_popup_reset_to_default_button()
         self.policies.verify_column_options_popup_save_button()
         self.policies.verify_column_options_popup_cancel_button()
         assert expected_options == self.policies.get_column_options_popup_options()

    @pytest.mark.sanity
    def test_07_verify_policies_tab_default_column_headers(self):
        #
        expected_table_headers = ["Policy Name", "Status", "Assigned To", "Category", "Modified By", "Last Modified"]
        sleep(3) # Adding sleep to wait for the table to load
        assert expected_table_headers == self.policies.verify_policies_table_headers()

    def test_08_verify_column_option_popup_cancel_button(self):
        #
        self.policies.click_policies_tab_column_option_gear_btn()
        self.policies.click_column_option("Category")
        self.policies.click_column_options_popup_cancel_button()

        # Verify Policies table Status Column
        self.policies.verify_policies_table_column("Category")
    
    @pytest.mark.sanity
    def test_09_verify_column_option_popup_save_button(self):
        #
        self.policies.click_policies_tab_column_option_gear_btn()
        self.policies.click_column_option("Category")
        self.policies.click_column_options_popup_save_button()     
        
        # Verify Policies table Status Column
        self.policies.verify_policies_tab_table_data_load()
        self.policies.verify_policies_table_column("Category",displayed=False)

        # Reverting the Column option changes
        self.policies.click_policies_tab_column_option_gear_btn()
        self.policies.click_column_option("Category")
        self.policies.click_column_options_popup_save_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.verify_policies_table_column("Category",displayed=True)

    def test_10_verify_policy_details_policy_settings_search(self):
        #
        self.policies.create_policy(policy_name,policy_settings="Manual Feed Prompt")
        self.policies.search_policy(policy_name)
        self.policies.click_first_entry_link()
        self.policies.verify_policy_details_policy_settings_search("Manual Feed Prompt")
        self.policies.verify_policy_settings_card()
        self.policies.click_policy_settings_card()
        self.policies.verify_policy_settings_card(expanded=True)

        # Removing the Policy
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()
        self.policies.search_policy(policy_name)
        sleep(5) # Adding sleep to wait for the table to load
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("remove")
        self.policies.click_contextual_footer_continue_button()
        self.policies.click_remove_policy_popup_remove_button()
        self.policies.check_toast_successful_message("Policy has been removed.")

    def test_11_verify_edit_policy_screen_ui(self):
        # 
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()

        # Verify Edit Policy UI
        self.policies.verify_edit_policy_policy_name_text_field()
        self.policies.verify_edit_policy_note_text_field()
        self.policies.verify_edit_policy_search_box()
        self.policies.verify_edit_policy_add_button() 

    def test_12_verify_are_you_sure_to_save_this_policy_popup(self):
        # 
        self.policies.click_first_entry_link()
        self.policies.click_policy_details_card_edit_button()
        sleep(3) # Adding sleep to wait for the Edit page to load
        self.policies.update_policy_name("Policy Name")
        self.policies.click_policy_save_button()

        # Verify Are you sure to save this policy popup UI
        self.policies.verify_are_you_sure_to_save_this_policy_popup()
        self.policies.verify_are_you_sure_to_save_this_policy_popup_description()
        self.policies.verify_are_you_sure_to_save_this_policy_popup_policy_name()
        self.policies.verify_are_you_sure_to_save_this_policy_popup_cancel_button()
        self.policies.verify_are_you_sure_to_save_this_policy_popup_save_button()
        self.policies.click_are_you_sure_to_save_this_policy_popup_cancel_button()
        self.policies.verify_are_you_sure_to_save_this_policy_popup(displayed=False)
        assert "Policy Name" == self.policies.get_updated_policy_name()

    def test_13_verify_add_policy_in_edit_policy_screen(self):
        # 
        policy_settings = "Use Requested Tray"
        self.policies.create_policy(policy_name,policy_settings)
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        sleep(5) # Adding sleep to wait for the Edit Policy page to load

        # Add new policy settings to this policy
        self.policies.click_edit_policy_add_button()
        self.policies.search_policy_settings_in_add_policy_popup("Manual Feed Prompt")
        self.policies.click_add_policy_checkbox()
        self.policies.click_add_policy_popup_add_button()
        self.policies.click_policy_save_button()
        self.policies.click_confirm_policy_save_button()
        self.policies.check_toast_successful_message("Policy has been saved successfully.")
        self.policies.dismiss_toast()

    def test_14_verify_search_functionality_in_edit_policy_screen(self):
        # 
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()

        # Verify search functionality in edit policy screen
        self.policies.verify_policy_details_policy_settings_search("Manual Feed Prompt")

    def test_15_verify_remove_policy_settings_in_edit_policy_screen(self):
        # 
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        sleep(5) # Adding sleep to wait for the Edit Policy page to load

        # Remove added policy setting
        policy_settings_count = self.policies.get_policy_settings_count()
        self.policies.verify_policy_details_policy_settings_search("Manual Feed Prompt")
        self.policies.click_remove_policy_settings_trash_button()
        self.policies.click_policy_save_button()
        self.policies.click_confirm_policy_save_button()
        self.policies.check_toast_successful_message("Policy has been saved successfully.")
        self.policies.dismiss_toast()
        sleep(5) # Adding sleep to wait for the Policies page to load
        # self.policies.click_remediations_printer_policies_button()
        self.policies.verify_policies_tab_table_data_load()

        # Verify policy settings removed successfully
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        assert policy_settings_count-1 == self.policies.get_policy_settings_count()

    def test_16_verify_add_policy_popup_cancel_button_functionality(self):
        # 
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()

        # Select policy to add and then click cancel
        policy_settings_count = self.policies.get_policy_settings_count()
        self.policies.click_edit_policy_add_button()
        self.policies.search_policy_settings_in_add_policy_popup("Manual Feed Prompt")
        self.policies.click_add_policy_checkbox()
        self.policies.click_edit_policy_screen_add_policy_popup_cancel_button()
        assert policy_settings_count == self.policies.get_policy_settings_count()

    def test_17_verify_add_policy_popup_ui(self):
        # 
        self.policies.search_policy(policy_name)
        self.policies.click_policy_checkbox()
        self.policies.click_contextual_footer_select_action_dropdown()
        self.policies.select_action_dropdown_option("edit")
        self.policies.click_contextual_footer_continue_button()
        sleep(4) # Adding sleep to wait for the Edit Policy page to load
        self.policies.click_edit_policy_add_button()

        # Verify add policy popup
        self.policies.verify_add_policy_pop_up()  
        self.policies.verify_add_policy_pop_up_title()
        self.policies.verify_add_policy_related_items()
        self.policies.verify_add_policy_cancel_button()
        self.policies.verify_add_policy_add_button()
        self.policies.verify_add_policy_popup_search_funtionality("Manual Feed Prompt")
        self.policies.click_edit_policy_screen_add_policy_popup_cancel_button()
        self.policies.verify_add_policy_pop_up(displayed=False)

        # Removing the created policy
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.remove_policy(policy_name)
        self.policies.check_toast_successful_message("Policy has been removed.")