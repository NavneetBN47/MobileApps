import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Immersive(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_check_immersive_show_up_C42197733(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # navigate to immersive
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_immersive_title_show_up(), "Immersive title is not displayed"
    

    @pytest.mark.function
    @pytest.mark.consumer
    def test_02_check_immersive_remember_state_when_relaunch_hpx_C42197735(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        # navigate to immersive
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(3)
        if self.fc.fd["audio"].verify_immersive_toggle_on_state() == "1":
            self.fc.fd["audio"].click_immersive_audio_toggle()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(3)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_immersive_toggle_off_state() == "0", "Immersive toggle is not off"
        time.sleep(2)
        self.fc.fd["audio"].click_immersive_audio_toggle()

    
    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_immersive_audio_toggle_can_turn_on_off_successfully_C42197736(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        time.sleep(1)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(1)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(1)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(1)
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        time.sleep(1)
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        if self.fc.fd["audio"].verify_immersive_toggle_on_state() == "1":
            self.fc.fd["audio"].click_immersive_audio_toggle()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_immersive_toggle_off_state() == "0", "Immersive toggle is not off"
        time.sleep(2)
        self.fc.fd["audio"].click_immersive_audio_toggle()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_immersive_toggle_on_state() == "1", "Immersive toggle is not on"
        time.sleep(2)