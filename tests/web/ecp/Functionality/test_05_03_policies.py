import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import random
pytest.app_info = "ECP"

#Generate test policy name
policy_name="auto_policy"+str(random.randint(100,999))

class Test_01_ES_Policies(object):

    # Following variavles are severity option index, used for severity dropdown.
    LOW=0
    MEDIUM=1
    HIGH=2

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_policies(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_tab()
        return self.endpoint_security.verify_table_loaded()

    def test_01_verify_policy_page_table(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961335
        self.endpoint_security.verify_all_page_size_options_new([5, 25, 50, 100, 500])
        self.endpoint_security.verify_table_displaying_correctly_new(5, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(25, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(50, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(100, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(500, page=1)

    def test_02_verify_policy_page_refresh_btn(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961334
        cur_time = self.endpoint_security.get_sync_time_info()
        sleep(1)
        self.endpoint_security.click_refresh_button()
        new_time = self.endpoint_security.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def test_03_verify_default_sort(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636862468
        self.endpoint_security.verify_table_sort("status", ["Assigned", "Unassigned"])
    
    def test_04_verify_sort_change(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636862468
        self.endpoint_security.click_table_header_by_name("status")
        self.endpoint_security.verify_table_sort("status", ["Unassigned", "Assigned"])

    def test_05_verify_policies_contextual_footer(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636862467
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.verify_contextual_footer()
        self.endpoint_security.verify_contextual_footer_cancel_button()
        self.endpoint_security.verify_contextual_footer_selected_item_label()
        self.endpoint_security.verify_contextual_footer_select_action_dropdown()
        self.endpoint_security.verify_contextual_footer_continue_button()

    def test_06_verify_policies_contextual_footer_select_action_dropdown_options(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961338
        expected_option=["Copy to Same Location","Edit","Export","Remove"]
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        assert expected_option == self.endpoint_security.get_contextual_footer_select_action_dropdown_options()

    def test_07_verify_policies_contextual_footer_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961342
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.verify_contextual_footer()
        self.endpoint_security.click_contextual_footer_cancel_button()
        self.endpoint_security.verify_contextual_footer(displayed=False)
    
    def test_08_verify_create_policy_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636150773
        self.endpoint_security.click_create_policy_button()

        self.endpoint_security.enter_policy_name(policy_name)
        sleep(5) # Need to wait for the policy name to be updated
        self.endpoint_security.select_policy_settings_type("Skip Template")
        self.endpoint_security.click_create_policy_next_button()
        
        self.endpoint_security.search_create_policy_settings("AirPrint")
        self.endpoint_security.click_select_policy_settings_checkbox()
        self.endpoint_security.click_create_policy_next_button()

        self.endpoint_security.click_create_policy_create_button()
        self.endpoint_security.verify_policy_created_successfully_popup_title()
        self.endpoint_security.verify_policy_created_successfully_popup_description()
        self.endpoint_security.verify_policy_created_successfully_popup_policy_name(policy_name)
        self.endpoint_security.verify_policy_created_successfully_popup_done_button()
        self.endpoint_security.click_create_policy_done_button()
        self.endpoint_security.verify_table_policy_by_name(policy_name, policy_search=True)

    def test_09_verify_policies_search_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636862466
        self.endpoint_security.verify_table_policy_by_name(policy_name, policy_search=True)

    def test_10_verify_policies_invalid_search_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/636862466
        self.endpoint_security.search_policy("invalidpolicy")
        self.endpoint_security.verify_no_items_found()
    
    def test_11_verify_clone_policy_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961339
        self.endpoint_security.search_policy(policy_name)
        policy_setings_names = self.endpoint_security.get_policy_settings_names()
        self.endpoint_security.click_policies_breadcrumb()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("clone")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.check_toast_successful_message("Policy has been cloned.")
        self.endpoint_security.dismiss_toast()
        self.endpoint_security.verify_table_policy_by_name(policy_name+" (1)", policy_search=True)
        assert policy_setings_names == self.endpoint_security.get_policy_settings_names()

        # Removing the Cloned Policy
        self.endpoint_security.click_policies_breadcrumb()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.search_policy(policy_name+" (1)")
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("remove")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_remove_policy_popup_remove_button()
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")
        self.endpoint_security.search_policy(policy_name+" (1)")
        self.endpoint_security.verify_no_items_found()
    
    def test_12_verify_policy_rename_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961340
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()

        # Update Policy Name
        self.endpoint_security.update_policy_name("update_"+policy_name)
        self.endpoint_security.click_policy_save_button()
        self.endpoint_security.click_are_you_sure_popup_save_button()
        self.endpoint_security.check_toast_successful_message("Policy has been saved successfully.")
        self.endpoint_security.verify_table_policy_by_name("update_"+policy_name, policy_search=True)

    def test_13_verify_remove_policy_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/678961343
        self.endpoint_security.search_policy("update_"+policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("remove")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_remove_policy_popup_remove_button()
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")
        self.endpoint_security.search_policy("update_"+policy_name)
        self.endpoint_security.verify_no_items_found()
    
    def test_14_verify_policy_details(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959995
        policy_settings = "Require HTTPS Redirect"
        self.endpoint_security.create_policy(policy_name,policy_settings)
        self.endpoint_security.search_policy(policy_name)
        actual_policy_settings = self.endpoint_security.get_policy_settings_names()
        self.endpoint_security.verify_policy_details_card()
        self.endpoint_security.click_policy_details_card()
        self.endpoint_security.verify_policy_details_card(expanded=False)
        self.endpoint_security.verify_policy_details_card_policy_name(policy_name)
        self.endpoint_security.verify_policy_details_card_edit_button()
        self.endpoint_security.click_policy_details_card_more_button()
        self.endpoint_security.verify_policy_details_card_remove_option()
        assert policy_settings == actual_policy_settings[0]

    def test_15_verify_policy_details_remove_policy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960001
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.click_policy_details_card_more_button()
        self.endpoint_security.click_policy_details_card_remove_option()
        self.endpoint_security.click_remove_policy_popup_remove_button()
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.verify_no_items_found()

    def test_16_verify_policy_details_policy_settings_search(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678960002
        self.endpoint_security.create_policy(policy_name,policy_settings="Require HTTPS Redirect")
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.verify_policy_details_policy_settings_search("Require HTTPS Redirect")
        self.endpoint_security.verify_policy_settings_card()
        self.endpoint_security.click_policy_settings_card()
        self.endpoint_security.verify_policy_settings_card(expanded=True)

        # Removing the Policy
        self.endpoint_security.click_policies_breadcrumb()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("remove")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_remove_policy_popup_remove_button()
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")

    def test_17_verify_edit_policy_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635194
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()

        # Verify Edit Policy UI
        self.endpoint_security.verify_page_title("Edit Policy")
        self.endpoint_security.verify_edit_policy_refresh_button()
        self.endpoint_security.verify_edit_policy_policy_name_text_field()
        self.endpoint_security.verify_edit_policy_note_text_field()
        self.endpoint_security.verify_edit_policy_search_box()
        self.endpoint_security.verify_edit_policy_add_button()  

    def test_18_verify_are_you_sure_to_save_this_policy_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635203
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635204
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.click_policy_details_card_edit_button()
        self.endpoint_security.update_policy_name("Policy Name")
        self.endpoint_security.click_policy_save_button()

        # Verify Are you sure to save this policy popup UI
        self.endpoint_security.verify_are_you_sure_to_save_this_policy_popup()
        self.endpoint_security.verify_are_you_sure_to_save_this_policy_popup_description()
        self.endpoint_security.verify_are_you_sure_to_save_this_policy_popup_policy_name()
        self.endpoint_security.verify_are_you_sure_to_save_this_policy_popup_cancel_button()
        self.endpoint_security.verify_are_you_sure_to_save_this_policy_popup_save_button()
        self.endpoint_security.click_are_you_sure_to_save_this_policy_popup_cancel_button()
        self.endpoint_security.verify_are_you_sure_to_save_this_policy_popup(displayed=False)
        assert "Policy Name" == self.endpoint_security.get_updated_policy_name()

    def test_19_verify_settings_not_saved_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961396
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961398
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.click_policy_details_card_edit_button()
    
        # Update Policy Name
        sleep(4) # Need to wait for the Edit policy page to load
        self.endpoint_security.update_policy_name("Policy Name")
        self.endpoint_security.click_policies_breadcrumb()
        
         # Verify Settings Not Saved Popup
        self.endpoint_security.verify_settings_not_saved_popup()
        self.endpoint_security.verify_settings_not_saved_popup_title()
        self.endpoint_security.verify_settings_not_saved_popup_desc()
        self.endpoint_security.verify_settings_not_saved_popup_cancel_button()
        self.endpoint_security.verify_settings_not_saved_popup_leave_button()

        # Click Settings not saved Cancel Button
        self.endpoint_security.click_settings_not_saved_popup_cancel_button()

        # Verify Settings not popup is displayed
        self.endpoint_security.verify_settings_not_saved_popup(displayed=False)
        assert "Policy Name" == self.endpoint_security.get_updated_policy_name()

    def test_20_verify_settings_not_saved_popup_leave_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961397
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.click_policy_details_card_edit_button()
    
        # Update Policy Name
        sleep(3) # Need to wait for the Edit policy page to load
        self.endpoint_security.update_policy_name("Policy Name")
        self.endpoint_security.click_policies_breadcrumb()

        # Click Settings not saved Leave Button
        self.endpoint_security.click_settings_not_saved_popup_leave_button()

        # Verify Policies screen is displayed
        self.endpoint_security.verify_page_title("Policies")
    
    def test_21_verify_contextual_footer_in_edit_policy_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961399
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961400
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.click_policy_details_card_edit_button()
    
        # Update Policy Name
        sleep(3) # Need to wait for the Edit policy page to load
        self.endpoint_security.update_policy_name("Policy Name")

        # Verify Contextual footer
        self.endpoint_security.verify_contextual_footer()
        self.endpoint_security.verify_contextual_footer_cancel_button()
        self.endpoint_security.verify_contextual_footer_save_button()

        #Verify cancel button functionality in Contextual footer
        self.endpoint_security.click_contextual_footer_cancel_button()
        self.endpoint_security.verify_contextual_footer(displayed=False)
        assert "Policy Name" != self.endpoint_security.get_updated_policy_name()

    def test_22_verify_add_policy_in_edit_policy_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635207
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635211
        policy_settings = "Use Requested Tray"
        self.endpoint_security.create_policy(policy_name,policy_settings)
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()

        # Add new policy settings to this policy
        self.endpoint_security.click_edit_policy_add_button()
        self.endpoint_security.search_policy_settings_in_add_policy_popup("Require HTTPS Redirect")
        self.endpoint_security.click_add_policy_checkbox()
        self.endpoint_security.click_add_policy_popup_add_button()
        self.endpoint_security.click_policy_save_button()
        self.endpoint_security.click_are_you_sure_popup_save_button()
        self.endpoint_security.check_toast_successful_message("Policy has been saved successfully.")

    def test_23_verify_search_functionality_in_edit_policy_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635206
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()

        # Verify search functionality in edit policy screen
        self.endpoint_security.verify_policy_details_policy_settings_search("Require HTTPS Redirect")

    def test_24_verify_remove_policy_settings_in_edit_policy_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635212
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()

        # Remove added policy setting
        policy_settings_count = self.endpoint_security.get_policy_settings_count()
        self.endpoint_security.verify_policy_details_policy_settings_search("Require HTTPS Redirect")
        self.endpoint_security.click_remove_policy_settings_trash_button()
        self.endpoint_security.click_policy_save_button()
        self.endpoint_security.click_are_you_sure_popup_save_button()
        self.endpoint_security.check_toast_successful_message("Policy has been saved successfully.")
        self.endpoint_security.dismiss_toast()

        # Verify policy settings removed successfully
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()
        assert policy_settings_count-1 == self.endpoint_security.get_policy_settings_count()

    def test_25_verify_add_policy_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/720635210
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()

        # Select policy to add and then click cancel
        policy_settings_count = self.endpoint_security.get_policy_settings_count()
        self.endpoint_security.click_edit_policy_add_button()
        self.endpoint_security.search_policy_settings_in_add_policy_popup("Require HTTPS Redirect")
        self.endpoint_security.click_add_policy_checkbox()
        self.endpoint_security.click_edit_policy_screen_add_policy_popup_cancel_button()
        assert policy_settings_count == self.endpoint_security.get_policy_settings_count()

    def test_26_verify_add_policy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961407
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678961408
        self.endpoint_security.search_policy(policy_name)
        self.endpoint_security.click_policy_checkbox()
        self.endpoint_security.click_contextual_footer_select_action_dropdown()
        self.endpoint_security.select_action_dropdown_option("edit")
        self.endpoint_security.click_contextual_footer_continue_button()
        self.endpoint_security.click_edit_policy_add_button()

        # Verify add policy popup
        self.endpoint_security.verify_add_policy_pop_up()  
        self.endpoint_security.verify_add_policy_pop_up_title()
        self.endpoint_security.verify_add_policy_related_items()
        self.endpoint_security.verify_add_policy_cancel_button()
        self.endpoint_security.verify_add_policy_add_button()
        self.endpoint_security.verify_add_policy_popup_search_funtionality("Require HTTPS Redirect")
        self.endpoint_security.click_edit_policy_screen_add_policy_popup_cancel_button()
        self.endpoint_security.verify_add_policy_pop_up(displayed=False)

        # Removing the creaetd policy
        self.endpoint_security.click_policies_breadcrumb()
        self.endpoint_security.click_policies_tab()
        self.endpoint_security.remove_policy(policy_name)
        self.endpoint_security.check_toast_successful_message("Policy has been removed.")

    def test_27_verify_create_policy_basic_information_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959935
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959936
        self.endpoint_security.click_create_policy_button()

        # Verify create policy basic info screen
        self.endpoint_security.verify_create_policy_popup()
        self.endpoint_security.verify_create_policy_popup_title()
        self.endpoint_security.verify_basic_info_screen_step_title()
        self.endpoint_security.verify_basic_info_screen_step_description()
        self.endpoint_security.verify_basic_info_screen_policy_name_field()
        self.endpoint_security.verify_basic_info_screen_policy_name_field_error_msg()
        self.endpoint_security.verify_basic_info_screen_policy_settings_type_error_msg()
        self.endpoint_security.verify_basic_info_screen_note_field()
        self.endpoint_security.verify_create_policy_cancel_button()
        self.endpoint_security.enter_policy_name(policy_name)

        # Click on cancel button
        self.endpoint_security.click_create_policy_cancel_button()
        self.endpoint_security.verify_create_policy_popup(displayed=False)

        # Verify Policies screen is displayed
        self.endpoint_security.verify_page_title("Policies")

    def test_28_verify_create_policy_templates_and_attributes_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959937
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959939
        self.endpoint_security.click_create_policy_button()
        self.endpoint_security.enter_policy_name(policy_name)
        self.endpoint_security.select_policy_settings_type("Skip Template")
        self.endpoint_security.click_create_policy_next_button()

        # Verify create policy template and attributes screen
        self.endpoint_security.verify_create_policy_popup()
        self.endpoint_security.verify_create_policy_step2_title()
        self.endpoint_security.verify_create_policy_step2_description()
        self.endpoint_security.verify_create_policy_step2_related_items()
        self.endpoint_security.verify_add_policy_popup_search_funtionality("AirPrint")
        self.endpoint_security.verify_create_policy_next_button_status("disabled")

        # Click on cancel button
        self.endpoint_security.click_create_policy_cancel_button()
        self.endpoint_security.verify_create_policy_popup(displayed=False)

        # Verify Policies screen is displayed
        self.endpoint_security.verify_page_title("Policies")

    def test_29_verify_create_policy_set_options_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959942
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959944
        # https://hp-testrail.external.hp.com/index.php?/tests/view/678959943
        self.endpoint_security.click_create_policy_button()
        self.endpoint_security.enter_policy_name(policy_name)
        self.endpoint_security.select_policy_settings_type("Skip Template")
        self.endpoint_security.click_create_policy_next_button()
        self.endpoint_security.search_create_policy_settings("AirPrint")
        self.endpoint_security.click_select_policy_settings_checkbox()
        self.endpoint_security.verify_create_policy_next_button_status("enabled")
        self.endpoint_security.click_create_policy_next_button()

        # Verify create policy set options screen ui
        self.endpoint_security.verify_create_policy_popup()
        self.endpoint_security.verify_create_policy_step3_title()
        self.endpoint_security.verify_create_policy_step3_description()
        self.endpoint_security.search_create_policy_settings("AirPrint")
        self.endpoint_security.verify_create_policy_cancel_button()
        self.endpoint_security.verify_create_policy_back_button()
        self.endpoint_security.verify_create_policy_create_button()

        # Click on cancel button
        self.endpoint_security.click_create_policy_cancel_button()
        self.endpoint_security.verify_create_policy_popup(displayed=False)

        # Verify Policies screen is displayed
        self.endpoint_security.verify_page_title("Policies")
    
    def test_30_verify_column_option_popup_ui(self):
        # 
        expected_options= ["Policy Name","Status","Assigned To","Category","Modified By","Last Modified"]
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.verify_column_options_popup_title()
        self.endpoint_security.verify_column_options_popup_reset_to_default_button()
        self.endpoint_security.verify_column_options_popup_cancel_button()
        self.endpoint_security.verify_column_options_popup_save_button()
        assert expected_options == self.endpoint_security.get_column_options_popup_options()

    def test_31_verify_column_option_popup_save_button_functionality(self):
        # 
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.click_column_option("Category")
        self.endpoint_security.click_column_options_popup_save_button()

        # Verify Policies table Category Column
        self.endpoint_security.verify_policies_table_column("Category",displayed=False)

        # Reverting the Column option changes
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.click_column_option("Category")
        self.endpoint_security.click_column_options_popup_save_button()
        self.endpoint_security.verify_policies_table_column("Category")

    def test_32_verify_column_option_popup_cancel_button_functionality(self):
        # 
        self.endpoint_security.click_policies_column_options_gear_button()
        self.endpoint_security.click_column_option("Category")
        self.endpoint_security.click_column_options_popup_cancel_button()

        # Verify Policies table Category Column
        self.endpoint_security.verify_policies_table_column("Category")