import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_3_5mm")
class Test_Suite_Audio(object):
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    @pytest.mark.require_platform(["not available"])    # missing hardware necessary for this test, will remove once we have it
    def test_01_connected_external_device_will_show_on_combo_box_and_is_selected_automatically_C42197638(self):
        self.fc.fd["devicesMFE"].click_device_card()
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        self.vcosmos.remove_charger_and_usb()
        self.vcosmos.remove_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_microphone_array_selected_willie_robotics()) is True,"microphone array is not selected"
        assert bool(self.fc.fd["audio"].verify_speaker_selected_willie_robotics()) is True,"speaker array is not selected"
        #plug usb headphone
        self.vcosmos.add_charger_and_usb()
        assert bool(self.fc.fd["audio"].verify_usb_headphone_input_selected_willie_robotics()) is True,"usb headphone array is not selected"
        assert bool(self.fc.fd["audio"].verify_usb_headphone_output_selected_willie_robotics()) is True,"usb headphone array is not selected"

        self.fc.fd["audio"].click_input_combobox_open_button()
        assert bool(self.fc.fd["audio"].verify_microphone_array_dropbox_show_up_willie_robotics()) is True,"microphone array is not present"
        assert bool(self.fc.fd["audio"].verify_usb_headphone_input_dropbox_show_up_willie_robotics()) is True,"usb headphone is not present"
        #this closed the open dropbox (added in automation bug)
        self.fc.fd["audio"].click_output_combobox_open_button()
        self.fc.fd["audio"].click_output_combobox_open_button()
        assert bool(self.fc.fd["audio"].verify_output_device_internal_speaker_dropbox_show_up_willie_robotics()) is True,"internal speaker is not present"
        assert bool(self.fc.fd["audio"].verify_usb_headphone_output_dropbox_show_up_willie_robotics()) is True,"usb headphone is not present"

        self.vcosmos.remove_charger_and_usb()
        self.fc.fd["audio"].click_input_combobox_open_button()
        #plug 3.5 headphone
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_3_5_headphone_input_selected_willie_robotics()) is True,"3.5 headphone is not selected"
        assert bool(self.fc.fd["audio"].verify_3_5_headphone_output_selected_willie_robotics()) is True,"3.5 headphone is not selected"

        self.fc.fd["audio"].click_input_combobox_open_button()
        assert bool(self.fc.fd["audio"].verify_3_5_headphone_input_dropbox_show_up_willie_robotics()) is True,"3.5 headphone is not present"
        assert bool(self.fc.fd["audio"].verify_microphone_array_dropbox_show_up_willie_robotics()) is True,"microphone array is not present"
        assert bool(self.fc.fd["audio"].verify_usb_headphone_output_selected_willie_robotics()) is False,"usb headphone is present"
        #this closed the open dropbox (added in automation bug)
        self.fc.fd["audio"].click_output_combobox_open_button()
        self.fc.fd["audio"].click_output_combobox_open_button()
        assert bool(self.fc.fd["audio"].verify_output_device_headphone_show_up_willie_robotics()) is True,"3.5 headphone array is not present"
        assert bool(self.fc.fd["audio"].verify_output_device_internal_speaker_dropbox_show_up_willie_robotics()) is True,"speaker is not present"
        assert bool(self.fc.fd["audio"].verify_usb_headphone_output_dropbox_show_up_willie_robotics()) is False,"usb headphone is present"
        self.fc.fd["audio"].click_input_combobox_open_button()
        self.vcosmos.remove_3_5_headphone()

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_02_mute_unmute_from_keyboard_verify_the_status_of_mute_button_C42197655(self):
        self.vcosmos.add_charger_and_usb()
        self.fc.fd["devicesMFE"].click_device_card()
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0","mute toggle is on"
        self.vcosmos.press_mute_button()
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "1","mute toggle is off"
        self.vcosmos.press_mute_button()
        assert self.fc.fd["audio"].get_mute_toggle_for_input_status() == "0","mute toggle is on"
        self.fc.fd["devicesMFE"].maximize_app()
        self.vcosmos.clean_up_logs()