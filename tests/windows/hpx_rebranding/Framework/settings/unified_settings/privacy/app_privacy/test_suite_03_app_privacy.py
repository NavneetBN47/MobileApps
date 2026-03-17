import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_03_App_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.energy_consumption = request.cls.fc.fd["energy_consumption"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.regression
    def test_01_verify_the_link_here_available_under_advertising_toogle_C59522303(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on homepage"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_side_panel(), "Profile side panel not visible"
        assert self.profile.verify_profile_settings_btn(), "Profile settings button not found"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is True
        assert self.hpx_settings.verify_here_link_in_advertising_toggle(), "'here' link not found under advertising toggle"
        self.hpx_settings.click_here_link_in_advertising_toggle()
        url=self.energy_consumption.get_webpage_url()
        logging.info(f"Current URL is: {url}")
        assert url == "hpsmart.com/us/en/plain/data-sharing-notice", "Incorrect URL"

    



        