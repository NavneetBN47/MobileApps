from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.vcosmos_utilities import VcosmosUtilities
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_usb_and_charger")
class Test_Suite_PC_Device_HPGO(object):
    
    #this suite should run on divinity platform
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_click_hpgo_card_under_pc_device_page_C42902489(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(7)
        # verify hpgo card is show up
        assert self.fc.fd["hp_go"].verify_hpgo_card_show_up(), "HP Go card is not displayed"
        # Click on the HP Go card
        self.fc.fd["hp_go"].click_hpgo_card()
        time.sleep(2)
        assert self.fc.fd["hp_go"].verify_hp_go_title_on_hp_go_page(), "HP Go title is not displayed"
