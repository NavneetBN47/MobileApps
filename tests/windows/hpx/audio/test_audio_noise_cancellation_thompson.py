from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Audio_Noise_Cancellation(object):
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
            cls.fc.launch_myHP()
            time.sleep(3)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    #supported on thompson due to external device name
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_check_mic_mode_status_with_different_devices_C32784848(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["devices"].maximize_app()
        time.sleep(2)

        if  self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() != "1":
            self.fc.fd["audio"].click_internal_speaker_on_thompson()
            time.sleep(4)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_text_show() is True, "Conference is not show"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not selected"
        assert self.fc.fd["audio"].verify_personal_text_show() is True, "Personal is not show"
        assert bool(self.fc.fd["audio"].verify_studio_recording_show()) is True, "Studio Recording is not show"

        # Check with 3.5mm headphone
        self.fc.fd["audio"].click_headset_output_for_mm()
        time.sleep(2)
        assert self.fc.fd["audio"].is_headset_input_mm_device_selected() == "2", "headphone is not be selected"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_text_show() is False, "Conference is show"

        # Check with USB headphone
        self.fc.fd["audio"].click_headset_usb_input()
        time.sleep(2)
        assert self.fc.fd["audio"].is_headset_usb_input_selected() == "2", "headphone is not be selected"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_text_show() is False, "Conference is show"

        # Check with internal speaker again
        self.fc.fd["audio"].select_microphone_usb_audio_external_device()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_text_show() is True, "Conference is not show"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not selected"
        assert self.fc.fd["audio"].verify_personal_text_show() is True, "Personal is not show"
        assert bool(self.fc.fd["audio"].verify_studio_recording_show()) is True, "Studio Recording is not show"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_check_noise_reduction__status_with_different_input_devices_C42412540(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        if  self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() != "1":
            self.fc.fd["audio"].click_internal_speaker_on_thompson()
            time.sleep(4)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"

        # Check with 3.5mm headphone
        self.fc.fd["audio"].click_headset_output_for_mm()
        time.sleep(2)
        assert self.fc.fd["audio"].is_headset_input_mm_device_selected() == "2", "headphone is not be selected"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"

        # Check with USB headphone
        self.fc.fd["audio"].click_headset_usb_input()
        time.sleep(2)
        assert self.fc.fd["audio"].is_headset_usb_input_selected() == "2", "headphone is not be selected"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"

        # Check with internal speaker again
        self.fc.fd["audio"].click_internal_speaker_on_thompson()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_check_noise_removal__status_with_different_output_devices_C42412541(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        if  self.fc.fd["audio"].is_internal_speaker_on_thompson_selected() != "1":
            self.fc.fd["audio"].click_internal_speaker_on_thompson()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"

        # Check with 3.5mm headphone
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        time.sleep(2)
        assert self.fc.fd["audio"].is_internal_speaker_output_device_thompson_selected() == "2", "headphone is not be selected"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"

        # Check with USB headphone
        self.fc.fd["audio"].click_headset_usb_input()
        time.sleep(2)
        assert self.fc.fd["audio"].is_headset_usb_input_selected() == "2", "headphone is not be selected"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"

        # Check with internal speaker again
        self.fc.fd["audio"].click_internal_speaker_on_thompson()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
