import pytest
import re
from datetime import datetime
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

def validate_temperature_format_without_prefix(text):
    pattern = r"^\d+\.\d+\sF\s\(\d+\sC\)$"
    match = re.match(pattern, text)
    return match is not None

def validate_serial_number_format(serial):
    pattern = r"^\d{5}\s\d{4}/\d{2}/\d{2}$"
    if not re.match(pattern, serial):
        return "Invalid format"
    
    # Extract and validate the date. Serial Format: 
    try:
        _, date_part = serial.split()
        datetime.strptime(date_part, "%Y/%m/%d")
    except ValueError:
        return "Invalid date"
    
    return True

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Battery_UI(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_maximize_my_battery_health_description_C51602127(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        time.sleep(2)
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
        assert bool(self.fc.fd["battery"].verify_maximize_battery_health_title_ltwo_consumer()) is True, "maximize battery health title is not displayed"
        assert "When this feature is turned on, the battery will only charge up to 80%. This maximizes the battery's lifespan. You will see a heart icon on the battery icon and a message saying" in self.fc.fd["battery"].get_maximize_battery_health_description_ltwo(), "description not displayed"

    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_02_prerequisites_and_uw_software_install_sanity_C51602111(self):
        self.driver.ssh.send_command('Install-WindowsUpdate -AcceptAll -AutoReboot',raise_e=False, timeout=240)
        system_info = self.driver.ssh.send_command('(Get-Service -Name "HP System Info HSA Service").Status', timeout=20)
        service_status_system_info = system_info.get('stdout', '').strip()
        assert "Running" in service_status_system_info, f"Expected service 'HP System Info HSA Service' to be 'Running', but got {system_info}"
        
        network_info = self.driver.ssh.send_command('(Get-Service -Name "HP Network HSA Service").Status', timeout=20)
        service_status_network_info = network_info.get('stdout', '').strip()
        assert "Running" in service_status_network_info, f"Expected service 'HP Network HSA Service' to be 'Running', but got {network_info}"
        
        app_helper = self.driver.ssh.send_command('(Get-Service -Name "HP App Helper HSA Service").Status', timeout=20)
        service_status_app_helper = app_helper.get('stdout', '').strip()
        assert "Running" in service_status_app_helper, f"Expected service 'HP App Helper HSA Service' to be 'Running', but got {app_helper}"


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_03_ui_validation_C51602114(self, language):
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx_rebranding/batterymanagerlocalization.json", language, "batteryManager")
        self.fc.update_properties(language) 

        temperature_value = self.fc.fd["battery"].get_temperature_value_ltwo()
        assert validate_temperature_format_without_prefix(temperature_value), "Temperature format is not correct"
        
        serial_number_value = self.fc.fd["battery"].get_serial_number_value_ltwo()
        assert (validate_serial_number_format(serial_number_value)), "Serial number format is not correct"

        expected_battery_manager_information_title = lang_settings["batteryInformation"]
        actual_battery_manager_information_title = self.fc.fd["battery"].get_battery_information_title_ltwo()
        assert expected_battery_manager_information_title.casefold() == actual_battery_manager_information_title.casefold(), f"Expected {expected_battery_manager_information_title} but got {actual_battery_manager_information_title}"
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_battery_consumer_consistency_for_bhm_toggle_switch_C51602124(self):
        #Turn On/Off toggle button of Maximize battery health
        if self.fc.fd["battery"].get_maximize_battery_health_toggle() == "1":
            self.fc.fd["battery"].click_maximize_battery_health_toggle()
            assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "0", "Toggle button is not turned ON"
        else:
            self.fc.fd["battery"].click_maximize_battery_health_toggle()
            assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "1", "Toggle button is not turned OFF"
        if self.fc.fd["battery"].get_maximize_battery_health_toggle() == "0":
            self.fc.fd["battery"].click_maximize_battery_health_toggle()
            assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "1", "Toggle button is not turned OFF"
        for _ in range(3):
            self.fc.fd["battery"].get_focus_on_app("battery_manager_title_ltwo")
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            #added for loop coz some times back btn not click at one go
            for _ in range(2):
                if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                    break
                else:
                    self.fc.fd["devicesMFE"].click_back_button_rebranding()
                    
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            #added for loop coz some times back btn not click at one go
            for _ in range(2):
                if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                    break
                else:
                    self.fc.fd["devicesMFE"].click_back_button_rebranding()
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "1", "Toggle button is not turned OFF"
        self.fc.fd["battery"].click_maximize_battery_health_toggle()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "0", "Toggle button is not turned ON"
        self.fc.fd["battery"].get_focus_on_app("battery_manager_title_ltwo")
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        #added for loop coz some times back btn not click at one go
        for _ in range(2):
            if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                break
            else:
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "0", "Toggle button is not turned ON"
