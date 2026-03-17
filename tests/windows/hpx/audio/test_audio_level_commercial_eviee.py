from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Audio_Level_Commercial(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        time.sleep(2)
        cls.fc.launch_myHP()
        
    #suit for eviee commercial
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_audio_will_show_greater_than_24c1_platform_C37999465(self):
        time.sleep(3)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        output_display = self.fc.fd["audio"].verify_output_title()
        assert output_display == True, "Output title doesn't show on audio control page"
