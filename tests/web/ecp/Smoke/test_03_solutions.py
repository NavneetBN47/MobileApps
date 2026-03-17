import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"
 
class Test_03_Endpoint_Security(object):
 
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
 
    def test_01_verify_endpoint_security_dashboard_and_devices_list_page(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29152774
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153141
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        # self.endpoint_security.click_devices_tab()  # Devices tab got removed from the UI so commenting this line
        # self.endpoint_security.verify_selected_tab("devices_tab")
        # self.endpoint_security.verify_table_loaded()
        # self.endpoint_security.verify_table_sort("status", ["Online", "Offline"])
   
    @pytest.mark.skip # This test case is not valid anymore as the Devices tab got removed from the UI
    def test_02_verify_device_name_search_box(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153737
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153735
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()  
        self.endpoint_security.search_device("HP ")
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.verify_search_results("HP")
        self.endpoint_security.search_device("badprinter")
        self.endpoint_security.verify_no_items_found()
 
    @pytest.mark.skip
    def test_03_verify_export_devices_popup(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29172064
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153739
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.click_export_all()
        self.endpoint_security.verify_export_popup()
        self.endpoint_security.click_cancel_button()
 
        #verify export button
        self.endpoint_security.click_export_all()
        self.endpoint_security.verify_export_popup()
        self.endpoint_security.click_export_button()
        self.endpoint_security.check_toast_successful_message("File has been downloaded successfully!")
       
    @pytest.mark.skip    
    def test_04_verify_refresh_details_page(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153728
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153766
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        #verifying refresh on device list page
        self.endpoint_security.verify_refresh_device_tab_functionality()
        self.endpoint_security.click_first_entry_link()
        #verifying refresh on details page
        self.endpoint_security.verify_refresh_device_detail_functionality()
 
    @pytest.mark.skip
    def test_05_verify_pagination(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29172151
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.verify_all_page_size_options_new([5,25, 50, 100, 500])
        self.endpoint_security.verify_table_displaying_correctly_new(5, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(25, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(50, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(100, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(500, page=1)
 
    @pytest.mark.skip
    def test_06_verify_devices_details_page(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153764
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
 
        entry_detail = self.endpoint_security.get_devices_detail_info()
        self.endpoint_security.click_first_entry_link()
        assert entry_detail == self.endpoint_security.verify_devices_details_list_synced_with_device_tab()
 
    @pytest.mark.parametrize('report_name', ["assessment", "remediation"])
    def test_07_verify_export_reports_popup(self, report_name):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214751
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214776
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device("online")
        self.endpoint_security.click_first_entry_link()
        sleep(5) # wait for the page to load
        self.devices.verify_device_details_hp_secure_fleet_manager_tab()
        self.devices.click_device_details_hp_secure_fleet_manager_tab()
        sleep(5) # wait for the page to load
        self.endpoint_security.select_report(report_name)
        self.endpoint_security.click_device_report_export_btn()
        # self.endpoint_security.verify_export_dialog_popup(report_name)
       
    @pytest.mark.parametrize('report_name', ["assessment", "remediation"])
    def test_08_verify_report_content_can_be_expanded_and_collapsed(self,report_name):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29172163
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device("online")
        self.endpoint_security.click_first_entry_link()
        self.devices.verify_device_details_hp_secure_fleet_manager_tab()
        self.devices.click_device_details_hp_secure_fleet_manager_tab()
        sleep(5) # wait for the page to load
        self.endpoint_security.select_report(report_name)
        self.endpoint_security.verify_report_content_expanded()
        self.endpoint_security.click_report_content()
        self.endpoint_security.verify_report_content_collapsed()
        self.endpoint_security.click_report_content()
        self.endpoint_security.verify_report_content_expanded()
   
    def test_09_verify_security_trend_default_drop_down(self):
       #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29152829
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.verify_security_trend_loaded()
        self.endpoint_security.verify_security_trend_dropdown_current_option("Last 24 hours")
        self.endpoint_security.select_security_trends_dropdown("Last 7 days")
        self.endpoint_security.select_security_trends_dropdown("Last 30 days")
 
    @pytest.mark.parametrize("option_name", ["Last 24 hours","Last 7 days","Last 30 days"])
    def test_10_verify_security_trend_other_options(self,option_name):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29152831
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29152886
        #TODO this is no where near complete
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        sleep(5) # Adding time out to load the page
        self.endpoint_security.select_security_trends_dropdown(option_name)
 
    @pytest.mark.skip
    def test_11_verify_solutions_device_tab_match_with_global_device_tab(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/679212069
        # https://hp-testrail.external.hp.com/index.php?/tests/view/679212080
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.click_groups_side_bar_expand_btn()
 
        # get global devices group names and their device counts
        global_device_all_group_count=self.devices.get_device_count("All")
        global_device_group_details=dict(zip(self.devices.get_group_names(), self.devices.get_group_counts()))
 
        # get Solutions-->Devices tab devices group names and their device counts
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.devices.click_groups_side_bar_expand_btn()
 
        assert global_device_all_group_count == self.devices.get_device_count("All")
        solutions_device_group_details=dict(zip(self.endpoint_security.get_group_names(), self.endpoint_security.get_group_counts()))
        assert global_device_group_details == solutions_device_group_details
 
    @pytest.mark.skip
    def test_12_verify_solutions_devices_tab_column_option_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/679212040
        expected_options= ["Model Name","Assessment","Status", "Connectivity","Serial Number","Group"]
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.devices.click_devices_column_option_settings_gear_button()
        self.devices.verify_column_options_popup_title()
        self.devices.verify_column_options_popup_reset_to_default_button()
        self.devices.verify_column_options_popup_cancel_button()
        self.devices.verify_column_options_popup_save_button()
        assert expected_options == self.devices.get_column_options_popup_options()
 
    @pytest.mark.skip
    def test_13_verify_solutions_devices_tab_column_option_popup_save_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/679212041
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.devices.click_devices_column_option_settings_gear_button()
        self.endpoint_security.click_solutions_device_tab_column_option("Connectivity")
        self.devices.click_column_options_popup_save_button()
 
        # Verify Solutions-->Device table CONNECTIVITY Column
        self.endpoint_security.verify_solutions_device_table_column("Connectivity",displayed=False)
 
        # Reverting the Column option changes
        self.devices.click_devices_column_option_settings_gear_button()
        self.endpoint_security.click_solutions_device_tab_column_option("Connectivity")
        self.devices.click_column_options_popup_save_button()
        self.endpoint_security.verify_solutions_device_table_column("Connectivity")
 
    @pytest.mark.skip
    def test_14_verify_solutions_devices_tab_column_option_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/679212041
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.devices.click_devices_column_option_settings_gear_button()
        self.endpoint_security.click_solutions_device_tab_column_option("Connectivity")
        self.devices.click_column_options_popup_cancel_button()
 
        # Verify Solutions-->Device table CONNECTIVITY Column
        self.endpoint_security.verify_solutions_device_table_column("Connectivity")