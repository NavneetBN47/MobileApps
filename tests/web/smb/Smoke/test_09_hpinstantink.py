import logging
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_09_SMB_HPInstantInk(object):

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
        self.hpinstantink = self.fc.fd["hpinstantink"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]

    def test_01_verify_hpinstantink_ui_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32799334

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_hpinstantink_menu_btn()
        self.hpinstantink.verify_hpinstantink_title()
        self.hpinstantink.verify_hpinstantink_description()

        #Verify never run out details
        self.hpinstantink.verify_hpinstantink_never_run_out_title()
        self.hpinstantink.verify_hpinstantink_never_run_out_description()

        # #verify savings claim (Ink) details
        # self.hpinstantink.verify_hpinstantink_savings_claim_ink_title()
        # self.hpinstantink.verify_hpinstantink_savings_claim_ink_description()
        # self.hpinstantink.verify_hpinstantink_savings_claim_ink_key_point_hyperlink()

        #verify savings claim (Toner) details
        self.hpinstantink.verify_hpinstantink_savings_claim_toner_title()
        # self.hpinstantink.verify_hpinstantink_savings_claim_toner_description()
        self.hpinstantink.verify_hpinstantink_savings_claim_toner_key_point_hyperlink()

    def test_02_verify_key_point_intelligence_hyperlink(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32799338

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_hpinstantink_menu_btn()
        self.hpinstantink.click_hpinstantink_savings_claim_toner_key_point_hyperlink()
        self.hpinstantink.verify_new_tab_opened()
        self.hpinstantink.verify_key_point_intelligence_url()

    def test_03_verify_signup_now_button(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32804618

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_hpinstantink_menu_btn()
        if self.hpinstantink.verify_signup_now_button() is not False:
            self.hpinstantink.click_signup_now_button()
            self.hpinstantink.verify_enrolling_printer_title()
        else:
            logging.info("Signup Now button is not available")