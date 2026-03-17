import pytest
import time
import logging
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM

@pytest.fixture(scope="function",autouse=True)
def set_printer_to_ready_state_cdm(request):
    request.cls.driver.press_key_home()
    request.cls.fc.terminate_and_relaunch_hpx()
    time.sleep(10)
    InformationSimulatorCDM.ready(request.cls.error_manager)
    time.sleep(5)    # allow time to set the printer to be ready state
    logging.info("Set the printer to ready state.")