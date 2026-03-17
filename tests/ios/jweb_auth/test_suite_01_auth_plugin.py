import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web import const as w_const
from time import sleep

pytest.app_info = "JWEB_AUTH"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_auth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_auth_setup
        cls.home = cls.fc.fd["home"]
        cls.jweb_auth_settings = cls.fc.fd["jweb_auth_settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.stack = request.config.getoption("--stack")

        test_account = cls.fc.get_jweb_auth_test_data(cls.stack)
        cls.username = test_account["username"]
        cls.password = test_account["password"]
        cls.tenant_id = test_account["tenant_id"]
        cls.scope = test_account["scope"]
        cls.resource = test_account["resource"]

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        """
        Enable allow network access, user interaction, and show account creation link
        """
        self.fc.close_app()
        self.fc.flow_load_home_screen()
        self.home.select_top_bar_button('Plugin', raise_e=False)
        self.auth_plugin.select_send_token_options(True)
        self.auth_plugin.control_auth_token_switches([False, True, True, True, False])
        yield None
        self.auth_plugin.select_auth_logout_test()

    def test_01_validate_return_of_token(self):
        """
        C31686066: Validate the return of access token after signing in
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart
            - expecting Access Token to be retrieved  
        C31740201: Validate the return of device token after signing in
            - login using the steps defined in C31686066
            - select Token Type as Device, with scope as 'IPPPrint.v1' 
            - set resource value to 'urn:uuid:47a5f948-78ac-415a-9d99-18661113c2f5' and select test
            - expecting device token in returned in login result
        """
        self.auth_plugin.select_token_type_to_request('user')
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_auth_get_token_test()
        sleep(2)
        self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['tenantID'] is not None
        self.auth_plugin.select_token_type_to_request('device')
        self.auth_plugin.send_text_to_scope_textbox(self.scope)
        self.auth_plugin.send_text_to_device_uuid_textbox(self.resource)
        self.auth_plugin.select_auth_get_token_test()
        token_result = self.auth_plugin.auth_get_token_result()
        assert 'tokenOptions' in token_result, f"tokenOptions not found in result: {token_result}"
        assert self.auth_plugin.auth_get_token_result()['tokenOptions']['printerUuid'] is not None
    
    def test_02_validate_return_of_access_token(self):
        """
        C31740202: Validate the return of access token after creating account
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Create Account
            - click on test, and create a new HPSmart account
            - expecting Access Token to be retrieved  
        """
        self.auth_plugin.select_user_interaction_entry_point('createAccount')
        self.auth_plugin.select_auth_get_token_test()
        self.hpid.create_account()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
    
    def test_03_validate_login_and_return_of_device_token_disabled_network(self):
        """
        C31740205: Validate the return of device token after signing in by disabling the allow network access
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart, expecting Access Token to be retrieved  
            - Disable the allow network access option, select Token Type as Device, with scope as 'IPPPrint.v1' 
            - set resource value to 'urn:uuid:47a5f948-78ac-415a-9d99-18661113c2f5' and select test
            - expecting device token in returned in login result
        """
        self.auth_plugin.select_token_type_to_request('user')
        self.auth_plugin.send_text_to_scope_textbox("openid")
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_get_token_test()
        if not self.auth_plugin.auth_get_token_result(raise_e=False):
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.control_auth_token_switches([False, False, True, True, False])
        self.auth_plugin.select_token_type_to_request('device')
        self.auth_plugin.send_text_to_scope_textbox(self.scope)
        self.auth_plugin.send_text_to_device_uuid_textbox(self.resource)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    def test_04_validate_creation_and_return_of_device_token_disabled_network(self):
        """
        C31740206: Validate the return of device token after creating account by disabling the allow network access 
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Create Account
            - click on test, and create a new HPSmart account
            - expecting Access Token to be retrieved
            - Disable the allow network access option, select Token Type as Device, with scope as 'IPPPrint.v1' 
            - set resource value to 'urn:uuid:47a5f948-78ac-415a-9d99-18661113c2f5' and select test
            - expecting device token in returned in login result
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_user_interaction_entry_point('createAccount')
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
        self.hpid.create_account()
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.control_auth_token_switches([False, False, True, True, False])
        self.auth_plugin.select_token_type_to_request('device')
        self.auth_plugin.send_text_to_scope_textbox(self.scope)
        self.auth_plugin.send_text_to_device_uuid_textbox(self.resource)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "networkNotAllowed"

    def test_05_validate_login_and_error_without_mentioning_scope(self):
        """
        C31686067: Validate the return of device token after signing in without mentioning scope
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart, expecting Access Token to be retrieved  
            - set token type as Device, and leave Scope without text, and set  resource value to 'urn:uuid:47a5f948-78ac-415a-9d99-18661113c2f5'
            - select test, expecting error code with "invalidOption"
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_get_token_test()
        if not self.auth_plugin.auth_get_token_result(raise_e=False):
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_token_type_to_request('device')
        self.auth_plugin.send_text_to_device_uuid_textbox(self.resource)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "invalidOption"
    
    def test_06_validate_login_and_error_without_mentioning_resource(self):
        """
        C31686067: Validate the return of device token after signing in without mentioning resource
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart, expecting Access Token to be retrieved  
            - set token type as Device, and scope as 'IPPPrint.v1', and leave resource value blank
            - select test, expecting invalidOption error with details asking for Scope and Device UUID to be provided
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_get_token_test()
        if not self.auth_plugin.auth_get_token_result(raise_e=False):
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.send_text_to_tenant_id_textbox(self.tenant_id)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['tenantID'] is not None
        self.auth_plugin.select_token_type_to_request('device')
        self.auth_plugin.send_text_to_scope_textbox(self.scope)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "invalidOption"
        assert "printeruuid" in self.auth_plugin.auth_get_token_result()['error']['reason'].lower()

    def test_07_validate_login_and_error_without_mentioning_scope_and_resource(self):
        """
        C31686067: Validate the return of device token after signing in without mentioning resource
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart, expecting Access Token to be retrieved  
            - set token type as Device, and scope as and leave resource value and scope as blank
            - select test, expecting invalidOption error with details asking for Scope and Device UUID to be provided
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_get_token_test()
        if not self.auth_plugin.auth_get_token_result(raise_e=False):
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_token_type_to_request('device')
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == "invalidOption"
        assert "printeruuid" in self.auth_plugin.auth_get_token_result()['error']['reason'].lower()

    def test_08_validate_logout_method(self):
        """
        C31740209: Validate the logout out method after signing in
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart, expecting Access Token to be retrieved
            - go to Auth.logout() and click on test
            - expecting a pop up saying "Logout"
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_get_token_test()
        if not self.auth_plugin.auth_get_token_result(raise_e=False):
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result() == {}

    def test_09_validate_logout_method(self):
        """
        C31740210: Validate the logged in out method after signing in
            - after navigating to the Auth Plugin, click on set set subscriber, allow send token options, and set token type as user
            - enable allowing Network Access, User Interaction, and Show Account Creation Link, with the scope set to openid, and interaction as Sign In
            - click on test, and sign in to HPSmart, expecting Access Token to be retrieved
            - go to Auth.isLoggedIn() and click on test
            - expecting returned result of True
        """
        self.auth_plugin.select_set_set_subscriber_btn()
        self.auth_plugin.select_auth_get_token_test()
        if not self.auth_plugin.auth_get_token_result(raise_e=False):
            self.driver.wait_for_context(w_const.WEBVIEW_URL.HPID(self.fc.stack), timeout=30)
            self.hpid.login(self.username, self.password)
        assert 'tokenValue' in self.auth_plugin.auth_get_token_result()
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()['value']