import pytest
import time
import logging
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM


@pytest.fixture(scope="function", autouse=True)
def set_printer_to_ready_state_ledm(request):
    request.cls.driver.press_key_home()
    request.cls.fc.terminate_and_relaunch_hpx()
    time.sleep(10)
    InformationSimulatorLEDM.ready(request.cls.error_manager)
    time.sleep(5)    # time to allow the printer to be ready state
    logging.info("Printer is in ready state")
