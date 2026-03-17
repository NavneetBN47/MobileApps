import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
pytest.app_info = "ECP"


class Test_01_ES_Overview(object):

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


    def test_02_verify_status_card_devices(self):
        #test case https://hp-testrail.external.hp.com/index.php?/cases/view/29152891
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_solutions_menu_btn()
        self.endpoint_security.click_hp_secure_fleet_manager()
        self.endpoint_security.verify_security_dashboard("overview_section")
        self.endpoint_security.get_all_entitled_devices()
        self.endpoint_security.click_entitled_devices()
        self.devices.verify_navigated_tab("assigned-tab")
        self.endpoint_security.verify_table_loaded()
        self.endpoint_security.verify_status_devices()