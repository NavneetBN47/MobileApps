import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import logging


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_External_speaker_settings(object):


    @pytest.mark.function
    @pytest.mark.consumer
    def test_01_check_speaker_configuration_ui_C42214021(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)  
        # select other device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up(), "Output internal speaker device is not displayed"
        self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)
        # verify external speaker settings show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
        time.sleep(2)
        # click external speaker settings
        self.fc.fd["audio"].click_external_speaker_settings()
        time.sleep(2)
        # verify external speaker settings text show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
        time.sleep(2)
        # click external speaker settings restore default button
        self.fc.fd["audio"].click_external_speaker_settings_restore_default()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=16)
        time.sleep(2)
        # verify speaker configuration option show up
        assert self.fc.fd["audio"].verify_multistreaming_toggle_off_show_up() , "Multistreaming toggle is not displayed"
        time.sleep(2) 
        self.fc.fd["audio"].click_speaker_configuration_open_option()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_stereo_show_up(), "Speaker configuration option stereo is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_quad_show_up(), "Speaker configuration option quad is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_speaker_configuration_option_surround_show_up(), "Speaker configuration option surround is not displayed"
        time.sleep(2)
        # click speaker configuration option to select surround
        self.fc.fd["audio"].select_speaker_configuration_option_surround()
        time.sleep(2)
        # verify speaker configuration option surround
        assert self.fc.fd["audio"].get_speaker_configuration_option() == "Surround", "Speaker configuration option surround is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_distance() == "15 ft", "Front left speaker distance default is not 15 ft"
        time.sleep(2)
        self.fc.fd["audio"].click_front_left_speaker_distance_combobox()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_distance_combobox_14_9_ft_show_up(), "Front left speaker distance combobox 14.9 ft is not displayed"
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_volume() == "0 dB", "Front right speaker distance default is not -1 dB"
        time.sleep(2)
        self.fc.fd["audio"].click_front_left_speaker_volume_combobox()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_front_left_speaker_volume_combobox_1_db_show_up(), "Front right speaker volume combobox 0 db is not displayed"
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.OTA
    def test_02_back_audio_page_by_click_back_arrow_on_external_speaker_settings_page_C52017572(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "back arrow shows on audio control page"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up(), "Output internal speaker device is not displayed"
        self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=14)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_external_speaker_settings_title_show_up(), "External speaker settings title is not displayed"
        assert self.fc.fd["audio"].verify_arrow_right_on_external_speaker_settings_show_up(), "External speaker settings arrow is not displayed"
        self.fc.fd["audio"].click_arrow_right_on_external_speaker_settings()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_back_button_on_audio_page(), "back arrow shows on audio control page"
        assert self.fc.fd["audio"].verify_external_speaker_settings_title_show_up(), "External speaker settings title is not displayed"
        self.fc.fd["audio"].click_back_button_on_audio_page()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_title_on_header_show_up(), "Audio title shows on audio control page"
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"


    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_verify_external_speaker_settings_can_be_remember_when_relaunch_hpx_C42197706(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)  
        # select other device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].verify_output_device_35mm_headphone_on_snowball_show_up()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_35mm_headphone_on_snowball()
        time.sleep(2)
        # select internal speaker device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)
        # verify external speaker settings show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
        time.sleep(2)
        # click external speaker settings
        self.fc.fd["audio"].click_external_speaker_settings()
        time.sleep(2)
        # verify external speaker settings text show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
        time.sleep(2)
        self.fc.fd["audio"].swipe_to_external_speaker_settings_restore_defaults_button()
        time.sleep(2)
        # click external speaker settings restore default button
        self.fc.fd["audio"].click_external_speaker_settings_restore_default()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=16)
        time.sleep(2)
        # click speaker configuration option to select surround
        self.fc.fd["audio"].click_speaker_configuration_open_option()
        time.sleep(2)
        self.fc.fd["audio"].verify_speaker_configuration_option_surround_show_up()
        time.sleep(2)
        self.fc.fd["audio"].select_speaker_configuration_option_surround()
        time.sleep(2)
        # verify speaker configuration option surround show up
        assert self.fc.fd["audio"].get_speaker_configuration_option() == "Surround", "Speaker configuration option surround is not displayed"
        time.sleep(2)
        # verify front left speaker distance default is 15 ft
        assert self.fc.fd["audio"].verify_front_left_speaker_distance() == "15 ft", "Front left speaker distance default is not 15 ft"
        time.sleep(2)
        # click front left speaker distance combobox
        self.fc.fd["audio"].click_front_left_speaker_distance_combobox()
        time.sleep(2)
        # verify front left speaker distance combobox 14.9 ft show up
        assert self.fc.fd["audio"].verify_front_left_speaker_distance_combobox_14_9_ft_show_up(), "Front left speaker distance combobox 15.1 ft is not displayed"
        time.sleep(2)
        # select front left speaker distance combobox 14.9 ft
        self.fc.fd["audio"].select_front_left_speaker_distance_combobox_14_9_ft()
        time.sleep(2)
        # verify front left speaker distance is 14.9 ft
        assert self.fc.fd["audio"].verify_front_left_speaker_distance() == "14.9 ft", "Front left speaker distance is not 14.9 ft"
        time.sleep(2)
        # verify front left speaker volume default is 0 db
        assert self.fc.fd["audio"].verify_front_left_speaker_volume() == "0 dB", "Front right speaker distance default is not -1 dB"
        time.sleep(2)
        # click front left speaker volume combobox
        self.fc.fd["audio"].click_front_left_speaker_volume_combobox()
        time.sleep(2)
        # verify front left speaker volume combobox -1 db show up
        assert self.fc.fd["audio"].verify_front_left_speaker_volume_combobox_1_db_show_up(), "Front right speaker volume combobox 0 db is not displayed"
        time.sleep(2)
        # select front left speaker volume combobox -1 db
        self.fc.fd["audio"].select_front_left_speaker_volume_combobox_1_db()
        time.sleep(2)
        # verify front left speaker volume is -1 db
        assert self.fc.fd["audio"].verify_front_left_speaker_volume() == "-1 dB", "Front right speaker volume is not -1 dB"
        time.sleep(2)

        # click back button on top left corner
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(2)
        # verify output internal device is selected
        assert self.fc.fd["audio"].verify_output_internal_device_show_on_arti(), "Output internal device is not selected"
        time.sleep(2)
        # click back button on top left corner
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        # verify audio card is show up
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        # click audio card
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # select other device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].verify_output_35mm_external_device_arti_show()
        time.sleep(2)
        self.fc.fd["audio"].select_output_35mm_external_device_arti()
        time.sleep(2)
        # select internal speaker device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].verify_output_internal_device_arti_show()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device_arti()
        time.sleep(2)
        # verify output internal device is selected
        assert self.fc.fd["audio"].verify_output_internal_device_show_on_arti(), "Output internal device is not selected"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)
        # verify external speaker settings show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
        time.sleep(2)
        # click external speaker settings
        self.fc.fd["audio"].click_external_speaker_settings()
        time.sleep(2)
        # verify external speaker settings text show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
        time.sleep(2)
        # verify front left speaker distance is 14.9 ft
        assert self.fc.fd["audio"].verify_front_left_speaker_distance() == "14.9 ft", "Front left speaker distance is not 14.9 ft"
        time.sleep(2)
        # verify front left speaker volume default is -1 db
        assert self.fc.fd["audio"].verify_front_left_speaker_volume() == "-1 dB", "Front right speaker distance default is not -1 dB"
        time.sleep(2)

        # relaunch myHP
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # select other device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].verify_output_device_35mm_headphone_on_snowball_show_up()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_35mm_headphone_on_snowball()
        time.sleep(2)
        # select internal speaker device
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
        time.sleep(2)
        # verify output internal device is selected
        assert self.fc.fd["audio"].verify_output_internal_device_show_on_arti(), "Output internal device is not selected"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=16)
        time.sleep(3)
        # verify external speaker settings show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
        time.sleep(2)
        # click external speaker settings
        self.fc.fd["audio"].click_external_speaker_settings()
        time.sleep(2)
        # verify external speaker settings text show up
        assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
        time.sleep(2)
        # verify front left speaker distance is 14.9 ft
        assert self.fc.fd["audio"].verify_front_left_speaker_distance() == "14.9 ft", "Front left speaker distance is not 14.9 ft"
        time.sleep(2)
        # verify front left speaker volume default is -1 db
        assert self.fc.fd["audio"].verify_front_left_speaker_volume() == "-1 dB", "Front right speaker distance default is not -1 dB"
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer
    def test_04_verify_multi_streaming_work_well_when_launch_hpx_C42197702(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        
        # verify output external speaker headphone show
        if self.fc.fd["audio"].verify_output_external_speaker_headphone_show() is True:
            logging.info("Output external speaker headphone is available")
            # select other device
            self.fc.fd["audio"].verify_output_device_usb_headphone_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_device_usb_headphone_on_snowball()
            time.sleep(2)
            # select output external speaker headphone
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].click_output_external_speaker_headphone()
            time.sleep(2)
            # get output external speaker headphone is selected
            assert self.fc.fd["audio"].get_output_drop_down_list_name() == "Speaker/Headphone (Realtek(R) Audio)", "Output external speaker headphone is not selected"
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=16)
            time.sleep(3)
            # verify external speaker settings show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
            time.sleep(2)
            # click external speaker settings
            self.fc.fd["audio"].click_external_speaker_settings()
            time.sleep(2)
            # verify external speaker settings text show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
            time.sleep(2)
            # verify multistreaming toggle have show
            assert self.fc.fd["audio"].verify_multistreaming_toggle_off_show_up() , "Multistreaming toggle is not displayed"
            time.sleep(2) 
            # verify multistreaming toggle is off state
            assert self.fc.fd["audio"].get_multistreaming_toggle_off_state() == "0", "Multistreaming toggle is not disabled"
            time.sleep(5)
            # click multistreaming toggle
            self.fc.fd["audio"].click_multistreaming_toggle_off_state()
            time.sleep(2)
            # verify multistreaming toggle is on state
            assert self.fc.fd["audio"].get_multistreaming_toggle_on_state() == "1", "Multistreaming toggle is not disabled"
            time.sleep(2)
            if bool(self.fc.fd["audio"].verify_continue_button_on_speaker_not_support_dialog()):
            # click continue button on speaker not support dialog
                self.fc.fd["audio"].click_continue_button_on_speaker_not_support_dialog()
                time.sleep(2)
            elif self.fc.fd["devices_details_pc_mfe"].click_back_devices_button():
                time.sleep(2)
            # select other device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_device_usb_headphone_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_device_usb_headphone_on_snowball()
            time.sleep(2)
            # select internal speaker device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
            time.sleep(2)
            # select other device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_device_usb_headphone_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_device_usb_headphone_on_snowball()
            time.sleep(2)
            # select internal speaker device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
            time.sleep(2)
            # verify output internal device is selected
            assert self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up(), "Output internal device is not selected"
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=16)
            time.sleep(3)
            # verify external speaker settings show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
            time.sleep(2)
            # click external speaker settings
            self.fc.fd["audio"].click_external_speaker_settings()
            time.sleep(2)
            # verify external speaker settings text show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
            time.sleep(2)
            # verify multistreaming toggle have show
            assert self.fc.fd["audio"].verify_multistreaming_toggle_on_show_up() , "Multistreaming toggle is not displayed"
            time.sleep(2) 
            # verify multistreaming toggle is on state
            assert self.fc.fd["audio"].get_multistreaming_toggle_on_state() == "1", "Multistreaming toggle is not disabled"
            time.sleep(2)
            # click multistreaming toggle
            self.fc.fd["audio"].click_multistreaming_toggle_on_state()
            time.sleep(2)
            # verify multistreaming toggle is off state
            assert self.fc.fd["audio"].get_multistreaming_toggle_off_state() == "0", "Multistreaming toggle is not disabled"
            time.sleep(2)
            if bool(self.fc.fd["audio"].verify_continue_button_on_speaker_not_support_dialog()):
            # click continue button on speaker not support dialog
                self.fc.fd["audio"].click_continue_button_on_speaker_not_support_dialog()
                time.sleep(2)
            elif self.fc.fd["devices_details_pc_mfe"].click_back_devices_button():
                time.sleep(2)
            # verify output external speaker headphone is selected
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_output_external_speaker_headphone_show(), "Output external speaker headphone is not selected"
            time.sleep(2) 
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)

        # verify output internal device show on arti
        else:
            # select other device
            self.fc.fd["audio"].verify_output_usb_external_device_arti_show()
            time.sleep(2)
            self.fc.fd["audio"].select_output_usb_external_device_arti()
            time.sleep(2)
            # select internal speaker device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_internal_device_arti_show()
            time.sleep(2)
            self.fc.fd["audio"].select_output_internal_device_arti()
            time.sleep(2)
            # verify output internal device is selected
            assert self.fc.fd["audio"].verify_output_internal_device_show_on_arti(), "Output internal device is not selected"
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=16)
            time.sleep(3)
            # verify external speaker settings show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
            time.sleep(2)
            # click external speaker settings
            self.fc.fd["audio"].click_external_speaker_settings()
            time.sleep(2)
            # verify external speaker settings text show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
            time.sleep(2)
            # verify multistreaming toggle have show
            assert self.fc.fd["audio"].verify_multistreaming_toggle_on_show_up() , "Multistreaming toggle is not displayed"
            time.sleep(2) 
            # verify multistreaming toggle is on state
            assert self.fc.fd["audio"].get_multistreaming_toggle_on_state() == "1", "Multistreaming toggle is not disabled"
            time.sleep(2)
            # click multistreaming toggle
            self.fc.fd["audio"].click_multistreaming_toggle_on_state()
            time.sleep(2)
            # verify multistreaming toggle is off state
            assert self.fc.fd["audio"].get_multistreaming_toggle_off_state() == "0", "Multistreaming toggle is not disabled"
            time.sleep(2)
            if bool(self.fc.fd["audio"].verify_continue_button_on_speaker_not_support_dialog()):
            # click continue button on speaker not support dialog
                self.fc.fd["audio"].click_continue_button_on_speaker_not_support_dialog()
                time.sleep(2)
            elif self.fc.fd["devices_details_pc_mfe"].click_back_devices_button():
                time.sleep(2)
            # select other device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_device_usb_headphone_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_device_usb_headphone_on_snowball()
            time.sleep(2)
            # select output external speaker headphone
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].click_output_external_speaker_headphone()
            time.sleep(2)
            # select other device
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].verify_output_device_usb_headphone_on_snowball_show_up()
            time.sleep(2)
            self.fc.fd["audio"].click_output_device_usb_headphone_on_snowball()
            time.sleep(2)
            # select output external speaker headphone
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].click_output_external_speaker_headphone()
            time.sleep(2)
            # verify output external speaker headphone is selected
            assert self.fc.fd["audio"].verify_output_external_speaker_headphone_show(), "Output external speaker headphone is not selected"
            time.sleep(2)
            self.fc.swipe_window(direction="down", distance=16)
            time.sleep(3)
            # verify external speaker settings show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
            time.sleep(2)
            # click external speaker settings
            self.fc.fd["audio"].click_external_speaker_settings()
            time.sleep(2)
            # verify external speaker settings text show up
            assert self.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
            time.sleep(2)
            # verify multistreaming toggle have show
            assert self.fc.fd["audio"].verify_multistreaming_toggle_off_show_up() , "Multistreaming toggle is not displayed"
            time.sleep(2) 
            # verify multistreaming toggle is off state
            assert self.fc.fd["audio"].get_multistreaming_toggle_off_state() == "0", "Multistreaming toggle is not disabled"
            time.sleep(5)
            # click multistreaming toggle
            self.fc.fd["audio"].click_multistreaming_toggle_off_state()
            time.sleep(2)
            # verify multistreaming toggle is on state
            assert self.fc.fd["audio"].get_multistreaming_toggle_on_state() == "1", "Multistreaming toggle is not disabled"
            time.sleep(2)
            if bool(self.fc.fd["audio"].verify_continue_button_on_speaker_not_support_dialog()):
            # click continue button on speaker not support dialog
                self.fc.fd["audio"].click_continue_button_on_speaker_not_support_dialog()
                time.sleep(2)
            elif self.fc.fd["devices_details_pc_mfe"].click_back_devices_button():
                time.sleep(2)
            #verify output internal device is selected
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_output_internal_speaker_on_snowball_show_up(), "Output internal device is not selected"
            time.sleep(2)
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)