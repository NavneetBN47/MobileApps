import pytest
import logging
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_01_SMB_Login(object):

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
        self.account = ma_misc.get_smb_account_info(self.stack + "_journey_testing")
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        self.hpid_tenantID = self.account["tenantID"]

                
        yield # Cleanup:
        self.home.logout()


    def test_01_hero_flow_login(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/30463295
        #Verify user can log in with a valid account
        logging.info("Using account: {self.hpid_username}")
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_smb_home_title_bar()
        sleep(2)
