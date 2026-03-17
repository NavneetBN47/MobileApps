import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Advanced_Personal_Mode(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_01_apm_mode_will_show_on_spupport_device_C53412166(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=9)
        time.sleep(2)
        # verify apm mode title will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_title_show()) is True, "APM mode is not showing on supported device"
        time.sleep(2)
        # verify apm mode tips will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_tips_show()) is True, "APM mode tips is not showing on supported device"
        time.sleep(2)
        # verify apm mode toggle will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_toggle_show()) is True, "APM mode toggle is not showing on supported device"
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_02_verify_can_turn_on_off_apm_toggle_C58365049(self):
        if self.fc.fd["audio"].verify_apm_mode_title_show() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=9)
            time.sleep(2)
        # verify apm mode title will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_title_show()) is True, "APM mode is not showing on supported device"
        time.sleep(2)
        # verify apm mode toggle will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_toggle_show()) is True, "APM mode toggle is not showing on supported device"
        time.sleep(2)
        # judge apm mode toggle status
        if self.fc.fd["audio"].verify_apm_mode_toggle_status() == "1":
            self.fc.fd["audio"].click_apm_mode_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_apm_mode_toggle_status() == "0", "APM mode toggle is not off"
        time.sleep(2)
        self.fc.fd["audio"].click_apm_mode_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_apm_mode_toggle_status() == "1", "APM mode toggle is not on"
        time.sleep(2)
        
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_03_check_APM_ui_C53365925(self):
        if self.fc.fd["audio"].verify_apm_mode_title_show() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=9)
            time.sleep(2)
            # verify apm mode title will show
            assert bool(self.fc.fd["audio"].verify_apm_mode_title_show()) is True, "APM mode is not showing on supported device"
            time.sleep(2)
        # verify apm mode title will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_title_show()) is True, "APM mode is not showing on supported device"
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_apm_mode_tips_show()) is True, "APM mode tips is not showing on supported device"
        time.sleep(2)
        # verify apm mode toggle will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_toggle_show()) is True, "APM mode toggle is not showing on supported device"
        time.sleep(2)
        if self.fc.fd["audio"].verify_apm_mode_toggle_status() == "1":
            self.fc.fd["audio"].click_apm_mode_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_apm_mode_toggle_status() == "0", "APM mode toggle is not off"
        time.sleep(2)   
        

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_04_check_APM_tooltip_contents_C56287624(self):
        if self.fc.fd["audio"].verify_apm_mode_title_show() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=6)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=9)
            time.sleep(2)
            # verify apm mode title will show
            assert bool(self.fc.fd["audio"].verify_apm_mode_title_show()) is True, "APM mode is not showing on supported device"
            time.sleep(2)
        # verify apm mode tips will show
        assert bool(self.fc.fd["audio"].verify_apm_mode_tips_show()) is True, "APM mode tips is not showing on supported device"
        time.sleep(2)
        self.fc.fd["audio"].click_APM_tooltip_contents()
        time.sleep(2)
        assert self.fc.fd["audio"].get_APM_tooltip_contents() == "Capture only your voice, filtering other voices and background noises, for crystal-clear conversations as you move around your PC."