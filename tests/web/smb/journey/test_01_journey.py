import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_01_SMB_Login(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request, record_testsuite_property):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["printers"]
        self.users = self.fc.fd["users"]
        self.solutions = self.fc.fd["solutions"]
        self.settings = self.fc.fd["settings"]
        self.instantink_smb = self.fc.fd["instantink_smb"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.account = ma_misc.get_smb_account_info(self.stack, "SMB")
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        record_testsuite_property("suite_test_category", "Journey")


    def test_01_verify_home_page(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_smb_home_title_bar()
        self.home.verify_smart_notification_widget_title()

    def test_02_verify_printer_page(self):
        self.home.click_printers_menu_btn()
        self.printers.verify_printers_page_title()
        self.printers.verify_printers_page_desc()

    def test_03_verify_users_page(self):
        self.home.click_users_menu_btn()
        self.users.verify_users_page_title()
        self.users.verify_users_page_description()

    """
    #need to verify code with veera, don't know what's going on here
    def test_04_verify_settings_menu_page(self):
        self.home.click_settings_menu_btn()
        self.settings.verify_preferences_screen_title()
        self.settings.verify_preferences_screen_description()
    """

    def test_05_verify_instantink_page(self):
        self.home.click_hpinstantink_menu_btn()
        self.instantink_smb.verify_promotional_banner()