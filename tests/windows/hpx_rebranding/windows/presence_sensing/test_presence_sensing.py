import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Presence_Sensing_UI(object):
            
    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_verify_presence_sensing_show_C43876462(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_sensing_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "Presence Sensing card is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_presence_sensing_microsoft_ui_C43876463(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_sensing_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_presence_sensing_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["presence_sensing"].verify_turn_off_my_screen_btn_show(), "Turn off my screen button is not displayed"
        assert self.fc.fd["presence_sensing"].verify_wake_my_device_btn_show(), "Wake my device button is not displayed"
        assert self.fc.fd["presence_sensing"].verify_dim_my_screen_btn_show(), "Dim my screen button is not displayed"
        self.fc.close_windows_settings_panel()
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_switch_back_and_relaunch_C43876465(self):
        time.sleep(5)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_sensing_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "Presence Sensing card is not displayed"
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=4)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_return_button_on_top_left_corner()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_sensing_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "Presence Sensing card is not displayed"
