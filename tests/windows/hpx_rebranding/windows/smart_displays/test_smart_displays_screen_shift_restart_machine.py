import time
import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Smart_Displays_Screen_Shift_Restart_Machine(object):
    
   
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_restart_machine_verify_screen_display_function_C65453124(self, request):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_lone_page()
        time.sleep(2)
        self.fc.fd["smart_displays"].verify_banner_image_show(), "Banner image is not displayed"


        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_lone_page()
        time.sleep(2)
        self.fc.fd["smart_displays"].verify_banner_image_show(), "Banner image is not displayed"
