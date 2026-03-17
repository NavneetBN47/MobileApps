from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Level(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()

    #the 360 nitanny with  less that 24C1 cycle
    @pytest.mark.ota
    def test_01_wnb_360_and_detachable_C32342036(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        assert bool( self.fc.fd["audio"].verify_bang_and_olufsen_logo()) is True, "bang and olufsen logo is invisible"