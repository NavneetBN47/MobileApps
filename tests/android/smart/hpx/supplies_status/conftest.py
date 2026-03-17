import pytest
import time
from MobileApps.libs.flows.android.smart.flow_container import FlowContainer, FLOW_NAMES


@pytest.fixture(scope="session",autouse=True)
def class_setup_for_android_supplies(request,android_smart_flow_setup,load_printers_session):
    session_driver,session_fc = android_smart_flow_setup
    request.session.driver = session_driver
    request.session.fc = session_fc
    # Printer Information
    p = load_printers_session
    printer_ip  = p.get_printer_information()["ip address"]
    printer_serial_number = p.get_printer_information()["serial number"]
    request.session.printer_ip = printer_ip
    request.session.printer_serial_number = printer_serial_number
    request.session.fc.reset_app()
    request.session.fc.flow_load_home_screen(skip_value_prop=True)
    request.session.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS].click_add_device_btn()
    time.sleep(5)
    request.session.driver.wdvr.execute_script("mobile: clickGesture", {"x": 500, "y": 1000})
    request.session.fc.fd[FLOW_NAMES.PRINTERS].search_printer_by_ip(printer_ip)
    def clean_up():
        request.session.fc.kill_hpx_app()
        request.session.fc.kill_chrome()
    request.addfinalizer(clean_up)
