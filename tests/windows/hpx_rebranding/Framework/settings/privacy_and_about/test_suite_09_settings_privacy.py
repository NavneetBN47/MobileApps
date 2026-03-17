import pytest

from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_09_Settings_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        
    @pytest.mark.regression
    def test_01_verify_consents_set_on_selecting_decline_optional_data_on_app_visiblity_C58769294(self):
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.reset_myHP_app_through_command()
        self.app_consents.verify_decline_optional_data()
        self.app_consents.click_decline_optional_data_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"        
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents page not displayed"
        assert self.hpx_settings.get_manage_privacy_product_improvement_toggle_state() == "OFF", "Product improvement toggle is ON"
        assert self.hpx_settings.get_manage_privacy_advertising_toggle_state() == "OFF", "Advertising toggle is ON"
        self.hpx_settings.verify_device_privacy_text()
        self.hpx_settings.click_device_privacy_btn()
        self.hpx_settings.verify_device_privacy_consents()
        assert self.hpx_settings.get_computer_privacy_customer_support_toggle_state() == "OFF", "customer support toggle is ON"
        assert self.hpx_settings.get_computer_privacy_product_improvement_toggle_state() == "OFF", "product improvement toggle should is ON"
        assert self.hpx_settings.get_computer_privacy_advertising_toggle_state() == "OFF", "advertising toggle should is ON"

    @pytest.mark.regression
    def test_02_verify_consents_set_on_selecting_decline_optional_data_C58769296(self):
        self.fc.reset_myHP_app_through_command()
        assert self.app_consents.verify_decline_optional_data(), "Decline optional data is not visible"
        self.app_consents.click_decline_optional_data_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_settings_btn(), "Profile settings button is not displayed"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button is not displayed"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        self.hpx_settings.verify_application_privacy_consents()
        assert self.hpx_settings.get_manage_privacy_product_improvement_toggle_state() == "OFF", "Product improvement toggle should be OFF after declining optional data"
        assert self.hpx_settings.get_manage_privacy_advertising_toggle_state() == "OFF", "Advertising toggle should be OFF after declining optional data"