import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures()
class Test_Suite_06_Settings_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        request.cls.fc.web_password_credential_delete()
        request.cls.fc.change_system_region_to_china()
        yield
        request.cls.fc.consent_managed_registry_key(request.cls.driver.ssh, condition=False)
        request.cls.fc.consent_allow_marketing(request.cls.driver.ssh, condition=False)
        request.cls.fc.change_system_region_to_united_states()



    @pytest.mark.regression
    def test_01_verify_computer_privacy_page_ui_and_contents_C58769279(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.reset_myHP_app_through_command()
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept all button not found on app consents screen"
        self.app_consents.click_accept_all_button()
        assert self.app_consents.verify_continue_as_guest_button_show_up(), "Continue as guest button not found on PC consents screen"
        self.app_consents.click_continue_as_guest_button()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_side_panel(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents(), "Application Privacy Consents section not found"
        self.hpx_settings.click_device_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_consents(), "Device Privacy Consents section not found"
        assert self.hpx_settings.verify_customer_support_consent(), "Customer support consent title missing"
        assert self.hpx_settings.verify_computer_privacy_customer_support_description_text(),  "Customer support description missing"
        assert self.hpx_settings.verify_computer_privacy_product_improvement_text(), "Product improvement description missing"
        assert self.hpx_settings.verify_computer_privacy_advertising_description_text(), "Advertising description missing"
      
    @pytest.mark.regression  
    def test_02_verify_consents_set_on_selecting_accepted_all_on_app_and_pc_fuf_consents_screen_C58769290(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition=True)
        self.fc.reset_myHP_app_through_command()
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept all button not found on app consents screen"
        self.app_consents.click_accept_all_button()
        assert self.app_consents.verify_continue_as_guest_button_show_up(), "Continue as guest button not found on PC consents screen"
        self.app_consents.click_continue_as_guest_button()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_side_panel(), "Profile side panel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents(), "Application Privacy Consents section not found"
        assert self.hpx_settings.get_manage_privacy_product_improvement_toggle_state() == "ON", "Product improvement toggle should be ON after giving accept all consents"
        assert self.hpx_settings.get_manage_privacy_advertising_toggle_state() == "ON", "Advertising toggle should be ON after giving accept all consents"
        self.hpx_settings.click_device_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_consents(), "Device Privacy Consents section not found"
        assert self.hpx_settings.verify_customer_support_consent(), "Customer support consent title missing"
        assert self.hpx_settings.get_computer_privacy_customer_support_toggle_state() == "ON", \
            "Customer Support toggle is OFF after giving accept all consents"
        assert self.hpx_settings.get_computer_privacy_product_improvement_toggle_state() == "ON", \
            "Product Improvement toggle is OFF after giving accept all consents"
        assert self.hpx_settings.get_computer_privacy_advertising_toggle_state() == "ON", \
            "Advertising toggle is OFF after giving accept all consents"


