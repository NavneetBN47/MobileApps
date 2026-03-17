import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Wellbeing_UI(object):
    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_luanch_hpx_to_pcdevice_page_and_check_wellbeing_show_C51598825(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "Wellbeing card not found"
    

    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_02_restart_machine_verify_wellbeing_function_C63936962(self, request):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(10)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(1)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)

        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen time toggle is not off"
        assert self.fc.fd["wellbeing"].verify_alert_options_title_show_up(), "Alert options is not displayed"
        assert self.fc.fd["wellbeing"].verify_set_preferred_distance_icon_show_up(), "Set preferred distance icon is not displayed"

        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(1)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(2)

        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen time toggle is not off"
        assert self.fc.fd["wellbeing"].verify_alert_options_title_show_up(), "Alert options is not displayed"
        assert self.fc.fd["wellbeing"].verify_set_preferred_distance_icon_show_up(), "Set preferred distance icon is not displayed"


