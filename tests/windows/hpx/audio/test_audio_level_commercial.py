from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Audio_Level_Commercial(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        time.sleep(2)
        cls.fc.launch_myHP()
        
    #warpath only
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_audio_will_not_show_less_than_24c1_platform_C37999493(self):
        time.sleep(3)
        self.fc.restart_app()

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)

        assert bool(self.fc.fd["audio"].verify_home_audio_show()) is False

        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)

        assert bool(self.fc.fd["audio"].verify_audio_show()) is False