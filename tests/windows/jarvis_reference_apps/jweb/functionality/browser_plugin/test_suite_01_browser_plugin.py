import pytest

pytest.app_info = "JWEB"

class Test_Suite_01_Browser_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, jweb_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.browser_plugin = cls.fc.fd["browser_plugin"]

    def test_01_verify_browser_test_plugin_service_login(self):
        """
        C28698082: Validating AuthBrowser API to open an in-app browser sessions
            - After selecting the test btn from AuthBrowser.open(), and returning from the browser, verify result contains a token
            - Expecting the result contains a token
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_mode(raise_e=False)
        self.home.select_jweb_reference_btn(raise_e=False)
        self.home.select_url_go_btn(raise_e=False)
        self.home.select_plugin_from_home("auth browser")
        self.browser_plugin.select_browser_test()
        self.browser_plugin.select_redirect_link()
        assert "[object Object]" in self.browser_plugin.get_browser_sign_in_result_text()