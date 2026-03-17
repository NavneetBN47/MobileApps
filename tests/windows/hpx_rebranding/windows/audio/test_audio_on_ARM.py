import time
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_functional_MEP_notification")
class Test_Suite_Audio_On_ARM(object):


    @pytest.mark.function
    @pytest.mark.integration
    @pytest.mark.ARM
    def test_01_check_MEP_notification_on_ARM_machine_C49136453(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
            time.sleep(3)
        # check input mic on windows will show up after open settings page
        assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
        self.fc.fd["audio"].click_input_mic_on_quardo()
        time.sleep(5)
        # check audio enhancements combobox on windows after clicking input mic
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        self.fc.fd["audio"].click_non_mep_option_on_windows()
        time.sleep(5)
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_new_mep_option_on_windows()
        time.sleep(4)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_toast_show_up(), "MEP notification toast is not displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.integration
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    def test_02_check_MEP_ui_on_ARM_machine_C58771973(self):
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        # check MEP option on myHP
        if self.fc.fd["audio"].verify_mep_ui_show_up() is False:
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
             # check input mic on windows will show up after open settings page
            assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
            self.fc.fd["audio"].click_input_mic_on_quardo()
            time.sleep(5)
            # check audio enhancements combobox on windows after clicking input mic
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_new_mep_option_on_windows()
            time.sleep(4)
            self.fc.close_windows_settings_panel()
            time.sleep(3)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"

    
    @pytest.mark.function
    @pytest.mark.ARM
    def test_03_check_MEP_prompts_C49136468(self):
        if self.fc.fd["audio"].verify_mep_ui_show_up is False:
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
             # check input mic on windows will show up after open settings page
            assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
            self.fc.fd["audio"].click_input_mic_on_quardo()
            time.sleep(5)
            # check audio enhancements combobox on windows after clicking input mic
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_new_mep_option_on_windows()
            time.sleep(4)
            self.fc.close_windows_settings_panel()
            time.sleep(3)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        assert self.fc.fd["audio"].verify_mep_contents_on_myhp_show_up(), "Learn more link is not displayed on myHP"
        self.fc.fd["audio"].click_learn_more_link_on_mep()
        time.sleep(5)
        # check MEP pop up dialog
        assert self.fc.fd["audio"].verify_mep_pop_up_dialog_title_show_up(), "MEP title is not displayed on pop-up dialog"
        assert self.fc.fd["audio"].verify_mep_pop_up_dialog_second_title_show_up(), "MEP second title is not displayed on pop-up dialog"
        assert self.fc.fd["audio"].verify_noise_reduction_contents_on_mep_pop_up_dialog_show_up(), "Noise reduction contents are not displayed on MEP pop up dialog"
        assert self.fc.fd["audio"].verify_conference_mode_contents_on_mep_pop_up_dialog_show_up, "Conference mode contents are not displayed on MEP pop up dialog"
        assert self.fc.fd["audio"].verify_personal_mode_contents_on_mep_pop_up_dialog_show_up(), "Personal mode contents are not displayed on MEP pop up dialog"
        assert self.fc.fd["audio"].verify_studio_recording_mode_contents_on_mep_pop_up_dialog_show_up(), "Studio recording mode contents are not displayed on MEP pop up dialog"
        assert self.fc.fd["audio"].verify_cancel_button_on_mep_pop_up_dialog_show_up(), "Cancel button is not displayed on MEP pop up dialog"
        assert self.fc.fd["audio"].verify_go_to_windows_sound_settings_button_on_mep_pop_up_dialog_show_up(), "Go to Windows sound settings button is not displayed on MEP pop up dialog"
        self.fc.fd["audio"].click_cancel_button_on_mep_pop_up_dialog()
        time.sleep(2)


    @pytest.mark.function
    @pytest.mark.ARM
    @pytest.mark.integration
    def test_04_check_audio_will_have_reduced_functionality_after_enable_mep_C49136452(self):
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        if self.fc.fd["audio"].verify_mep_ui_show_up() is False:
            self.fc.swipe_window(direction="down", distance=20)
            time.sleep(3)
            assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
            self.fc.fd["audio"].click_restore_defaults_button()
            time.sleep(3)
            self.fc.close_myHP()
            time.sleep(3)
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
             # check input mic on windows will show up after open settings page
            assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
            self.fc.fd["audio"].click_input_mic_on_quardo()
            time.sleep(5)
            # check audio enhancements combobox on windows after clicking input mic
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_new_mep_option_on_windows()
            time.sleep(4)
            self.fc.close_windows_settings_panel()
            time.sleep(3)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check MEP option on myHP
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        assert self.fc.fd["audio"].verify_mep_contents_on_myhp_show_up(), "Learn more link is not displayed on myHP"
        # check audio functionality after enable MEP
        assert self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle() == 'false', "AI noise removal toggle is enabled after enable MEP"
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].is_enabled_noise_reduction_toggle() == 'false', "Noise reduction toggle is enabled after enable MEP"
        # assert self.fc.fd["audio"].is_enabled_mic_mode_toggle() == 'false', "Mic mode combobox is enabled after enable MEP"
    

    @pytest.mark.function
    @pytest.mark.ARM
    def test_05_check_audio_work_well_after_click_restore_defaults_button_C49136466(self):
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check restore defaults button on myHP
        if self.fc.fd["audio"].verify_mep_ui_show_up() is False:
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
             # check input mic on windows will show up after open settings page
            assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
            self.fc.fd["audio"].click_input_mic_on_quardo()
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_new_mep_option_on_windows()
            time.sleep(4)
            self.fc.close_windows_settings_panel()
            time.sleep(3)  
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # click restore defaults button on myHP
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # check MEP on myhp
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        assert self.fc.fd["audio"].verify_mep_contents_on_myhp_show_up(), "Learn more link is not displayed on myHP"

    
    @pytest.mark.function
    @pytest.mark.ARM
    def test_06_check_mep_will_keep_after_relaunch_myhp_C49136463(self):
        if self.fc.fd["audio"].verify_mep_ui_show_up() is False:
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
            # check input mic on windows will show up after open settings page
            assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
            self.fc.fd["audio"].click_input_mic_on_quardo()
            time.sleep(5)
            # check audio enhancements combobox on windows after clicking input mic
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_new_mep_option_on_windows()
            time.sleep(4)
            self.fc.close_windows_settings_panel()
            time.sleep(3)
            self.fc.launch_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        # check MEP on myhp
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        # relaunch myHP 
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check MEP on myhp
        assert self.fc.fd["audio"].verify_mep_ui_show_up(), "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_windows_sound_settings_mep_show_up(), "Windows sound settings not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(), "Learn more link is not displayed on myHP"
        self.fc.close_myHP()
        time.sleep(3)

    
    @pytest.mark.function
    @pytest.mark.ARM
    def test_07_check_mep_function_will_enable_with_non_mep_option_selected_C49136451(self):
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.close_myHP()
        time.sleep(5)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
            time.sleep(3)
        # check input mic on windows will show up after open settings page
        assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
        self.fc.fd["audio"].click_input_mic_on_quardo()
        time.sleep(5)
        # check audio enhancements combobox on windows after clicking input mic
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_non_mep_option_on_windows()
        time.sleep(4)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is False, "MEP ui is displayed on myHP"
        # check audio functionality after enable MEP
        assert self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle() == "true","Noise removal toggle is not enabled after enable MEP"
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].is_enabled_noise_reduction_toggle() == "true", "Noise reduction toggle is not enabled after enable MEP"
        self.fc.close_myHP()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_08_check_audio_will_recover_after_disable_mep_from_link_C49136462(self):
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(5)
        if self.fc.fd["audio"].verify_mep_ui_show_up() is False:
            self.fc.close_myHP()
            time.sleep(3)
            self.fc.open_system_settings_sound()
            time.sleep(5)
            if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                self.fc.fd["audio"].click_on_system_settings_maximize_button()
                time.sleep(3)
            # check input mic on windows will show up after open settings page
            assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
            self.fc.fd["audio"].click_input_mic_on_quardo()
            time.sleep(5)
            # check audio enhancements combobox on windows after clicking input mic
            assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
            self.fc.fd["audio"].click_new_mep_option_on_windows()
            time.sleep(4)
            self.fc.close_windows_settings_panel()
            time.sleep(3)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(5)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is True, "MEP ui is not displayed on myHP"
        assert self.fc.fd["audio"].verify_learn_more_link_title_on_mep_show_up(),"Learn more link is not displayed after enable MEP"
        self.fc.fd["audio"].click_learn_more_link_on_mep()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_pop_up_dialog_title_show_up(), "MEP title is not displayed on pop-up dialog"
        assert self.fc.fd["audio"].verify_go_to_windows_sound_settings_button_on_mep_pop_up_dialog_show_up(), "Go to Windows sound settings button is not displayed on MEP pop up dialog"
        self.fc.fd["audio"].click_go_to_windows_sound_settings_button_on_mep_pop_up_dialog()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        # check input mic on windows will show up after open settings page
        assert self.fc.fd["audio"].verify_mic_on_all_sounds_devices_page_show_up(), "Input mic is not displayed on Quardo"
        self.fc.fd["audio"].click_mic_on_all_sounds_devices_page()
        time.sleep(5)
        # check audio enhancements combobox on windows after clicking input mic
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        self.fc.fd["audio"].click_non_mep_option_on_windows()
        time.sleep(4)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        # check MEP on myhp
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is False, "MEP ui is displayed on myHP"
        assert self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle() == 'true',"Noise removal toggle is not enabled after enable MEP"
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].is_enabled_noise_reduction_toggle() == 'true', "Noise reduction toggle is not enabled after enable MEP"
        self.fc.close_myHP()
        time.sleep(3)
    

    @pytest.mark.function
    @pytest.mark.ARM
    def test_09_check_there_have_three_options_on_windows_C49136449(self):
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        # check input mic on windows will show up after open settings page
        assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
        self.fc.fd["audio"].click_input_mic_on_quardo()
        time.sleep(5)
        # check audio enhancements combobox on windows after clicking input mic
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_new_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        assert self.fc.fd["audio"].verify_off_option_on_windows_input_side_show_up(), "Off option is not displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_10_check_audio_will_work_well_after_disable_mep_C49136454(self):
        self.fc.close_myHP()
        time.sleep(2)
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        # check input mic on windows will show up after open settings page
        assert self.fc.fd["audio"].verify_input_mic_on_quardo_show_up(), "Input mic is not displayed on Quardo"
        self.fc.fd["audio"].click_input_mic_on_quardo()
        time.sleep(5)
        # check audio enhancements combobox on windows after clicking input mic
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        self.fc.fd["audio"].click_non_mep_option_on_windows()
        time.sleep(5)
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        # check audio functionality after disable MEP
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_mep_ui_show_up() is False, "MEP ui is displayed on myHP"
        assert self.fc.fd["audio"].is_enabled_ai_noise_removal_toggle() == 'true',"Noise removal toggle is not enabled after enable MEP"
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].is_enabled_noise_reduction_toggle() == 'true', "Noise reduction toggle is not enabled after enable MEP"
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