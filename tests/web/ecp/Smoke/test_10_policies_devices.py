import pytest
from SAF.misc import saf_misc
from time import sleep
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "ECP"

class Test_10_ECP_Policies_Devices(object):

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
        self.customer = self.account["customer"]
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_policies_devices(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        return self.home.click_policies_menu_btn()
        # Commenting because policy devices has been removed from the UI
        # self.endpoint_security.click_policies_devices_tab()
        # return self.endpoint_security.verify_policies_devices_page()

    #Policy Devices tab has been removed from the UI So skipping the below testcases
    @pytest.mark.skip
    def test_01_verify_policies_devices_page_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274735
        self.endpoint_security.verify_policies_devices_refresh_btn()
        self.endpoint_security.verify_policies_devices_search_device_name_txtbox()
        self.endpoint_security.verify_page_size_btn()
        self.endpoint_security.verify_policies_devices_column_option_gear_button()
        self.endpoint_security.verify_policies_devices_groups_title()
    
    @pytest.mark.skip
    def test_02_verify_policies_devices_pagination(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274741
        self.endpoint_security.verify_all_page_size_options_new([5,25, 50, 100, 500])
        self.endpoint_security.verify_table_displaying_correctly_new(5, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(25, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(50, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(100, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(500, page=1)

    @pytest.mark.skip 
    def test_03_verify_policy_devices_refresh_button(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274743
        cur_time = self.endpoint_security.get_sync_time_info()
        sleep(1)
        self.endpoint_security.click_refresh_button()
        new_time = self.endpoint_security.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    @pytest.mark.skip
    def test_04_verify_hero_flow_search(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274736
        self.endpoint_security.search_device("HP ")
        self.endpoint_security.verify_policies_devices_page()
        self.endpoint_security.verify_search_results("HP")

    @pytest.mark.skip
    def test_05_verify_error_case_search(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274736
        self.endpoint_security.search_device("InvalidData")
        self.endpoint_security.verify_no_items_found()

    @pytest.mark.skip
    def test_06_verify_policies_devices_tab_match_with_global_device_tab(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274744
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274755
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.click_groups_side_bar_expand_btn()

        # get global devices group names and their device counts
        global_device_all_group_count=self.devices.get_device_count("All")
        global_device_group_details=dict(zip(self.devices.get_group_names(), self.devices.get_group_counts()))

        # get Policies-->Devices tab devices group names and their device counts
        self.home.click_policies_menu_btn()
        self.endpoint_security.click_policies_devices_tab()
        self.endpoint_security.verify_policies_devices_page()

        assert global_device_all_group_count == self.devices.get_device_count("All")
        policies_device_group_details=dict(zip(self.endpoint_security.get_group_names(), self.endpoint_security.get_group_counts()))
        assert global_device_group_details == policies_device_group_details

    @pytest.mark.skip
    def test_07_verify_sort_order(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274738

        #verify_default_sort
        self.endpoint_security.verify_policies_devices_table_sort("compliance",["Noncompliant","Compliant","Unknown"])
    
        ##verify_sort_order_change
        self.endpoint_security.click_table_header_by_name("compliance")
        self.endpoint_security.verify_policies_devices_page()
        self.endpoint_security.verify_policies_devices_table_sort("compliance",["Unknown","Compliant","Noncompliant"])
    
    @pytest.mark.skip
    def test_08_verify_column_option_popup_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274742
        expected_options= ["Model Name", "Compliance","Serial Number","Policy","Last Run"]
        self.endpoint_security.click_policies_devices_column_option_gear_button()
        self.endpoint_security.verify_policies_devices_column_options_popup_title()
        self.endpoint_security.verify_policies_devices_column_options_popup_reset_to_default_button()
        self.endpoint_security.verify_policies_devices_column_options_popup_cancel_button()
        self.endpoint_security.verify_policies_devices_column_options_popup_save_button()
        assert expected_options == self.endpoint_security.get_policies_devices_column_options_popup_options()
    
    @pytest.mark.skip
    def test_09_verify_devices_details_page(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274745
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274751
        self.endpoint_security.search_device("HP ")
        entry_detail = self.endpoint_security.get_policies_devices_detail_info()
        self.endpoint_security.click_first_entry_link()
        assert entry_detail == self.endpoint_security.verify_devices_details_list_synced_with_policies_device_tab()

    @pytest.mark.skip
    def test_10_verify_policy_devices_details_refresh_button(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274750
        self.endpoint_security.search_device("HP ")
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.verify_policies_devices_detail_loaded()

        cur_time = self.endpoint_security.get_sync_time_info()
        sleep(1)
        self.endpoint_security.click_refresh_button()
        new_time = self.endpoint_security.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    @pytest.mark.skip
    def test_11_verify_basic_info_card_can_be_expanded_and_collapsed(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274752
        self.endpoint_security.search_device("HP ")
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.verify_policies_devices_detail_loaded()
        self.endpoint_security.verify_policy_device_details_basic_info_card()
        self.endpoint_security.click_policy_device_details_basic_info_card()
        self.endpoint_security.verify_policy_device_details_basic_info_card(expanded=False)
        self.endpoint_security.click_policy_device_details_basic_info_card()
        self.endpoint_security.verify_policy_device_details_basic_info_card()
    
    def test_12_verify_compliance_status_card_can_be_expanded_and_collapsed(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274746
        #https://hp-testrail.external.hp.com/index.php?/tests/view/746274747
        # self.endpoint_security.search_device("HP ")
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.endpoint_security.click_first_entry_link()
        self.endpoint_security.verify_device_details_policy_tab()
        self.endpoint_security.click_device_details_policy_tab()
    
        # Verify Policies - Compliance Status Widget UI
        self.endpoint_security.verify_device_details_policy_compliance_status_card()
        self.endpoint_security.verify_device_details_policy_run_now_button()
        self.endpoint_security.verify_policy_device_details_compliance_status_card_title()
        self.endpoint_security.click_device_details_policy_compliance_status_card()
        self.endpoint_security.verify_device_details_policy_compliance_status_card()
        self.endpoint_security.click_device_details_policy_compliance_status_card()
        self.endpoint_security.verify_device_details_policy_compliance_status_card()
    
        # Verify Policies - Policy Status Widget UI
        self.endpoint_security.verify_device_details_policy_widget_policy_card()
        self.endpoint_security.verify_device_details_policy_widget_edit_button()
        self.endpoint_security.verify_device_details_policy_tab_policy_widget_collapse()
        self.endpoint_security.click_device_details_policy_tab_policy_widget()
        self.endpoint_security.verify_device_details_policy_tab_policy_widget_expand()