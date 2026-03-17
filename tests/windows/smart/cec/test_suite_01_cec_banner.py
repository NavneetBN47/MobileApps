import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_01_CEC_Banner(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.login_info_2 = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_to_main_ui_login_add_printer(self):
        """
        Precondition: Login HP account and add printer to Main Page.
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_close_cec_engagement(self):
        """
        Close all engagements on CEC Jweb area, relaunch app, verify CEC Jweb area doesn't show
        Click 'x' on the first engagement on CEC Jweb area, verify a new engagement shows to the right

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749319
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749317
        """
        self.home.verify_cec_banner()
        self.home.verify_cec_engagement_list_items()
        for i in range(1,20):
            if self.home.click_cec_engagement_close_btn(raise_e=False) is False:
                break
        else:
            raise Exception("More than 20 CEC engagement, please increase the range!!!")
        logging.info("Closed {} CEC Engagement".format(i-1))
        if 'pie' in self.stack:
            pytest.skip("Skip this test as some CEC items have no dismiss button for pie stack")

        assert self.home.verify_cec_banner(raise_e=False) is False

        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=20)
        assert self.home.verify_cec_banner(raise_e=False) is False

    def test_03_cec_engagement_different_account(self):
        """
        Close all engagements on CEC Jweb area, relaunch app, sign in different account, verify CEC Jweb shows again 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28874357
        """
        self.fc.sign_out()
        self.fc.web_password_credential_delete()
        self.fc.restart_hp_smart()
        self.home.verify_home_screen(timeout=20)
        self.fc.sign_in(self.login_info_2["email"], self.login_info_2["password"])
        self.home.verify_home_screen(timeout=30)
        self.home.verify_cec_banner()
        self.home.verify_cec_engagement_list_items()
        

