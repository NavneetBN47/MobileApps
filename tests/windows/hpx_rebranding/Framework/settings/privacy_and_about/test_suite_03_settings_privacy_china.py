import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_03_Setting_Privacy_China(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.regression
    def test_01_verify_pipl_device_and_app_consents_C67872437(self):
        self.fc.change_system_region_to_china()
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.css.maximize_hp()
        if self.app_consents.verify_manage_choices_btn():
            self.app_consents.click_manage_choices_btn()
        assert self.app_consents.verify_data_transfer_consent_for_china()
        self.app_consents.click_data_transfer_consent_for_china()
        self.app_consents.click_manage_privacy_continue_btn()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_data_transfer_china_consent_toggle_is_clicked()

    @pytest.mark.regression
    def test_02_verify_pipl_data_transfer_toggle_func_C67872438(self):
        self.fc.change_system_region_to_china()
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.css.maximize_hp()
        if self.app_consents.verify_manage_choices_btn():
            self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_data_transfer_consent_for_china()
        self.app_consents.click_data_transfer_consent_for_china()
        self.app_consents.click_manage_privacy_continue_btn()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_profile_settings_btn(), "Settings btn on profile sidepanel missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button not found"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_data_transfer_china_consent_toggle_is_clicked()
        assert self.hpx_settings.verify_product_improvement_china_toggle_is_avaibale() is True, "Product Improvement toggle is not enabled"
        assert self.hpx_settings.verify_advertising_china_is_avaibale() is True, "Advertising toggle is not enabled"
