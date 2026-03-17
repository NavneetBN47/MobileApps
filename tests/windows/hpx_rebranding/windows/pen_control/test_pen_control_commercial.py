import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_UI(object):

    def scroll_to_top_and_get_current_assignment(self, button):
    # Workaround for intermittent UI issue:
    # Occasionally, the page fails to scroll back to the top and only blinks without changing position.
    # When this happens, the only reliable way to reach the top is to relaunch the app and re-navigate to the page.
    # This snippet first attempts to scroll to the top and verifies the position.
    # If the scroll fails, it relaunches the app and navigates back to the same page.
        time.sleep(2)
        self.fc.swipe_to_top()  # Scroll to top first
        if not self.fc.fd["pen_control"].get_current_assignment():  # See if current assignment shows up. If not , relaunch app
            self.fc.close_myHP()
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_customize_buttons_page()
            if button == "top_button_single_press":
                self.fc.fd["pen_control"].click_single_press_button_commercial()
            elif button == "upper_barrel_button":
                self.fc.fd["pen_control"].click_customize_upper_barrel_button()
            elif button == "lower_barrel_button":
                self.fc.fd["pen_control"].click_lower_barrel_button_commercial()
        return getattr(self.fc.fd["pen_control"], f"get_{button}_current_assignment_value")()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_customize_button_ui_C44225283(self):
        self.fc.check_and_navigate_to_my_pen_page()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()

        # Verify Pen -> Customize buttons page titles and values
        assert "Upper barrel button" in self.fc.fd["pen_control"].get_upper_barrel_button_text(), "Upper barrel button is not visible"
        assert "Universal select" in self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page(), "Universal select action with arrow is not visible"
        assert "Lower barrel button" in self.fc.fd["pen_control"].get_lower_barrel_button_text(), "Lower barrel button is not visible"
        assert "Erase" in self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page(), "Erase action with arrow is not visible"
        assert "Top button - Single press" in self.fc.fd["pen_control"].get_top_button_single_press_right_arrow(), "Top button - Single press is not visible"
        assert "MS Whiteboard" in self.fc.fd["pen_control"].get_pen_control_customize_btn_top_btn_single_press_action_ltwo_page(), "MS whiteboard action with arrow is not visible"
        assert "Top button - Double press" in self.fc.fd["pen_control"].get_top_button_double_press_text(), "Top button - Double press is not visible"
        assert "Screen snipping" in self.fc.fd["pen_control"].get_pen_control_customize_btn_screen_snipping_action_ltwo_page(), "Screen snipping is not visible"
        assert "Top button - Long press" in self.fc.fd["pen_control"].get_top_button_long_press_text(), "Top button - Long press is not visible"
        assert "Quick note" in self.fc.fd["pen_control"].get_pen_control_customize_btn_top_btn_long_press_action_ltwo_page(), "Quick note action with arrow is not visible"
        assert self.fc.fd["pen_control"].get_customize_buttons_restore_default_button_text() == "Restore defaults", "Restore Defaults button is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_upper_barrel_button_ui_C44225284(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()

        # Verify Pen -> Upper barrel button headers
        assert self.fc.fd["pen_control"].get_upper_barrel_button_ltwo_page_title() == "Upper barrel button", "Upper barrel button title is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_hover_click_toggle_lthree_page() == "0", "hover-click toggle not in off state"
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_universal_select_lthree_page() == "Universal select", "Universal select is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_lower_barrel_button_ui_C44225285(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_lower_barrel_button_commercial()

        # Verify Pen -> Lower barrel button page headers
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_title_text_lthree_page() == "Lower barrel button", "Lower barrel button title is not visible"
        assert self.fc.fd["pen_control"].get_lowerbarrel_hover_click_toggle_state_lthree_page() == "0", "hover-click toggle not in off state"
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_erase_text() == "Erase", "Erase is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_lower_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_lower_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_lower_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_top_button_single_press_ui_C44225286(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_single_press_button_commercial()

        # Verify Pen -> Top button - Single Press page headers
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_top_btn_single_press_title_text_lthree_page() == "Top button - Single press", "Top button - Single press title is not visible"
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_top_button_single_press_ms_whiteboard_text() == "MS Whiteboard", "MS whiteboard is not visible"
        assert self.fc.fd["pen_control"].get_top_button_single_press_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_top_button_single_press_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_top_button_single_press_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_single_press_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_top_button_double_press_ui_C44225287(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_double_press_button_commercial()

        # Verify Pen -> Top button - Double Press page headers
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_top_btn_double_press_title_text_lthree_page() == "Top button - Double press", "Top button - Double press title is not visible"
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_top_button_double_press_screen_snipping_text() == "Screen snipping", "Screen snipping is not visible"
        assert self.fc.fd["pen_control"].get_top_button_double_press_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_top_button_double_press_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_top_button_double_press_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_double_press_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_top_button_long_press_ui_C44225288(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_long_press_button_commercial()

        # Verify Pen -> Top button - Long Press page headers
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_top_btn_long_press_title_text_lthree_page() == "Top button - Long press", "Top button - Long press title is not visible"
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_top_button_long_press_quick_note_text() == "Quick note", "Quick note is not visible"
        assert self.fc.fd["pen_control"].get_top_button_long_press_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_top_button_long_press_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["pen_control"].get_top_button_long_press_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"

        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_long_press_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_top_button_single_press_button_action_list_ui_C43124469(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()        
        self.fc.fd["pen_control"].click_single_press_button_commercial()

        # Verify Top Button - Single Press -> Productivity section titles
        assert self.fc.fd["pen_control"].verify_single_press_side_menu_title_commercial() == "Top button - Single press", "Top button - Single press title is not visible"
        assert self.fc.fd["pen_control"].get_top_button_single_press_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_page_up_text_commercial() == "Page up", "Page up action item is not visible"
        assert self.fc.fd["pen_control"].get_page_down_text_commercial() == "Page down", "Page down action item is not visible"

        # Verify Top Button - Single Press -> Pen section titles
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["pen_control"].get_top_button_single_press_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_text_commercial() == "Touch on/off", "Touch on/off action is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_text_commercial() == "Pen menu", "Pen menu action item is not visible"
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled action item is not visible"

        # Verify Top Button - Single Press -> Apps section titles
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_app_consumer")
        assert self.fc.fd["pen_control"].get_top_button_single_press_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen snipping action is not visible"
        assert self.fc.fd["pen_control"].get_windows_search_text_commercial() == "Windows search", "Windows search action is not visible"
        assert self.fc.fd["pen_control"].get_top_button_long_press_sticky_notes_text() == "Sticky notes", "Sticky notes action is not visible"
        assert self.fc.fd["pen_control"].get_open_app_text_commercial() == "Open app", "Open app is not visible"
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        assert self.fc.fd["pen_control"].get_onenote_text_commercial() == "OneNote", "OneNote app is not viisble"
        assert self.fc.fd["pen_control"].get_top_button_long_press_quick_note_text() == "Quick note", "Quick note is not visible"

        # Verify Top Button - Single Press -> Media Control section titles
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_top_button_single_press")
        assert self.fc.fd["pen_control"].get_top_button_single_press_media_control_title() == "Media control", "Media control title is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", "Play/pause action is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track action is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() =="Previous track", "Previous track action is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up action is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_top_button_single_press")
        self.fc.fd["pen_control"].click_more_link_top_button_single_press()
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down action is not visible"
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio action is not visible"

        #click mute audio radio btn and verify this action should be current assignment in top button single press
        self.fc.fd["pen_control"].click_pen_control_customize_btn_top_btn_single_press_mute_audio_radio_btn_lthree_page()
        current_assignment = self.scroll_to_top_and_get_current_assignment("top_button_single_press")
        assert current_assignment == "Mute audio", f"[Top button - Single press] Current Assignment mismatch: expected 'Mute audio', got '{current_assignment}'"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_upper_barrel_button_action_list_C43124458(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()           
        
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        # Verify Upper Barrel Button -> Productivity section titles
        assert self.fc.fd["pen_control"].get_upper_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_productivity_universal_select_text_lthree_page() == "Universal select", "Universal Select text is not visible under productivity"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_radial_menu_text() == "Radial menu", "Radial menu is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "Paste is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_undo_text() == "Undo", "Undo is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_copy_text() == "Copy", "Copy is not visible"
        self.fc.fd["pen_control"].click_more_link_on_productivity_button()
        time.sleep(5)
        self.fc.fd["pen_control"].scroll_down_to_element("customize_upper_barrel_button_go_forward")
        assert self.fc.fd["pen_control"].get_upper_barrel_button_redo_text() == "Redo", "Redo is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_up_text() == "Page up", "Page up is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_down_text() == "Page down", "Page down is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_go_back_text() == "Go back", "Go back is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_go_forward_text() == "Go forward", "Go forward is not visible"

        # Click on Undo radio button and verify that the current assignment now shows Undo
        self.fc.fd["pen_control"].click_undo_radio_btn_upper_barrel()
        self.fc.swipe_to_top()
        current_assignment = self.fc.fd["pen_control"].get_upper_barrel_button_current_assignment_value()
        assert current_assignment == "Undo", f"[Upper Barrel Button] Current Assignment mismatch: expected 'Undo', got '{current_assignment}'"

        # Verify Upper Barrel Button -> Pen section titles
        self.fc.swipe_window(direction="down", distance=12)  #From top, scroll fast and then scroll to element
        self.fc.fd["pen_control"].scroll_down_to_element("customize_upper_barrel_button_left_click")
        assert self.fc.fd["pen_control"].get_upper_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_text_commercial() == "Touch on/off", "Touch on/off is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_right_click_text() == "Right click", "Right click is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_left_click_text() == "Left click", "Left click is not visible"
        self.fc.fd["pen_control"].click_more_link_on_productivity_button()
        assert self.fc.fd["pen_control"].get_upper_barrel_button_middle_click_text() == "Middle click", "Middle click is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_fourth_click_text() == "Fourth click", "Fourth click is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("customize_upper_barrel_button_fifth_click")
        assert self.fc.fd["pen_control"].get_upper_barrel_button_fifth_click_text() == "Fifth click", "Fifth click is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_text_commercial() == "Pen menu", "Pen menu is not visible"
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled is not visible"

        # Click on Fourth click radio button and verify that the current assignment now shows Fourth click
        self.fc.fd["pen_control"].click_upper_barrel_button_fourth_click_text()
        time.sleep(2)
        self.fc.swipe_to_top()
        current_assignment = self.fc.fd["pen_control"].get_upper_barrel_button_current_assignment_value()
        assert current_assignment == "Fourth click", f"[Upper Barrel Button] Current Assignment mismatch: expected 'Fourth click', got '{current_assignment}'"

        # Verify Upper Barrel Button -> Apps section titles
        self.fc.swipe_window(direction="down", distance=20) #From top, scroll fast and then scroll to element
        self.fc.fd["pen_control"].scroll_down_to_element("customize_top_button_single_press_switch_application")
        assert self.fc.fd["pen_control"].get_upper_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_windows_search_text_commercial() == "Windows search", "Windows search is not visible"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_text_commercial() == "MS Whiteboard", "MS Whiteboard is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen snipping is not visible"
        assert self.fc.fd["pen_control"].get_switch_application_text_commercial() == "Switch application", "Switch application is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("web_browser_text_commercial")
        assert self.fc.fd["pen_control"].get_web_browser_text_commercial() == "Web browser", "Web browser is not visible"
        self.fc.fd["pen_control"].click_more_link_on_productivity_button()
        self.fc.fd["pen_control"].scroll_down_to_element("open_app_text_commercial")
        assert self.fc.fd["pen_control"].get_email_text_commercial() == "E-mail", "E-mail is not visible"
        assert self.fc.fd["pen_control"].get_open_app_text_commercial() == "Open app", "Open app is not visible"
       
        # Click on E-mail radio button and verify that the current assignment now shows E-mail
        self.fc.fd["pen_control"].click_email_text_commercial()
        self.fc.swipe_to_top()
        current_assignment = self.scroll_to_top_and_get_current_assignment("upper_barrel_button")
        assert current_assignment == "E-mail", f"[Upper Barrel Button] Current Assignment mismatch: expected 'E-mail', got '{current_assignment}'"

        # Verify Upper Barrel Button -> Media control section titles
        self.fc.swipe_window(direction="down", distance=24) #From top, scroll fast and then scroll to element
        self.fc.fd["pen_control"].scroll_down_to_element("previous_track_text_commercial")
        assert self.fc.fd["pen_control"].get_upper_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", " Play/Pause is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("previous_track_text_commercial")
        self.fc.fd["pen_control"].click_more_link_on_productivity_button()
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible"

        # Click on Mute audio radio button and verify that the current assignment now shows Mute audio
        self.fc.fd["pen_control"].click_mute_audio_text_commercial()
        current_assignment = self.scroll_to_top_and_get_current_assignment("upper_barrel_button")
        assert current_assignment == "Mute audio", f"[Upper Barrel Button] Current Assignment mismatch: expected 'Mute audio', got '{current_assignment}'"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_lower_barrel_button_action_list_C43124467(self):
        self.fc.check_and_navigate_to_customize_buttons_page()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
        self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
        self.fc.fd["pen_control"].click_lower_barrel_button_commercial()

        # Verify Lower Barrel Button -> Productivity section titles
        assert self.fc.fd["pen_control"].get_current_assignment() == "Current assignment", "Current assignment is not visible"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_productivity_title() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_productivity_arrow_icon() == "Productivity Chevron Down", "Productivity Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_productivity_universal_select_text_lthree_page() == "Universal select", "Universal Select is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_radial_menu_text() == "Radial menu", "Radial menu is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "Paste is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_undo_text() == "Undo", "Undo is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_copy_text() == "Copy", "Copy is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_productivity_lower_barrel")
        self.fc.fd["pen_control"].click_more_link_on_productivity_button_lower_barrel()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_redo_text() == "Redo", "Redo is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_up_text() == "Page up", "Page up is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_page_down_text() == "Page down", "Page down is not visible"
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["pen_control"].get_upper_barrel_button_go_back_text() == "Go back", "Go back is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_go_forward_text() == "Go forward", "Go forward is not visible"

        # Verify Lower Barrel Button -> Pen section titles
        self.fc.fd["pen_control"].scroll_down_to_element("lower_barrel_button_pen_title")
        assert self.fc.fd["pen_control"].get_lower_barrel_button_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_pen_arrow_icon() == "Pen Chevron Down", "Pen Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_text_commercial() == "Touch on/off", "Touch on/off is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("customize_upper_barrel_button_right_click")
        assert self.fc.fd["pen_control"].get_upper_barrel_button_right_click_text() == "Right click", "Right click is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_left_click_text() == "Left click", "Left click is not visible"
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["pen_control"].click_more_link_on_productivity_button_lower_barrel()
        assert self.fc.fd["pen_control"].get_upper_barrel_button_middle_click_text() == "Middle click", "Middle click is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_fourth_click_text() == "Fourth click", "Fourth click is not visible"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_fifth_click_text() == "Fifth click", "Fifth click is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_text_commercial() == "Pen menu", "Pen menu is not visible"
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled is not visible"

        # Verify Lower Barrel Button -> Apps section titles   
        self.fc.fd["pen_control"].scroll_down_to_element("lower_barrel_button_apps_title")
        assert self.fc.fd["pen_control"].get_lower_barrel_button_apps_title() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_apps_arrow_icon() == "Apps Chevron Down", "Apps Arrow Icon is not visible"
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_productivity_lower_barrel")
        assert self.fc.fd["pen_control"].get_windows_search_text_commercial() == "Windows search", "Windows search is not visible"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_text_commercial() == "MS Whiteboard", "MS whiteboard is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen snipping is not visible"
        assert self.fc.fd["pen_control"].get_switch_application_text_commercial() == "Switch application", "Switch application is not visible"
        assert self.fc.fd["pen_control"].get_web_browser_text_commercial() == "Web browser", "Web browser is not visible"
        self.fc.fd["pen_control"].click_more_link_on_productivity_button_lower_barrel()
        time.sleep(2)
        self.fc.fd["pen_control"].scroll_down_to_element("open_app_text_commercial")
        assert self.fc.fd["pen_control"].get_email_text_commercial() == "E-mail", "E-mail is not visible"
        assert self.fc.fd["pen_control"].get_open_app_text_commercial() == "Open app", "Open app is not visible"
        self.fc.fd["pen_control"].click_pen_control_customize_btn_lower_barrel_btn_apps_email_action_lthree_page()

        # Verify Lower Barrel Button -> Media control section titles
        self.fc.fd["pen_control"].scroll_down_to_element("more_link_on_productivity_lower_barrel")
        assert self.fc.fd["pen_control"].get_lower_barrel_button_media_control_title() == "Media control", "Media control title  is not visible"
        assert self.fc.fd["pen_control"].get_media_control_arrow_icon() == "Media control Chevron Down", "Media control Arrow Icon is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", " Play/Pause is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down is not visible"
        self.fc.fd["pen_control"].click_more_link_on_productivity_button_lower_barrel()
        time.sleep(5)
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio is not visible"

        # Click on Mute audio radio button and verify that the current assignment now shows Mute audio
        self.fc.fd["pen_control"].click_pen_control_customize_btn_lower_barrel_btn_media_control_mute_audio_action_lthree_page()
        current_assignment = self.scroll_to_top_and_get_current_assignment("lower_barrel_button")
        assert current_assignment == "Mute audio", f"[Lower Barrel Button] Current Assignment mismatch: expected 'Mute audio', got '{current_assignment}'"
