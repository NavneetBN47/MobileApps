from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Commercial(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        time.sleep(2)
        cls.fc.launch_myHP()
        
    #snowhite only with audio
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_audio_control_module_will_not_show_up_when_standalone_app_exists_C40812513(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_home_audio_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_audio_show()) is True
        self.fc.close_myHP()
        self.fc.install_audio_standalone_24h2()
        self.fc.launch_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_home_audio_show()) is False
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_audio_show()) is False
        self.fc.close_myHP()
        self.fc.uninstall_audio_standalone()
        self.fc.launch_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_home_audio_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_audio_show()) is True

    @pytest.mark.commercial
    def test_02_with_3_5mm_verify_it_should_show_4_presets_C38000796(self):
        self.fc.restart_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].verify_pc_audio_show()    
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_auto_preset_show()) is True
        assert bool(self.fc.fd["audio"].verify_preset_music_show()) is True
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is True
        self.fc.fd["audio"].click_headphone_plugin_pc()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_auto_preset_show()) is True
        assert bool(self.fc.fd["audio"].verify_preset_music_show()) is True
        assert bool(self.fc.fd["audio"].verify_voice_checkbox_show()) is True
        assert bool(self.fc.fd["audio"].verify_movie_checkbox_show()) is True




