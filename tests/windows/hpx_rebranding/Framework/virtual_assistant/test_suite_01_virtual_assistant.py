import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Virtual_Assistant(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.virtual_assistant = request.cls.fc.fd["virtual_assistant"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.device_card = request.cls.fc.fd["device_card"]
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_01_verify_end_session_C53542403(self):
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "Devices", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "My Computer", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        end_session_btn = self.virtual_assistant.verify_end_session_btn()
        assert end_session_btn == "End session", "Text on End Session button is incorrect"
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_end_session_btn()
        self.virtual_assistant.verify_end_session_overlay()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_keep_open_va_btn()
        self.virtual_assistant.verify_virtual_assistant_side_panel()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_end_session_btn()
        self.virtual_assistant.verify_end_session_overlay()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_close_va_btn()
        self.driver.swipe(distance=9, direction="up")
        self.device_card.verify_pc_devices_back_button()
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=False), "PC name on homepage not loaded/visible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_02_verify_text_box_C53542404(self):
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "Devices", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "My Computer", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        end_session_btn = self.virtual_assistant.verify_end_session_btn()
        assert end_session_btn == "End session", "Text on End Session button is incorrect"
        self.virtual_assistant.verify_enter_your_question()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.input_your_question("sound issue")
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_send_btn()
        self.virtual_assistant.verify_i_can_help_you_with()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_03_verify_feedback_btn_va_C53542405(self):
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "Devices", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "My Computer", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_feedback_va_btn()
        self.virtual_assistant.verify_feedback_prompt()
