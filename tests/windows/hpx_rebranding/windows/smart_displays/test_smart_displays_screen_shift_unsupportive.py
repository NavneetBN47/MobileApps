import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
# This test suite only available ITG and STG build now
class Test_Smart_Displays_Screen_Shift_Unsupportive(object):

    @pytest.mark.function
    @pytest.mark.consumer
    def test_01_verify_smart_displays_on_unsupportive_machine_C57812968(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page() is False, "Smart Displays L1 card is displayed"



