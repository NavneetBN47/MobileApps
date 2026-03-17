import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_08_Settings_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        yield
        request.cls.fc.consent_managed_registry_key(request.cls.driver.ssh, condition=False)
        request.cls.fc.consent_allow_marketing(request.cls.driver.ssh, condition="Accepted")
        request.cls.fc.consent_allow_product_enhancement(request.cls.driver.ssh, condition="Accepted")
        request.cls.fc.consent_allow_support(request.cls.driver.ssh,condition="Accepted")

    @pytest.mark.regression
    def test_01_verify_managed_devices_functionality_C60498989(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Rejected")
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_text(), "Device privacy text is not displayed"        
        self.hpx_settings.click_device_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_consents(), "Device privacy consents are not displayed"
        actual_warning_msg = self.hpx_settings.get_system_admin_warning_msg()
        expected_warning_msg = "Some preferences can only be changed by a system administrator."
        assert expected_warning_msg == actual_warning_msg, "Warning message text is mismatching"
        assert self.hpx_settings.get_computer_privacy_customer_support_toggle_state() == "OFF", "customer support toggle is ON"
        assert self.hpx_settings.get_computer_privacy_product_improvement_toggle_state() == "OFF", "product improvement toggle should is ON"
        assert self.hpx_settings.get_computer_privacy_advertising_toggle_state() == "OFF", "advertising toggle should is ON"
        