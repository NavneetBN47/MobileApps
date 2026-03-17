from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_PC_Device_Functional_Gestures(object):


    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_gesture_card_on_pc_device_C42902492(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gestures card is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=7)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_gesture_card()
        assert self.fc.fd["gestures"].verify_gesture_card_title_show(), "Gestures title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_gesture_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_gesture_card_lone_page_show(), "Gestures card is not displayed"

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_touchpad_card_on_pc_device_C53003657(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page(), "Touchpad card is not displayed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        assert self.fc.fd["touchpad"].verify_touchpad_title_show(), "Touchpad title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page(), "Touchpad card is not displayed"
        self.fc.swipe_window(direction="up", distance=5)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
    