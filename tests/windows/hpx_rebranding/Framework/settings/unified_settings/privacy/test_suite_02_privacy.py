import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_02_Privacy(object):
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
    def test_01_verify_the_link_available_under_product_improvement_toogle_C59522304(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on homepage"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_side_panel(), "Profile side panel not visible"
        assert self.profile.verify_profile_settings_btn(), "Profile settings button not found"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents(), "Application Privacy Consents section not found"
        self.hpx_settings.click_device_privacy_arrow_button()
        assert self.hpx_settings.verify_computer_privacy_title(), "Computer Privacy title not found"
        self.hpx_settings.click_computer_privacy_product_improvement_link()
        url=self.energy_consumption.get_webpage_url()
        logging.info(f"Current URL is: {url}")
        assert url == "hpsmart.com/us/en/data-notice", "Incorrect URL"