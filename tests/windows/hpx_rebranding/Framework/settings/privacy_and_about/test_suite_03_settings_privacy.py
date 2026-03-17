import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_03_Settings_Privacy(object):
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
    def test_01_verify_manage_privacy_settings_page_58769277(self):
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_manage_privacy_title(), "Manage privacy title not found"
        self.hpx_settings.verify_application_privacy_text()
        self.app_consents.verify_manage_privacy_description_text()
        self.hpx_settings.verify_application_privacy_consents()
        self.hpx_settings.verify_device_privacy_text()

    @pytest.mark.regression
    def test_02_verify_manage_privacy_settings_page_59486532(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_manage_privacy_title(), "Manage privacy title not found"
        assert self.hpx_settings.verify_privacy_statement_link(), "Privacy statement link invisble"
        self.hpx_settings.click_privacy_statement_link()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_03_managed_app_functionality_60498991(self):
        self.fc.app_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_manage_privacy_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_system_admin_warning_msg()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is False
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is False

    @pytest.mark.regression
    def test_04_managed_app_functionality_60498988(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_manage_privacy_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents()
        assert self.hpx_settings.verify_device_privacy_text()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is True
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is True

    @pytest.mark.regression
    def test_05_verify_delete_your_account_hidden_in_signout_57437649(self):
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_manage_privacy_btn()
        assert self.hpx_settings.verify_delete_your_account_text() == False, "delete your account link found"