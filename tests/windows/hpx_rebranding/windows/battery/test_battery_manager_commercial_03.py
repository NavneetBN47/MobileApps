import pytest
import time
import re
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

def extract_whr(input_string):
    match = re.search(r'\d+', input_string)
    if match:
        return int(match.group())
    return None  # Return None if no integer is found

def extract_percentage(input_string):
    # Extracts the first integer percentage value from a string in the format '(25%)' or '25%'.
    match = re.search(r"\(?(\d+)%\)?", input_string)
    if match:
        return int(match.group(1))
    raise ValueError("No percentage found in the string.")

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):

    #this suite should run on any commercial  platform where max battery capacity is greater than 80% like machu.
    @pytest.mark.function
    @pytest.mark.commercial
    def test_01_maximize_battery_health_radio_button_C51250247(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()

        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        #FCC/maximum capacity greater or equal to 80%.

        max_capacity = self.fc.fd["battery"].get_max_capacity_text()
        logging.info(f"max_capacity: {max_capacity}")
        max_battery_capacity_percentage = re.search("(([0-9]{1,3})%)",str(max_capacity)).group(2)
        logging.info(f"max_battery_capacity_percentage: {max_battery_capacity_percentage}")
        max_battery_capacity = extract_whr(max_capacity)
        logging.info(f"max_battery_capacity_percentage: {max_battery_capacity}")

        if(int(max_battery_capacity_percentage) >= 80):
            new_capacity = self.fc.fd["battery"].get_new_capacity_text()
            new_capacity_whr = extract_whr(new_capacity)
            logging.info(f"new_capacity_whr: {new_capacity_whr}")
            BHM_max_capacity_BCC=round(new_capacity_whr*0.8)

            max_capacity = self.fc.fd["battery"].get_max_capacity_text()
            max_battery_capacity_percentage = extract_whr(max_capacity)
            logging.info(f"max_battery_capacity_percentage: {max_battery_capacity_percentage}")
            
            battery_state =  self.fc.fd["battery"].get_current_battery_percentage_text()
            current_battery_percentage = extract_percentage(battery_state)
            logging.info(f"current_battery_percentage: {current_battery_percentage}") 

            current_battery_charge_FCC=round(max_battery_capacity_percentage*round(current_battery_percentage/100))
            logging.info(f"current_battery_charge_FCC: {current_battery_charge_FCC}")

            current_battery_percentage_optimize=round(round(current_battery_charge_FCC/BHM_max_capacity_BCC)*100)
            logging.info(f"current_battery_percentage: {current_battery_percentage}")
            self.fc.swipe_window(direction="down", distance=2)
            self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
            time.sleep(4) #Needs time to update the battery percentage
            battery_state =  self.fc.fd["battery"].get_current_battery_percentage_text()
            current_battery_percentage_maximize = extract_percentage(battery_state)
            logging.info(f"current_battery_percentage when maximize option: {current_battery_percentage}") 
            assert current_battery_percentage_maximize == current_battery_percentage_optimize, f"Expected value is {current_battery_percentage_optimize} but got {current_battery_percentage_maximize}"

    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_02_optimize_battery_performance_radio_button_battery_manager_module_C58385531(self):
        self.fc.swipe_window(direction="up", distance=5)
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        assert self.fc.fd["battery"].verify_battery_information_title_ltwo(), "Battery Information title is not displayed"
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["battery"].verify_charging_option_title_ltwo(), "Charging Option title is not displayed"
        assert bool(self.fc.fd["battery"].is_selected_optimize_battery_performance_radio_button_ltwo())is True, "Optimize battery performance is not selected"

    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_03_minimize_battery_health_radio_button_from_ui_C58443262(self):
        self.fc.swipe_window(direction="down", distance=1)
        assert self.fc.fd["battery"].verify_minimize_battery_title_ltwo(), "Minimize battery health management title is not displayed"
        assert self.fc.fd["battery"].verify_minimize_battery_description_ltwo(), "Minimize battery health management description is not displayed"
        assert self.fc.fd["battery"].verify_minimize_battery_radio_button_ltwo(), "Minimize battery health management radio button is not displayed"
        self.fc.fd["battery"].click_miniimize_battery_health_radio_button_ltwo()
        assert bool(self.fc.fd["battery"].is_selected_miniimize_battery_health_radio_button_ltwo())is True, "Minimize battery health management radio button is not selected"