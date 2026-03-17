import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_functional_audio_level")
class Test_Suite_Audio_Level(object):
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    @pytest.mark.integration
    def test_01_check_audio_level_ui_C42213869(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)  
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=14)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        # check Output ui
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        assert self.fc.fd["audio"].verify_output_source_title_show_up(), "Output source title is not displayed"
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        assert self.fc.fd["audio"].verify_output_combobox_open_button_show_up(), "Output combobox open button is not displayed"
        assert self.fc.fd["audio"].verify_output_volume_title_show_up(), "Output volume title is not displayed"
        assert self.fc.fd["audio"].verify_output_volume_0_show_up(), "Output volume 0 is not displayed"
        assert self.fc.fd["audio"].verify_output_volume_slider_show_up(), "Output volume slider is not displayed"
        assert self.fc.fd["audio"].verify_output_volume_100_show_up(), "Output volume 100 is not displayed"
        assert self.fc.fd["audio"].verify_mute_txt_for_output_show_up(), "Output mute text is not displayed"
        assert self.fc.fd["audio"].verify_mute_toggle_for_output_show_up(), "Output mute toggle is not displayed"
        time.sleep(2)
        # check mute toggle for output
        Op = self.fc.fd["audio"].get_mute_toggle_for_output_status()
        assert Op == "0", "Output mute toggle is not off"
        # check Input ui
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_title_show_up(), "Input title is not displayed"
        assert self.fc.fd["audio"].verify_input_source_title_show_up(), "Input source title is not displayed"
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        assert self.fc.fd["audio"].verify_input_combobox_open_button_show_up(), "Input combobox open button is not displayed"
        assert self.fc.fd["audio"].verify_input_volume_title_show_up(), "Input volume title is not displayed"
        assert self.fc.fd["audio"].verify_input_volume_0_show_up(), "Input volume 0 is not displayed"
        assert self.fc.fd["audio"].verify_input_volume_slider_show_up(), "Input volume slider is not displayed"
        assert self.fc.fd["audio"].verify_input_volume_100_show_up(), "Input volume 100 is not displayed"
        assert self.fc.fd["audio"].verify_mute_txt_for_input_show_up(), "Output mute text is not displayed"
        assert self.fc.fd["audio"].verify_mute_toggle_for_input_show_up(), "Output mute toggle is not displayed"
        time.sleep(2)
        # check mute toggle for input
        Ip = self.fc.fd["audio"].get_mute_toggle_for_input_status()
        assert Ip == "0", "Input mute toggle is not off"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_02_check_output_slider_value_C42197640(self):
        self.fc.swipe_window(direction="up", distance=14)
        time.sleep(2)
        if self.fc.fd["audio"].verify_output_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        # set new settings for output
        self.fc.fd["audio"].set_audio_output_slider_value_decrease(10)
        time.sleep(20)
        assert round(float(self.fc.fd["audio"].get_output_slider_value())) <= 40, "Output slider value can be set correctly"
        time.sleep(5)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_03_check_input_slider_value_C42197642(self):
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        if self.fc.fd["audio"].verify_input_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(4)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
        assert self.fc.fd["audio"].verify_input_title_show_up(), "Input title is not displayed"
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        # set new settings for input
        self.fc.fd["audio"].set_audio_input_slider_value_increase(10)
        time.sleep(20)
        assert round(float(self.fc.fd["audio"].get_input_slider_value())) >= 40, "Input slider value can be set correctly"
        time.sleep(5)

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_check_output_slider_value_get_reflected_on_windows_setting_C42197644(self):
        self.fc.swipe_window(direction="up", distance=14)
        time.sleep(2)
        if self.fc.fd["audio"].verify_output_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(4)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        # set new settings for output
        self.fc.fd["audio"].set_audio_output_slider_value_increase(10)
        time.sleep(20)
        # check new settings for windows
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize() is False:
            self.fc.open_system_settings_sound()
            time.sleep(3)
        self.fc.fd["audio"].click_on_system_settings_maximize_button()
        system_output_value = self.fc.fd["audio"].get_windows_system_sound_output_volume_tab()
        assert int(system_output_value) >= 40, "Output slider value can be synced correctly"
        self.fc.close_windows_settings_panel()
        time.sleep(3)
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_check_input_slider_value_get_reflected_on_windows_setting_C42197643(self):
        self.fc.close_windows_settings_panel()
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        # set new settings for input
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(4)
        # check new settings for windows
        self.fc.open_system_settings_sound()
        time.sleep(2)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        system_input_value = self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert int(system_input_value) > 95, "Input slider value can be synced correctly"
        time.sleep(3)
        self.fc.close_windows_settings_panel()