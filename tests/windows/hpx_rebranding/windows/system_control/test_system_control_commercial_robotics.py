import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_charger")
class Test_Suite_System_Control(object):
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_bi_directional_sync_with_win_os_for_system_control_smart_sense_v2_hpx_application_to_windows_settings_C52986226(self):
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(2)
        if self.fc.fd["system_control"].get_smart_sense_radio_button_commercial_is_selected() == "false":
            self.fc.fd["system_control"].click_smart_sense_radio_button_commercail()
        time.sleep(2)
        assert self.fc.fd["system_control"].get_smart_sense_radio_button_commercial_is_selected() == "true", "Smart sense mode is not selcted"
        self.driver.ssh.send_command("start ms-settings:batterysaver")
        self.fc.fd["system_control"].click_windows_power_mode_dropdown()
        assert self.fc.fd["system_control"].get_plugged_in_selected_value() == "Balanced", "Balanced mode is not selected"
        self.fc.close_windows_settings_panel()
        assert self.fc.fd["system_control"].get_smart_sense_radio_button_commercial_is_selected() == "true", "Smart sense mode is disabled"
        self.fc.fd["system_control"].click_performance_toggle()
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        self.driver.ssh.send_command("start ms-settings:batterysaver")
        self.fc.fd["system_control"].click_windows_power_mode_dropdown()
        assert self.fc.fd["system_control"].get_plugged_in_selected_value() == "Best Performance", "Best Performance mode is not selected"
        self.fc.close_windows_settings_panel()
        self.vcosmos.remove_charger_and_usb()
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        self.fc.fd["system_control"].click_smart_sense_radio_button_commercail()
        assert self.fc.fd["system_control"].get_smart_sense_radio_button_commercial_is_selected() == "true", "Smart sense mode is not selcted"
        self.driver.ssh.send_command("start ms-settings:batterysaver")
        self.fc.fd["system_control"].click_windows_power_mode_dropdown()
        assert self.fc.fd["system_control"].get_plugged_in_selected_value() == "Balanced", "Balanced mode is not selected"
        self.fc.close_windows_settings_panel()
        assert self.fc.fd["system_control"].get_smart_sense_radio_button_commercial_is_selected() == "true", "Smart sense mode is disabled"
        self.fc.fd["system_control"].click_performance_toggle()
        assert self.fc.fd["system_control"].get_system_performance_radiobutton_is_selected() == "true", "Performance mode is not selected"
        self.driver.ssh.send_command("start ms-settings:batterysaver")
        self.fc.fd["system_control"].click_windows_power_mode_dropdown()
        assert self.fc.fd["system_control"].get_plugged_in_selected_value() == "Best Performance", "Best Performance mode is not selected"
        self.fc.close_windows_settings_panel()
        self.vcosmos.add_charger_and_usb()
        self.fc.fd["system_control"].click_smart_sense_radio_button_commercail()
        self.vcosmos.clean_up_logs()
        self.fc.close_myHP()