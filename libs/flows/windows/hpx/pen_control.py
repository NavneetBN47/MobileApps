from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time
from selenium.webdriver.common.keys import Keys

class PenControl(HPXFlow):
    flow_name = "pen_control"

    def verify_support_module_show(self):
        return self.driver.wait_for_object("support_module_title", raise_e=False, timeout=20)
    
    def verify_pen_control_module_show_on_global_navigation_panel(self):
        return self.driver.wait_for_object("pen_control_module", raise_e=False, timeout=20)

    def verify_device_info(self):
        return self.driver.wait_for_object("info_icon", raise_e=False, timeout=20)

    def click_device_info(self):
        self.driver.click("info_icon")

    def get_single_press_text(self):
        return self.driver.get_attribute("single_press", "Name")

    def get_double_press_text(self):
        return self.driver.get_attribute("double_press", "Name")

    def get_long_press_text(self):
        return self.driver.get_attribute("long_press", "Name")

    def get_upper_barrel_text(self):
        return self.driver.get_attribute("upper_barrel", "Name")

    def get_lower_barrel_text(self):
        return self.driver.get_attribute("lower_barrel", "Name")

    def get_single_press_default_text(self):
        return self.driver.wait_for_object("single_press_default_text").get_attribute("Name")

    def get_double_press_default_text(self):
        return self.driver.wait_for_object("double_press_default_text").get_attribute("Name")

    def get_long_press_default_text(self):
        return self.driver.wait_for_object("long_press_default_text").get_attribute("Name")

    def get_upper_barrel_btn_default_text(self):
        return self.driver.wait_for_object("upper_barrel_btn_default_text").get_attribute("Name")

    def get_lower_barrel_btn_default_text(self):
        return self.driver.wait_for_object("lower_barrel_btn_default_text").get_attribute("Name")

    def get_pressure_slider_default_text(self):
        return self.driver.wait_for_object("pressure_slider_text").get_attribute("Name")

    def get_tilt_slider_default_text(self):
        return self.driver.wait_for_object("tilt_slider_text").get_attribute("Name")

    def verify_resotre_button_show(self):
        return self.driver.wait_for_object("reatore_btn", raise_e=False, timeout=20)

    def verify_product_number_show(self):
        return self.driver.wait_for_object("product_number", raise_e=False, timeout=20)

    def verify_serial_number_show(self):
        return self.driver.wait_for_object("serial_number", raise_e=False, timeout=20)

    def get_productnumber_value_tooltip_text(self):
        return self.driver.wait_for_object("product_number_value_tooltip").get_attribute("Name")

    def get_serialnumber_value_tooltip_text(self):
        return self.driver.wait_for_object("serial_number_value_tooltip").get_attribute("Name")

    def verify_presenceof_serialnumber_tooltip(self):
        return self.driver.wait_for_object("serial_number_value_tooltip", raise_e=False, timeout=10)

    def verify_presenceof_productnumber_tooltip(self):
        return self.driver.wait_for_object("product_number_value_tooltip", raise_e=False, timeout=15)

    def click_productnumber_value_tooltip(self):
        self.driver.click("product_number_value_tooltip")

    def click_serialnumber_value_tooltip(self):
        self.driver.click("serial_number_value_tooltip")

    def get_connection_status(self):
        return self.driver.get_attribute("connection_status", "Name")

    def verify_battery_title_show(self):
        return self.driver.wait_for_object("battery_title", raise_e=False, timeout=20)

    def verify_connection_title_show(self):
        return self.driver.wait_for_object("connection_title", raise_e=False, timeout=20)

    def verify_default_pen_name(self):
        return self.driver.wait_for_object("default_pen_name", raise_e=False, timeout=20)

    def verify_battery_status(self):
        return self.driver.wait_for_object("battery_status", raise_e=False, timeout=20)

    def verify_edit_button(self):
        return self.driver.wait_for_object("edit_button", raise_e=False, timeout=20)

    def verify_bluetooth_status(self):
        return self.driver.wait_for_object("bluetooth_status", raise_e=False, timeout=20)

    def click_product_number(self):
        self.driver.click("product_number")

    def click_serial_number(self):
        self.driver.click("serial_number")

    def get_product_number_value(self):
        return self.driver.wait_for_object("product_number").get_attribute("Name")

    def get_serial_number_value(self):
        return self.driver.wait_for_object("serial_number").get_attribute("Name")

    def click_upper_barrel_dropdown(self):
        self.driver.click("upper_barrel_dropdown")

    def verify_go_forward_show(self):
        return self.driver.wait_for_object("go_forward", raise_e=False, timeout=20)

    def click_go_forward(self):
        self.driver.click("go_forward")

    def click_restore_button(self):
        self.driver.wait_for_object("restore_btn", raise_e=False, timeout=30)
        self.driver.click("restore_btn", timeout=20)

    def click_restore_defaults_btn(self):
        self.driver.click("restore_btn", timeout = 10)

    def verify_restore_defaults_btn(self):
        return self.driver.wait_for_object("restore_btn", raise_e=False, timeout=20)

    def verify_touch_on_off_show(self):
        return self.driver.wait_for_object("touch_on_off", raise_e=False, timeout=20)

    def verify_erase_show(self):
        return self.driver.wait_for_object("erase", raise_e=False, timeout=20)

    def verify_page_up_show(self):
        return self.driver.wait_for_object("page_up", raise_e=False, timeout=20)

    def verify_paste_show(self):
        return self.driver.wait_for_object("paste", raise_e=False, timeout=20)

    def verify_undo_show(self):
        return self.driver.wait_for_object("undo", raise_e=False, timeout=20)

    def verify_pen_sensitivity_title_show(self):
        return self.driver.wait_for_object("pen_sensitivity_title", raise_e=False, timeout=20)

    def verify_pressure_title_title_show(self):
        return self.driver.wait_for_object("pressure_title", raise_e=False, timeout=20)

    def verify_tilt_title_show(self):
        return self.driver.wait_for_object("tilt_title", raise_e=False, timeout=20)

    def verify_pressure_slider_show(self):
        return self.driver.wait_for_object("pressure_slider", raise_e=False, timeout=20)

    def verify_tilt_slider_show(self):
        return self.driver.wait_for_object("tilt_slider", raise_e=False, timeout=20)

    def click_lower_barrel_dropdown(self):
        self.driver.click("lower_barrel_dropdown")

    def get_pressure_slider_value(self):
        return self.driver.get_attribute("pressure_slider", "Name")

    def click_upper_barrel_button_hover_toggle_off(self):
        self.driver.click("upper_barrel_button_hover_click_toggle_off")

    def click_upper_barrel_button_hover_toggle_on(self):
        self.driver.click("upper_barrel_button_hover_click_toggle_on")

    def click_lower_barrel_button_hover_toggle_off(self):
        self.driver.click("lower_barrel_button_hover_click_toggle_off")

    def click_lower_barrel_button_hover_toggle_on(self):
        self.driver.click("lower_barrel_button_hover_click_toggle_on")

    def verify_upper_barrel_button_hover_toggle_off(self):
        return self.driver.get_attribute("upper_barrel_button_hover_click_toggle_off","Toggle.ToggleState")

    def verify_upper_barrel_button_hover_toggle_on(self):
        return self.driver.get_attribute("upper_barrel_button_hover_click_toggle_on","Toggle.ToggleState")

    def verify_lower_barrel_button_hover_toggle_off(self):
        return self.driver.get_attribute("lower_barrel_button_hover_click_toggle_off","Toggle.ToggleState")

    def verify_lower_barrel_button_hover_toggle_on(self):
         return self.driver.get_attribute("lower_barrel_button_hover_click_toggle_on","Toggle.ToggleState")

    def verify_pen_control_module_show(self):
        return self.driver.wait_for_object("pen_control_title_text", raise_e=False, timeout=20)

    def get_battery_title_text(self):
        return self.driver.get_attribute("battery_title", "Name")

    def get_connection_title_text(self):
        return self.driver.get_attribute("connection_title", "Name")

    def get_disconnected_battery_text(self):
        return self.driver.get_attribute("disconnected_battery", "Name")

    def get_top_btn_text(self):
        return self.driver.get_attribute("top_btn", "Name")

    def get_single_press_drop_down_text(self):
        return self.driver.get_attribute("single_press_drop_down", "Name")

    def get_double_press_dropdown_text(self):
        return self.driver.get_attribute("double_press_dropdown", "Name")

    def get_long_press_drop_down_text(self):
        return self.driver.get_attribute("long_press_drop_down", "Name")

    def get_hover_click_upper_barrel_text(self):
        return self.driver.get_attribute("hover_click_upper_barrel", "Name")

    def get_hover_click_lower_barrel_text(self):
        return self.driver.get_attribute("hover_click_lower_barrel", "Name")

    def get_upper_barrel_dropdown_text(self):
        return self.driver.get_attribute("upper_barrel_dropdown", "Name")

    def get_lower_barrel_dropdown_text(self):
        return self.driver.get_attribute("lower_barrel_dropdown", "Name")

    def get_pen_sensitivity_title_text(self):
        return self.driver.get_attribute("pen_sensitivity_title", "Name")

    def get_pressure_title_text(self):
        return self.driver.get_attribute("pressure_title", "Name")

    def get_tilt_title_text(self):
        return self.driver.get_attribute("tilt_title", "Name")

    def get_low_pressure_sensitivity_text(self):
        return self.driver.get_attribute("low_pressure_sensitivity", "Name")

    def get_high_pressure_sensitivity_text(self):
        return self.driver.get_attribute("high_pressure_sensitivity", "Name")

    def get_low_tilt_text(self):
        return self.driver.get_attribute("low_tilt", "Name")

    def get_high_tilt_text(self):
        return self.driver.get_attribute("high_tilt", "Name")

    def get_restore_btn_text(self):
        return self.driver.get_attribute("restore_btn", "Name")

    def click_single_press_dd(self):
        self.driver.click("single_press_drop_down")

    def get_single_press_touch_on_off(self):
        return self.driver.wait_for_object("single_press_touch_on_off").get_attribute("Name")

    def get_single_press_window_search(self):
        return self.driver.wait_for_object("single_press_window_search").get_attribute("Name")

    def get_single_press_ms_white_board(self):
        return self.driver.wait_for_object("single_press_ms_white_board").get_attribute("Name")

    def get_single_press_screen_snip(self):
        return self.driver.wait_for_object("single_press_screen_snip").get_attribute("Name")

    def get_single_press_sticky_notes(self):
        return self.driver.wait_for_object("single_press_sticky_notes").get_attribute("Name")

    def get_single_press_page_up(self):
        return self.driver.wait_for_object("single_press_page_up").get_attribute("Name")

    def get_single_press_page_down(self):
        return self.driver.wait_for_object("single_press_page_down").get_attribute("Name")

    def get_single_press_play_pause(self):
        return self.driver.wait_for_object("single_press_play_pause").get_attribute("Name")

    def get_single_press_next_track(self):
        return self.driver.wait_for_object("single_press_next_track").get_attribute("Name")

    def get_single_press_previus_track(self):
        return self.driver.wait_for_object("single_press_previus_track").get_attribute("Name")

    def get_single_press_volume_up(self):
        return self.driver.wait_for_object("single_press_volume_up").get_attribute("Name")

    def get_single_press_volume_down(self):
        return self.driver.wait_for_object("single_press_volume_down").get_attribute("Name")

    def get_single_press_mute_audio(self):
        return self.driver.wait_for_object("single_press_mute_audio").get_attribute("Name")

    def get_single_press_disable(self):
        return self.driver.wait_for_object("single_press_disable").get_attribute("Name")

    def get_single_press_pen_menu(self):
        return self.driver.wait_for_object("single_press_pen_menu").get_attribute("Name")

    def click_ms_white_board(self):
        self.driver.click("single_press_ms_white_board")

    def get_double_press_touch_on_off(self):
        return self.driver.wait_for_object("double_press_touch_on_off").get_attribute("Name")

    def get_double_press_window_search(self):
        return self.driver.wait_for_object("double_press_window_search").get_attribute("Name")

    def get_double_press_ms_white_board(self):
        return self.driver.wait_for_object("double_press_ms_white_board").get_attribute("Name")

    def get_double_press_screen_snip(self):
        return self.driver.wait_for_object("double_press_screen_snip").get_attribute("Name")

    def get_double_press_sticky_notes(self):
        return self.driver.wait_for_object("double_press_sticky_notes").get_attribute("Name")

    def get_double_press_page_up(self):
        return self.driver.wait_for_object("double_press_page_up").get_attribute("Name")

    def get_double_press_page_down(self):
        return self.driver.wait_for_object("double_press_page_down").get_attribute("Name")

    def get_double_press_play_pause(self):
        return self.driver.wait_for_object("double_press_play_pause").get_attribute("Name")

    def get_double_press_next_track(self):
        return self.driver.wait_for_object("double_press_next_track").get_attribute("Name")

    def get_double_press_previus_track(self):
        return self.driver.wait_for_object("double_press_previus_track").get_attribute("Name")

    def get_double_press_volume_up(self):
        return self.driver.wait_for_object("double_press_volume_up").get_attribute("Name")

    def get_double_press_volume_down(self):
        return self.driver.wait_for_object("double_press_volume_down").get_attribute("Name")

    def get_double_press_mute_audio(self):
        return self.driver.wait_for_object("double_press_mute_audio").get_attribute("Name")

    def get_double_press_disable(self):
        return self.driver.wait_for_object("double_press_disable").get_attribute("Name")
  
    def get_double_press_pen_menu(self):
        return self.driver.wait_for_object("double_press_pen_menu").get_attribute("Name")

    def click_double_press_dd(self):
        self.driver.click("double_press_dropdown")

    def click_long_press_dd(self):
        self.driver.click("long_press_drop_down")

    def get_long_press_touch_on_off(self):
        return self.driver.wait_for_object("long_press_touch_on_off").get_attribute("Name")

    def get_long_press_window_search(self):
        return self.driver.wait_for_object("long_press_window_search").get_attribute("Name")

    def get_long_press_ms_white_board(self):
        return self.driver.wait_for_object("long_press_ms_white_board").get_attribute("Name")

    def get_long_press_screen_snip(self):
        return self.driver.wait_for_object("long_press_screen_snip").get_attribute("Name")

    def get_long_press_sticky_notes(self):
        return self.driver.wait_for_object("long_press_sticky_notes").get_attribute("Name")

    def get_long_press_page_up(self):
        return self.driver.wait_for_object("long_press_page_up").get_attribute("Name")

    def get_long_press_page_down(self):
        return self.driver.wait_for_object("long_press_page_down").get_attribute("Name")

    def get_long_press_play_pause(self):
        return self.driver.wait_for_object("long_press_play_pause").get_attribute("Name")

    def get_long_press_next_track(self):
        return self.driver.wait_for_object("long_press_next_track").get_attribute("Name")

    def get_long_press_previus_track(self):
        return self.driver.wait_for_object("long_press_previus_track").get_attribute("Name")

    def get_long_press_volume_up(self):
        return self.driver.wait_for_object("long_press_volume_up").get_attribute("Name")

    def get_long_press_volume_down(self):
        return self.driver.wait_for_object("long_press_volume_down").get_attribute("Name")

    def get_long_press_mute_audio(self):
        return self.driver.wait_for_object("long_press_mute_audio").get_attribute("Name")

    def get_long_press_disable(self):
        return self.driver.wait_for_object("long_press_disable").get_attribute("Name")

    def get_long_press_pen_menu(self):
        return self.driver.wait_for_object("long_press_pen_menu").get_attribute("Name")

    def click_double_press_ms_white_board(self):
        self.driver.click("double_press_ms_white_board")

    def click_long_press_ms_white_board(self):
        self.driver.click("long_press_ms_white_board")

    def get_upper_barrel_touch_on_off(self):
        return self.driver.wait_for_object("upper_barrel_touch_on_off").get_attribute("Name")

    def get_upper_barrel_erase(self):
        return self.driver.wait_for_object("upper_barrel_erase").get_attribute("Name")

    def get_upper_barrel_right_click(self):
        return self.driver.wait_for_object("upper_barrel_right_click").get_attribute("Name")

    def get_upper_barrel_page_up(self):
        return self.driver.wait_for_object("upper_barrel_page_up").get_attribute("Name")

    def get_upper_barrel_page_down(self):
        return self.driver.wait_for_object("upper_barrel_page_down").get_attribute("Name")

    def get_upper_barrel_go_back(self):
        return self.driver.wait_for_object("upper_barrel_go_back").get_attribute("Name")

    def get_upper_barrel_go_forward(self):
        return self.driver.wait_for_object("upper_barrel_go_forward").get_attribute("Name")

    def get_upper_barrel_copy(self):
        return self.driver.wait_for_object("upper_barrel_copy").get_attribute("Name")

    def get_upper_barrel_paste(self):
        return self.driver.wait_for_object("upper_barrel_paste").get_attribute("Name")

    def get_upper_barrel_undo(self):
        return self.driver.wait_for_object("upper_barrel_undo").get_attribute("Name")

    def get_upper_barrel_redo(self):
        return self.driver.wait_for_object("upper_barrel_redo").get_attribute("Name")

    def get_upper_barrel_left_click(self):
        return self.driver.wait_for_object("upper_barrel_left_click").get_attribute("Name")

    def get_upper_barrel_middle_click(self):
        return self.driver.wait_for_object("upper_barrel_middle_click").get_attribute("Name")

    def get_upper_barrel_fourth_click(self):
        return self.driver.wait_for_object("upper_barrel_fourth_click").get_attribute("Name")

    def get_upper_barrel_fifth_click(self):
        return self.driver.wait_for_object("upper_barrel_fifth_click").get_attribute("Name")

    def get_upper_barrel_window_search(self):
        return self.driver.wait_for_object("upper_barrel_window_search").get_attribute("Name")

    def get_upper_barrel_one_note(self):
        return self.driver.wait_for_object("upper_barrel_one_note").get_attribute("Name")

    def get_upper_barrel_ms_whiteboard(self):
        return self.driver.wait_for_object("upper_barrel_ms_whiteboard").get_attribute("Name")

    def get_upper_barrel_screen_snipping(self):
        return self.driver.wait_for_object("upper_barrel_screen_snipping").get_attribute("Name")

    def get_upper_barrel_switch_application(self):
        return self.driver.wait_for_object("upper_barrel_switch_application").get_attribute("Name")

    def get_upper_barrel_web_browser(self):
        return self.driver.wait_for_object("upper_barrel_web_browser").get_attribute("Name")

    def get_upper_barrel_email(self):
        return self.driver.wait_for_object("upper_barrel_email").get_attribute("Name")

    def get_upper_barrel_play_pause(self):
        return self.driver.wait_for_object("upper_barrel_play_pause").get_attribute("Name")

    def get_upper_barrel_next_track(self):
        return self.driver.wait_for_object("upper_barrel_next_track").get_attribute("Name")

    def get_upper_barrel_previous_track(self):
        return self.driver.wait_for_object("upper_barrel_previous_track").get_attribute("Name")

    def get_upper_barrel_volume_up(self):
        return self.driver.wait_for_object("upper_barrel_volume_up").get_attribute("Name")

    def get_upper_barrel_volume_down(self):
        return self.driver.wait_for_object("upper_barrel_volume_down").get_attribute("Name")

    def get_upper_barrel_mute(self):
        return self.driver.wait_for_object("upper_barrel_mute").get_attribute("Name")

    def get_upper_barrel_disable(self):
        return self.driver.wait_for_object("upper_barrel_disable").get_attribute("Name")

    def get_upper_barrel_pen_menu(self):
        return self.driver.wait_for_object("upper_barrel_pen_menu").get_attribute("Name")

    def click_upper_barrel_right_click(self):
        self.driver.click("upper_barrel_right_click")

    def get_lower_barrel_touch_on_off(self):
        return self.driver.wait_for_object("lower_barrel_touch_on_off").get_attribute("Name")

    def get_lower_barrel_erase(self):
        return self.driver.wait_for_object("lower_barrel_erase").get_attribute("Name")

    def get_lower_barrel_right_click(self):
        return self.driver.wait_for_object("lower_barrel_right_click").get_attribute("Name")

    def get_lower_barrel_page_up(self):
        return self.driver.wait_for_object("lower_barrel_page_up").get_attribute("Name")

    def get_lower_barrel_page_down(self):
        return self.driver.wait_for_object("lower_barrel_page_down").get_attribute("Name")

    def get_lower_barrel_go_back(self):
        return self.driver.wait_for_object("lower_barrel_go_back").get_attribute("Name")

    def get_lower_barrel_go_forward(self):
        return self.driver.wait_for_object("lower_barrel_go_forward").get_attribute("Name")

    def get_lower_barrel_copy(self):
        return self.driver.wait_for_object("lower_barrel_copy").get_attribute("Name")

    def get_lower_barrel_paste(self):
        return self.driver.wait_for_object("lower_barrel_paste").get_attribute("Name")

    def get_lower_barrel_undo(self):
        return self.driver.wait_for_object("lower_barrel_undo").get_attribute("Name")

    def get_lower_barrel_redo(self):
        return self.driver.wait_for_object("lower_barrel_redo").get_attribute("Name")

    def get_lower_barrel_left_click(self):
        return self.driver.wait_for_object("lower_barrel_left_click").get_attribute("Name")

    def get_lower_barrel_middle_click(self):
        return self.driver.wait_for_object("lower_barrel_middle_click").get_attribute("Name")

    def get_lower_barrel_fourth_click(self):
        return self.driver.wait_for_object("lower_barrel_fourth_click").get_attribute("Name")

    def get_lower_barrel_fifth_click(self):
        return self.driver.wait_for_object("lower_barrel_fifth_click").get_attribute("Name")

    def get_lower_barrel_window_search(self):
        return self.driver.wait_for_object("lower_barrel_window_search").get_attribute("Name")

    def get_lower_barrel_ms_whiteboard(self):
        return self.driver.wait_for_object("lower_barrel_ms_whiteboard").get_attribute("Name")

    def get_lower_barrel_screen_snipping(self):
        return self.driver.wait_for_object("lower_barrel_screen_snipping").get_attribute("Name")

    def get_lower_barrel_switch_application(self):
        return self.driver.wait_for_object("lower_barrel_switch_application").get_attribute("Name")

    def get_lower_barrel_web_browser(self):
        return self.driver.wait_for_object("lower_barrel_web_browser").get_attribute("Name")

    def get_lower_barrel_email(self):
        return self.driver.wait_for_object("lower_barrel_email").get_attribute("Name")

    def get_lower_barrel_play_pause(self):
        return self.driver.wait_for_object("lower_barrel_play_pause").get_attribute("Name")

    def get_lower_barrel_next_track(self):
        return self.driver.wait_for_object("lower_barrel_next_track").get_attribute("Name")

    def click_info_icon(self):
        self.driver.click("info_icon", timeout = 10)

    def get_lower_barrel_previous_track(self):
        return self.driver.wait_for_object("lower_barrel_previous_track").get_attribute("Name")

    def get_lower_barrel_volume_up(self):
        return self.driver.wait_for_object("lower_barrel_volume_up").get_attribute("Name")

    def get_lower_barrel_volume_down(self):
        return self.driver.wait_for_object("lower_barrel_volume_down").get_attribute("Name")

    def get_lower_barrel_mute_audio(self):
        return self.driver.wait_for_object("lower_barrel_mute_audio").get_attribute("Name")

    def get_lower_barrel_disable(self):
        return self.driver.wait_for_object("lower_barrel_disable").get_attribute("Name")

    def get_lower_barrel_pen_menu(self):
        return self.driver.wait_for_object("lower_barrel_pen_menu").get_attribute("Name")

    def click_lower_barrel_erase(self):
        self.driver.click("lower_barrel_erase")

    def click_device_name_tooltip(self):
        self.driver.click("device_name_tooltip")

    def click_upper_barrel_tool_tip(self):
        self.driver.click("upper_barrel_tooltip", timeout = 10)

    def click_lower_barrel_tooltip(self):
        self.driver.click("lower_barrel_tooltip", timeout = 10)

    def click_default_pen_name(self):
        self.driver.click("default_pen_name")

    def click_battery_status(self):
        self.driver.click("battery_status")

    def click_bluetooth_tooltip(self):
        self.driver.click("bluetooth_status")

    def get_upper_barrel_tool_tip(self):
        return self.driver.wait_for_object("upper_barrel_tooltip").get_attribute("Name")

    def get_lower_barrel_tool_tip(self):
        return self.driver.wait_for_object("lower_barrel_tooltip").get_attribute("Name")

    def get_default_pen_name(self):
        return self.driver.wait_for_object("default_pen_name").get_attribute("Name")

    def get_hp_digital_pen_sub_title_text(self):
        return self.driver.wait_for_object("hp_digital_pen_sub_title").get_attribute("Name")

    def click_start_btn(self):
        self.sp.click_start_btn()

    def input_text_in_search_box(self, app_name):
        self.driver.wait_for_object("search_text_box", timeout=30)
        self.driver.send_keys("search_text_box", app_name)

    def get_barrel_btn_tooltip_text(self):
        return self.driver.wait_for_object("barrel_btn_tooltip_text").get_attribute("Name")

    def get_device_name_tooltip_text(self):
        return self.driver.wait_for_object("device_name_tooltip_text").get_attribute("Name")

    def click_myHP_app_On_Start_To_Open(self):
        self.sp.click_myHP_app_On_Start()

    def click_myHP_app_On_Start(self):
        self.driver.click("myHP_app_On_Start")

    def verify_open_btn_on_HP(self):
        return self.driver.wait_for_object("open_btn_on_HP")

    def get_battery_tooltip_text(self):
        battery_status = self.driver.wait_for_object("battery_status").get_attribute("Name")
        return battery_status[:7]

    def get_bluetooth_tooltip_text(self):
        return self.driver.wait_for_object("bluetooth_status").get_attribute("Name")

    def click_edit_button(self):
        self.driver.click("edit_button", timeout = 10)

    def verify_restore_default_button(self):
        return self.driver.get_attribute("restore_btn","Name")

    def click_double_press_touch_on_off(self):
        self.driver.click("double_press_touch_on_off")

    def click_product_number_copy_icon(self):
        self.driver.click("product_num_copy_icon")

    def click_serial_number_copy_icon(self):
        self.driver.click("serial_num_copy_icon")

    def click_firmware_version_copy_icon(self):
        self.driver.click("firmware_version_copy_icon")

    def click_long_press_previous_track(self):
        self.driver.click("long_press_previus_track")

    def click_upper_barrel_erase(self):
        self.driver.click("upper_barrel_erase")

    def click_lower_barrel_right_click(self):
        self.driver.click("lower_barrel_right_click")

    def verify_info_icon(self):
        return self.driver.wait_for_object("info_icon", raise_e=False, timeout=60)
    
    def get_pen_name_tooltips(self):
        self.click_default_pen_name()
        return self.driver.wait_for_object("device_name_tooltip").get_attribute("Name")
    
    def get_firmware_version_text(self):
        return self.driver.wait_for_object("firmwareversion").get_attribute("Name")
    
    def click_firmware_version_stg(self):
        self.driver.click("firmware_version_stg")
    
    def click_product_number_stg(self):
        self.driver.click("product_number_stg")
    
    def click_serial_number_stg(self):
        self.driver.click("serial_number_stg")
    
    def get_product_number_stg_text(self):
        return self.driver.wait_for_object("product_number_stg").get_attribute("Name")

    def get_serial_number_stg_text(self):
        return self.driver.wait_for_object("serial_number_stg").get_attribute("Name")
    
    def get_battery_status_tool_tip_text(self):
        return self.driver.get_attribute("battery_status","Name")
    
    def get_upper_barrel_cons_undo(self):
        return self.driver.get_attribute("upper_barrel_cons_undo","Name")
    
    def get_upper_barrel_cons_shift_key(self):
        return self.driver.get_attribute("upper_barrel_cons_shift_key","Name")

    def get_upper_barrel_cons_control_key(self):
        return self.driver.get_attribute("upper_barrel_cons_control_key","Name")

    def get_upper_barrel_cons_alt_key(self):
        return self.driver.get_attribute("upper_barrel_cons_alt_key","Name")

    def get_upper_barrel_cons_windows_key(self):
        return self.driver.get_attribute("upper_barrel_cons_windows_key","Name")
    
    def get_upper_barrel_cons_tab_key(self):
        return self.driver.get_attribute("upper_barrel_cons_tab_key","Name")

    def get_upper_barrel_cons_volume_up(self):
        return self.driver.get_attribute("upper_barrel_cons_volume_up","Name")

    def get_upper_barrel_cons_volume_down(self):
        return self.driver.get_attribute("upper_barrel_cons_volume_down","Name")

    def get_upper_barrel_cons_mute_unmute(self):
        return self.driver.get_attribute("upper_barrel_cons_mute_unmute","Name")

    def get_upper_barrel_cons_play_pause(self):
        return self.driver.get_attribute("upper_barrel_cons_play_pause","Name")

    def get_upper_barrel_cons_right_arrow_key(self):
        return self.driver.get_attribute("upper_barrel_cons_right_arrow_key","Name")

    def get_upper_barrel_cons_left_arrow_key(self):
        return self.driver.get_attribute("upper_barrel_cons_left_arrow_key","Name")

    def get_upper_barrel_cons_new_browser_tab(self):
        return self.driver.get_attribute("upper_barrel_cons_new_browser_tab","Name")

    def get_upper_barrel_cons_previous_page(self):
        return self.driver.get_attribute("upper_barrel_cons_previous_page","Name")

    def get_upper_barrel_cons_next_page(self):
        return self.driver.get_attribute("upper_barrel_cons_next_page","Name")

    def get_upper_barrel_cons_take_screenshot(self):
        return self.driver.get_attribute("upper_barrel_cons_take_screenshot","Name")

    def get_upper_barrel_cons_launch_task_manager(self):
        return self.driver.get_attribute("upper_barrel_cons_launch_task_manager","Name")

    def get_upper_barrel_cons_switch_between_apps(self):
        return self.driver.get_attribute("upper_barrel_cons_switch_between_apps","Name")

    def get_upper_barrel_cons_show_the_desktop(self):
        return self.driver.get_attribute("upper_barrel_cons_show_the_desktop","Name")

    def get_upper_barrel_cons_right_click(self):
        return self.driver.get_attribute("upper_barrel_cons_right_click","Name")

    def get_upper_barrel_cons_disable_pen_buttons(self):
        return self.driver.get_attribute("upper_barrel_cons_disable_pen_buttons","Name")

    def get_upper_barrel_cons_scroll(self):
        return self.driver.get_attribute("upper_barrel_cons_scroll","Name")

    def get_upper_barrel_cons_erase(self):
        return self.driver.get_attribute("upper_barrel_cons_erase","Name")

    def click_upper_barrel_cons_right_click(self):
        self.driver.click("upper_barrel_cons_right_click")

    def get_lower_barrel_cons_undo(self):
        return self.driver.get_attribute("lower_barrel_cons_undo","Name")

    def get_lower_barrel_cons_shift_key(self):
        return self.driver.get_attribute("lower_barrel_cons_shift_key","Name")

    def get_lower_barrel_cons_control_key(self):
        return self.driver.get_attribute("lower_barrel_cons_control_key","Name")

    def get_lower_barrel_cons_alt_key(self):
        return self.driver.get_attribute("lower_barrel_cons_alt_key","Name")

    def get_lower_barrel_cons_windows_key(self):
        return self.driver.get_attribute("lower_barrel_cons_windows_key","Name")

    def get_lower_barrel_cons_tab_key(self):
        return self.driver.get_attribute("lower_barrel_cons_tab_key","Name")

    def get_lower_barrel_cons_volume_up(self):
        return self.driver.get_attribute("lower_barrel_cons_volume_up","Name")

    def get_lower_barrel_cons_volume_down(self):
        return self.driver.get_attribute("lower_barrel_cons_volume_down","Name")

    def get_lower_barrel_cons_mute_unmute(self):
        return self.driver.get_attribute("lower_barrel_cons_mute_unmute","Name")

    def get_lower_barrel_cons_play_pause(self):
        return self.driver.get_attribute("lower_barrel_cons_play_pause","Name")

    def get_lower_barrel_cons_right_arrow_key(self):
        return self.driver.get_attribute("lower_barrel_cons_right_arrow_key","Name")

    def get_lower_barrel_cons_left_arrow_key(self):
        return self.driver.get_attribute("lower_barrel_cons_left_arrow_key","Name")

    def get_lower_barrel_cons_new_browser_tab(self):
        return self.driver.get_attribute("lower_barrel_cons_new_browser_tab","Name")

    def get_lower_barrel_cons_previous_page(self):
        return self.driver.get_attribute("lower_barrel_cons_previous_page","Name")

    def get_lower_barrel_cons_next_page(self):
        return self.driver.get_attribute("lower_barrel_cons_next_page","Name")

    def get_lower_barrel_cons_take_screenshot(self):
        return self.driver.get_attribute("lower_barrel_cons_take_screenshot","Name")

    def get_lower_barrel_cons_launch_task_manager(self):
        return self.driver.get_attribute("lower_barrel_cons_launch_task_manager","Name")

    def get_lower_barrel_cons_switch_berween_apps(self):
        return self.driver.get_attribute("lower_barrel_cons_switch_berween_apps","Name")

    def get_lower_barrel_cons_show_the_desktop(self):
        return self.driver.get_attribute("lower_barrel_cons_show_the_desktop","Name")

    def get_lower_barrel_cons_right_click(self):
        return self.driver.get_attribute("lower_barrel_cons_right_click","Name")

    def get_lower_barrel_cons_disable_pen_buttons(self):
        return self.driver.get_attribute("lower_barrel_cons_disable_pen_buttons","Name")

    def get_lower_barrel_cons_scroll(self):
        return self.driver.get_attribute("lower_barrel_cons_scroll","Name")

    def get_lower_barrel_cons_erase(self):
        return self.driver.get_attribute("lower_barrel_cons_erase","Name")

    def click_lower_barrel_cons_right_click(self):
        self.driver.click("lower_barrel_cons_right_click")
    
    def verify_right_click_show(self):
        return self.driver.wait_for_object("right_itg", raise_e=False, timeout=20)
    
    def click_more_link_on_productivity(self):
        return self.driver.click("more_link_on_productivity", raise_e=False)
    
    def get_ms_whiteboard_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_commercial","Name")
    
    def get_screen_snipping_commercial(self):
        return self.driver.get_attribute("screen_snipping_commercial","Name")
    
    def get_sticky_notes_commercial(self):
        return self.driver.get_attribute("sticky_notes_commercial","Name")
    
    def verify_sticky_notes_toggle_commer(self):
        return self.driver.get_attribute("sticky_notes_radio_toggle_commercial","Toggle.ToggleState")
    
    def get_right_click_commercial(self):
        return self.driver.get_attribute("right_click_commercial","Name")
    
    def get_pen_sensitivity_commercial(self):
        return self.driver.get_attribute("pen_sensitivity_commercial","Name")
    
    def click_pen_sensitivity_commercial(self):
        self.driver.click("pen_sensitivity_commercial")
    
    def get_pen_sensitivity_title_commercial(self):
        return self.driver.get_attribute("pen_sensitivity_title_commercial","Name", timeout = 10)
    
    def get_tilt_commercial(self):
        return self.driver.get_attribute("tilt_commercial","Name")
    
    def click_erase_btn_consumer(self):
        self.driver.click("erase_btn_consumer")
    
    def click_erase_btn_commercial(self):
        self.driver.click("erase_btn_commercial")
    
    def get_right_click_pen_commercial(self):
        return self.driver.get_attribute("right_click_pen_commercial","Name")
    
    def get_touch_on_off_commercial(self):
        return self.driver.get_attribute("touch_on_off_commercial","Name")
    
    def get_left_click_commercial(self):
        return self.driver.get_attribute("left_click_commercial","Name")
    
    def get_middle_click_commercial(self):
        return self.driver.get_attribute("middle_click_commercial","Name")
    
    def get_page_down_commercial(self):
        return self.driver.get_attribute("page_down_commercial","Name")
    
    def get_go_back_commercial(self):
        return self.driver.get_attribute("go_back_commercial","Name")
    
    def get_go_forward_commercial(self):
        return self.driver.get_attribute("go_forward_commercial","Name")
    
    def get_fourth_click_commercial(self):
        return self.driver.get_attribute("fourth_click_commercial","Name")
    
    def get_fifth_click_commercial(self):
        return self.driver.get_attribute("fifth_click_commercial","Name")
    
    def get_pen_menu_commercial(self):
        return self.driver.get_attribute("pen_menu_commercial","Name")
    
    def get_disabled_commercial(self):
        return self.driver.get_attribute("disabled_commercial","Name")
    
    def click_pen_dd(self):
        self.driver.click("pen_title", timeout = 10)
    
    def get_ms_whiteboard_commercial_apps(self):
        return self.driver.get_attribute("ms_whiteboard_commercial_apps","Name")
    
    def get_screen_snipping_commercial_apps(self):
        return self.driver.get_attribute("screen_snipping_commercial_apps","Name")
    
    def get_switch_application_commercial(self):
        return self.driver.get_attribute("switch_application_commercial","Name")
    
    def get_web_browser_commercial(self):
        return self.driver.get_attribute("web_browser_commercial","Name")
    
    def get_e_mail_commercial(self):
        return self.driver.get_attribute("e_mail_commercial","Name")
    
    def get_windows_search_commercial(self):
        return self.driver.get_attribute("windows_search_commercial","Name")
    
    def get_play_pause_commercial(self):
        return self.driver.get_attribute("play_pause_commercial","Name")
    
    def get_next_track_commercial(self):
        return self.driver.get_attribute("next_track_commercial","Name")
    
    def get_previous_track_commercial(self):
        return self.driver.get_attribute("previous_track_commercial","Name")
    
    def get_volume_up_commercial(self):
        return self.driver.get_attribute("volume_up_commercial","Name")
    
    def get_volume_down_commercial(self):
        return self.driver.get_attribute("volume_down_commercial","Name")
    
    def get_mute_audio_commercial(self):
        return self.driver.get_attribute("mute_audio_commercial","Name")
    
    def get_erase_btn_consumer(self):
        return self.driver.get_attribute("erase_btn_consumer","Name")
    
    def get_erase_btn_commercial(self):
        return self.driver.get_attribute("erase_btn_commercial","Name")
    
    def get_lower_barrel_btn(self):
        return self.driver.get_attribute("lower_barrel_btn","Name")
    
    def get_copy_commercial(self):
        return self.driver.get_attribute("copy_commercial","Name")
    
    def get_paste_commercial(self):
        return self.driver.get_attribute("paste_commercial","Name")
    
    def get_redo_commercial(self):
        return self.driver.get_attribute("redo_commercial","Name")
    
    def get_page_up_commercial(self):
        return self.driver.get_attribute("page_up_commercial","Name")
    
    def click_right_click_commercial(self):
        self.driver.click("right_click_commercial")
    
    def get_upper_barrel_btn_right_click(self):
        return self.driver.get_attribute("upper_barrel_btn_right_click","Name", timeout = 10)
    
    def get_pen_title(self):
        return self.driver.get_attribute("pen_title","Name")
    
    def get_erase_text(self):
        return self.driver.get_attribute("erase_text_consumer","Name")
    
    def get_erase_text_commercial(self):
        return self.driver.get_attribute("erase_text_commercial","Name")
    
    def get_apps(self):
        return self.driver.get_attribute("apps","Name", timeout = 10)
    
    def get_media_control(self):
        return self.driver.get_attribute("media_control","Name", timeout = 10)
    
    def click_media_control_dropdown(self):
        self.driver.click("media_control_dropdown", timeout = 10)
    
    def get_productivity(self):
        return self.driver.get_attribute("productivity","Name")
    
    def get_right_click_consumer_btn_pen(self):
        return self.driver.get_attribute("right_click_consumer_btn_text","Name")
    
    def click_right_click_btn_consumer(self):
        self.driver.click("right_click_consumer_btn_text")
    
    def get_right_click_pen_consumer(self):
        return self.driver.get_attribute("right_click_consumer","Name")
    
    def get_disable_pen_buttons_consumer(self):
        return self.driver.get_attribute("disable_pen_buttons_consumer","Name")
    
    def get_take_screenshot_consumer(self):
        return self.driver.get_attribute("take_screenshot_consumer","Name")
    
    def get_switch_between_apps_consumer(self):
        return self.driver.get_attribute("switch_between_apps_consumer","Name")
    
    def get_launch_task_manager_consumer(self):
        return self.driver.get_attribute("launch_task_manager_consumer","Name")
    
    def get_new_browser_tab_consumer(self):
        return self.driver.get_attribute("new_browser_tab_consumer","Name")
    
    def get_show_the_desktop_consumer(self):
        return self.driver.get_attribute("show_the_desktop_consumer","Name")
    
    def get_more_link_on_app_consumer(self):
        return self.driver.get_attribute("more_link_on_app_consumer","Name")
    
    def click_more_link_on_app_consumer(self):
        self.driver.click("more_link_on_app_consumer", timeout = 10)
        
    def click_apps_dropdown(self):
        self.driver.click("apps", timeout = 10)
    
    def get_play_pause_consumer(self):
        return self.driver.get_attribute("play_pause_consumer","Name")
    
    def get_volume_up(self):
        return self.driver.get_attribute("volume_up","Name")
    
    def get_volume_up_commercial(self):
        return self.driver.get_attribute("volume_up_commercial","Name")
    
    def get_volume_down(self):
        return self.driver.get_attribute("volume_down","Name")
    
    def get_volume_down_commercial(self):
        return self.driver.get_attribute("volume_down_commercial","Name")
    
    def get_mute_unmute_consumer(self):
        return self.driver.get_attribute("mute_unmute_consumer","Name")
    
    def get_undo_consumer(self):
        return self.driver.get_attribute("undo_consumer","Name")
    
    def get_undo_commercial(self):
        return self.driver.get_attribute("undo_commercial","Name")
    
    def get_shift_key_consumer(self):
        return self.driver.get_attribute("shift_key_consumer","Name")
    
    def get_control_key_consumer(self):
        return self.driver.get_attribute("control_key_consumer","Name")
    
    def get_alt_key_consumer(self):
        return self.driver.get_attribute("alt_key_consumer","Name")
    
    def get_windows_key_consumer(self):
        return self.driver.get_attribute("windows_key_consumer","Name")
    
    def get_tab_key_consumer(self):
        return self.driver.get_attribute("tab_key_consumer","Name")
    
    def get_right_arrow_key_consumer(self):
        return self.driver.get_attribute("right_arrow_key_consumer","Name")
    
    def get_left_arrow_key_consumer(self):
        return self.driver.get_attribute("left_arrow_key_consumer","Name")
    
    def get_previous_page_consumer(self):
        return self.driver.get_attribute("previous_page_consumer","Name")
    
    def get_next_page_consumer(self):
        return self.driver.get_attribute("next_page_consumer","Name")
    
    def get_scroll_consumer(self):
        return self.driver.get_attribute("scroll_consumer","Name")
    
    def get_more_link_on_productivity(self):
        return self.driver.get_attribute("more_link_on_productivity","Name")
    
    def get_device_name_tooltip_commercial(self):
        return self.driver.get_attribute("device_name_tooltip","Name")

    def click_single_press_button_commercial(self):
        self.driver.click("single_press", timeout =10)

    def verify_single_press_button_show(self):
        return self.driver.wait_for_object("single_press_button", raise_e=False, timeout=20)

    def verify_double_press_button_show(self):
        return self.driver.wait_for_object("double_press_button", raise_e=False, timeout=20)

    def verify_long_press_button_show(self):
        return self.driver.wait_for_object("long_press_button", raise_e=False, timeout=20)

    def verify_single_press_side_menu_title_commercial(self):
        return self.driver.get_attribute("single_press_title_commercial","Name", timeout = 10)

    def verify_double_press_side_menu_title_commercial(self):
        return self.driver.get_attribute("double_press_title_commercial","Name", timeout = 10)

    def verify_long_press_side_menu_title_commercial(self):
        return self.driver.get_attribute("long_press_title_commercial","Name")

    def click_single_press_button_commercial(self):
        self.driver.click("single_press_button", timeout = 10)

    def click_double_press_button_commercial(self):
        self.driver.click("double_press_button", timeout = 10)

    def click_long_press_button_commercial(self):
        self.driver.click("long_press_button", timeout = 10)

    def get_upper_barrel_image_button_show_commercial(self):
        return self.driver.get_attribute("upper_barrel_image_button_commercial","Name")
    
    def get_default_upper_barrel_button_commercial(self):
        return self.driver.get_attribute("right_click_consumer_btn_text","Name", timeout = 10)
    
    def click_upper_barrel_image_button_commercial(self):
        self.driver.click("upper_barrel_image_button_commercial", timeout = 10)
    
    def verify_upper_barrel_button_text_show_commercial(self):
        return self.driver.get_attribute("upper_barrel_btn_right_click","Name", timeout = 10)
    
    def get_universal_select_toggle_text_show_commercial(self):
        return self.driver.get_attribute("universal_select_toggle_text","Name")
    
    def get_universal_select_toggle_is_select_commercial(self):
        return self.driver.get_attribute("universal_select_toggle_consumer","Toggle.ToggleState")
    
    def get_left_click_toggle_text_show_commercial(self):
        return self.driver.get_attribute("left_click_toggle_text","Name",timeout = 10)
    
    def click_left_click_toggle_commercial(self):
        self.driver.click("left_click_radio_toggle_comercial",timeout = 10)

    def get_left_click_toggle_is_select_commercial(self):
        return self.driver.get_attribute("left_click_radio_toggle_comercial","Toggle.ToggleState", timeout = 10)
    
    def get_lower_barrel_image_button_show_commercial(self):
        return self.driver.get_attribute("lower_barrel_image_button_commercial","Name", timeout = 10)

    def get_default_lower_barrel_button_commercial(self):
        return self.driver.get_attribute("erase_btn_consumer","Name", timeout=10)
    
    def click_lower_barrel_image_button_commercial(self):
        self.driver.click("default_lower_barrel_button_commercial", timeout = 10)

    def verify_lower_barrel_button_text_show_commercial(self):
        return self.driver.get_attribute("lower_barrel_btn","Name", timeout = 10)

    def get_erase_toggle_text_show_commercial(self):
        return self.driver.get_attribute("erase_text_list_commercial","Name")
    
    def get_erase_toggle_is_select_commercial(self):
        return self.driver.get_attribute("erase_radio_toggle_commercial","Toggle.ToggleState")
    
    def get_middle_click_toggle_text_show_commercial(self):
        return self.driver.get_attribute("middle_click_commercial_text_commercial","Name")
    
    def click_middle_click_toggle_commercial(self):
        self.driver.click("middle_click_radio_toggle_commercial", timeout = 10)

    def get_middle_click_is_select_commercial(self):
        return self.driver.get_attribute("middle_click_radio_toggle_commercial","Toggle.ToggleState", timeout = 10)
    
    def get_pen_control_custom_name_show_commercial(self):
        return self.driver.get_attribute("pen_control_title_text","Name")
    
    def click_pen_control_custom_name_commercial(self):
        self.driver.click("pen_control_title_text")
    
    def change_pen_name_consumer(self, text):
        self.driver.wait_for_object("device_name_input_consumer", timeout=10)
        self.driver.send_keys("device_name_input_consumer", text)
        el = self.driver.wait_for_object("device_name_input_consumer", displayed=False, timeout=3)
        time.sleep(3)
        el.send_keys(Keys.ENTER)

    def get_more_button_link_in_pen_mode_show_commercial(self):
        return self.driver.get_attribute("more_button_link_in_pen_mode_commercial","Name", timeout = 10)
    
    def click_more_button_link_in_pen_mode_commercial(self):
        self.driver.click("more_button_link_in_pen_mode_commercial", timeout = 10)

    def get_fourth_click_button_text_show_commercial(self):
        return self.driver.get_attribute("fourth_click_text_commercial","Name")
    
    def get_disabled_button_text_show_commercial(self):
        return self.driver.get_attribute("disabled_text_commercial","Name")
    
    def get_single_press_button_show_commercial(self):
        return self.driver.get_attribute("single_press_button","Name")
		
    def get_top_button_single_press_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("single_press_title_commercial","Name", timeout = 20)
    
    def get_ms_white_board_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_text_commercial","Name", timeout = 20)
    
    def get_ms_white_board_toggle_is_select_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_radio_toggle_commercial","Toggle.ToggleState", timeout = 20)
    
    def verify_restore_default_button_not_show_when_configure_key_list_show_commercial(self):
        return self.driver.wait_for_object("restore_btn", raise_e=False, timeout=20)
    
    def get_double_press_button_show_commercial(self):
        return self.driver.get_attribute("double_press_button","Name")

    def get_top_button_double_press_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("double_press_title_commercial","Name")
    
    def get_screen_snipping_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("screen_snipping_text_commercial","Name")
    
    def get_screen_snipping_toggle_is_select_commercial(self):
        return self.driver.get_attribute("screen_snipping_radio_toggle_commercial","Toggle.ToggleState")
    
    def get_long_press_button_show_commercial(self):
        return self.driver.get_attribute("long_press_button","Name")

    def get_top_button_long_press_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("long_press_title_commercial","Name")
    
    def get_sticky_notes_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("sticky_notes_text_commercial","Name")
    
    def get_sticky_notes_toggle_is_select_commercial(self):
        return self.driver.get_attribute("sticky_notes_toggle_is_select_commercial","Name")
    
    def verify_action_list_not_show_commercial(self):
        return self.driver.wait_for_object("action_list_not_show_commercial", raise_e=False, timeout=20)
    
    def verify_restore_default_button_show_when_configure_key_list_close_commercial(self):
        return self.driver.wait_for_object("restore_btn", raise_e=False, timeout=20)
    
    def get_pen_control_default_name_on_right_side_commercial(self):
        return self.driver.get_attribute("pen_control_title_text","Name", timeout = 10)
    
    def verify_pen_edit_icon_show_commercial(self):
        return self.driver.wait_for_object("edit_button", raise_e=False, timeout=20)
    
    def click_pen_edit_icon_commercial(self):
        self.driver.click("edit_button")

    def verify_pen_name_edit_box_show_commercial(self):
        return self.driver.wait_for_object("device_name_input_consumer", raise_e=False, timeout=20)
    
    def enter_device_name(self, text):
        self.driver.wait_for_object("device_name_input_consumer", timeout=10)
        self.driver.send_keys("device_name_input_consumer", text)
        el = self.driver.wait_for_object("device_name_input_consumer", displayed=False, timeout=3)
        time.sleep(3)
        el.send_keys(Keys.ENTER)

    def get_pen_name_on_right_side_commercial(self):
        return self.driver.get_attribute("pen_control_title_text","Name", timeout = 10)
    
    def get_pen_name_on_left_side_commercial(self):
        return self.driver.get_attribute("pen_name_on_left_side_commercial","Name")
    
    def get_pen_control_default_name_on_left_side_commercial(self):
        return self.driver.get_attribute("pen_name_on_left_side_commercial","Name")

    def scroll_touch_on_off_element_commercial(self):
        self.driver.send_keys("touch_on_off", Keys.PAGE_UP)

    def scroll_down_volume_up_element_commercial(self):
        self.driver.send_keys("volume_up_commercial", Keys.PAGE_DOWN)

    def click_mute_audio_checkbox_commercial(self):
        self.driver.click("pen_control_mute_audio_radio_button_commercial", timeout = 10)

    def verify_mute_audio_checkbox_is_selected(self):
        return self.driver.get_attribute("pen_control_mute_audio_radio_button_commercial", "SelectionItem.IsSelected")
   
    def verify_pen_control_show_in_navigation_bar_commercial(self):
        return self.driver.wait_for_object("pen_name_on_left_side_commercial", raise_e=False, timeout=20)
    
    def verify_pen_control_not_show_in_navigation_bar_commercial(self):
        return self.driver.wait_for_object("pen_name_on_left_side_commercial", raise_e=False, timeout=20)

    def verify_bluetooth_icon_show_commercial(self):
        return self.driver.wait_for_object("bluetooth_status", raise_e=False, timeout=20)
    
    def verify_info_icon_show_commercial(self):
        return self.driver.wait_for_object("info_icon", raise_e=False, timeout=20)
    
    def get_single_press_text_commercial(self):
        return self.driver.get_attribute("single_press","Name")
    
    def get_single_press_text_along_with_default_action_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_commercial","Name")
    
    def get_double_press_text_commercial(self):
        return self.driver.get_attribute("double_press","Name")
    
    def get_double_press_text_along_with_default_action_commercial(self):
        return self.driver.get_attribute("screen_snipping_commercial","Name")
    
    def get_long_press_text_commercial(self):
        return self.driver.get_attribute("long_press","Name")
    
    def get_long_press_text_along_with_default_action_commercial(self):
        return self.driver.get_attribute("sticky_notes_commercial","Name")
    
    def get_pen_sensitivity_button_show_commercial(self):
        return self.driver.get_attribute("pen_sensitivity_button_commercial","Name")
    
    def get_restore_defaults_button_show_commercial(self):
        return self.driver.get_attribute("restore_btn","Name")
    
    def get_top_image_button_show_commercial(self):
        return self.driver.get_attribute("top_image_button_commercial","Name")
    
    def get_pen_sensitivity_image_button_show_commercial(self):
        return self.driver.get_attribute("pen_sensitivity_image_button_commercial","Name")
    
    def verify_lower_barrel_erase_radio_button_is_selected(self):
        return self.driver.get_attribute("lower_barrel_erase_radio_toggle_consumer", "Toggle.ToggleState")
    
    def verify_lower_barrel_erase_radio_button_consumer_is_selected(self):
        return self.driver.get_attribute("erase_radio_toggle_commercial", "Toggle.ToggleState")
    
    def verify_upper_barrel_right_click_radio_button_is_selected(self):
        return self.driver.get_attribute("upper_barrel_right_click_radio_button_consumer", "SelectionItem.IsSelected", timeout = 10)
    
    def get_universal_select_commercial(self):
        return self.driver.get_attribute("universal_select_commercial","Name")
    
    def click_universal_select_commercial(self):
        self.driver.click("universal_select_commercial")
    
    def get_universal_select_dropdown_text_commercial(self):
        return self.driver.get_attribute("universal_select_commercial_dropdown_text","Name")
    
    def click_more_link_on_pen(self):
        return self.driver.click("more_link_on_pen", raise_e=False, timeout = 30)
    
    def click_more_link_on_apps(self):
        return self.driver.click("more_link_on_apps", raise_e=False)
    
    def click_more_link_on_media(self):
        return self.driver.click("more_link_on_media", raise_e=False)
    
    def click_productivity_dd(self):
        self.driver.click("productivity")
    
    def click_pen_section_dd(self):
        self.driver.click("pen_section_dd")

    def scroll_up_right_click_element_consumer(self):
        self.driver.send_keys("upper_barrel_right_click_radio_button_consumer", Keys.PAGE_UP)

    def scroll_down_right_click_element_consumer(self):
        self.driver.send_keys("upper_barrel_right_click_radio_button_consumer", Keys.PAGE_DOWN)

    def get_right_click_element_consumer(self):
        return self.driver.get_attribute("upper_barrel_right_click_radio_button_consumer","Name")

    def get_lower_barrel_erase_selected_value(self):
        return self.driver.get_attribute("lower_barrel_erase_radio_button_consumer", "Name")
    
    def get_pen_menu_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("pen_menu_commercial","Name")
    
    def click_pen_menu_toggle_commercial(self):
        self.driver.click("pen_menu_radio_toggle_commercial")

    def get_pen_menu_toggle_is_select_commercial(self):
        return self.driver.get_attribute("pen_menu_toggle_commercial","Name")
    
    def get_default_single_press_button_now_commercial(self):
        return self.driver.get_attribute("now_is_pen_menu_","Name")
    
    def get_disabled_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("disabled_commercial","Name")
    
    def click_disabled_toggle_commercial(self):
        self.driver.click("disabled_radio_toggle_commercial")

    def get_disabled_toggle_is_select_commercial(self):
        return self.driver.get_attribute("disabled_radio_toggle_commercial","Toggle.ToggleState")
    
    def get_default_double_press_button_now_commercial(self):
        return self.driver.get_attribute("now_is_disabled","Name")
    
    def get_windows_search_text_in_configure_key_list_show_commercial(self):
        return self.driver.get_attribute("windows_search_commercial","Name")
    
    def click_windows_search_toggle_commercial(self):
        self.driver.click("windows_search_radio_toggle_commercial")

    def get_windows_search_toggle_is_select_commercial(self):
        return self.driver.get_attribute("windows_search_radio_toggle_commercial","Toggle.ToggleState")
    
    def get_default_long_press_button_now_commercial(self):
        return self.driver.get_attribute("now_is_windows_search","Name")
    
    def click_ms_white_board_toggle_commercial(self):
        self.driver.click("ms_whiteboard_radio_toggle_commercial", timeout = 30 )
    
    def get_double_press_button_now_is_ms_whiteboard_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_commercial","Name")
    
    def get_long_press_button_now_is_ms_whiteboard_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_commercial","Name")
    
    def get_upper_barrel_button_now_is_ms_whiteboard_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_commercial","Name")
    
    def get_lower_barrel_button_now_is_ms_whiteboard_commercial(self):
        return self.driver.get_attribute("ms_whiteboard_commercial","Name")
    
    def verify_presenceof_firmware_tooltip(self):
        return self.driver.wait_for_object("firmware_version_copy_icon", raise_e=False, timeout=20)
    
    def get_firmwareversion_value_tooltip_text(self):
        return self.driver.wait_for_object("firmware_version_copy_icon").get_attribute("Name")
    
    def hover_on_pen_name_commercial(self):
        self.driver.click("device_name_tooltip", timeout = 10)

    def get_pen_name_tooltip_commercial(self):
        return self.driver.wait_for_object("device_name_tooltip").get_attribute("Name")

    def verify_ms_white_board_radio_button_is_selected(self):
        return self.driver.get_attribute("ms_white_toggle_commercial", "SelectionItem.IsSelected")

    def get_ms_white_board_name_commercial(self):
        return self.driver.wait_for_object("ms_white_toggle_commercial").get_attribute("Name")

    def verify_screen_snipping_radio_button_is_selected(self):
        return self.driver.get_attribute("screen_snipping_toggle_is_select_commercial","SelectionItem.IsSelected")

    def verify_sticky_notes_radio_button_is_selected(self):
        return self.driver.get_attribute("sticky_notes_toggle_is_select_commercial","SelectionItem.IsSelected")

    def verify_universal_select_radio_button_is_selected(self):
        return self.driver.get_attribute("universal_select_toggle_is_select_commercial","SelectionItem.IsSelected")

    def get_tilt_tip_slider_value(self,slider_name):
        slider_element = self.driver.get_attribute(slider_name, attribute = "RangeValue.Value")
        return slider_element

    def get_side_menu_navigation_pen_name(self):
        return self.driver.get_attribute("pen_control_module","Name", raise_e=False, timeout=20)

    def get_page_up_text_commercial(self):
        return self.driver.get_attribute("page_up_text_commercial","Name")

    def get_page_down_text_commercial(self):
        return self.driver.get_attribute("page_down_text_commercial","Name")

    def get_touch_on_off_text_commercial(self):
        return self.driver.get_attribute("touch_on_off_text_commercial","Name")
    
    def get_pen_menu_text_commercial(self):
        return self.driver.get_attribute("pen_menu_text_commercial","Name")
    
    def get_disabled_text_commercial(self):
        return self.driver.get_attribute("disabled_text_commercial","Name")
    
    def get_screen_snipping_text_commercial(self):
        return self.driver.get_attribute("screen_snipping_text_commercial","Name")
    
    def get_windows_search__text_commercial(self):
        return self.driver.get_attribute("windows_search_text_commercial","Name")
    
    def get_play_pause_text_commercial(self):
        return self.driver.get_attribute("play_pause_text_commercial","Name")
    
    def get_next_track_text_commercial(self):
        return self.driver.get_attribute("next_track_text_commercial","Name")
    
    def get_previous_track_text_commercial(self):
        return self.driver.get_attribute("previous_track_text_commercial","Name")
    
    def get_volume_up_text_commercial(self):
        return self.driver.get_attribute("volume_up_text_commercial","Name")
    
    def get_volume_down_text_commercial(self):
        return self.driver.get_attribute("volume_down_text_commercial","Name")
    
    def get_mute_audio_text_commercial(self):
        return self.driver.get_attribute("mute_audio_text_commercial","Name")

    def verify_pen_sensivity_slider_visible(self):
        return self.driver.wait_for_object("tilt_sensitivity_slider", raise_e=False, timeout = 10)

    def set_slider_value_increase(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.UP)
            time.sleep(3)

    def set_slider_value_decrease(self,value,slider_name):
        slider = self.driver.wait_for_object(slider_name)
        for _ in range(value):
            slider.send_keys(Keys.DOWN)
            time.sleep(3)

    def get_tilt_tip_slider_min_value(self,slider_name):
        slider_element = self.driver.get_attribute(slider_name, attribute = "RangeValue.Minimum")
        return slider_element

    def get_tilt_tip_slider_max_value(self,slider_name):
        slider_element = self.driver.get_attribute(slider_name, attribute = "RangeValue.Maximum")
        return slider_element

    def verify_pen_tip_pressure_slider_visible(self):
        return self.driver.wait_for_object("tilt_sensitivity_slider", raise_e=False, timeout = 10)
    
    def get_universal_select_text_commercial(self):
        return self.driver.get_attribute("universal_select_text_commercial","Name")
    
    def verify_proximity_icon(self):
        return self.driver.wait_for_object("proximity_icon", raise_e=False, timeout=20)
    
    def get_proximity_icon_tooltip_text(self):
        return self.driver.wait_for_object("proximity_icon").get_attribute("Name")
    
    def click_proximity_icon(self):
        self.driver.click("proximity_icon")

    def verify_upper_barrel_tool_tip_visible(self):
        return self.driver.wait_for_object("upper_barrel_tooltip", raise_e=False, timeout = 10)

    def verify_lower_barrel_tool_tip_visible(self):
        return self.driver.wait_for_object("lower_barrel_tooltip", raise_e=False, timeout = 10)

    def verify_product_number_copy_icon(self):
        return self.driver.wait_for_object("product_number_copy_icon", raise_e=False, timeout=10)

    def verify_serial_number_copy_icon(self):
        return self.driver.wait_for_object("serial_number_copy_icon", raise_e=False, timeout=10)

    def verify_firmware_copy_icon(self):
        return self.driver.wait_for_object("firmware_copy_icon", raise_e=False, timeout=10)
    
    def upper_barrel_button_hover_click_toggle_off_is_displayed(self):
        return self.driver.wait_for_object("upper_barrel_button_hover_click_toggle_off", raise_e=False, timeout = 10)
    
    def lower_barrel_button_hover_click_toggle_off_is_displayed(self):
        return self.driver.wait_for_object("lower_barrel_button_hover_click_toggle_off", raise_e=False, timeout = 10)

    def verify_connection_proximity_show(self):
        return self.driver.wait_for_object("connection_proximity", raise_e=False, timeout=20)
    
    def get_pen_control_default_name_on_right_side_consumer(self):
        return self.driver.get_attribute("device_name_tooltip","Name", timeout = 10)

    def get_pen_control_serail_number_value_commercial(self):
        return self.driver.get_attribute("serail_number_value","Name", timeout = 10)

    def click_pen_settings_button(self):
        return self.driver.click("pen_setting_button", raise_e=False, timeout = 10)

    def get_pen_setting_notification_header(self):
        return self.driver.get_attribute("pen_setting_notification_header","Name", timeout = 10)

    def get_pen_not_detected_alert_title(self):
        return self.driver.get_attribute("pen_not_detected_alert_title","Name", timeout = 10)

    def get_power_saving_header(self):
        return self.driver.get_attribute("power_saving_header","Name", timeout = 10)

    def get_power_saving_desc(self):
        return self.driver.get_attribute("power_saving_desc","Name", timeout = 10)

    def get_one_step_inking_header(self):
        return self.driver.get_attribute("one_step_inking_header","Name", timeout = 10)

    def get_one_step_inking_desc(self):
        return self.driver.get_attribute("one_step_inking_desc","Name", timeout = 10)

    def get_pen_setting_page_title(self):
        return self.driver.get_attribute("pen_setting_title","Name", timeout = 10)

    def verify_pen_not_detected_toggle_is_visible(self):
        return self.driver.wait_for_object("pen_not_detected_toggle", raise_e=False, timeout=10)

    def verify_power_saving_toggle_is_visible(self):
        return self.driver.wait_for_object("power_saving_toggle", raise_e=False, timeout=10)

    def verify_one_step_inking_dropdown_is_visible(self):
        return self.driver.wait_for_object("one_step_inking_dropdown", raise_e=False, timeout=10)

    def click_one_step_inking_dropdown(self):
        return self.driver.click("one_step_inking_dropdown", raise_e=False, timeout = 10)

    def verify_inking_dropdown_value_one_note(self):
        return self.driver.get_attribute("one_step_inking_dropdown_value_one_note","Name", timeout = 10)

    def verify_inking_dropdown_value_microsoft_whiteboard(self):
        return self.driver.get_attribute("one_step_inking_dropdown_value_microsoft_whiteboard","Name", timeout = 10)

    def verify_inking_dropdown_value_snipping_tool(self):
        return self.driver.get_attribute("one_step_inking_dropdown_value_snipping_tool","Name", timeout = 10)

    def verify_inking_dropdown_value_disabled(self):
        return self.driver.get_attribute("one_step_inking_dropdown_value_disabled","Name", timeout = 10)

    def verify_pen_not_detected_toggle_status(self):
        return self.driver.get_attribute("pen_not_detected_toggle","Toggle.ToggleState")

    def verify_power_saving_toggle_status(self):
        return self.driver.get_attribute("power_saving_toggle","Toggle.ToggleState")

    def click_pen_not_detected_toggle_button(self):
        return self.driver.click("pen_not_detected_toggle", raise_e=False, timeout = 10)

    def click_power_saving_toggle_button(self):
        return self.driver.click("power_saving_toggle", raise_e=False, timeout = 10)

    def verify_pen_is_selected_from_navbar(self):
        return self.driver.get_attribute("pen_name_on_left_side_commercial", "SelectionItem.IsSelected", timeout = 20)
