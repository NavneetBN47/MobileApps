import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Smart_Displays_Commercial(object):
        
    @pytest.mark.function
    def test_01_smart_displays_ui_on_commercial_C61075923(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_commercial_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_commercial_lone_page()

        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_feature_notice_commercial_show(), "Feature notice on commercial version is not displayed"
        assert self.fc.fd["smart_displays"].verify_look_to_move_toggle_show(), "Look to Move toggle is not displayed"
        assert self.fc.fd["smart_displays"].verify_look_to_control_toggle_show(), "Look to Control toggle is not displayed"
        assert self.fc.fd["smart_displays"].verfy_restore_default_button_commercial_show(), "Restore Default button on commercial version is not displayed"
    

    @pytest.mark.function
    def test_02_launch_smart_display_through_pc_device_page_C61075926(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_commercial_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_commercial_lone_page()

        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_look_to_move_toggle_show(), "Look to Move toggle is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_03_default_state_smart_display_C61075927(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_commercial_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_commercial_lone_page()

        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_look_to_move_button_status() == "0", "Look to Move toggle is not in default off state"
        assert self.fc.fd["smart_displays"].verify_look_to_control_button_status() == "0", "Look to Control toggle is not in default off state"


    @pytest.mark.ota
    @pytest.mark.function
    def test_04_restore_default_button_C61075928(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_commercial_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_commercial_lone_page()

        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_look_to_move_button_status() == "0", "Look to Move toggle is not in default off state"
        assert self.fc.fd["smart_displays"].verify_look_to_control_button_status() == "0", "Look to Control toggle is not in default off state"

        time.sleep(2)
        self.fc.fd["smart_displays"].turn_on_look_to_move_toggle()
        time.sleep(2)
        self.fc.fd["smart_displays"].turn_on_look_to_control_toggle()
        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_look_to_move_button_status() == "1", "Look to Move toggle is not turned on"
        assert self.fc.fd["smart_displays"].verify_look_to_control_button_status() == "1", "Look to Control toggle is not turned on"
        time.sleep(2)
        self.fc.fd["smart_displays"].click_restore_default_button_commercial()

        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_look_to_move_button_status() == "0", "Look to Move toggle is not restored to off state"
        assert self.fc.fd["smart_displays"].verify_look_to_control_button_status() == "0", "Look to Control toggle is not restored to off state"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_error_handling_for_missing_external_display_C61075971(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_commercial_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_commercial_lone_page()

        time.sleep(2)

        assert self.fc.fd["smart_displays"].get_error_handling_message() == "To activate the features, connect an external display and open the camera shutter.", "Error handling message is not correct"

