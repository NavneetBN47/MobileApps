from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
import time

class Battery(HPXFlow):
    flow_name = "battery"

    def verify_battery_title_show(self):
        return self.driver.wait_for_object("title", raise_e=False, timeout=20)
    
    def get_info_title_text(self):
        return self.driver.get_attribute("info_title","Name")

    def get_new_capacity_text(self):
        return self.driver.get_attribute("new_capacity_text","Name")
    
    def get_max_capacity_text(self):
        return self.driver.get_attribute("max_capacity_text","Name")

    def get_temperature_text(self):
        return self.driver.get_attribute("temperature_text","Name")
    
    def get_battery_health_text(self):
        return self.driver.get_attribute("battery_health_text","Name")
    
    def get_serial_numer_text(self):
        return self.driver.get_attribute("serial_numer_text","Name")
    
    def verify_three_am_item_show(self):
        return self.driver.wait_for_object("three_am_item", raise_e=False, timeout=10)
    
    def click_sunday_dropdown(self):
        self.driver.click("sunday_dropdown")
    
    def click_three_am_item(self):
        self.driver.click("three_am_item")
    
    def click_clear_schedule(self):
        self.driver.click("clear_schedule_btn")
    
    def click_schedule_charging_box(self):
        self.driver.click("battery_charg_checkbox")
    
    def get_charge_option_title_text(self):
        return self.driver.get_attribute("charge_options_title","Name")

    def get_charge_option_subtitle_text(self):
        return self.driver.get_attribute("charge_options_subtitle","Name")
    
    def get_optimize_battery_text(self):
        return self.driver.get_attribute("optimize_battery_text","Name")
    
    def get_max_battery_text(self):
        return self.driver.get_attribute("max_battery_text","Name")

    def get_schdedule_battery_text(self):
        return self.driver.get_attribute("schdedule_battery_text","Name")
    
    def get_health_normal_text(self):
        return self.driver.get_attribute("health_normal","Name")
    
    def click_maximize_charging_box(self):
        self.driver.click("maximize_charg_checkbox")
    
    def click_optimize_charging_box(self):
        self.driver.click("optimize_charg_checkbox")
    
    def click_start_charge_dropdown_list(self):
        self.driver.click("start_charge_dropdown")

    def click_battery_thirty_percent(self):
        self.driver.click("battery_thirty_percent")

    def click_sunday_end_dropdown(self):
        self.driver.click("sunday_end_dropdown")

    def click_four_am_item(self):
        self.driver.click("four_am_item")

    def get_sunday_start_dropdown(self):
        return self.driver.get_attribute("sunday_dropdown","Name")

    def get_sunday_end_dropdown(self):
        return self.driver.get_attribute("sunday_end_dropdown","Name")
    
    def get_start_charge_dropdown_list(self):
        return self.driver.get_attribute("start_charge_dropdown","Name")
    
    def verify_four_am_item_show(self):
        return self.driver.wait_for_object("four_am_item", raise_e=False, timeout=10)
    
    def get_schedule_charging_box_toggle_status(self):
        return self.driver.get_attribute("battery_charg_checkbox","Toggle.ToggleState")
    
    def click_devicename_on_header(self):
        self.driver.click("devicename_on_header")

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

    def add_battery_registry(self):
        self.click_search_bar_on_windows()
        time.sleep(3)
        self.search_bar_on_windows("run")
        self.click_open_tab()
        time.sleep(5)
        self.run_command_to_add_registry_key("powershell -Command \"Start-Process powershell -ArgumentList '-Command New-Item -Path ''HKLM:\SOFTWARE\HP\HP App'' -Name ''BatteryDisabled'' -ItemType Key' -Verb RunAs\"")
        time.sleep(5)
        self.click_run_ok_tab()

    def remove_battery_registry(self):
        self.click_search_bar_on_windows()
        time.sleep(3)
        self.search_bar_on_windows("run")
        self.click_open_tab()
        time.sleep(5)
        self.run_command_to_add_registry_key("powershell -Command \"Start-Process powershell -ArgumentList '-Command Remove-Item -Path ''HKLM:\SOFTWARE\HP\HP App\BatteryDisabled'' -Force -Verbose' -Verb RunAs\"")
        time.sleep(5)
        self.click_run_ok_tab()

    def open_battery_manager_from_run(self):
        self.click_search_bar_on_windows()
        time.sleep(3)
        self.search_bar_on_windows("run")
        self.click_open_tab()
        time.sleep(5)
        self.run_command_to_add_registry_key("hpx://pcbatterymanager")
        time.sleep(5)
        self.click_run_ok_tab()

    def get_charging_text(self):
        return self.driver.get_attribute("charging_text", "Name")
    
    def get_battery_information_header(self):
        return self.driver.get_attribute("battery_information_header", "Name")
    
    def click_maximum_capacity_tool_tip(self):
        self.driver.click("maximum_capacity_tooltip")

    def get_maximum_capacity_tooltip(self):
        return self.driver.get_attribute("maximum_capacity_tooltip", "Name")
    
    def click_charging_option_tooltip(self):
        self.driver.click("charging_option_tooltip")

    def get_charging_option_tooltip(self):
        return self.driver.get_attribute("charging_option_tooltip", "Name")

    def click_optimize_battery_tooltip(self):
        self.driver.click("optimize_battery_tooltip")

    def get_optimize_battery_tooltip(self):
        return self.driver.get_attribute("optimize_battery_tooltip", "Name")
    
    def click_maximize_battery_tooltip(self):
        self.driver.click("maximize_battery_tooltip")

    def get_maximize_battery_tooltip(self):
        return self.driver.get_attribute("maximize_battery_tooltip", "Name")
    
    def click_schedule_battery_tooltip(self):
        self.driver.click("schedule_battery_tooltip")

    def get_schedule_battery_tooltip(self):
        return self.driver.get_attribute("schedule_battery_tooltip", "Name")
    
    def click_schdedule_battery_text_list(self):
        self.driver.click("schdedule_battery_text")

    def get_schedule_battery_description(self):
        return self.driver.get_attribute("schedule_battery_description", "Name")

    def get_days_of_week_text(self):
        return self.driver.get_attribute("days_of_week", "Name")
    
    def get_start_time_text(self):
        return self.driver.get_attribute("start_time", "Name")
    
    def get_end_time_text(self):
        return self.driver.get_attribute("end_time", "Name")
    
    def get_total_text(self):
        return self.driver.get_attribute("total", "Name")
    
    def get_sunday_text(self):
        return self.driver.get_attribute("sunday", "Name")
    
    def get_monday_text(self):
        return self.driver.get_attribute("monday", "Name")
    
    def get_tuesday_text(self):
        return self.driver.get_attribute("tuesday", "Name")
    
    def get_wednesday_text(self):
        return self.driver.get_attribute("wednesday", "Name")
    
    def get_thursday_text(self):
        return self.driver.get_attribute("thursday", "Name")
    
    def get_friday_text(self):
        return self.driver.get_attribute("friday", "Name")
    
    def get_saturday_text(self):
        return self.driver.get_attribute("saturday", "Name")
    
    def get_hours_text(self):
        return self.driver.get_attribute("hrs", "Name")
    
    def get_clear_schedule(self):
        return self.driver.get_attribute("clear_schedule", "Name")
    
    def get_percentage_text(self):
        return self.driver.get_attribute("percentage", "Name")
    
    def get_battery_percentage_text(self):
        return self.driver.get_attribute("battery_percentage", "Name")
    
    def click_time_sunday(self):
        self.driver.click("sunday_dropdown_time")

    def get_error_message_endtime_missing(self):
        return self.driver.get_attribute("error_message_endtime_missing", "Name")
    
    def click_monday_dropdown_button(self):
        self.driver.click("monday_dropdown_button")

    def click_monday_dropdown_time(self):
        self.driver.click("monday_dropdown_time")
        
    def get_error_message_starttime_missing(self):
        return self.driver.get_attribute("error_message_starttime_missing", "Name")

    def get_invalid_end_label(self):
        return self.driver.get_attribute("invalid_end_label", "Name")
    
    def get_invalid_start_label(self):
        return self.driver.get_attribute("invalid_start_label", "Name")
    
    def click_monday_starttime_dropdown_button(self):
        self.driver.click("monday_starttime_dropdown_button")

    def click_sunday_endtime_time(self):
        self.driver.click("sunday_endtime_time")

    def click_monday_dropdown_time_start(self):
        self.driver.click("monday_dropdown_time_start") 

    def click_monday_dropdown_time(self):
        self.driver.click("monday_dropdown_time") 

    def click_schedule_battery_text(self):
        self.driver.click("schedule_battery_text")

    def get_batterymanager_title_text(self):
        return self.driver.get_attribute("title","Name")
    
    def get_battery_manager_error_text(self):
        return self.driver.get_attribute("battery_manager_error","Name")
    
    def is_run_ok_button_visible(self):
        return self.driver.wait_for_object("run_ok_button", raise_e=False, timeout=10)
    
    def verify_battery_manager_error_text_show(self):
        return self.driver.wait_for_object("battery_manager_error", raise_e=False, timeout=15)
    
    def get_health_calibrate(self):
        return self.driver.get_attribute("health_calibrate", "Name")
    
    def get_optimize_battery_box_toggle_status(self):
        return self.driver.get_attribute("optimize_charg_checkbox","Toggle.ToggleState")

    def get_maximize_battery_box_toggle_status(self):
        return self.driver.get_attribute("maximize_charg_checkbox","Toggle.ToggleState")

    def click_time_sunday_2_am(self):
        self.driver.click("sunday_dropdown_time_2_am")
    
    def click_time_sunday_start(self):
        self.driver.click("sunday_dropdown_time_start")

    def click_time_sunday_end(self):
        self.driver.click("sunday_dropdown_time_end")
    
    def verify_start_time_missing_text_show(self):
        return self.driver.wait_for_object("error_message_starttime_missing", raise_e=False, timeout=5)
    
    def verify_end_time_missing_text_show(self):
        return self.driver.wait_for_object("error_message_endtime_missing", raise_e=False, timeout=5)
    
    def verify_maximize_battery_health_consumer_show(self):
        return self.driver.wait_for_object("maximize_battery_health_consumer", raise_e=False, timeout=20)

    def get_maximize_battery_health_toggle_status_off(self):
        return self.driver.get_attribute("maximize_battery_health_toggle_off","Toggle.ToggleState",timeout=20)
    
    def click_maximize_battery_health_toggle_turn_on(self):
        self.driver.click("maximize_battery_health_toggle_off", timeout=20)

    def click_maximize_battery_health_toggle_turn_off(self):
        self.driver.click("maximize_battery_health_toggle_on", timeout=20)

    def get_maximize_battery_health_toggle_status_on(self):
        return self.driver.get_attribute("maximize_battery_health_toggle_on","Toggle.ToggleState",timeout=20)