import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Auido_Equalizer(object):
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
        yield "select internal speaker"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        cls.fc.fd["audio"].click_internal_speaker_output_device_grogu()
        time.sleep(3)

    #suite on ramses, contino
    #this test case has been created because different platforms has different expected results
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_restore_defaults_button_will_work_well_with_equalizer_C41858117(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_on_device()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(75,"equalizer_slider_32volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_64volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(60,"equalizer_slider_8kvolume")
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(5)
        restored_32volume = self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume")
        assert restored_32volume == "0", "Equalizer slider 32 value is not 0"
        time.sleep(5)
        restored_64volume = self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume")
        assert restored_64volume == "0", "Equalizer slider 64 value is not 0"
        time.sleep(5)
        restored_8kvolume = self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume")
        assert restored_8kvolume == "0", "Equalizer slider 8k value is not 0"

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_change_output_device_verify_change_should_be_saved_C32154141(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["audio"].click_speaker_on_device()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_equalizer_text_show() is True,"Equlizer text is not visible"
        assert self.fc.fd["audio"].verify_equalizer_tooltip_icon_show() is True,"Equalizer tooltip is not visible"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume") == "0", "Equalizer slider 32 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume") == "0", "Equalizer slider 64 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_125volume") == "0", "Equalizer slider 125 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_250volume") == "0", "Equalizer slider 250 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume") == "0", "Equalizer slider 500 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_1kvolume") == "0", "Equalizer slider 1k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_2kvolume") == "0", "Equalizer slider 2k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_4kvolume") == "0", "Equalizer slider 4k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume") == "0", "Equalizer slider 8k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_16kvolume") == "0", "Equalizer slider 16k value is not 0"
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_32volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_64volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_125volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_250volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_500volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_1kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_2kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_4kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_8kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_16kvolume")
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume") == "12", "Equalizer slider 32 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume") == "12", "Equalizer slider 64 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_125volume") == "12", "Equalizer slider 125 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_250volume") == "12", "Equalizer slider 250 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume") == "12", "Equalizer slider 500 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_1kvolume") == "12", "Equalizer slider 1k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_2kvolume") == "12", "Equalizer slider 2k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_4kvolume") == "12", "Equalizer slider 4k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume") == "12", "Equalizer slider 8k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_16kvolume") == "12", "Equalizer slider 16k value is not 12"
        self.fc.fd["audio"].click_headphone_plugin_pc()
        time.sleep(5)
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume") == "0", "Equalizer slider 32 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume") == "0", "Equalizer slider 64 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_125volume") == "0", "Equalizer slider 125 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_250volume") == "0", "Equalizer slider 250 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume") == "0", "Equalizer slider 500 value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_1kvolume") == "0", "Equalizer slider 1k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_2kvolume") == "0", "Equalizer slider 2k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_4kvolume") == "0", "Equalizer slider 4k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume") == "0", "Equalizer slider 8k value is not 0"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_16kvolume") == "0", "Equalizer slider 16k value is not 0"
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_32volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_64volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_125volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_250volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_500volume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_1kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_2kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_4kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_8kvolume")
        self.fc.fd["audio"].set_equalizer_slider_value_increase(30,"equalizer_slider_16kvolume")
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume") == "12", "Equalizer slider 32 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume") == "12", "Equalizer slider 64 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_125volume") == "12", "Equalizer slider 125 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_250volume") == "12", "Equalizer slider 250 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume") == "12", "Equalizer slider 500 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_1kvolume") == "12", "Equalizer slider 1k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_2kvolume") == "12", "Equalizer slider 2k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_4kvolume") == "12", "Equalizer slider 4k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume") == "12", "Equalizer slider 8k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_16kvolume") == "12", "Equalizer slider 16k value is not 12"
        self.fc.fd["audio"].click_speaker_on_device()
        time.sleep(5)
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume") == "12", "Equalizer slider 32 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_64volume") == "12", "Equalizer slider 64 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_125volume") == "12", "Equalizer slider 125 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_250volume") == "12", "Equalizer slider 250 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume") == "12", "Equalizer slider 500 value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_1kvolume") == "12", "Equalizer slider 1k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_2kvolume") == "12", "Equalizer slider 2k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_4kvolume") == "12", "Equalizer slider 4k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume") == "12", "Equalizer slider 8k value is not 12"
        assert self.fc.fd["audio"].get_slider_value("equalizer_slider_16kvolume") == "12", "Equalizer slider 16k value is not 12"
        self.fc.swipe_window(direction="down", distance=2)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()


    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_equalizer_10_bars_remember_C32841927(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        
        self.fc.fd["audio"].set_equalizer_slider_value_increase(100,"equalizer_slider_32volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(100,"equalizer_slider_500volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(100,"equalizer_slider_8kvolume")
        time.sleep(2)
        
        self.fc.close_myHP()
        time.sleep(5)
        self.fc.launch_myHP()
        
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)

    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_04_equalizer_sliders_minimum_value_C32770330(self):
        self.fc.restart_myHP()
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        
        self.fc.fd["audio"].set_equalizer_slider_value_decrease(100,"equalizer_slider_32volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_decrease(100,"equalizer_slider_500volume")
        time.sleep(5)
        self.fc.fd["audio"].set_equalizer_slider_value_decrease(100,"equalizer_slider_8kvolume")
        time.sleep(2)
        
        volume32_value = self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume")
        assert volume32_value == "-12", "Equalizer slider 32 value is not -12"
        time.sleep(5)
        volume500_value = self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume")
        assert volume500_value == "-12", "Equalizer slider 500 value is not -12"
        time.sleep(5)
        volume8k_value = self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume")
        assert volume8k_value == "-12", "Equalizer slider 8k value is not -12"
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_05_equalizer_sliders_maximum_value_C32588198(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_internal_speaker_on_thompson()
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        time.sleep(2)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(100,"equalizer_slider_32volume")
        time.sleep(3)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(100,"equalizer_slider_500volume")
        time.sleep(3)
        self.fc.fd["audio"].set_equalizer_slider_value_increase(100,"equalizer_slider_8kvolume")
        time.sleep(3)
        
        volume32_value = self.fc.fd["audio"].get_slider_value("equalizer_slider_32volume")
        assert volume32_value == "12", "Equalizer slider 32 value is not 12"
        time.sleep(3)
        volume500_value = self.fc.fd["audio"].get_slider_value("equalizer_slider_500volume")
        assert volume500_value == "12", "Equalizer slider 500 value is not 12"
        time.sleep(3)
        volume8k_value = self.fc.fd["audio"].get_slider_value("equalizer_slider_8kvolume")
        assert volume8k_value == "12", "Equalizer slider 8k value is not 12"
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.fd["audio"].verify_restore_defaults_button_show()