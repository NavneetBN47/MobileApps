import re
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

def validate_text_grammer(self, language, expected_text, actual_text):
    lang_settings = self.fc.processing_localization_language("resources/test_data/hpx_rebranding/batterymanagerlocalization.json", language, "batteryManager")
    self.fc.update_properties(language)
    
    expected_text_value = lang_settings[expected_text]
    try:
        assert expected_text_value.casefold() == actual_text.casefold(), f"Expected {expected_text_value} but got {actual_text}"
        return True
    except AssertionError as e:
            print(f"Assertion failed: {e}")
            return False

def validate_temperature_format_without_prefix(text):
    pattern = r"^\d+\.\d+\sF\s\(\d+\sC\)$"
    match = re.match(pattern, text)
    return match is not None

def validate_serial_number_format(serial):
    # Validates the format of a serial number to be like XXXXX XXXX/XX/XX for eg. '12345 6789/12/31'.
    return bool(re.match(r"^\d{5}\s\d{4}/\d{2}/\d{2}$", serial.strip()))

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Battery_UI(object):

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_pc_device_battery_manager_module_C51250219(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_text_lone(), "Battery manager card text is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_icon_lone(), "Battery manager card icon is not displayed"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_navigate_to_battery_manager_module_C51250220(self):
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
    
    @pytest.mark.ota
    def test_03_schedule_battery_charging_default_threshold_value_C51250227(self):
        assert self.fc.fd["battery"].verify_charging_option_title_ltwo(), "Charging Option title is not displayed"
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=12)
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        self.fc.fd["battery"].scroll_to_element("threshold_dropdown_ltwo")
        assert self.fc.fd["battery"].get_threshold_dropdown_ltwo() == "20%", "value is not 20%"
        self.fc.swipe_window(direction="up", distance=10)

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_schedule_battery_charging_reset_schedule_button_C51250228(self):
        self.fc.swipe_window(direction="up", distance=10)
        assert self.fc.fd["battery"].verify_charging_option_title_ltwo(), "Charging Option title is not displayed"
        self.fc.swipe_window(direction="down", distance=3)
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=8)
        assert "Start time" in self.fc.fd["battery"].get_start_time_sunday_ltwo(), "Default no value is not there"
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_sunday_twelve_am_option_ltwo()
        assert "12:00 AM" in self.fc.fd["battery"].get_start_time_sunday_ltwo(), "12:00 AM value is not selected"
        assert self.fc.fd["battery"].verify_reset_schedule_button_ltwo(), "Reset button is not visible"
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()
        self.fc.fd["battery"].scroll_to_element("start_time_sunday_ltwo")
        assert "Start time" in self.fc.fd["battery"].get_start_time_sunday_ltwo(), "Default no value is not there"

    @pytest.mark.ota
    def test_05_schedule_battery_charging_renavigate_C51250230(self):
        self.fc.swipe_window(direction="up", distance=5)
        assert self.fc.fd["battery"].verify_charging_option_title_ltwo(), "Charging Option title is not displayed"
        assert bool(self.fc.fd["battery"].is_selected_optimize_battery_performance_radio_button_ltwo())is True, "Optimize battery performance is not selected"
        self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        assert bool(self.fc.fd["battery"].is_selected_schedule_battery_radio_button_ltwo())is True, "Schedule battery charging performance is not selected"
        self.fc.swipe_window(direction="up", distance=8)
        self.fc.fd["battery"].get_focus_on_app("battery_manager_title_ltwo_commercial")
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        for _ in range(2):
            if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                break
            else:
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        self.fc.swipe_window(direction="down", distance=6)
        assert bool(self.fc.fd["battery"].is_selected_optimize_battery_performance_radio_button_ltwo())is True, "Optimize battery performance is not selected"

    @pytest.mark.ota
    def test_06_charging_options_C51250224(self):
        self.fc.swipe_window(direction="up", distance=20) 
        optimize_description = self.fc.fd["battery"].get_optimize_battery_performance_description_ltwo()
        expected_optimize_description = "This mode automatically manages your battery's health by dynamically adjusting its maximum charge capacity. This helps to prolong battery lifespan without significantly impacting runtime."
        assert optimize_description == expected_optimize_description,"description doesnot match"
        maxmize_description = self.fc.fd["battery"].get_maximize_battery_health_description_ltwo()
        expected_maxmize_description = "This mode prioritizes long-term battery health by limiting its available full charge capacity. This is ideal for users who primarily keep their device plugged in."
        assert maxmize_description == expected_maxmize_description,"description doesnot match"
        self.fc.swipe_window(direction="down", distance=6)
        schedule_descripton = self.fc.fd["battery"].get_schedule_battery_charging_description_ltwo()
        expected_schedule_descripton = "Set specific times for your notebook to use its internal battery even when plugged in. Useful for regions that have consistent rolling blackouts."
        assert schedule_descripton  == expected_schedule_descripton, "description doesnot match"

    @pytest.mark.require_sanity_check(["sanity"])
    def test_07_sanity_ui_screen_charge_options_C43080275(self, language):
        self.fc.swipe_window(direction="up", distance=6)
        assert bool(self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial()) is True, "Battery manager title is not displayed"
        assert self.fc.fd["battery"].verify_battery_information_title_ltwo(), "Battery Information title is not displayed"
        assert bool(self.fc.fd["battery"].verify_battery_state()) is True, "Battery state/percentage is not displayed"
        current_battery_charging_state = self.fc.fd["battery"].get_battery_charging_state()
        valid_battery_charging_state = {"charging", "fullycharge", "discharging"}
        for charging_state in valid_battery_charging_state:
            if validate_text_grammer(self, language, charging_state, current_battery_charging_state):
                break
        else:
            raise AssertionError(f"No valid battery state found in {current_battery_charging_state}")
        assert bool(self.fc.fd["battery"].verify_battery_icon_in_front_of_state()) is True, "Battery icon is not displayed"
        assert bool(self.fc.fd["battery"].verify_battery_new_capacity_value()) is True, "New capacity value is not displayed"
        assert bool(self.fc.fd["battery"].verify_max_capacity()) is True, "Maximum capacity value is not displayed"
        current_battery_health = self.fc.fd["battery"].get_battery_health_text()
        valid_battery_health_status = {"weak", "normal", "veryWeek", "requiredReplacement", "noBattery", "calibrate", "unknown"}

        for health_status in valid_battery_health_status:
            if validate_text_grammer(self, language, health_status, current_battery_health):
                break
        else:
            raise AssertionError(f"No valid battery state found in {current_battery_charging_state}")
        temperature_value = self.fc.fd["battery"].get_temperature_value_ltwo()
        assert validate_temperature_format_without_prefix(temperature_value), "Temperature format is not correct"
        serial_number_value = self.fc.fd["battery"].get_serial_number_value_ltwo()
        assert validate_serial_number_format(serial_number_value), f"Serial number format is not correct. Serial Number: {serial_number_value}"
        assert bool(self.fc.fd["battery"].verify_charging_option_title_ltwo()) is True, "Charging Option title is not displayed"
        assert self.fc.fd["battery"].get_optimize_battery_performance_title_ltwo() == "Optimize battery performance", "Optimize battery performance title is not displayed"
        assert bool(self.fc.fd["battery"].verify_optimize_battery_performancet_radio_button_ltwo()) is True, "Optimize battery performance radio button is not displayed"
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["battery"].get_maximize_battery_health_management_title_ltwo() == "Maximize battery health management", "Maximize battery health management title is not displayed"
        assert bool(self.fc.fd["battery"].verify_maximize_battery_health_management_radio_button()) is True, "Maximize battery health management radio button is not displayed"
        assert self.fc.fd["battery"].get_schedule_battery_charging_title_ltwo() == "Schedule battery charging"," Schedule battery charging title is not displayed"
        assert bool(self.fc.fd["battery"].verify_schedule_battery_radio_button_ltwo()) is True, "Schedule battery charging radio button is not displayed"
       # Note: Default Optimize battery performance radio button should be selected
        assert bool(self.fc.fd["battery"].is_selected_optimize_battery_performance_radio_button_ltwo())is True, "Optimize battery performance is not selected"

    @pytest.mark.require_sanity_check(["sanity"])
    def test_08_schedule_battery_charging_C51250225(self):
        self.fc.fd["battery"].scroll_to_element("schedule_battery_radio_button_ltwo")
        self.fc.fd["battery"].verify_schedule_battery_radio_button_ltwo()
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)    
        self.fc.fd["battery"].click_start_time_sunday_ltwo()
        self.fc.fd["battery"].click_sunday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_sunday_ltwo()
        self.fc.fd["battery"].click_one_am_option_end_time_ltwo()
        self.fc.fd["battery"].click_start_time_monday_ltwo()
        self.fc.fd["battery"].click_monday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_monday_ltwo()
        self.fc.fd["battery"].click_monday_one_am_option_ltwo()
        self.fc.fd["battery"].click_start_time_tuesday_ltwo()
        self.fc.fd["battery"].click_tuesday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_tuesday_ltwo()
        self.fc.fd["battery"].click_tuesday_one_am_option_ltwo()
        self.fc.swipe_window(direction="down", distance=5) 
        self.fc.fd["battery"].click_start_time_wednesday_ltwo()
        self.fc.fd["battery"].click_wednesday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_wednesday_ltwo()
        self.fc.fd["battery"].click_wednesday_one_am_option_ltwo()
        self.fc.fd["battery"].click_start_time_thursday_ltwo()
        self.fc.fd["battery"].click_thursday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_thursday_ltwo()
        self.fc.fd["battery"].click_thursday_one_am_option_ltwo()
        self.fc.fd["battery"].click_start_time_friday_ltwo()
        self.fc.fd["battery"].click_friday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_friday_ltwo()
        self.fc.fd["battery"].click_friday_one_am_option_ltwo()
        self.fc.fd["battery"].click_start_time_saturday_ltwo()
        self.fc.fd["battery"].click_saturday_twelve_am_option_ltwo()
        self.fc.fd["battery"].click_end_time_saturday_ltwo()
        self.fc.fd["battery"].click_saturday_one_am_option_ltwo()               
        self.fc.swipe_window(direction="down", distance=10)
        self.fc.fd["battery"].click_reset_schedule_button_ltwo()

    @pytest.mark.ota
    def test_09_charging_options_tooltip_C51250223(self):
        self.fc.swipe_window(direction="up", distance=20)
        self.fc.fd["battery"].click_maximum_capacity_tooltip()
        assert bool(self.fc.fd["battery"].verify_maximum_capacity_tooltip()) is True,"Maximum capacity tooltip is not displayed"
        self.fc.fd["battery"].click_charging_options_tooltip()
        assert bool(self.fc.fd["battery"].verify_charging_options_tooltip()) is True,"Charging options tooltip is not displayed"       

    @pytest.mark.function
    def test_10_deeplink_support_for_battery_manager_C51250254(self):
        #app need to close from above tc
        self.fc.close_myHP()
        self.fc.fd["battery"].run_deeplink_battery_manager()
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["battery"].verify_battery_information_title_ltwo(), "Battery Information title is not displayed"
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["battery"].verify_charging_option_title_ltwo(), "Charging Option title is not displayed"
        self.fc.close_myHP()