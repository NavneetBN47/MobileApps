import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Display_Context_Aware(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_oob_default_apps_C51570659(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)
        # verify disney plus app is not present
        if self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page() is False: #Ensure Application is not present
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
        # verify tencent app is not present
        if self.fc.fd["display_control"].verify_tencent_app_ltwo_page() is False: #Ensure Application is not present
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
        # verify iqiyi app  is not present
        if self.fc.fd["display_control"].verify_iqiyi_app_ltwo_page() is False: #Ensure Application is not present          
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
        # verify Disney+ app\tencent\iqiyi are present
        assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page(), "Disney+ app is not present in the application list"
        assert self.fc.fd["display_control"].verify_tencent_app_ltwo_page(), "Tencent app is not present in the application list"
        assert self.fc.fd["display_control"].verify_iqiyi_app_ltwo_page(), "Iqiyi app is not present in the application list"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_delete_button_enable_and_disable_state_C51570658(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)
        # verify no delete profile button show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == False, "Delete profile button is present"
        time.sleep(1)
        # add Access app on the application list and click continue button
        # click on custom settings button
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        time.sleep(3)
        # verify add application text show in app list
        assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
        # search Access app on the search frame
        self.fc.fd["display_control"].search_apps_on_search_frame("Access")
        time.sleep(2)
        # click search app on the search frame
        self.fc.fd["display_control"].click_searched_app_on_search_frame()
        time.sleep(2)
        # click continue button
        self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
        time.sleep(4)
        # verify Access app is added in the application list
        assert bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()) is True, "Access app is not added in the application list"
        time.sleep(2)
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_delete_oob_app_C51570661(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)
        # verify disney plus app is not present
        if self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page() is False: #Ensure Application is not present
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
        # verify tencent app is not present
        if self.fc.fd["display_control"].verify_tencent_app_ltwo_page() is False: #Ensure Application is not present
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
        # verify iqiyi app  is not present
        if self.fc.fd["display_control"].verify_iqiyi_app_ltwo_page() is False: #Ensure Application is not present          
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
        # verify Disney+ app\tencent\iqiyi are present
        assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page(), "Disney+ app is not present in the application list"
        assert self.fc.fd["display_control"].verify_tencent_app_ltwo_page(), "Tencent app is not present in the application list"
        assert self.fc.fd["display_control"].verify_iqiyi_app_ltwo_page(), "Iqiyi app is not present in the application list"

        # Select any OOB app in the list want to delete
        # delete Disney+ app
        if self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page():
            self.fc.fd["display_control"].click_disney_plus_app_ltwo_page()
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # verify delete profile dialog pop up and delete profile text show 
        assert self.fc.fd["display_control"].verify_delete_profil_dialog_delete_profile_text_show(), "Delete profile text is not present"
        time.sleep(1)
        # verify delete profile dialog description text show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_description_text() == "Are you sure you want to remove this app configuration? This application will be removed from all modules.", "Delete profile dialog description text is not present"
        time.sleep(1)
        # vefify delete profile dialog cancel button show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_cancel_button_show(), "Delete profile dialog cancel button is not present"
        time.sleep(1)
        # verify delete profile dialog continue button show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_continue_button_show(), "Delete profile dialog continue button is not present"
        time.sleep(1)
        # verify do not show again xbox show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_do_not_show_again_checkbox_show(), "Delete profile dialog do not show again checkbox is not present"
        time.sleep(1)
        # click delete profile dialog continue button
        self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        time.sleep(2)
        # verify disply plus app will disappear
        assert bool(self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page()) is False, "Disney+ app is still present in the application list"
        time.sleep(2)
        # add disney+ apps on the application list
        application_list = ["Disney+"]
        for i in range(len(application_list)):
            self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
            time.sleep(3)
            assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
            self.fc.fd["display_control"].search_apps_on_search_frame(application_list[i])
            time.sleep(2)
            self.fc.fd["display_control"].click_searched_app_on_search_frame()
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            time.sleep(4)

        # verify all apps are added in the application list
        app_context = ["disney"]
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is True, f"{app} app is not added in the application list"
            time.sleep(2)
        
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_delete_app_without_delete_profile_page_C53045345(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)
        
        # add more apps on the application list
        application_list = ["Camera", "Command Prompt"]
        for i in range(len(application_list)):
            self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
            time.sleep(3)
            assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
            self.fc.fd["display_control"].search_apps_on_search_frame(application_list[i])
            time.sleep(2)
            self.fc.fd["display_control"].click_searched_app_on_search_frame()
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            time.sleep(4)
 
        # verify all apps are added in the application list
        app_context = ["camera", "command_prompt"]
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is True, f"{app} app is not added in the application list"
            time.sleep(2)
    
        # Select any app in the list want to delete
        # delete camera app
        if self.fc.fd["display_control"].verify_camera_app_ltwo_page():
            self.fc.fd["display_control"].click_camera_app_ltwo_page()
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # verify delete profile dialog pop up and delete profile text show 
        assert self.fc.fd["display_control"].verify_delete_profil_dialog_delete_profile_text_show(), "Delete profile text is not present"
        time.sleep(1)
        # verify delete profile dialog description text show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_description_text() == "Are you sure you want to remove this app configuration? This application will be removed from all modules.", "Delete profile dialog description text is not present"
        time.sleep(1)
        # verify delete profile dialog continue button show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_continue_button_show(), "Delete profile dialog continue button is not present"
        time.sleep(1)
        # verify do not show again xbox show
        assert self.fc.fd["display_control"].verify_delete_profile_dialog_do_not_show_again_checkbox_show(), "Delete profile dialog do not show again checkbox is not present"
        time.sleep(1)
        # click do not show again checkbox
        self.fc.fd["display_control"].click_delete_profile_dialog_do_not_show_again_checkbox()
        time.sleep(1)
        # verify do not show again checkbox is checked
        assert self.fc.fd["display_control"].get_delete_profile_dialog_do_not_show_again_checkbox_checked() == "1", "Delete profile dialog do not show again checkbox is not checked"
        time.sleep(1)
        # click delete profile dialog continue button
        self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        time.sleep(2)
        # verify camera app disappear
        assert bool(self.fc.fd["display_control"].verify_camera_app_ltwo_page()) is False, "Camera app is still present in the application list"
        time.sleep(2)
        
        # delete command_prompt app
        if self.fc.fd["display_control"].verify_command_prompt_app_ltwo_page():
            self.fc.fd["display_control"].click_command_prompt_app_ltwo_page()
            time.sleep(2)   
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # verify command_prompt app disappear
        assert bool(self.fc.fd["display_control"].verify_command_prompt_app_ltwo_page()) is False, "Command Prompt app is still present in the application list"
        time.sleep(2)
        
    @pytest.mark.ota
    @pytest.mark.function
    def test_05_application_setting_app_delete_C51570665(self):
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)
        
        # add more apps on the application list
        application_list = ["Media player", "Magnify", "Paint", "News"] 
        for i in range(len(application_list)):
            self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
            time.sleep(3)
            assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
            self.fc.fd["display_control"].search_apps_on_search_frame(application_list[i])
            time.sleep(2)
            self.fc.fd["display_control"].click_searched_app_on_search_frame()
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            time.sleep(4)
 
        # verify all apps are added in the application list
        app_context = ["media_player", "magnify","paint","news"]
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is True, f"{app} app is not added in the application list"
            time.sleep(2)
    
        # Select any app in the list want to delete
        # delete media_player app
        if self.fc.fd["display_control"].verify_media_player_app_ltwo_page():
            self.fc.fd["display_control"].click_media_player_app_ltwo_page()
            time.sleep(2)
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # click delete profile dialog continue button
        self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        time.sleep(2)
        # verify camera app disappear
        assert bool(self.fc.fd["display_control"].verify_media_player_app_ltwo_page()) is False, "Camera app is still present in the application list"
        time.sleep(2)

        # delete magnify app
        if self.fc.fd["display_control"].verify_magnify_app_ltwo_page():
            self.fc.fd["display_control"].click_magnify_app_ltwo_page()
            time.sleep(2)   
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # click delete profile dialog continue button
        self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        time.sleep(2)   
        # verify magnify app disappear
        assert bool(self.fc.fd["display_control"].verify_magnify_app_ltwo_page()) is False, "Magnify app is still present in the application list"
        time.sleep(2)

        # delete paint app
        if self.fc.fd["display_control"].verify_paint_app_ltwo_page():
            self.fc.fd["display_control"].click_paint_app_ltwo_page()
            time.sleep(2)   
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # click delete profile dialog continue button
        self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        time.sleep(2)
        # verify paint app disappear
        assert bool(self.fc.fd["display_control"].verify_paint_app_ltwo_page()) is False, "Paint app is still present in the application list"
        time.sleep(2)   

        # delete news app
        if self.fc.fd["display_control"].verify_news_app_ltwo_page():
            self.fc.fd["display_control"].click_news_app_ltwo_page()
            time.sleep(2)       
        # verify delete profile button will show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == True, "Delete profile button is not present"
        time.sleep(1)
        # click delete profile button
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        time.sleep(2)
        # click delete profile dialog continue button
        self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        time.sleep(2)
        # verify news app disappear
        assert bool(self.fc.fd["display_control"].verify_news_app_ltwo_page()) is False, "News app is still present in the application list"
        time.sleep(2)

        # restart myHP to verify all apps are deleted
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)
        # verify all apps are deleted
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is False, f"{app} app is still present in the application list"
            time.sleep(2)
    

    @pytest.mark.function
    def test_06_navigate_to_each_button_use_tab_C51570679(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)

        self.fc.fd["display_control"].press_tab("display_control_all_application_button_ltwo_page")
        time.sleep(2)
        assert self.fc.fd["display_control"].is_focus_on_element("display_control_all_application_button_ltwo_page"), "Display control all application button is not focused"
        time.sleep(2)
        self.fc.fd["display_control"].press_tab("display_control_add_application_button_ltwo_page")
        time.sleep(2)
        assert self.fc.fd["display_control"].is_focus_on_element("display_control_add_application_button_ltwo_page"), "Display control add application button is not focused"
    

    @pytest.mark.function
    def test_07_press_alt_f4_from_keyboard_C51570688(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        assert self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page(), "All Applications Button is not present."
        time.sleep(2)
        self.fc.fd["display_control"].press_alt_f4_to_close_app()
        time.sleep(2)
        assert self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page() is False, "All Applications Button displayed after alt+f4"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_08_uninstall_application_C51570666(self):
        time.sleep(2)
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): 
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)

        if self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page() is False: 
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
            time.sleep(2)
            if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
                self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
            assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page(), "Disney+ app is not present in the application list"


        time.sleep(2)
        self.fc.uninstall_disney_plus_app()

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): 
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page(), "Disney+ app is not present in the application list"
    


    @pytest.mark.ota
    @pytest.mark.function
    def test_09_adding_application_through_tab_C52928009(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)

        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."

        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"

        if bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()):
            time.sleep(2)
            self.fc.fd["audio"].click_access_app_on_application_list()
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_delete_profile_button()
            time.sleep(2)
            self.fc.fd["display_control"].click_delete_profile_dialog_continue_button()
        
        time.sleep(2)
        self.fc.fd["display_control"].press_tab("display_control_add_application_button_ltwo_page")
        time.sleep(2)
        self.fc.fd["display_control"].press_enter("display_control_add_application_button_ltwo_page")
        time.sleep(3)
        self.fc.fd["audio"].press_tab("search_access_on_application_list")
        time.sleep(2)
        self.fc.fd["audio"].press_enter("search_access_on_application_list")
        time.sleep(2)
        self.fc.fd["display_control"].press_tab("display_control_add_app_continue_button_ltwo_page")
        time.sleep(2)
        self.fc.fd["display_control"].press_enter("display_control_add_app_continue_button_ltwo_page")
        time.sleep(2)
        assert bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()) is True, "Access app is not added in the application list"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_10_delete_application_through_tab_C52928452(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)

        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."

        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"


        if bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()) is False:
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
            time.sleep(2)    
            self.fc.fd["display_control"].search_apps_on_search_frame("Access")
            time.sleep(2)
            self.fc.fd["display_control"].click_searched_app_on_search_frame()
            time.sleep(2)
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()


        time.sleep(2)
        self.fc.fd["audio"].press_tab("access_on_application_list")
        time.sleep(2)
        self.fc.fd["audio"].press_enter("access_on_application_list")
        time.sleep(2)
        self.fc.fd["display_control"].press_tab("display_control_delete_profile_button")
        time.sleep(2)
        self.fc.fd["display_control"].press_enter("display_control_delete_profile_button")
        time.sleep(2)
        self.fc.fd["display_control"].press_tab("delete_profile_dialog_continue_button")
        time.sleep(2)
        self.fc.fd["display_control"].press_enter("delete_profile_dialog_continue_button")
        time.sleep(2)
        assert bool(self.fc.fd["display_control"].verify_access_app_show_on_application_list()) is False, "Access app is not removed from the application list"


    @pytest.mark.ota
    @pytest.mark.function
    def test_11_uninstall_oob_apps_and_reset_hpx_C53046320(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): 
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        time.sleep(2)

        if self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page() is False: 
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(10)
            self.fc.kill_msstore_process()
            time.sleep(8)
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
            time.sleep(2)
            if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page():
                self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
            assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page(), "Disney+ app is not present in the application list"


        time.sleep(2)
        self.fc.uninstall_disney_plus_app()

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): 
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page(), "Disney+ app is not present in the application list"

        time.sleep(2)
        self.fc.reset_app()

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(2)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): 
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        assert self.fc.fd["display_control"].verify_disney_plus_app_ltwo_page() is False, "Disney+ app is present in the application list after reset app"
