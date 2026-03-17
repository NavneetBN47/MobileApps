import pytest
import random
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

#Generate test group name
# group_name="auto_test"+str(random.randint(100,999))

class Test_02_Workforce_Devices_Printers_Groups(object):

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
        self.serial_number = request.config.getoption("--proxy-device")
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

    def test_01_verify_search_field_default_text_based_on_group_selection(self):
        #
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()

        # Verify the default search field text
        self.printers.verify_printers_search_txtbox_text("All")
        
        # Retrieve all available group names dynamically
        group_names = self.printers.get_all_printer_group_names()
        
        # Iterate over each group name and verify the search field default text
        for group_name in group_names:
            self.printers.click_printers_group(group_name)
            self.printers.verify_printers_search_txtbox_text(group_name)

    def test_02_verify_groups_section_displays_all_printer_groups_with_correct_counts(self):
       
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
 
        # Retrieve all group names and their displayed counts from the UI
        group_names, group_counts = self.printers.get_all_printer_groups_with_counts()
        assert group_names and group_counts, "No groups found in the Groups section."
 
        # Optionally, verify that the sum of all group counts matches the total number of printers
        total_printers = self.printers.get_groups_all_group_count()
        sum_of_group_counts = sum(group_counts)
        assert sum_of_group_counts == total_printers, (
            f"Sum of group counts ({sum_of_group_counts}) doesn't match the total printers ({total_printers})"
        )
 
    def test_03_verify_all_groups_display_correct_printer_counts(self):
        """
        Verify the all groups count with total number of printers displayed in the table.
        """
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
 
        # Retrieve all group names and their displayed counts from the UI
        all_group_count = self.printers.get_groups_all_group_count()
        total_printers_in_table = self.printers.get_printers_table_count()
        assert all_group_count == total_printers_in_table, (
            f"'All' group count ({all_group_count}) doesn't match the total printers in table ({total_printers_in_table})"
        )
   
    def test_04_verify_clicking_group_shows_only_selected_group_printers(self):
        #
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()
 
        group_names = self.printers.get_all_printer_group_names()
        assert group_names, "No custom groups found to test."
 
        self.printers.verify_selected_group_printers(group_names)

    @pytest.mark.skip(reason="Skipping test case temporarily")
    def test_05_verify_multiple_printers_move_and_remove_to_group_functionality(self):
        #
        # Ensure groups side bar is expanded
        if self.printers.verify_groups_side_bar_collapse_button_is_displayed() == False:
            self.printers.click_groups_side_bar_expand_btn()

        # Create a new group named "testing"
        self.printers.click_printers_create_group_button()
        self.printers.enter_group_name(group_name)
        self.printers.click_create_group_popup_create_button()
        # Verify the newly created group is displayed in Groups section
        self.printers.verify_group_name(group_name)

        # Select "Ungrouped" group
        self.printers.click_printers_group("Ungrouped")
        self.printers.verify_devices_printers_table_loaded()
        ungrouped_printers = self.printers.get_all_printers_serial_number()
        assert ungrouped_printers, "No printers found in 'Ungrouped' group to move."

        # Click all printers checkbox
        self.printers.click_all_printers_checkbox()

        # From floating menu, click on move to group option
        self.printers.click_move_to_group_button()

        # From move to group popup, move the selected devices to "testing" group
        self.printers.select_group(group_name)
        self.printers.click_move_to_group_popup_move_button()
        sleep(5) #adding sleep so that table could load with printer 

        # Verify if the devices are moved to the group
        self.printers.click_printers_group(group_name)
        self.printers.click_devices_printers_page_refresh_button()
        self.printers.verify_devices_printers_table_loaded()
        new_group_printers = self.printers.get_all_printers_serial_number()
        for printer in ungrouped_printers:
            assert printer in new_group_printers, f"Printer '{printer}' was not moved to {group_name} group."

        #remove all the printers from newly created group
        self.printers.click_printers_group(group_name)
        group_printer_count=self.printers.get_printer_count(group_name)
        ungrouped_printer_count=self.printers.get_printer_count("Ungrouped")
        self.printers.verify_devices_printers_table_loaded()
        self.printers.click_all_printers_checkbox()
        self.printers.click_contextual_footer_select_action_dropdown()
        self.printers.select_contextual_footer_select_action_dropdown_option("Remove from group")
        self.printers.click_contextual_footer_continue_button()
        self.printers.click_remove_from_group_popup_remove_button()

        # Verify The Group Count After removing printer from that group
        sleep(5)
        assert ungrouped_printer_count == self.printers.get_printer_count(group_name)
        #Verify the printers are moved to ungrouped group
        assert group_printer_count == self.printers.get_printer_count("Ungrouped")

        # Delete the newly created group
        self.printers.click_printers_edit_groups_button()
        self.printers.click_edit_groups_popup_group_name(group_name)
        self.printers.click_edit_groups_popup_delete_button()
        self.printers.click_delete_group_popup_delete_button()
        self.printers.dismiss_toast()
        self.printers.click_edit_groups_popup_close_button()

        # verify the deleted group name, should not display under Groups
        self.printers.verify_group_name(group_name,displayed=False)