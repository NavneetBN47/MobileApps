import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_07_SMB_Solutions(object):

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
        self.printers = self.fc.fd["printers"]
        self.solutions = self.fc.fd["solutions"]
        self.account = self.fc.fd["account"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
   
    def test_01_verify_solutions_discover_all_link(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30516296
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_solutions_menu_btn()
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        if self.solutions.verify_solutions_hp_smart_pro_is_displayed(displayed=False) ==True:
            logging.info("HP Smart Pro entitlenment is not active")
        else: 
            self.solutions.verify_solutions_discover_all_features_link()
            self.solutions.click_solutions_discover_all_features_link()
            self.solutions.verify_solutions_discover_all_hp_smart_pro_page_title()

    def test_02_verify_solutions_learn_more_about_hp_plus_link(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30519148
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.verify_solutions_learn_more_about_hp_plus_link()
        self.solutions.click_solutions_learn_more_about_hp_link()
        self.solutions.verify_new_tab_opened()
        self.solutions.verify_solutions_learn_more_hp_plus_page_url()

    def test_03_verify_solutions_sustainability_forest_first_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30519153
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_solutions_menu_btn()
        self.solutions.verify_solutions_title()
        self.solutions.click_solutions_sustainability_forest_first_button()
        self.printers.verify_sustainability_screen_title()
   