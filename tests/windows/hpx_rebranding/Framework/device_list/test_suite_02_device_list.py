import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Device_List(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        request.cls.web_driver = utility_web_session
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.profile= request.cls.fc.fd["profile"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()
    
    @pytest.mark.regression
    def test_01_verify_sign_in_from_device_list_navigation_with_user_initials_C58931318(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), " Back to devices button is not displayed"
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devicesMFE.verify_device_card_show_up(raise_e=True), "Device List page not displayed"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP", "AH")," User initials after sign in do not match expected values"

        

