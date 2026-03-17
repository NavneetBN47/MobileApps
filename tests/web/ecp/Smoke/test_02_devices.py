import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import random
pytest.app_info = "ECP"

#Generate test group name
group_name="auto_test"+str(random.randint(100,999))

class Test_02_ECP_Devices_List(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_devices(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        # self.devices.click_devices_group_all_option("All groups")
        sleep(5) #wait for the devices page to load
        return self.devices.verify_device_page()

    def test_01_verify_pagination(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29136330
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29136323
        self.devices.verify_all_page_size_options_new([5,25, 50, 100, 500])
        self.devices.verify_table_displaying_correctly_new(5, page=1)
        self.devices.verify_table_displaying_correctly_new(25, page=1)
        self.devices.verify_table_displaying_correctly_new(50, page=1)
        self.devices.verify_table_displaying_correctly_new(100, page=1)
        self.devices.verify_table_displaying_correctly_new(500, page=1)
     
    def test_02_verify_refresh(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092858
        cur_time = self.devices.get_sync_time_info()
        sleep(1)
        self.devices.click_refresh_button()
        new_time = self.devices.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def test_03_verify_hero_flow_search(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092859
        self.devices.search_device("HP ")
        self.devices.verify_device_page()
        self.devices.verify_search_results("HP")

    def test_04_verify_error_case_search(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093896
        self.devices.search_device("InvalidData")
        self.devices.verify_no_items_found()
    
    def test_05_verify_export_functionality(self):
        self.devices.export_devices()

    def test_06_verify_devices_details(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29133139
        entry_detail = self.devices.get_devices_detail_info()
        self.devices.click_first_entry_link()
        assert entry_detail == self.devices.verify_devices_details()

    def test_07_verify_device_view_details(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29133164
        #entry_detail = self.devices.get_devices_detail_info() # Solution Device tab got removed from the UI, so commenting this line
        self.devices.click_first_entry_link()
        # entry_detail["assessment_status"] = self.devices.get_security_risk_detail()
        self.devices.click_device_details_view_link()
        
        #verify_navigated_device_details_page
        self.devices.verify_navigated_tab("fleetmanager-tab") # Testcase is faling due to an application issue
        # assert entry_detail == self.devices.verify_devices_details_list_synced_with_device_screen()

    def test_08_verify_device_page_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29133476
        self.devices.verify_page_title("Devices")

        # All Devices Tab is removed as part of 0.45
        # self.devices.verify_all_devices_tab()

        self.devices.verify_refresh_btn()
        self.devices.verify_search_device_name_txtbox()
        self.devices.verify_device_export_btn()
        self.devices.verify_page_size_btn()

    def test_09_verify_export_devices_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324463
        self.devices.click_device_export_btn()
        self.devices.verify_export_devices_popup_title()
        self.devices.verify_export_devices_popup_description()
        self.devices.verify_export_devices_popup_select_file_type_dropdown()
        self.devices.verify_export_devices_popup_cancel_button()
        self.devices.verify_export_devices_popup_export_button()
        self.devices.click_export_devices_popup_cancel_button()

    def test_10_verify_export_devices_popup_select_file_type_dropdown_option(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324463
        file_type_option="CSV"
        self.devices.click_device_export_btn()
        self.devices.click_export_devices_popup_select_file_type_dropdown()
        logging.info(self.devices.get_select_file_type_dropdown_options())
        assert file_type_option == self.devices.get_select_file_type_dropdown_options()

    def test_11_verify_devices_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324485
        self.devices.click_devices_checkbox()
        self.devices.verify_contextual_footer()
        self.devices.verify_contextual_footer_cancel_button()
        self.devices.verify_contextual_footer_selected_item_label()
        self.devices.verify_contextual_footer_select_action_dropdown()
        self.devices.verify_contextual_footer_continue_button()

    def test_12_verify_devices_contextual_footer_select_action_dropdown_options(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324485
        expected_options=["Move to Group","Configure Device"]
        self.devices.click_devices_checkbox()
        self.devices.verify_contextual_footer()
        self.devices.click_contextual_footer_select_action_dropdown()
        assert expected_options == self.devices.get_contextual_footer_select_action_dropdown_options()

    def test_13_verify_devices_contextual_footer_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324485
        self.devices.click_devices_checkbox()
        self.devices.click_contextual_footer_select_action_dropdown()
        self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
        self.devices.click_contextual_footer_cancel_button()
        self.devices.verify_contextual_footer_is_not_displayed()

    def test_14_verify_devices_move_to_group_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324491
        self.devices.click_devices_checkbox()
        self.devices.click_contextual_footer_select_action_dropdown()
        self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
        self.devices.click_contextual_footer_continue_button()
       
        # Verify Remove From Group Pop-up
        self.devices.verify_move_to_group_popup_title()
        self.devices.verify_move_to_group_popup_description()
        self.devices.verify_move_to_group_popup_groups_to_move_field()
        self.devices.verify_move_to_group_popup_cancel_button()
        self.devices.verify_move_to_group_popup_move_button()
        self.devices.click_move_to_group_popup_cancel_button()

    # def test_15_verify_create_group_popup_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324431
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_create_group_button()
    #     self.devices.verify_create_group_popup_title()
    #     self.devices.verify_create_group_popup_description()
    #     self.devices.verify_create_group_popup_group_name_field()
    #     # self.devices.verify_create_group_popup_parent_group_field() # Parent Group is removed from the UI
    #     self.devices.verify_create_group_popup_cancel_button()
    #     self.devices.verify_create_group_popup_create_button()
    #     self.devices.click_create_group_popup_cancel_button()

    def test_16_verify_column_option_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30324464
        expected_options = [
        "Serial Number", "Model Name", "Device Status Message", "Connectivity", "Last Synced", "Group", 
        "Policies", "Policy Date Run", "Security Assessment", "Policy Compliance", "Firmware Version", "Location", 
        "Connectivity Types", "Device Name", "Date Added", "Wired (IPv4 Address)", "Asset Number", "Manufacturer", 
        "Apps", "Wired (IPv6 Address)", "Wired (MAC Address)", "Wired (Hostname)", "Wireless (IPv4 Address)", 
        "Wireless (IPv6 Address)", "Wireless (MAC Address)", "Wireless (Hostname)", "Wi-Fi Direct (IPv4 Address)", 
        "Wi-Fi Direct (IPv6 Address)", "Wi-Fi Direct (MAC Address)", "Wi-Fi Direct (Hostname)", "Status", "Status Updated"]
        self.devices.click_devices_column_option_settings_gear_button()
        self.devices.verify_column_options_popup_title()
        self.devices.verify_column_options_popup_reset_to_default_button()
        self.devices.verify_column_options_popup_cancel_button()
        self.devices.verify_column_options_popup_save_button()
        assert expected_options == self.devices.get_column_options_popup_options()

    def test_17_verify_column_option_popup_save_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30772653
        self.devices.click_devices_column_option_settings_gear_button()
        self.devices.click_column_option("Connectivity")
        self.devices.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.devices.verify_devices_tabel_column("Connectivity",displayed=False)

        # Reverting the Column option changes
        self.devices.click_devices_column_option_settings_gear_button()
        self.devices.click_column_option("Connectivity")
        self.devices.click_column_options_popup_save_button()
        self.devices.verify_devices_tabel_column("Connectivity")

    def test_18_verify_column_option_popup_cancel_button_functionality(self):
        # 
        self.devices.click_devices_column_option_settings_gear_button()
        self.devices.click_column_option("Connectivity")
        self.devices.click_column_options_popup_cancel_button()

        # Verify Customers table Domain Column
        self.devices.verify_devices_tabel_column("Connectivity")

    # def test_19_verify_devices_edit_group_popup_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324443
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.verify_edit_group_popup_title()
    #     self.devices.verify_edit_group_popup_description()
    #     self.devices.verify_edit_group_popup_delete_button()
    #     self.devices.verify_edit_group_popup_create_tab()
    #     self.devices.verify_edit_group_popup_rename_tab()
    #     self.devices.verify_edit_group_popup_close_button()
    #     self.devices.click_edit_group_popup_close_button()

    # def test_20_verify_devices_edit_group_popup_create_tab_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324443
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.verify_edit_group_popup_create_tab_description()
    #     self.devices.verify_edit_group_popup_create_tab_group_name_label()
    #     self.devices.verify_edit_group_popup_create_tab_group_name_field()
    #     # self.devices.verify_edit_group_popup_create_tab_parebnt_group_label()
    #     # self.devices.verify_edit_group_popup_create_tab_parebnt_group_dropdown()
    #     self.devices.verify_edit_group_popup_create_tab_create_button()

    # def test_21_verify_devices_edit_group_popup_rename_tab_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324454
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_rename_tab()
    #     self.devices.verify_edit_group_popup_rename_tab_description()
    #     self.devices.verify_edit_group_popup_rename_tab_group_name_label()
    #     self.devices.verify_edit_group_popup_rename_tab_group_name_field()
    #     self.devices.verify_edit_group_popup_rename_tab_rename_button()

    # def test_22_verify_create_group_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324447
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_create_group_button()
    #     self.devices.enter_group_name(group_name)
    #     # self.devices.select_parent_group() # Parent Group is removed from the UI
    #     self.devices.click_create_group_popup_create_button()

    #     # Verify the newly created group is displayed in Groups section
    #     self.devices.verify_group_name(group_name)

    # def test_23_verify_devices_edit_group_popup_rename_tab_validation(self):
    #     # 
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_rename_tab()
    #     self.devices.verify_select_group_warning_message()
    #     self.devices.verify_edit_group_popup_rename_tab_rename_button_is_disabled()
    #     self.devices.click_edit_group_popup_group_name(group_name)
    #     self.devices.verify_select_group_warning_message(displayed=False)
    #     self.devices.verify_edit_group_popup_rename_tab_group_name_textbox_status("enabled")

    # def test_24_verify_delete_group_popup_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30772609
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_group_name(group_name)
    #     self.devices.click_edit_group_popup_delete_button()

    #     # Verify Delete Popup UI
    #     self.devices.verify_delete_group_popup_title()
    #     self.devices.verify_delete_group_popup_description()
    #     self.devices.verify_delete_group_popup_cancel_button()
    #     self.devices.verify_delete_group_popup_delete_button()
    #     self.devices.click_delete_group_popup_cancel_button()

    # def test_25_verify_rename_group_name_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324456
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_group_name(group_name)
    #     self.devices.click_edit_group_popup_rename_tab()
    #     self.devices.edit_group_popup_enter_group_name("update_"+group_name)
    #     self.devices.click_edit_group_popup_rename_tab_rename_button()
    #     self.devices.verify_edit_group_popup_close_button()
    #     self.devices.click_edit_group_popup_close_button()

    #     # Verify group name is Renamed
    #     self.devices.verify_group_name("update_"+group_name)

    #     # Reverting the changes
    #     self.devices.dismiss_toast()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_group_name("update_"+group_name)
    #     self.devices.click_edit_group_popup_rename_tab()
    #     self.devices.edit_group_popup_enter_group_name(group_name)
    #     self.devices.click_edit_group_popup_rename_tab_rename_button()

    #     # Verify group name is Renamed
    #     self.devices.verify_group_name(group_name)

    # def test_26_verify_devices_move_to_group_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324491
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     group_device_count=self.devices.get_device_count(group_name)
    #     device_serial_number=self.devices.get_device_serial_number()
    #     self.devices.click_devices_checkbox()
    #     self.devices.click_contextual_footer_select_action_dropdown()
    #     self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
    #     self.devices.click_contextual_footer_continue_button()
    #     self.devices.select_group(group_name)
    #     self.devices.click_move_to_group_popup_move_button()

    #     # Verify The Group Count and Serial numbner After moving device to it
    #     self.devices.click_devices_group(group_name)
    #     assert group_device_count+1 == self.devices.get_device_count(group_name)
    #     assert device_serial_number == self.devices.get_device_serial_number()
    
    # def test_27_verify_devices_remove_from_group_popup_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324495
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_group(group_name)
    #     self.devices.click_devices_checkbox()
    #     self.devices.click_contextual_footer_select_action_dropdown()
    #     self.devices.select_contextual_footer_select_action_dropdown_option("Remove from group")
    #     self.devices.click_contextual_footer_continue_button()
       
    #     # Verify Remove From Group Pop-up
    #     self.devices.verify_remove_from_group_popup_title()
    #     self.devices.verify_remove_from_group_popup_description()
    #     self.devices.verify_remove_from_group_popup_cancel_button()
    #     self.devices.verify_remove_from_group_popup_remove_button()
    #     self.devices.click_remove_from_group_popup_cancel_button()

    # def test_28_verify_devices_remove_from_group_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324495
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     group_device_count=self.devices.get_device_count(group_name)
    #     self.devices.click_devices_group(group_name)
    #     self.devices.click_devices_checkbox()
    #     self.devices.click_contextual_footer_select_action_dropdown()
    #     self.devices.select_contextual_footer_select_action_dropdown_option("Remove from group")
    #     self.devices.click_contextual_footer_continue_button()
    #     self.devices.click_remove_from_group_popup_remove_button()
    #     sleep(5) # Wait for the page to load the device table

    #     # Verify The Group Count After removing device from that group
    #     assert group_device_count-1 == self.devices.get_device_count(group_name)

    # def test_29_verify_delete_group_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30772609
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_group_name(group_name)
    #     self.devices.click_edit_group_popup_delete_button()
    #     self.devices.click_delete_group_popup_delete_button()
    #     self.devices.click_edit_group_popup_close_button()

    #     # verify the deleted group name, should not display under Groups
    #     self.devices.verify_group_name(group_name,displayed=False)

    # def test_30_verify_create_group_functionality_in_edit_group_popup(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30324444
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.enter_edit_group_popup_create_tab_group_name(group_name)
    #     self.devices.click_edit_group_popup_create_tab_create_button()
    #     self.devices.verify_edit_group_popup_close_button()
    #     self.devices.click_edit_group_popup_close_button()

    #     # Verify the newly created group is displayed in Groups section
    #     self.devices.verify_group_name(group_name)

    #     # Delete the created Group
    #     self.devices.dismiss_toast()
    #     self.devices.click_devices_edit_group_button()
    #     self.devices.click_edit_group_popup_group_name(group_name)
    #     self.devices.click_edit_group_popup_delete_button()
    #     self.devices.click_delete_group_popup_delete_button()
    #     self.devices.click_edit_group_popup_close_button()

    #     # verify the deleted group name, should not display under Groups
    #     self.devices.verify_group_name(group_name,displayed=False)

    # def test_31_verify_remove_from_group_option_disabled_for_all_and_ungrouped_group(self):
    #     # 
    #     if self.devices.verify_groups_side_bar_collapse_button_is_displayed() == False:
    #         self.devices.click_groups_side_bar_expand_btn()
    #     self.devices.click_devices_checkbox()
    #     self.devices.click_contextual_footer_select_action_dropdown()
    #     self.devices.verify_remove_from_group_option_status("disabled")
    #     self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
    #     self.devices.click_contextual_footer_cancel_button()
        
    #     # Check for Ungrouped Group
    #     self.devices.click_devices_group("Ungrouped")
    #     self.devices.click_devices_checkbox()
    #     self.devices.click_contextual_footer_select_action_dropdown()
    #     self.devices.verify_remove_from_group_option_status("disabled")
    #     self.devices.select_contextual_footer_select_action_dropdown_option("Move to group")
    #     self.devices.click_contextual_footer_cancel_button()