from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Auido_OTA(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        time.sleep(10)
        cls.fc.fd["home"].click_to_install_signed_build()
        time.sleep(60)
        cls.fc.launch_myHP()
        time.sleep(5)
          
    def test_01_upgrade_myhp_verify_it_works_well_C35894177(self):
        self.fc.ota_app_after_update()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()    
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].verify_internal_speaker_output_device()
        self.fc.fd["audio"].verify_microphone_array_amd_input_device()
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        if not self.fc.fd["audio"].verify_equalizer_text_show():
            print("Equalizer text is not visible")
        if not self.fc.fd["audio"].verify_equalizer_tooltip_icon_show():
            print("Equalizer tooltip not visible")
        if not self.fc.fd["audio"].verify_equalizer_slider_volume_show():
            print("Equalizer slider 32 not visible")
        else:
            assert self.fc.fd["audio"].verify_equalizer_text_show(), "Equalizer text is not visible"
            assert self.fc.fd["audio"].verify_equalizer_tooltip_icon_show(), "Equalizer tooltip not visible"
            assert self.fc.fd["audio"].verify_equalizer_slider_volume_show(), "Equalizer slider 32 not visible"
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=7)
        self.fc.fd["audio"].verify_restore_defaults_button_show()
        self.fc.exit_hp_app_and_msstore()