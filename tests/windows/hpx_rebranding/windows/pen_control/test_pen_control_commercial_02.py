import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_UI(object):

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_top_button_double_press_button_action_list_C43124471(self):
        self.fc.check_and_navigate_to_my_pen_page()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button() 
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen snipping is not visible"
        assert self.fc.fd["pen_control"].get_top_button_double_press_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_up_text() == "Page up", "Page up is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_down_text() == "Page down", "Page down is not visible"
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_double_press_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_text_commercial() == "Touch on/off", "Touch on/off is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_text_commercial() == "Pen menu", "Pen menu is not visible"
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled is not visible"
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_double_press_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_text_commercial() == "MS Whiteboard", "MS whiteboard is not visible"
        assert bool(self.fc.fd["pen_control"].verify_pen_control_top_btn_double_press_screen_snipping_action_lthree_page()) is True, "Screen snipping is not visible"
        assert self.fc.fd["pen_control"].get_windows_search_text_commercial() == "Windows search", "Windows search is not visible"
        assert self.fc.fd["pen_control"].get_top_button_long_press_sticky_notes_text() == "Sticky notes", "Sticky notes is not visible"
        assert self.fc.fd["pen_control"].get_open_app_text_commercial() == "Open app", "Open app is not visible"
        self.fc.fd["pen_control"].click_customize_button_windows_search_text()
        self.fc.fd["pen_control"].scroll_down_to_element("volume_down_text_commercial")
        self.fc.fd["pen_control"].click_more_link_top_button_double_press()
        assert self.fc.fd["pen_control"].get_top_button_double_press_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", " Play/Pause is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
        self.fc.swipe_window(direction="down", distance=12)
        self.fc.fd["pen_control"].click_more_link_top_button_double_press()
        time.sleep(5)
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible"
        self.fc.fd["pen_control"].click_pen_control_top_btn_double_press_media_control_mute_audio_action_lthree_page()
        time.sleep(2)
        self.fc.swipe_to_top()
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible in Current Assignment"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_more_action_link_C53060071(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_universal_select_lthree_page() == "Universal select", "Universal Select is not visible"
        self.fc.fd["pen_control"].click_pencontrol_upper_barrel_btn_prod_radial_menu()  
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["pen_control"].click_more_link_on_productivity_button()
        time.sleep(5)
        self.fc.fd["pen_control"].scroll_to_element("pencontrol_name_prod_radial_goforward")
        assert self.fc.fd["pen_control"].get_pencontrol_name_prod_radial_redo() == "Redo", "Redo is not visible"
        assert self.fc.fd["pen_control"].get_pencontrol_name_prod_page_up() == "Page up", "Page up is not visible"
        assert self.fc.fd["pen_control"].get_pencontrol_name_prod_radial_pagedown() == "Page down", "Page down is not visible"
        assert self.fc.fd["pen_control"].get_pencontrol_name_prod_radial_goback() == "Go back", "Go back is not visible"
        assert self.fc.fd["pen_control"].get_pencontrol_name_prod_radial_goforward() == "Go forward", "Go forward is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_restore_defaults_customize_buttons_C43124474(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
        self.fc.fd["pen_control"].click_pencontrol_upper_barrel_btn_prod_radial_menu()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Upper barrel button" in self.fc.fd["pen_control"].get_upper_barrel_button_text(), "Upper barrel button is not visible"
        self.fc.fd["pen_control"].click_lower_barrel_button_commercial()
        self.fc.fd["pen_control"].click_pencontrol_lower_barrel_btn_prod_paste()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Lower barrel button" in self.fc.fd["pen_control"].get_lower_barrel_button_text(), "Lower barrel button is not visible"
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        self.fc.fd["pen_control"].click_pencontrol_topbutton_singlepress_row()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Top button - Single press" in self.fc.fd["pen_control"].get_top_button_single_press_text(), "Top button - Single press is not visible"
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        self.fc.fd["pen_control"].click_pencontrol_topbutton_doublepress_row()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Top button - Double press" in self.fc.fd["pen_control"].get_top_button_double_press_text(), "Top button - Double press is not visible"
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        self.fc.fd["pen_control"].click_pencontrol_topbutton_longpress_row()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Top button - Long press" in self.fc.fd["pen_control"].get_top_button_long_press_text(), "Top button - Long press is not visible"
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
        assert self.fc.fd["pen_control"].get_customize_buttons_restore_default_button_text() == "Restore defaults", "Restore Defaults button is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_different_actions_in_the_Dropdown_list_C53020024(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Upper barrel button" in self.fc.fd["pen_control"].get_upper_barrel_button_text(), "Upper barrel button is not visible"
        self.fc.fd["pen_control"].click_lower_barrel_button_commercial()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Lower barrel button" in self.fc.fd["pen_control"].get_lower_barrel_button_text(), "Lower barrel button is not visible"
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Top button - Single press" in self.fc.fd["pen_control"].get_top_button_single_press_text(), "Top button - Single press is not visible"
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Top button - Double press" in self.fc.fd["pen_control"].get_top_button_double_press_text(), "Top button - Double press is not visible"
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Top button - Long press" in self.fc.fd["pen_control"].get_top_button_long_press_text(), "Top button - Long press is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_top_button_long_press_button_action_list_C43124473(self):
        self.fc.check_and_navigate_to_customize_buttons_page()        
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button() 
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        assert self.fc.fd["pen_control"].get_top_button_long_press_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_up_text() == "Page up", "Page up is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_down_text() == "Page down", "Page down is not visible"
        self.fc.fd["pen_control"].click_customize_button_page_up_text()
        self.fc.swipe_window(direction="up", distance=10)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_up_text() == "Page up", "Page up is not visible"
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_long_press_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_text_commercial() == "Touch on/off", "Touch on/off is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_text_commercial() == "Pen menu", "Pen menu is not visible"
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled is not visible"
        self.fc.fd["pen_control"].click_customize_button_disabled_text()
        self.fc.fd["pen_control"].scroll_to_element("disabled_text_commercial")
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled is not visible"
        self.fc.swipe_window(direction="down", distance=8)
        assert self.fc.fd["pen_control"].get_top_button_long_press_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_text_commercial() == "MS Whiteboard", "MS Whiteboard is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen snipping is not visible"
        assert self.fc.fd["pen_control"].get_windows_search_text_commercial() == "Windows search", "Windows search is not visible"
        assert self.fc.fd["pen_control"].get_top_button_long_press_sticky_notes_text() == "Sticky notes", "Sticky notes is not visible"
        assert self.fc.fd["pen_control"].get_open_app_text_commercial() == "Open app", "Open app is not visible"
        self.fc.fd["pen_control"].click_pen_control_top_btn_double_press_media_control_quick_note_action_lthree_page()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=18)
        assert self.fc.fd["pen_control"].get_top_button_long_press_quick_note_text() == "Quick note", "Windows search is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("top_button_long_press_media_control_title")
        assert self.fc.fd["pen_control"].get_top_button_long_press_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", " Play/Pause is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("next_track_text_commercial")
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_top_button_long_press")
        self.fc.fd["pen_control"].click_more_link_top_button_long_press()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible"
        self.fc.fd["pen_control"].click_pen_control_customize_btn_top_btn_long_press_media_control_mute_action_lthree_page()
        time.sleep(2)
        self.fc.close_myHP() # workaround. After choosing Media Control -> Mute action, scrolling to top doesn't work consistently. Only way to get to top is to relaunch app. 
        self.fc.launch_myHP()
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible"
        self.fc.fd["pen_control"].click_customize_back_button()
        self.fc.fd["pen_control"].click_customize_back_button()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_default_radial_menu_values_C44606948(self):
        self.fc.check_and_navigate_to_my_pen_page()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        self.fc.fd["pen_control"].click_radial_menu_buttons()
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track is not visible"
        assert self.fc.fd["pen_control"].get_web_browser_text_commercial() == "Web browser", "Web browser is not visible"
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible"
        assert self.fc.fd["pen_control"].get_email_text_commercial() == "E-mail", "E-mail is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        self.fc.fd["pen_control"].scroll_to_element("play_pause_text_commercial")
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", " Play/Pause is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_moonracer_pen_commercial_C52235899(self):
        self.fc.check_and_navigate_to_my_pen_page()
        assert self.fc.fd["pen_control"].get_hp_rechargeable_active_pen_g3pencontrol() == "HP Rechargeable Active Pen G3", "HP Rechargeable Active Pen G3 is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_pen_sensitivity_ui_C44262364(self):
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        self.fc.fd["pen_control"].click_pen_sensitivity_card()
        assert self.fc.fd["pen_control"].get_pressure_sensitivity_text() == "Pressure", "Pressure is not visible"
        assert self.fc.fd["pen_control"].get_pressure_low_sensitivity_text() == "Pressure Low", "Pressure Low is not visible"
        assert self.fc.fd["pen_control"].get_pressure_high_sensitivity_text() == "Pressure High", "Pressure High is not visible"
        assert self.fc.fd["pen_control"].get_tilt_sensitivity_text() == "Tilt", "Tilt is not visible"
        assert self.fc.fd["pen_control"].get_tilt_narrow_sensitivity_text() == "Pen Tilt Angle Narrow", "Pen Tilt Angle Narrow is not visible"
        assert self.fc.fd["pen_control"].get_tilt_wide_sensitivity_text() == "Pen Tilt Angle Wide", "Pen Tilt Angle Wide is not visible"
        assert self.fc.fd["pen_control"].get_pen_sensitivity_restore_defaults_btn_text() == "Restore defaults", "Restore Defaults button is not visible"

    @pytest.mark.function
    def test_09_module_launch_via_deeplink_C53020052(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pencontrol")
        time.sleep(5) # Give app chance to launch
        assert self.fc.fd["pen_control"].verify_customize_buttons(), "Pen Control is not launched via deeplink"