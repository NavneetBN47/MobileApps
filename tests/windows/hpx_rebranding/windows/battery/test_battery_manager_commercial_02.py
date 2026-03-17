import datetime
from MobileApps.libs.flows.windows.hpx_rebranding.utility.generate_battery_report import generate_battery_report, retrieve_and_parse_battery_report
import pytest
import time
import re


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

def calculate_new_battery_capacity(current_battery_percentage, max_battery_capacity_percentage):
        return round((current_battery_percentage/max_battery_capacity_percentage) * 100)
     
def extract_percentage(input_string):
    match = re.search(r"\((\d+)%\)", input_string)
    if match:
        return int(match.group(1))
    
    match = re.search(r"(\d+)%", input_string)
    if match:
        return int(match.group(1))

    raise ValueError("No percentage found in the string.")

def extract_whr(input_string):
    match = re.search(r'\d+', input_string)
    if match:
        return int(match.group())
    return None  # Return None if no integer is found

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_ac_power_thresholds_C51250235(self):
        self.fc.maximize_and_verify_device_card()        
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()

        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["battery"].verify_when_plugged_in_threshold_dropdown()

        for value in range(1, 10):
            if value >= 5: 
                #The dropdown shows first 4 values. For the next 5, we have to scroll through the dropdown.
                # With automation, scrolling is flaky and sometimes the dropdown freezes. 
                # The workaround is to navigate away and back.
                self.fc.swipe_window(direction="up", distance=6)
                self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
                self.fc.swipe_window(direction="down", distance=6)
                self.fc.fd["battery"].verify_when_plugged_in_threshold_dropdown()

            self.fc.fd["battery"].navigate_threshold_list_menu(value=value)
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Temporary workaround. Application loses focus
            expected_percent = value * 10
            getattr(self.fc.fd["battery"], f"click_when_plugged_in_threshold_{expected_percent}_percent")()
            actual_value = self.fc.fd["battery"].get_when_plugged_in_threshold_dropdown_value()
            assert actual_value == f"{expected_percent}%", f"Expected value is {expected_percent}% but got {actual_value}"
            time.sleep(1)

    @pytest.mark.function
    def test_02_verify_max_capacity_new_capacity_values_C51250249(self):
        self.fc.swipe_window(direction="up", distance=12)

        report_path = generate_battery_report(self)
        assert report_path, "Battery report path is invalid or not generated."
        battery_info = retrieve_and_parse_battery_report(self, report_path)
        assert battery_info, "Battery information could not be retrieved or is empty."
           
        max_capacity = self.fc.fd["battery"].get_max_capacity_text()
        max_capacity_whr = extract_whr(max_capacity)
        assert battery_info["FULL CHARGE CAPACITY"] == max_capacity_whr, f"Expected value is {battery_info['FULL CHARGE CAPACITY']} but got {max_capacity_whr}"

        new_capacity = self.fc.fd["battery"].get_new_capacity_text()
        new_capacity_whr = extract_whr(new_capacity)
        assert battery_info["DESIGN CAPACITY"] == new_capacity_whr, f"Expected value is {battery_info['DESIGN CAPACITY']} but got {new_capacity_whr}"

        serial_number = self.fc.fd["battery"].get_serial_number_value_ltwo()
        assert battery_info["SERIAL NUMBER"] == serial_number, f"Expected value is {battery_info['SERIAL NUMBER']} but got {serial_number}"

    @pytest.mark.function
    def test_03_fcc_max_capacity_value_when_mbh_selected_C51250252(self):
        self.fc.swipe_to_top()
        assert self.fc.fd["battery"].verify_optimize_battery_performancet_radio_button_ltwo(), "Battery manager optimize battery performance radio button is not displayed"
        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        time.sleep(5) #Give time to update the battery percentagesv
        report_path = generate_battery_report(self)
        report_parsed = retrieve_and_parse_battery_report(self, report_path)
        report_optimized_max_capacity_whr = report_parsed["FULL CHARGE CAPACITY"] 

        assert self.fc.fd["battery"].verify_maximize_battery_health_management_radio_button(), "Battery manager maximize battery health management radio button is not displayed"
        self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
        time.sleep(5) #Give time to update the battery percentages
        report_path = generate_battery_report(self)
        report_parsed = retrieve_and_parse_battery_report(self, report_path)
        report_mbh_max_capacity_max_capacity_whr = report_parsed["FULL CHARGE CAPACITY"] 

        app_mbh_max_capacity = self.fc.fd["battery"].get_max_capacity_text()
        app_mbh_max_capacity_whr = extract_whr(app_mbh_max_capacity)
        assert app_mbh_max_capacity_whr == report_mbh_max_capacity_max_capacity_whr, f"Expected app value is {app_mbh_max_capacity_whr} but report shows {report_mbh_max_capacity_max_capacity_whr}"

        assert report_optimized_max_capacity_whr == report_mbh_max_capacity_max_capacity_whr, f"Optimized value is {report_optimized_max_capacity_whr} MBR value is {report_mbh_max_capacity_max_capacity_whr}"

    # This test should be run on longhornz, rex or ernesto
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_schedule_battery_charging_renavigate_within_page_C52979738(self):
        #Reverted the time — sometimes the notification suite fails, and the time doesn’t revert back, as happened today
        self.driver.ssh.send_command('Start-ScheduledTask -TaskName "RevertSystemTime"', timeout=80)

        self.fc.swipe_window(direction="down", distance=6)
        assert self.fc.fd["battery"].verify_schedule_battery_radio_button_ltwo(), "Schedule battery radio button is not displayed"
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=6)

        current_day = datetime.datetime.today().strftime('%A').lower()

        # Set start time to current day 12:00AM
        charging_time_frame = self.fc.fd["battery"].set_start_time_this_morning(current_day)
        time.sleep(2) # UI needs time to update

        # Set end time to current day 11:59PM. The app looses focus when navigating back to back lists, so we need to retry clicking the end time selection and maximize the app a couple of times as a workaround
        charging_time_frame.append(self.fc.fd["battery"].set_end_time_tonight(current_day)) 
        use_click_end_time_date_method = f"click_end_time_{current_day}_ltwo"
        getattr(self.fc.fd["battery"], use_click_end_time_date_method)()
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        getattr(self.fc.fd["battery"], use_click_end_time_date_method)()
        charging_time_frame.append(self.fc.fd["battery"].set_end_time_tonight(current_day))

        self.fc.swipe_window(direction="up", distance=12)

        if(not self.fc.fd["battery"].verify_battery_state_charging_state()): # UI sometimes gets stuck when navigating back to back lists
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            getattr(self.fc.fd["battery"], charging_time_frame[2])()  # retry clicking
            getattr(self.fc.fd["battery"], charging_time_frame[3])()  # retry clicking

        self.fc.swipe_window(direction="up", distance=12)

        max_wait_time = 120  # total seconds to wait for battery to start discharging
        poll_interval = 5    # check every 5 seconds

        battery_state = self.fc.fd["battery"].get_battery_charging_state()
        print(f"DEBUG: Initial battery state before waiting: {battery_state}")
        if battery_state != "Discharging":
            for elapsed in range(0, max_wait_time, poll_interval):
                time.sleep(poll_interval)
                battery_state = self.fc.fd["battery"].get_battery_charging_state()
                print(f"DEBUG: Battery state after {elapsed + poll_interval} seconds: {battery_state}")
                if battery_state == "Discharging":
                    break
            else:
                raise AssertionError(f"Battery did not start discharging after waiting {max_wait_time} seconds. Last state: {battery_state}")

        assert battery_state == "Discharging", f"Battery is not discharging. Got: {battery_state}"

        self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
        time.sleep(2) #UI Needs to Update
        assert self.fc.fd["battery"].get_battery_charging_state() == "Charging", "Battery is not charging"

        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        time.sleep(5) #UI Needs to Update
        assert self.fc.fd["battery"].get_battery_charging_state() == "Charging", "Battery is not charging"
        time.sleep(2) # UI needs time to update

        self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
        time.sleep(5) #UI Needs to Update
        assert self.fc.fd["battery"].get_battery_charging_state() == "Charging", "Battery is not charging"

        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        time.sleep(5) #UI Needs to Update
        assert self.fc.fd["battery"].get_battery_charging_state() == "Charging", "Battery is not charging"
        time.sleep(2) # UI needs time to update

        self.fc.swipe_window(direction="down", distance=3)
        
        self.fc.fd["battery"].click_schedule_battery_radio_button_ltwo()
        self.fc.swipe_window(direction="down", distance=8)
        self.fc.fd["battery"].click_reset_schedule_button_ltwo() #Reset the schedule so battery does not die
        self.fc.fd["battery"].scroll_to_element("reset_schedule_button_ltwo")
        
        # Set start time to current day 12:00AM
        charging_time_frame_02 = self.fc.fd["battery"].set_start_time_this_morning(current_day)
        time.sleep(2) # UI needs time to update

        # Set end time to current day 11:59PM. The app looses focus when navigating back to back lists, so we need to retry clicking the end time selection and maximize the app a couple of times as a workaround
        use_click_end_time_date_method = f"click_end_time_{current_day}_ltwo"
        getattr(self.fc.fd["battery"], use_click_end_time_date_method)()
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        getattr(self.fc.fd["battery"], use_click_end_time_date_method)()
        charging_time_frame_02.append(self.fc.fd["battery"].set_end_time_tonight(current_day))
        self.fc.swipe_window(direction="up", distance=12)

        if(not self.fc.fd["battery"].verify_battery_state_charging_state()): # UI sometimes gets stuck when navigating back to back lists
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            getattr(self.fc.fd["battery"], charging_time_frame_02[2])()  # retrying clicking
            getattr(self.fc.fd["battery"], charging_time_frame_02[3])()  # retrying clicking

        valid_battery_charging_state = {"Charging", "Fully Charged", "Discharging"}
        battery_state = self.fc.fd["battery"].get_battery_charging_state()

        if battery_state in valid_battery_charging_state:
            if battery_state != "Discharging":
                max_wait_time = 120  # total seconds to wait for battery to start discharging
                poll_interval = 5    # check every 5 seconds
                for elapsed in range(0, max_wait_time, poll_interval):
                    time.sleep(poll_interval)
                    battery_state = self.fc.fd["battery"].get_battery_charging_state()
                    print(f"DEBUG: Battery state after {elapsed + poll_interval} seconds: {battery_state}")
                    if battery_state == "Discharging":
                        break
                else:
                    raise AssertionError(f"Battery did not start discharging after waiting {max_wait_time} seconds. Last state: {battery_state}")
            assert battery_state == "Discharging", f"Battery is not discharging. Got: {battery_state}"
        else:
            raise AssertionError(f"No valid battery state found. Got: {battery_state}")   
        
        self.fc.swipe_window(direction="down", distance=12)
        self.fc.fd["battery"].click_reset_schedule_button_ltwo() #Reset the schedule so battery does not die
        self.fc.swipe_window(direction="up", distance=12)
    
    @pytest.mark.function
    def test_05_battery_commercial_contextual_config_for_battery_manager_C53231326(self):
        self.fc.swipe_to_top()
        self.fc.fd["battery"].click_optimize_battery_performance_radio_button_ltwo()
        self.fc.fd["battery"].get_focus_on_app("battery_manager_title_ltwo_commercial")
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        for _ in range(2):
            if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                break
            else:
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
        contextual_text = self.fc.fd["battery"].get_battery_card_contextual_text()
        assert contextual_text == "Optimize battery performance", f"Expected value is Optimize battery performance but got {contextual_text}"
        
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        self.fc.fd["battery"].click_maximize_battery_health_management_radio_button_ltwo()
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        contextual_text = self.fc.fd["battery"].get_battery_card_contextual_text()
        assert contextual_text == "Maximize battery health", f"Expected value is Maximize battery health but got {contextual_text}"
        self.fc.close_myHP()