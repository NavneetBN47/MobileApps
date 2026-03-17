import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_System_Control_Optimize_OLED_Unsupportive(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_optimize_oled_consumption_not_show_C51244966(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        time.sleep(3)

        assert self.fc.fd["system_control"].verify_optimize_oled_toggle_show() is False, "Optimize OLED toggle is displayed"
        assert self.fc.fd["system_control"].verify_optimize_oled_title_show() is False, "Optimize OLED title is displayed"
