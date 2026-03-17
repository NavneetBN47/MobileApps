import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Display_Context_Aware(object):
        
    @pytest.mark.ota
    def test_01_app_settings_add_application_ui_C51570672(self):
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        if self.fc.fd["display_control"].verify_display_control_support_popup() == True:
            self.fc.fd["display_control"].click_display_control_ok_support_popup_button()

        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)

        assert self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page(), "All Applications Button is not present."
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()

        assert self.fc.fd["display_control"].verify_display_control_add_app_search_bar_ltwo_page(),"Search Application is not present."
        assert self.fc.fd["display_control"].verify_display_control_application_list_ltwo_page(),"Application List is not present."
        assert self.fc.fd["display_control"].verify_display_control_continue_button_ltwo_page(),"Continue button is not present."
        assert self.fc.fd["display_control"].verify_display_control_cancel_button_ltwo_page(),"Cancel button is not present."

        self.fc.fd["display_control"].click_display_control_cancel_button_ltwo_page() 
    
    @pytest.mark.ota
    def test_02_app_settings_ui_display_control_C51570671(self):
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
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()

        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"No Applications In Carasouel."
        self.fc.fd["display_control"].click_display_control_disney_plus_app()

        assert self.fc.fd["display_control"].verify_display_control_app_settings_header(),"Header is not present."
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(),"All Apps Button is not present."
        assert self.fc.fd["display_control"].verify_display_control_app_settings_app_name, "App Name is not present."
        assert self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page(), "Add App Button is not present."
        assert self.fc.fd["display_control"].verify_display_control_delete_profile_button(), "Delete Profile Button is not present." 

    @pytest.mark.ota
    def test_03_app_setting_delete_profile_ui_C51570673(self):
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
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()

        assert self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"No Applications In Carasouel."
        self.fc.fd["display_control"].click_display_control_disney_plus_app()

        assert self.fc.fd["display_control"].verify_display_control_delete_profile_button(),"Delete profile is not present."
        self.fc.fd["display_control"].click_display_control_delete_profile_button()
        assert self.fc.fd["display_control"].verify_display_control_cancel_button_ltwo_page(),"Cancel Button is not present."
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_continue_btn()) is True,"Continue Button is not present."
        assert self.fc.fd["display_control"].verify_display_control_delete_profile_checkbox_ltwo_page(),"'Do Not Show Again' Check Box is not present."
        
        self.fc.fd["display_control"].click_display_control_cancel_button_ltwo_page()

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_no_apps_and_default_state_C51570650(self):
        self.fc.uninstall_disney_plus_app()
        time.sleep(2)
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        if self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(): #Ensure Application is on the correct page
            self.fc.fd["display_control"].click_display_control_all_application_button_ltwo_page()
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify no delete profile button show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == False, "Delete profile button is present"
        time.sleep(2)
        # verify context aware text
        assert self.fc.fd["display_control"].get_display_control_for_all_applications_text() == "For all applications", "For all applications text is not matching"
        time.sleep(2)        
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
        time.sleep(2)
        # verify all application button is shown
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(), "All application button is not selected"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_first_launch_context_aware_list_C51570656(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify all application button is be selected
        assert self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page(), "All application button is not selected"
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
        # verify no delete profile button show
        assert bool(self.fc.fd["display_control"].verify_display_control_delete_profile_button()) == False, "Delete profile button is present"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_06_adding_application_C52986236(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
        
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

        # add Access app on the application list and click cancel button
        # click on custom settings button
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        time.sleep(3)
        # verify add application text show in app list
        assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
        # search Access app on the search frame
        self.fc.fd["display_control"].search_apps_on_search_frame("Calculator")
        time.sleep(2)
        # click search app on the search frame
        self.fc.fd["display_control"].click_searched_app_on_search_frame()
        time.sleep(2)
        # click cancel button
        self.fc.fd["display_control"].click_cancel_button_on_dialog()
        time.sleep(4)
        # verify calculator app is not added in the application list
        assert bool(self.fc.fd["display_control"].verify_calculator_app_show_on_application_list()) is False, "Calculator app is added in the application list"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_07_select_and_add_multiple_application_C51570655(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
        
        # add more apps on the application list
        application_list = ["Camera", "Command Prompt", "Excel", "Media Player", "Microsoft Edge", "Narrator", "Task Manager", "Clock", "Microsoft Store", "Photos", "settings", "Word",]
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

        # check arrow next on application list
        assert self.fc.fd["audio"].verify_arrow_next_on_application_list() is True, "Arrow is not show up"
        time.sleep(2)
        
        # verify all apps are added in the application list
        app_context = ["camera", "command_prompt", "excel", "media_player", "microsoft_edge", "narrator", "task_manager", "clock", "microsoft_store", "photos", "settings", "word"]
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is True, f"{app} app is not added in the application list"
            time.sleep(2)
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_08_verify_application_name_C51570657(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
  
        # verify all apps are added in the application list
        app_context = ["camera", "command_prompt", "excel", "media_player", "microsoft_edge", "narrator", "task_manager", "clock", "microsoft_store", "photos", "settings", "word"]
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is True, f"{app} app is not added in the application list"
            time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_09_adding_multiple_application_C51570654(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
  
        # add more apps on the application list
        application_list = ["Get Help", "Get Started", "News", "Weather", "Copilot"]
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
        app_context = ["get_help", "get_started", "news", "weather", "copilot"]
        for app in app_context:
            assert bool(self.fc.fd["display_control"].verify_all_app_show_on_application_list(app)) is True, f"{app} app is not added in the application list"
            time.sleep(2)   

        
    @pytest.mark.ota
    @pytest.mark.function
    def test_10_application_select_and_unselect_in_add_application_list_C53033386(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(),"Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(3)
        # verify display text show
        assert self.fc.fd["display_control"].verify_display_control_text_ltwo_page() == "Display","Display Text is not matching."
        # verify custom settings button show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_application_button_ltwo_page()) == True, "Custom settings button is not present"
  
        # verify continue button will not show
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
        time.sleep(2)    
        self.fc.fd["display_control"].search_apps_on_search_frame("Access")
        time.sleep(2)
        self.fc.fd["display_control"].click_searched_app_on_search_frame()
        time.sleep(2)
        self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
        # verify continue button will not show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_app_continue_button_ltwo_page()) == False, "Continue button is not clickable"
        time.sleep(2)

        # verify continue still will show
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_display_control_add_application_text_show_in_app_list(), "Add application text is not present in the application list"
        time.sleep(2)    
        self.fc.fd["display_control"].search_apps_on_search_frame("Access")
        time.sleep(2)
        self.fc.fd["display_control"].click_searched_app_on_search_frame()
        time.sleep(2)
        self.fc.fd["display_control"].click_searched_app_on_search_frame()
        time.sleep(2)
        # verify continue button still will show
        assert bool(self.fc.fd["display_control"].verify_display_control_add_app_continue_button_ltwo_page()) == True, "Continue button is clickable"
        time.sleep(2)

