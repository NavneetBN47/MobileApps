import pytest
import time
import logging
import os
from SAF.misc import windows_utils
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc.ledm_log_collector import LEDMLogCollector
from MobileApps.libs.ma_misc.cdm_log_collector import CDMLogCollector

def pytest_addoption(parser):
    supplies_argument_group = parser.getgroup('SupplyStatus Test Parameters')
    supplies_argument_group.addoption("--supplies-logs", action="store_true", default=False, help="Flag to enable LEDM log collection on test failure")
    supplies_argument_group.addoption("--ledm", action="store_true", default=None, help="Flag to enable LEDM log collection on test failure")
    supplies_argument_group.addoption("--cdm", action="store_true", default=None, help="Flag to enable CDM log collection on test failure")

@pytest.fixture(scope="session",autouse=True)
def setup_to_add_printer(request,windows_test_setup,load_printers_session):
    session_driver = windows_test_setup
    fc = FlowContainer(session_driver)
    request.session.driver = session_driver
    request.session.fc = fc
    p = load_printers_session
    printer_ip = p.get_printer_information()["ip address"]
    serial_number = p.get_printer_information()["serial number"]
    request.printer_ip = printer_ip
    # Store at session level for class-level access
    request.session.printer_ip = printer_ip
    request.session.printer_serial_number = serial_number
    set_the_test_environment(request)
    re_launch_if_app_not_open_successfully(request)
    adding_printer_flow(request)

    def supplies_cleanup():
        fc.kill_chrome_process()
        fc.kill_hpx_process()
        remote_artifact_path = "{}\\{}\\LocalState".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if windows_utils.check_path_exist(session_driver.ssh, remote_artifact_path) is True:
            session_driver.ssh.send_command('Get-ChildItem {} | Remove-Item -Recurse -Force'.format(remote_artifact_path), raise_e=False)
            time.sleep(3)
            logging.info(f"Clean up HPX LocalState successfully.")

        try:
            session_driver.ssh.send_command('Stop-Process -Name "*Store*"')
            session_driver.ssh.send_command('Stop-Process -Name "*SystemSettings*"')
            session_driver.ssh.send_command('Stop-Process -Name "*onenote*"')
            process_output = session_driver.ssh.send_command("Get-Process")["stdout"]
            if "PSADriverApp" in process_output:
                session_driver.ssh.send_command('Stop-Process -Name "PSADriverApp"')
            if "HPPrinterHealthMonitor" in process_output:
                session_driver.ssh.send_command('Stop-Process -Name "HPPrinterHealthMonitor"')
            if "HPAudioControl_19H1" in process_output:
                session_driver.ssh.send_command('Stop-Process -Name "HPAudioControl_19H1"')
        except Exception as e: 
            logging.warning(f"Unable to set size minimize: {e}")
    request.addfinalizer(supplies_cleanup)

def set_the_test_environment(request):
    """
    Restore the system to ready state after test execution.
    """
    fc = request.session.fc
    fc.terminate_conflicting_hp_processes()
    fc.fd["accessibility"].dismiss_open_windows_overlays()
    fc.change_system_region_to_united_states()
    fc.web_password_credential_delete()
    fc.initial_hpx_printer_env()
    time.sleep(2)  # allow time for the environment to initialize

def adding_printer_flow(request):
    """
    Adding printer flow used by SupplyStatus tests.
    """
    fc = request.session.fc
    fc.fd["devicesMFE"].verify_add_device_button_show_up()
    fc.fd["devicesMFE"].click_add_button()
    fc.fd["addprinter"].verify_add_device_panel()
    fc.fd["addprinter"].click_choose_printer_button()
    fc.fd["supplies_status"].add_printer_by_using_ip_if_no_printers_found()
    fc.fd["addprinter"].wait_for_printer_input_box_ready()
    fc.fd["addprinter"].click_input_textbox()
    fc.fd["addprinter"].input_ip_address(ip=request.printer_ip)
    fc.fd["addprinter"].click_add_printer_btn()
    logging.info("Click 'Add Printer' button.")
    if fc.fd["addprinter"].verify_auto_install_driver_to_print(raise_e=False):
        fc.fd["addprinter"].verify_auto_install_driver_to_print_disappear()
        if fc.fd["addprinter"].verify_auto_install_driver_done(timeout=5, raise_e=False):
            logging.info("Driver installed successfully.")
            fc.fd["addprinter"].click_continue_btn()
        else:
            logging.warning("Driver installation failed.")
            fc.fd["addprinter"].click_top_exit_setup_btn()
            if fc.fd["addprinter"].verify_setup_incomplete_dialog(raise_e=False):
                fc.fd["addprinter"].click_setup_incomplete_dialog_exit_setup_btn()
                if fc.fd["addprinter"].verify_printer_setup_is_incomplete_dialog(raise_e=False):
                    fc.fd["addprinter"].click_printer_setup_is_incomplete_dialog_ok_btn()
    logging.info("Printer added successfully.")

def ledm_log_collection(request, test_result_folder, ip_address, test_case_name):
    """
    Collect LEDM logs from printer for supply status debugging.
    Specifically moved to SupplyStatus conftest for targeted log collection.
    """
    if not ip_address:
        logging.warning("No printer IP address provided for LEDM log collection.")
        return

    log_collector = LEDMLogCollector()
    log_collector.printer_ip = ip_address

    logging.info(f"Collecting the LEDM logs...")
    log_data = {
        "product_status_dyn": log_collector.collect_product_status_dyn(),
        "product_consumable_config_dyn": log_collector.collect_product_consumable_config_dyn(),
        "product_config_dyn": log_collector.collect_product_config_dyn()
    }

    for log_type, data in log_data.items():
        file_name = f"{log_type}_{test_case_name}.xml"
        file_path = os.path.join(test_result_folder, file_name)
        log_collector.write_log_to_file(data, file_path)

def cdm_log_collection(request, test_result_folder, ip_address, test_case_name):
    """
    Collect CDM logs from printer for supply status debugging.
    Specifically moved to SupplyStatus conftest for targeted log collection.
    """
    if not ip_address:
        logging.warning("No printer IP address provided for CDM log collection.")
        return

    log_collector = CDMLogCollector()
    log_collector.printer_ip = ip_address

    logging.info(f"Collecting the CDM logs...")
    log_data = {
        "cdm_supplies_public": log_collector.collect_supplies_public(),
        "cdm_alerts": log_collector.collect_alerts()
    }

    for log_type, data in log_data.items():
        file_name = f"{log_type}_{test_case_name}.xml"
        file_path = os.path.join(test_result_folder, file_name)
        log_collector.write_log_to_file(data, file_path)

@pytest.fixture(scope="function", autouse=True)
def supply_status_cleanup(request):
    """
    Auto-cleanup fixture for SupplyStatus tests.
    Collects LEDM logs when tests fail.
    """
    yield
    if request.session.testsfailed and request.config.getoption("--supplies-logs"):
        logging.info(f"Test failed: {request.node.name}")
        logging.error("SupplyStatus test failed. Collecting LEDM logs...")
        try:
            p = request.cls.p
            ip_addr = p.get_printer_information()["ip address"]
            attachment_root_path = pytest.test_result_folder + "attachment/"
            if not os.path.isdir(attachment_root_path):
                os.makedirs(attachment_root_path)
            test_case_name = request.node.name
            if request.config.getoption("--ledm"):
                # Collect LEDM logs
                ledm_log_collection(request, attachment_root_path, ip_addr, test_case_name)
                logging.info("LEDM logs collected successfully for SupplyStatus test failure.")
            elif request.config.getoption("--cdm"):
                # Collect CDM logs
                cdm_log_collection(request, attachment_root_path, ip_addr, test_case_name)
                logging.info("CDM logs collected successfully for SupplyStatus test failure.")
        except Exception as e:
            logging.warning(f"Failed to collect logs: {e}")
    else:
        logging.info("No test failures detected or --supplies-logs flag not provided. Skipping LEDM log collection.")

def re_launch_if_app_not_open_successfully(request):
    fc  = request.session.fc
    for attempt in range(3):
        logging.info(f"Launching myHP app, attempt {attempt+1}...")
        fc.launch_myHP()
        if not fc.is_app_open():
            logging.warning(f"myHP app not launched, attempt {attempt+1} failed.")
            continue
        if fc.fd["devicesMFE"].verify_profile_and_settings_icon_button_lzero_page() is not False:
            logging.info("myHP app launched successfully & homepage loaded successfully...")
            fc.fd["css"].maximize_hp()
            break
        fc.close_myHP()
