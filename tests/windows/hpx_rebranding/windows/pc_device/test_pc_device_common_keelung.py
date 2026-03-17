from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_PC_Device_Functional_Common(object):
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_no_battery_status_badge_C53002514(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].get_battery_status_icon_text() == "Battery Off No battery", "Battery status icon text is not matching"



