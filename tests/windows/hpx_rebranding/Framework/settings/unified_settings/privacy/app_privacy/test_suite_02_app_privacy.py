import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_02_App_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.regression
    def test_01_verify_term_of_use_navigation_C67516437(self):
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        assert self.hpx_settings.verify_settings_notifications_title(), "settings notification title invisible"
        assert self.hpx_settings.verify_privacy_tab_visible(), "privacy tab invisible"
        assert self.hpx_settings.verify_about_section_title(), "about section title invisible"
        assert self.hpx_settings.verify_terms_of_use(), "terms of use link invisible"
        self.hpx_settings.click_terms_of_use()
        assert self.devicesMFE.verify_browser_webview_pane(), "Browser webview pane is not visible"
        assert "support.hp.com/us-en/document/ish_12628951-12629012-16?openCLC=true" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect Webpage URL"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_02_verify_end_user_license_agreement_navigation_C67516438(self):
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        assert self.hpx_settings.verify_settings_notifications_title(), "settings notification title invisible"
        assert self.hpx_settings.verify_privacy_tab_visible(), "privacy tab invisible"
        assert self.hpx_settings.verify_about_section_title(), "about section title invisible"
        assert self.hpx_settings.verify_end_user_license_agreement(), "hp end user license agreement link invisible"
        self.hpx_settings.click_hp_end_user_license_agreement()
        assert self.devicesMFE.verify_browser_webview_pane(), "Browser webview pane is not visible"
        assert "support.hp.com/us-en/document/ish_4416646-4390016-16?openCLC=true" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_03_verify_end_user_license_agreement_navigation_C67516439(self):
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        assert self.hpx_settings.verify_settings_notifications_title(), "settings notification title invisible"
        assert self.hpx_settings.verify_privacy_tab_visible(), "privacy tab invisible"
        assert self.hpx_settings.verify_about_section_title(), "about section title invisible"
        assert self.app_consents.verify_ai_terms_of_use_link(), "ai terms of use link invisible"
        self.fc.kill_chrome_process()
        self.app_consents.click_ai_terms_of_use_link()
        assert self.devicesMFE.verify_browser_webview_pane(), "Browser webview pane is not visible"
        assert "support.hp.com/us-en/document/ish_12637390-12637445-16?openCLC=true" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect URL"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_04_consents_toggles_inactive_unless_transfer_consent_enabled_C53304046(self):
        self.fc.reset_myHP_app_through_command()
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")
        self.fc.change_system_region_to_china()
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        assert self.app_consents.verify_data_transfer_consent_for_china(), "Data transfer consent is not visible"
        assert self.app_consents.verify_product_improvement_china_is_enabled() is False, "Product improvement button is clickable"
        assert self.app_consents.verify_advertising_china_is_enabled() is False, "Advertising button is clickable"
        self.app_consents.click_data_transfer_consent_for_china()
        assert self.app_consents.verify_product_improvement_china_is_enabled() is True, "Product improvement button is not clickable"
        assert self.app_consents.verify_advertising_china_is_enabled() is True, "Advertising button is not clickable"

    @pytest.mark.regression
    def test_05_verify_app_only_consents_shown_during_fuf_C60498992(self):
        self.fc.reset_myHP_app_through_command()
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Unknown")
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        assert self.app_consents.verify_app_only_consents_screen(), "App only consents screen not shown during FUF"