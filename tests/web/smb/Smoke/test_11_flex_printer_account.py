import pytest
from SAF.misc import saf_misc
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_11_SMB_Flex_Printer_Account(object):

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
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.account = self.fc.fd["account"]
        self.users = self.fc.fd["users"]
        self.printers = self.fc.fd["printers"]
        self.solutions = self.fc.fd["solutions"]
        self.accounts = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.accounts["flex_account_email"]
        self.hpid_password = self.accounts["flex_account_password"]
        self.hpid_tenantID = self.accounts["tenantID"]
    
    def test_01_verify_login_timeout(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/41261364
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_smb_home_title_bar()
        self.driver.active_sleep(30)
        self.driver.wdvr.refresh()
        self.home.verify_smb_home_title_bar()

    def test_02_verify_side_menu(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/41339128
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_hpinstantink_menu_btn()
        self.home.verify_printers_menu_btn()
        self.home.verify_users_menu_btn()
        self.home.verify_solutions_menu_btn_displayed(displayed=False)
        self.home.verify_sustainability_menu_btn_displayed(displayed=False)
        self.home.verify_account_menu_btn()
        self.home.verify_help_center_menu()

    def test_03_logout(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/41381083
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.logout()
        self.login.verify_smb_login_label()  

    def test_04_verify_welcome_text(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30515973
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        actual_welcome_text = self.home.get_welcome_text()
        self.home.click_account_menu_btn()
        self.home.click_account_profile_button()
        first_name = self.home.get_first_name_in_account_profile()
        expected_welcome_text = "Welcome, " + first_name +"!"
        assert expected_welcome_text == actual_welcome_text
         
    def test_05_verify_organization_name(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/41339134
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.home.click_account_profile_button()
        self.home.click_organization_tab()
        org_id = self.home.get_last_four_digit_of_uid()
        org_name = self.home.get_organization_name_in_account_profile()
        length = len(org_name)
        if length >11:
            actual_org_name = org_name[0:6]+"..."+org_name[length-5:]+" (..."+org_id+")"
        else:
            actual_org_name = org_name+" (..."+org_id+")"
        self.home.click_avatar_button()
        assert actual_org_name == self.home.get_organization_id()
    
    def test_06_verify_printers_screen_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30516064
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519654

        #verify printer details
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_printers_menu_btn()
        self.printers.verify_printers_page_title()
        self.printers.verify_printers_page_desc()
        self.printers.verify_printer_table_refresh_button()
        self.printers.verify_printer_table_last_updated_date_time()
        self.printers.verify_printer_table_search_box()
        self.printers.verify_printer_table_view_button()
        self.printers.verify_printer_card_view_button()
    
    def test_07_verify_users_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711404
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711495
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.verify_users_page_title()
        self.users.verify_users_page_description()
        self.users.verify_user_breadcrumb()
    
    def test_08_verify_account_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519059
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_account_menu_btn()
        self.account.verify_account_screen_title()
        self.account.verify_account_screen_description()
        self.account.verify_account_profile_tab_title()
        self.account.verify_account_profile_tab_description()
        self.account.verify_preferences_tab_title()
        self.account.verify_preferences_tab_description()