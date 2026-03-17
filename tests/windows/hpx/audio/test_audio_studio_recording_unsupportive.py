from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Auido_Studio_Recording(object):
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
            cls.fc.launch_app()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

            
    # suite does not supported on bopeep thompson and arti   
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_audio_studio_recording_unsupport_machine_C38000097(self):
        time.sleep(2)
        self.fc.restart_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_studio_recording_show()) is False, "Studio Recording is show"
