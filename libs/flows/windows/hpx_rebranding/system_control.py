from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
from SAF.decorator.saf_decorator import screenshot_compare


class SystemControl(HPXRebrandingFlow):
    flow_name = "system_control"

    def verify_system_control_title_show(self):
        return self.driver.wait_for_object("system_control_title", raise_e=False, timeout=10)    
    
    def verify_system_control_performance_control_title_show(self):
        return self.driver.wait_for_object("system_control_performance_control_title", raise_e=False, timeout=10)
    
    def verify_system_control_performance_control_description(self):
        return self.driver.wait_for_object("system_control_performance_control_description", raise_e=False, timeout=10)
    
    def verify_system_control_cool_title_show(self):
        return self.driver.wait_for_object("system_control_cool_title", raise_e=False, timeout=10)
    
    def verify_system_control_quiet_title_show(self):
        return self.driver.wait_for_object("system_control_quiet_title", raise_e=False, timeout=10)
    
    def verify_system_control_powersaver_title_show(self):
        return self.driver.wait_for_object("system_control_powersaver_title", raise_e=False, timeout=10)
    
    def verify_system_control_performance_title_show(self):
        return self.driver.wait_for_object("system_control_performance_title", raise_e=False, timeout=10)
    
    def verify_system_control_focus_mode_title_show(self):
        return self.driver.wait_for_object("foucus_mode_title", raise_e=False, timeout=10)
    
    def verify_system_control_dim_background_title_show(self):
        return self.driver.wait_for_object("dim_background_title", raise_e=False, timeout=10)

    def click_balanced_toggle(self):
        self.driver.click("system_control_balanced_toggle", timeout=10)
    
    def click_cool_toggle(self):
        self.driver.click("system_control_cool_toggle", timeout=10)

    def click_quiet_toggle(self):
        self.driver.click("system_control_quiet_toggle", timeout=10)

    def click_powersaver_toggle(self):
        self.driver.click("system_control_powersaver_toggle", timeout=10)

    def click_performance_toggle(self):
        self.driver.click("system_control_performance_toggle", timeout=10)

    def get_system_control_powersaver_radiobutton_enable_disable_state(self):
        return self.driver.get_attribute("system_control_powersaver_toggle", "IsEnabled",  timeout = 10)

    def get_system_control_balance_radiobutton_is_selected(self):
        return self.driver.get_attribute("system_control_balanced_toggle", "SelectionItem.IsSelected",  timeout = 10)
    
    def get_system_control_powersaver_radiobutton_is_selected(self):
        return self.driver.get_attribute("system_control_powersaver_toggle", "SelectionItem.IsSelected",  timeout = 10)
    
    def get_system_control_cool_radiobutton_is_selected(self):
        return self.driver.get_attribute("system_control_cool_toggle", "SelectionItem.IsSelected",  timeout = 10)
    
    def get_system_quiet_radiobutton_is_selected(self):
        return self.driver.get_attribute("system_control_quiet_toggle", "SelectionItem.IsSelected",  timeout = 10)
    
    def get_system_performance_radiobutton_is_selected(self):
        return self.driver.get_attribute("system_control_performance_toggle", "SelectionItem.IsSelected",  timeout = 10)
    
    def get_system_smart_sense_radiobutton_is_selected(self):
        return self.driver.get_attribute("smart_sense_radio_button", "SelectionItem.IsSelected",  timeout = 10)
    
    def click_smart_sense_radio_button(self):
        self.driver.click("smart_sense_radio_button",timeout = 5)

    def get_smart_sense_radio_button_commercial_is_selected(self):
        return self.driver.get_attribute("smart_sense_radio_button_commercial", "SelectionItem.IsSelected",  timeout = 10)
    
    def click_smart_sense_radio_button_commercail(self):
        self.driver.click("smart_sense_radio_button_commercial", timeout = 10)
    
    def click_focus_mode_toggle(self):
        self.driver.click("dim_background_toggle", timeout = 5)
    
    def verify_smart_sense_title_show(self):
        if self.driver.wait_for_object("smart_sense_title_commercial", raise_e=False, timeout=10) is not False:
            return True
        elif self.driver.wait_for_object("smart_sense_title_consumer", raise_e=False, timeout=10) is not False:
            return True
        else:
            return False
    
    def verify_power_saving_mode_title_show(self):
        return self.driver.wait_for_object("power_saving_mode_title", raise_e=False, timeout=10)
    
    def verify_optimize_oled_title_show(self):
        return self.driver.wait_for_object("optimize_oled_title", raise_e=False, timeout=10)
    
    def verify_optimize_oled_toggle_show(self):
        return self.driver.wait_for_object("optimize_oled_toggle", raise_e=False, timeout=10)
    
    def get_smart_sense_tooltip_text(self):
        return self.driver.get_attribute("smart_sense_tooltip", "Name",  timeout = 10)
    
    def get_cool_tooltip_text(self):
        return self.driver.get_attribute("cool_tooltip", "Name",  timeout = 10)

    def get_quiet_tooltip_text(self):
        return self.driver.get_attribute("quiet_tooltip", "Name",  timeout = 10)
    
    def get_performance_tooltip_text(self):
        return self.driver.get_attribute("performance_tooltip", "Name",  timeout = 10)
    
    def get_optimize_oled_tooltip_text(self):
        return self.driver.get_attribute("optimize_oled_tooltip", "Name",  timeout = 10)
    
    def verify_high_performance_mode_show(self):
        return self.driver.wait_for_object("high_performance_text", raise_e=False, timeout=10)

    def verify_smart_sence_tips_icon_show(self):
        return self.driver.wait_for_object("smart_sense_tips_icon", raise_e=False, timeout=10)

    def click_smart_sence_tips_icon(self):
        self.driver.click("smart_sense_tips_icon", timeout=10)

    def get_smart_sence_tips(self):
        return self.driver.get_attribute("smart_sense_tips_icon", "Name", timeout=10)

    def verify_balanced_title_show(self):
        return self.driver.wait_for_object("system_control_balanced_title", raise_e=False, timeout=10)

    def verify_balanced_tips_icon_show(self):
        return self.driver.wait_for_object("system_control_balanced_tips_icon", raise_e=False, timeout=10)

    def click_balanced_icon(self):
        self.driver.click("system_control_balanced_tips_icon", timeout=10)

    def get_balanced_tips(self):
        return self.driver.get_attribute("system_control_balanced_tips_icon", "Name", timeout=10)

    def verify_cool_tips_icon_show(self):
        return self.driver.wait_for_object("system_control_cool_tips_icon", raise_e=False, timeout=10)
    
    def click_cool_tips_icon(self):
        self.driver.click("system_control_cool_tips_icon", timeout=10)

    def get_cool_tips(self):
        return self.driver.get_attribute("system_control_cool_tips_icon", "Name", timeout=10)

    def verify_power_saver_tips_icon_show(self):
        return self.driver.wait_for_object("system_control_powersaver_tips_icon", raise_e=False, timeout=10)
    
    def click_power_saver_tips_icon(self):
        self.driver.click("system_control_powersaver_tips_icon", timeout=10)

    def get_power_saver_tips(self):
        return self.driver.get_attribute("system_control_powersaver_tips_icon", "Name", timeout=10)

    def verify_quiet_tips_icon_show(self):
        return self.driver.wait_for_object("system_control_quiet_tips_icon", raise_e=False, timeout=10)
    
    def click_quiet_tips_icon(self):
        self.driver.click("system_control_quiet_tips_icon", timeout=10)

    def get_quiet_tips(self):
        return self.driver.get_attribute("system_control_quiet_tips_icon", "Name", timeout=10)

    def verify_performanced_tips_icon_show(self):
        return self.driver.wait_for_object("system_control_performance_tips_icon", raise_e=False, timeout=10)
    
    def click_performanced_tips_icon(self):
        self.driver.click("system_control_performance_tips_icon", timeout=10)

    def get_performanced_tips(self):
        return self.driver.get_attribute("system_control_performance_tips_icon", "Name", timeout=10)

    def verify_dim_background_window_tips_icon_show(self):
        return self.driver.wait_for_object("dim_background_window_tips_icon", raise_e=False, timeout=10)
    
    def click_dim_background_window_tips_icon(self):
        self.driver.click("dim_background_window_tips_icon", timeout=10)

    def get_dim_background_window_tips(self):
        return self.driver.get_attribute("dim_background_window_tips_icon", "Name", timeout=10)
    
    def verify_dim_background_toggle_show(self):
        return self.driver.wait_for_object("dim_background_toggle", raise_e=False, timeout=10)
    
    def verify_dim_background_toggle_default_state(self):
        return self.driver.get_attribute("dim_background_toggle", "Toggle.ToggleState",  timeout = 10)
    
    def click_return_button_on_top_left_corner(self):
        self.driver.click("return_button_on_top_left_corner", timeout = 15)
    
    def click_windows_energy_saver_item(self):
        self.driver.click("windows_energy_save_open_button", timeout = 15)
    
    def click_windows_energy_saver_button(self):
        self.driver.click("windows_energy_save_button", timeout = 15)
    
    def verify_windows_energy_saver_button_state(self):
        return self.driver.get_attribute("windows_energy_save_button", "Toggle.ToggleState",  timeout = 10)
    
    def verify_energy_saver_enabled_title_show(self):
        return self.driver.get_attribute("energy_saver_enable_text", "Name", raise_e=False, timeout=20)
    
    def click_optimize_oled_toggle(self):
        self.driver.click("optimize_oled_toggle", timeout=10)
    
    def get_optimize_oled_toggle_state(self):
        return self.driver.get_attribute("optimize_oled_toggle", "Toggle.ToggleState",  timeout = 10)

    def verify_energy_saver_enabled_banner_show(self):
        return self.driver.wait_for_object("energy_saver_enabled_banner", raise_e=False, timeout=10)
    
    def get_energy_saver_enabled_banner_description_text(self):
        return self.driver.get_attribute("energy_saver_enabled_banner_description_text", "Name", raise_e=False, timeout=10) 
    
    def get_power_mode_text_state_in_system_settings(self):
        return self.driver.get_attribute("power_mode_text_state_in_system_settings", "Name", raise_e=False, timeout=10)
    
    def open_system_settings_power_and_battery(self):
        self.driver.ssh.send_command('powershell start ms-settings:powersleep', timeout=10)
    
    def click_smart_resource_optimizer_toggle(self):
        self.driver.click("smart_resource_optimizer_toggle", timeout=10)
    
    def verify_smart_resource_optimizer_toggle_show(self):
        return self.driver.wait_for_object("smart_resource_optimizer_toggle", raise_e=False, timeout=10)
    
    def get_smart_resource_optimizer_description(self):
        return self.driver.get_attribute("smart_resource_optimizer_description", "Name", raise_e=False, timeout=10)
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_system_control_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("system_control_title", raise_e=False, timeout=10)    
    
    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_system_control_performance_control_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("system_control_performance_control_title", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_system_control_cool_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("system_control_cool_title", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_system_control_focus_mode_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("foucus_mode_title", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_system_control_dim_background_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("dim_background_title", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_smart_sense_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        if self.driver.wait_for_object("smart_sense_title_commercial", raise_e=False, timeout=10) is not False:
            return True
        elif self.driver.wait_for_object("smart_sense_title_consumer", raise_e=False, timeout=10) is not False:
            return True
        else:
            return False

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_power_saving_mode_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("power_saving_mode_title", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["machine_name", "page_number", "text_size"], pass_ratio=0.03)
    def verify_optimize_oled_title_show_image(self, machine_name, page_number, element, text_size=100, raise_e=True):
        return self.driver.wait_for_object("optimize_oled_title", raise_e=False, timeout=10)

    @screenshot_compare(pass_ratio=0.03)
    def verify_color_filter(self):
        return self.driver.wait_for_object("system_control_title", raise_e=False, timeout=10)

    @screenshot_compare(pass_ratio=0.03)
    def verify_color_filter_commercial(self):
        return self.driver.wait_for_object("system_control_title", raise_e=False, timeout=10)

    @screenshot_compare(include_param=["mode"], pass_ratio=0.03)
    def verify_system_control_title_show_mode(self, mode):
        return self.driver.wait_for_object("system_control_title", raise_e = False, timeout = 10)
    
    @screenshot_compare(include_param=["mode"])
    def verify_power_saving_mode_title_show_mode(self, mode):
        return self.driver.wait_for_object("power_saving_mode_title", raise_e=False, timeout=10)
    
    def verify_energy_saver_enabled_banner_description_show(self):
        return self.driver.wait_for_object("energy_saver_enabled_banner_description_text", raise_e=False, timeout=10)