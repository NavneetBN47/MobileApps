import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Settings_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_verify_notification_settings_under_settings_side_panel_C58769249(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.hpx_settings.click_profile_settings_btn()
        assert self.hpx_settings.verify_settings_title(), "settings title is not visible"
        assert self.css.verify_notification_title_show_up(), "notification title missing"

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_verify_device_supply_status_under_notifications_settings_C58769252(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_side_panel()
        self.hpx_settings.click_profile_settings_btn()
        self.hpx_settings.verify_settings_title()
        assert self.css.verify_notification_title_show_up(), "notification title is invisible"
        assert self.hpx_settings.verify_device_supply_status_text(), "device supply status text invisible"

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_03_verify_description_of_device_supply_option_C58769255(self):
        self.profile.navigate_to_settings_from_home()
        self.hpx_settings.verify_settings_title()
        assert self.css.verify_notification_title_show_up(), "notification title is invisible"
        self.hpx_settings.verify_device_supply_status_text()
        self.hpx_settings.verify_device_supply_status_description_text()
        description = self.hpx_settings.get_device_supply_status_description_text()
        actual_description = "Never miss important messages or notifications from your device."
        assert description == actual_description, "Description under Device & Supply Status >> Notifications >> Settings, is mismatching"

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_04_verify_device_supply_status_toggle_functionality_C58769261(self):
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        self.profile.navigate_to_settings_from_home()
        self.hpx_settings.verify_settings_title()
        assert self.css.verify_notification_title_show_up(), "notification title is invisible"
        self.hpx_settings.verify_device_supply_status_text()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "1", "Device and supply toggle is not working as expected"
        self.hpx_settings.click_device_supply_status_toggle()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "0", "Device and supply toggle is not working as expected"
        for _ in range(9): # clicking the toggle repeatedly
            self.hpx_settings.click_device_supply_status_toggle()
            status = self.hpx_settings.return_toggle_status_device_supply()
            logging.info(f"Device and Supply Status Toggle State: '{status}'")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_05_verify_device_supply_status_toggle_C58769267(self):
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
        toggle_status = self.hpx_settings.get_system_settings_notifications_toggle_state()
        assert toggle_status == "0", "Notifications toggle should be OFF"
        self.fc.close_windows_settings_panel()
        self.fc.launch_myHP_command()
        self.profile.navigate_to_settings_from_home()
        status = self.hpx_settings.return_toggle_status_device_supply()
        assert status == "0", "Device and supply toggle should be OFF"
        self.hpx_settings.click_device_supply_status_toggle()
        self.fc.open_system_settings_notifications()
        toggle_status = self.hpx_settings.get_system_settings_notifications_toggle_state()
        assert toggle_status == "1", "Notifications toggle should be ON"
        self.fc.close_windows_settings_panel()