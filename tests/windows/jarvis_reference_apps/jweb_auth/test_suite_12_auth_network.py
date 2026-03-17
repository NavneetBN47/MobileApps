import pytest

pytest.app_info = "JWEB_AUTH"

toggle_combinations = [[False, False, False, False, True], [False, False, False, False, False],
                       [False, False, False, True, True], [False, False, False, True, False], 
                       [False, False, True, False, True], [False, False, True, False, False],
                       [False, False, True, True, True], [False, False, True, True, False],
                       [True, False, False, False, True], [True, False, False, False, False],
                       [True, False, False, True, True], [True, False, False, True, False],
                       [True, False, True, False, True], [True, False, True, False, False],
                       [True, False, True, True, True], [True, False, True, True, False]]

class Test_Suite_12_Auth_Network(object):

    @pytest.mark.auth
    @pytest.mark.parametrize('entry_point', ["sign_in"])
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_01_verify_by_disabling_the_network_access_option_C53045014(self, entry_point, bool_toggles):
        """
        C53045014: Verify by disabling the Network aAccess option (User has logged in and the access token expired-Create Account)
            - after navigating to Auth Plugin, disable "Allow Network access," trying the combination defined in toggle_combinations
            - Select "SignIn" as User Interaction Entry Point, click Test under Auth.getToken()
            - expecting networkNotAllowed error
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.fc.call_auth_interaction_entry_point(entry_point)
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "networkNotAllowed"