import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "SMART"

class Test_Suite_01_Mobile_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.softfax_offer = cls.fc.fd["softfax_offer"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_mobile_fax_option(self):
        """
        IOS & MAC:
        C33405095 - Verify Mobile Fax option UI through App Settings
        """
        self.fc.go_home(stack=self.stack, create_account=True)
        self.home.select_app_settings()
        self.app_settings.select_mobile_fax()
        if pytest.platform == "IOS":
            self.driver.wait_for_context(w_const.WEBVIEW_URL.SOFTFAX_OFFER, timeout=30)
        self.softfax_offer.verify_get_started_screen(timeout=30 if pytest.platform == "MAC" else 10)