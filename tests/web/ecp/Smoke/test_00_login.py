import pytest
import time
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_02_ECP_Home(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.home = self.fc.fd["home"]
        self.t_account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.t_account["email"]
        self.hpid_password = self.t_account["password"]

    def test_01_verify_login_timeout(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29259419
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.driver.active_sleep(930)
        self.driver.wdvr.refresh()
        self.login.verify_ecp_login()