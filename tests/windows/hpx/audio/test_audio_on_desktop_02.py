from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Desktop(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    
    def round_up(self,input_value):
        return round(float(input_value))

    #tc 7 to 10 can only run in thompson due to speaker and external devices names AUId are different from anyother devices.
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_input_device_mute_unmute_status_C40795418(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)

        # Mute 3.5mm headphone firstly
        assert bool(self.fc.fd["audio"].verify_3_5mm_headphone_input_device()) is True, "3.5mm headphone is not visible"
        self.fc.fd["audio"].select_headphone_input_device()
        time.sleep(2)
        input_mic_status = self.fc.fd["audio"].get_mute_unmute_status_on_input_mic()
        if "Off" in input_mic_status:
            self.fc.fd["audio"].click_mute_unmute_input_mic_button()
            time.sleep(5)
            mic_status = self.fc.fd["audio"].get_mute_unmute_status_on_input_mic()
            assert "On" in mic_status,"Mic is not mute"

        # Mute internal speaker secondly
        self.fc.fd["audio"].click_input_mic_icon_input_device()
        time.sleep(5)

        input_mic_status = self.fc.fd["audio"].get_mute_unmute_status_on_input_mic()
        if "Off" in input_mic_status:
            self.fc.fd["audio"].click_mute_unmute_input_mic_button()
            time.sleep(5)
            mic_status = self.fc.fd["audio"].get_mute_unmute_status_on_input_mic()
            assert "On" in mic_status,"Mic is not mute"

        self.fc.fd["audio"].select_headphone_input_device()
        time.sleep(5)
        self.fc.fd["audio"].click_mute_unmute_input_mic_button()
        time.sleep(5)
        mic_status = self.fc.fd["audio"].get_mute_unmute_status_on_input_mic()
        assert "Off" in mic_status,"Mic is mute for external headphone"

        self.fc.fd["audio"].click_input_mic_icon_input_device()
        time.sleep(5)
        self.fc.fd["audio"].click_mute_unmute_input_mic_button()
        time.sleep(5)
        mic_status = self.fc.fd["audio"].get_mute_unmute_status_on_input_mic()
        assert "Off" in mic_status,"Mic is mute for internal mic"

        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(5)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(5)
        self.driver.swipe(direction="up", distance=3)

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_check_audio_settings_will_be_remembered_by_different_devices_C31675700(self):
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["devices"].maximize_app()
        time.sleep(2)

        # set internal speaker to 100
        self.fc.fd["audio"].click_speaker_on_device()
        time.sleep(2)

        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        time.sleep(5)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert self.round_up(output_value)== 100,"Volume is not 100"

        # set internal mic to 100
        if self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() != "1":
            self.fc.fd["audio"].click_internal_speaker_on_thompson()
            time.sleep(2)

        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"input_slider")
        time.sleep(5)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "100"==input_value,"Volume is not 100"

        # set headset speaker to 0
        self.fc.fd["audio"].click_headphone_plugin_pc()
        time.sleep(2)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        if self.round_up(output_value) != 0:
            self.fc.fd["audio"].set_slider_value_decrease(self.round_up(output_value),"output_slider")
            output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert "0"==output_value,"Volume is not 0"

        # set headset mic to 0
        self.fc.fd["audio"].click_headset_output_for_mm()
        time.sleep(5)
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        if self.round_up(input_value) != 0:
            self.fc.fd["audio"].set_slider_value_decrease(self.round_up(input_value),"input_slider")
            input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "0"==input_value,"Volume is not 0"

        # check internal speaker and mic remembered settings(100)
        self.fc.fd["audio"].click_speaker_on_device() 
        time.sleep(5)
        self.fc.fd["audio"].click_internal_speaker_on_thompson()
        time.sleep(5)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert "100"==output_value,"Volume is not 100"
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "100"==input_value,"Volume is not 100"

        # check external speaker and mic remembered settings(0)
        self.fc.fd["audio"].click_headphone_plugin_pc()
        time.sleep(5)
        self.fc.fd["audio"].click_headset_output_for_mm()
        time.sleep(5)
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert "0"==output_value,"Volume is not 0"
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "0"==input_value,"Volume is not 0"
        
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_check_internal_device_will_show_up_at_least_C40795816(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        self.fc.fd["audio"].verify_home_audio_show()
        assert bool(self.fc.fd["audio"].verify_speaker_on_device()) is True, "Internal speaker is not visible"
        assert bool(self.fc.fd["audio"].verify_internal_mic_input_device()) is True, "Internal mic is not visible"
        