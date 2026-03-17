import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "SMB"

class Test_08_01_SMB_Smart_Security(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.account = self.fc.fd["account"]
        self.printers = self.fc.fd["printers"]
        self.solutions = self.fc.fd["solutions"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]

            
    def test_01_verify_smart_security_ui_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516303
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_smart_security_button()

        #verify smart security ui
        self.solutions.verify_smart_security_title()
        self.solutions.verify_smart_security_description()
        self.solutions.verify_smart_security_refresh_button()
        self.solutions.verify_smart_security_last_refresh_date_time()
        self.solutions.verify_smart_security_search_textbox()
        expected_table_header = ["Printer Name", "Location", "Connectivity", "Security Status"]
        assert expected_table_header==self.solutions.verify_smart_security_table_headers()
        page_count = self.solutions.get_smart_security_pagination_count()
        if page_count == 0 :
            self.solutions.verify_smart_security_table_empty()
        else:
            self.solutions.verify_smart_security_page_load()

    #sorting not based on connectivity status
    # def test_02_verify_sorting_functionality_smart_security(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30520991
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
    #     self.home.click_solutions_menu_btn()
    #     self.solutions.verify_solutions_title()
    #     self.solutions.click_solutions_smart_security_button()
    #     self.solutions.verify_smart_security_title()
    #     #verify default sorting
    #     self.solutions.verify_table_sort("connectivity",["Not connected","Connected"])
    #     #verify sorting by printers name
    #     self.solutions.click_table_header_by_name("device_name")
    #     self.solutions.verify_smart_security_page_load()
    #     self.solutions.verify_table_sort("connectivity",["Connected","Not connected"])

    def test_03_verify_smart_security_refresh_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516304
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        cur_time = self.solutions.get_sync_time_info()
        sleep(1)
        self.solutions.click_smart_security_refresh_button()              
        new_time = self.solutions.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split(";")[1], self.driver.get_timezone(), "%m/%d/%Y at %I:%M:%S %p") == True
        assert new_time != cur_time

    @pytest.mark.parametrize('search_string',  ["invalidname","Storm"])
    def test_04_verify_smart_security_search_functionality(self,search_string):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516305
        
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        self.solutions.smart_security_search_printers(search_string, timeout=20)
        self.solutions.click_search_clear_button()

    def test_05_pagination_smart_security(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516306
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()

        # Verify and wait for printer table data load
        self.solutions.verify_smart_security_page_load()

        self.solutions.verify_all_page_size_options_new([10, 25, 50, 100])
        self.solutions.verify_table_displaying_correctly_new(10, page=1)
        self.solutions.verify_table_displaying_correctly_new(25, page=1)
        self.solutions.verify_table_displaying_correctly_new(50, page=1)
        self.solutions.verify_table_displaying_correctly_new(100, page=1)

    def test_06_verify_smart_security_details_ui_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516303
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen
        self.solutions.click_table_header_by_name("device_name")
        self.solutions.verify_and_click_connected_printer()
        #verify printer details in smart security detail screen
        # self.solutions.verify_smart_security_detail_screen_printer_name()
        # self.solutions.verify_smart_security_detail_screen_printer_model()
        self.solutions.verify_smart_security_detail_screen_printer_connectivity()
        self.solutions.verify_smart_security_detail_screen_printer_security_status()
        self.solutions.verify_smart_security_detail_screen_printer_detail_link()
        self.solutions.verify_smart_security_detail_screen_refresh_button()
        self.solutions.verify_smart_security_detail_screen_refresh_text()
        #verify security monitoring details
        self.solutions.verify_security_monitoring_toggle_button()
        self.solutions.verify_security_monitoring_title()
        self.solutions.verify_security_monitoring_status()

    def test_07_verify_smart_security_details_security_settings_ui_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516303
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen
        self.solutions.click_table_header_by_name("device_name")
        self.solutions.verify_and_click_connected_printer()

        #turn on security monitoring if it is off
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="false":
            self.solutions.click_security_monitoring_toggle_button()

        #verify security settings details
        self.solutions.verify_security_settings_title()
        self.solutions.verify_security_settings_desc()
        self.solutions.verify_admin_password_title()
        self.solutions.verify_admin_password_tool_tip()
        self.solutions.verify_admin_password_expand_button()
        # self.solutions.verify_automatic_firmware_update_title()
        # self.solutions.verify_automatic_firmware_update_tool_tip()
        # self.solutions.verify_automatic_firmware_update_expand_button()
        self.solutions.verify_snmp_title()
        self.solutions.verify_snmp_tool_tip()
        self.solutions.verify_snmp_expand_button()
    
    def test_08_verify_smart_security_details_refresh_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519364
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen
        self.solutions.click_table_header_by_name("device_name")
        self.solutions.verify_and_click_connected_printer()
        #verify printer details in smart security detail screen
        # self.solutions.verify_smart_security_detail_screen_printer_name()
        cur_time = self.solutions.get_sync_time_info()
        sleep(1)
        self.solutions.click_smart_security_detail_screen_refresh_button()
        new_time = self.solutions.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(((new_time.split("Last updated")[1]).replace("&nbsp;","")), self.driver.get_timezone(), "%m/%d/%Y at %I:%M:%S %p") == True
        assert new_time != cur_time

    def test_09_verify_smart_security_mointoring_toggle_button_popup_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521038
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521039
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/30521042
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        #navigate to solution screen
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        #navigate to smart security screen
        self.solutions.click_solutions_smart_security_button()
        self.solutions.verify_smart_security_title()
        #navigate to smart security detail screen
        self.solutions.click_table_header_by_name("device_name")
        self.solutions.verify_and_click_connected_printer()
        #verify smart security detail screen
        # self.solutions.verify_smart_security_detail_screen_printer_name()
        toggle_status=self.solutions.get_security_monitoring_toggle_status()
        if toggle_status=="true":
            self.solutions.click_security_monitoring_toggle_button()
            self.solutions.verify_security_monitoring_popup_title()
            self.solutions.verify_security_monitoring_popup_desc()
            self.solutions.verify_security_monitoring_popup_cancel_button()
            self.solutions.verify_security_monitoring_popup_turnoff_button()
            self.solutions.click_security_monitoring_popup_cancel_button()
        else:
            self.solutions.verify_security_monitoring_title()

    def test_10_verify_printer_details_link_on_smart_security_printer_details_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30521021
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.click_solutions_smart_security_button()
        self.solutions.click_table_header_by_name("device_name")
        self.solutions.verify_and_click_connected_printer()
        self.solutions.click_printer_details_link()
        self.printers.verify_printer_details_screen_overview_title()