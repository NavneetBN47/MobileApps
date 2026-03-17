import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from SAF.misc import saf_misc
import pytest
from SAF.misc.ssh_utils import SSH


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Speaker_Swap(object):
        
    
    @pytest.mark.function
    @pytest.mark.consumer
    def test_01_check_speaker_swap_ui_C42214019(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        if self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(40)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=17)
        time.sleep(3)
        # check advanced audio settings card
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        assert self.fc.fd["audio"].verify_advanced_audio_settings_arrow_show_up(), "Advanced audio settings arrow is not displayed"
        # navigate to speaker swap
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=4)
        time.sleep(3)
        # check speaker swap
        assert self.fc.fd["audio"].verify_speaker_swap_title_show_up(), "Speaker swap title is not displayed"
        assert self.fc.fd["audio"].verify_speaker_swap_toggle_show_up(), "Speaker swap toggle is not displayed"
        assert self.fc.fd["audio"].get_speaker_swap_toggle_status() == "1", "Speaker swap toggle is not enabled"
    
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_02_relaunch_myhp_speaker_swap_can_be_remembered_C42197705(self):
        if self.fc.fd["audio"].verify_speaker_swap_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            # check advanced audio settings card
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=17)
            time.sleep(3)
            assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
            assert self.fc.fd["audio"].verify_advanced_audio_settings_arrow_show_up(), "Advanced audio settings arrow is not displayed"
            self.fc.fd["audio"].click_advanced_audio_settings_arrow()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_swap_title_show_up(), "Speaker swap title is not displayed"
        assert self.fc.fd["audio"].verify_speaker_swap_toggle_show_up(), "Speaker swap toggle is not displayed"
        # check speaker swap toggle
        assert self.fc.fd["audio"].get_speaker_swap_toggle_status() == "1", "Speaker swap toggle is not enabled"
        # turn off speaker swap
        self.fc.fd["audio"].click_speaker_swap_toggle()
        # check speaker swap toggle
        assert self.fc.fd["audio"].get_speaker_swap_toggle_status() == "0", "Speaker swap toggle is not disabled"
        # relaunch myHP
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=17)
        time.sleep(3)
        # check advanced audio settings card
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        # navigate to speaker swap
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        # check speaker swap toggle
        assert self.fc.fd["audio"].get_speaker_swap_toggle_status() == "0", "Speaker swap toggle is not disabled"       

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_03_restore_default_work_with_speak_swap_C42197792(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=17)
        time.sleep(3)
        # navigate to speaker swap
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(2)
        if self.fc.fd["audio"].get_speaker_swap_toggle_status() == "1":
            self.fc.fd["audio"].click_speaker_swap_toggle()
            time.sleep(3)
        self.fc.fd["audio"].click_advanced_settings_restore_defaults_button()
        time.sleep(3)
        assert self.fc.fd["audio"].get_speaker_swap_toggle_status() == "1"