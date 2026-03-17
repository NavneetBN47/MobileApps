import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "JWEB_AUTH"

class Test_Suite_08_Auth_Plugin_Token_Expiration(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.system = cls.fc.fd["system"]
        cls.home = cls.fc.fd["home"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]
        cls.scope = test_account["scope"]
        cls.resource = test_account["resource"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_auth_plugin(self):
        self.fc.reset_app()
        self.home.select_top_bar_button('Plugin', raise_e=False)

    def test_01_verify_login_token_lifetime_requirements_disabled(self):
        """
        C36914544 - Verify user can login with appropriate credentials to get token if TokenLifeTimeRequirements are disabled.
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()

    def test_02_verify_weblet_token_lifetime_requirements_options_available(self):
        """
        C36914545 - Verify in Weblet Token LifeTime Requirements options is available
        """
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.verify_token_lifetime_options()

    def test_03_verify_previous_token_remains_after_setting_max_seconds_since_issued(self):
        """
        C36914555 - Verify previous token is retrieved as we set preferredMaximumSecondsSinceIssued=300s and satisfiesTokenLifetimeRequirements will be shown false
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMaximumSecondsSinceIssued")
        self.auth_plugin.send_text_to_token_lifetime_textbox(300)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        old_token_value = self.auth_plugin.auth_get_token_result()["tokenValue"]
        sleep(10)
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        assert old_token_value == self.auth_plugin.auth_get_token_result()["tokenValue"]

    def test_04_verify_new_token_is_retrieved_after_setting_max_seconds_until_expiration(self):
        """
        C36914556 - Verify new token is retrieved after 30sec when set preferredMinimumSecondsUntilExpiration = 36000s (10 hours) and satisfiesTokenLifetimeRequirements is false
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMinimumSecondsUntilExpiration")
        self.auth_plugin.send_text_to_token_lifetime_textbox(36000)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        old_token_value = self.auth_plugin.auth_get_token_result()["tokenValue"]
        sleep(10)
        self.auth_plugin.select_auth_get_token_test()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        assert old_token_value != self.auth_plugin.auth_get_token_result()["tokenValue"]

    def test_05_verify_access_token_is_returned_after_entering_tenantId_and_setting_preferredMaximumSecondsSinceIssued(self):
        """
        C38256392 - Verify access token is returned after entering tenantId and setting preferredMaximumSecondsSinceIssued=0s
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMaximumSecondsSinceIssued")
        self.auth_plugin.send_text_to_token_lifetime_textbox(0)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        sleep(10)
        assert self.auth_plugin.auth_get_token_result()['tenantID'] is not None
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        assert self.auth_plugin.auth_get_token_result()["tokenValue"]

    def test_06_verify_login_screen_shows_up_enable_skip_refresh_token_set_preferredMaximumSecondsSinceIssued(self):
        """
        C38256393 - Verify Login Screen shows up when 'openid' is passed as Scopes and after enabling SkipToken Refresh and set preferredMaximumSecondsSinceIssued as 0
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, True])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMaximumSecondsSinceIssued")
        self.auth_plugin.send_text_to_token_lifetime_textbox(0)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(10)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_auth_get_token_test()
        assert self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))

    def test_07_verify_login_screen_shows_up_disable_skip_refresh_token_set_preferredMaximumSecondsSinceIssued(self):
        """
        C38326158 - Verify Login Screen shows up when 'openid' is passed as Scopes and after disabling SkipToken Refresh and set preferredMaximumSecondsSinceIssued as 0
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMaximumSecondsSinceIssued")
        self.auth_plugin.send_text_to_token_lifetime_textbox(0)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(10)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.control_auth_token_switches([False, True, True, True, True])
        self.auth_plugin.select_auth_get_token_test()
        assert self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))

    def test_08_verify_login_screen_shows_up_empty_scope(self):
        """
        C38256394 - Verify Login Screen shows up when nothing is passed as Scopes and after enabling SkipToken Refresh and set preferredMaximumSecondsSinceIssued as 0
        """
        self.auth_plugin.control_auth_token_switches([False, True, True, True, True])
        self.fc.call_auth_interaction_entry_point("signIn")
        self.auth_plugin.select_add_token_lifetime_option_btn()
        self.auth_plugin.change_token_type("preferredMaximumSecondsSinceIssued")
        self.auth_plugin.send_text_to_token_lifetime_textbox(0)
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))
        self.hpid.login(self.username, self.password)
        sleep(10)
        self.auth_plugin.send_text_to_scope_textbox("")
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_auth_get_token_test()
        assert self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack))