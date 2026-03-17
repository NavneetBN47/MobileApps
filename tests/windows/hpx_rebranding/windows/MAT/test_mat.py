import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from SAF.misc.ssh_utils import SSH
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
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        cls.stack = request.config.getoption("--stack")
        cls.fc.launch_myHP()
 
 
    @pytest.mark.require_platform(["ultron"])
    def test_01_install_hpx_C51213104(self):
        time.sleep(4)
        if bool(self.fc.fd["devicesMFE"].verify_device_card_show_up(raise_e = False)) is False:
            assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        else:
            assert bool(self.fc.fd["devicesMFE"].verify_device_card_show_up()) is True, "Device card is not displayed on home page"


    @pytest.mark.require_platform(["ultron"])
    def test_02_check_support_module_C51213115(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        self.fc.click_profile_button()
        time.sleep(4)
        assert self.fc.fd["css"].verify_support_option_show_on_profile_page(), "Support option is not displayed on profile page"
        self.fc.fd["css"].click_support_option_on_profile_page()
        time.sleep(2)
        assert self.fc.fd["css"].verify_support_title_show_up(), "Support title is not displayed"
        time.sleep(2)
        self.fc.fd["css"].click_back_to_menu_button()
        time.sleep(2)
        assert self.fc.fd["css"].verify_close_button_show_up(), "close button is not displayed"
        self.fc.fd["css"].click_close_button()
        time.sleep(2)
 
 
    @pytest.mark.require_platform(["ultron"])
    def test_03_check_HPPK_module_on_commercial_paltform_C51213145(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        assert self.fc.fd["hppk"].verify_progkey_menucard_ctl_visible(), "Programmable key ctrl icon is not displayed"
 
   
    @pytest.mark.require_platform(["ultron"])
    def test_04_check_smart_experience_module_C51213160(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page(), "Presence detection is not displayed"
        time.sleep(5)
        self.fc.fd["smart_experience"].scroll_to_element("presence_detection_card_lone_page")
        presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
        time.sleep(2)
        assert presence_detection_card_lone_page.text == "Presence detection", "Presence detection card is not present."
        time.sleep(2)
        self.fc.fd["smart_experience"].click_presence_detection_card_lone_page()
        time.sleep(2)
        assert self.fc.fd["smart_experience"].verify_pivacy_alert_text_ultron_ltwo_page(), "Privacy Alert text is not displayed"      
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_ultron_text_ltwo_page(), "Auto Screen Dimming text is not displayed"
        assert self.fc.fd["smart_experience"].verify_restore_default_button_ltwo_page(), "Restore Default button is not displayed"
 
 
    @pytest.mark.require_platform(["ultron"])
    def test_05_uninstall_hpx_C51213102(self):
        time.sleep(4)
        self.fc.uninstall_app()
        time.sleep(2)
        file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\LocalState"'
        time.sleep(2)
        file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
        time.sleep(2)
        assert file_exist is False, "LocalState folder is not deleted"  
 
   
    @pytest.mark.require_platform(["keelung27"])
    def test_06_check_home_module_C51213112(self):
        time.sleep(4)
        assert bool(self.fc.fd["devicesMFE"].verify_device_card_show_up()) is True, "Device card is not displayed on home page"
        assert bool(self.fc.fd["devicesMFE"].verify_profile_icon_show_up()) is True, "Profile icon is not displayed on home page"
 
     
    @pytest.mark.require_platform(["keelung27"])
    def test_07_check_devices_module_C51213114(self):
        time.sleep(4)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up()) is True, "Back devices button is not displayed on PC devices page"
        assert bool(self.fc.fd["devicesMFE"].verify_profile_icon_show_up()) is True, "Profile icon is not displayed on PC devices page"
        if self.stack == "rebrand_pie":
            assert bool(self.fc.fd["devicesMFE"].verify_bell_icon_show_up()) is True, "Bell icon is not displayed on home page"
        assert bool(self.fc.fd["devicesMFE"].verify_sign_in_button_show_up()) is True, "Sign in button is not displayed on PC devices page"
 
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()) is True, "Display control lone page is not displayed on PC devices page"
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up()) is True, "Audio card is not displayed on PC devices page"
 
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(2)
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_product_information_title_show_up()) is True, "Product information title is not displayed on PC devices page"
        self.fc.swipe_window(direction="up", distance=15)
       
 
    @pytest.mark.require_platform(["keelung27"])
    def test_08_check_well_being_screen_time_module_C51213126(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "Well being card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
 
 
    @pytest.mark.require_platform(["keelung27"])
    def test_09_check_well_being_screen_distance_module_C51213128(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen distance title is not displayed"
        assert self.fc.fd["wellbeing"].verify_alert_options_title_show_up(), "Alert options title is not displayed"
        assert self.fc.fd["wellbeing"].verify_set_preferred_distance_title_show_up(), "Set preferred distance title is not displayed"
        self.fc.swipe_window(direction="up", distance=7)
        time.sleep(2)
 
 
    @pytest.mark.require_platform(["keelung27"])
    def test_10_check_display_control_module_C51213122(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        self.fc.swipe_window(direction="up", distance=4)
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
 
 
    @pytest.mark.require_platform(["keelung27"])
    def test_11_check_presence_sensing_module_C51213159(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "Presence Sensing card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_presence_sensing_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["presence_sensing"].verify_turn_off_my_screen_btn_show(), "Turn off my screen button is not displayed"
        assert self.fc.fd["presence_sensing"].verify_wake_my_device_btn_show(), "Wake my device button is not displayed"
        assert self.fc.fd["presence_sensing"].verify_dim_my_screen_btn_show(), "Dim my screen button is not displayed"
        self.fc.close_windows_settings_panel()
 
 
    @pytest.mark.require_platform(["goldy"])
    def test_12_check_audio_module_on_consumer_platform_C51213143(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        assert self.fc.fd["audio"].verify_input_title_show_up(), "Input title is not displayed"
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(4)
    
    
    @pytest.mark.require_platform(["goldy"])
    def test_13_check_settings_module_C51213117(self):
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.click_profile_button()
        time.sleep(4)
        assert self.fc.fd["css"].verify_settings_button_on_profile_page(), "Settings button is not displayed"
        self.fc.fd["css"].click_settings_button_on_profile_page()
        time.sleep(2)
        assert self.fc.fd["css"].verify_settings_title_show_up(), "Settings title is not displayed"
        assert self.fc.fd["css"].verify_manage_privacy_settings_button_on_settings_show_up(), "Privacy card is not displayed"
        assert self.fc.fd["css"].verify_back_to_menu_button_show_up(), "Back to menu button is not displayed"
        self.fc.fd["css"].click_back_to_menu_button()
        time.sleep(2)
 
   
    @pytest.mark.require_platform(["goldy"])
    def test_14_check_feedback_module_C51573089(self):
        assert self.fc.fd["css"].verify_feedback_button_on_profile_page(), "Feedback button is not displayed"
        self.fc.fd["css"].click_feedback_button_on_profile_page()
        time.sleep(2)
        assert self.fc.fd["css"].verify_feedback_title_show_up(), "Feedback title is not displayed"
        assert self.fc.fd["css"].verify_send_feedback_button_show_up, "Send feedback button is not displayed"      
        assert self.fc.fd["css"].verify_back_to_menu_button_show_up(), "Back to menu button is not displayed"
 
   
    @pytest.mark.require_platform(["goldy"])
    def test_15_check_dock_station_module_C51213139(self):
        self.fc.restart_myHP()
        time.sleep(4)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)
        assert bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is True, "Dock station card is not displayed"
        self.fc.fd["devicesMFE"].click_dock_station_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        assert self.fc.fd["dock_station"].verify_product_information_txt_show_up(), "Product information txt is not displayed"
 
 
    @pytest.mark.require_platform(["goldy"])
    def test_16_check_bell_notification_C51213124(self):
        self.fc.restart_myHP()
        time.sleep(4)
        assert self.fc.fd["css"].verify_bell_icon_show_up(), "bell icon is not displayed"
        self.fc.fd["css"].click_bell_icon()
        time.sleep(2)
        assert self.fc.fd["css"].verify_notification_title_show_up(), "notification title is not displayed"
 
 
    @pytest.mark.require_stack("rebrand_production")
    @pytest.mark.require_platform(["goldy"])
    def test_17_check_no_app_version_on_the_top_of_prod_build_C51213130(self):
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_app_version_on_the_top()) is False, "App version is displayed on the top"
 
 
    @pytest.mark.require_platform(["willie"])
    def test_18_check_touch_pad_module_on_consumer_platform_C51213132(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page(), "Touchpad card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_touchpad_title_show(), "Touchpad title is not shown"
        assert self.fc.fd["touchpad"].verify_adjust_feedback_intensity_link_show(), "Adjust feedback intensity link is not shown"
        assert self.fc.fd["touchpad"].verify_restore_default_button_show(), "Restore default button is not shown"
       
 
    @pytest.mark.require_platform(["willie"])
    def test_19_check_system_control_module_on_consumer_machine_C51213149(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
        assert self.fc.fd["system_control"].verify_system_control_performance_control_title_show(), "Performance Control title is not displayed"
    
    
    @pytest.mark.require_platform(["not available"])
    def test_20_check_pen_control_module_on_consumer_machine_C51213147(self):
        time.sleep(5)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_pen_card()
        self.fc.fd["pen_control"].click_customize_buttons()
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_card_show_up()) is True, "Upper barrel button is not displayed"
        assert bool(self.fc.fd["pen_control"].verify_lower_barrel_card_show_up()) is True, "Lower barrel button is not displayed"


    @pytest.mark.require_platform(["willie"])
    def test_21_check_video_control_module_C52567128(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
        time.sleep(3)
        if self.fc.fd["video_control"].verify_camera_pop_up_continue_button():
            self.fc.fd["video_control"].click_camera_pop_up_continue_button()
            time.sleep(2)
            self.fc.fd["video_control"].click_to_install_hp_presence_app()
            time.sleep(60)
            self.fc.kill_msstore_process()
            time.sleep(2)
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
            time.sleep(5)
            if self.fc.fd["video_control"].verify_tutorial_next_button_show():
                self.fc.fd["video_control"].click_tutorial_next_button()
                time.sleep(2)
                self.fc.fd["video_control"].click_tutorial_next_button()
            
        time.sleep(2)
        self.fc.close_myHP()
        assert self.fc.fd["video_control"].verify_auto_frame_title_show_up(), "Auto frame title is not displayed"
        self.fc.kill_camera_process()
 
 
    @pytest.mark.require_platform(["snowwhite"])
    def test_22_check_audio_control_module_on_commercial_machine_C51213151(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
        assert self.fc.fd["audio"].verify_input_title_show_up(), "Input title is not displayed"
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(4)
 
 
    @pytest.mark.require_platform(["enstrom"])
    def test_23_check_battery_manager_module_on_consumer_platform_C51213135(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(2)
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
 
 
    @pytest.mark.require_platform(["snowwhite"])
    def test_25_check_system_control_module_on_commercial_machine_C51213158(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)
        self.fc.fd["system_control"].click_smart_sense_radio_button_commercail()
        time.sleep(2)
        assert self.fc.fd["system_control"].get_smart_sense_radio_button_commercial_is_selected() == "true", "Smart sense mode is not selcted"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(4)


    @pytest.mark.require_platform(["snowwhite"])
    def test_26_check_battery_manager_module_on_commercial_platform_C52076597(self):
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(2)
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        assert self.fc.fd["battery"].verify_battery_information_title_ltwo(), "Battery Information title is not displayed"
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(4)


    @pytest.mark.require_platform(["snowwhite"])
    def test_27_check_energey_consumption_module_C51213141(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        time.sleep(2)
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
 
 
    @pytest.mark.require_platform(["snowwhite"])
    def test_28_check_gesture_module_C51213137(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gesture card not found"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        time.sleep(3)
        assert self.fc.fd["gestures"].verify_gesture_card_title_show(), "Gesture card title not found"
        assert self.fc.fd["gestures"].verify_feedback_message_show(), "Feedback message not found"

 
    @pytest.mark.require_platform(["london"])
    def test_29_check_HPPK_module_on_hpone_platform_C51213153(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        assert self.fc.fd["hppk"].verify_progkey_info_icon_visible(), "Programmable key info icon is not displayed"
 
 
    @pytest.mark.require_platform(["machu13x"])
    def test_30_check_pen_control_module_on_commercial_machine_C51213156(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        assert self.fc.fd["devicesMFE"].verify_pen_card_show(), "Pen card is not displayed"
        self.fc.fd["devicesMFE"].click_pen_card()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        assert self.fc.fd["pen_control"].verify_radial_menu_commercial(), "Radial Menu is not available"
 
   
    @pytest.mark.require_platform(["divinity"])
    def test_31_check_hp_go_module_C56668399(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hp_go_card_show_on_pc_device_page(), "hp go card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hp_go_card()
        time.sleep(3)
        assert self.fc.fd["hp_go"].verify_hp_go_title_on_hp_go_page(), "HP Go title is not displayed"
        assert self.fc.fd["hp_go"].verify_hp_go_information_txt_on_hp_go_page(), "HP Go information text is not displayed"
        assert self.fc.fd["hp_go"].verify_hp_go_connection_txt_on_hp_go_page(), "HP Go connection text is not displayed"
 
 
    @pytest.mark.require_platform(["divinity"])
    def test_32_check_audio_control_module_on_arm_platform_C52108259(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_conference_show_up(), "Conference is not displayed"
        assert self.fc.fd["audio"].get_restore_default_button_text() == "Restore default", "Restore defaults button is not displayed"
    
    @pytest.mark.require_platform(["divinity"])
    def test_33_check_vision_ai_module_on_arm_platform_C58596420(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        time.sleep(3)
        assert self.fc.fd["smart_experience"].verify_auto_hdr_text_ltwo_page(), "Auto HDR text is not displayed"
        assert self.fc.fd["smart_experience"].verify_onlooker_detection_text_ltwo_page(), "Onlooker detection text is not displayed"


    @pytest.mark.require_platform(["andaz"])
    def test_34_check_video_control_on_arm_platform_C58525791(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page(), "Video control card is not displayed"
    

    @pytest.mark.require_platform(["andaz"])
    def test_35_check_presence_sensing_on_arm_platform_C58525793(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_presence_sensing_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["presence_sensing"].verify_turn_off_my_screen_btn_show(), "Turn off my screen button is not displayed"
        self.fc.close_windows_settings_panel()
    
    
    # # This feature is not available
    # @pytest.mark.require_platform(["turbine"])
    # def test_36_verify_ai_companion_displayed_C61419503(self):
    #     time.sleep(5)
    #     assert self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header(), "HP AI Assistant button is not visible on header"
    #     time.sleep(3)
    #     self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
    

    @pytest.mark.require_platform(["bantie"])
    def test_37_verify_task_group_displayed_C62735570(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_task_group_lone_page(), "Task group L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_task_group_card_lone_page()
        time.sleep(2)
        assert self.fc.fd["task_group"].verify_task_group_create_new_show(), "Task group creaate new button is not displayed"
