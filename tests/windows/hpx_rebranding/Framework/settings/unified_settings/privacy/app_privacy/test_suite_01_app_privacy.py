import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_01_App_Privacy(object):
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
    def test_01_app_consents_toggles_persists_after_navigate_to_other_page_C59522348(self):
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        self.app_consents.click_product_improvement_btn()
        self.app_consents.click_advertising_btn()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is False
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is False
        self.hpx_settings.click_manage_privacy_settings_back_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is False
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is False

    @pytest.mark.regression
    def test_02_verify_app_privacy_consents_contents_C67516498(self):
        self.fc.change_system_region_to_united_states()
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.app_consents.verify_product_improvement_btn()
        assert self.app_consents.verify_adverstising_btn()
        assert self.hpx_settings.verify_application_privacy_text(), "Application privacy text missing"
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents missing"
        assert self.hpx_settings.verify_product_improvement_description_text(), "Product improvement description text missing"
        assert self.hpx_settings.verify_advertising_description_text(), "Advertising description text missing"

    @pytest.mark.regression
    def test_03_verify_consents_are_set_on_after_click_acceptall_C67516499(self):
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.css.maximize_hp()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is True
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is True

    @pytest.mark.regression
    def test_04_verify_consents_are_set_on_after_click_decline_data_C67516500(self):
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.css.maximize_hp()
        self.app_consents.click_decline_optional_data_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is False
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is False

    @pytest.mark.regression
    def test_05_verify_app_privacy_consents_contents_C67516501(self):
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.app_consents.verify_adverstising_btn(), "Advertising button is not visible"
        assert self.app_consents.verify_advertising_here_link(), "Advertising here link not visible"
        self.app_consents.click_advertising_here_link()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Advertising link Browser tab name is: {tab_name}")
        self.fc.kill_chrome_process()