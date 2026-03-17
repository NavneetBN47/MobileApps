from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Pen_Control_Commercial(object):
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
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_verify_top_buttons_C38252226(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() 
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        assert self.fc.fd["pen_control"].get_single_press_text() == "Single press", "single press title is not found"
        assert self.fc.fd["pen_control"].get_double_press_text() == "Double press", "double press title is not found"
        assert self.fc.fd["pen_control"].get_long_press_text() == "Long press", "long press title is not found"
        
        assert bool(self.fc.fd["pen_control"].verify_single_press_button_show()) is True, "single press button is not visible"
        assert bool(self.fc.fd["pen_control"].verify_double_press_button_show()) is True, "double press button is not visible"
        assert bool(self.fc.fd["pen_control"].verify_long_press_button_show()) is True, "long press button is not visible"
        

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_verify_single_press_action_ui_C38252227(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        assert bool(self.fc.fd["pen_control"].verify_single_press_button_show()) is True, "single press button is not visible"
        actual_single_press_btn_text = self.fc.fd["pen_control"].get_single_press_text_along_with_default_action_commercial()
        assert actual_single_press_btn_text == "MS whiteboard", "Single press text Mismatch"
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        assert self.fc.fd["pen_control"].verify_single_press_side_menu_title_commercial() == "Top button - Single press", "single press title is not visible"
        assert bool(self.fc.fd["pen_control"].verify_ms_white_board_radio_button_is_selected()) == True,"ms white board checkbox is not selected"
        assert self.fc.fd["pen_control"].get_ms_white_board_name_commercial() == actual_single_press_btn_text, "ms white board name is not matching with default action"

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_verify_double_press_action_ui_C38278057(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        assert bool(self.fc.fd["pen_control"].verify_double_press_button_show()) is True, "double press button is not visible"
        actual_double_press_btn_text = self.fc.fd["pen_control"].get_double_press_text_along_with_default_action_commercial()
        assert actual_double_press_btn_text == "Screen snipping", "Screen snipping text Mismatch"
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        assert self.fc.fd["pen_control"].verify_double_press_side_menu_title_commercial() == "Top button - Double press", "double press title is not visible"
        assert bool(self.fc.fd["pen_control"].verify_screen_snipping_radio_button_is_selected()) == True,"screen snipping radio button is not selected"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_in_configure_key_list_show_commercial() == "Screen snipping", "screen snipping name is not matching with default action"

    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_verify_long_press_action_ui_C38282635(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        assert bool(self.fc.fd["pen_control"].verify_long_press_button_show()) is True, "long press button is not visible"
        actual_long_press_btn_text = self.fc.fd["pen_control"].get_long_press_text_along_with_default_action_commercial()
        assert actual_long_press_btn_text == "Sticky notes", "Sticky notes text Mismatch"
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        assert self.fc.fd["pen_control"].verify_long_press_side_menu_title_commercial() == "Top button - Long press", "long press title is not visible"
        assert bool(self.fc.fd["pen_control"].verify_sticky_notes_radio_button_is_selected()) == True,"sticky notes radio button is not selected"
        assert self.fc.fd["pen_control"].get_sticky_notes_text_in_configure_key_list_show_commercial() == "Sticky notes", "screen snipping name is not matching with default action"

    @pytest.mark.commercial
    @pytest.mark.function
    def test_05_verify_single_press_action_list_C38293679(self):
        self.fc.restart_myHP()
        time.sleep(10)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        assert self.fc.fd["pen_control"].verify_single_press_side_menu_title_commercial() == "Top button - Single press", "single press title is not visible"
        assert self.fc.fd["pen_control"].get_page_up_text_commercial() == "Page up", "Page up action item is not visible"
        assert self.fc.fd["pen_control"].get_page_down_text_commercial() == "Page down", "Page down action item is not visible"

        assert self.fc.fd["pen_control"].get_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_text_commercial() == "Touch On/Off", "Touch on/off action is not visible"
        self.fc.fd["pen_control"].scroll_touch_on_off_element_commercial()
        assert self.fc.fd["pen_control"].get_productivity() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_text_commercial() == "Pen menu", "Pen menu action item is not visible"
        assert self.fc.fd["pen_control"].get_disabled_text_commercial() == "Disabled", "Disabled action item is not visible"

        assert self.fc.fd["pen_control"].get_apps() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen snipping action is not visible"
        assert self.fc.fd["pen_control"].get_windows_search__text_commercial() == "Windows search", "Windows search action is not visible"

        assert self.fc.fd["pen_control"].get_media_control() == "Media control", "Media control title is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", "Play/pause action is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track action is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() =="Previous track", "Previous track action is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up action is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down action is not visible"
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio action is not visible"
        

    @pytest.mark.commercial
    @pytest.mark.function
    def test_06_verify_and_click_upper_barrel_image_button_C38282657(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # click restore default button
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(5)
        # verify upper_barrel__image_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel__image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # click upper_barrel_button
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify upper_barrel_button text show
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper barrel button text Mismatch"
        time.sleep(1)
        # verify universal select toggle text show
        assert self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial() == "Universal Select", "Universal Select text Mismatch"
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)


    @pytest.mark.commercial
    @pytest.mark.function
    def test_07_click_and_assign_upper_barrel_button_C38313858(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # click restore default button
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(5)
        # verify upper_barrel__image_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel__image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # click upper_barrel_button
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()

        time.sleep(1)
        #Hover Click toggle switch along with a tooltip icon should be present in the action list.
        assert bool(self.fc.fd["pen_control"].upper_barrel_button_hover_click_toggle_off_is_displayed()) is True, "Hover Click toggle switch is not visible"
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_tool_tip_visible()) is True,"Upper barrel tool tip is not visible"
        assert self.fc.fd["pen_control"].get_productivity() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_universal_select_text_commercial() == "Universal Select", "Universal Select action item is not visible"
        assert self.fc.fd["pen_control"].get_copy_commercial() == "Copy", "Copy action item is not visible"
        assert self.fc.fd["pen_control"].get_paste_commercial() == "Paste", "Paste action item is not visible"
        assert self.fc.fd["pen_control"].get_undo_commercial() == "Undo", "Undo action item is not visible"
        assert self.fc.fd["pen_control"].get_redo_commercial() == "Redo", "Redo action item is not visible"
        #click more link on productivity
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        assert self.fc.fd["pen_control"].get_page_up_commercial() == "Page up", "Page up action item is not visible"
        assert self.fc.fd["pen_control"].get_page_down_commercial() == "Page down", "Page down action item is not visible"
        assert self.fc.fd["pen_control"].get_go_back_commercial() == "Go back", "Go back action item is not visible"
        assert self.fc.fd["pen_control"].get_go_forward_commercial() == "Go forward", "Go forward action item is not visible"
        #click on productivity carrot icon to collapse the list
        self.fc.fd["pen_control"].click_productivity_dd()
        assert self.fc.fd["pen_control"].get_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_erase_text_commercial() == "Erase", "Erase action is not visible"
        assert self.fc.fd["pen_control"].get_right_click_pen_commercial() == "Right click", "Right Click action is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_commercial() == "Touch On/Off", "Touch On/Off action is not visible"
        assert self.fc.fd["pen_control"].get_left_click_commercial() == "Left click", "Left click action is not visible"
        assert self.fc.fd["pen_control"].get_middle_click_commercial() == "Middle click", "Middle click action is not visible"
        #click more link on pen
        self.fc.fd["pen_control"].click_more_button_link_in_pen_mode_commercial()
        assert self.fc.fd["pen_control"].get_fourth_click_commercial() == "Fourth click", "Fourth click action is not visible"
        assert self.fc.fd["pen_control"].get_fifth_click_commercial() == "Fifth click", "Fifth click action is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_commercial() == "Pen menu", "Pen menu action is not visible"
        assert self.fc.fd["pen_control"].get_disabled_commercial() == "Disabled", "Disabled action is not visible"
        #click on pen carrot icon to collapse the list
        self.fc.fd["pen_control"].click_pen_section_dd()
        #App actions
        assert self.fc.fd["pen_control"].get_apps() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_commercial_apps() == "MS whiteboard", "MS whiteboard action is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_commercial_apps() == "Screen snipping", "Screen snipping action is not visible"
        assert self.fc.fd["pen_control"].get_switch_application_commercial() == "Switch application", "Windows search action is not visible"
        assert self.fc.fd["pen_control"].get_web_browser_commercial() == "Web browser", "Web browser action is not visible"
        assert self.fc.fd["pen_control"].get_e_mail_commercial() == "E-mail", "E-mail action is not visible"
        #click more link on apps
        self.fc.fd["pen_control"].click_more_link_on_apps()
        assert self.fc.fd["pen_control"].get_windows_search_commercial() == "Windows search", "Windows search action is not visible"
        #media control list
        assert self.fc.fd["pen_control"].get_media_control() == "Media control", "Media control title is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", "Play/Pause action is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track action is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track action is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up action is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down action is not visible"
        #click more link
        self.fc.fd["pen_control"].click_more_link_on_media()
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio action is not visible"
        #Select any action from the action list--selecting ms white board
        self.fc.fd["pen_control"].click_ms_white_board_toggle_commercial()
        assert self.fc.fd["pen_control"].get_right_click_consumer_btn_pen() == "MS whiteboard", "MS whiteboard action is not visible"



    @pytest.mark.commercial
    @pytest.mark.function
    def test_08_verify_and_click_lower_barrel_image_button_C38313861(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify lower_barrel__image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel__image_button is right click
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # click lower_barrel_button
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify lower_barrel_button text show
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        time.sleep(1)
        # verify erase toggle text show
        assert self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial() == "Erase", "Erase text Mismatch"
        # verify erase toggle is select
        assert self.fc.fd["pen_control"].get_erase_toggle_is_select_commercial() == "1", "Erase toggle is not selected"
        time.sleep(1)
        # click lower_barrel_button to make list disappear
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)


    @pytest.mark.commercial
    @pytest.mark.function
    def test_09_click_more_action_link_C38313865(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify upper_barrel_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify lower_barrel__image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel__image_button is erase
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # click lower_barrel_button
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify lower_barrel_button text show
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        time.sleep(1)
        # verify more button link in pen mode show
        assert self.fc.fd["pen_control"].get_more_button_link_in_pen_mode_show_commercial() == "More", "More text Mismatch"
        time.sleep(3)
        # click more button link in pen mode 
        self.fc.fd["pen_control"].click_more_button_link_in_pen_mode_commercial()
        time.sleep(1)
        # verify fourth click button text show
        assert self.fc.fd["pen_control"].get_fourth_click_button_text_show_commercial() == "Fourth click", "Fourth click text Mismatch"
        time.sleep(1)
        #verify disabled button text show
        assert self.fc.fd["pen_control"].get_disabled_button_text_show_commercial() == "Disabled", "Disabled text Mismatch"
        time.sleep(1)
        # click lower_barrel_button to make list disappear
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
    

    @pytest.mark.commercial
    @pytest.mark.function
    def test_10_click_and_assign_lower_barrel_button_C38313862(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        # verify lower_barrel__image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel__image_button is right click
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # click lower_barrel_button
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        #Hover Click toggle switch along with a tooltip icon should be present in the action list.
        assert bool(self.fc.fd["pen_control"].lower_barrel_button_hover_click_toggle_off_is_displayed()) is True, "Hover Click toggle switch is not visible"
        assert bool(self.fc.fd["pen_control"].verify_lower_barrel_tool_tip_visible()) is True,"Upper barrel tool tip is not visible"
        assert self.fc.fd["pen_control"].get_pen_title() == "Pen", "Pen title is not visible"
        assert self.fc.fd["pen_control"].get_erase_text_commercial() == "Erase", "Erase action is not visible"
        assert self.fc.fd["pen_control"].get_right_click_pen_commercial() == "Right click", "Right Click action is not visible"
        assert self.fc.fd["pen_control"].get_touch_on_off_commercial() == "Touch On/Off", "Touch On/Off action is not visible"
        assert self.fc.fd["pen_control"].get_left_click_commercial() == "Left click", "Left click action is not visible"
        assert self.fc.fd["pen_control"].get_middle_click_commercial() == "Middle click", "Middle click action is not visible"
        #click more link on pen
        self.fc.fd["pen_control"].click_more_button_link_in_pen_mode_commercial()
        assert self.fc.fd["pen_control"].get_fourth_click_commercial() == "Fourth click", "Fourth click action is not visible"
        assert self.fc.fd["pen_control"].get_fifth_click_commercial() == "Fifth click", "Fifth click action is not visible"
        assert self.fc.fd["pen_control"].get_pen_menu_commercial() == "Pen menu", "Pen menu action is not visible"
        assert self.fc.fd["pen_control"].get_disabled_commercial() == "Disabled", "Disabled action is not visible"
        #click on pen carrot icon to collapse the list
        self.fc.fd["pen_control"].click_pen_section_dd()
        #App actions
        assert self.fc.fd["pen_control"].get_apps() == "Apps", "Apps title is not visible"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_commercial_apps() == "MS whiteboard", "MS whiteboard action is not visible"
        assert self.fc.fd["pen_control"].get_screen_snipping_commercial_apps() == "Screen snipping", "Screen snipping action is not visible"
        assert self.fc.fd["pen_control"].get_switch_application_commercial() == "Switch application", "Windows search action is not visible"
        assert self.fc.fd["pen_control"].get_web_browser_commercial() == "Web browser", "Web browser action is not visible"
        assert self.fc.fd["pen_control"].get_e_mail_commercial() == "E-mail", "E-mail action is not visible"
        #click more link on apps
        self.fc.fd["pen_control"].click_more_link_on_apps()
        assert self.fc.fd["pen_control"].get_windows_search_commercial() == "Windows search", "Windows search action is not visible"
        #media control list
        assert self.fc.fd["pen_control"].get_media_control() == "Media control", "Media control title is not visible"
        assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause", "Play/Pause action is not visible"
        assert self.fc.fd["pen_control"].get_next_track_text_commercial() == "Next track", "Next track action is not visible"
        assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track", "Previous track action is not visible"
        assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up", "Volume up action is not visible"
        assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down", "Volume down action is not visible"
        #click more link
        self.fc.fd["pen_control"].click_more_link_on_media()
        assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio", "Mute audio action is not visible"
        assert self.fc.fd["pen_control"].get_productivity() == "Productivity", "Productivity title is not visible"
        assert self.fc.fd["pen_control"].get_universal_select_text_commercial() == "Universal Select", "Universal Select action item is not visible"
        assert self.fc.fd["pen_control"].get_copy_commercial() == "Copy", "Copy action item is not visible"
        assert self.fc.fd["pen_control"].get_paste_commercial() == "Paste", "Paste action item is not visible"
        assert self.fc.fd["pen_control"].get_undo_commercial() == "Undo", "Undo action item is not visible"
        assert self.fc.fd["pen_control"].get_redo_commercial() == "Redo", "Redo action item is not visible"
        #click more link on productivity
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        assert self.fc.fd["pen_control"].get_page_up_commercial() == "Page up", "Page up action item is not visible"
        assert self.fc.fd["pen_control"].get_page_down_commercial() == "Page down", "Page down action item is not visible"
        assert self.fc.fd["pen_control"].get_go_back_commercial() == "Go back", "Go back action item is not visible"
        assert self.fc.fd["pen_control"].get_go_forward_commercial() == "Go forward", "Go forward action item is not visible"
        #click on productivity carrot icon to collapse the list
        #Select any action from the action list--selecting ms white board
        time.sleep(2)
        self.fc.fd["pen_control"].click_ms_white_board_toggle_commercial()
        time.sleep(5)
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "MS whiteboard", "MS whiteboard action is not visible"
