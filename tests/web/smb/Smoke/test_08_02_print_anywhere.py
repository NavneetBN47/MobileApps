import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_08_02_SMB_Print_Any_Where(object):

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

    def test_01_verify_print_any_where_ui_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516311
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30532171
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516307
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30529501
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()

        #verify print anywhere ui
        self.solutions.verify_print_anywhere_title()
        # self.solutions.verify_print_anywhere_description()
        self.solutions.verify_print_anywhere_detail_description()
        self.solutions.verify_print_anywhere_refresh_button()
        self.solutions.verify_print_anywhere_last_refresh_date_time()
        self.solutions.verify_print_anywhere_search_textbox()
        self.solutions.verify_print_anywhere_page_table_loads()
        expected_table_header = ["PRINTER NAME", "LOCATION", "PRINT ANYWHERE", "PRIVATE PICKUP"]
        assert expected_table_header==self.solutions.verify_print_anywhere_table_headers()
        page_count = self.solutions.get_smart_security_pagination_count()
        if page_count == 0 :
            self.solutions.verify_smart_security_table_empty()
        else:
            self.solutions.verify_print_any_where_table_first_entry()

    def test_02_verify_print_anywhere_refresh_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516308
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        cur_time = self.solutions.get_sync_time_info()
        self.solutions.click_print_anywhere_refresh_button()
        self.solutions.get_print_anywhere_last_refresh_date_time()
        new_time = self.solutions.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated:")[1], self.driver.get_timezone(), " %d %b %Y | %I:%M:%S %p") == True
        assert new_time != cur_time

    @pytest.mark.parametrize('search_string',  ["invalidname","Storm"])
    def test_03_verify_print_anywhere_search_functionality(self,search_string ):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516313
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516309
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.smart_security_search_printers(search_string, timeout=20)
        self.solutions.click_search_clear_button()
    
    # def test_04_verify_sorting_functionality_print_any_where(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30711415
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
    #     self.home.click_solutions_menu_btn()
    #     self.solutions.verify_solutions_title()
    #     self.solutions.click_solutions_print_anywhere_button()
    #     self.solutions.verify_print_anywhere_title()
    #     self.solutions.verify_print_anywhere_tab_title()
    #     #verify default sorting
    #     self.solutions.verify_table_sort("print_anywhere",["On","Off"])
    #     #verify sorting by printers name
    #     self.solutions.click_table_header_by_name("device_name")
    #     self.solutions.verify_table_sort("print_anywhere",["On","Off"])

    def test_05_pagination_print_any_where(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516314
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516310
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_print_anywhere_button()
        self.solutions.verify_print_anywhere_title()
        self.solutions.verify_print_anywhere_page_table_loads()
        self.solutions.verify_all_page_size_options_new([5, 10, 15, 20])
        self.solutions.verify_table_displaying_correctly_new(5, page=1)
        self.solutions.verify_table_displaying_correctly_new(10, page=1)
        self.solutions.verify_table_displaying_correctly_new(15, page=1)
        self.solutions.verify_table_displaying_correctly_new(20, page=1)
