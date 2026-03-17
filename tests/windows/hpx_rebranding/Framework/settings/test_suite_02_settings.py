import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Settings(object):
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
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_verify_settings_side_panel_user_is_signed_in_C42631124_C53303765(self):
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_profile_icon_signed_in()
        self.profile.verify_account_link()
        assert self.profile.verify_support_device_btn(), "Support button is missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_settings_side_panel()
        assert self.hpx_settings.verify_sign_out_btn(), "Sign out button is missing from settings side panel"

    @pytest.mark.regression
    @pytest.mark.ota
    def test_02_verify_sign_out_button_available_on_settings_C58797407(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_profile_icon_signed_in()
        self.profile.verify_global_sidebar_signed_in()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_sign_out_btn(), "Sign out button is missing from settings side panel"
        self.hpx_settings.click_sign_out_btn()
        self.fc.close_myHP()
        self.fc.launch_myHP_and_skip_fuf()
        self.devicesMFE.click_profile_and_settings_icon_button_lzero_page()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_sign_out_after_clicking_sign_out_btn() == False, "Sign out button is still present after signing out"