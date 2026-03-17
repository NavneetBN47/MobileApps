import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_App_privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.profile = request.cls.fc.fd["profile"]
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        request.cls.fc.web_password_credential_delete()
        request.cls.fc.change_system_region_to_china()
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_consents_settings_privacy_C58769292(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents missing"
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked(), "Product improvement toggle not clicked"
        assert self.hpx_settings.verify_advertising_toggle_is_clicked(), "Advertising toggle not clicked"

    @pytest.mark.regression
    def test_02_verify_here_link_in_advertising_toggle_C59522303(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents missing"
        assert self.hpx_settings.verify_here_link_in_advertising_toggle(), "Here link in advertising toggle missing"

    @pytest.mark.regression
    def test_03_verify_app_privacy_ui_and_its_contents_C58769287(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents missing"
        assert self.hpx_settings.verify_product_improvement_description_text(), "Product improvement description text missing"
        assert self.hpx_settings.verify_advertising_description_text(), "Advertising description text missing"
        logging.info("Product Improvement description text: {}".format(self.hpx_settings.get_product_improvement_description_text()))
        logging.info("Advertising description text: {}".format(self.hpx_settings.get_advertising_description_text()))

    @pytest.mark.regression
    def test_04_verify_app_and_pc_consents_C58769298(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents missing"
        assert self.hpx_settings.verify_device_privacy_text(), "Device privacy text missing"
        self.hpx_settings.click_device_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_consents(), "Device privacy consents missing"

    @pytest.mark.regression
    def test_05_verify_toggle_switches_in_privacy_tab_C58769306(self):
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        assert self.hpx_settings.verify_privacy_tab_visible(), "privacy tab invisible"
        assert self.hpx_settings.verify_privacy_statement_link(), "HP privacy statement link invisible"
        assert self.hpx_settings.verify_about_section_title(), "about section title invisible"
        assert self.hpx_settings.verify_terms_of_use(), "terms of use link invisible"
        assert self.hpx_settings.verify_about_user_license_agreement(), "about user license agreement invisible"

    @pytest.mark.regression
    def test_06_verify_data_transfer_toggle_under_app_privacy_C58769281(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents missing"
        assert self.hpx_settings.verify_product_improvement_description_text(), "Product improvement description text missing"
        assert self.hpx_settings.verify_advertising_description_text(), "Advertising description text missing"
        self.hpx_settings.verify_data_transfer_china_consent_toggle_is_clicked()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is False
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is False
