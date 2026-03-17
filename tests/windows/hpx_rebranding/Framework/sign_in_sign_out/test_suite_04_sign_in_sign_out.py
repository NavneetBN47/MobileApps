import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_04_Sign_In_Sign_Out(object):
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
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_verify_user_initials_are_visible_device_card_C53303906(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.get_user_initials_after_signin()
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        self.profile.get_user_initials_after_signin()
        self.profile.click_top_profile_icon_signed_in()
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP"), "User not signed in/credentials not matching"

    @pytest.mark.regression
    def test_02_verify_user_initials_are_visible_C53303895(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.get_user_initials_after_signin()
        self.profile.click_top_profile_icon_signed_in()
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP"), "User not signed in/credentials not matching"

    @pytest.mark.regression
    def test_03_verify_sign_out_btn_C53303898(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_profile_icon_signed_in()
        self.profile.verify_global_sidebar_signed_in()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_sign_out_btn(), "sign out button missing"

    @pytest.mark.regression
    def test_04_verify_user_sign_out_C53303899(self):
        self.profile.click_navbar_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_profile_icon_signed_in()
        self.profile.verify_global_sidebar_signed_in()
        self.profile.click_profile_settings_btn()
        self.profile.minimize_hp()
        self.hpx_settings.click_myhp_on_task_bar()
        self.hpx_settings.click_sign_out_btn()
        assert self.devicesMFE.verify_device_card_show_up(), "Device card page not showing up after sign out"
        self.profile.verify_navbar_sign_in_button()