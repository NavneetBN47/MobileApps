import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
import logging

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_UI(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_contextual_config_battery_manager_module_C58444988(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"        
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo(), "Battery manager title is not displayed"
        assert self.fc.fd["battery"].verify_battery_information_title_ltwo(), "Battery Information title is not displayed"
        #Battery manager should open with selected default radio button on Optimize battery performance
        if self.fc.fd["battery"].get_maximize_battery_health_toggle() == "0":
            self.fc.fd["battery"].click_maximize_battery_health_toggle()
        assert self.fc.fd["battery"].get_maximize_battery_health_toggle() == "1", "Maximize Battery Health toggle is off"
        self.fc.fd["battery"].get_focus_on_app("battery_manager_title_ltwo")
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        #added for loop coz some times back btn not click at one go
        for _ in range(2):
            if self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone():
                break
            else:
                self.fc.fd["devicesMFE"].click_back_button_rebranding()
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
        assert self.fc.fd["battery"].get_battery_card_contextual_text() == "Maximize battery health", "Battery manager card contextual text is not as expected"

    @pytest.mark.function
    @pytest.mark.ota
    def test_02_battery_consumer_stopping_fusion_services_C51602112(self):
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"        
        self.fc.close_myHP()
        state = self.fc.stop_hpsysinfo_fusion_services()
        logging.info("Service stop state: {}".format(state))
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        assert bool(self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone()) is False, "Battery manager card is displayed"
        self.fc.start_hpsysinfo_fusion_services()
        self.fc.close_myHP()
