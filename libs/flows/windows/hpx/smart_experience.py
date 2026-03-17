import time
from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SmartExperience(HPXFlow):
    flow_name = "smart_experience"

    def verify_privacy_alert_title(self):
        return self.driver.get_attribute("privacy_alert_title","Name", raise_e=False, timeout=20)
    
    def verify_privacy_alert_subtitle(self):
        return self.driver.get_attribute("privacy_alert_subtitle","Name", raise_e=False, timeout=20)
    
    def verify_snooze_duration_title(self):
        return self.driver.get_attribute("snooze_duration_title","Name", raise_e=False, timeout=20)
    
    def verify_privacy_alert_restoreBtn(self):
        return self.driver.get_attribute("privacy_alert_restoreBtn","Name", raise_e=False, timeout=20)
    
    def verify_auto_screen_title(self):
        return self.driver.get_attribute("auto_screen_title","Name", raise_e=False, timeout=20)

    def verify_auto_screen_subtitle(self):
        return self.driver.get_attribute("auto_screen_subtitle","Name", raise_e=False, timeout=20)
    
    def verify_auto_screen_subtitle(self):
        return self.driver.get_attribute("auto_screen_subtitle","Name", raise_e=False, timeout=20)
    
    def verify_external_monitor_text(self):
        return self.driver.get_attribute("external_monitor_text","Name", raise_e=False, timeout=20)
    
    def verify_auto_screen_restoreBtn(self):
        return self.driver.get_attribute("auto_screen_restoreBtn","Name", raise_e=False, timeout=20)
    
    def click_do_not_show_checkbox(self):
        self.driver.click("not_show_checkbox")
    
    def click_cancel_button(self):
        self.driver.click("cancel_button")
    
    def click_continue_button(self):
        self.driver.click("continue_button")
    
    def click_privacy_alert_button(self):
        self.driver.click("privacy_alert_toggle")

    def verify_cancel_button_show(self):
        return self.driver.get_attribute("cancel_button", "Name", raise_e=False)
    
    def click_auto_screen_button(self):
        self.driver.click("toggle_switch_auto_dimming_popup")

    def verify_privacy_alert_item_tab_show(self):
        return self.driver.wait_for_object("privacy_alert_item_tab", raise_e=False, timeout=10)
    
    def verify_auto_screen_item_tab_show(self):
        return self.driver.wait_for_object("auto_screen_item_tab", raise_e=False, timeout=10)
    
    def verify_privacy_popup_title(self):
        return self.driver.get_attribute("privacy_popup_title","Name", raise_e=False, timeout=20)
    
    def verify_privacy_popup_subtitle(self):
        return self.driver.get_attribute("privacy_popup_subtitle","Name", raise_e=False, timeout=20)
    
    def verify_hp_statement_link_subtitle(self):
        return self.driver.get_attribute("hp_statement_link","Name", raise_e=False, timeout=20)
    
    def verify_do_not_text_show(self):
        return self.driver.get_attribute("not_show_message","Name", raise_e=False, timeout=20)
    
    def verify_continue_button_show(self):
        self.driver.wait_for_object("continue_button", raise_e=False, timeout=10)
    
    def verify_privacy_alert_btn_status(self):
        return self.driver.get_attribute("privacy_alert_toggle", "Toggle.ToggleState", timeout=10)

    def verify_auto_screen_dimming_btn_status(self):
        return self.driver.get_attribute("toggle_switch_auto_dimming_popup", "Toggle.ToggleState")
    
    def click_snooze_dropdown_list(self):
        if self.driver.wait_for_object("end_of_day", raise_e=False, timeout=10) is False:
            self.driver.click("snooze_dropdown_list", timeout=10)
    
    def verify_end_of_day_show(self):
        return self.driver.wait_for_object("end_of_day", raise_e=False, timeout=10)
    
    def click_ten_minutes(self):
        self.driver.click("ten_minutes", raise_e=False, timeout=10)
    
    def verify_ten_minutes_show(self):
        return self.driver.wait_for_object("ten_minutes", raise_e=False, timeout=10)
    
    def verify_five_minutes_show(self):
        return self.driver.wait_for_object("five_minutes", raise_e=False, timeout=10)
    
    def verify_thirty_minutes_show(self):
        return self.driver.wait_for_object("thirty_minutes", raise_e=False, timeout=10)
    
    def verify_one_hour_show(self):
        return self.driver.wait_for_object("one_hour", raise_e=False, timeout=10)

    def verify_auto_screen_dimming_title(self):
        return self.driver.get_attribute("auto_screen_title","Name", raise_e=False, timeout=20)
    
    def verify_auto_screen_dimming_subtitle(self):
        return self.driver.get_attribute("privacy_alert_description_on_popup","Name", raise_e=False, timeout=20)
    
    def get_privacy_alert_nav_text(self):
        return self.driver.get_attribute("privacy_alert_nav","Name")
    
    def verify_privacy_alert_title_visible(self):
        return self.driver.wait_for_object("privacy_alert_title", raise_e=False, timeout=10) is not False
    
    def verify_please_text_visible(self):
        return self.driver.wait_for_object("please_text", raise_e=False, timeout=20)
    
    def get_please_text(self):
        return self.driver.get_attribute("please_text","Name")
    
    def click_privacy_alert_toggle_on(self):
        self.driver.click("privacy_alert_toggle")
    
    def verify_privacy_alert_popup(self):
        return self.driver.wait_for_object("privacy_alert_title_on_popup", raise_e=False, timeout=10)
    
    def get_privacy_alert_popup_title_text(self):
        return self.driver.get_attribute("privacy_alert_title_on_popup","Name")
    
    def get_privacy_alert_description_on_popup(self):
        return self.driver.get_attribute("privacy_alert_description_on_popup","Name", raise_e=False, timeout=20)
    
    def get_do_not_show_text(self):
        return self.driver.get_attribute("do_not_show_msg","Name")
    
    def get_cancle_btn_on_popup(self):
        return self.driver.get_attribute("cancel_btn_on_popup","Name")
    
    def get_continue_btn_on_popup(self):
        return self.driver.get_attribute("continue_btn_on_popup","Name")
    
    def get_hp_privacy_statement_text(self):
        return self.driver.get_attribute("hp_privacy_statement_text","Name")
    
    def click_continue_on_popup(self):
        self.driver.click("continue_btn_on_popup")
    
    def click_snooze_duration_dd(self):
        if self.driver.get_attribute("snooze_dropdown_list","ExpandCollapse.ExpandCollapseState")=='Collapsed':
            self.driver.click("snooze_dropdown_list")
    
    def get_five_minutes(self):
        return self.driver.get_attribute("five_minutes","Name")
    
    def get_ten_minutes(self):
        return self.driver.get_attribute("ten_minutes","Name")
    
    def get_thirty_minutes(self):
        return self.driver.get_attribute("thirty_minutes","Name")
    
    def get_one_hour(self):
        return self.driver.get_attribute("one_hour","Name")
    
    def get_end_of_day(self):
        return self.driver.get_attribute("end_of_day","Name")
    
    def get_auto_screen_dimming_nav_title(self):
        return self.driver.get_attribute("auto_screen_dimming_nav_title","Name")
    
    def get_auto_screen_dimming_text(self):
        return self.driver.get_attribute("auto_screen_dimming_text","Name")
    
    def click_on_auto_screen_dimming_tooltip(self):
        self.driver.click("auto_screen_dimming_tooltip")
    
    def get_auto_screen_dimming_tooltip(self):
        return self.driver.get_attribute("auto_screen_dimming_tooltip","Name")
    
    def get_auto_screen_dimming_des_text(self):
        return self.driver.get_attribute("auto_screen_dimming_des_text","Name")
    
    def get_disable_checkbox_text(self):
        return self.driver.get_attribute("disable_checkbox_text","Name")
    
    def get_auto_screen_dimming_restore_btn(self):
        return self.driver.get_attribute("auto_screen_dimming_restore_btn","Name")
    
    def get_hp_privacy_link_btn_on_popup(self):
        return self.driver.get_attribute("hp_privacy_link_btn_on_popup","Name")
    
    def get_cancel_btn_auto_screen_dimming_popup(self):
        return self.driver.get_attribute("cancel_btn_auto_screen_dimming_popup","Name")
    
    def get_continue_btn_auto_screen_dimming_popup(self):
        return self.driver.get_attribute("continue_btn_auto_screen_dimming_popup","Name")
    
    def click_continue_btn_auto_screen_dimming_popup(self):
        self.driver.click("continue_btn_auto_screen_dimming_popup")
    
    def click_restore_btn_auto_dimming(self):
        self.driver.click("auto_screen_dimming_restore_btn")
    
    def click_toggle_switch_auto_dimming_popup(self):
        self.driver.click("toggle_switch_auto_dimming_popup")
    
    def click_privacy_alert_tool_tip(self):
        self.driver.click("privacy_alert_tool_tip")
    
    def get_privacy_alert_tool_tip(self):
        return self.driver.get_attribute("privacy_alert_tool_tip","Name")
    
    def click_do_not_show_privacy_chkbox(self):
        self.driver.click("do_not_show_privacy_chkbox")
    
    def state_do_not_show_dimming_chkbox(self):
        return self.driver.get_attribute("do_not_show_dimming_chkbox","Toggle.ToggleState")
    
    def click_do_not_show_dimming_chkbox(self):
        self.driver.click("do_not_show_dimming_chkbox")

    def click_privacy_alert_dialogue_cancel_btn(self):
        self.driver.click("cancel_btn_on_popup")

    def click_privacy_alert_link(self):
        self.driver.click("privacy_hp_statement_link")

    def click_privacy_alert_restore_default_btn(self):
        self.driver.click("privacy_alert_restoreBtn")

    def click_auto_screen_dimming_dialogue_cancel_btn(self):
        self.driver.click("cancel_btn_auto_screen_dimming_popup")

    def click_autoscreen_dimming_link(self):
        self.driver.click("privacy_hp_statement_link")

    def click_donotshow_checkbox(self):
        self.driver.click("not_show_message")

    def click_autoscreen_checkbox(self):
        self.driver.click("autoscreen_checkbox")

    def click_smart_experience_to_pcdevice_nav(self):
        self.driver.click("smart_experience_to_pcdevice_nav", timeout=10)
