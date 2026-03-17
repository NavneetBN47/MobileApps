from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction
import time

class EnergyConsumption(HPXFlow):
    flow_name = "energy_consumption"

    def verify_energy_consumption(self):
        return self.driver.wait_for_object("energy_consumption", raise_e=False, timeout = 20)
    
    def click_energy_consumption(self):
        self.driver.click("energy_consumption", timeout = 40)

    def verify_energy_consumption_header(self):
        return self.driver.wait_for_object("energy_consumption_header", raise_e=False)
    
    def verify_setting_module(self):
        return self.driver.wait_for_object("setting_module", raise_e=False)
    
    def click_setting_module(self):
        self.driver.click("setting_module", timeout = 40)

    def verify_about_button(self):
        return self.driver.wait_for_object("about_button", raise_e=False)
    
    def click_about_button(self):
        self.driver.click("about_button", timeout = 40)

    def verify_app_version(self):
        return self.driver.wait_for_object("app_version", raise_e=False)

    def verify_data_consumption_header(self):
        return self.driver.wait_for_object("data_consumption_header", raise_e=False)
    
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
    
    def click_consumption_trend_dropdown(self):
        self.driver.click("consumption_trend_dropdown")
    
    def select_consumption_trend_6_days(self):
        self.driver.click("consumption_trend_6_days")
    
    def select_consumption_trend_6_month(self):
        self.driver.click("consumption_trend_6_month")
    
    def select_consumption_trend_12_hours(self):
        self.driver.click("consumption_trend_12_hours")
    
    def verify_power_consumption_measurement(self):
        return self.driver.wait_for_object("power_consumption_measurement", raise_e=False)
    
    def verify_consumption_trend_description(self):
        return self.driver.wait_for_object("consumption_trend_description", raise_e=False)
        
    def verify_daily_average_text(self):
        return self.driver.wait_for_object("daily_average_text", raise_e=False)

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
    
    def click_download_report_button(self):
        self.driver.click("download_report_button")