import pytest
import time
import logging
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM

@pytest.fixture(scope="function",autouse=True)
def set_printer_to_ready_state_cdm(request):
    if request.cls.fc.is_app_open():
        logging.info("App is already open, closing it first.")
        request.cls.fc.close_myHP()
        re_launch_if_app_not_open_successfully(request)
    else:
        re_launch_if_app_not_open_successfully(request)
    InformationSimulatorCDM.ready(request.cls.error_manager)
    request.cls.fc.verify_whther_app_is_on_printer_card_page()
    time.sleep(5)    # allow time to set the printer to be ready state

def re_launch_if_app_not_open_successfully(request):
    for attempt in range(3):
        logging.info(f"Launching myHP app, attempt {attempt+1}...")
        request.cls.fc.launch_myHP_command()
        if not request.cls.fc.is_app_open():
            logging.warning(f"myHP app not launched, attempt {attempt+1} failed.")
            continue
        if request.cls.fc.fd["devicesMFE"].verify_profile_and_settings_icon_button_lzero_page() is not False:
            logging.info("myHP app launched successfully & homepage loaded successfully...")
            request.cls.fc.fd["css"].maximize_hp()
            break
        request.cls.fc.close_myHP()
