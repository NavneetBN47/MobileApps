import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_03_Signin_And_Navigate(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.feedback = request.cls.fc.fd["feedback"]
        cls.css = request.cls.fc.fd["css"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.accessibility = request.cls.fc.fd["accessibility"]
        cls.stack = request.config.getoption("--stack")
        request.cls.fc.web_password_credential_delete()
        cls.profile.minimize_chrome()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_navigate_to_support_page_C55175097_C53303900(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_signed_in_profile_icon()
        self.profile.click_support_device_btn()
        if self.stack == "rebrand_production":
            self.hpx_support.verify_support_side_panel("support_link")
        else:
            self.hpx_support.verify_support_side_panel()
        self.hpx_settings.go_home_from_settings_and_support("support_page")

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_navigate_to_settings_page_C55175099_C53303902(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_signed_in_profile_icon()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()
        self.hpx_settings.go_home_from_settings_and_support()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_navigate_to_feedback_C55175100_C53303903(self):
        assert self.profile.verify_devicepage_avatar_btn(), "avatar icon missing"
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_feedback_btn(), "feedback button invisible"
        self.profile.click_feedback_btn()
        self.feedback.verify_feedback_slide_title()
        self.feedback.click_menu_btn_from_feedback()
        self.profile.click_close_avatar_btn()

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_04_navigate_to_subscription_page_C53303901(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_profile_icon_signed_in()
        self.profile.verify_global_sidebar_signed_in()
        assert self.profile.verify_subscriptions_link(), "subscription link missing"
        self.profile.click_subscriptions_link()
        self.hpx_support.verify_browser_pane()

    @pytest.mark.regression
    def test_05_hp_logo_on_uto_page_C59594127(self):
        self.profile.click_navbar_sign_in_button()
        self.accessibility.verify_hp_app_icon_in_windows_settings()

    @pytest.mark.regression
    def test_06_hp_logo_on_uto_page_C59793312(self):
        self.profile.click_navbar_sign_in_button()
        self.profile.verify_and_click_on_try_again_text()
        self.profile.verify_navbar_sign_in_button()


    