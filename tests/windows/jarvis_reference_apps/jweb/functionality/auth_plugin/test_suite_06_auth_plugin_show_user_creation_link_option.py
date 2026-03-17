import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "JWEB"

toggle_combinations = [[True, True, True, False, True],
                       [True, True, True, False, False]]
entry_points = ['sign_in', 'create_account']

class Test_Suite_06_Auth_Plugin_Show_User_Creation_Link_Option(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, jweb_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]

        cls.home.click_maximize()

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_auth_plugin(self):
        self.fc.navigate_to_auth_plugin()
        self.auth_plugin.select_auth_logout_test()

    @pytest.fixture()
    def login_to_hpid(self):
        self.fc.login_to_hpid()

    @pytest.fixture()
    def logout_from_hpid(self):
        self.auth_plugin.select_auth_logged_in_test()
        if self.auth_plugin.auth_logged_in_result()["value"] is not False:
            self.auth_plugin.select_auth_logout_test()

    @pytest.mark.parametrize('entry_point', entry_points)
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_01_verify_by_disabling_account_creation_not_logged_in(self, entry_point, bool_toggles, logout_from_hpid):
        """
        C28715448: Verify by disabling the Account creation option(User not yet logged in; access token-Sign In)
            - After navigating to Auth Plugin, disable "Show Account creation Link?" checkbox, and try all checkbox combination defined within the test
            - Select "Sign In" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - Expecting HPID Login Page to open without the create account link present 
        C28715449: Verify by disabling the Account creation option(User not yet logged in; access token-Create Account)
            - Same as above, except select "Create Account" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - Expecting HPID to open with create account page open
        """
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test(change_check=False)
        if entry_point == 'sign_in':
            assert not self.hpid.verify_create_an_account_page(visible=True)
        elif entry_point == 'create_account':
            assert self.hpid.verify_create_an_account_page()
        self.home.click_close_pop_up('Popup Window')

    @pytest.mark.parametrize('entry_point', entry_points)
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_02_verify_by_disabling_account_creation_logged_in(self, login_to_hpid, entry_point, bool_toggles):
        """
        C28715496: Verify by disabling the Account creation option(User has logged in; access token-Sign in)
            - After navigating to the Auth Plugin, sign into HPID account via toggling all options to True and selecting Test
            - Select "Sign In" with all of the checkbox  combinations defined within the test, clicking Test under Auth.getToken()
            - If SkipRefreshToken is toggled on, expecting a redirect to the HPID login page without a create account link present
            - If SkipRefreshToken is toggled off, expecting an updated Token value to be updated within the results of Auth.getToken()
        C28715497: Verify by disabling the Account creation option(User has logged in; access token-Create Account)
            - Same as above, except select "Create Account" as User Interaction Entry Point, and click on Test under Auth.getToken()
            - If SkipRefreshToken is toggled on, expecting a redirect to the create account page
            - If SkipRefreshToken is toggled off, expecting an updated Token value to be updated within the results of Auth.getToken()
        """
        if self.auth_plugin.auth_get_token_result() is False:
            sleep(5)
        token = self.auth_plugin.auth_get_token_result()['tokenValue']
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test(change_check=False)
        if entry_point == 'create_account':
            assert token == self.auth_plugin.auth_get_token_result()['tokenValue']
        elif entry_point == 'sign_in':
            assert not self.hpid.verify_create_an_account_page()
        self.home.click_close_pop_up('Popup Window', raise_e=False)
