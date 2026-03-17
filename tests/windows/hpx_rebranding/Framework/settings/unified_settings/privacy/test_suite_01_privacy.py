import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.energy_consumption = request.cls.fc.fd["energy_consumption"]
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        request.cls.fc.web_password_credential_delete()
        request.cls.fc.change_system_region_to_china()
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    @pytest.mark.ota
    def test_01_verify_manage_privacy_settings_option_C58769275(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        assert self.verify_manage_privacy_btn(), "manage privacy settings button invisible"

    @pytest.mark.regression
    def test_02_verify_hp_privacy_statement_navigated_to_external_browser_C58769312(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_privacy_statement_link(), "HP privacy statement link invisible"
        self.hpx_settings.click_privacy_statement_link()
        url=self.energy_consumption.get_webpage_url()
        logging.info(f"Current URL is: {url}")
        assert url == "hp.com/sg-en/privacy/privacy-central.html", "Incorrect URL"
