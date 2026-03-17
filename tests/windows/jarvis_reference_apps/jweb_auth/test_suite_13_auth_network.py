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

class Test_Suite_13_Auth_Network(object):

    @pytest.mark.auth
    @pytest.mark.parametrize('bool_toggles', toggle_combinations)
    def test_01_verify_by_disabling_account_creation_option_C53045034(self, bool_toggles):
        """
        C53045034 and C57736382: Verify that the existing token is returned when "Allow Network Access?" is disabled
        """
        self.auth_plugin.control_auth_token_switches(bool_toggles)
        self.auth_plugin.select_auth_get_token_test()
        auth_get_token_result = self.auth_plugin.verify_error_code_result()
        assert auth_get_token_result["error"]["code"] == "networkNotAllowed"