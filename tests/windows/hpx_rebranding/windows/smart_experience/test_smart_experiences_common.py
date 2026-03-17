import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Smart_Experience(object):

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_smart_experience_camera_and_presence_detection_card_displays_respective_devices_C53018751(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
            self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
            presence_detection_header_text_lwo_page = self.fc.fd["smart_experience"].get_camera_and_presence_detection_header_masadan_ltwo_page()
            assert presence_detection_header_text_lwo_page == "Presence detection","presence detection text is not present."
        if self.platform.lower()=='ultron':
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
            self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
            time.sleep(5)
            presence_detection_header_text_lwo_page = self.fc.fd["smart_experience"].get_camera_and_presence_detection_header_ultron_ltwo_page()
            assert  presence_detection_header_text_lwo_page == "Presence detection","Presence detection text is not present."

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_smart_experience_ui_validation_all_cards_on_all_devices_C51244784(self):
        logging.info(f"Platform {self.platform.lower()}")
        if self.platform.lower() == 'masadansku5':
            assert self.fc.fd["smart_experience"].verify_auto_hdr_text_ltwo_page(), "Auto HDR card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_auto_hdr_description_ltwo_page(), "Auto HDR card description is not displayed"
            assert self.fc.fd["smart_experience"].verify_attention_focus_text_ltwo_page(), "Attention focus card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_attention_focus_description_ltwo_page(), "Attention focus card description is not displayed"
            assert self.fc.fd["smart_experience"].verify_onlooker_detection_text_ltwo_page(), "Onlooker detection card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_onlooker_detection_description_ltwo_page(), "Onlooker detection card description is not displayed"
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.swipe_window(direction="down", distance=5)
            assert self.fc.fd["smart_experience"].verify_intelligent_dynamic_contrast_text_ltwo_page(), "Intelligent dynamic contrast card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_intelligent_dynamic_contrast_description_ltwo_page(), "Intelligent dynamic contrast card description is not displayed"
            assert self.fc.fd["smart_experience"].verify_enable_screen_blur_ltwo_page(), "Enable screen blur card is not displayed"

        if self.platform.lower()== 'masadanxsku4':
            assert self.fc.fd["smart_experience"].verify_auto_hdr_text_ltwo_page(), "Auto HDR card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_auto_hdr_description_ltwo_page(), "Auto HDR card description is not displayed"
            assert self.fc.fd["smart_experience"].verify_onlooker_detection_text_ltwo_page(), "Onlooker detection card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_onlooker_detection_description_ltwo_page(), "Onlooker detection card description is not displayed"
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.swipe_window(direction="down", distance=5)
            assert self.fc.fd["smart_experience"].verify_enable_sure_view_ltwo_page(), "Sure view card is not displayed"

        if self.platform.lower()=='ultron':
            assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_ultron_text_ltwo_page(), "Auto Screen Dimming card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_description_ultron_ltwo_page(), "Auto Screen Dimming card description is not displayed"
            self.fc.swipe_window(direction="down", distance=4)
            assert self.fc.fd["smart_experience"].verify_pivacy_alert_text_ultron_ltwo_page(), "Privacy Alert card text is not displayed"
            assert self.fc.fd["smart_experience"].verify_pivacy_alert_description_ultron_ltwo_page(), "Privacy Alert card description is not displayed"

        assert self.fc.fd["smart_experience"].verify_restore_default_button_ltwo_page(), "Restore Default button is not displayed"

    @pytest.mark.ota
    def test_03_auto_hdr_C53018753(self):
        if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
            assert self.fc.fd["smart_experience"].verify_auto_hdr_description_ltwo_page(), "AUTO HDR description is not present."
            auto_hdr_desription = self.fc.fd["smart_experience"].get_auto_hdr_description_two_page()
            assert  "Automatically enhances video brightness, contrast, and colors" in auto_hdr_desription, "Description incorrect : " + auto_hdr_desription

    @pytest.mark.ota
    def test_04_default_values_of_the_features_C51244785(self):
        logging.info(f"Platform {self.platform.lower()}")
        
        if self.platform.lower() == 'masadansku5':
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            assert self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "1", "AUTO HDR toggle button state is not ON."
            assert self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state() == "0", "Onlooker detection state is not OFF."
            assert self.fc.fd["smart_experience"].get_enable_screen_blur_toggle_button_state() == "0", "Enable SureView toggle button state is not OFF."

    @pytest.mark.ota
    def test_05_persistence_auto_hdr_C51244814(self):
        logging.info(f"Platform {self.platform.lower()}")
        if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["smart_experience"].click_auto_hdr_toggle_button()
            assert self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "0", "AUTO HDR toggle button state is not OFF."
            time.sleep(2)

            self.fc.close_myHP()
            time.sleep(2)
            self.fc.launch_myHP()

            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=5)
            
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
            self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
            assert self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "0", "AUTO HDR toggle button state is not OFF."
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app()
            self.fc.fd["smart_experience"].click_auto_hdr_toggle_button() #Restore the default value

    @pytest.mark.ota
    def test_06_restore_default_button_C51244815(self):
        logging.info(f"Platform {self.platform.lower()}")
        if self.platform.lower() == 'masadansku5':
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["smart_experience"].click_onlooker_detection_toggle_button()
            assert self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state() == "1", "AUTO HDR toggle button state is not ON."
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app()
            self.fc.fd["smart_experience"].click_attention_focus_toggle_button_toggle_button_state()
            assert self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state() == "1", "AUTO HDR toggle button state is not ON."
            self.fc.swipe_window(direction="down", distance=4)
            self.fc.fd["smart_experience"].click_restore_default_button_ltwo_page()
            assert self.fc.fd["smart_experience"].get_onlooker_detection_toggle_button_state() == "0", "AUTO HDR toggle button state is not OFF."
            assert self.fc.fd["smart_experience"].get_attention_focus_toggle_button_state() == "0", "AUTO HDR toggle button state is not OFF."

    @pytest.mark.ota
    def test_07_consistency_multiple_app_runs_C51244818(self):
        #Loop 3 times
        for i in range(3):
            self.fc.close_myHP()
            time.sleep(2)
            self.fc.launch_myHP()
            self.fc.maximize_and_verify_device_card()
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.swipe_window(direction="down", distance=5)
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page.text == "Presence detection", "Camera and presence detection card is not present."
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            time.sleep(5)
            self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
            time.sleep(5)
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app()
            self.fc.fd["smart_experience"].click_auto_hdr_toggle_button()

    @pytest.mark.ota
    def test_08_launching_app_through_deeplink_C53017972(self):
        logging.info(f"Platform {self.platform.lower()}")
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://presencedetection")    
        if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
            assert self.fc.fd["smart_experience"].verify_camera_and_presence_detection_header_masadan_ltwo_page(), "Camera and presence detection header is not displayed"
        if self.platform.lower() == 'ultron':
            assert self.fc.fd["smart_experience"].verify_camera_and_presence_detection_header_ultron_ltwo_page(), "Camera and presence detection header is not displayed"
        
    @pytest.mark.ota
    def test_09_turn_on_hdr_from_windows_settings_C51244805(self):
        logging.info(f"Platform {self.platform.lower()}")
        try:
            if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
                self.fc.close_myHP()
                self.fc.open_camera_hdr_settings()
                time.sleep(2)             
                assert self.fc.fd["smart_experience"].verify_smart_experience_use_video_hdr_in_system_setting_menu_button(),"Camera HDR Settings for HP Camera Missing"
                self.fc.fd["smart_experience"].click_smart_experience_use_video_hdr_in_system_setting_menu_button()
                time.sleep(2)
                if self.fc.fd["smart_experience"].get_smart_experience_use_system_settings_video_hdr_toggle_switch_state() == "0":
                    self.fc.fd["smart_experience"].click_smart_experience_use_system_settings_video_hdr_toggle_switch()
                time.sleep(2)
                state = self.fc.fd["smart_experience"].get_smart_experience_use_system_settings_video_hdr_toggle_switch_state()
                assert state == "1", f"HDR check box is not True. State: {state}" 
                self.fc.close_windows_settings_panel()
                self.fc.launch_myHP()
                self.fc.maximize_and_verify_device_card()
                self.fc.swipe_window(direction="down", distance=6)
                time.sleep(3)
                presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
                assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
                self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
                time.sleep(2)
                state = self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state()
                assert state == "1", f"AUTO HDR toggle button state is not ON.State: {state}"
        finally:
            self.fc.close_myHP()

    @pytest.mark.ota
    def test_10_hpx_auto_hdr_Vs_windows_video_hdr_C51244804(self):
        logging.info(f"Platform {self.platform.lower()}")
        try:
            if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
                self.fc.launch_myHP()   
                self.fc.maximize_and_verify_device_card()
                self.fc.swipe_window(direction="down", distance=6)
                time.sleep(3)
                presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
                assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
                self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
                time.sleep(5)
                self.fc.fd["smart_experience"].get_focus_on_app("auto_hdr_toggle_button_ltwo_page")
                if self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "1":
                    self.fc.fd["smart_experience"].click_auto_hdr_toggle_button()
                assert self.fc.fd["smart_experience"].get_auto_hdr_toggle_button_state() == "0", "AUTO HDR toggle button state is not OFF."
                time.sleep(5)
                self.fc.close_myHP()
                self.fc.open_camera_hdr_settings()
                assert self.fc.fd["smart_experience"].verify_smart_experience_use_video_hdr_in_system_setting_menu_button(),"Camera HDR Settings for HP Camera Missing"
                self.fc.fd["smart_experience"].click_smart_experience_use_video_hdr_in_system_setting_menu_button()
                time.sleep(2)
                assert bool(self.fc.fd["smart_experience"].get_smart_experience_use_system_settings_video_hdr_toggle_switch_state()) is True, "HDR check box is not True. State: " + self.fc.fd["smart_experience"].get_smart_experience_use_video_hdr_toggle_switch_state()
        finally:
            self.fc.close_windows_settings_panel()