import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_05_Workforce_Devices_Printers_Groups(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.printers_groups = self.fc.fd["printers_groups"]
        self.serial_number = request.config.getoption("--proxy-device")
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
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.printers.click_devices_printers_button()
        self.printers.click_printers_group("All")
        return self.printers.verify_devices_printers_table_loaded()  

    @pytest.mark.sanity
    def test_01_verify_printers_groups_ui(self):
        #
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.verify_groups_title()
        self.printers.verify_printers_manage_group_button()
        self.printers.verify_groups_all_group_title()
        self.printers.verify_groups_all_group_count()
        self.printers.verify_groups_all_group_expand_btn()  

    @pytest.mark.sanity
    def test_02_verify_groups_side_bar_expand_collapse_functionality(self):
        # 
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        self.printers.verify_groups_side_bar_collapse_btn()
        self.printers.verify_groups_title()
        
        self.printers.click_groups_side_bar_collapse_btn()
        self.printers.verify_groups_side_bar_expand_btn()
        self.printers.verify_groups_title(displayed=False)    

    @pytest.mark.sanity
    def test_03_verify_printers_move_to_group_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128883
        self.printers.click_printers_checkbox()
        self.printers.click_move_to_group_button()
       
        # Verify Remove From Group Pop-up
        self.printers.verify_move_to_group_popup_title()
        self.printers.verify_move_to_group_popup_description()
        self.printers.verify_move_to_group_popup_groups_to_move_field()
        self.printers.verify_move_to_group_popup_cancel_button()
        self.printers.verify_move_to_group_popup_move_button()
        self.printers.click_move_to_group_popup_cancel_button()      

    @pytest.mark.sanity
    def test_04_verify_manage_group_button_in_printers_page_ui(self):
        #
        # Verify "Manage group" button is displayed
        assert self.printers.verify_printers_manage_group_button(), "Manage Group button is not displayed"
        self.printers.click_printers_manage_group_button()
        # Verify Groups- Printers page navigation
        self.printers_groups.verify_groups_page_breadcrumb()
        self.printers_groups.verify_groups_printers_tab_title()
        self.printers_groups.verify_groups_printers_page_loaded()

    @pytest.mark.sanity
    def test_05_verify_groups_printers_tab_ui(self):
        #
        expected_table_headers = ['Group Name', 'Created On', 'Automated Rules', 'Assigned Printers', 'Assigned Policies']

        self.printers.click_printers_manage_group_button()
        # Verify Groups- Printers page UI
        self.printers_groups.verify_groups_printers_tab_title()
        self.printers_groups.verify_groups_printers_add_group_button()
        self.printers_groups.verify_groups_printers_table_column_option_gear_button()
        self.printers_groups.verify_page_size_btn()
        self.printers_groups.verify_page_nav()
        assert self.printers_groups.get_groups_printers_table_headers() == expected_table_headers, "Table headers do not match expected headers"

    @pytest.mark.sanity
    def test_06_verify_printers_groups_column_options_popup_ui(self):
        #
        expected_options= ["Group Name", "Created On", "Automated Rules", "Assigned Printers", "Assigned Policies"]
        self.printers.click_printers_manage_group_button()
        self.printers_groups.click_groups_printers_table_column_option_gear_button()
        self.printers_groups.verify_column_options_popup_title()
        self.printers_groups.verify_column_options_popup_reset_to_default_button()
        self.printers_groups.verify_column_options_popup_cancel_button()
        self.printers_groups.verify_column_options_popup_save_button()
        assert expected_options == self.printers_groups.get_column_options_popup_options()
    
    @pytest.mark.sanity
    def test_07_verify_printers_groups_column_option_popup_save_button_functionality(self):
        #
        self.printers.click_printers_manage_group_button()
        self.printers_groups.click_groups_printers_table_column_option_gear_button()
        self.printers_groups.click_column_option("Automated Rules")
        self.printers_groups.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.printers_groups.verify_groups_printers_table_loaded()
        self.printers_groups.verify_groups_printers_table_column("Automated Rules",displayed=False)

        #Reverting the Column option changes
        self.printers_groups.click_groups_printers_table_column_option_gear_button()
        self.printers_groups.click_column_option("Automated Rules")
        self.printers_groups.click_column_options_popup_save_button()
        self.printers_groups.verify_groups_printers_table_column("Automated Rules")

    @pytest.mark.sanity
    def test_08_verify_printers_groups_column_option_popup_reset_to_default_button_functionality(self):
        #
        self.printers.click_printers_manage_group_button()
        self.printers_groups.click_groups_printers_table_column_option_gear_button()
        self.printers_groups.click_column_option("Automated Rules")
        self.printers_groups.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.printers_groups.verify_groups_printers_table_loaded()
        self.printers_groups.verify_groups_printers_table_column("Automated Rules",displayed=False)

        # Verify Reset to default button functionality
        self.printers_groups.click_groups_printers_table_column_option_gear_button()
        self.printers_groups.click_column_options_popup_reset_to_default_button()
        self.printers_groups.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.printers_groups.verify_groups_printers_table_loaded()
        self.printers_groups.verify_groups_printers_table_column("Automated Rules")

    @pytest.mark.sanity
    def test_09_verify_column_option_popup_cancel_button_functionality(self):
        #
        self.printers.click_printers_manage_group_button()
        self.printers_groups.click_groups_printers_table_column_option_gear_button()
        self.printers_groups.click_column_option("Automated Rules")
        self.printers_groups.click_column_options_popup_cancel_button()

        # Verify Customers table Domain Column
        self.printers_groups.verify_groups_printers_table_loaded()
        self.printers_groups.verify_groups_printers_table_column("Automated Rules")

    def test_10_verify_printer_groups_pagination(self):
        #
        self.printers.click_printers_manage_group_button()
        self.printers.verify_all_page_size_options([5, 25, 50, 100])
        self.printers.verify_table_displaying_correctly(5, page=1)
        self.printers.verify_table_displaying_correctly(25, page=1)
        self.printers.verify_table_displaying_correctly(50, page=1)
        self.printers.verify_table_displaying_correctly(100, page=1)

    @pytest.mark.sanity
    def test_11_verify_add_printer_group_functionality_without_rules(self):
        #
        self.printers.click_printers_manage_group_button()
        sleep(5)
        self.printers_groups.click_groups_printers_add_group_button()

        # Enter group name and description
        self.printers_groups.enter_group_name(group_name)
        self.printers_groups.enter_group_description("Test group without rules")

        # Uncheck the 'Add group rules' checkbox if it is checked
        self.printers_groups.click_add_group_rules_checkbox()
        self.printers_groups.click_add_groups_next_button()

        # # Verify toast notification message
        # assert f'Printer group "{group_name}" created' == self.printers_groups.verify_add_groups_toast_message(), "Toast notification for group creation not displayed"

        # close the toast notification if any
        self.printers.dismiss_toast()

        # Optionally, verify group creation success
        assert self.printers_groups.verify_group_name(group_name), "Group was not created successfully without rules"

    @pytest.mark.sanity
    def test_12_verify_remove_printer_group_functionality(self):
        #
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

    @pytest.mark.sanity
    @pytest.mark.parametrize('operator_name', ["Equals", "Starts with", "Contains"])
    def test_13_verify_add_printer_group_functionality_with_rules_model_name_property(self,operator_name):
        #
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
        # Navigate to "Ungrouped" group
        self.printers.click_printers_group("Ungrouped")
        
        # Verify table is loaded and not empty
        self.printers.verify_devices_printers_table_loaded()
    
        # Collect first row printer model name
        first_row_model_name = self.printers.get_all_printers_model_name_from_the_group()[0]
        first_row_model_name = first_row_model_name.strip()

        if operator_name in ["Starts with"]:
            first_row_model_name = first_row_model_name[:8]  # Take first 8 characters for 'Starts with' operator
        elif operator_name in ["Contains"]:
            # Take middle portion of model name for 'Contains' operator
            if len(first_row_model_name) > 6:
                start_pos = len(first_row_model_name) // 4
                first_row_model_name = first_row_model_name[start_pos:start_pos + 6]

        # Search and collect how many printers are present with same model name
        self.printers.search_printers(first_row_model_name)
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_search_results_with_model_name(first_row_model_name)
        printers_with_same_model_name_count = self.printers.get_printers_table_count()
        # Get printers detail info
        entry_detail = self.printers.get_printers_detail_info()
        
        # For "Isn't equal to", we need to know total printers to calculate expected count
        if operator_name == "Isn't equal to":
            # Clear search and get all ungrouped printers count
            self.printers.click_search_clear_button()
            self.printers.verify_devices_printers_table_loaded()
            total_ungrouped_printers_count = self.printers.get_printers_table_count()
            expected_printers_count = total_ungrouped_printers_count - printers_with_same_model_name_count
        else:
            expected_printers_count = printers_with_same_model_name_count
        
        self.printers.click_printers_manage_group_button()
        sleep(5)
        self.printers_groups.click_groups_printers_add_group_button()

        # Enter group name and description
        self.printers_groups.enter_group_name(group_name)
        self.printers_groups.enter_group_description("Test group with rules- Model Name")

        # Check the 'Add group rules' checkbox if it is unchecked
        self.printers_groups.click_add_groups_next_button()

        self.printers_groups.verify_create_printer_group_rule_page()
        self.printers_groups.click_create_printer_group_rule_page_property_dropdown()
        self.printers_groups.select_create_printer_group_rule_page_property("Model.name")
        self.printers_groups.click_create_printer_group_rule_page_opertor_dropdown()
        self.printers_groups.select_create_printer_group_rule_page_operator(operator_name)
        self.printers_groups.click_create_printer_group_rule_page_value_dropdown()
        
        if operator_name in ["Isn't equal to","Equals"]:
            self.printers_groups.click_create_printer_group_rule_page_value_option(first_row_model_name)
        else:
            self.printers_groups.enter_create_printer_group_rule_page_value(first_row_model_name)

        self.printers_groups.click_create_printer_group_rule_page_next_button()

        self.printers_groups.verify_create_printer_group_review_page()
        #####
        group_rules = 1
        self.printers_groups.click_create_printer_group_review_page_create_button()
    
        # # Verify toast notification message
        # assert f'Printer group "{group_name}" created' == self.printers_groups.verify_add_groups_toast_message(), "Toast notification for group creation not displayed"

        # close the toast notification if any
        self.printers.dismiss_toast()

        # Optionally, verify group creation success
        assert self.printers_groups.verify_group_name(group_name), "Group was not created successfully with rules"
        sleep(10)
        self.printers_groups.select_group_by_name(group_name)

        #Verify assigned printers count and details in group details - Overview tab
        self.printers_groups.verify_printers_groups_details_page()
        self.printers_groups.verify_printer_groups_details_page_group_title(group_name)
        self.printers_groups.verify_printer_groups_details_page_overview_tab()
        assert group_name == self.printers_groups.get_printer_groups_details_page_group_name(), "Group name mismatch in details page"
        assert group_rules == self.printers_groups.get_printer_groups_details_page_group_rules(), "Group rules count mismatch"
        assert expected_printers_count == self.printers_groups.get_printer_groups_details_page_assigned_printers_count(), "Assigned printers count mismatch"
        assert "Test group with rules- Model Name" == self.printers_groups.get_printer_groups_details_page_group_description(), "Group description mismatch"

        # Verify assigned printers details in group details - Rules and Printers tab
        self.printers_groups.click_printer_groups_details_page_rules_and_printers_tab()
        self.printers_groups.verify_printer_groups_details_page_rules_and_printers_tab()
        self.printers_groups.click_printer_groups_details_page_refresh_button()
        sleep(10)
        self.printers_groups.verify_group_rules_table_loaded()
        assert self.printers_groups.get_property_name_in_group_rules_table() == ['Model Name']
        # Normalize apostrophe characters (smart/curly quotes to straight quotes) for comparison
        ui_operators = self.printers_groups.get_operator_in_group_rules_table()
        ui_operator = ui_operators[0].replace('\u2019', "'").replace('\u2018', "'")  # Replace curly quotes with straight
        normalized_operator_name = operator_name.replace('\u2019', "'").replace('\u2018', "'")
        assert ui_operator == normalized_operator_name, f"Operator mismatch: expected '{normalized_operator_name}', got '{ui_operator}'"
        assert self.printers_groups.get_value_in_group_rules_table() == [first_row_model_name]
        self.printers_groups.click_printer_groups_details_page_refresh_button()
        sleep(30)
        # Verify entry_detail printers are present/absent in the group based on operator
        self.printers_groups.verify_groups_assigned_printers_table_loaded()
        group_page_printers_detail = self.printers_groups.get_groups_page_printers_detail_info()

        if operator_name == "Isn't equal to":
            # For "Isn't equal to", verify printers with the model name are NOT in the group
            for printer in entry_detail:
                found = False
                for group_printer in group_page_printers_detail:
                    common_keys = set(printer.keys()) & set(group_printer.keys())
                    if all(printer.get(key) == group_printer.get(key) for key in common_keys):
                        found = True
                        break
                assert not found, f"Printer {printer.get('serial_number')} with model '{first_row_model_name}' should NOT be in group for 'Isn't equal to' operator"
        else:
            # For other operators, verify printers ARE in the group
            for printer in entry_detail:
                found = False
                for group_printer in group_page_printers_detail:
                    common_keys = set(printer.keys()) & set(group_printer.keys())
                    if all(printer.get(key) == group_printer.get(key) for key in common_keys):
                        found = True
                        break
                assert found, f"Printer {printer.get('serial_number')} from original search not found in group details page"
                
        # Navigate back to devices -> printers page
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        
        # Verify the new group name is present in the groups sidebar
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() is False:
            self.printers.click_groups_side_bar_expand_btn()
        sleep(30)
        assert self.printers.verify_group_name(group_name), f"Group '{group_name}' not found in groups sidebar"
        self.printers.click_printers_group(group_name)
        self.printers.verify_devices_printers_table_loaded()

        self.printers.click_devices_printers_page_refresh_button()
        self.printers.verify_devices_printers_table_loaded()
        sleep(20)
        
        # Verify all the printers are present with all columns in the new group on printers page
        new_group_printers_detail_full = self.printers.get_printers_detail_info()
        
        if operator_name == "Isn't equal to":
            # For "Isn't equal to", verify printers with the model name are NOT in the group
            for printer in entry_detail:
                found = False
                for group_printer in new_group_printers_detail_full:
                    if all(printer.get(key) == group_printer.get(key) for key in printer.keys() if key != 'group'):
                        found = True
                        break
                assert not found, f"Printer {printer.get('serial_number')} with model '{first_row_model_name}' should NOT be in group for 'Isn't equal to' operator"
        else:
            # For other operators, verify printers ARE in the group
            for printer in entry_detail:
                found = False
                for group_printer in new_group_printers_detail_full:
                    # Compare all keys from original entry_detail except 'group'
                    if all(printer.get(key) == group_printer.get(key) for key in printer.keys() if key != 'group'):
                        # Verify the group field has changed to the new group
                        assert group_printer.get('group') == group_name, f"Printer {printer.get('serial_number')} group not updated to '{group_name}'. Got: '{group_printer.get('group')}'"
                        found = True
                        break
        for printer in entry_detail:
            found = False
            for group_printer in new_group_printers_detail_full:
                # Compare all keys from original entry_detail except 'group'
                if all(printer.get(key) == group_printer.get(key) for key in printer.keys() if key != 'group'):
                    # Verify the group field has changed to the new group
                    assert group_printer.get('group') == group_name, f"Printer {printer.get('serial_number')} group not updated to '{group_name}'. Got: '{group_printer.get('group')}'"
                    found = True
                    break
            assert found, f"Printer {printer.get('serial_number')} from original search not found in group on printers page"

        #remove the created group to clean up
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