import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Common(object):
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_01_check_audio_on_pc_device_page_C42197594(self):
        time.sleep(3)
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device card shows up"
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_back_pc_device_page_by_click_back_arrow_on_audio_page_C52017570(self):
        if self.fc.fd["audio"].verify_back_button_on_audio_page is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(4)
        assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "back arrow shows on audio control page"
        self.fc.fd["audio"].click_back_button_on_audio_page()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up(), "back arrow shows on devices page"
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(4)
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device card shows up"


    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_back_audio_page_by_click_back_arrow_on_advanced_audio_settings_page_C52017571(self):
        if self.fc.fd["devicesMFE"].verify_device_card_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        assert self.fc.fd["audio"].verify_advanced_audio_settings_arrow_show_up(), "Advanced audio settings arrow is not displayed"
        self.fc.fd["audio"].click_advanced_audio_settings_arrow()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "back arrow shows on audio control page"
        assert self.fc.fd["audio"].verify_advanced_audio_settings_title_show_up(), "Advanced audio settings title is not displayed"
        self.fc.fd["audio"].click_back_button_on_audio_page()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        self.fc.close_myHP()

  
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ARM
    @pytest.mark.commercial
    def test_04_check_DTS_sound_unbound_link_will_show_on_myhp_after_installing_on_non_dts_machine_C60502047(self):
        self.fc.install_DTS_sound_unbind_apps_from_ms_store("DTS Sound Unbound", "dts_sound_unbound_on_ms_store")
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check DTS sound unbound link
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_dts_unbound_link_show_up(), "DTS sound unbound link is not displayed"
        self.fc.uninstall_dts_sound_unbound_app()