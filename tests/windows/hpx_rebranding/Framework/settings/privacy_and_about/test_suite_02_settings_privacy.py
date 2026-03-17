import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_02_Settings_Privacy(object):
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
    def test_01_verify_managed_device_functionality_C67872439(self):
        self.fc.change_system_region_to_united_states()
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()

    @pytest.mark.regression
    def test_02_verify_consents_on_settings_C67872440(self):
        self.fc.change_system_region_to_united_states()
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_manage_privacy_btn()
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked() is True
        assert self.hpx_settings.verify_advertising_toggle_is_clicked() is True
