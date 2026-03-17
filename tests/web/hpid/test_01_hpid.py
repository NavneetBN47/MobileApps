import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
from MobileApps.libs.flows.web.smart.smart_printer_consent import SmartPrinterConsent

pytest.app_info = "HPCONNECT"

class Test_01_HPID_Web(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, web_session_setup, request, record_testsuite_property):
        self = self.__class__
        self.driver = web_session_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")

        record_testsuite_property("suite_test_stack", self.stack)
        record_testsuite_property("suite_test_platform", pytest.platform)

        self.hpid = HPID(self.driver)
        self.hp_connect = HPConnect(self.driver)
        self.ucde_privcy = UCDEPrivacy(self.driver)
        #Test is performed with the basic HPID account
        self.account = ma_misc.get_hpid_account_info(self.stack, "basic", claimable=False)
        self.smart_printer_consent = SmartPrinterConsent(self.driver)
        record_testsuite_property("suite_test_category", "HPID")

    def test_01_hpid_sign_in(self):
        self.hp_connect.navigate(self.stack)
        self.hp_connect.accept_privacy_popup()
        sleep(1)
        self.hp_connect.verify_sign_in_btn()
        self.hp_connect.click_sign_in_btn()
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.account["email"], self.account["password"])
        self.ucde_privcy.skip_ucde_privacy_screen(timeout=3)
        self.hp_connect.verify_UCDE_banner(timeout=30)
        self.driver.performance.stop_timer("hpid_login")
        self.driver.performance.time_stamp("t10")

    def test_02_hpid_sign_out(self):
        self.hp_connect.sign_out()
        self.hp_connect.verify_sign_in_btn()
        self.driver.performance.stop_timer("hpid_logout")
    
    def test_03_hpid_sign_up(self):
        self.hp_connect.navigate(self.stack)
        if self.hp_connect.verify_signed_in():
            self.hp_connect.sign_out()
        self.hp_connect.accept_privacy_popup()
        self.hp_connect.click_sign_up_btn()
        self.hpid.create_account()
        self.smart_printer_consent.verify_printer_full_page_consent_screen()        
        self.driver.performance.stop_timer("hpid_create_account")
