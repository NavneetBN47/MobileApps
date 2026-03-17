from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time
from selenium.webdriver.common.keys import Keys
from SAF.decorator.saf_decorator import screenshot_compare
import logging
import re

class Battery(HPXRebrandingFlow):
    flow_name = "battery"

    def verify_battery_manager_title_ltwo(self):
        return self.driver.wait_for_object("battery_manager_title_ltwo", raise_e=False, timeout=15) is not False

    def verify_battery_information_title_ltwo(self):
        return self.driver.wait_for_object("battery_information_title_ltwo", raise_e=False, timeout=40) is not False

    def verify_charging_option_title_ltwo(self):
        return self.driver.wait_for_object("charging_option_title_ltwo", raise_e=False, timeout=20) is not False

    def verify_schedule_battery_radio_button_ltwo(self):
        return self.driver.wait_for_object("schedule_battery_radio_button_ltwo", raise_e=False, timeout=15) is not False

    def verify_maximize_battery_health_management_radio_button_ltwo(self):
        return self.driver.wait_for_object("maximize_battery_health_management_radio_button_ltwo", raise_e=False, timeout=15) is not False

    def verify_optimize_battery_performancet_radio_button_ltwo(self):
        return self.driver.wait_for_object("optimize_battery_performance_radio_button_ltwo", raise_e=False, timeout=15) is not False

    def get_charging_option_description_ltwo(self):
        return self.driver.get_attribute("charging_option_description_ltwo", "Name", timeout=15)

    def get_optimize_battery_performance_title_ltwo(self):
        return self.driver.get_attribute("optimize_battery_performance_title_ltwo", "Name", timeout=15)

    def get_maximize_battery_health_management_title_ltwo(self):
        return self.driver.get_attribute("maximize_battery_health_management_title_ltwo", "Name", timeout=15)

    def get_schedule_battery_charging_title_ltwo(self):
        return self.driver.get_attribute("schedule_battery_charging_title_ltwo", "Name", timeout=15)

    def click_schedule_battery_radio_button_ltwo(self):
        self.driver.click("schedule_battery_radio_button_ltwo", timeout=15)

    def get_threshold_dropdown_ltwo(self):
        return self.driver.get_attribute("threshold_dropdown_ltwo", "Name", timeout=15)

    def verify_reset_schedule_button_ltwo(self):
        return self.driver.wait_for_object("reset_schedule_button_ltwo", raise_e=False, timeout=15) is not False

    def click_reset_schedule_button_ltwo(self):
        self.driver.click("reset_schedule_button_ltwo", timeout=20)

    def get_start_time_sunday_ltwo(self):
        return self.driver.get_attribute("start_time_sunday_ltwo", "Name", timeout=15)
    
    def get_end_time_sunday_ltwo(self):
        return self.driver.get_attribute("end_time_sunday_ltwo", "Name", timeout=15)

    def get_time_difference_sunday_ltwo(self):
        return self.driver.get_attribute("time_difference_sunday_ltwo", "Name", timeout=30)

    def click_start_time_sunday_ltwo(self):
        self.driver.click("start_time_sunday_ltwo", timeout=30)

    def click_end_time_sunday_ltwo(self):
        self.driver.click("end_time_sunday_ltwo", timeout=30)

    def click_start_time_monday_ltwo(self):
        self.driver.click("start_time_monday_ltwo", timeout=30)

    def click_end_time_monday_ltwo(self):
        self.driver.click("end_time_monday_ltwo", timeout=30)

    def click_start_time_tuesday_ltwo(self):
        self.driver.click("start_time_tuesday_ltwo", timeout=30)

    def click_end_time_tuesday_ltwo(self):
        self.driver.click("end_time_tuesday_ltwo", timeout=30)

    def click_start_time_wednesday_ltwo(self):
        self.driver.click("start_time_wednesday_ltwo", timeout=30)

    def click_end_time_wednesday_ltwo(self):
        self.driver.click("end_time_wednesday_ltwo", timeout=30)

    def click_start_time_thursday_ltwo(self):
        self.driver.click("start_time_thursday_ltwo", timeout=30)

    def click_end_time_thursday_ltwo(self):
        self.driver.click("end_time_thursday_ltwo", timeout=30)
        
    def click_start_time_friday_ltwo(self):
        self.driver.click("start_time_friday_ltwo", timeout=30)  

    def click_end_time_friday_ltwo(self):
        self.driver.click("end_time_friday_ltwo", timeout=30)      

    def click_start_time_saturday_ltwo(self):
        self.driver.click("start_time_saturday_ltwo", timeout=30)     

    def click_end_time_saturday_ltwo(self):
        self.driver.click("end_time_saturday_ltwo", timeout=30)   

    def click_sunday_twelve_am_option_ltwo(self):
        self.driver.click("sunday_twelve_am_option_ltwo", timeout=15)

    def click_monday_twelve_am_option_ltwo(self):
        self.driver.click("monday_twelve_am_option_ltwo", timeout=15)

    def click_monday_one_am_option_ltwo(self):
        self.driver.click("monday_one_am_option_ltwo", timeout=15)   

    def click_tuesday_twelve_am_option_ltwo(self):
        self.driver.click("tuesday_twelve_am_option_ltwo", timeout=15)

    def click_tuesday_one_am_option_ltwo(self):
        self.driver.click("tuesday_one_am_option_ltwo", timeout=15)         

    def click_wednesday_twelve_am_option_ltwo(self):
        self.driver.click("wednesday_twelve_am_option_ltwo", timeout=15)

    def click_wednesday_one_am_option_ltwo(self):
        self.driver.click("wednesday_one_am_option_ltwo", timeout=15) 

    def click_thursday_twelve_am_option_ltwo(self):
        self.driver.click("thursday_twelve_am_option_ltwo", timeout=15)

    def click_thursday_one_am_option_ltwo(self):
        self.driver.click("thursday_one_am_option_ltwo", timeout=15) 

    def click_friday_twelve_am_option_ltwo(self):
        self.driver.click("friday_twelve_am_option_ltwo", timeout=15)

    def click_friday_one_am_option_ltwo(self):
        self.driver.click("friday_one_am_option_ltwo", timeout=15) 

    def click_saturday_twelve_am_option_ltwo(self):
        self.driver.click("saturday_twelve_am_option_ltwo", timeout=15)

    def click_saturday_one_am_option_ltwo(self):
        self.driver.click("saturday_one_am_option_ltwo", timeout=15) 

    def is_selected_schedule_battery_radio_button_ltwo(self):
        return self.driver.get_attribute("schedule_battery_radio_button_ltwo", "SelectionItem.IsSelected", timeout=15)

    def is_selected_maximize_battery_health_management_radio_button_ltwo(self):
        return self.driver.get_attribute("maximize_battery_health_management_radio_button_ltwo", "SelectionItem.IsSelected", timeout=15)

    def is_selected_optimize_battery_performance_radio_button_ltwo(self):
        return self.driver.get_attribute("optimize_battery_performance_radio_button_ltwo", "SelectionItem.IsSelected", timeout=15)

    def run_deeplink_battery_manager(self):
        self.click_search_bar_on_windows()
        time.sleep(3)
        self.search_bar_on_windows("run")
        self.click_open_tab()
        time.sleep(5)
        self.run_command_to_add_registry_key("hpx://pcbatterymanager")
        time.sleep(5)
        self.click_run_ok_tab()
        time.sleep(5)

    def click_search_bar_on_windows(self):
        self.driver.click("search_bar_on_windows")

    def search_bar_on_windows(self,app_name):
        self.driver.send_keys("search_bar_on_windows", app_name)

    def run_command_to_add_registry_key(self,command):
        self.driver.send_keys("run_text_box",command)

    def click_open_tab(self):
        self.driver.click("app_open")    

    def click_run_ok_tab(self):
        self.driver.click("run_ok_button", timeout = 30)

    def verify_maximize_battery_health_title_ltwo_consumer(self):
        return self.driver.wait_for_object("maximize_battery_health_management_title_ltwo", raise_e=False, timeout=15) is not False

    def verify_maximize_battery_health_description_ltwo_consumer(self):
        return self.driver.wait_for_object("maximize_battery_health_description_ltwo_consumer", raise_e=False, timeout=15) is not False

    def verify_battery_manager_title_ltwo_commercial(self):
        return self.driver.wait_for_object("battery_manager_title_ltwo_commercial", raise_e=False, timeout=15) is not False
    
    def get_optimize_battery_performance_description_ltwo(self):
        return self.driver.get_attribute("optimize_battery_performance_description", "Name", timeout=15)

    def get_maximize_battery_health_description_ltwo(self):
        return self.driver.get_attribute("maximize_battery_health_description", "Name", timeout=15)

    def get_schedule_battery_charging_description_ltwo(self):
        return self.driver.get_attribute("schedule_battery_charging_description", "Name", timeout=15)
    
    def click_twelve_thirty_am_option_start_time_ltwo(self):
        self.driver.click("twelve_thirty_am_option_start_time_ltwo", timeout= 20)

    def click_end_time_sunday_dropbox_ltwo(self):
        self.driver.click("end_time_sunday_dropbox_ltwo", timeout=20)

    def click_one_am_option_end_time_ltwo(self):
        self.driver.click("one_am_option_end_time_ltwo", timeout=10)

    def verify_start_charging_notification(self):
        return self.driver.wait_for_object("start_charging_notification", raise_e=False, timeout=3) is not False
    
    def verify_end_charging_notification(self):
        return self.driver.wait_for_object("end_charging_notification", raise_e=False, timeout=10) is not False

    def click_twelve_thirty_endtime_sunday(self):
        self.driver.click("twelve_thirty_endtime_sunday", timeout=20)

    def click_notifications_in_windows_notification_clearup(self):
        self.driver.click("notifications_in_windows_notification_clearup", raise_e=False, timeout=30)

    def verify_notifications_in_windows_notification_for_myhp(self):
        return self.driver.wait_for_object("notifications_in_windows_notification_for_myhp", raise_e=False, timeout=20) is not False
    
    def click_end_time_sunday_tweleve_am_ltwo(self):
        self.driver.click("end_time_sunday_tweleve_am_ltwo", timeout=30)

    def get_error_invalid_start_time_ltwo(self):
        return self.driver.get_attribute("error_invalid_start_time_ltwo", "Name", timeout=15)
    
    def get_error_invalid_end_time_ltwo(self):
        return self.driver.get_attribute("error_invalid_end_time_ltwo", "Name", timeout=15)
    
    def click_optimize_battery_performance_radio_button_ltwo(self):
        self.driver.click("optimize_battery_performance_radio_button_ltwo", timeout=30)

    def click_start_charging_notification(self):
        self.driver.click("start_charging_notification_from_task_bar", timeout=30)
    
    def click_notification_tab_with_notification_taskbar(self):
        self.driver.click("notification_tab_with_notification_taskbar", timeout=30)

    def click_end_charging_notification(self):
        self.driver.click("end_charging_notification_from_task_bar", timeout=30)

    def click_charging_options_info(self):
        return self.driver.click("charging_options_info", timeout=15)
    
    def verify_charging_options_tooltip(self):
        return self.driver.wait_for_object("charging_options_tooltip", raise_e=False, timeout=30) is not False

    def click_maximum_capacity_info(self):
        return self.driver.click("maximum_capacity_info", timeout=15)
    
    def verify_maximum_capacity_tooltip(self):
        return self.driver.wait_for_object("maximum_capacity_tooltip", raise_e=False, timeout=30) is not False

    def click_maximize_battery_health_radio_button_ltwo(self):
        return self.driver.click("maximize_battery_health_management_radio_button_ltwo", timeout=15)
      
    def get_temperature_value_ltwo(self):    
        return self.driver.get_attribute("temperature_value_ltwo", "Name", timeout=15)
    
    def get_serial_number_value_ltwo(self):
        return self.driver.get_attribute("serial_number_value_ltwo", "Name", timeout=15)

    def get_battery_information_title_ltwo(self):
        return self.driver.get_attribute("battery_information_title_ltwo", "Name", timeout=15)

    def verify_battery_state(self):
        return self.driver.wait_for_object("battery_state", raise_e=False, timeout=30) is not False
    
    def get_current_battery_percentage_text(self):
        return self.driver.get_attribute("battery_state", "Name", timeout=20)
    
    def verify_max_capacity(self):
        return self.driver.wait_for_object("battery_maximum_capacity_value", raise_e=False, timeout=30) is not False
    
    def get_max_capacity_text(self):
        return self.driver.get_attribute("battery_maximum_capacity_value", "Name", timeout=20)
    
    def verify_battery_new_capacity_value(self):
        return self.driver.wait_for_object("battery_new_capacity_value", raise_e=False, timeout=30) is not False    
    
    def get_new_capacity_text(self):
        return self.driver.get_attribute("battery_new_capacity_value", "Name", timeout=20)
    
    def verify_maximize_battery_health_management_radio_button(self):
        return self.driver.wait_for_object("maximize_battery_health_management_radio_button", raise_e=False, timeout=30) is not False
    
    def click_maximize_battery_health_management_radio_button_ltwo(self):
        self.driver.click("maximize_battery_health_management_radio_button", timeout=30)

    def verify_when_plugged_in_threshold_dropdown(self):
        return self.driver.wait_for_object("when_plugged_in_threshold_dropdown", raise_e=False, timeout=30) is not False
    
    def get_when_plugged_in_threshold_dropdown_value(self):
        return self.driver.get_attribute("when_plugged_in_threshold_dropdown", "Name", timeout=30)
    
    def click_when_plugged_in_threshold_dropdown(self):
        for _ in range(3):
            if bool(self.driver.wait_for_object("when_plugged_in_threshold_10_percent", raise_e=False, timeout=10)) is True:
                break
            else:
                self.driver.click("when_plugged_in_threshold_dropdown", timeout=30)

    def click_when_plugged_in_threshold_10_percent(self):
        self.driver.click("when_plugged_in_threshold_10_percent", timeout=30)

    def click_when_plugged_in_threshold_20_percent(self):
        self.driver.click("when_plugged_in_threshold_20_percent", timeout=30)

    def click_when_plugged_in_threshold_30_percent(self):
        self.driver.click("when_plugged_in_threshold_30_percent", timeout=30)
    
    def click_when_plugged_in_threshold_40_percent(self):
        self.driver.click("when_plugged_in_threshold_40_percent", timeout=30)

    def click_when_plugged_in_threshold_50_percent(self):
        self.driver.click("when_plugged_in_threshold_50_percent", timeout=30)

    def click_when_plugged_in_threshold_60_percent(self):
        self.driver.click("when_plugged_in_threshold_60_percent", timeout=30)
    
    def click_when_plugged_in_threshold_70_percent(self):
        self.driver.click("when_plugged_in_threshold_70_percent", timeout=30)

    def click_when_plugged_in_threshold_80_percent(self):
        self.driver.click("when_plugged_in_threshold_80_percent", timeout=30)

    def click_when_plugged_in_threshold_90_percent(self):
        self.driver.click("when_plugged_in_threshold_90_percent", timeout=30)

    def navigate_threshold_list_menu(self, value = 5):
        el = self.driver.wait_for_object("when_plugged_in_threshold_dropdown", raise_e=False, timeout=30)
        self.driver.click("when_plugged_in_threshold_dropdown", timeout=30)
        el.send_keys(str(value))
        
    def get_charging_option_title_ltwo(self):
        return self.driver.get_attribute("charging_option_title_ltwo", "Name", timeout=15)
    
    def get_charging_option_tooltip(self):
        return self.driver.get_attribute("charging_options_info", "Name", timeout=15)
    
    def get_battery_scheduler_days_title_ltwo(self):
        return self.driver.get_attribute("scheduler_days_title_ltwo", "Name", timeout=15)
    
    def get_battery_scheduler_start_time_title_ltwo(self):
        return self.driver.get_attribute("scheduler_start_time_title_ltwo", "Name", timeout=15)
    
    def get_battery_scheduler_end_time_title_ltwo(self):
        return self.driver.get_attribute("scheduler_end_time_title_ltwo", "Name", timeout=15)
    
    def get_scheduler_total_hours_title_ltwo(self):
        return self.driver.get_attribute("scheduler_total_hours_title_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_sunday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_sunday_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_monday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_monday_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_tuesday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_tuesday_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_wednesday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_wednesday_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_thursday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_thursday_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_friday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_friday_ltwo", "Name", timeout=15)
    
    def get_scheduler_days_of_the_week_title_saturday_ltwo(self):
        return self.driver.get_attribute("scheduler_day_of_the_week_saturday_ltwo", "Name", timeout=15)
    
    def get_scheduler_battery_percentage_description_ltwo(self):
        return self.driver.get_attribute("scheduler_battery_percentage_description_ltwo", "Name", timeout=15)
    
    def get_reset_schedule_button_ltwo(self):
        return self.driver.get_attribute("reset_schedule_button_ltwo", "Name", timeout=15)
    
    def get_battery_charging_state(self):
        return self.driver.get_attribute("battery_state_charging_state", "Name", timeout=15)
    
    def get_battery_health_text(self):
        return self.driver.get_attribute("battery_health_value", "Name", timeout=15)

    def get_battery_new_capacity_text(self):
        return self.driver.get_attribute("battery_new_capacity_value", "Name", timeout=15)

    def click_maximize_battery_health_radio_button_ltwo(self):
        return self.driver.click("maximize_battery_health_management_radio_button_ltwo", timeout=15)
    
    def click_sunday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("sunday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def click_monday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("monday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def click_tuesday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("tuesday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def click_wednesday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("wednesday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def click_thursday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("thursday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def click_friday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("friday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def click_saturday_eleven_fifty_nine_pm_option_ltwo(self):
        return self.driver.click("saturday_eleven_fifty_nine_pm_option_ltwo", timeout=15)
    
    def navigate_to_eleven_fifty_nine_pm_option_ltwo(self, current_day):
        end_time_date_list_box = f"{current_day}_end_time_list_box_ltwo"
        el = self.driver.wait_for_object(end_time_date_list_box, raise_e=False, timeout=30)
        el.send_keys(Keys.DOWN, Keys.DOWN, Keys.UP)
    
    def check_methods_exist(self, method_names):
        # Ensure that all dynamically generated methods exist
        for method_name in method_names:
            if not hasattr(self, method_name):
                raise AttributeError(f"Method '{method_name}' not found in Battery class. Check method names.")

    def set_start_time_this_morning(self, current_day):
        # Dynamically construct method names
        use_click_start_time_date_method = f"click_start_time_{current_day}_ltwo"
        use_click_start_time_method = f"click_{current_day}_twelve_am_option_ltwo"
        self.check_methods_exist([use_click_start_time_date_method, use_click_start_time_method])

        # Click start time selection
        getattr(self, use_click_start_time_date_method)()
        time.sleep(1)
        getattr(self, use_click_start_time_method)()
        time.sleep(1)
        return [use_click_start_time_date_method, use_click_start_time_method] # Navigating lists can cause app to lose focus. Providing list of methods to retry once app has focus
    
    def set_end_time_tonight(self, current_day):
        # Dynamically construct method names
        use_click_end_time_date_method = f"click_end_time_{current_day}_ltwo"
        use_click_end_time_method = f"click_{current_day}_eleven_fifty_nine_pm_option_ltwo"
        self.check_methods_exist([use_click_end_time_date_method, use_click_end_time_method])
       
        self.navigate_to_eleven_fifty_nine_pm_option_ltwo(current_day)
        getattr(self, use_click_end_time_method)() #click end time selection
        return [ use_click_end_time_date_method, use_click_end_time_method] # Navigating lists can cause app to lose focus. Providing list of methods to retry once app has focus

    def single_scroll_up_sunday_start_time_list_box(self,sunday_start_time):
        sunday_start_time = self.driver.wait_for_object(sunday_start_time, raise_e=False, timeout=30)
        sunday_start_time.send_keys(Keys.UP)

    def verify_battery_state_charging_state(self):
        return self.driver.wait_for_object("battery_state_charging_state", raise_e=False, timeout=15) is not False
    
    def click_Sunday_twelve_am_option_ltwo(self):
        self.driver.click("sunday_twelve_am_option_ltwo", timeout=15)
    
    def get_battery_card_contextual_text(self):
        return self.driver.get_attribute("battery_card_contextual_text", "Name", timeout=15)

    def verify_battery_icon_in_front_of_state(self):
        return self.driver.wait_for_object("battery_icon_in_front_of_state", raise_e=False, timeout=15) is not False

    def click_maximum_capacity_tooltip(self):
        self.driver.click("maximum_capacity_tooltip", timeout=15)
    
    def click_charging_options_tooltip(self):
        self.driver.click("charging_options_tooltip", timeout=15)

    def verify_minimize_battery_title_ltwo(self):
        return self.driver.wait_for_object("battery_minimize_battery_health_title",  raise_e=False, timeout=15)

    def verify_minimize_battery_description_ltwo(self):
        return self.driver.wait_for_object("battery_minimize_battery_health_description",  raise_e=False, timeout=15)

    def verify_minimize_battery_radio_button_ltwo(self):
        return self.driver.wait_for_object("battery_minimize_battery_health_radio_button", raise_e=False, timeout=15)

    def click_miniimize_battery_health_radio_button_ltwo(self):
        self.driver.click("battery_minimize_battery_health_radio_button", timeout=15)

    def is_selected_miniimize_battery_health_radio_button_ltwo(self):
        return self.driver.get_attribute("battery_minimize_battery_health_radio_button", "SelectionItem.IsSelected", timeout=15)
    
    def get_start_charging_notification_text(self):
        return self.driver.get_attribute("start_charging_notification", "Name", timeout=30)

    def get_maximize_battery_health_toggle(self):
        return self.driver.get_attribute("maximize_battery_health_toggle", "Toggle.ToggleState", timeout=15)
    
    def click_maximize_battery_health_toggle(self):
        self.driver.click("maximize_battery_health_toggle", timeout=15)

    # ========== LOCALIZATION METHODS ==========

    def get_battery_manager_title_ltwo_commercial(self):
        return self.driver.get_attribute("battery_manager_title_ltwo_commercial", "Name", timeout=15)
    
    def get_battery_manager_state_text(self):
        return self.driver.get_attribute("battery_manager_state_text", "Name", timeout=15)

    def get_battery_manager_new_capacity_text(self):
        return self.driver.get_attribute("battery_manager_new_capacity_text", "Name", timeout=15)

    def get_battery_manager_max_capacity_text(self):
        return self.driver.get_attribute("battery_manager_max_capacity_text", "Name", timeout=15)
    
    def get_maximum_capacity_title_ltwo(self):
        return self.driver.get_attribute("maximum_capacity_title_ltwo", "Name", timeout=15)
    
    def get_maximum_capacity_tooltip(self):
        return self.driver.get_attribute("maximum_capacity_tooltip", "Name", timeout=15)

    def get_battery_manager_temperature_text(self):
        return self.driver.get_attribute("battery_manager_temperature_text", "Name", timeout=15)
    
    def get_battery_manager_serial_number_text(self):
        return self.driver.get_attribute("battery_manager_serial_number_text", "Name", timeout=15)

    def get_battery_minimize_battery_health_title_ltwo(self):
        return self.driver.get_attribute("battery_minimize_battery_health_title_ltwo", "Name", timeout=15)
    
    def get_battery_minimize_battery_health_description(self):
        return self.driver.get_attribute("battery_minimize_battery_health_description", "Name", timeout=15)
        
    def get_hours_from_day_time_diff_from_text(self, text):
        # Remove any space and number from text while preserving all letters (including international characters)
        clean_text = re.sub(r'[\d\s]', '', text)
        logging.info(f"Extracted text after removing numbers and spaces: '{clean_text}' from original: '{text}'")
        return clean_text
        
    def get_battery_health_title_ltwo(self):
        return self.driver.get_attribute("battery_manager_battery_health_text", "Name", timeout=30)
    
    def get_battery_minimize_battery_health_title(self):
        return self.driver.get_attribute("battery_minimize_battery_health_title", "Name", timeout=30)
    
    def get_battery_manager_monday_time_difference_text(self):
        return self.driver.get_attribute("battery_manager_monday_time_difference_text", "Name", timeout=30)
    
    def get_battery_manager_tuesday_time_difference_text(self):
        return self.driver.get_attribute("battery_manager_tuesday_time_difference_text", "Name", timeout=30)

    def get_battery_manager_wednesday_time_difference_text(self):
        return self.driver.get_attribute("battery_manager_wednesday_time_difference_text", "Name", timeout=30)

    def get_battery_manager_thursday_time_difference_text(self):
        return self.driver.get_attribute("battery_manager_thursday_time_difference_text", "Name", timeout=30)

    def get_battery_manager_friday_time_difference_text(self):
        return self.driver.get_attribute("battery_manager_friday_time_difference_text", "Name", timeout=30)

    def get_battery_manager_saturday_time_difference_text(self):
        return self.driver.get_attribute("battery_manager_saturday_time_difference_text", "Name", timeout=30)
    
    def get_battery_manager_start_time_missing_error_text(self):
        return self.driver.get_attribute("battery_manager_start_time_missing_error_text", "Name", timeout=30)
    
    def get_battery_manager_end_time_missing_error_text(self):
        return self.driver.get_attribute("battery_manager_end_time_missing_error_text", "Name", timeout=30)
    
    def extract_percentage_from_text(self, text):
        try:
            match = re.search(r'(\d+)%', text)
            percentage = int(match.group(1))
            logging.info(f"Extracted battery percentage: {percentage}% from text: '{text}'")
            return percentage
        except Exception as e:
            logging.error(f"Error extracting battery percentage from text: {e}")
            return None

    @screenshot_compare(root_obj="battery_module_image",pass_ratio=0.01)
    def verify_color_filter(self):
        return self.driver.wait_for_object("battery_manager_title_ltwo", raise_e=False, timeout=10)

    def click_retask_notification_toast_x_button(self):
        self.driver.click("retask_notification_toast_x_button", timeout=10)

    def get_end_charging_notification_text(self):
        return self.driver.get_attribute("end_charging_notification", "Name", timeout=30)
    
    @screenshot_compare(root_obj="battery_module_image", include_param=["machine_type","reg"], pass_ratio=0.01)
    def verify_battery_ui(self, machine_type, reg):
        return self.driver.wait_for_object("battery_manager_title_ltwo", raise_e=False, timeout=10)
    
    @screenshot_compare(root_obj="battery_module_image", include_param=["page_number","mode"], pass_ratio=0.01)
    def verify_battery_manager_page_ui(self, page_number, mode, element):
        return self.driver.wait_for_object(element, raise_e=False, timeout=10)
    
    @screenshot_compare(root_obj="battery_module_image", include_param=["machine_type", "percent"], pass_ratio=0.01)
    def verify_magnifier(self, machine_type, percent):
        return self.driver.wait_for_object("battery_manager_title_ltwo", raise_e=False, timeout=10)
    
    def get_battery_manager_title_ltwo(self):
        return self.driver.get_attribute("battery_manager_title_ltwo", "Name", timeout=15)
