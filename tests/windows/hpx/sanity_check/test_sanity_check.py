import time
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from SAF.misc import windows_utils
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class TestSuiteSanityCheck(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.fc.launch_myHP_for_mat()
        cls.fc.kill_chrome_process()


    @pytest.mark.testrail("S75484.C33407733")
    @pytest.mark.require_platform(["ultron"])
    def test_01_show_hp_registration_first_launch_C33407733(self):

        self.fc.fd["hp_registration"].verify_hp_registration_show()
        text = self.fc.fd["hp_registration"].check_sub_title_text()
        assert text == "Register your PC for faster warranty support", "Hp registration sub title is not displayed"

    @pytest.mark.require_platform(["ultron"])
    @pytest.mark.testrail("S75484.C33407550")
    def test_02_install_hpx_C33407550(self):
        time.sleep(5)
        self.fc.restart_myHP()

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

    @pytest.mark.require_platform(["bopeep"])
    @pytest.mark.testrail("S75484.C33407775")
    def test_03_check_home_module_C33407775(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        if bool (self.fc.fd["hp_registration"].verify_hpone_page_show()):
            self.fc.fd["hp_registration"].click_hpone_page_skip_btn()

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(3)
        self.driver.swipe(direction="down", distance=2)
        assert bool(self.fc.fd["sanity_check"].verify_home_audio_card_show()) is True, "Home audio card is not displayed"
        assert bool(self.fc.fd["home"].verify_get_most_put_of_hp()) is True, "Get the most out of HP is not displayed"


    @pytest.mark.testrail("S75484.C33407861")
    @pytest.mark.require_platform(["ultron"])
    @pytest.mark.require_stack(["production"])
    def test_04_login_with_hpid_C33407861(self):
        time.sleep(5)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        self.fc.fd["hp_login"].verify_profile_icon_show()
        self.fc.fd["hp_login"].click_profile_icon()
        self.fc.fd["hpid"].login("felixx300010@outlook.com", "Goodyou123456")

        assert bool(self.fc.fd["hp_login"].verify_success_icon_show()) is True, "Success icon is not displayed"
        self.fc.fd["hp_login"].click_sign_out_btn()
        assert bool(self.fc.fd["hp_login"].verify_profile_icon_show()) is True, "Profile icon is not displayed"
        time.sleep(2)
        self.fc.kill_chrome_process()
    

    @pytest.mark.require_platform(["bopeep"])
    @pytest.mark.testrail("S75484.C33407781")
    def test_05_check_pc_device_module_C33407781(self):
        time.sleep(3)
        self.fc.kill_chrome_process()
        time.sleep(3)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_to_pc_device()

        assert bool(self.fc.fd["sanity_check"].verify_audio_module_show()) is True, "Audio module is not displayed"

    
    @pytest.mark.testrail("S75484.C33407773")
    @pytest.mark.require_platform(["bopeep"])
    def test_06_audio_UI_C33407773(self):
        time.sleep(3)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        assert self.fc.fd["audio"].verify_output_title() is True, "Output title is not displayed"
        assert self.fc.fd["audio"].verify_output_icon() is True, "Output icon is not displayed"
        assert self.fc.fd["audio"].verify_input_icon() is True, "Input icon is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_show() is True, "Noise removal is not displayed"
        assert self.fc.fd["audio"].verify_noise_eduction_show() is True, "Noise reduction is not displayed"


    @pytest.mark.require_platform(["bopeep"])
    @pytest.mark.testrail("S75484.C33407783")
    def test_07_check_support_module_show_C33407783(self):
        time.sleep(3)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_to_support()
        time.sleep(8)
        
        self.fc.kill_chrome_process()
        time.sleep(3)

        assert bool(self.fc.fd["sanity_check"].verify_support_guide_title_show()) is True, "Support guide title is not displayed"
        


    @pytest.mark.require_platform(["bopeep"])
    @pytest.mark.testrail("S75484.C33407776")
    def test_08_verify_settings_module_display_C33407776(self):
        time.sleep(5)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        time.sleep(5)

        self.fc.fd["navigation_panel"].navigate_to_settings()
        if self.fc.fd["settings"].verify_privacy_tab() is False:
            self.fc.fd["navigation_panel"].navigate_to_settings()
            time.sleep(2)
        settings_header  = self.fc.fd["settings"].verify_settings_header(), "Settings header is not displayed"
        assert self.fc.fd["settings"].verify_privacy_tab() is True, "Privacy tab is not displayed"
        assert self.fc.fd["settings"].verify_notfications_tab() is True, "Notifications tab is not displayed"
        assert self.fc.fd["settings"].verify_about_tab() is True, "About tab is not displayed"
        assert self.fc.fd["settings"].get_feedback_tab() == "Feedback", "Feedback tab is not displayed"

    

    @pytest.mark.testrail("S75484.C33407779")
    @pytest.mark.require_platform(["bopeep"])
    def test_09_display_control_module_show_C33407779(self):
        time.sleep(3)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        assert bool(self.fc.fd["sanity_check"].verify_display_control_show()) is True, "Display control is not displayed"

    
    @pytest.mark.require_platform(["ultron"])
    @pytest.mark.testrail("S75484.C33407782")
    def test_10_check_programmable_key_module_C33407782(self):
        time.sleep(5)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_pc_programmable_key_module()

        assert bool(self.fc.fd["sanity_check"].verify_programmable_key_module_show()) is True, "Programmable key module is not displayed"


    @pytest.mark.testrail("S75484.C35605631")
    @pytest.mark.require_platform(["ultron"])
    @pytest.mark.require_stack(["production"]) 
    def test_11_check_hpx_top_version_exist_C35605631(self):
        
        time.sleep(2)

        assert bool(self.fc.fd["sanity_check"].check_top_build_version()) is False, "Top build version is not displayed"


    # @pytest.mark.testrail("S75484.C33407863")
    # @pytest.mark.require_platform(["ultron"])
    # @pytest.mark.require_stack(["production"])
    # def test_12_check_smart_experience_module_C33407863(self):
    #     time.sleep(3)
    #     self.fc.kill_chrome_process()
    #     time.sleep(3)

    #     assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
    #     self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
    #     assert bool(self.fc.fd["sanity_check"].verify_privacy_alert_module_show()) is True, "Privacy alert module is not displayed"
    #     self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
    #     assert bool(self.fc.fd["sanity_check"].verify_auto_dimming_module_show()) is True, "Auto dimming module is not displayed"
        

    @pytest.mark.testrail("S75484.C33407778")
    @pytest.mark.require_platform(["willie"])
    def test_13_check_pen_control_module_C33407778(self):
        time.sleep(2)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        assert bool(self.fc.fd["sanity_check"].verify_pen_right_click_show()) is True, "Pen right click is not displayed"


    @pytest.mark.require_platform(["ultron"])
    @pytest.mark.testrail("S75484.C33407865")
    def test_14_check_bell_icon_C33407865(self):
        time.sleep(3)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["sanity_check"].click_bell_icon()
        self.fc.fd["sanity_check"].verify_notfication_tips_show()

        assert self.fc.fd["sanity_check"].get_notfications_tips_text() == "Notifications", "Notifications is not displayed"
        assert self.fc.fd["sanity_check"].get_new_message_text() == "No new messages!", "No new messages is not displayed"
    
    
    @pytest.mark.testrail("S75484.C34351866")
    @pytest.mark.require_platform(["bopeep"])
    def test_15_check_system_control_module_C34351866(self):
        time.sleep(3)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
    
        assert bool(self.fc.fd["sanity_check"].verify_system_control_subtitle_show_consumer()) is True, "System control subtitle is not displayed on consumer platform"
    

    @pytest.mark.testrail("S75484.C34351868")
    @pytest.mark.require_platform(["bopeep"])
    def test_16_check_screen_time_module_C34351868(self):
        time.sleep(3)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_screen_time()
    
        assert bool(self.fc.fd["sanity_check"].verify_screen_time_subtitle()) is True, "Screen time subtitle is not displayed"
    

    @pytest.mark.testrail("S75484.C34351869")
    @pytest.mark.require_platform(["bopeep"])
    def test_17_check_screen_distance_module_C34351869(self):
        time.sleep(3)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_screen_distance()
    
        assert bool(self.fc.fd["sanity_check"].verify_screen_distance_subtitle_show()) is True, "Screen distance subtitle is not displayed"
    

    @pytest.mark.testrail("S75484.C34351869")
    @pytest.mark.require_platform(["willie"])
    def test_18_check_touchpad_module_C36318093(self):
        time.sleep(3)
        self.fc.restart_myHP()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_touchpad_module()
        time.sleep(2)

        assert bool(self.fc.fd["sanity_check"].verify_touchpad_show()) is True, "Touchpad is not displayed"
        assert self.fc.fd["sanity_check"].get_gesture_control_text() == "Enable gesture control"


    @pytest.mark.require_platform(["longhornz"])
    def test_19_check_battery_manager_module_C40610965(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        self.fc.fd["navigation_panel"].navigate_to_battery_module()
        time.sleep(2)
        assert bool(self.fc.fd["sanity_check"].verify_battery_information_show()) is True, "Battery information is not displayed"
        assert bool(self.fc.fd["sanity_check"].verify_charging_options_show()) is True, "Charging options is not displayed"


    @pytest.mark.require_platform(["testudo"])
    def test_20_check_gesture_module_C41948027(self):
        time.sleep(3)
        self.fc.restart_myHP()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        self.fc.fd["navigation_panel"].navigate_to_gesture_module()
        assert bool(self.fc.fd["gesture"].verify_gesture_panel_banner_show()) is True, "Gesture panel banner is not displayed"
        assert bool(self.fc.fd["gesture"].verify_try_this_gesture_button_show()) is True, "Try this gesture button is not displayed"
        assert bool(self.fc.fd["gesture"].verify_pause_resume_card_title_show()) is True, "Pause resume card title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_volume_adjust_card_title_show()) is True, "Volume adjust card title is not displayed"
        assert bool(self.fc.fd["gesture"].verify_page_scroll_card_title_show()) is True, "Page scroll card title is not displayed"
    
    @pytest.mark.testrail("S75484.C33407863")
    @pytest.mark.require_platform(["masadan"])
    def test_21_check_presence_detection_module_C44741811(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_presence_detection()
        assert bool(self.fc.fd["vision_ai"].verify_auto_hdr_text_show()) is True, "Auto HDR  is not displayed"
        assert bool(self.fc.fd["vision_ai"].verify_intelligent_dynamic_contrast_text_show()) is True, "Intgelligent dynamic contrast is not displayed"
        assert bool(self.fc.fd["vision_ai"].verify_attention_focus_text_show()) is True, "Attention focus is not displayed"
    
    @pytest.mark.require_platform(["goldy"])
    def test_22_check_dock_station_module_C43270589(self):
        time.sleep(2)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"

        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_edit_button_show()) is True, "Dock station title edit button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_name_show()) is True, "Dock station module name is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_support_button_show()) is True, "Dock station support button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_scroll_view_show()) is True, "Dock station image is not displayed"


    @pytest.mark.testrail("S75484.C43466490")
    @pytest.mark.require_platform(["masadan"])
    def test_23_audio_UI_C43466490(self):
        time.sleep(3)
        self.fc.restart_app()

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_to_pc_audio()

        assert self.fc.fd["audio"].verify_output_title() is True, "Output title is not displayed"
        assert self.fc.fd["audio"].verify_output_icon() is True, "Output icon is not displayed"
        assert self.fc.fd["audio"].verify_input_icon() is True, "Input icon is not displayed"
        assert self.fc.fd["audio"].verify_noise_removal_show() is True, "Noise removal is not displayed"
        assert self.fc.fd["audio"].verify_noise_eduction_show() is True, "Noise reduction is not displayed"


    @pytest.mark.require_platform(["london"])
    @pytest.mark.testrail("S75484.C43466491")
    def test_24_check_programmable_key_module_C43466491(self):
        time.sleep(5)
        self.fc.restart_myHP()

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"

        self.fc.fd["navigation_panel"].navigate_pc_programmable_key_module()

        assert bool(self.fc.fd["sanity_check"].verify_programmable_key_module_show()) is True, "Programmable key module is not displayed"


    @pytest.mark.testrail("S75484.C43466492")
    @pytest.mark.require_platform(["ernesto"])
    def test_25_check_pen_control_module_C43466492(self):
        time.sleep(2)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        assert bool(self.fc.fd["sanity_check"].verify_pen_right_click_show()) is True, "Pen right click is not displayed"


    @pytest.mark.testrail("S75484.C43466493")
    @pytest.mark.require_platform(["ernesto"])
    def test_26_check_system_control_module_C43466493(self):
        time.sleep(3)
        self.fc.restart_myHP()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_system_control()
    
        assert bool(self.fc.fd["sanity_check"].verify_system_control_subtitle_show_commercial()) is True, "System control subtitle is not displayed on commercial platform"


    @pytest.mark.testrail("S75484.C43465933")
    @pytest.mark.require_platform(["longhornz"])
    def test_27_check_energy_consumption_module_C43465933(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is True, "Energy consumption module is  not visible"

    @pytest.mark.testrail("S75484.C44040268")
    @pytest.mark.require_platform(["goldy"])
    def test_28_check_presence_sensing_module_C44040268(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_presence_sensing_module_show()) is True, "Presence sensing module is  not visible"
        self.fc.fd["navigation_panel"].click_presence_sensing_module()
        assert bool(self.fc.fd["navigation_panel"].verify_power_battery_settings_page_show()) is True, "Power and battery settings page is not visible"
        self.fc.fd["navigation_panel"].click_close_button_on_power_battery_settings_page()
        time.sleep(2)

    @pytest.mark.require_platform(["ultron"])
    @pytest.mark.testrail("S75484.C33407551")
    def test_29_uninstall_hpx_C33407551(self):
        time.sleep(5)
        self.fc.uninstall_app()
        time.sleep(2)
        file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\LocalState"'
        time.sleep(2)
        file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
        time.sleep(2)
        assert file_exist is False, "LocalState folder is not deleted"    