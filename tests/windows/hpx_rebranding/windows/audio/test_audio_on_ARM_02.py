import time
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_functional_MEP_notification")
class Test_Suite_Audio_On_ARM_02(object):


    @pytest.mark.function
    @pytest.mark.ARM
    def test_01_check_MEP_notification_ui_on_ARM_machine_C49136455(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_hp_title_show_up(), "MEP notification hp title is not displayed on Windows"
        assert self.fc.fd["audio"].verify_settings_for_this_notification_show_up(), "MEP notification toast settings button is not displayed on Windows"
        assert self.fc.fd["audio"].verify_move_this_notification_to_notification_center_show_up(), "MEP notification close button is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_effects_switch_show_up(), "Audio effects switch is not displayed on MEP notification toast on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_switch_back_button_show_up(), "MEP notification switch back button is not displayed on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_dismiss_button_show_up(), "MEP notification dismiss button is not displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(3)

    
    @pytest.mark.function
    @pytest.mark.ARM
    def test_02_click_close_button_on_mep_notification_toast_C49136458(self):
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_move_this_notification_to_notification_center_show_up(), "MEP notification close button is not displayed on Windows"
        self.fc.fd["audio"].click_move_this_notification_to_notification_center()
        time.sleep(3)
        # check mep notification toast is closed after clicking close button on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up() is False, "MEP notification toast is still displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_03_click_dismiss_button_on_mep_notification_toast_C49136457(self):
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_dismiss_button_show_up(), "MEP notification dismiss button is not displayed on Windows"
        self.fc.fd["audio"].click_mep_notification_dismiss_button()
        time.sleep(3)
        # check mep notification toast is closed after clicking close button on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up() is False, "MEP notification toast is still displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_04_click_switch_back_button_will_go_to_audio_settings_page_C49136456(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(3)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(4)
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_switch_back_button_show_up(), "MEP notification switch back button is not displayed on Windows"
        self.fc.fd["audio"].click_mep_notification_switch_back_button()
        time.sleep(4)
        # check audio settings page is displayed after clicking switch back button on windows
        assert self.fc.fd["audio"].verify_all_sounds_devices_on_windows_show_up(), "All sound devices page is not displayed on Windows"
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_05_uninstall_install_myhp_with_mep_notification_C49136465(self):
        self.fc.uninstall_app()
        time.sleep(5)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        if self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up() is False:
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up() is False, "MEP notification toast is displayed on Windows"
        # check mep notification will pop up again after installing myhp
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        time.sleep(5)
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_hp_title_show_up(), "MEP notification hp title is not displayed on Windows"
        assert self.fc.fd["audio"].verify_settings_for_this_notification_show_up(), "MEP notification toast settings button is not displayed on Windows"
        assert self.fc.fd["audio"].verify_move_this_notification_to_notification_center_show_up(), "MEP notification close button is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_effects_switch_show_up(), "Audio effects switch is not displayed on MEP notification toast on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_switch_back_button_show_up(), "MEP notification switch back button is not displayed on Windows"
        assert self.fc.fd["audio"].verify_mep_notification_dismiss_button_show_up(), "MEP notification dismiss button is not displayed on Windows"


    @pytest.mark.function
    @pytest.mark.ARM
    def test_06_notification_will_not_pop_up_when_turn_off_notification_from_windows_C49136459(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        if self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up() is False:
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_settings_on_MEP_notification_show_up(), "MEP notification settings button is not displayed on Windows"
        # open notification page on windows settings page
        self.fc.fd["audio"].click_settings_on_MEP_notification()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_go_to_notification_settings_button_on_MEP_notification_show_up(), "Go to notification settings button is not displayed"
        self.fc.fd["audio"].click_go_to_notification_settings_button_on_MEP_notification()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_notification_toggle_on_windows_settings_page_show_up(), "Notification settings page is not displayed on windows settings page"
        self.fc.fd["audio"].click_notification_toggle_on_windows_settings_page()
        time.sleep(3)
        # check MEP notification will not pop up after turning off notification toggle on windows settings page
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        if self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up() is False:
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up() is False, "MEP notification toast is displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.open_system_settings_notifications()
        time.sleep(3)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_hp_notification_toggle_on_windows_settings_page_show_up(), "Notification settings page is not displayed on windows settings page"
        if self.fc.fd["audio"].is_hp_notification_toggle_enabled() == "0":
            self.fc.fd["audio"].click_hp_notification_toggle_on_windows_settings_page()
            time.sleep(3)
        assert self.fc.fd["audio"].is_hp_notification_toggle_enabled() == "1", "HP notification toggle is not turned on"
        self.fc.close_windows_settings_panel()
        time.sleep(3)


    @pytest.mark.function
    @pytest.mark.ARM
    def test_07_notification_will_not_pop_up_when_turn_off_notification_from_myhp_C49136460(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        if self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up() is False:
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up(), "MEP notification toast is not displayed on Windows"
        assert self.fc.fd["audio"].verify_settings_on_MEP_notification_show_up(), "MEP notification settings button is not displayed on Windows"
        # open notification page on myhp side
        self.fc.fd["audio"].click_settings_on_MEP_notification()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_turn_off_notification_from_myhp_side_show_up(), "Trun off all notifications for HP button is not displayed"
        self.fc.fd["audio"].click_turn_off_notification_from_myhp_side()
        time.sleep(3)
        # check MEP notification will not pop up after turning off notification toggle on windows settings page
        self.fc.close_windows_settings_panel()
        time.sleep(3)
        self.fc.open_system_settings_sound()
        time.sleep(5)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up() is False:
            assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
            self.fc.fd["audio"].click_input_device_on_windows()
            time.sleep(5)
        # check input mic on windows
        if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
            self.fc.fd["audio"].click_input_mic_on_windows()
            time.sleep(5)
        else:
            for _ in range(3):
                self.fc.close_windows_settings_panel()
                time.sleep(3)
                self.fc.open_system_settings_sound()
                time.sleep(5)
                if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
                    self.fc.fd["audio"].click_on_system_settings_maximize_button()
                    break
                if self.fc.fd["audio"].verify_input_mic_on_windows_show_up():
                    self.fc.fd["audio"].click_input_mic_on_windows()
                    time.sleep(5)
                    break
                else:
                    assert self.fc.fd["audio"].verify_input_device_show_up(), "Input device button is not displayed on Windows"
                    self.fc.fd["audio"].click_input_device_on_windows()
                    time.sleep(5)
                    assert self.fc.fd["audio"].verify_input_mic_on_windows_show_up(), "Input mic is not displayed on Windows"
        assert self.fc.fd["audio"].verify_audio_enhancements_combobox_on_windows_show_up(), "Audio enhancements combobox is not displayed on Windows"
        if self.fc.fd["audio"].verify_mep_option_on_windows_show_up():
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
        if self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up() is False:
            self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
            time.sleep(5)
            self.fc.fd["audio"].click_non_mep_option_on_windows()
            time.sleep(5)
            assert self.fc.fd["audio"].verify_non_mep_option_on_windows_show_up(), "Non-MEP option is not displayed on Windows"
        self.fc.fd["audio"].click_audio_enhancements_combobox_on_windows()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_mep_option_on_windows_show_up(), "MEP options are not displayed on Windows"
        self.fc.fd["audio"].click_mep_option_on_windows()
        time.sleep(3)
        # check mep notification toast pops up after selecting MEP option on windows
        assert self.fc.fd["audio"].verify_mep_notification_windows_toast_show_up() is False, "MEP notification toast is displayed on Windows"
        self.fc.close_windows_settings_panel()
        time.sleep(5)
        self.fc.open_system_settings_notifications()
        time.sleep(3)
        if "Maximize Settings" == self.fc.fd["audio"].verify_system_settings_window_maximize():
            self.fc.fd["audio"].click_on_system_settings_maximize_button()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_hp_notification_toggle_on_windows_settings_page_show_up(), "Notification settings page is not displayed on windows settings page"
        if self.fc.fd["audio"].is_hp_notification_toggle_enabled() == "0":
            self.fc.fd["audio"].click_hp_notification_toggle_on_windows_settings_page()
            time.sleep(3)
        assert self.fc.fd["audio"].is_hp_notification_toggle_enabled() == "1", "HP notification toggle is not turned on"
        self.fc.close_windows_settings_panel()
        time.sleep(3)