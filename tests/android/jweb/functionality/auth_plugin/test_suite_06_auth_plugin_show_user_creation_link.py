import pytest

pytest.app_info = "JWEB"

class Test_Suite_06_Auth_Plugin_Show_User_Creation_Link_Option(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.console = cls.fc.fd["console"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]
        cls.hpid = cls.fc.fd["hpid"]

    toggle_combinations = [[True, True, True, False, True], [True, True, True, False, False]]

    @pytest.mark.parametrize('entry_point', ["signIn", "createAccount"])
    @pytest.mark.parametrize('toggle_combination', toggle_combinations)
    def test_01_verify_by_disabling_account_creation(self, toggle_combination, entry_point):
        """
        C28715448: Verify by disabling the Account Creation Option (User not yet logged in - Sign In)
            - after navigating to Auth Plugin, disable "Show Account Creation Link" checkbox, and try all toggle_combinations for other the options
            - select "Sign In" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting HP Smart sign in page with no account creation button present
        C28715449: Verify by disabling the Account Creation Option (User not yet logged in - Create Account)
            - after navigating to Auth Plugin, disable "Show Account Creation Link" checkbox, and try all toggle_combinations for other the options
            - select "Create Account" as the User Interaction Entry Point, and click on Test under Auth.getToken()
            - expecting HP Smart Create Account Page
        """
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        self.home.select_plugin_from_home("auth")
        self.auth_plugin.select_user_interaction_entry_point(entry_point)
        self.auth_plugin.control_auth_token_switches(toggle_combination)
        self.auth_plugin.select_auth_get_token_test()
        if entry_point == "signIn":
            assert self.hpid.verify_create_an_account_page() is False
        else:
            assert self.hpid.verify_create_an_account_page() is True