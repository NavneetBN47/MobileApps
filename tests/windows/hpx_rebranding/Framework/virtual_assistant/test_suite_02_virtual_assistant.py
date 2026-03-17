import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_02_Virtual_Assistant(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.virtual_assistant = request.cls.fc.fd["virtual_assistant"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_01_verify_clicked_start_over_btn_va_C53542406(self):
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        self.virtual_assistant.verify_minimize_btn_va()
        self.virtual_assistant.verify_va_start_messages()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_start_over_btn()
        self.virtual_assistant.verify_start_over_form()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_start_over_with_a_new_issue_btn()
        self.virtual_assistant.verify_va_start_messages()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_02_verify_click_hp_privacy_va_C53542407(self):
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        self.virtual_assistant.verify_va_start_messages()
        self.virtual_assistant.verify_bottom_privacy_btn()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_va_bottom_privacy_btn()
        actual_tab_name = self.hpx_support.get_browser_tab_name()
        privacy_tab_name = "HP Privacy Central"
        assert privacy_tab_name in actual_tab_name, "privacy link tab name mismatch/tab taken more then 5 seconds to load"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_stg
    def test_03_verify_virtual_assistant_C53542402(self):
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.click_start_virtual_assistant()
        va_back_btn_text = self.virtual_assistant.verify_text_on_back_btn_va()
        assert va_back_btn_text == "button", "Text on back button of VA issue selection page is not as expected"
        self.virtual_assistant.navigate_to_va_chat_window()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.select_pc_btn()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.choose_performance()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_yes_btn()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        chromebook_card = self.virtual_assistant.verify_chromebook_card()
        if chromebook_card:
            self.virtual_assistant.click_chromecard_no_btn()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.verify_hp_pc_updating_driver_link()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.virtual_assistant.click_hp_pc_updating_driver_link()
        self.virtual_assistant.handle_feature_unavailable_popup()
        actual_tab_name = "HP PCs - Updating drivers using Windows Update (Windows 11, 10) | HP® Support - Google Chrome"
        tab_name = self.hpx_support.get_browser_tab_name()
        assert tab_name in actual_tab_name, "driver link tab name mismatch/tab taken more then 5 seconds to load"
        self.fc.kill_chrome_process()
