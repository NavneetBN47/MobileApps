import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.skip_kill_chrome
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_02_Welcome_Screen(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.css = request.cls.fc.fd["css"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_user_signed_in_and_app_reset_C53542650(self):
        self._function_setup()
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.css.click_sign_in_btn_welcome_page()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present on homepage"
        self.fc.close_myHP()
        self.fc.web_password_credential_delete()


######################################################################
#                               PRIVATE FUNCTIONS                    #
######################################################################

    def _function_setup(self):
        if self.app_consents.verify_accept_all_button_show_up():
            self.app_consents.click_accept_all_button()
