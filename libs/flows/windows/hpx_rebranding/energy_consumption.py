from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time
import logging
from selenium.webdriver.common.keys import Keys
from SAF.decorator.saf_decorator import screenshot_compare


class EnergyConsumption(HPXRebrandingFlow):
    flow_name = "energy_consumption"

    def verify_energy_consumption(self):
        return self.driver.wait_for_object("energy_consumption", raise_e=False, timeout = 20)

    def click_energy_consumption(self):
        self.driver.click("energy_consumption", timeout = 40)

    def verify_energy_consumption_header(self):
        return self.driver.wait_for_object("energy_consumption_header", raise_e=False, timeout = 30)

    def verify_consumption_trends_dropdown(self):
        return self.driver.wait_for_object("consistency_check_dropdown", raise_e=False, timeout = 20)

    def select_value_from_consumption_trends_dropdown(self, option):
        self.driver.click("consistency_check_dropdown", timeout = 20)
        self.driver.click(option, timeout = 20)

    def get_consumption_trends_dropdown_selected_option(self):
        return self.driver.get_attribute("consistency_check_dropdown", "Value.Value", timeout = 20)

    def verify_option_from_consumption_trends_dropdown(self, option):
        return self.driver.wait_for_object(option, raise_e=False, timeout = 20)

    def verify_consumption_trends_subtitle_dropdown(self):
        return self.driver.wait_for_object("consumption_trends_subtitle", raise_e=False, timeout = 20)

    def click_on_consumption_trends_dropdown(self):
        self.driver.click("consistency_check_dropdown", timeout = 20)

    def verify_how_to_adjust_power_and_sleep_settings_in_windows_link(self):
        return self.driver.wait_for_object("how_to_adjust_power_and_sleep_settings_in_windows_link", raise_e=False)
    
    def verify_caring_for_your_battery_in_windows_link(self):
        return self.driver.wait_for_object("caring_for_your_battery_in_windows_link", raise_e=False)
    
    def verify_battery_saving_tips_for_windows_link(self):
        return self.driver.wait_for_object("battery_saving_tips_for_windows_link", raise_e=False)
    
    def verify_change_the_power_mode_for_your_windows_pc_link(self):
        return self.driver.wait_for_object("change_the_power_mode_for_your_windows_pc_link", raise_e=False)
    
    def verify_manage_background_activity_for_apps_in_windows_link(self):
        return self.driver.wait_for_object("manage_background_activity_for_apps_in_windows_link", raise_e=False)
    
    def verify_learn_more_about_energy_recommendations_microsoft_support_link(self):
        return self.driver.wait_for_object("learn_more_about_energy_recommendations_microsoft_support_link", raise_e=False)

    def click_how_to_adjust_power_and_sleep_settings_in_windows_link(self):
        self.driver.click("how_to_adjust_power_and_sleep_settings_in_windows_link")
    
    def get_webpage_url(self):
        return self.driver.get_attribute("power_sleep_setting_webpage_url","Value.Value")
    
    def click_caring_for_your_battery_in_windows_link(self):
        self.driver.click("caring_for_your_battery_in_windows_link")
    
    def click_battery_saving_tips_for_windows_link(self):
        self.driver.click("battery_saving_tips_for_windows_link")
    
    def click_change_the_power_mode_for_your_windows_pc_link(self):
        self.driver.click("change_the_power_mode_for_your_windows_pc_link")

    def click_manage_background_activity_for_apps_in_windows_link(self):
        self.driver.click("manage_background_activity_for_apps_in_windows_link")
    
    def click_learn_more_about_energy_recommendations_microsoft_support_link(self):
        self.driver.click("learn_more_about_energy_recommendations_microsoft_support_link")
    
    def verify_hp_logo(self):
        return self.driver.wait_for_object("hp_logo", raise_e=False)
    
    def verify_energy_recommendation_logo(self):
        return self.driver.wait_for_object("energy_recommendation_logo", raise_e=False)
    
    def get_hp_excite_msg(self):
        return self.driver.get_attribute("hp_excite_msg", "Name")
    
    def click_go_beyond_hyperlink(self):
        self.driver.click("go_beyond_hyperlink")

    def click_small_go_beyond_hyperlink(self,element):
        time.sleep(5)
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        el.send_keys(Keys.ENTER)
       
    
    def click_download_report_button(self):
        self.driver.click("download_report_button")

    def verify_update_bios_message(self):
        is_header = self.driver.wait_for_object("update_bios", raise_e=False, timeout = 20)
        is_description = self.driver.wait_for_object("update_bios_description", raise_e=False, timeout = 20)
        return is_header and is_description
    
    def verify_learn_more_link(self):
        return self.driver.wait_for_object("learn_more_link", raise_e=False)
    
    def verify_data_unavailable_label(self):
        return self.driver.wait_for_object("data_unavailable", raise_e=False)
    
    def verify_total_energy_consumption(self):
        return self.driver.wait_for_object("total_energy_consumption", raise_e=False)

    def verify_product_carbon_footprint_link(self):
        return self.driver.wait_for_object("product_carbon_footprint_link", raise_e=False)
    
    def click_product_carbon_footprint_link_text(self):
        self.driver.click("product_carbon_footprint_link")
    
    def verify_energy_environment_link(self):
        return self.driver.wait_for_object("energy_environment_link", raise_e=False)
    
    def click_energy_environment_link(self):
        self.driver.click("energy_environment_link")
    
    def verify_product_carbon_footprint_report_title(self):
        return self.driver.wait_for_object("product_carbon_footprint_report_title", raise_e=False)
    
    def verify_epa_home_page_title(self):
        return self.driver.wait_for_object("epa_home_page_title", raise_e=False)
    
    def verify_energy_environment_report_title(self):
        return self.driver.wait_for_object("energy_environment_report_title", raise_e=False)
    
    def click_myhp_on_task_bar(self):
        self.driver.click("myhp_on_task_bar", timeout= 20)
    
    def click_ok_btn(self):
        if self.driver.wait_for_object("btn_ok", raise_e=False):
           self.driver.click("btn_ok", timeout= 20) 
    
    def verify_data_consumption_header(self):
        return self.driver.wait_for_object("data_consumption_header", raise_e=False)

    def verify_energy_consumption_header_text(self):
        return self.driver.wait_for_object("energy_consumption_header_text", raise_e=False, timeout=15) is not False
    
    def select_value_from_total_energy_consumption_dropdown(self, option):
        self.driver.click("total_energy_consumption_dropdown", timeout = 20)
        self.driver.click(option, timeout = 20)
    
    def click_show_more_button(self):
        self.driver.click("total_energy_consumption_show_more_button",timeout = 20)
        
    def click_show_less_button(self):
        self.driver.click("total_energy_consumption_show_less_button",timeout = 20)
    
    def click_total_energy_consumption_dropdown(self):
        self.driver.click("total_energy_consumption_dropdown", timeout = 20)
    
    def verify_last_week_option(self):
        return self.driver.get_attribute("last_week", "Name", timeout = 10)

    def verify_last_month_option(self):
        return self.driver.get_attribute("last_month", "Name", timeout = 10)

    def select_last_month_option(self):
        self.driver.click("last_month", timeout = 10)

    def get_collect_data_text_on_energy_consumption_page(self):
        return self.driver.get_attribute("collect_data_text_on_energy_consumption_page", "Name", timeout = 10)

    @screenshot_compare(root_obj="energy_consumption_module_page", pass_ratio=0.01)
    def verify_color_filter(self):
        return self.driver.wait_for_object("energy_consumption_header", raise_e=False, timeout=10)

    @screenshot_compare(root_obj="energy_consumption_module_page", include_param=["machine_type", "percent"], pass_ratio=0.02)
    def verify_magnifier(self, machine_type, percent):
        return self.driver.wait_for_object("energy_consumption_header", raise_e=False, timeout=10)
    
    @screenshot_compare(root_obj="energy_consumption_module_page",include_param=["machine_name", "page_number","mode"], pass_ratio=0.01)
    def verify_energy_consumption_page(self, machine_name, page_number, element, mode, raise_e=True):
        return self.driver.wait_for_object(element, raise_e=raise_e, timeout=10)
    
    def verify_and_navigate_energy_consumption_page(self):
        title_element = self.verify_energy_consumption_header()
        if title_element is False:
            logging.info("Energy Consumption page is not opened, navigating to Energy Consumption page")
            self.close_myHP()
            self.launch_myHP()
            time.sleep(2)
            self.maximize_and_verify_device_card()
            self.swipe_window(direction="down", distance=2)
            assert self.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Energy consumption card is not displayed"
            self.fd["devices_details_pc_mfe"].click_energy_consumption_card()
            time.sleep(2)   
        else:
            logging.info("Energy Consumption page is already opened")
