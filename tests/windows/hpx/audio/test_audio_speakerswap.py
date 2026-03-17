from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Audio_SpeakerSwap(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    # whole suite only can be ran on gidget
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_01_check_speaker_swap_ui_C32333017(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_speak_swap_show()) is True, "Speaker swap is not show"
        assert self.fc.fd["audio"].verify_speak_swap_btn_status_on() == "1", "Speaker swap button is not on"
        time.sleep(2)
        self.fc.fd["audio"].close_audio_settings()
        time.sleep(2)

    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_turn_on_off_speak_swap_C33141929(self):
        self.fc.restart_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)

        assert bool(self.fc.fd["audio"].verify_speak_swap_show()) is True, "Speaker swap is not show"
        if self.fc.fd["audio"].verify_speak_swap_btn_status_on() == "1":
            self.fc.fd["audio"].click_speak_swap_btn_on()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_off() == "0", "Speaker swap button is not off"
            self.fc.fd["audio"].click_speak_swap_btn_off()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_on() == "1", "Speaker swap button is not on"
        else:
            self.fc.fd["audio"].verify_speak_swap_btn_status_on()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_on() == "1", "Speaker swap button is not on"
            time.sleep(2)
            self.fc.fd["audio"].verify_speak_swap_btn_status_off()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_off() == "0", "Speaker swap button is not off"
            time.sleep(2)
        self.fc.fd["audio"].close_audio_settings()
        time.sleep(2)

    def test_03_speaker_swap_button_will_be_remembered_even_we_relaunch_myhp_C32841926(self):
        self.fc.restart_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_speak_swap_show()) is True, "Speaker swap is not show"
        if bool(self.fc.fd["audio"].is_speak_swap_button_on_visible()) == True:
            self.fc.fd["audio"].click_speak_swap_btn_on()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_off() == "0", "Speaker swap button is not off"
        else:
            self.fc.fd["audio"].click_speak_swap_btn_off()
            time.sleep(2)
            self.fc.fd["audio"].click_speak_swap_btn_on()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_off() == "0", "Speaker swap button is not off"
        time.sleep(3)
        self.fc.close_myHP()
        time.sleep(5)
        self.fc.launch_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speak_swap_btn_status_off() == "0", "Speaker swap button is not off"
        time.sleep(2)
        self.fc.fd["audio"].close_audio_settings()

    
    @pytest.mark.consumer
    @pytest.mark.function
    def test_04_restore_defaults_button_will_work_well_with_Speaker_swap_C37543567(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.fd["audio"].click_audio_settings_btn()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_speak_swap_show()) is True, "Speaker swap is not show"
        if self.fc.fd["audio"].verify_speak_swap_btn_on_show():
            self.fc.fd["audio"].click_speak_swap_btn_on()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_speak_swap_btn_status_off() == "0", "Speaker swap button is not off"
        self.fc.fd["audio"].close_audio_settings()
        self.fc.swipe_window(direction="down", distance=8)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.swipe_window(direction="up", distance=8)
        self.fc.fd["audio"].click_audio_settings_btn()
        
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_speak_swap_show()) is True, "Speaker swap is not show"
        assert self.fc.fd["audio"].verify_speak_swap_btn_status_on() == "1", "Speaker swap button is not on"
