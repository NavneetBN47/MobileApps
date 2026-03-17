import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_PenControl_UI(object):

    #this suite should run on willie with trio pen and robotic introduction

    @pytest.mark.consumer
    @pytest.mark.function
    def test_01_trio_pen_consumer_C56331599(self):
        assert self.fc.fd["devicesMFE"].verify_pen_card_show() is False, "Pen card is shown before introducing the pen"
        self.vcosmos.introduce_pen()
        self.vcosmos.clean_up_logs()
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(2)
        #"HP Digital pen" name should be displayed in the UI of the module
        assert self.fc.fd["pen_control"].get_trio_pen_name_consumer() == "HP Digital Pen", "HP Digital Pen is not displayed"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_customize_button_UI_for_consumer_C44225289(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
        assert "Upper barrel button" in self.fc.fd["pen_control"].get_upper_barrel_button_text(), "Upper barrel button is not visible"
        assert self.fc.fd["pen_control"].get_right_click_text_commercial() == "Right-click", "Right-click is not visible"
        assert "Lower barrel button" in self.fc.fd["pen_control"].get_lower_barrel_button_text() , "Lower barrel button is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_erase_text() == "Erase", "Erase is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_upper_barrel_button_UI_for_consumer_C44225290(self): 
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_right_click_text_commercial() == "Right-click", "Right-click is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_lower_barrel_button_UI_for_consumer_C44225291(self): 
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_erase_text() == "Erase", "Erase"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_lower_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_upper_barrel_button_action_list_C43385327(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        assert self.fc.fd["pen_control"].get_upper_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_undo_text() == "Undo", "Undo is not visible"
        assert self.fc.fd["pen_control"].get_shift_key_text() == "Shift key", "Shift key is not visible"
        assert self.fc.fd["pen_control"].get_control_key_text() == "Control key", "Control key is not visible"
        assert self.fc.fd["pen_control"].get_alt_key_text() == "Alt key", "Alt key is not visible"
        assert self.fc.fd["pen_control"].get_windows_key_text() == "Windows key", "Windows key is not visible"        
        self.fc.swipe_window(direction="down", distance=2)
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_tab_key_text() == "Tab key", "Tab key is not visible"
        assert self.fc.fd["pen_control"].get_right_arrow_key_text() == "Right arrow key", "Right arrow key is not visible"
        assert self.fc.fd["pen_control"].get_left_arrow_key_text() == "Left arrow key", "Left arrow key is not visible"
        assert self.fc.fd["pen_control"].get_previous_page_text() == "Previous page", "Previous page is not visible"
        assert self.fc.fd["pen_control"].get_next_page_text() == "Next page", "Next page is not visible"
        assert self.fc.fd["pen_control"].get_scroll_text() == "Scroll", "Scroll is not visible"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_erase_text_commercial() == "Erase", "Erase is not visible"        
        assert self.fc.fd["pen_control"].get_disable_pen_buttons_text() == "Disable pen buttons", "Left click is not visible"        
        assert self.fc.fd["pen_control"].get_upper_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["pen_control"].get_take_screenshot_text() == "Take screenshot", "Take screenshot is not visible"
        assert self.fc.fd["pen_control"].get_switch_between_apps_text() == "Switch between apps", "Switch between apps is not visible"
        assert self.fc.fd["pen_control"].get_launch_task_manager_text() == "Launch task manager", "Launch task manager is not visible"
        assert self.fc.fd["pen_control"].get_new_browser_tab_text() == "New browser tab", "New browser tab is not visible"
        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_show_the_desktop_text() == "Show the desktop", "Show the desktop is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_consumer() == "Play / Pause", "Play / Pause is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        assert self.fc.fd["pen_control"].get_mute_unmute_text() == "Mute / Unmute", "Mute / Unmute is not visible"
        self.fc.fd["pen_control"].click_mute_unmute_radio_btn_upper_barrel()
        if self.fc.fd["pen_control"].mute_unmute_radio_btn_upper_barrel_selected() == "false":
            self.fc.fd["pen_control"].click_mute_unmute_radio_btn_upper_barrel()
        self.fc.swipe_window(direction="up", distance=25)
        assert self.fc.fd["pen_control"].get_current_assignment_selected_value() == "Mute / Unmute", "Mute/Unmute is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_lower_barrel_button_action_list_C43385444(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()
        assert self.fc.fd["pen_control"].get_lower_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_undo_text() == "Undo", "Undo is not visible"
        assert self.fc.fd["pen_control"].get_shift_key_text() == "Shift key", "Shift key is not visible"
        assert self.fc.fd["pen_control"].get_control_key_text() == "Control key", "Control key is not visible"
        assert self.fc.fd["pen_control"].get_alt_key_text() == "Alt key", "Alt key is not visible"
        assert self.fc.fd["pen_control"].get_windows_key_text() == "Windows key", "Windows key is not visible"        
        self.fc.swipe_window(direction="down", distance=2)
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        time.sleep(5)   
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_tab_key_text() == "Tab key", "Tab key is not visible"
        assert self.fc.fd["pen_control"].get_right_arrow_key_text() == "Right arrow key", "Right arrow key is not visible"
        assert self.fc.fd["pen_control"].get_left_arrow_key_text() == "Left arrow key", "Left arrow key is not visible"
        assert self.fc.fd["pen_control"].get_previous_page_text() == "Previous page", "Previous page is not visible"
        assert self.fc.fd["pen_control"].get_next_page_text() == "Next page", "Next page is not visible"
        assert self.fc.fd["pen_control"].get_scroll_text() == "Scroll", "Scroll is not visible"
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_lower_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"        
        assert self.fc.fd["pen_control"].get_right_click_text_commercial() == "Right-click", "Right-click is not visible"
        assert self.fc.fd["pen_control"].get_disable_pen_buttons_text() == "Disable pen buttons", "Left click is not visible"
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_lower_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_take_screenshot_text() == "Take screenshot", "Take screenshot is not visible"
        assert self.fc.fd["pen_control"].get_switch_between_apps_text() == "Switch between apps", "Switch between apps is not visible"
        assert self.fc.fd["pen_control"].get_launch_task_manager_text() == "Launch task manager", "Launch task manager is not visible"
        assert self.fc.fd["pen_control"].get_new_browser_tab_text() == "New browser tab", "New browser tab is not visible"
        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_show_the_desktop_text() == "Show the desktop", "Show the desktop is not visible"        
        assert self.fc.fd["pen_control"].get_lower_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_consumer() == "Play / Pause", "Play / Pause is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        assert self.fc.fd["pen_control"].get_mute_unmute_text() == "Mute / Unmute", "Mute / Unmute is not visible"
        self.fc.fd["pen_control"].click_mute_unmute_radio_btn_lower_barrel()
        if self.fc.fd["pen_control"].mute_unmute_radio_btn_lower_barrel_selected() == "false":
            self.fc.fd["pen_control"].click_mute_unmute_radio_btn_lower_barrel()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=25)
        assert self.fc.fd["pen_control"].get_current_assignment_selected_value() == "Mute / Unmute", "Mute / Unmute is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    def test_07_more_action_link_C53060087(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        assert self.fc.fd["pen_control"].get_upper_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        assert self.fc.fd["pen_control"].get_upper_barrel_button_undo_text() == "Undo", "Undo is not visible"
        assert self.fc.fd["pen_control"].get_shift_key_text() == "Shift key", "Shift key is not visible"
        assert self.fc.fd["pen_control"].get_control_key_text() == "Control key", "Control key is not visible"
        assert self.fc.fd["pen_control"].get_alt_key_text() == "Alt key", "Alt key is not visible"
        assert self.fc.fd["pen_control"].get_windows_key_text() == "Windows key", "Windows key is not visible"        
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_previous_page_text() == "Previous page", "Previous page is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_restore_defaults_customize_buttons_C43385575(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        self.fc.fd["pen_control"].click_undo_radio_btn_upper_barrel()
        if self.fc.fd["pen_control"].undo_radio_btn_upper_barrel_selected() == "false":
            self.fc.fd["pen_control"].click_undo_radio_btn_upper_barrel()
        self.fc.fd["pen_control"].click_customize_back_button()   
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()
        self.fc.swipe_window(direction="down", distance=20)
        self.fc.fd["pen_control"].click_mute_unmute_radio_btn_lower_barrel()
        if self.fc.fd["pen_control"].mute_unmute_radio_btn_lower_barrel_selected() == "false":
            self.fc.fd["pen_control"].click_mute_unmute_radio_btn_lower_barrel()
        self.fc.swipe_window(direction="up", distance=20)
        self.fc.fd["pen_control"].click_consumer_customize_buttons()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
        assert "Upper barrel button" in self.fc.fd["pen_control"].get_upper_barrel_button_text() , "Upper barrel button is not visible"
        assert self.fc.fd["pen_control"].get_right_click_text_commercial() == "Right-click", "Right-click is not visible"
        assert "Lower barrel button" in self.fc.fd["pen_control"].get_lower_barrel_button_text() , "Lower barrel button is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_erase_text() == "Erase", "Erase is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_customize_button_UI_for_consumer_C43385089(self):
        self.fc.check_and_navigate_to_my_pen_page()   
        self.fc.fd["pen_control"].click_customize_buttons()
        assert "Upper barrel button" in self.fc.fd["pen_control"].get_upper_barrel_button_text() , "Upper barrel button is not visible"
        assert self.fc.fd["pen_control"].get_right_click_text_commercial() == "Right-click", "Right-click is not visible"
        assert "Lower barrel button" in self.fc.fd["pen_control"].get_lower_barrel_button_text() , "Lower barrel button is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_erase_text() == "Erase", "Erase is not visible"  

    @pytest.mark.consumer
    @pytest.mark.function
    def test_10_module_launch_via_deeplink_C55499654(self):
        self.fc.close_myHP()# close app to verify deeplink
        self.fc.launch_module_using_deeplink("hpx://pencontrol")
        time.sleep(20)
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["pen_control"].wait_for_customize_buttons_element()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_11_module_launch_from_windows_settings_C55499655(self):
        self.fc.close_myHP()# close app to verify deeplink
        self.fc.fd["pen_control"].click_more_settings_via_blutooth_devices()
        time.sleep(20)
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["pen_control"].wait_for_customize_buttons_element()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        self.fc.uninstall_app()
        self.fc.fd["pen_control"].click_more_settings_via_blutooth_devices()
        assert bool(self.fc.fd["pen_control"].verify_get_an_app_open_this_hpx_link_popup()) is True, "Get an app to open this hpx link popup is not visible"
        self.fc.fd["pen_control"].click_windows_settings_title_bar()
        self.fc.close_windows_settings_panel()