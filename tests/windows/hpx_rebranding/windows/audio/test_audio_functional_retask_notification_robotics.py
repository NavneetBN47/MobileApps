import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_3_5mm")
class Test_Suite_Audio(object):
        
    #run in sidon for now due to limited robotics
    @pytest.mark.function
    @pytest.mark.consumer
    def test_01_plugin_3_5mm_headphone_verify_notification_will_pop_up_when_myhp_open_C50737843(self):
        self.vcosmos.remove_3_5_headphone()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        #revert notification toast select box values possibly carried from previous test
        if (self.fc.fd["audio"].get_retask_notification_toast_select_options_line_in()):
            self.fc.fd["audio"].click_retask_notification_combo_box()
            self.fc.fd["audio"].click_retask_notification_toast_select_option_speaker()
            self.fc.fd["audio"].click_retask_notification_toast_ok_button()
        self.vcosmos.remove_3_5_headphone()
    
    @pytest.mark.function
    @pytest.mark.consumer
    def test_02_plugin_3_5mm_headphone_verify_notification_will_pop_up_without_myhp_open_C50737844(self):
        self.vcosmos.remove_3_5_headphone()
        self.fc.close_myHP()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.vcosmos.remove_3_5_headphone()

    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_plugin_3_5mm_headphone_multiple_times_verify_notification_will_pop_up_everytime_C50737846(self):
        self.vcosmos.remove_3_5_headphone()
        self.fc.launch_myHP()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.vcosmos.remove_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.vcosmos.remove_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.vcosmos.remove_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"

    @pytest.mark.function
    @pytest.mark.consumer
    def test_04_plugin_3_5mm_headphone_verify_its_default_option_will_be_headphone_C50737853(self):
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        assert self.fc.fd["audio"].verify_retask_notification_toast_select_options() == "Speaker Out", "Speaker out is not showing"
        self.vcosmos.remove_3_5_headphone()

    @pytest.mark.function
    @pytest.mark.consumer
    def test_05_plugin_3_5mm_headphone_again_verify_it_will_remember_device_options_C50737854(self):
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        assert self.fc.fd["audio"].verify_retask_notification_toast_select_options() == "Speaker Out", "Speaker out is not showing"
        self.fc.fd["audio"].click_retask_notification_combo_box()
        self.fc.fd["audio"].click_retask_notification_toast_select_option_line_in()
        self.fc.fd["audio"].click_retask_notification_toast_ok_button()
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert self.fc.fd["audio"].verify_retask_notification_toast_select_option_line_in() == "Line In","Line In is not selected"
        #reverting changes
        self.fc.fd["audio"].click_retask_notification_combo_box()
        self.fc.fd["audio"].click_retask_notification_toast_select_option_speaker()
        self.fc.fd["audio"].click_retask_notification_toast_ok_button()
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.consumer
    def test_06_check_notification_function_verify_verify_turn_off_all_notification_for_myhp_works_well_C50737850(self):
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.fc.fd["audio"].click_retask_notification_settings_button()
        self.fc.fd["audio"].click_retask_notification_turn_off_notifications()
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.driver.ssh.send_command("start ms-settings:notifications", raise_e=False, timeout=10)
        assert self.fc.fd["audio"].get_windows_setting_myhp_notification_toggle_on_off_status() == "0","Toggle is on for myhp notification"
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        #revert changes
        self.fc.fd["audio"].click_windows_setting_myhp_notification_toggle_on_off_status()
        time.sleep(2)
        assert self.fc.fd["audio"].get_windows_setting_myhp_notification_toggle_on_off_status() == "1","If toggle is not on it will fail test 07"
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        self.vcosmos.remove_3_5_headphone()

    @pytest.mark.function
    @pytest.mark.consumer
    def test_07_check_notification_function_verify_verify_turn_off_all_notification_for_myhp_works_well_C50737851(self):
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.fc.fd["audio"].click_retask_notification_settings_button()
        assert self.fc.fd["audio"].get_retask_notification_turn_off_notifications() == "Turn off all notifications for HP","Turn off all notifications for myHP is not visible"
        assert self.fc.fd["audio"].get_retask_notification_toast_go_to_notification() == "Go to notification settings", "Go to notification setting is not visible"
        self.fc.fd["audio"].click_retask_notification_toast_go_to_notification()
        assert self.fc.fd["audio"].get_windows_setting_myhp_page_notification_toggle_on_off_status() == "1","Toggle is off for myHP notification"
        self.fc.fd["audio"].click_windows_setting_myhp_page_notification_toggle_on_off_status()
        assert self.fc.fd["audio"].get_windows_setting_myhp_page_notification_toggle_on_off_status() == "0","Toggle is on for myHP notification"
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        #revert changes
        self.fc.fd["audio"].click_windows_setting_myhp_page_notification_toggle_on_off_status()
        assert self.fc.fd["audio"].get_windows_setting_myhp_page_notification_toggle_on_off_status() == "1","If toggle is not on it will fail test 08"
        self.fc.close_windows_settings_panel()
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.consumer
    def test_08_turn_off_notification_on_windows_side_directly_verify_notification_will_also_not_pop_up_C50737852(self):
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.driver.ssh.send_command("start ms-settings:notifications", raise_e=False, timeout=10)
        assert self.fc.fd["audio"].get_windows_setting_myhp_notification_toggle_on_off_status() == "1","Toggle is off for myHP notification"
        self.fc.fd["audio"].click_windows_setting_myhp_notification_toggle_on_off_status()
        assert self.fc.fd["audio"].get_windows_setting_myhp_notification_toggle_on_off_status() == "0","Toggle is on for myHP notification"
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        self.fc.close_windows_settings_panel()
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        #revert changes
        self.driver.ssh.send_command("start ms-settings:notifications", raise_e=False, timeout=10)
        assert self.fc.fd["audio"].get_windows_setting_myhp_notification_toggle_on_off_status() == "0","Toggle is on for myHP notification"
        self.fc.fd["audio"].click_windows_setting_myhp_notification_toggle_on_off_status()
        assert self.fc.fd["audio"].get_windows_setting_myhp_notification_toggle_on_off_status() == "1","If toggle is not on it will fail test 09"
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        self.vcosmos.remove_3_5_headphone()
            
    @pytest.mark.function
    @pytest.mark.consumer
    def test_09_check_notification_function_verify_x_button_works_well_C50737849(self):
        self.vcosmos.remove_3_5_headphone()
        self.vcosmos.add_3_5_headphone()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is True, "Retask Notification is not showing"
        self.fc.fd["audio"].click_retask_notification_toast_x_button()
        assert bool(self.fc.fd["audio"].verify_retask_notification_toast_show()) is False, "Retask Notification is showing"
        self.vcosmos.remove_3_5_headphone()
        #delete all the logs created
        self.vcosmos.clean_up_logs()