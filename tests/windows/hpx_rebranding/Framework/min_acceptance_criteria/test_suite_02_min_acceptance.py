import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Min_Acceptance(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_login_and_logout_C51788443(self):
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        if logged_in:
            self.device_card.click_pc_devices_back_button()
            assert self.devicesMFE.verify_device_card_show_up(), "Devices card is not present"
            self.devicesMFE.click_device_card()
            self.devicesMFE.click_back_button_rebranding()
            self.hpx_settings.sign_out_from_settings()
        self.css.verify_sign_in_button_show_up()
        self.css.click_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.click_device_card()
        self.devicesMFE.click_back_button_rebranding()
        self.fc.close_myHP()
        self.profile.minimize_chrome()
        self.fc.web_password_credential_delete()
        self.fc.launch_myHP_command()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.click_back_button_rebranding()
        assert self.devicesMFE.verify_device_card_show_up(), "Devices card is not present"
