import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_05_Sign_In_Sign_Out(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.css = request.cls.fc.fd["css"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_sign_in_C53303904(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_profile_icon_signed_in()
        assert self.profile.verify_account_link(), "account link invisible"
        self.profile.click_account_link()
        self.devicesMFE.verify_browser_webview_pane()

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_verify_user_profile_options_global_sidebar_C53303897(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_account_link(), "account link invisible"
        assert self.profile.verify_subscriptions_link(), "subscription link invisible"
        assert self.profile.verify_support_device_btn(), "support button invisible"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"

    @pytest.mark.regression
    def test_03_verify_user_stayed_signedin_after_relaunching_the_app_C53303907(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.fc.close_myHP()
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/logged out unexpectedly after relaunching the app"

    @pytest.mark.regression
    def test_04_verify_user_remains_signed_out_after_sign_out_and_relaunch_C53303908(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        self.profile.verify_global_sidebar_signed_in()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.click_sign_out_btn()
        assert self.profile.verify_navbar_sign_in_button(), "nav bar sign-in button missing"
        self.fc.close_myHP()
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.profile.verify_navbar_sign_in_button(), "nav bar sign-in button missing"

    @pytest.mark.regression
    def test_06_user_able_to_click_on_profile_after_signin_signout_C58998486(self):  
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.css.click_sign_in_btn_welcome_page()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.profile.verify_top_profile_icon_signed_in(), "User failed to sign in via external browser"
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP", "AH")," User initials after sign in do not match expected values"
        self.fc.kill_chrome_process()
        self.profile.click_profile_icon_signed_in()
        self.profile.click_close_avatar_btn()
        self.profile.click_profile_icon_signed_in()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.click_sign_out_btn()
        self.profile.click_profile_icon_show_up()
        assert self.profile.verify_devicepage_avatar_btn(), "Avatar button on device details page not visible after signing out from profile settings"

