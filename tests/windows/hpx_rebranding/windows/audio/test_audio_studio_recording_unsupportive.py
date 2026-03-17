import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Audio_Studio_Recording_Unsupportive(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.classic_fc = classic_FlowContainer(cls.driver)           
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["display_control"].click_to_install_signed_build()
            time.sleep(60)
            cls.classic_fc.launch_myHP()
            time.sleep(5)
            cls.classic_fc.ms_store_app_update()
            cls.fc.ota_app_after_update("classic")
        else:
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_check_studio_recording_unsupportive_machine_C42197743(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)

        self.fc.fd["audio"].verify_input_combobox_show_up()
        self.fc.fd["audio"].click_input_combobox_open_button()
        self.fc.fd["audio"].select_input_internal_device()
        time.sleep(2)

        if self.fc.fd["audio"].verify_conference_show_up():
            self.fc.fd["audio"].click_conference_items()
        elif self.fc.fd["audio"].verify_personal_show_up():
            self.fc.fd["audio"].click_personal_items()
        else:
            self.fc.fd["audio"].click_studio_recording_items()
        
        assert self.fc.fd["audio"].verify_studio_recording_mode_show_up() is False, "Studio recording is displayed"