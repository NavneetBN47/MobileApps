import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Touchpad_Unsupported(object):
        
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_check_touchpad_dont_show_on_pc_device_C43876475(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page() is False, "Touchpad card is displayed"

