import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Slaves(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_slaves_can_run_suite_normally(self):
        self.fc.fd["devicesMFE"].click_device_card()