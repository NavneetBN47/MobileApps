import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Audio_Context_Aware(object):

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_01_check_context_aware_ui_without_OOB_apps_C50895178(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        # navigate to audio card
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # check context aware
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_02_check_OOB_apps_will_show_on_application_list_automatically_C42214055(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.reset_hp_application()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(5)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert self.fc.fd["audio"].verify_for_all_applications_text_show_up(), "for all applications text is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_check_search_function_C42197763(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # add Access app on the application list
        self.fc.fd["audio"].click_add_application_button()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
        assert self.fc.fd["audio"].verify_search_application_frame_show_up(), "search application frame is not displayed"
        assert self.fc.fd["audio"].verify_application_list_on_dialog_show_up(), "application list is not displayed"
        assert self.fc.fd["audio"].verify_cancel_button_on_dialog_show_up(), "cancel button is not show"
        assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
        time.sleep(5)
        self.fc.fd["audio"].search_apps_on_search_frame("Access")
        time.sleep(5)
        self.fc.fd["audio"].click_searched_app_on_search_frame()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_serached_app_is_be_selected(), "access app is not show on the searched application list"
        time.sleep(2)
        self.fc.fd["audio"].click_cancel_button_on_dialog()
        time.sleep(2)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_04_add_apps_on_application_list_C42520793(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # add Access app on the application list
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
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up(), "Audio presets title is not displayed"
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets music button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets music button is be selected"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_05_delete_added_application_C42197760(self):
        self.fc.swipe_window(direction="up", distance=20)
        time.sleep(4)
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # add Access app on the application list
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
            if self.fc.fd["audio"].verify_access_app_show_on_application_list() is False:
                self.fc.reset_hp_application()
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_device_card()
                time.sleep(3)
                assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
                self.fc.fd["devices_details_pc_mfe"].click_audio_card()
                time.sleep(2)
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
        # delete Access app on the application list
        self.fc.fd["audio"].click_access_app_on_application_list()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_delete_button_show_up(), "Delete button is not displayed"
        self.fc.fd["audio"].click_delete_button()
        time.sleep(4)
        assert bool(self.fc.fd["audio"].verify_delete_profile_txt_on_dialog_show_up()) is True, "Delete page header is not show"
        assert bool(self.fc.fd["audio"].verify_continue_button_on_delete_app_dialog_show_up()) is True, "Delete page description is not show"
        self.fc.fd["audio"].click_continue_button_on_delete_app_dialog()
        time.sleep(4)
        assert bool(self.fc.fd["audio"].verify_access_app_show_on_application_list()) is False, "Access app is still show on application list"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_06_check_more_apps_arrow_show_up_with_11_apps_show_on_application_list_C42320341(self):
        self.fc.reset_hp_application()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # add more apps on the application list
        application_list = ["Disney+", "爱奇艺", "腾讯", "Access", "Paint", "Camera", "Calculator", "Clock", "Microsoft Store", "Photos", "Settings"]
        for i in range(len(application_list)):
            self.fc.fd["audio"].click_add_application_button()
            time.sleep(2)
            assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
            assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
            self.fc.fd["audio"].search_apps_on_search_frame(application_list[i])
            time.sleep(2)
            self.fc.fd["audio"].click_searched_app_on_search_frame()
            time.sleep(3)
            self.fc.fd["audio"].click_continue_button_on_dialog()
            time.sleep(4)
        # check arrow next on application list
        assert self.fc.fd["audio"].verify_arrow_next_on_application_list() is True, "Arrow is not show up"
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
    
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_07_check_arrow_can_work_well_after_11_apps_added_C42197757(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # Add more apps on the application list
        if self.fc.fd["audio"].verify_arrow_next_on_application_list() is False:
            application_list = ["Disney+", "爱奇艺", "腾讯", "Access", "Paint", "Camera", "Calculator", "Clock", "Microsoft Store", "Photos", "Settings"]
            for i in range(len(application_list)):
                self.fc.fd["audio"].click_add_application_button()
                time.sleep(2)
                assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
                assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
                self.fc.fd["audio"].search_apps_on_search_frame(application_list[i])
                time.sleep(2)
                self.fc.fd["audio"].click_searched_app_on_search_frame()
                time.sleep(3)
                self.fc.fd["audio"].click_continue_button_on_dialog()
                time.sleep(4)
        self.fc.fd["audio"].click_arrow_next_on_application_list()
        time.sleep(2)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_08_check_added_app_cannot_be_added_again_C42197758(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.reset_hp_application()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
            self.fc.fd["audio"].click_global_icon()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # add Access app on the application list
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
            if self.fc.fd["audio"].verify_access_app_show_on_application_list() is False:
                self.fc.reset_hp_application()
                self.fc.fd["devicesMFE"].click_device_card()
                time.sleep(3)
                self.fc.fd["devices_details_pc_mfe"].click_audio_card()
                time.sleep(2)
                self.fc.fd["audio"].click_global_icon()
                time.sleep(2)
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


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_09_check_Presets_will_change_to_Movie_automatically_when_using_IMAX_apps_C42197769(self):
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        # check IMAX apps if show on application list
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
            if self.fc.fd["audio"].verify_tencent_app_show_on_application_list() is False:
                self.fc.fd["audio"].click_add_application_button()
                time.sleep(2)
                assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
                assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
                self.fc.fd["audio"].search_apps_on_search_frame("腾讯")
                time.sleep(2)
                self.fc.fd["audio"].click_searched_app_on_search_frame()
                time.sleep(3)
                self.fc.fd["audio"].click_continue_button_on_dialog()
                time.sleep(4)
                if self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list() is False:
                    self.fc.fd["audio"].click_add_application_button()
                    time.sleep(2)
                    assert self.fc.fd["audio"].verify_add_application_txt_on_dialog_show_up(), "add application txt on dialog is not displayed"
                    assert self.fc.fd["audio"].verify_continue_button_on_dialog_show_up(), "continue button is not show"
                    self.fc.fd["audio"].search_apps_on_search_frame("爱奇艺")
                    time.sleep(2)
                    self.fc.fd["audio"].click_searched_app_on_search_frame()
                    time.sleep(3)
                    self.fc.fd["audio"].click_continue_button_on_dialog()
                    time.sleep(4)
        assert bool(self.fc.fd["audio"].verify_aiqiyi_app_show_on_application_list()) is True, "Aiqiyi app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_tencent_app_show_on_application_list()) is True, "Tencent app is not show on application list"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        # click disney app on the application list
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        # click aiqiyi app on the application list
        self.fc.fd["audio"].click_aiqiyi_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        # click tencent app on the application list
        self.fc.fd["audio"].click_tencent_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_10_app_settings_will_be_recover_after_click_global_icon_C42197777(self):
        if self.fc.fd["audio"].verify_global_icon_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        assert self.fc.fd["audio"].verify_add_application_button_show_up(), "add application button is not displayed"
        assert bool(self.fc.fd["audio"].verify_disney_app_show_on_application_list()) is True, "Disney app is not show on application list"
        # check disney function
        self.fc.fd["audio"].click_disney_app_on_application_list()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_movie_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_movie_button_status()) is True, "Audio presets movie button is be selected"
        self.fc.swipe_window(direction="up", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_global_icon_show_up(), "global icon is not displayed"
        self.fc.fd["audio"].click_global_icon()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=8)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_audio_presets_title_show_up()
        assert self.fc.fd["audio"].verify_audio_presets_music_button_show_up(), "Audio presets movie button is not displayed"
        assert bool(self.fc.fd["audio"].get_presets_music_button_status()) is True, "Audio presets movie button is be selected"