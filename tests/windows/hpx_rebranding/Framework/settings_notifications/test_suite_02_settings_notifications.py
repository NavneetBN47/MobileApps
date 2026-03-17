import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_02_Settings_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.css = request.cls.fc.fd["css"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_verify_device_supply_status_and_windows_settings_C67872432(self):
        # Launch myHP app and navigate to Settings > Notifications this test case is failing HPXAPPS-38035
        self.profile.navigate_to_settings_from_home()
        self.hpx_settings.verify_settings_title()
        assert self.css.verify_notification_title_show_up(), "notification title is invisible"
        self.hpx_settings.verify_device_supply_status_text()
        self.hpx_settings.verify_device_supply_status_description_text()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "1", "Device and supply toggle should be turned ON as default"
        self.fc.close_myHP()
        self.fc.open_system_settings_notifications()
        toggle_status = self.hpx_settings.get_system_settings_notifications_toggle_state()
        if toggle_status == "1":
            self.hpx_settings.click_system_notifications_toggle()
        assert toggle_status == "0", "Notifications toggle should be OFF"
        self.fc.close_windows_settings_panel()
        self.fc.launch_myHP_command()
        self.profile.navigate_to_settings_from_home()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "1", "Device and supply toggle should be ON"

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_consistency_of_device_and_supply_status_toggle_state_C67872433(self):
        self.profile.navigate_to_settings_from_home()
        status = self.hpx_settings.return_toggle_status_device_supply()
        if status == "1":
            self.hpx_settings.click_device_supply_status_toggle()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "0", "Device and supply toggle should be OFF"
        self.hpx_settings.go_home_from_settings_and_support()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.profile.navigate_to_settings_from_home()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "0", "Device and supply toggle should be OFF"
        self.fc.close_myHP()
        self.fc.launch_myHP_command()
        self.profile.navigate_to_settings_from_home()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "0", "Device and supply toggle should be OFF"