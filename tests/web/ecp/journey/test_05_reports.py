import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_05_ECP_Reports(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.reports = self.fc.fd["reports"]
        self.account = ma_misc.get_ecp_account_info(self.stack + "_journey_testing")
        self.hpid_username = self.account["alt-email"]
        self.hpid_password = self.account["alt-password"]
        
        yield # Cleanup:
        self.home.logout()


    def test_05_verify_reports_mfe(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236562
        #Verify that the reports page loads
        print(f"Using account: {self.hpid_username}")
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, retry=2, raise_e=True)
        self.home.verify_reports_menu_btn()
        self.home.click_reports_menu_btn()

        self.reports.verify_reports_page(table_load=False)

