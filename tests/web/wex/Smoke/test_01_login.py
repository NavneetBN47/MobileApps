import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"

class Test_01_WEX_Login(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["fleet_management_devices"]
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]

    @pytest.mark.sanity
    def test_01_verify_login_flow(self, request):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/1393128896

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        #verifying landing page breadcrumb
        self.home.verify_home_page_title()

        #verifying side menu buttons
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        self.home.verify_home_menu_btn()
        request.addfinalizer( self.home.logout)