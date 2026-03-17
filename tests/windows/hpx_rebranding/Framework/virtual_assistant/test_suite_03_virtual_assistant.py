import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_03_Virtual_Assistant(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.virtual_assistant = request.cls.fc.fd["virtual_assistant"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.profile.minimize_chrome()
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_01_va_sign_in_C53542408(self):
        self.css.verify_sign_in_button_show_up()
        self.css.click_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        self.profile.minimize_chrome()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=False), "After sign-in, device details page did not load"
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        self.virtual_assistant.verify_feedback_va_btn()
        self.virtual_assistant.verify_start_over_btn()
        self.fc.close_myHP()
        self.fc.web_password_credential_delete()
