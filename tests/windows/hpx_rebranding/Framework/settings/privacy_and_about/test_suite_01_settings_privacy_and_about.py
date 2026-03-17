import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Settings_Privacy_And_About(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.device_card = request.cls.fc.fd["device_card"]
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.ota
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_01_verify_privacy_statement_link_C58769270(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_privacy_tab_visible()
        assert self.hpx_settings.verify_privacy_statement_link(), "Privacy statement link is not present"
        self.hpx_settings.click_privacy_statement_link()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.kill_chrome_process()

    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.regression
    def test_02_verify_app_version_settings_C53303837_C53578727(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_version_about_show(), "app version is not visible"
        app_version = self.hpx_settings.get_app_version_copy_btn().split("+")[0]
        ssh_version = ".".join(self.fc.fd["display_control"].verify_myhp_app_version().strip().split(".")[:-1])
        logging.info(f"App Version: '{app_version}'")
        logging.info(f"SSH Version: '{ssh_version}'")
        assert app_version == ssh_version, f"App version '{app_version}' and SSH version '{ssh_version}' are not matching"

    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.regression
    def test_03_verify_terms_of_use_link_C58769314(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_terms_of_use(), "Terms of use link is not present"
        self.hpx_settings.click_terms_of_use()
        assert self.devicesMFE.verify_browser_webview_pane(), "Browser webview pane is not visible"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_04_manage_privacy_preferences_ui_C67872435(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_manage_privacy_title(), "Manage privacy title not found"
        self.hpx_settings.verify_application_privacy_consents()
        assert self.hpx_settings.verify_device_privacy_text(), "Device privacy text is not present"

    @pytest.mark.regression
    def test_05_device_privacy_visibility_C67872436(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        self.driver.swipe(distance=9)
        self.hpx_settings.click_device_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_consents(), "device privacy consents not found"

    @pytest.mark.regression
    def test_06_verify_version_is_not_clickable_C67872441(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()
        assert self.hpx_settings.verify_version_about_show(), "app version is not visible"
        self.hpx_settings.verify_version_read_only()
        self.hpx_settings.verify_settings_side_panel()

    @pytest.mark.regression
    def test_07_verify_visibility_of_manage_your_privacy_C67872434(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()
        assert self.hpx_settings.verify_privacy_tab_visible(), "privacy tab is not visible"
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"

    @pytest.mark.regression
    def test_08_verify_user_license_agreement_C58769316(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile Icon is missing from homepage"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()
        assert self.hpx_settings.verify_about_user_license_agreement(), "user license agreement link not found"
        self.hpx_settings.click_about_user_license_agreement()
        self.device_card.handle_feature_unavailable_popup()
        self.devicesMFE.verify_browser_webview_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        expected_tab_content = "End-User License Agreement | HP® Support - Google Chrome"
        assert tab_name in expected_tab_content, "tab name mismatch/browser not launched"
