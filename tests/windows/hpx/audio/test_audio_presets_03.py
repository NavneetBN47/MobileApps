import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Auido_Presets(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(2)
        
    #commercial device(snowwhite)
    @pytest.mark.commercial
    def test_01_launch_myhp_to_audio_control_page_verify_auto_option_will_show_up_under_presets_C38000796(self):
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
    
