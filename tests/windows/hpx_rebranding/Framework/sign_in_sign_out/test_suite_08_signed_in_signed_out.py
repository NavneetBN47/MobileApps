import pytest

from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_08_Sign_In_Sign_Out(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()
        
     
    @pytest.mark.regression
    def test_01_verify_direct_signin_via_nav_panel_C53303896(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.profile.click_profile_icon_show_up()
        assert self.profile.verify_profile_side_panel(), "Profile side panel is not displayed"
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name is not visible after signing in"
        assert self.profile.verify_top_profile_icon_signed_in(), "App is not signed in successfully"
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP","AH","UN"),  f"User initials '{user_initials}' do not match expected values after sign-in."
        
    @pytest.mark.regression
    def test_02_verify_delete_account_link_hidden_C57437649(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "Sign in button is not present on devices MFE page"
        self.profile.click_profile_icon_show_up()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy settings button is not present"
        assert not self.profile.verify_delete_your_account_link(), "Delete Your Account link is visible"
 
   