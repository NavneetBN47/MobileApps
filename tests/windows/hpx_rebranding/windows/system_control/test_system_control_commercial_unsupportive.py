import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_System_Control_Commercial_Unsupportive(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_optimize_oled_consumption_not_show_C44275141(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)

        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show() is False, "System Control card is displayed"
        time.sleep(2)
        