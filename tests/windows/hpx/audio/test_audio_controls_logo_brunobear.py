from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Level(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(2)
    

    #the brunobear with equal to 24C1 cycle and upper
    def test_01_nomen_hyperx_dtsx_C37677679(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        assert bool( self.fc.fd["audio"].verify_hyperx_logo()) is True, "hyperX logo is invisible"
        self.fc.fd["audio"].click_headphone_plugin_pc()
        assert bool( self.fc.fd["audio"].verify_dtsx_logo_24c1_and_above()) is True, "DTSX logo is invisible"
        self.fc.fd["audio"].click_headset_usb_input_rameses()
        assert bool( self.fc.fd["audio"].verify_hyperx_logo()) is False, "hyperX logo is visible"
        assert bool( self.fc.fd["audio"].verify_dtsx_logo_24c1_and_above()) is False, "DTSX logo is visible"
