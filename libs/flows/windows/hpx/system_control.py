from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SystemControl(HPXFlow):
    flow_name = "system_control"
    
    def get_system_control_header_text(self):
        return self.driver.wait_for_object("system_control_header").get_attribute("Name")
    
    def get_balanced(self):
        return self.driver.get_attribute("balanced","Name")

    def verify_system_control_card(self):
        return self.driver.wait_for_object("system_control_card", raise_e=False, timeout=20)

    def verify_system_control_title(self):
        return self.driver.wait_for_object("system_control_title", raise_e=False, timeout=20)

    def verify_system_control_subtitle(self):
        return self.driver.wait_for_object("system_control_subtitle", raise_e=False, timeout=20)

    def verify_balanced(self):
        return self.driver.wait_for_object("balanced", raise_e=False, timeout=20)

    def verify_cool(self):
        return self.driver.wait_for_object("cool", raise_e=False, timeout=10)

    def verify_quiet(self):
        return self.driver.wait_for_object("quiet", raise_e=False, timeout=20)

    def verify_power_saver(self):
        return self.driver.wait_for_object("power_saver", raise_e=False, timeout=20)

    def get_cool(self):
        return self.driver.wait_for_object("cool").get_attribute("Name")
    
    def get_quiet(self):
        return self.driver.wait_for_object("quiet").get_attribute("Name")
    
    def get_performance(self):
        return self.driver.wait_for_object("performance").get_attribute("Name")
    
    def get_power_saver(self):
        return self.driver.wait_for_object("power_saver").get_attribute("Name")
    
    def get_thermal_setting_text(self):
        return self.driver.get_attribute("thermal_setting_title","Name")
    
    def click_thermal_setting_tool_tip(self):
        self.driver.click("thermal_setting_tool_tip")
    
    def get_thermal_setting_tool_tip_text(self):
        return self.driver.get_attribute("thermal_setting_tool_tip","Name")
    
    def get_thermal_setting_sub_text(self):
        return self.driver.get_attribute("thermal_setting_sub_title","Name")
    
    def click_smart_sense_tool_tip(self):
        self.driver.click("smart_sense_tool_tip")
    
    def get_smart_sense_tool_tip(self):
        return self.driver.get_attribute("smart_sense_tool_tip","Name")
    
    def click_quiet_Tool_tip(self):
        self.driver.click("quiet_tool_tip")
    
    def get_quiet_Tool_tip_text(self):
        return self.driver.get_attribute("quiet_tool_tip","Name")
    
    def click_cool_tool_tip(self):
        self.driver.click("cool_tool_tip")
    
    def get_cool_tool_tip_text(self):
        return self.driver.get_attribute("cool_tool_tip","Name")
    
    def click_performance_tool_tip(self):
        self.driver.click("performance_tool_tip")
    
    def get_performance_tool_tip_text(self):
        return self.driver.get_attribute("performance_tool_tip","Name")
    
    def verify_smart_sense(self):
        return self.driver.wait_for_object("smart_sense", raise_e=False, timeout=10)
    
    def verify_cool_commercial(self):
        return self.driver.wait_for_object("cool_commercial", raise_e=False, timeout=10)
    
    def verify_quiet_commercial(self):
        return self.driver.wait_for_object("quiet_commercial", raise_e=False, timeout=10)
    
    def verify_performance_commercial(self):
        return self.driver.wait_for_object("performance_commercial", raise_e=False, timeout=10)
    
    def verify_performance_control_title(self):
        return self.driver.wait_for_object("performance_control_title", raise_e=False, timeout=10)
    
    def verify_performance_control_tool_tip(self):
        return self.driver.wait_for_object("performance_control_tool_tip", raise_e=False, timeout=10)
    
    def verify_performance_control_subtitle(self):
        return self.driver.wait_for_object("performance_control_subtitle", raise_e=False, timeout=10)
    
    def verify_smart_sense_tooltip(self):
        return self.driver.wait_for_object("smart_sense_tooltip", raise_e=False, timeout=10)
    
    def verify_cool_tooltip_commercial(self):
        return self.driver.wait_for_object("cool_tool_tip", raise_e=False, timeout=10)
    
    def verify_Quiet_tooltip_commercial(self):
        return self.driver.wait_for_object("Quiet_tooltip_commercial", raise_e=False, timeout=10)
    
    def verify_performance_tooltip_commercial(self):
        return self.driver.wait_for_object("performance_tooltip_commercial", raise_e=False, timeout=10)
    
    def hover_performance_control_tool_tip(self):
        self.driver.click("performance_control_tool_tip", timeout = 10)
    
    def get_performance_control_tool_tip(self):
        return self.driver.get_attribute("performance_control_tool_tip","Name")
    
    def hover_smart_sense_tooltip(self):
        self.driver.click("smart_sense_tooltip", timeout = 10)
    
    def get_smart_sense_tooltip(self):
        return self.driver.get_attribute("smart_sense_tooltip","Name")
    
    def hover_cool_tooltip_commercial(self):
        self.driver.click("cool_tooltip_commercial", timeout = 10)
    
    def get_cool_tooltip_commercial(self):
        return self.driver.get_attribute("cool_tooltip_commercial","Name")
    
    def hover_quiet_tooltip_commercial(self):
        self.driver.click("Quiet_tooltip_commercial", timeout = 10)
    
    def get_quiet_tooltip_commercial(self):
        return self.driver.get_attribute("quiet_tooltip_commercial","Name")
    
    def hover_performance_tooltip_commercial(self):
        self.driver.click("performance_commercial_tooltip", timeout = 10)
    
    def get_performance_tooltip_commercial(self):
        return self.driver.get_attribute("performance_commercial_tooltip","Name")
    
    def verify_performance_control_sub_title(self):
        return self.driver.wait_for_object("performance_control_subtitle", raise_e=False, timeout=10)
    
    def verify_cool_mode_selected(self):
        state = self.driver.get_attribute("cool_commercial","SelectionItem.IsSelected")
        return state
    
    def select_cool_mode(self):
        self.driver.click("cool_commercial")
    
    def get_system_control_title(self):
        return self.driver.get_attribute("system_control_title","Name")

    def get_system_control_title_tooltip(self):
        return self.driver.get_attribute("system_control_title_tooltip","Name")
    
    def get_system_control_subtitle(self):
        return self.driver.get_attribute("system_control_subtitle","Name")
    
    def click_system_control_title_tooltip(self):
        self.driver.click("system_control_title_tooltip")
    
    def get_smart_sense_tooltip_consumer(self):
        return self.driver.get_attribute("smart_sense_tooltip_consumer","Name")
    
    def click_smart_sense_tool_tip_consumer(self):
        self.driver.click("smart_sense_tooltip_consumer")
    
    def click_balanced_tooltip_consumer(self):
        self.driver.click("balanced_tooltip_consumer")
    
    def get_balanced_tooltip_consumer(self):
        return self.driver.get_attribute("balanced_tooltip_consumer","Name")
    
    def get_cool_tooltip_consumer(self):
        return self.driver.get_attribute("cool_tooltip_consumer","Name")
    
    def click_cool_tooltip_consumer(self):
        self.driver.click("cool_tooltip_consumer")
    
    def click_quiet_tooltip_consumer(self):
        self.driver.click("quiet_tooltip_consumer")
    
    def get_quiet_tooltip_consumer(self):
        return self.driver.get_attribute("quiet_tooltip_consumer","Name")
    
    def click_performance_tooltip_consumer(self):
        self.driver.click("performance_tooltip_consumer")
    
    def get_performance_tooltip_consumer(self):
        return self.driver.get_attribute("performance_tooltip_consumer","Name")
    
    def click_power_saver_tooltip_consumer(self):
        self.driver.click("power_saver_tooltip_consumer")
    
    def get_power_saver_tooltip_consumer(self):
        return self.driver.get_attribute("power_saver_tooltip_consumer","Name")
    
    def verify_performance_control_title_consumer(self):
        return self.driver.wait_for_object("performance_control_title_consumer", raise_e=False, timeout=10)
    
    def verify_cool_mode_selected_consumer(self):
        return self.driver.get_attribute("cool","SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def get_thermal_setting_title_consumer(self):
        return self.driver.get_attribute("thermal_setting_title_consumer","Name")
    
    def get_thermal_setting_sub_title_consumer(self):
        return self.driver.get_attribute("thermal_setting_sub_title_consumer","Name")
    
    def get_cool_commercial(self):
        return self.driver.get_attribute("cool_commercial","Name")
    
    def click_cool_commercial(self):
        self.driver.click("cool_commercial")
    
    def click_quiet_commercial_tooltip(self):
        self.driver.click("quiet_commercial_tooltip")
    
    def click_performance_commercial_tooltip(self):
        self.driver.click("performance_commercial_tooltip")
    
    def get_performance_commercial_tooltip(self):
        return self.driver.get_attribute("performance_commercial_tooltip","Name")
    
    def get_quiet_commercial(self):
        return self.driver.get_attribute("quiet_commercial","Name")
    
    def get_performance_commercial(self):
        return self.driver.get_attribute("performance_commercial","Name")
    
    def verify_performance(self):
        return self.driver.wait_for_object("performance", raise_e=False, timeout=10)

    def click_smart_sense_consumer(self):
        self.driver.click("smart_sense_consumer")
    
    def click_balanced_consumer(self):
        self.driver.click("balanced")
    
    def click_cool_consumer(self):
        self.driver.click("cool")
    
    def click_quiet_consumer(self):
        self.driver.click("quiet")
    
    def click_performance_consumer(self):
        self.driver.click("performance",timeout = 10)
    
    def click_power_saver_consumer(self):
        self.driver.click("power_saver")

    def get_system_control_title(self):
        return self.driver.get_attribute("system_control_title","Name")
    
    def verify_smart_sense_consumer(self):
        return self.driver.wait_for_object("smart_sense_consumer", raise_e=False, timeout=10)
    
    def get_quiet_commercial_tooltip(self):
        return self.driver.get_attribute("quiet_commercial_tooltip","Name")
    
    def click_system_control_title_tooltip_commercial(self):
        self.driver.click("system_control_title_tooltip_commercial")
    
    def get_system_control_title_tooltip_commercial(self):
        return self.driver.get_attribute("system_control_title_tooltip_commercial","Name")
    
    def verify_system_control_title_tooltip_consumer(self):
        return self.driver.wait_for_object("system_control_title_tooltip", raise_e=False, timeout=10)

    def verify_smart_sense_selected_consumer(self):
        return self.driver.get_attribute("smart_sense_consumer","SelectionItem.IsSelected", raise_e=False, timeout=30)
    
    def verify_balanced_selected_consumer(self):
        return self.driver.get_attribute("balanced","SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def verify_quiet_selected_consumer(self):
        return self.driver.get_attribute("quiet","SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def verify_performance_selected_consumer(self):
        return self.driver.get_attribute("performance","SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def verify_focus_mode_toggle_off_consumer(self):
        return self.driver.get_attribute("focus_mode_toggle_off_consumer","Toggle.ToggleState", raise_e=False, timeout=10)
    
    def click_focus_mode_toggle_off_consumer(self): 
        self.driver.click("focus_mode_toggle_off_consumer")

    def verify_focus_mode_toggle_on_consumer(self):
        return self.driver.get_attribute("focus_mode_toggle_on_consumer","Toggle.ToggleState", raise_e=False, timeout=10)
    
    def click_focus_mode_toggle_on_consumer(self):
        self.driver.click("focus_mode_toggle_on_consumer")

    def verify_balance_name(self):
        return self.driver.get_attribute("balance_name","Name", raise_e=False, timeout=10)
    
    def verify_best_power_efficiency(self):
        return self.driver.get_attribute("best_power_efficiency","Name", raise_e=False, timeout=10)
    
    def verify_best_performance(self):
        return self.driver.get_attribute("best_performance","Name", raise_e=False, timeout=10)
    
    def verify_power_mode(self):
        return self.driver.get_attribute("power_mode","Name", raise_e=False, timeout=30)
    
    def click_power_mode(self):
        self.driver.click("power_mode", timeout=30)

    def click_best_performance(self):
        self.driver.click("best_performance", timeout=30)

    def click_best_power_efficiency(self):
        self.driver.click("best_power_efficiency", timeout=30)

    def click_balance_name(self):
        self.driver.click("balance_name", timeout=30)

    def verify_smart_sense_selected_commercial(self):
        return self.driver.get_attribute("smart_sense","SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def verify_performance_commercial_selected_commercial(self):
        return self.driver.get_attribute("performance_commercial","SelectionItem.IsSelected", raise_e=False, timeout=10)
    
    def click_performance_commercial(self):
        self.driver.click("performance_commercial", timeout=30)

    def verify_focus_mode_text_show(self):
        return self.driver.get_attribute("focus_mode_text_on_consumer","Name")

    def verify_dim_background_windows_text_show(self):
        return self.driver.get_attribute("dim_background_windows_text_on_consumer","Name")

    def verify_dim_background_windows_tips_icon_show(self):
        return self.driver.get_attribute("dim_background_windows_tips_icon_on_consumer","Name")
    
    def click_power_mode_dd_in_settings(self):
        self.driver.click("power_mode_dd_in_settings", timeout=30)
    
    def click_plug_in_combo_box(self):
        self.driver.click("plug_in_combo_box", timeout=30)

    def verify_power_saver_selected_consumer(self):
        return self.driver.get_attribute("power_saver","SelectionItem.IsSelected", raise_e=False, timeout=20)

    def verify_power_saver_is_enabled(self):
        return self.driver.get_attribute("power_saver","IsEnabled", raise_e=False, timeout=20)

    def verify_oled_toggle_off(self):
        return self.driver.get_attribute("oled_toggle_off","Toggle.ToggleState", raise_e=False, timeout=20)
    
    def verify_oled_toggle_on(self):
        return self.driver.get_attribute("oled_toggle_on","Toggle.ToggleState", raise_e=False, timeout=20)
    
    def get_oled_toggle_text(self):
        return self.driver.get_attribute("oled_toggle_text","Name", raise_e=False, timeout=20)
    
    def click_oled_toggle_on(self):
        self.driver.click("oled_toggle_off", timeout=20)

    def click_oled_toggle_off(self):
        self.driver.click("oled_toggle_on", timeout=20)
