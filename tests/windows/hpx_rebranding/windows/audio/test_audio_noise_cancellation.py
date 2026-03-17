import time
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Noise_Cancellation(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_01_check_noise_cancellation_ui_C42214009(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        # check oise cancellation ui
        if self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up(), "AI Noise Removal toggle is not displayed"
        # restore noise cancellation ui
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=7)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up(), "AI Noise Reduction toggle is not displayed"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_02_turn_on_off_noise_removal_toggle_C43809586(self):
        self.fc.swipe_window(direction="up", distance=5)
        time.sleep(2)
        if self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_removal_title_show_up(), "AI Noise Removal title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_removal_toggle_show_up(), "AI Noise Removal toggle is not displayed"
        if self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1":
            time.sleep(2)
            self.fc.fd["audio"].turn_off_noise_removal()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
            time.sleep(2)
            self.fc.fd["audio"].turn_on_noise_removal()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"
        else:
            time.sleep(2)
            self.fc.fd["audio"].turn_on_noise_removal()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "AI Noise Removal toggle is not turned on"
            time.sleep(2)
            self.fc.fd["audio"].turn_off_noise_removal()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_off_state() == "0", "AI Noise Removal toggle is not turned off"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_03_turn_on_off_noise_reduction_toggle_C43809587(self):
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        if self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=13)
            time.sleep(2)
        # restore noise cancellation ui
        self.fc.fd["audio"].swipe_to_restore_defaults_button()
        time.sleep(2)
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=7)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_title_show_up(), "AI Noise Reduction title is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "AI Noise Reduction tooltip is not displayed"
        assert self.fc.fd["audio"].verify_ai_noise_reduction_toggle_show_up(), "AI Noise Reduction toggle is not displayed"
        if self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1":
            time.sleep(2)
            self.fc.fd["audio"].turn_off_noise_reduction()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "0", "Noise Reduction toggle is not turned off"
            time.sleep(2)
            self.fc.fd["audio"].turn_on_noise_reduction()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
        else:
            time.sleep(2)
            self.fc.fd["audio"].turn_on_noise_reduction()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise Reduction toggle is not turned on"
            time.sleep(2)
            self.fc.fd["audio"].turn_off_noise_reduction()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_off_state() == "0", "Noise Reduction toggle is not turned off"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    def test_04_verify_conference_personal_checkbox_C43809585(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        if self.fc.fd["audio"].verify_conference_show_up():
            self.fc.fd["audio"].click_conference_items()
        elif self.fc.fd["audio"].verify_personal_show_up():
            self.fc.fd["audio"].click_personal_items()
        else:
            self.fc.fd["audio"].click_studio_recording_items()
        time.sleep(2)
        self.fc.fd["audio"].selected_personal_mode()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_personal_show_up(), "Personal option doesn't show up"
        self.fc.fd["audio"].click_personal_items()
        time.sleep(2)
        self.fc.fd["audio"].selected_conferenece_mode()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_conference_show_up(), "Conference option doesn't show up"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    def test_05_check_noise_cancellation_tooltip_C49136657(self):
        self.fc.swipe_window(direction="up", distance=10)
        time.sleep(2)
        if self.fc.fd["audio"].verify_ai_noise_removal_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_removal_tooltip_show_up(), "AI Noise Removal tooltip is not displayed"
        self.fc.fd["audio"].click_ai_noise_removal_tooltip()
        assert self.fc.fd["audio"].get_ai_noise_removal_tooltip_text() == "This feature will remove background noise coming from your speaker", "AI Noise Removal tooltip text is not displayed"
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_ai_noise_reduction_tooltip_show_up(), "Noise Reduction tooltip is not displayed"
        self.fc.fd["audio"].click_noise_reduction_tooltip()
        assert self.fc.fd["audio"].get_noise_reduction_tooltip_text() == "Removes background noise coming from your microphone", "Noise Reduction tooltip text is not displayed"