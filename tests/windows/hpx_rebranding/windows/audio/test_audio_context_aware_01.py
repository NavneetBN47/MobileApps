import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Audio_Context_Aware_01(object):

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_IMAX_app_new_settings_can_be_remembered_C42197773(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check context aware default settings
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        # select disney app and check its default settings
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # assign new settings for IMAX app
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        # recover to preset default settings
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        # check the settings for IMAX app again
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        # restore to default settings by clicking restore defaults button
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=18)
        time.sleep(2)
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_non_IMAX_app_new_settings_can_be_remembered_C42197774(self):
        self.fc.swipe_window(direction="up", distance=18)
        time.sleep(2)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        # check access app if will show on application list
        if self.fc.fd["audio"].verify_access_app_show_on_application_list() is False:
            self.fc.fd["audio"].click_add_application_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
            assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show on pop-up dialog page"
            self.fc.fd["audio"].search_apps_on_search_frame("Access")
            time.sleep(2)
            self.fc.fd["audio"].click_searched_app_on_search_frame()
            time.sleep(3)
            self.fc.fd["audio"].click_continue_button_on_dialog()
            time.sleep(4)
        # check context aware default settings and assign new settings for non IMAX app
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # recover to preset default settings by clicking global icon
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        # check the settings for non IMAX app again
        self.fc.fd["audio"].click_access_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # restore to default settings by clicking restore defaults button
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=18)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_apps_settings_can_be_remembered_C42197775(self):
        self.fc.swipe_window(direction="up", distance=18)
        time.sleep(2)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        # Set new settings for IMAX app
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        # Set new settings for non IMAX app
        if self.fc.fd["audio"].verify_access_app_show_on_application_list() is False:
            self.fc.fd["audio"].click_add_application_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
            assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
            self.fc.fd["audio"].search_apps_on_search_frame("Access")
            time.sleep(2)
            self.fc.fd["audio"].click_searched_app_on_search_frame()
            time.sleep(3)
            self.fc.fd["audio"].click_continue_button_on_dialog()
            time.sleep(4)
            assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        # Verify the settings for IMAX app
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        # Verify the settings for non IMAX app
        self.fc.fd["audio"].click_access_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # verify the settings for IMAX apps
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_presets_option_will_change_to_music_when_using_non_IMAX_app_C42197766(self):
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        # change Presets default option to a new option
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        # Add access app on the application list
        if self.fc.fd["audio"].verify_access_app_show_on_application_list() is False:
            self.fc.fd["audio"].click_add_application_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
            assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
            self.fc.fd["audio"].search_apps_on_search_frame("Access")
            time.sleep(2)
            self.fc.fd["audio"].click_searched_app_on_search_frame()
            time.sleep(3)
            self.fc.fd["audio"].click_continue_button_on_dialog()
            time.sleep(4)
        # Check context aware default settings for access app
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        # restore to default settings by clicking restore defaults button
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=18)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_presets_option_will_not_change_when_app_not_on_application_list_C42197771(self):
        self.fc.swipe_window(direction="up", distance=18)
        time.sleep(2)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        # Check the status of presets button when launch Disney app
        self.fc.fd["audio"].launch_windows_app("Disney")
        time.sleep(4)
        self.fc.fd["audio"].click_myhp_on_taskbar()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # Check the status of presets button when launch calculator app which is not on the application list
        self.fc.fd["audio"].launch_windows_app("Calculator")
        time.sleep(2)
        self.fc.fd["audio"].click_myhp_on_taskbar()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.kill_calculator_app_process()
        time.sleep(2)
        self.fc.kill_disney_video_process()
        time.sleep(2)
   
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_06_check_Presets_option_when_launch_IMAX_apps_C52927238(self):
        self.fc.kill_calculator_app_process()
        time.sleep(2)
        self.fc.kill_disney_video_process()
        time.sleep(2)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(5)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        # Check the status of presets button when launch Disney app
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].launch_windows_app("Disney")
        time.sleep(4)
        self.fc.fd["audio"].click_myhp_on_taskbar()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.kill_disney_video_process()
        time.sleep(2)
        # Check the status of presets button when launch aiqyi app
        self.fc.fd["audio"].launch_windows_app("爱奇艺")
        time.sleep(4)
        self.fc.fd["audio"].click_myhp_on_taskbar()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.fd["audio"].click_audio_presets_music_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.kill_iqiyi_video_process()
        time.sleep(2)
        # Check the status of presets button when launch Tencent app
        self.fc.fd["audio"].launch_windows_app("腾讯")
        time.sleep(5)
        self.fc.fd["audio"].click_myhp_on_taskbar()
        time.sleep(5)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.kill_tencent_video_process()
        time.sleep(2)
        # restore to default settings by clicking restore defaults button
        self.fc.swipe_window(direction="up", distance=18)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=18)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)

    
    @pytest.mark.consumer
    @pytest.mark.function
    def test_07_check_Presets_option_when_launch_non_IMAX_apps_C52927381(self):
        self.fc.kill_disney_video_process()
        time.sleep(2)
        self.fc.kill_iqiyi_video_process()
        time.sleep(2)
        self.fc.kill_tencent_video_process()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=18)
        time.sleep(2)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # assign new presets option
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        # add calculator app on the application list
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        if self.fc.fd["audio"].verify_calculator_app_show_on_application_list() is False:
            self.fc.fd["audio"].click_add_application_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
            assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
            self.fc.fd["audio"].search_apps_on_search_frame("calculator")
            time.sleep(2)
            self.fc.fd["audio"].click_searched_app_on_search_frame()
            time.sleep(3)
            self.fc.fd["audio"].click_continue_button_on_dialog()
            time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_uninstalled_app_will_show_on_application_list_when_relaunch_hpx_C42197761(self):
        self.fc.reset_hp_application()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        # check audio standalone app is uninstalled
        self.fc.uninstall_disney_plus_app()
        time.sleep(10)
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        # check audio standalone app will still show up after relaunching myHP
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"    


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_uninstalled_app_will_not_show_on_application_list_C42197762(self):
        # add hp audio standalone app and check it on myhp
        self.fc.close_myHP()
        time.sleep(2)
        self.fc.uninstall_disney_plus_app()
        time.sleep(10)
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is False, "Disney app is show on application list"