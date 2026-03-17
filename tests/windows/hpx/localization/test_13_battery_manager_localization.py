import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["battery_manager_screenshot"])
def screenshot_folder_name(request):
    return request.param

class Test_Suite_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, publish_hpx_localization_screenshot, screenshot_folder_name):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        cls.attachment_path = conftest_misc.get_attachment_folder()

    def test_13_battery_manager_module_C41920192(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/batterymanagerlocalization.json", language, "batteryManager")
        self.fc.update_properties(language) 
        time.sleep(3)
        self.fc.fd["battery"].remove_battery_registry()
        time.sleep(3)
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.launch_myHP() 
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_battery_module()
        time.sleep(3)
        #battery_manager
        time.sleep(8)
        expected_battery_manager_text=lang_settings["batteryManagerTitle"]
        actual_battery_manager_text=self.fc.fd["battery"].get_batterymanager_title_text()
        ma_misc.create_localization_screenshot_folder("battery_manager_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "battery_manager_screenshot/{}_battery_manager_homepage.png".format(language))
        soft_assertion.assert_equal(actual_battery_manager_text, expected_battery_manager_text, "Battery manager text is not matching, expected string text is {expected_battery_manager_text}, but got {actual_battery_manager_text}. ")
        # charging
        if  self.fc.fd["battery"].get_charging_text() == lang_settings["charging"]:
            expected_charging_text = lang_settings["charging"]
            actual_charging_text = self.fc.fd["battery"].get_charging_text()
            soft_assertion.assert_equal(actual_charging_text, expected_charging_text, f"Charging text is not matching. Expected string text is {expected_charging_text}, but got {actual_charging_text}.")
        #Check_for_discharging_text
        elif self.fc.fd["battery"].get_charging_text() == lang_settings["discharging"]:
             expected_charging_text = lang_settings["discharging"]
             actual_charging_text = self.fc.fd["battery"].get_charging_text()
             soft_assertion.assert_equal(actual_charging_text, expected_charging_text, f"Discharging text is not matching. Expected string text is {expected_charging_text}, but got {actual_charging_text}.")
        #Check_for_fully_charged_text
        else:
            expected_charging_text = lang_settings["fullycharge"]
            actual_charging_text = self.fc.fd["battery"].get_charging_text()
            soft_assertion.assert_equal(actual_charging_text, expected_charging_text, f"Fully charged text is not matching. Expected string text is {expected_charging_text}, but got {actual_charging_text}.")
        #battery_information_header
        expected_battery_information_header_text=lang_settings["batteryInformation"]
        actual_battery_information_header_text=self.fc.fd["battery"].get_battery_information_header()
        soft_assertion.assert_equal(actual_battery_information_header_text, expected_battery_information_header_text, f"battery information text is not matching, expected string text is {expected_battery_information_header_text}, but got {actual_battery_information_header_text}. ")
        #new_capacity
        expected_new_capacity_text=lang_settings["newCapacity"]
        actual_new_capacity_text=self.fc.fd["battery"].get_new_capacity_text()
        soft_assertion.assert_equal(actual_new_capacity_text, expected_new_capacity_text, f"new capacity text is not matching, expected string text is {expected_new_capacity_text}, but got {actual_new_capacity_text}. ")
        #maximum_capacity
        expected_maximum_capacity_text=lang_settings["maximumCapacity"]
        actual_maximum_capacity_text=self.fc.fd["battery"].get_max_capacity_text()
        soft_assertion.assert_equal(actual_maximum_capacity_text, expected_maximum_capacity_text, f"maximum capacioty text is not matching, expected string text is {expected_maximum_capacity_text}, but got {actual_maximum_capacity_text}. ")
        #temperature
        expected_temperature_text=lang_settings["temperature"]
        actual_temperature_text=self.fc.fd["battery"].get_temperature_text()
        soft_assertion.assert_equal(actual_temperature_text, expected_temperature_text, f"temperature text is not matching, expected string text is {expected_temperature_text}, but got {actual_temperature_text}. ")
        #serial_number
        expected_serial_number_text=lang_settings["serialNumber"]
        actual_serial_number_text=self.fc.fd["battery"].get_serial_numer_text()
        soft_assertion.assert_equal(actual_serial_number_text, expected_serial_number_text, f"serial number text is not matching, expected string text is {expected_serial_number_text}, but got {actual_serial_number_text}. ")
        #battery_health
        expected_battery_health_text=lang_settings["batteryHealth"]
        actual_battery_health_text=self.fc.fd["battery"].get_battery_health_text()
        soft_assertion.assert_equal(actual_battery_health_text, expected_battery_health_text, f"battery health text is not matching, expected string text is {expected_battery_health_text}, but got {actual_battery_health_text}. ")
        #Normal
        expected_normal_text=lang_settings["normal"]
        actual_normal_text=self.fc.fd["battery"].get_health_normal_text()
        soft_assertion.assert_equal(actual_normal_text, expected_normal_text, f"normal health text is not matching, expected string text is {expected_normal_text}, but got {actual_normal_text}. ")
        #maximum_capacity_tooltip
        self.fc.fd["battery"].click_maximum_capacity_tool_tip()
        time.sleep(3)
        expected_maximum_capacity_tooltip = lang_settings["maximumCapacityTooltip"]
        actual_maximum_capacity_tooltip = self.fc.fd["battery"].get_maximum_capacity_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "battery_manager_screenshot/{}_maximum_capacity_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_maximum_capacity_tooltip, expected_maximum_capacity_tooltip, f"maximum capacity tool tip text is not matching, expected string text is {expected_maximum_capacity_tooltip}, but got {actual_maximum_capacity_tooltip}. ")
        time.sleep(3)
        #charging_option
        expected_charging_option_text=lang_settings["chargingOptions"]
        actual_charging_option_text=self.fc.fd["battery"].get_charge_option_title_text()
        soft_assertion.assert_equal(actual_charging_option_text, expected_charging_option_text, f"charging option text is not matching, expected string text is {expected_charging_option_text}, but got {actual_charging_option_text}. ")
        #charging_desciption
        expected_charging_desciption_text=lang_settings["batteryManagerDescription"]
        actual_charging_desciption_text=self.fc.fd["battery"].get_charge_option_subtitle_text()
        soft_assertion.assert_equal(actual_charging_desciption_text, expected_charging_desciption_text, f"charging description text is not matching, expected string text is {expected_charging_desciption_text}, but got {actual_charging_desciption_text}. ")
        #charging_option_tooltip
        self.fc.fd["battery"].click_charging_option_tooltip()
        time.sleep(3)
        expected_charging_option_tooltip = lang_settings["chargingOptionTooltip"]
        actual_charging_option_tooltip = self.fc.fd["battery"].get_charging_option_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "battery_manager_screenshot/{}_charging_option_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_charging_option_tooltip, expected_charging_option_tooltip, f"charging option tool tip text is not matching, expected string text is {expected_charging_option_tooltip}, but got {actual_charging_option_tooltip}. ")
        time.sleep(3)
        #optimize_battery_performance
        expected_optimize_battery_performance_text=lang_settings["optimizeBatteryPerformance"]
        actual_optimize_battery_performance_text=self.fc.fd["battery"].get_optimize_battery_text()
        soft_assertion.assert_equal(actual_optimize_battery_performance_text, expected_optimize_battery_performance_text, f"optimize battery perf text is not matching, expected string text is {expected_optimize_battery_performance_text}, but got {actual_optimize_battery_performance_text}. ")
        #maximize_battery_health
        expected_maximize_battery_health_text=lang_settings["maximizeBatteryHealth"]
        actual_maximize_battery_health_text=self.fc.fd["battery"].get_max_battery_text()
        soft_assertion.assert_equal(actual_maximize_battery_health_text, expected_maximize_battery_health_text, f"maximize health text is not matching, expected string text is {expected_maximize_battery_health_text}, but got {actual_maximize_battery_health_text}. ")
        #schedule_battery_charging
        expected_schedule_battery_charging_text=lang_settings["scheduleBatteryCharging"]
        actual_schedule_battery_charging_text=self.fc.fd["battery"].get_schdedule_battery_text()
        soft_assertion.assert_equal(actual_schedule_battery_charging_text, expected_schedule_battery_charging_text, f"schedule battery text is not matching, expected string text is {expected_schedule_battery_charging_text}, but got {actual_schedule_battery_charging_text}. ")
        self.fc.fd["battery"].click_schdedule_battery_text_list()
        #optimize_battery_performance_tooltip
        self.fc.fd["battery"].click_optimize_battery_tooltip()
        time.sleep(3)
        expected_optimize_battery_performance_tooltip = lang_settings["letHpManageBatteryTooltip"]
        actual_optimize_battery_performance_tooltip = self.fc.fd["battery"].get_optimize_battery_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "battery_manager_screenshot/{}_optimize_battery_performance_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_optimize_battery_performance_tooltip, expected_optimize_battery_performance_tooltip, f"optmiize battery performance tool tip text is not matching, expected string text is {expected_optimize_battery_performance_tooltip}, but got {actual_optimize_battery_performance_tooltip}. ")
        time.sleep(3)
        # maximize_battery_health_tooltip
        self.fc.fd["battery"].click_maximize_battery_tooltip()
        time.sleep(3)
        expected_maximize_battery_health_tooltip = lang_settings["maximizeBattteryHealthTooltip"]
        actual_maximize_battery_health_tooltip = self.fc.fd["battery"].get_maximize_battery_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "battery_manager_screenshot/{}_maximize_battery_health_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_maximize_battery_health_tooltip, expected_maximize_battery_health_tooltip, f"maximize battery tool tip text is not matching, expected string text is {expected_maximize_battery_health_tooltip}, but got {actual_maximize_battery_health_tooltip}. ")
        time.sleep(3)
        #schedule_battery_charging_tooltip
        self.fc.fd["battery"].click_schedule_battery_tooltip()
        time.sleep(3)
        expected_schedule_battery_charging_tooltip = lang_settings["scheduleChargingDescription"]
        actual_schedule_battery_charging_tooltip = self.fc.fd["battery"].get_schedule_battery_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "battery_manager_screenshot/{}_schedule_battery_charging_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_schedule_battery_charging_tooltip, expected_schedule_battery_charging_tooltip, f"battery charging tool tip text is not matching, expected string text is {expected_schedule_battery_charging_tooltip}, but got {actual_schedule_battery_charging_tooltip}. ")
        time.sleep(3)
        #schedule_battery_charging_description
        self.fc.fd["battery"].click_schedule_charging_box()
        expected_schedule_battery_text=lang_settings["scheduleChargingDescription"]
        actual_schedule_battery_text=self.fc.fd["battery"].get_schedule_battery_description()
        soft_assertion.assert_equal(actual_schedule_battery_text, expected_schedule_battery_text, f"scheduleb battery description text is not matching, expected string text is {expected_schedule_battery_text}, but got {actual_schedule_battery_text}. ")
        #day_of_week
        expected_day_of_week_text=lang_settings["dayOfTheWeek"]
        actual_day_of_week_text=self.fc.fd["battery"].get_days_of_week_text()
        soft_assertion.assert_equal(actual_day_of_week_text, expected_day_of_week_text, f"day of week text is not matching, expected string text is {expected_day_of_week_text}, but got {actual_day_of_week_text}. ")
        #start_time
        expected_start_time_text=lang_settings["startTime"]
        actual_start_time_text=self.fc.fd["battery"].get_start_time_text()
        soft_assertion.assert_equal(actual_start_time_text, expected_start_time_text, f"start time text is not matching, expected string text is {expected_start_time_text}, but got {actual_start_time_text}. ")
        #end_time
        expected_end_time_text=lang_settings["endTime"]
        actual_end_time_text=self.fc.fd["battery"].get_end_time_text()
        soft_assertion.assert_equal(actual_end_time_text, expected_end_time_text, f"end timne text is not matching, expected string text is {expected_end_time_text}, but got {actual_end_time_text}. ")
        #total
        expected_total_text=lang_settings["totalHours"]
        actual_total_text=self.fc.fd["battery"].get_total_text()
        soft_assertion.assert_equal(actual_total_text, expected_total_text, f"total hours text is not matching, expected string text is {expected_total_text}, but got {actual_total_text}. ")
        #sunday
        expected_sunday_text=lang_settings["sunday"]
        actual_sunday_text=self.fc.fd["battery"].get_sunday_text()
        soft_assertion.assert_equal(actual_sunday_text, expected_sunday_text, f"sunday text is not matching, expected string text is {expected_sunday_text}, but got {actual_sunday_text}. ")
        #monday
        expected_monday_text=lang_settings["monday"]
        actual_monday_text=self.fc.fd["battery"].get_monday_text()
        soft_assertion.assert_equal(actual_monday_text, expected_monday_text, f"mondays text is not matching, expected string text is {expected_monday_text}, but got {actual_monday_text}. ")
        #tuesday
        expected_tuesday_text=lang_settings["tuesday"]
        actual_tuesday_text=self.fc.fd["battery"].get_tuesday_text()
        soft_assertion.assert_equal(actual_tuesday_text, expected_tuesday_text, f"tuesdays text is not matching, expected string text is {expected_tuesday_text}, but got {actual_tuesday_text}. ")
        #wednesday
        expected_wednesday_text=lang_settings["wednesday"]
        actual_wednesday_text=self.fc.fd["battery"].get_wednesday_text()
        soft_assertion.assert_equal(actual_wednesday_text, expected_wednesday_text, f"wednesdays text is not matching, expected string text is {expected_wednesday_text}, but got {actual_wednesday_text}. ")
        #thursay
        expected_thursay_text=lang_settings["thursday"]
        actual_thursay_text=self.fc.fd["battery"].get_thursday_text()
        soft_assertion.assert_equal(actual_thursay_text, expected_thursay_text, f"thursay text is not matching, expected string text is {expected_thursay_text}, but got {actual_thursay_text}. ")
        #friday
        expected_friday_text=lang_settings["friday"]
        actual_friday_text=self.fc.fd["battery"].get_friday_text()
        soft_assertion.assert_equal(actual_friday_text, expected_friday_text, f"friday text is not matching, expected string text is {expected_friday_text}, but got {actual_friday_text}. ")
        #saturday
        expected_saturday_text=lang_settings["saturday"]
        actual_saturday_text=self.fc.fd["battery"].get_saturday_text()
        soft_assertion.assert_equal(actual_saturday_text, expected_saturday_text, f"saturdays text is not matching, expected string text is {expected_saturday_text}, but got {actual_saturday_text}. ")
        #hour
        expected_hour_text=lang_settings["hour"]
        actual_hour_text=self.fc.fd["battery"].get_hours_text()
        soft_assertion.assert_equal(actual_hour_text, expected_hour_text, f"hour text is not matching, expected string text is {expected_hour_text}, but got {actual_hour_text}. ")
        #clear_schedule
        expected_clear_schedule_health_text=lang_settings["clearSchedule"]
        actual_clear_schedule_health_text=self.fc.fd["battery"].get_clear_schedule()
        soft_assertion.assert_equal(actual_clear_schedule_health_text, expected_clear_schedule_health_text, f"clear schedule text is not matching, expected string text is {expected_clear_schedule_health_text}, but got {actual_clear_schedule_health_text}. ")
        #battery_percent
        expected_battery_percent_text=lang_settings["setBatteryPercentage"]
        actual_battery_percenth_text=self.fc.fd["battery"].get_percentage_text()
        soft_assertion.assert_equal(actual_battery_percenth_text, expected_battery_percent_text, f"battery percent text is not matching, expected string text is {expected_battery_percent_text}, but got {actual_battery_percenth_text}. ")
        #start_time_missing
        self.fc.fd["battery"].click_sunday_end_dropdown()
        self.fc.fd["battery"].click_sunday_endtime_time()
        expected_start_time_missing_text=lang_settings["startTimeMissing"]
        actual_start_time_missing_text=self.fc.fd["battery"].get_error_message_starttime_missing()
        soft_assertion.assert_equal(actual_start_time_missing_text, expected_start_time_missing_text, f"start time missing text is not matching, expected string text is {expected_start_time_missing_text}, but got {actual_start_time_missing_text}. ")
        #end_time_missing
        self.fc.fd["battery"].click_monday_starttime_dropdown_button()
        self.fc.fd["battery"].click_monday_dropdown_time_start()
        expected_end_time_missing_text=lang_settings["endTimeMissing"]
        actual_end_time_missing_text=self.fc.fd["battery"].get_error_message_endtime_missing()
        soft_assertion.assert_equal(expected_end_time_missing_text, actual_end_time_missing_text, f"end time missing text is not matching, expected string text is {expected_end_time_missing_text}, but got {actual_end_time_missing_text}. ") 
        #invalid_endtime
        self.fc.fd["battery"].click_monday_dropdown_button()
        self.fc.fd["battery"].click_monday_dropdown_time()
        expected_end_time_missingl_text=lang_settings["endTimeError"]
        actual_end_time_missing_text=self.fc.fd["battery"].get_invalid_end_label()
        soft_assertion.assert_equal(actual_end_time_missing_text, expected_end_time_missingl_text, f"invalid endtime text is not matching, expected string text is {expected_end_time_missingl_text}, but got {actual_end_time_missing_text}. ") 
        #invalid_starttime
        self.fc.fd["battery"].click_sunday_dropdown()
        self.fc.fd["battery"].click_time_sunday()
        expected_invalid_starttime_text=lang_settings["startTimeError"]
        actual_invalid_starttime_text=self.fc.fd["battery"].get_invalid_start_label()
        soft_assertion.assert_equal(actual_invalid_starttime_text, expected_invalid_starttime_text, f"invalid starttime health text is not matching, expected string text is {expected_invalid_starttime_text}, but got {actual_invalid_starttime_text}. ")
        #manage_your_power
        self.fc.close_myHP()
        self.fc.launch_myHP() 
        expected_manage_you_power_text=lang_settings["batteryManagerCard"]
        self.fc.fd["navigation_panel"].verify_battery_manager_text_settings()
        actual_manage_you_power_text=self.fc.fd["navigation_panel"].get_battery_manager_text_settings()
        soft_assertion.assert_equal(actual_manage_you_power_text, expected_manage_you_power_text, f"manager card is not matching, expected string text is {expected_manage_you_power_text}, but got {actual_manage_you_power_text}. ")
        #disable_battery
        self.fc.fd["navigation_panel"].click_battery_manager_text()
        time.sleep(10)
        if  self.fc.fd["battery"].verify_battery_manager_error_text_show() == lang_settings["adminITWarningMessage"]:
            expected_disable_battery_text=lang_settings["adminITWarningMessage"]
            actual_disable_battery_text=self.fc.fd["battery"].get_battery_manager_error_text()
            soft_assertion.assert_equal(actual_disable_battery_text, expected_disable_battery_text, f"admin IT warning text is not matching, expected string text is {expected_disable_battery_text}, but got {actual_disable_battery_text}. ")
        else:
            self.fc.fd["battery"].add_battery_registry()   
            time.sleep(3)
            self.fc.close_myHP()
            self.fc.launch_myHP() 
            self.fc.fd["navigation_panel"].verify_navigationicon_show()
            time.sleep(3)
            self.fc.fd["navigation_panel"].navigate_to_pc_device()
            self.fc.fd["devices"].click_for_battery_manager_card()
            time.sleep(5)
            expected_disable_battery_text=lang_settings["adminITWarningMessage"]
            actual_disable_battery_text=self.fc.fd["battery"].get_battery_manager_error_text()
            soft_assertion.assert_equal(actual_disable_battery_text, expected_disable_battery_text, f"admin IT warning text is not matching, expected string text is {expected_disable_battery_text}, but got {actual_disable_battery_text}. ")

        time.sleep(3)
        self.fc.fd["battery"].remove_battery_registry()
        time.sleep(5)
        self.fc.close_myHP()
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()
