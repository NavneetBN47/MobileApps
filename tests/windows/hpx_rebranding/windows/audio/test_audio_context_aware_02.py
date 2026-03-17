import time
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Audio_Context_Aware_02(object):


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_app_settings_error_ui_C42320302(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"

        # add hp privacy settings app
        self.fc.fd["audio"].click_add_application_button()
        time.sleep(2)
        self.fc.fd["audio"].search_apps_on_search_frame("privacy")
        time.sleep(2)
        self.fc.fd["audio"].click_searched_app_on_search_frame()
        time.sleep(3)
        self.fc.fd["audio"].click_continue_button_on_dialog()
        time.sleep(4)
        assert bool(self.fc.fd["audio"].verify_privacy_app_show_on_application_list()) is True, "hp privacy app is not show on application list"

        # uninstall hp privacy settings app to make the app settings show error
        self.fc.uninstall_hp_privacy_settings_app()
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_error_icon_on_application_list(), "error is not displayed"
        time.sleep(2)
        self.fc.close_myHP()
        time.sleep(2)
        self.fc.install_hp_privacy_settings_app()
        time.sleep(5)

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.integration
    def test_02_check_added_apps_name_will_show_correctly_on_the_application_list_C42520861(self):
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"

        # add access app
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
        else:
            self.fc.fd["audio"].click_access_app_on_application_list()
            time.sleep(4)
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is True, "Access app is not show on application list"
        access_name = self.fc.fd["audio"].get_access_name_on_application_list()
        assert access_name == "Access", "Access app name is not correct"

        # check for all applications text
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        for_all_applications_text = self.fc.fd["audio"].get_for_all_application_name_on_application_list()
        assert for_all_applications_text == "For all applications", "for all applications text is not correct"

        # check disney app
        if self.fc.fd["audio"].verify_disney_app_show_on_application_list() is False:
            self.fc.fd["audio"].click_add_application_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
            assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
            self.fc.fd["audio"].search_apps_on_search_frame("Disney")
            time.sleep(2)
            self.fc.fd["audio"].click_searched_app_on_search_frame()
            time.sleep(3)
            self.fc.fd["audio"].click_continue_button_on_dialog()
            time.sleep(4)
        else:
            self.fc.fd["audio"].click_disney_app_on_application_list()
            time.sleep(4)
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        disney_name = self.fc.fd["audio"].get_disney_name_on_application_list()
        assert disney_name == "Disney+", "Disney app name is not correct"

    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_restore_defaults_work_well_with_selected_application_C42197785(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        time.sleep(1)
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        # Set new settings for IMAX app
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        self.fc.fd["audio"].click_audio_presets_voice_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_voice_button_status()) is True, "Audio presets voice button is not be selected"
        self.fc.swipe_window(direction="up", distance=13)
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
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.fd["audio"].click_audio_presets_movie_button()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"
        # click restore defaults button
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is not be selected"
        self.fc.swipe_window(direction="up", distance=13)
        time.sleep(2)
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=13)
        time.sleep(2)
        # click restore defaults button
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(4)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is not be selected"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_check_context_aware_will_show_on_the_top_C42197755(self):
        self.fc.restart_myHP()
        time.sleep(3)
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


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.integration
    def test_05_check_OOB_apps_show_on_application_list_automatically_C42197764(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
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

        # install disney app\腾讯视频\爱奇艺 from ms store    
         # verify disney plus app is not present
        if self.fc.fd["audio"].verify_disney_app_show_on_application_list() is False: #Ensure Application is not present
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.change_system_region_to_united_states()
            time.sleep(15)
            self.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(3)
        # verify tencent app is not present
        if self.fc.fd["audio"].verify_tencent_app_show_on_application_list() is False: #Ensure Application is not present
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.change_system_region_to_china()
            time.sleep(15)
            self.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(3)
        # verify iqiyi app  is not present
        if self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list() is False: #Ensure Application is not present          
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.change_system_region_to_china()
            time.sleep(15)
            self.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(3)
        
        # restart myHP
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(3)

        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        self.fc.change_system_region_to_united_states()
        time.sleep(5)

    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_settings_back_to_default_settings_after_relaunch_myhp_C42197776(self):
        if self.fc.change_system_region_to_united_states() is False:
            self.fc.change_system_region_to_united_states()
            time.sleep(15)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
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
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is be selected"
        # restart myHP
        self.fc.restart_myHP()
        time.sleep(3)
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
        assert bool(self.fc.fd["audio"].is_for_all_application_button_selected()) is True, "Foa all application button is not selected"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is be selected"


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.integration
    def test_07_check_context_aware_will_show_all_pc_C42197754(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
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


    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_08_show_app_name_when_mouse_hover_on_app_C60639407(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
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
        # make sure disney app is present
        if self.fc.fd["audio"].verify_disney_app_show_on_application_list() is False: 
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.change_system_region_to_united_states()
            time.sleep(15)
            self.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(3)
        self.fc.fd["audio"].click_disney_app_on_application_list()
        assert self.fc.fd["audio"].verify_tooltips_for_app_on_the_application_list_show_up(), "tooltips for app on the application list is not displayed"