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
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
    

    #the tiger with  less that 24C1 cycle
    @pytest.mark.ota
    def test_01_n_b_omen_internal_speaker_C32342545(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        assert bool( self.fc.fd["audio"].verify_bang_and_olufsen_logo()) is True, "bang and olufsen logo is invisible"

    def test_01_n_b_omen_3_5_C32342542(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_headphone_plugin_pc()
        assert bool( self.fc.fd["audio"].verify_dts_logo_less_than_24c1()) is True, "DTSX logo is invisible"