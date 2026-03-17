import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_restart_machine(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.ota
    def test_01_test_machine_restart(self, request):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        
        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()