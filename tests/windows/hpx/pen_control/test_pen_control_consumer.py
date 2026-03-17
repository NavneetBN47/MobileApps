from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Pen_Control_Consumer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
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
            time.sleep(2)
            cls.fc.launch_myHP()
        time.sleep(5)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_pen_control_support_system_C38422179(self):
        time.sleep(2)
        self.fc.restart_myHP()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()

        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_default_pen_name()) is True, "Pen control name is not visible"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_lower_barrel_highlighted_value_C38494085(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_lower_barrel_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        self.fc.fd["pen_control"].click_erase_btn_consumer()
        side_menu_lower_barrel_selected_text_value = self.fc.fd["pen_control"].get_erase_btn_consumer()
        assert self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_is_selected() == "1", "Lower barrel erase radion is not selected"
        assert pen_lower_barrel_text == side_menu_lower_barrel_selected_text_value, "Lower barrel text Mismatch"


    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_03_verify_upper_barrel_highlighted_value_C38494082(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_upper_barrel_text = self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial()
        self.fc.fd["pen_control"].click_right_click_btn_consumer()
        side_menu_upper_barrel_selected_text_value = self.fc.fd["pen_control"].get_right_click_element_consumer()
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_right_click_radio_button_is_selected()) is True, "Upper barrel erase radion is not selected"
        assert pen_upper_barrel_text == side_menu_upper_barrel_selected_text_value, "Upper barrel text Mismatch"


    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_verify_upper_barrel_press_action_list_C38494083(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        soft_assertion.assert_true(self.fc.fd["navigation_panel"].verify_navigationicon_show())
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_upper_barrel_text = self.fc.fd["pen_control"].get_right_click_consumer_btn_pen()
        self.fc.fd["pen_control"].click_right_click_btn_consumer()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_btn_right_click(), "Upper barrel button", "upper barrel title is not visible")
        self.fc.swipe_window(direction="up", distance=4)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_undo_consumer(), "Undo", "Undo action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_shift_key_consumer(), "Shift key", "Shift key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_control_key_consumer(), "Control key", "Control key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_alt_key_consumer(), "Alt key", "Alt key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_windows_key_consumer(), "Windows key", "Windows key action item is not visible")
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tab_key_consumer(), "Tab key", "Tab key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_arrow_key_consumer(), "Right arrow key", "Right arrow key key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_left_arrow_key_consumer(), "Left arrow key", "Left arrow key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_page_consumer(), "Previous page", "Previous page action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_page_consumer(), "Next page", "Next page action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_scroll_consumer(), "Scroll", "Scroll action item is not visible")
        self.fc.fd["pen_control"].click_productivity_dd()

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_text(), "Erase", "Erase action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_pen_consumer(), "Right-click", "Right click action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_disable_pen_buttons_consumer(), "Disable pen buttons", "Disable pen button action item is not visible")
    
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_take_screenshot_consumer(), "Take screenshot", "Screen snipping action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_switch_between_apps_consumer(), "Switch between apps", "Switch between apps action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_launch_task_manager_consumer(), "Launch task manager", "Launch task manager action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_new_browser_tab_consumer(), "New browser tab", "New browser tab action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_show_the_desktop_consumer(), "Show the desktop", "Show the desktop action is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_play_pause_consumer(), "Play / Pause", "Play/pause action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_up(), "Volume up", "Volume up action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_down(),"Volume down", "Volume down action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_mute_unmute_consumer(), "Mute / Unmute", "Mute/Unmute action is not visible")
        side_menu_upper_barrel_selected_text_value = self.fc.fd["pen_control"].get_right_click_element_consumer()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_upper_barrel_right_click_radio_button_is_selected()))
        soft_assertion.assert_equal(pen_upper_barrel_text,side_menu_upper_barrel_selected_text_value,"Right-click text is not same as pen highlighted text")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.consumer
    @pytest.mark.function
    def test_06_verify_lower_barrel_press_action_list_C38494086(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        soft_assertion.assert_true(self.fc.fd["navigation_panel"].verify_navigationicon_show())
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_lower_barrel_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        self.fc.fd["pen_control"].click_erase_btn_consumer()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_btn(),"Lower barrel button","Lower barrel title is not visible")
        self.fc.swipe_window(direction="up", distance=4)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_undo_consumer(), "Undo", "Undo action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_shift_key_consumer(), "Shift key", "Shift key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_control_key_consumer(), "Control key", "Control key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_alt_key_consumer(), "Alt key", "Alt key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_windows_key_consumer(), "Windows key", "Windows key action item is not visible")
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tab_key_consumer(), "Tab key", "Tab key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_arrow_key_consumer(), "Right arrow key", "Right arrow key key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_left_arrow_key_consumer(), "Left arrow key", "Left arrow key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_page_consumer(), "Previous page", "Previous page action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_page_consumer(), "Next page", "Next page action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_scroll_consumer(), "Scroll", "Scroll action item is not visible")
        self.fc.fd["pen_control"].click_productivity_dd()

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_text(), "Erase", "Erase action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_click_pen_consumer(), "Right-click", "Right click action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_disable_pen_buttons_consumer(), "Disable pen buttons", "Disable pen button action item is not visible")
        
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_take_screenshot_consumer(), "Take screenshot", "Screen snipping action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_switch_between_apps_consumer(), "Switch between apps", "Switch between apps action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_launch_task_manager_consumer(), "Launch task manager", "Launch task manager action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_new_browser_tab_consumer(), "New browser tab", "New browser tab action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_show_the_desktop_consumer(), "Show the desktop", "Show the desktop action is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_play_pause_consumer(), "Play / Pause", "Play/pause action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_up(), "Volume up", "Volume up action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_down(),"Volume down", "Volume down action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_mute_unmute_consumer(), "Mute / Unmute", "Mute/Unmute action is not visible")
        side_menu_lower_barrel_selected_text_value = self.fc.fd["pen_control"].get_lower_barrel_erase_selected_value()
        soft_assertion.assert_equal((self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_is_selected()), "1","Lower barrel erase radion is not selected")
        soft_assertion.assert_equal(pen_lower_barrel_text,side_menu_lower_barrel_selected_text_value,"Right-click text is not same as pen highlighted text")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.consumer
    @pytest.mark.function
    def test_07_click_more_action_link_C38494088(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        soft_assertion.assert_true(self.fc.fd["navigation_panel"].verify_navigationicon_show())
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        self.fc.fd["pen_control"].click_erase_btn_consumer()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial(),"Lower barrel button", "Lower barrel button title is not visible")
        self.fc.fd["pen_control"].scroll_up_right_click_element_consumer()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_more_link_on_app_consumer(), "More", "More link is not visible")
        self.fc.fd["pen_control"].click_more_link_on_productivity()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tab_key_consumer(), "Tab key", "Tab key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_right_arrow_key_consumer(), "Right arrow key", "Right arrow key key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_left_arrow_key_consumer(), "Left arrow key", "Left arrow key action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_page_consumer(), "Previous page", "Previous page action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_page_consumer(), "Next page", "Next page action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_scroll_consumer(), "Scroll", "Scroll action item is not visible")
        soft_assertion.raise_assertion_errors()