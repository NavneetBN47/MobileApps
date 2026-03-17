from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Trio_Pen_Control_Commercial_02(object):
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
            cls.fc.close_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_click_more_action_link_C42215552(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image Mismatch"
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image Mismatch"
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        assert self.fc.fd["pen_control"].get_more_button_link_in_pen_mode_show_commercial() == "More", "More text Mismatch"
        self.fc.fd["pen_control"].click_more_button_link_in_pen_mode_commercial()
        assert self.fc.fd["pen_control"].get_fourth_click_button_text_show_commercial() == "Fourth click", "Fourth click text Mismatch"
        assert self.fc.fd["pen_control"].get_disabled_button_text_show_commercial() == "Disabled", "Disabled text Mismatch"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_default_pen_name_C42213611(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(7)
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP 705 Rechargeable Multi Pen", "Default pen name text Mismatch"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_pen_controls_ui_C42213587(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control is not show navigation bar"
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(7)
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP 705 Rechargeable Multi Pen", "Default pen name text Mismatch"
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        assert bool(self.fc.fd["pen_control"].verify_info_icon_show_commercial()) is True
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_sensitivity_commercial() == "Pen sensitivity", "Pen sensitivity text Mismatch"
        assert self.fc.fd["pen_control"].get_restore_defaults_button_show_commercial() == "Restore defaults", "Restore defaults text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_sensitivity_image_button_show_commercial() == "Pen Sensitivity Image", "Pen Sensitivity Image text Mismatch"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_pen_name_C42215541(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(7)
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP 705 Rechargeable Multi Pen", "Default pen name text Mismatch"
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        self.fc.fd["pen_control"].enter_device_name("HPXPen")
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        self.fc.fd["pen_control"].enter_device_name("HPXPen@@@"), "Pen name of changed text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        self.fc.fd["pen_control"].enter_device_name("")
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HP 705 Rechargeable Multi Pen", "Pen name of changed text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "Pen", "Pen name of changed text Mismatch"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_action_list_C42215542(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper barrel button text Mismatch"
        assert self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial() == "Universal Select", "Universal Select text Mismatch"
        assert self.fc.fd["pen_control"].get_universal_select_toggle_is_select_commercial() == "1", "Universal Select toggle is not selected"
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        assert bool(self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()) is True, "Pen control defaulr name is not show"
        self.fc.fd["pen_control"].click_pen_control_custom_name_commercial()
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        assert self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial() == "Erase", "Erase text Mismatch"
        assert self.fc.fd["pen_control"].get_erase_toggle_is_select_commercial() == "1", "Erase toggle is not selected"
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        assert bool(self.fc.fd["pen_control"].verify_action_list_not_show_commercial()) is False, "Action list should not show"
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_show_when_configure_key_list_close_commercial()) is True, "Restore button should not show when configure key list open"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_navigation_bar_C42215540(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_defaults_btn()
        time.sleep(7)
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_left_side_commercial() == "Pen", "Default pen name text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP 705 Rechargeable Multi Pen", "Default pen name text Mismatch"
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        self.fc.fd["pen_control"].enter_device_name("HPXPen"), "Pen name of changed text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"


    @pytest.mark.ota
    def test_07_lower_barrel_right_menu_C42215549(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_pen_dd()
        self.fc.fd["pen_control"].click_apps_dropdown()
        self.fc.fd["pen_control"].click_media_control_dropdown()
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_off(),"Lower barrel button hover toggle is not off")
        soft_assertion.assert_true ( self.fc.fd["pen_control"].verify_lower_barrel_tool_tip_visible(), "lower barrel hover info icon is not visible")
        actual_productivity_text=self.fc.fd["pen_control"].get_productivity()
        # --- Productivity section elements ---
        soft_assertion.assert_equal(actual_productivity_text,"Productivity", "Productivity text is not matching")
        actual_universal_text=self.fc.fd["pen_control"].get_universal_select_text_commercial()
        soft_assertion.assert_equal(actual_universal_text, "Universal Select","Universal select text is not matching")
        actual_copy_text=self.fc.fd["pen_control"].get_copy_commercial()
        soft_assertion.assert_equal(actual_copy_text, "Copy", "Copy text is not matching")
        actual_paste_text=self.fc.fd["pen_control"].get_paste_commercial()
        soft_assertion.assert_equal(actual_paste_text, "Paste", "Paste text is not matching")
        actual_undo_text=self.fc.fd["pen_control"].get_undo_commercial()
        soft_assertion.assert_equal(actual_undo_text, "Undo","Undo text is not matching")
        actual_redo_text=self.fc.fd["pen_control"].get_redo_commercial()
        soft_assertion.assert_equal(actual_redo_text, "Redo", "Redo text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        actual_page_up_text=self.fc.fd["pen_control"].get_page_up_commercial()
        soft_assertion.assert_equal(actual_page_up_text, "Page up", "Page up text is not matching")
        actual_page_down_text=self.fc.fd["pen_control"].get_page_down_commercial()
        soft_assertion.assert_equal(actual_page_down_text, "Page down","Page down text is not matching")
        actual_go_back_text=self.fc.fd["pen_control"].get_go_back_commercial()
        soft_assertion.assert_equal(actual_go_back_text, "Go back", "Go back text is not matching")
        actual_go_forward_text=self.fc.fd["pen_control"].get_go_forward_commercial()
        soft_assertion.assert_equal(actual_go_forward_text, "Go forward", "Go forward text is not matching")
        self.fc.fd["pen_control"].click_productivity_dd()
        self.fc.fd["pen_control"].click_pen_dd()
        # --- Pen section elements ---
        actual_pen_title_text=self.fc.fd["pen_control"].get_pen_title()
        soft_assertion.assert_equal(actual_pen_title_text, "Pen", "Pen title text is not matching")
        actual_erase_text=self.fc.fd["pen_control"].get_erase_text_commercial()
        soft_assertion.assert_equal(actual_erase_text, "Erase","Erase text is not matching")
        actual_right_click_btn_text=self.fc.fd["pen_control"].get_right_click_pen_commercial()
        soft_assertion.assert_equal(actual_right_click_btn_text, "Right click", "Right click text is not matching")
        actual_touch_on_off_text=self.fc.fd["pen_control"].get_touch_on_off_commercial()
        soft_assertion.assert_equal(actual_touch_on_off_text, "Touch On/Off","Touch On/Off text is not matching")
        actual_left_click_text=self.fc.fd["pen_control"].get_left_click_commercial()
        soft_assertion.assert_equal(actual_left_click_text, "Left click","Left click text is not matching")
        actual_middle_click_text=self.fc.fd["pen_control"].get_middle_click_commercial()
        soft_assertion.assert_equal(actual_middle_click_text, "Middle click", "Middle click text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_pen()
        actual_fourth_click_text=self.fc.fd["pen_control"].get_fourth_click_commercial()
        soft_assertion.assert_equal(actual_fourth_click_text, "Fourth click", "Fourth click text is not matching")
        actual_fifth_click_text=self.fc.fd["pen_control"].get_fifth_click_commercial()
        soft_assertion.assert_equal(actual_fifth_click_text, "Fifth click", "Fifth click text is not matching")
        actual_pen_menu_text=self.fc.fd["pen_control"].get_pen_menu_commercial()
        soft_assertion.assert_equal(actual_pen_menu_text, "Pen menu", "Pen menu text is not matching")
        actual_disabled_text=self.fc.fd["pen_control"].get_disabled_commercial()
        soft_assertion.assert_equal(actual_disabled_text, "Disabled", "Disabled text is not matching")
        self.fc.fd["pen_control"].click_pen_dd()
        self.fc.fd["pen_control"].click_apps_dropdown()
        # --- Apps section elements ---
        actual_apps_text=self.fc.fd["pen_control"].get_apps()
        soft_assertion.assert_equal(actual_apps_text, "Apps", "Apps title text is not matching")
        actual_ms_whiteboard_text=self.fc.fd["pen_control"].get_ms_whiteboard_commercial_apps()
        soft_assertion.assert_equal(actual_ms_whiteboard_text, "MS whiteboard", "MS whiteboard text is not matching")
        actual_screen_snipping_text=self.fc.fd["pen_control"].get_screen_snipping_commercial_apps()
        soft_assertion.assert_equal(actual_screen_snipping_text, "Screen snipping", "Screen snipping text is not matching")
        actual_switch_application_text=self.fc.fd["pen_control"].get_switch_application_commercial()
        soft_assertion.assert_equal(actual_switch_application_text, "Switch application", "Switch application text is not matching")
        actual_web_browser_text=self.fc.fd["pen_control"].get_web_browser_commercial()
        soft_assertion.assert_equal(actual_web_browser_text, "Web browser", "Web browser text is not matching")
        actual_e_mail_text=self.fc.fd["pen_control"].get_e_mail_commercial()
        soft_assertion.assert_equal(actual_e_mail_text, "E-mail", "E-mail text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_apps()
        time.sleep(2)
        actual_windows_search_text=self.fc.fd["pen_control"].get_windows_search_commercial()
        soft_assertion.assert_equal(actual_windows_search_text, "Windows search", "Windows search text is not matching")
        self.fc.fd["pen_control"].click_apps_dropdown()
        self.fc.fd["pen_control"].click_media_control_dropdown()
        # --- Media control section elements ---
        actual_media_control_text=self.fc.fd["pen_control"].get_media_control()
        soft_assertion.assert_equal(actual_media_control_text, "Media control", "Media control title text is not matching")
        actual_play_pause_text=self.fc.fd["pen_control"].get_play_pause_commercial()
        soft_assertion.assert_equal(actual_play_pause_text, "Play/Pause", "Play/pause text is not matching")
        actual_next_track_text=self.fc.fd["pen_control"].get_next_track_commercial()
        soft_assertion.assert_equal(actual_next_track_text, "Next track", "Next track text is not matching")
        actual_previous_track_text=self.fc.fd["pen_control"].get_previous_track_commercial()
        soft_assertion.assert_equal(actual_previous_track_text, "Previous track", "Previous track text is not matching")
        actual_volume_up_text=self.fc.fd["pen_control"].get_volume_up_commercial()
        soft_assertion.assert_equal(actual_volume_up_text, "Volume up", "Volume up text is not matching")
        actual_volume_down_text=self.fc.fd["pen_control"].get_volume_down_commercial()
        soft_assertion.assert_equal(actual_volume_down_text, "Volume down", "Volume down text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_media()
        actual_mute_audio_text=self.fc.fd["pen_control"].get_mute_audio_commercial()
        soft_assertion.assert_equal(actual_mute_audio_text, "Mute audio", "Mute audio text is not matching")
        self.fc.fd["pen_control"].click_media_control_dropdown()
        self.fc.fd["pen_control"].click_pen_dd()
        # change the lower barrel button default value to left click and verify the same in pen UI
        assert self.fc.fd["pen_control"].get_left_click_toggle_text_show_commercial() == "Left click", "Left click text Mismatch"
        self.fc.fd["pen_control"].click_left_click_toggle_commercial()
        assert self.fc.fd["pen_control"].get_left_click_toggle_is_select_commercial() == "1", "Left click toggle is not selected"
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Left click", "Left click text Mismatch"


    @pytest.mark.ota
    def test_08_upper_barrel_right_menu_C42215545(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_pen_dd()
        self.fc.fd["pen_control"].click_apps_dropdown()
        self.fc.fd["pen_control"].click_media_control_dropdown()
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_off(),"Upper barrel button hover toggle is not off")
        soft_assertion.assert_true ( self.fc.fd["pen_control"].verify_upper_barrel_tool_tip_visible(), "upper barrel hover info icon is not visible")
        # Productivity section elements
        actual_productivity_text=self.fc.fd["pen_control"].get_productivity()
        soft_assertion.assert_equal(actual_productivity_text,"Productivity", "Productivity text is not matching")
        actual_universal_text=self.fc.fd["pen_control"].get_universal_select_text_commercial()
        soft_assertion.assert_equal(actual_universal_text, "Universal Select","Universal select text is not matching")
        actual_copy_text=self.fc.fd["pen_control"].get_copy_commercial()
        soft_assertion.assert_equal(actual_copy_text, "Copy", "Copy text is not matching")
        actual_paste_text=self.fc.fd["pen_control"].get_paste_commercial()
        soft_assertion.assert_equal(actual_paste_text, "Paste", "Paste text is not matching")
        actual_undo_text=self.fc.fd["pen_control"].get_undo_commercial()
        soft_assertion.assert_equal(actual_undo_text, "Undo","Undo text is not matching")
        actual_redo_text=self.fc.fd["pen_control"].get_redo_commercial()
        soft_assertion.assert_equal(actual_redo_text, "Redo", "Redo text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        actual_page_up_text=self.fc.fd["pen_control"].get_page_up_commercial()
        soft_assertion.assert_equal(actual_page_up_text, "Page up", "Page up text is not matching")
        actual_page_down_text=self.fc.fd["pen_control"].get_page_down_commercial()
        soft_assertion.assert_equal(actual_page_down_text, "Page down","Page down text is not matching")
        actual_go_back_text=self.fc.fd["pen_control"].get_go_back_commercial()
        soft_assertion.assert_equal(actual_go_back_text, "Go back", "Go back text is not matching")
        actual_go_forward_text=self.fc.fd["pen_control"].get_go_forward_commercial()
        soft_assertion.assert_equal(actual_go_forward_text, "Go forward", "Go forward text is not matching")
        self.fc.fd["pen_control"].click_productivity_dd()
        self.fc.fd["pen_control"].click_pen_dd()
        # --- Pen section elements ---
        actual_pen_title_text=self.fc.fd["pen_control"].get_pen_title()
        soft_assertion.assert_equal(actual_pen_title_text, "Pen", "Pen title text is not matching")
        actual_erase_text=self.fc.fd["pen_control"].get_erase_text_commercial()
        soft_assertion.assert_equal(actual_erase_text, "Erase","Erase text is not matching")
        actual_right_click_btn_text=self.fc.fd["pen_control"].get_right_click_pen_commercial()
        soft_assertion.assert_equal(actual_right_click_btn_text, "Right click", "Right click text is not matching")
        actual_touch_on_off_text=self.fc.fd["pen_control"].get_touch_on_off_commercial()
        soft_assertion.assert_equal(actual_touch_on_off_text, "Touch On/Off","Touch On/Off text is not matching")
        actual_left_click_text=self.fc.fd["pen_control"].get_left_click_commercial()
        soft_assertion.assert_equal(actual_left_click_text, "Left click","Left click text is not matching")
        actual_middle_click_text=self.fc.fd["pen_control"].get_middle_click_commercial()
        soft_assertion.assert_equal(actual_middle_click_text, "Middle click", "Middle click text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_pen()
        actual_fourth_click_text=self.fc.fd["pen_control"].get_fourth_click_commercial()
        soft_assertion.assert_equal(actual_fourth_click_text, "Fourth click", "Fourth click text is not matching")
        actual_fifth_click_text=self.fc.fd["pen_control"].get_fifth_click_commercial()
        soft_assertion.assert_equal(actual_fifth_click_text, "Fifth click", "Fifth click text is not matching")
        actual_pen_menu_text=self.fc.fd["pen_control"].get_pen_menu_commercial()
        soft_assertion.assert_equal(actual_pen_menu_text, "Pen menu", "Pen menu text is not matching")
        actual_disabled_text=self.fc.fd["pen_control"].get_disabled_commercial()
        soft_assertion.assert_equal(actual_disabled_text, "Disabled", "Disabled text is not matching")
        self.fc.fd["pen_control"].click_pen_dd()
        self.fc.fd["pen_control"].click_apps_dropdown()
        # --- Apps section elements ---
        actual_apps_text=self.fc.fd["pen_control"].get_apps()
        soft_assertion.assert_equal(actual_apps_text, "Apps", "Apps title text is not matching")
        actual_ms_whiteboard_text=self.fc.fd["pen_control"].get_ms_whiteboard_commercial_apps()
        soft_assertion.assert_equal(actual_ms_whiteboard_text, "MS whiteboard", "MS whiteboard text is not matching")
        actual_screen_snipping_text=self.fc.fd["pen_control"].get_screen_snipping_commercial_apps()
        soft_assertion.assert_equal(actual_screen_snipping_text, "Screen snipping", "Screen snipping text is not matching")
        actual_switch_application_text=self.fc.fd["pen_control"].get_switch_application_commercial()
        soft_assertion.assert_equal(actual_switch_application_text, "Switch application", "Switch application text is not matching")
        actual_web_browser_text=self.fc.fd["pen_control"].get_web_browser_commercial()
        soft_assertion.assert_equal(actual_web_browser_text, "Web browser", "Web browser text is not matching")
        actual_e_mail_text=self.fc.fd["pen_control"].get_e_mail_commercial()
        soft_assertion.assert_equal(actual_e_mail_text, "E-mail", "E-mail text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_apps()
        time.sleep(2)
        actual_windows_search_text=self.fc.fd["pen_control"].get_windows_search_commercial()
        soft_assertion.assert_equal(actual_windows_search_text, "Windows search", "Windows search text is not matching")
        self.fc.fd["pen_control"].click_apps_dropdown()
        self.fc.fd["pen_control"].click_media_control_dropdown()
        # --- Media control section elements ---
        actual_media_control_text=self.fc.fd["pen_control"].get_media_control()
        soft_assertion.assert_equal(actual_media_control_text, "Media control", "Media control title text is not matching")
        actual_play_pause_text=self.fc.fd["pen_control"].get_play_pause_commercial()
        soft_assertion.assert_equal(actual_play_pause_text, "Play/Pause", "Play/pause text is not matching")
        actual_next_track_text=self.fc.fd["pen_control"].get_next_track_commercial()
        soft_assertion.assert_equal(actual_next_track_text, "Next track", "Next track text is not matching")
        actual_previous_track_text=self.fc.fd["pen_control"].get_previous_track_commercial()
        soft_assertion.assert_equal(actual_previous_track_text, "Previous track", "Previous track text is not matching")
        actual_volume_up_text=self.fc.fd["pen_control"].get_volume_up_commercial()
        soft_assertion.assert_equal(actual_volume_up_text, "Volume up", "Volume up text is not matching")
        actual_volume_down_text=self.fc.fd["pen_control"].get_volume_down_commercial()
        soft_assertion.assert_equal(actual_volume_down_text, "Volume down", "Volume down text is not matching")
        self.fc.fd["pen_control"].click_more_link_on_media()
        actual_mute_audio_text=self.fc.fd["pen_control"].get_mute_audio_commercial()
        soft_assertion.assert_equal(actual_mute_audio_text, "Mute audio", "Mute audio text is not matching")
        self.fc.fd["pen_control"].click_media_control_dropdown()
        self.fc.fd["pen_control"].click_pen_dd()
        # change the upper barrel button default value to left click and verify the same in pen UI
        assert self.fc.fd["pen_control"].get_left_click_toggle_text_show_commercial() == "Left click", "Left click text Mismatch"
        self.fc.fd["pen_control"].click_left_click_toggle_commercial()
        assert self.fc.fd["pen_control"].get_left_click_toggle_is_select_commercial() == "1", "Left click toggle is not selected"
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Left click", "Left click text Mismatch"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_action_list_ui_C42215543(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion = SoftAssert()
        # ---Verify lower barrel toggle button---
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_lower_barrel_button_hover_toggle_off(),"Lower barrel button hover toggle is not off")
        soft_assertion.assert_true ( self.fc.fd["pen_control"].verify_lower_barrel_tool_tip_visible(), "lower barrel hover info icon is not visible")
        # ---Verify lower barrel section---
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_btn(),"Lower barrel button","Lower barrel title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        self.fc.fd["pen_control"].click_pen_dd()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        self.fc.fd["pen_control"].click_apps_dropdown()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        self.fc.fd["pen_control"].click_media_control_dropdown()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        # ---Verify upper barrel toggle button---
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_upper_barrel_button_hover_toggle_off(),"Upper barrel button hover toggle is not off")
        soft_assertion.assert_true ( self.fc.fd["pen_control"].verify_upper_barrel_tool_tip_visible(), "upper barrel hover info icon is not visible")
        # ---Verify upper barrel section---
        self.fc.fd["pen_control"].click_pen_dd()
        self.fc.fd["pen_control"].click_apps_dropdown()
        self.fc.fd["pen_control"].click_media_control_dropdown()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_btn_right_click(), "Upper barrel button", "upper barrel title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_10_info_icon_desc_C42214975(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
           self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() 
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(5)
        self.fc.fd["pen_control"].verify_info_icon()
        self.fc.fd["pen_control"].click_info_icon()
        time.sleep(5)
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_presenceof_productnumber_tooltip(), "Product number tooltip is not shown")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_product_number_copy_icon(), "Product number copy icon is not visible")
        self.fc.fd["pen_control"].verify_presenceof_serialnumber_tooltip()
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_serial_number_copy_icon(), "Serial number copy icon is not visible")
        self.fc.fd["pen_control"].verify_presenceof_firmware_tooltip()
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_firmware_copy_icon(), "firmware icon is not visible")
        soft_assertion.raise_assertion_errors()


    @pytest.mark.ota
    def test_11_launch_via_deeplink_C48981049(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pencontrol")
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_pen_is_selected_from_navbar()), "pen is not selected from navbar")
        soft_assertion.raise_assertion_errors()
