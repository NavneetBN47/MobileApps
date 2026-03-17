import logging
import time
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare

class Wellbeing(HPXRebrandingFlow):
    flow_name = "wellbeing"


    def verify_screen_time_overall_card_show_up(self):
        return self.driver.wait_for_object("screen_time_overall card", raise_e=False, timeout=10)

    def verify_screen_time_title_show_up(self):
        return self.driver.wait_for_object("screen_time_title", raise_e=False, timeout=10)
    
    def verify_send_a_reminder_title_show_up(self):
        return self.driver.wait_for_object("send_a_reminder_title", raise_e=False, timeout=10)
    
    def verify_screen_distance_overall_card_show_up(self):
        return self.driver.wait_for_object("screen_distance_overall_card", raise_e=False, timeout=10)

    def verify_screen_distance_title_show_up(self):
        return self.driver.wait_for_object("screen_distance_title", raise_e=False, timeout=10)
    
    def verify_alert_options_title_show_up(self):
        return self.driver.wait_for_object("alert_options_title", raise_e=False, timeout=10)
    
    def verify_set_preferred_distance_title_show_up(self):
        return self.driver.wait_for_object("set_preferred_distance_title" , raise_e=False, timeout=10)
    
    def verify_screen_time_subtitle_show_up(self):
        return self.driver.wait_for_object("screen_time_subtitle", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_dialog_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_dialog", raise_e=False, timeout=10)
    
    def verify_send_a_reminder_subtitle_show_up(self):
        return self.driver.wait_for_object("send_a_reminder_subtitle", raise_e=False, timeout=10)
    
    def verify_send_a_reminder_toggle_show_up(self):
        return self.driver.wait_for_object("send_a_reminder_toggle", raise_e=False, timeout=10)

    def verify_reminder_combobox_show_up(self):
        return self.driver.wait_for_object("reminder_combobox", raise_e=False, timeout=10)
    
    def verify_reminder_combobox_open_button_show_up(self):
        return self.driver.wait_for_object("reminder_combobox_open_button", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_sun_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_sun", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_mon_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_mon", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_tue_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_tue", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_wed_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_wed", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_thu_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_thu", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_fri_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_fri", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_sat_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_sat", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_0h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_0h", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_2h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_2h", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_4h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_4h", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_6h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_6h", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_8h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_8h", raise_e=False, timeout=10)
    
    def verify_screen_time_bar_chart_10h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_10h", raise_e=False, timeout=10)

    def verify_screen_time_bar_chart_12h_show_up(self):
        return self.driver.wait_for_object("screen_time_bar_chart_12h", raise_e=False, timeout=10)
    
    def verify_screen_time_toggle_status(self):
        return self.driver.get_attribute("screen_time_toggle", "Toggle.ToggleState")
    
    def verify_send_a_reminder_toogle_status(self):
        return self.driver.get_attribute("send_a_reminder_toggle", "Toggle.ToggleState")
    
    def verify_screen_distance_toogle_status(self):
        return self.driver.get_attribute("screen_distance_toggle", "Toggle.ToggleState")
    
    def verify_set_preferred_distance_icon_show_up(self):
        return self.driver.wait_for_object("set_preferred_icon", raise_e=False, timeout=10)
    
    def click_screen_time_toggle(self):
        self.driver.click("screen_time_toggle")

    def click_send_a_reminder_toggle(self):
        self.driver.click("send_a_reminder_toggle")

    def click_screen_time_tooltip(self):
        self.driver.click("screen_time_tooltip")

    def get_screen_time_tooltip(self):
        return self.driver.get_attribute("screen_time_tooltip","Name")
    
    def click_send_a_reminder_tooltip(self):
        self.driver.click("send_a_reminder_tooltip")

    def get_send_a_reminder_tooltip(self):
        return self.driver.get_attribute("send_a_reminder_tooltip","Name")
    
    def click_alert_options_tooltip(self):
        self.driver.click("alert_options_tooltip")

    def get_alert_options_tooltip(self):
        return self.driver.get_attribute("alert_options_tooltip","Name")
    
    def click_screen_distance_toggle(self):
        self.driver.click("screen_distance_toggle")

    def get_alert_options(self):
        return self.driver.get_attribute("alert_options_drop_down_list","Name")
    
    def click_alert_options(self):
        self.driver.click("alert_options_drop_down_list")

    def verify_alert_options_show_on_drop_down_list(self):
        return self.driver.wait_for_object("alert_show_on_drop_down_list", raise_e=False, timeout=10)
    
    def select_alert_options(self):
        self.driver.click("alert_show_on_drop_down_list")

    def verify_set_preferred_distance_show_up(self):
        return self.driver.wait_for_object("set_preferred_distance", raise_e=False, timeout=10)
    
    def verify_set_preferred_distance_toggle_show_up(self):
        return self.driver.wait_for_object("set_preferred_distance_toggle", raise_e=False, timeout=10)
    
    def click_set_preferred_distance_toggle(self):
        self.driver.click("set_preferred_distance_toggle")
    
    def verify_current_set_distance_image_show_up(self):
        return self.driver.wait_for_object("current_set_distance_image", raise_e=False, timeout=10)

    def verify_set_button_show_up(self):
        return self.driver.wait_for_object("set_button", raise_e=False, timeout=10)
    
    def click_set_button(self):
        self.driver.click("set_button")

    def verify_restore_default_button_show_up(self):
        return self.driver.wait_for_object("restore_default_button", raise_e=False, timeout=10)
    
    def click_restore_default_button(self):
        self.driver.click("restore_default_button")

    def get_reminder_interval(self):
        return self.driver.get_attribute("reminder_interval","Name")
    
    def click_reminder_interval(self):
        self.driver.click("reminder_interval")

    def verify_reminder_interval_1_hour_show_up(self):
        return self.driver.wait_for_object("reminder_interval_1_hour", raise_e=False, timeout=10)
    
    def verify_reminder_interval_2_hour_show_up(self):
        return self.driver.wait_for_object("reminder_interval_2_hour", raise_e=False, timeout=10)
    
    def verify_reminder_interval_4_hour_show_up(self):
        return self.driver.wait_for_object("reminder_interval_4_hour", raise_e=False, timeout=10)
    
    def click_reminder_interval_1_hour(self):
        self.driver.click("reminder_interval_1_hour")

    def click_reminder_interval_2_hour(self):
        self.driver.click("reminder_interval_2_hour")

    def click_reminder_interval_4_hour(self):
        self.driver.click("reminder_interval_4_hour")

    def verify_reminder_interval_drop_down_list_grey_out(self):
        return self.driver.get_attribute("reminder_interval","IsEnabled", raise_e=False, timeout=10)
    
    def verify_reminder_interval_30_mins_show_up(self):
        return self.driver.wait_for_object("reminder_interval_30_mins", raise_e=False, timeout=10)
    
    def click_reminder_interval_30_mins(self):
        self.driver.click("reminder_interval_30_mins")

    def select_nudge_options(self):
        self.driver.click("nudge_options_show_on_drop_down_list")

    def click_cancel_button_on_current_set_distance_dialog(self):
        self.driver.click("cancel_button")

    def click_screen_time_title(self):
        self.driver.click("screen_time_title")
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_screen_time_title_show_up_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("screen_time_title", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.02)
    def verify_screen_distance_title_show_up_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("screen_distance_title", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["mode"], pass_ratio=0.02)
    def verify_screen_time_title_show_up_mode(self, mode):
        return self.driver.wait_for_object("screen_time_title", raise_e = False, timeout = 10)

    @screenshot_compare(include_param=["mode"], pass_ratio=0.02)
    def verify_screen_distance_title_show_up_mode(self, mode):
        return self.driver.wait_for_object("screen_distance_title", raise_e = False, timeout = 10)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"], pass_ratio=0.02)
    def verify_screen_time_title_show_up_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "color"], pass_ratio=0.02)
    def verify_screen_distance_title_show_up_color(self, machine_name, page_number, element, color=100, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)