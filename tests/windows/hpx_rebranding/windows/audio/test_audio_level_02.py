import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_functional_audio_level")
class Test_Suite_Audio_Level_02(object):

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_connect_usb_headphone_and_check_output_slider_value_get_reflected_on_windows_setting_C42197645(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # select usb headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_usb_external_device()
        time.sleep(3)
        # restore mute status by clicking restore default button
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(3)
        # set new output value for usb headphone
        self.fc.fd["audio"].set_audio_output_slider_value_increase(10)
        time.sleep(30)
        hp_output_value = self.fc.fd["audio"].get_output_slider_value()
        # verify output value for usb headphone on windows setting
        self.fc.open_system_settings_sound()
        time.sleep(2)
        if self.fc.fd["audio"].verify_sound_title_on_windows_show_up() is False:
            self.fc.fd["audio"].click_settings_on_taskbar()
            time.sleep(4)
            assert self.fc.fd["audio"].verify_sound_title_on_windows_show_up() is True, "Sound title is not displayed on Windows settings"
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
            time.sleep(2)
        self.fc.open_system_settings_sound()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_sound_title_on_windows_show_up(), "Sound title is not displayed on Windows settings"
        system_output_value = self.fc.fd["audio"].get_windows_system_sound_output_volume_tab()
        assert system_output_value == hp_output_value, "USB headphone output value is not reflected on windows setting"
        self.fc.close_windows_settings_panel()
        time.sleep(3)
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_connect_35_headphone_and_check_output_slider_value_get_reflected_on_windows_setting_C42197646(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # select 35mm headphone
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].select_output_35mm_external_device()
        time.sleep(4)
        # restore mute status by clicking restore default button
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=11)
        time.sleep(4)
        # set new output value for 35mm headphone
        self.fc.fd["audio"].set_audio_output_slider_value_decrease(100)
        time.sleep(40)
        hp_output_value = self.fc.fd["audio"].get_output_slider_value()
        time.sleep(10)
        # verify output value for 35mm headphone on windows setting
        self.fc.open_system_settings_sound()
        time.sleep(4)
        if self.fc.fd["audio"].verify_sound_title_on_windows_show_up() is False:
            self.fc.fd["audio"].click_settings_on_taskbar()
            time.sleep(4)
            assert self.fc.fd["audio"].verify_sound_title_on_windows_show_up(), "Sound title is not displayed on Windows settings"
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
            time.sleep(2)
        system_output_value = self.fc.fd["audio"].get_windows_system_sound_output_volume_tab()
        assert system_output_value == hp_output_value, "35mm headphone output value is not reflected on windows setting"
        self.fc.close_windows_settings_panel()
        time.sleep(3)
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_connect_usb_headphone_and_check_input_slider_value_get_reflected_on_windows_setting_C42197649(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # select usb headphone
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        if self.fc.fd["audio"].verify_input_usb_external_device_show_up() is False:
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].select_input_usb_external_device()
            time.sleep(3)
        # restore mute status by clicking restore default button
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=7)
        time.sleep(4)
        # set new input value for usb headphone
        self.fc.fd["audio"].set_audio_input_slider_value_decrease(100)
        time.sleep(20)
        assert int(self.fc.fd["audio"].get_input_slider_value()) < 50, "Input slider value is not set to 0"
        time.sleep(3)
        # verify input value for usb headphone on windows setting
        self.fc.open_system_settings_sound()
        time.sleep(3)
        self.fc.close_myHP()
        time.sleep(3)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        else:
            self.fc.close_windows_settings_panel()
            time.sleep(3)
            self.fc.open_system_settings_sound()
            time.sleep(3)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
        self.fc.swipe_window(direction="down", distance=2)
        system_input_value = self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert int(system_input_value) <= 50, "USB headphone input value is not reflected on windows setting"
        self.fc.close_windows_settings_panel()
        time.sleep(3)
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_connect_35mm_headphone_and_check_input_slider_value_get_reflected_on_windows_setting_C42197650(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        # select 35mm headphone
        if self.fc.fd["audio"].verify_input_35mm_external_device_show() is False:
            self.fc.fd["audio"].verify_input_combobox_show_up()
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(3)
            self.fc.fd["audio"].select_input_35mm_external_device()
            time.sleep(3)
        if self.fc.fd["audio"].get_mute_toggle_for_input_status() == "1":
            self.fc.fd["audio"].click_mute_toggle_for_input()
            time.sleep(3)
        # set new input value for 35mm headphone
        self.fc.fd["audio"].set_audio_input_slider_value_decrease(100)
        time.sleep(10)
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(10)
        self.fc.fd["audio"].get_input_slider_value()
        time.sleep(3)
        # verify input value for 35mm headphone on windows setting
        self.fc.open_system_settings_sound()
        time.sleep(4)
        self.fc.close_myHP()
        time.sleep(3)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(3)
        system_input_value = self.fc.fd["audio"].get_windows_system_sound_input_volume_tab()
        assert int(system_input_value) > 95, "35mm headphone input value is not reflected on windows setting"
        self.fc.close_windows_settings_panel()
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_connect_35mm_headphone_and_check_input_device_mute_status_C42197656(self):
        if self.fc.fd["audio"].verify_close_button_on_windows_settings_show_up() is True:
            self.fc.close_windows_settings_panel()
            time.sleep(3)
        if self.fc.fd["audio"].verify_input_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(3)
        # select 35mm headphone
        if self.fc.fd["audio"].verify_input_35mm_external_device_show() is False:
            self.fc.fd["audio"].verify_input_combobox_show_up()
            self.fc.fd["audio"].click_input_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].select_input_35mm_external_device()
            time.sleep(3)  
        # restore mute status by clicking restore default button
        self.fc.swipe_window(direction="down", distance=9)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(3)
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0", "Mute toggle is not enabled"
        time.sleep(3)
        # select internal microphone
        assert self.fc.fd["audio"].verify_input_combobox_show_up(), "Input combobox is not displayed"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_internal_device()
        time.sleep(3)
        # restore mute status by clicking restore default button
        self.fc.swipe_window(direction="down", distance=9)
        time.sleep(3)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(3)
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0"
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
    

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_check_internal_and_external_device_C42197667(self):
        if self.fc.fd["audio"].verify_output_combobox_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check internal and external device
        self.fc.fd["audio"].verify_output_combobox_show_up()
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].verify_output_35mm_external_device_show(), "35mm external device is not displayed on Output"
        self.fc.fd["audio"].verify_output_internal_device_show(), "Internal device is not displayed on Output"
        self.fc.fd["audio"].verify_output_usb_headphone_show(), "Usb external device is not displayed on Output"
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["audio"].verify_input_combobox_show_up()
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(4)
        self.fc.fd["audio"].verify_input_internal_device_show(), "Internal device is not displayed on Input"
        self.fc.fd["audio"].verify_input_35mm_external_device_show(), "35mm external device is not displayed on Input"
        self.fc.fd["audio"].verify_input_usb_external_device_show_up(), "Usb external device is not displayed on Input"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_different_device_and_remember_volume_status_C42197664(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        # select USB headphone for Output
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_usb_external_device()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        self.fc.fd["audio"].set_audio_output_slider_value_decrease(100)
        time.sleep(20)
        # select 3.5mm headphone for Output
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_35mm_external_device()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        # set new output value for 35mm headphone for Output
        self.fc.fd["audio"].set_audio_output_slider_value_increase(100)
        time.sleep(20)
        # verify output value for 35mm headphone for Output
        assert int(self.fc.fd["audio"].get_output_slider_value()) >= 20, "35mm headphone output value is not set correctly"
        # select usb headphone again for Output to verify the output value
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox doesn't show up"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_usb_external_device()
        time.sleep(5)
        assert int(self.fc.fd["audio"].get_output_slider_value()) <= 20, "USB headphone output value is not set correctly"
        # select 3.5mm headphone for input
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox doesn't show up"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_35mm_external_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        # set new input value for 35mm headphone for Input
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(20)
        # select usb headphone for Input
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_usb_external_device()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        # set new input value for usb headphone for Input
        self.fc.fd["audio"].set_audio_input_slider_value_increase(100)
        time.sleep(20)
        # select 3.5mm headphone for Input again
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_35mm_external_device()
        time.sleep(5)
        assert int(self.fc.fd["audio"].get_input_slider_value()) >= 20, "35mm headphone input value is not set correctly"
        # select usb headphone for input again
        assert self.fc.fd["audio"].verify_input_combobox_show_up() is True, "Input combobox doesn't show up"
        self.fc.fd["audio"].click_input_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_input_usb_external_device()
        time.sleep(5)
        assert int(self.fc.fd["audio"].get_input_slider_value()) >= 20, "USB headphone input value is not set correctly"