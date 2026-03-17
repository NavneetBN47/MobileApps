import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Settings(object):
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
        cls.device_card = request.cls.fc.fd["device_card"]
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_verify_navigation_side_panel_from_device_list_page_C42631109_C53303756(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_verify_menu_button_present_on_settings_side_panel_C42631115_C53303760(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_menu_back_btn_from_settings(), "menu back button in settings missing"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_verify_functionality_of_menu_btn_C42631116_C53303761(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_menu_back_btn_from_settings(), "menu back button in settings missing"
        self.hpx_settings.click_menu_back_btn_from_settings()
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_04_verify_settings_option_global_side_panel_C42631113_C53303762(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        user_not_signed_in = self.profile.check_signin_btn_present()
        if user_not_signed_in:
            logging.info("User is not signed in")
        else:
            self.profile.verify_account_link()
            logging.info("User is signed in")

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_05_verify_clicking_on_settings_btn_C42631114_C53303763(self):
        self.device_card.click_pc_devices_back_button()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_device_card()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    @pytest.mark.skip_in_prod
    def test_06_verify_settings_side_panel_user_not_signed_in_C42631123_C53303764(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()