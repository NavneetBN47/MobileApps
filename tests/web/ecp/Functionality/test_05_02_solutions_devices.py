import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
pytest.app_info = "ECP"
 
class Test_01_ES_Devices(object):
 
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.devices = self.fc.fd["devices"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]
 
    def test_01_verify_dropdown_for_device_details(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29172158
 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.endpoint_security.click_first_entry_link()
        sleep(5) #wait for the page to load
        self.devices.verify_device_details_hp_secure_fleet_manager_tab()
        self.devices.click_device_details_hp_secure_fleet_manager_tab()
        self.endpoint_security.select_reports_dropdown()
        self.endpoint_security.verify_reports_dropdown_options()
 
    # This test case is not valid anymore as the Devices tab got removed from the UI
    @pytest.mark.skip
    def test_02_verify_number_of_devices_displayed_per_page(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29172152
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.click_devices_tab()
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.verify_all_page_size_options_new([5, 25, 50, 100, 500])
        self.endpoint_security.verify_table_displaying_correctly_new(5, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(25, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(50, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(100, page=1)
        self.endpoint_security.verify_table_displaying_correctly_new(500, page=1)
 
    # def test_03_verify_default_sort(self):
    #     #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153742
    #     self.fc.navigate_endpoint_security_tab(self.stack, self.hpid_username, self.hpid_password, "devices")
    #     self.endpoint_security.verify_table_sort("device_status", ["Online", "Offline"])
   
    # def test_4_verify_sort_change(self):
    #     #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29153742
    #     self.fc.navigate_endpoint_security_tab(self.stack, self.hpid_username, self.hpid_password, "devices")
    #     self.endpoint_security.click_table_header_by_name("device_status")
    #     self.endpoint_security.verify_table_sort("device_status", ["Offline", "Online"])
   
    # def test_5_verify_device_details_report_timeframe_options(self):
    #     #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29172169
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     # self.fc.select_customer(self.customer)
    #     self.home.click_solutions_menu_btn()
    #     self.endpoint_security.click_hp_secure_fleet_manager()
    #     self.endpoint_security.click_devices_tab()
    #     self.endpoint_security.verify_table_loaded()
    #     self.endpoint_security.click_first_entry_link()
       
    #     #verify time frame in reports dropdown
    #     self.endpoint_security.select_report("remediation")
    #     self.endpoint_security.verify_details_report_loaded()
    #     self.endpoint_security.verify_details_report_dropdown_default_option("Last 7 days")
    #     self.endpoint_security.verify_details_report_dropdown_options(["Last 1 day","Last 7 days","Last 30 days"])
   
    @pytest.mark.parametrize('report_name', ["assessment", "remediation"])
    def test_6_verify_cancel_button_on_export_reports_popup(self, report_name):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214752
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214777
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device("online")
        self.endpoint_security.click_first_entry_link()
        self.devices.verify_device_details_hp_secure_fleet_manager_tab()
        self.devices.click_device_details_hp_secure_fleet_manager_tab()
        self.endpoint_security.select_report(report_name)
        self.endpoint_security.verify_device_report_type(report_name)
        self.endpoint_security.verify_device_report_description()
        self.endpoint_security.click_device_report_export_btn()
        # self.endpoint_security.click_cancel_button()
 
    # @pytest.mark.parametrize('report_name', ["assessment", "remediation"])
    # def test_7_verify_report_time_frame(self, report_name):
    #     #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214748
    #     #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214749
    #     #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29214750
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     self.fc.select_customer(self.customer)
    #     self.home.click_solutions_menu_btn()
    #     self.endpoint_security.click_hp_secure_fleet_manager()
    #     self.endpoint_security.click_devices_tab()
    #     self.endpoint_security.verify_table_loaded()
    #     self.endpoint_security.click_first_entry_link()
    #     self.endpoint_security.select_report(report_name)
    #     self.endpoint_security.verify_reports_displaying_correctly_for("Last 30 days")