import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Eventing_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.browser_plugin = cls.fc.fd["browser_plugin"]
        cls.security_gateway = cls.fc.fd["security_gateway"]

    def test_01_verify_browser_test_plugin_service_login(self):
        """
        C28698082: Validating AuthBrowser API to open an in-app browser sessions
            - After selecting the test btn from AuthBrowser.open(), and returning from the browser, verify result contains a token
            - Expecting the result contains a token
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("auth_browser")
        self.browser_plugin.select_browser_test()
        self.system.select_continue()
        self.security_gateway.select_redirect_me()
        assert "[object Object]" in self.browser_plugin.browser_sign_in_result()