import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.skip_kill_chrome
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_06_Signin_And_Navigate(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.css = request.cls.fc.fd["css"]
        cls.stack = request.config.getoption("--stack")
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_login_auth_via_external_browser_existing_user_C53303916(self):
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept All button not showing up on App only consents screen"
        assert self.app_consents.verify_manage_choices_btn(), "Manage Choices button not showing up on App only consents screen"
        assert self.app_consents.verify_decline_optional_data(), "Decline Optional Data button not showing up on App only consents screen"
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.app_consents.click_manage_choice_continue_btn()
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.css.click_sign_in_btn_welcome_page()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.profile.verify_top_profile_icon_signed_in(), "User failed to sign in via external browser"
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP", "AH")," User initials after sign in do not match expected values"
        self.fc.kill_chrome_process()