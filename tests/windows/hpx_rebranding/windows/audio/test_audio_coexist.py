import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
from SAF.misc.ssh_utils import SSH


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Coexist(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    @pytest.mark.integration
    def test_01_audio_control_will_show_up_with_standalone_app_existed_C42197728(self):
        # check audio control shows up originally
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.close_myHP()
        time.sleep(4)
        # install audio standalone app
        self.fc.install_audio_standalone_app()
        time.sleep(5)
        # relaunch myhp app to check audio control
        self.fc.launch_myHP()
        time.sleep(4)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        self.fc.uninstall_audio_standalone_app()
        time.sleep(5)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_02_check_audio_standalone_app_ui_C42197729(self):
        # install and launch audio standalone app
        self.fc.install_audio_standalone_app()
        time.sleep(5)
        self.fc.fd["audio"].launch_windows_app("HP Audio")
        time.sleep(15)
        assert self.fc.fd["audio"].verify_open_myhp_button_show_up(), "open myhp button doesn't show up"
        assert self.fc.fd["audio"].verify_not_now_button_show_up(), "not now button doesn't show up"
        assert self.fc.fd["audio"].verify_close_audio_standalone_app_button_show_up(), "close audio standalone app button doesn't show up"
        self.fc.fd["audio"].click_close_audio_standalone_app_button()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_not_now_button_show_up() is False, "audio standalone app doesn't close"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_03_it_will_navigate_to_home_page_when_click_open_my_hp_button_C42197730(self):
        self.fc.close_myHP()
        time.sleep(4)
        # install and launch audio standalone app
        self.fc.fd["audio"].launch_windows_app("HP Audio")
        time.sleep(15)
        if self.fc.fd["audio"].verify_open_myhp_button_show_up() == False:
            self.fc.install_audio_standalone_app()
            time.sleep(5)
            self.fc.fd["audio"].launch_windows_app("HP Audio")
            time.sleep(15)
        assert self.fc.fd["audio"].verify_open_myhp_button_show_up(), "open myhp button doesn't show up"
        assert self.fc.fd["audio"].verify_not_now_button_show_up(), "not now button doesn't show up"
        assert self.fc.fd["audio"].verify_close_audio_standalone_app_button_show_up(), "close audio standalone app button doesn't show up"
        self.fc.fd["audio"].click_open_myhp_button()
        time.sleep(8)
        # relaunch myhp app to check audio control
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "device card doesn't show up"