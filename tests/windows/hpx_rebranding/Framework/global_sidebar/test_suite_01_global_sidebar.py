import logging
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Global_Side_Bar(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.feedback = request.cls.fc.fd["feedback"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.stack = request.config.getoption("--stack")
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_user_not_signed_in_C53303683(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_sign_in_create_account_btn(), "sign-in/create acc button invisible"
        self.profile.click_sign_in_create_account_btn()
        self.devicesMFE.verify_browser_webview_pane()
        assert self.hpx_support.verify_create_account_btn(), "create account button invisible"
        assert self.hpx_support.verify_username_or_email_placeholder(), "username or email invisible"
        assert self.hpx_support.verify_sign_in_mobile_num(), "sign-in using mobile number invisible"
        assert self.hpx_support.verify_use_password_btn(), "use password button invisible"
        tab_name = self.hpx_support.get_browser_tab_name()
        expected_tab_name = "HP account - Google Chrome"
        assert expected_tab_name in tab_name, "tab name mismatch/browser not launched"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_navigate_to_support_page_C53303684(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel invisible"
        assert self.profile.verify_support_device_btn(), "support device button invisible"
        self.profile.click_support_device_btn()
        if self.stack == "rebrand_production":
            self.profile.click_support_link()
            self.devicesMFE.verify_browser_webview_pane()
            self.feedback.handle_feature_feedback_popup()
            tab_name = self.hpx_support.get_browser_tab_name()
            expected_tab_name = ["My Dashboard | HP® Customer Support", "Add Device"]
            assert any(name in tab_name for name in expected_tab_name), f"tab name mismatch: got '{tab_name}', expected one of {expected_tab_name}"
            self.hpx_support.verify_support_home_navbar_btn()
            self.hpx_support.verify_contact_us_navbar_btn()
            self.hpx_support.verify_business_support_navbar_btn()
            self.hpx_support.verify_support_home_link()
            self.hpx_support.verify_printing_support_link()
            self.hpx_support.verify_computing_support_link()
        else:
            logging.info("Support link is not available in ITG & STG builds")

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_navigate_to_settings_page_C53303686(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel invisible"
        assert self.profile.verify_profile_settings_btn(), "profile settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_settings_header(), "settings header invisible"
        assert self.hpx_settings.verify_privacy_tab_visible(), "Privacy tab is not visible"
        assert self.hpx_settings.verify_privacy_statement_link(), "Privacy statement link invisble"
        assert self.hpx_settings.verify_terms_of_use(), "Terms of use link invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_04_navigate_to_feedback_page_C53303687(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel invisible"
        assert self.profile.verify_feedback_btn(), "feedback button invisible"
        self.profile.click_feedback_btn()
        assert self.feedback.verify_feedback_slide_title(), "feedback side panel invisible"
        assert self.feedback.verify_menu_btn_from_feedback(), "menu button in feedback page invisible"
        assert self.feedback.verify_rating_star_field(), "Rating star field in feedback page invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_05_validate_close_button_C53303688(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel invisible"
        assert self.profile.verify_avatar_close_btn(), "close button in profile side panel invisible"
        self.profile.click_close_avatar_btn()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_06_validate_app_window_resize_C53303689(self):
        self.devicesMFE.restore_app()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.device_card.handle_feature_unavailable_popup()
        self.devicesMFE.verify_browser_webview_pane()
        assert self.hpx_support.verify_browser_login_page(), "login page invisible"
