from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Auido_Speaker_Configuration(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        
    #external speaker can only be connected on arti
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_speaker_configuration_default_UI_C32316744(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_speaker()
        time.sleep(1)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_External_Speaker_Settings_text_show()) is True, "External Speaker Settings text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Speaker_Configuration_text_show()) is True, "Speaker Configuration text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Stereo_btn_show()) is True, "Stereo button is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Quad_btn_show()) is True, "Quad button is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_5_1_btn_show()) is True, "5.1 button is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Setup_Test_Sound_text_show()) is True, "Setup Test Sound text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Sound_hide_text_show()) is True, "Sound hide text is not show"
        time.sleep(1)
        self.fc.fd["audio"].click_Setup_Test_Sound_hide_caret_custom_icon()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(3)
        assert bool(self.fc.fd["audio"].verify_Multi_Streaming_text_show()) is True, "Multi Streaming text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_switchSetMultiStreamOn_toggle_show()) is True, "switch Set Multi Stream On toggle is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Play_Test_btn_show()) is True, "Play Test button is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Front_Left_checkbox_show()) is True, "Front Left checkbox is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Front_Left_text_show()) is True, "Front Left text is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Front_Right_checkbox_show()) is True , "Front Right checkbox is not show"
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_Front_Right_text_show()) is True, "Front Right text is not show"
        self.fc.close_myHP()

       
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["WNF_P2_P3"])
    def test_02_will_not_remember_speaker_configuration_settings_C32881691(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_External_Speaker_Settings_text_show()) is True, "External Speaker Settings text is not show"
        assert bool(self.fc.fd["audio"].verify_Stereo_btn_show()) is True, "Stereo button is not show"
        assert bool(self.fc.fd["audio"].verify_Quad_btn_show()) is True, "Quad button is not show"
        assert bool(self.fc.fd["audio"].verify_5_1_btn_show()) is True, "5.1 button is not show"
        assert bool(self.fc.fd["audio"].verify_Sound_hide_text_show()) is True, "Sound hide text is not show"
        
        self.fc.fd["audio"].click_Setup_Test_Sound_hide_caret_custom_icon()
        time.sleep(3)
        
        self.fc.fd["audio"].click_Quad_btn()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        assert self.fc.fd["audio"].is_Front_left_checkbox_selected() == "1", "Front left checkbox is not selected"
        assert self.fc.fd["audio"].is_Front_right_checkbox_selected() == "1", "Front right checkbox is not selected"
        assert self.fc.fd["audio"].is_Back_left_checkbox_selected() == "1", "Back left checkbox is not selected"
        assert self.fc.fd["audio"].is_Back_right_checkbox_selected() == "1", "Back right checkbox is not selected"
        
        self.fc.fd["audio"].click_Front_left_checkbox()
        time.sleep(1)
        self.fc.fd["audio"].click_Back_left_checkbox()
        time.sleep(1)
        
        assert self.fc.fd["audio"].is_Front_left_checkbox_selected() == "0", "Front left checkbox is selected"
        assert self.fc.fd["audio"].is_Front_right_checkbox_selected() == "1", "Front right checkbox is not selected"
        assert self.fc.fd["audio"].is_Back_left_checkbox_selected() == "0","Back left checkbox is selected"
        assert self.fc.fd["audio"].is_Back_right_checkbox_selected() == "1", "Back right checkbox is not selected"

        self.fc.close_myHP()
        time.sleep(2)
        self.fc.launch_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)
        self.fc.fd["audio"].click_Setup_Test_Sound_hide_caret_custom_icon()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(3)

        assert self.fc.fd["audio"].is_Front_left_checkbox_selected() == "0", "Front left checkbox is selected"
        assert self.fc.fd["audio"].is_Front_right_checkbox_selected() == "1", "Front right checkbox is not selected"
        assert self.fc.fd["audio"].is_Back_left_checkbox_selected() == "0","Back left checkbox is selected"
        assert self.fc.fd["audio"].is_Back_right_checkbox_selected() == "1", "Back right checkbox is not selected"
        self.fc.close_myHP()
        
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_Turn_on_off_multi_streaming_C31726100(self):
        time.sleep(5)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_speaker_tab()
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["audio"].click_restore_button()
        self.fc.fd["audio"].click_restore_default_continue_button()
        assert bool(self.fc.fd["audio"].verify_Sound_hide_text_show()) is True, "Sound hide text is not show"
        time.sleep(1)
        if bool(self.fc.fd["audio"].verify_switchSetMultiStreamOn_toggle_show()) is False:
            self.fc.fd["audio"].click_Setup_Test_Sound_hide_caret_custom_icon()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
            assert bool(self.fc.fd["audio"].verify_switchSetMultiStreamOn_toggle_show()) is True, "switch Set Multi Stream On toggle is not show"
        time.sleep(1)
        self.fc.fd["audio"].click_switchSetMultiStreamOn_toggle()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=4)
        time.sleep(3)
        self.fc.fd["audio"].click_speaker_tab()
        self.fc.swipe_window(direction="down", distance=4)
        assert bool(self.fc.fd["audio"].verify_switchSetMultiStreamOff_toggle_show()) is True, "switch Set Multi Stream Off toggle is not show"
        time.sleep(1)
        self.fc.fd["audio"].click_switchSetMultiStreamOff_toggle()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        self.fc.fd["audio"].click_speaker_tab()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        if bool(self.fc.fd["audio"].verify_switchSetMultiStreamOn_toggle_show()) is False:
            self.fc.fd["audio"].click_Setup_Test_Sound_hide_caret_custom_icon()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=4)
            time.sleep(2)
        time.sleep(1)
        assert bool(self.fc.fd["audio"].verify_switchSetMultiStreamOn_toggle_show()) is True, "switch Set Multi Stream On toggle is not show"
        
    
    @pytest.mark.consumer
    @pytest.mark.function
    def test_04_restore_default_work_well_with_speaker_configuration_C32881791(self): 
        self.fc.restart_myHP() 
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not show"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_speaker_tab()
        self.fc.swipe_window(direction="down", distance=4)
        time.sleep(2)
        self.fc.fd["audio"].click_to_expand_caret()
        self.fc.swipe_window(direction="down", distance=4)
        
        self.fc.fd["audio"].click_fifty_one_tab()
        time.sleep(5)
        self.fc.fd["audio"].click_on_dropdown("subwoofer_db_dropdown")
        time.sleep(5)
        self.fc.fd["audio"].press_down_arrow_key("subwoofer_db_dropdown")

        self.fc.fd["audio"].click_on_dropdown("center_ft_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("center_ft_dropdown")

        self.fc.fd["audio"].click_on_dropdown("center_db_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("center_db_dropdown")
        
        self.fc.fd["audio"].click_on_dropdown("Front_left_ft_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("Front_left_ft_dropdown")

        self.fc.fd["audio"].click_on_dropdown("Front_left_db_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("Front_left_db_dropdown")
                
        self.fc.fd["audio"].click_on_dropdown("rightSelect_ft_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("rightSelect_ft_dropdown")

        self.fc.fd["audio"].click_on_dropdown("rightNextSelect_db_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("rightNextSelect_db_dropdown")
        
        self.fc.fd["audio"].click_on_dropdown("leftBottomSelect_ft_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("leftBottomSelect_ft_dropdown")

        self.fc.fd["audio"].click_on_dropdown("leftBottomNextSelect_db_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("leftBottomNextSelect_db_dropdown")

        self.fc.fd["audio"].click_on_dropdown("rightBottomSelect_ft_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("rightBottomSelect_ft_dropdown")   

        self.fc.fd["audio"].click_on_dropdown("rightBottomNextSelect_db_dropdown")
        self.fc.fd["audio"].press_down_arrow_key("rightBottomNextSelect_db_dropdown")

        self.fc.fd["audio"].click_to_collapse_caret()  
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["audio"].click_restore_button() 
        self.fc.fd["audio"].click_continue_button()
        self.fc.fd["audio"].click_to_expand_caret()   
               
        default_subwoofer_db_value = self.fc.fd["audio"].verify_subwoofer_db_value()
        assert default_subwoofer_db_value=="0 dB","Default suwoofer DB value did not change to 0 dB -{}".format(default_subwoofer_db_value)

        default_center_ft_value = self.fc.fd["audio"].verify_center_ft_value()
        assert default_center_ft_value=="15 ft","Default center FT value did not change to 15 ft -{}".format(default_center_ft_value)

        default_center_db_value = self.fc.fd["audio"].verify_center_db_value()
        assert default_center_db_value=="0 dB","Default center DB value did not change to 0 dB -{}".format(default_center_db_value)

        default_front_left_ft_value = self.fc.fd["audio"].verify_front_left_ft_value()
        assert default_front_left_ft_value=="15 ft","Default front left FT value did not change to 15 ft -{}".format(default_front_left_ft_value)

        default_front_left_db_value = self.fc.fd["audio"].verify_front_left_db_value()
        assert default_front_left_db_value=="0 dB","Default front left DB value did not change to 0 dB -{}".format(default_front_left_db_value)

        default_front_right_ft_value = self.fc.fd["audio"].verify_front_right_ft_value()
        assert default_front_right_ft_value=="15 ft","Default front right FT value did not change to 15 ft -{}".format(default_front_right_ft_value)

        default_front_right_db_value = self.fc.fd["audio"].verify_front_right_db_value()
        assert default_front_right_db_value=="0 dB","Default front right DB value did not change to 0 dB -{}".format(default_front_right_db_value)

        default_bottom_left_ft_value = self.fc.fd["audio"].verify_bottom_left_ft_value()
        assert default_bottom_left_ft_value=="15 ft","Default bottom left FT value did not change to 15 ft -{}".format(default_bottom_left_ft_value)

        default_bottom_left_db_value = self.fc.fd["audio"].verify_bottom_left_db_value()
        assert default_bottom_left_db_value=="0 dB","Default bottom left DB value did not change to 0 dB -{}".format(default_bottom_left_db_value)

        default_bottom_right_ft_value = self.fc.fd["audio"].verify_bottom_right_ft_value()
        assert default_bottom_right_ft_value=="15 ft","Default bottom right FT value did not change to 15 ft -{}".format(default_bottom_right_ft_value)

        default_bottom_right_db_value = self.fc.fd["audio"].verify_bottom_right_db_value()
        assert default_bottom_right_db_value=="0 dB","Default bottom right DB value did not change to 0 dB -{}".format(default_bottom_right_db_value)

        self.fc.fd["audio"].click_to_collapse_caret()