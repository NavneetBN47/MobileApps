import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_HPPK_Robotics(object):
    
    #this suite should run on masadanx platform
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_default_hppk_key_f11_C42900993(self):
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.close_myHP()
        self.vcosmos.press_f11_hppk_key()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        self.vcosmos.clean_up_logs()    