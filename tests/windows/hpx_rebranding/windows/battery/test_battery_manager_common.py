import pytest
import time
import re

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

def validate_temperature_format_without_prefix(text):
    # Validates the format of a temperature string to be in the format 'XX.X F (XX C)'.
    return bool(re.match(r"^\d+\.\d+\sF\s\(\d+\sC\)$", text))

def validate_serial_number_format(serial):
    # Validates the format of a serial number to be like XXXXX XXXX/XX/XX for eg. '12345 6789/12/31'.
    return bool(re.match(r"^\d{5}\s\d{4}/\d{2}/\d{2}$", serial.strip()))

def validate_text_grammar(self, language, expected_text, actual_text):
    lang_settings = self.fc.processing_localization_language(
        "resources/test_data/hpx_rebranding/batterymanagerlocalization.json", language, "batteryManager")
    self.fc.update_properties(language)

    expected_text_value = lang_settings[expected_text]
    try:
        assert expected_text_value.casefold() == actual_text.casefold(), f"Expected {expected_text_value} but got {actual_text}"
        return True
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        return False

def extract_percentage(input_string):
    # Extracts the first percentage value from a string in the format '(25%)' or '25%'.
    # Returns the percentage as an integer.Raises ValueError if no percentage is found.
    match = re.search(r"\(?(\d+)%\)?", input_string)
    if match:
        return int(match.group(1))
    raise ValueError("No percentage found in the string.")

def extract_whr_value(text):
    # Extracts the WHR (Watt-Hour) value from a given text like '50 WHR' or '50 whr'.
    # Returns the value as an integer or None if no match is found.
    match = re.search(r"(\d+)\s*[Ww][Hh][Rr]", text)
    return int(match.group(1)) if match else None

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):

    def verify_battery_manager_title(self):
        if self.platform.lower() in ("longhornz", "machu13x", "ernesto", "masadaNX", "rex", "masadansku5"):
            assert bool(self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial()) is True, "Commercial battery manager title is not displayed"
        if self.platform.lower() == "enstrom":
            assert bool(self.fc.fd["battery"].verify_battery_manager_title_ltwo()) is True, "Battery manager title is not displayed"

    def click_battery_card_verify_title_and_click_back(self):
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_lone(), "Battery manager title is not displayed"
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd[ "devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed after clicking back button"

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_01_no_crashes_and_glitches_C44226604(self):
        self.fc.maximize_and_verify_device_card()
        for _ in range(3):
            self.fc.swipe_window(direction="down", distance=2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            self.verify_battery_manager_title()
            time.sleep(2)
            self.fc.fd["battery"].get_focus_on_app("battery_manager_title_ltwo_commercial")
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            for _ in range(2):
                if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                    break
                else:
                    self.fc.fd["devicesMFE"].click_back_button_rebranding()
            
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed after multiple interactions"

    @pytest.mark.function
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_mps_consistency_C44226605(self):
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone() is True:
            self.click_battery_card_verify_title_and_click_back()
            # commercial and consumer
            if self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up() is True:
                self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            else:
                self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up()
                self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.click_battery_card_verify_title_and_click_back()
            self.fc.restart_myHP()
            self.fc.maximize_and_verify_device_card()
            self.click_battery_card_verify_title_and_click_back()

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_stopping_fusion_services_C51250241(self):
        # app needs to be closed to see application of services stop
        self.fc.close_myHP()
        self.fc.stop_hp_networkcap_exe()
        self.fc.stop_hp_apphelpercap_exe()
        self.fc.stop_hpsysinfo_fusion_services()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone()) is False, "Battery manager card is not displayed"
        # reverting back the services to start and app close for new launch battery manager to show.
        self.fc.start_hpsysinfo_fusion_services()
        self.fc.start_hp_apphelpercap_exe()
        self.fc.start_hp_networkcap_exe()
        self.fc.close_myHP()

    @pytest.mark.function
    @pytest.mark.commercial
    def test_04_battery_information_values_C51250222(self, language):
        time.sleep(2)
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        # for commercial run only
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        #This is a workaround as sometimes the battery manager title is not detected properly, and it lands to L0 instead of battery manager L2
        if not self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial():
            self.fc.close_myHP()
            time.sleep(5)
            self.fc.launch_myHP()
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=2)
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        
        self.fc.swipe_window(direction="up", distance=9)
        current_battery_percentage = self.fc.fd["battery"].get_current_battery_percentage_text()
        current_battery_percentage_value = extract_percentage(current_battery_percentage)
        assert 0 <= current_battery_percentage_value <= 100, "Battery percentage is not in the range of 0-100"

        current_battery_charging_state = self.fc.fd["battery"].get_battery_charging_state()
        valid_battery_charging_state = {"charging", "fullycharge", "discharging"}
        for charging_state in valid_battery_charging_state:
            if validate_text_grammar(self, language, charging_state, current_battery_charging_state):
                break
        else:
            raise AssertionError(f"No valid battery state found in {current_battery_charging_state}")

        current_battery_health = self.fc.fd["battery"].get_battery_health_text()
        valid_battery_health_status = {"weak", "normal", "veryWeek", "requiredReplacement", "noBattery", "calibrate", "unknown"}

        for health_status in valid_battery_health_status:
            if validate_text_grammar(self, language, health_status, current_battery_health):
                break
        else:
            raise AssertionError(f"No valid battery state found in {current_battery_charging_state}")

        new_capacity = self.fc.fd["battery"].get_battery_new_capacity_text()
        new_capacity_capacity_whr_value = extract_whr_value(new_capacity)
        
        battery_max_capacity = self.fc.fd["battery"].get_max_capacity_text()
        max_battery_percentage_value = extract_percentage(battery_max_capacity)
        max_battery_capacity_whr_value = extract_whr_value(battery_max_capacity)
        assert max_battery_percentage_value <= 100, "Max battery percentage is above 100"
        assert max_battery_capacity_whr_value <= new_capacity_capacity_whr_value, "Max battery capacity is above new capacity"

        temperature_value = self.fc.fd["battery"].get_temperature_value_ltwo()
        assert validate_temperature_format_without_prefix(temperature_value), "Temperature format is not correct"
        
        serial_number_value = self.fc.fd["battery"].get_serial_number_value_ltwo()
        assert validate_serial_number_format(serial_number_value), f"Serial number format is not correct. Serial Number: {serial_number_value}"
        self.fc.close_myHP()