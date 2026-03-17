import pytest

pytest.app_info = "JWEB"

class Test_Suite_02_Auth_Plugin_Allow_User_Interaction(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.console = cls.fc.fd["console"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]

    toggle_combinations = [[False, True, False, False, True], [False, True, False, False, False],
                           [False, True, False, True, True], [False, True, False, True, False],
                           [True, True, False, False, True], [True, True, False, False, False],
                           [True, True, False, True, True], [True, True, False, True, False]]

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('toggle_combination', toggle_combinations)
    def test_01_verify_disabled_user_interaction_signin_user_not_logged(self, toggle_combination, entry_point):
        """
        C28698070: Verify by disabling the User Interaction Option (User Not Yet Signed In - Sign In)
            - after navigating to Auth Plugin, disable "Allow User Interaction," trying the combination defined in toggle_combinations
            - Select "SignIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting userInteractionNotAllowed error
        C28698073: Verify by disabling the User Interaction Option (User Not Yet Signed In - Create Account)
            - same as test above, except "Create Account" is our User Interaction Entry Point
        """
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        self.home.select_plugin_from_home("auth")
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(toggle_combination)
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()['error']['code'] == 'userInteractionNotAllowed'