import os
import time
import pytest
import logging
import traceback

import MobileApps.libs.ma_misc.conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.common.gotham.flow_container import FlowContainer
from MobileApps.libs.flows.common.gotham.system_preferences import SystemPreferences
from selenium.common.exceptions import NoSuchElementException

pytest.platform = "WINDOWS"

def pytest_addoption(parser):
    test_option = parser.getgroup("GothamWin Test Parameters")

# ----------------      FUNCTION     ---------------------------

@pytest.fixture(scope="class", autouse=True)
def windows_smart_setup(request, ssh_client, windows_test_setup, utility_web_session):
    try:
        driver = windows_test_setup
        web_driver = utility_web_session
        try:
            web_driver.set_size("min")
        except Exception as e: 
            logging.warning(f"Unable to set size minimize")
            
        ssh = ssh_client
        ssh.send_command('netsh wlan delete profile *')
        if "244" not in ssh.send_command('Get-WinHomeLocation')["stdout"]:
            ssh.send_command('Set-WinHomeLocation -GeoId 244')

        try:    
            ssh.send_command('Stop-Service -Name Spooler -Force')
            time.sleep(1)
            ssh.send_command('Get-ChildItem "C:\\Windows\\System32\\spool\\PRINTERS\\" | Remove-Item -Recurse -Force')
            time.sleep(1)
            ssh.send_command('Start-Service -Name Spooler', timeout=30)
            ssh.send_command('Remove-Printer -Name "*HP*"', timeout=30)
            ssh.send_command('Remove-PrinterDriver -Name "HP*"', timeout=30)
        except Exception as e:
            logging.warning("Failed to delete printer driver")

        fc = FlowContainer(driver, web_driver)
        stack = request.config.getoption("--stack")
        
        fc.web_password_credential_delete()
        fc.reset_hp_smart()
        fc.change_stack_server(stack)
        return driver, fc
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment, exist_ok=True)
        c_misc.save_windows_app_log_and_publish(pytest.app_info, driver, session_attachment + "/", request.node.name)
        c_misc.save_screenshot_and_publish(driver, session_attachment + "/windows_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment + "/", file_name = "windows_test_setup_failed_page_source.txt")
        traceback.print_exc()   
        raise

@pytest.fixture(scope="class", autouse=True)
def smart_account_cleanup(request, windows_test_setup, utility_web_session):
    driver = windows_test_setup
    web_driver = utility_web_session 
    fc = FlowContainer(driver, web_driver)

    def logout():
        try:
            web_driver.set_size("min")
        except Exception as e: 
            logging.warning(f"Unable to set size minimize")
        fc.restart_hp_smart()
        try:
            fc.go_home()
            if fc.fd["home"].verify_logged_in(timeout=3, raise_e=False):
                fc.sign_out()  
        except Exception as e: 
            logging.warning(f"Unable to clean up due to: {e}")
    request.addfinalizer(logout)

@pytest.fixture(scope="class", autouse=True)
def printer_driver_cleanup(request, ssh_client, windows_test_setup, utility_web_session):
    """
    Clean up printer drivers installed on windows.
    """
    driver = windows_test_setup
    web_driver = utility_web_session 
    fc = FlowContainer(driver, web_driver)

    def printer_driver_delete():
        ssh = ssh_client
        printer = ssh.send_command('Get-Printer -Name "*hp*"')
        if printer["stdout"]:
            print_job = ssh.send_command('Get-WmiObject Win32_PrintJob')
            if print_job["stdout"]:
                # ssh.send_command('(Get-WmiObject Win32_PrintJob).Delete()')
                ssh.send_command('Stop-Service -Name Spooler -Force')
                time.sleep(1)
                ssh.send_command('Get-ChildItem "C:\\Windows\\System32\\spool\\PRINTERS\\" | Remove-Item -Recurse -Force', raise_e=False)
                time.sleep(1)
                ssh.send_command('Start-Service -Name Spooler')

            ssh.send_command('Remove-Printer -Name "*HP*"', timeout=20, raise_e=False)
            time.sleep(1)
            ssh.send_command('Remove-PrinterDriver -Name "HP*"', timeout=20, raise_e=False)
    request.addfinalizer(printer_driver_delete)

@pytest.fixture(scope="class")
def microsoft_account_cleanup(request, windows_test_setup, utility_web_session):
    driver = windows_test_setup
    web_driver = utility_web_session 
    fc = FlowContainer(driver, web_driver)
    sp = SystemPreferences(driver)
    launch_activity, close_activity = fc.get_activity_parameter()
    def logout():
        """
        Logout microsoft account
        """
        try: 
            driver.terminate_app(close_activity)
            time.sleep(2)
            driver.ssh.send_command('Start-Process "ms-windows-store://home"')
            sp.verify_ms_display()
            time.sleep(2)
            sp.click_ms_account_btn()
            if sp.verify_ms_is_login():
                sp.click_ms_sign_out_btn()
            
        except NoSuchElementException:         
            raise NoSuchElementException(
                    "Error happened during microsoft logout process...")
        finally:
            driver.ssh.send_command('Stop-Process -Name "*Store*"')
            driver.launch_app(launch_activity)
    request.addfinalizer(logout)

@pytest.fixture(scope="class")
def restore_system_time(request, windows_test_setup):
    driver = windows_test_setup
    def restore():
        status = driver.ssh.send_command('Get-Service w32time | select-object Status')['stdout'].strip()
        if 'Stopped' in status:
          driver.ssh.send_command('Start-Service w32time')
        driver.ssh.send_command('W32tm /resync /force', raise_e=False)
    request.addfinalizer(restore)

@pytest.fixture(scope="class")
def clear_shortcuts_jobs(request, windows_test_setup, utility_web_session):
    driver = windows_test_setup
    web_driver = utility_web_session
    fc = FlowContainer(driver, web_driver)
    def clear():
        try:
            logging.debug("Start cleaning up shortcuts jobs....")
            fc.clear_shortcuts_jobs()
        except Exception : 
            logging.warning("clean up failure, Please check shortcuts screen")
    request.addfinalizer(clear)

@pytest.fixture(scope="class")
def clear_printer_data(request, windows_test_setup, utility_web_session, load_printers_session):
    driver = windows_test_setup
    web_driver = utility_web_session
    fc = FlowContainer(driver, web_driver)
    p = load_printers_session
    ssid, password = c_misc.get_wifi_info(request)
    host = request.config.getoption("--mobile-device")
    user = "exec"
    def clear():
        driver.connect_to_wifi(host, user, ssid, password)
        time.sleep(2)
        logging.debug("Start clear printer data....")
        printer_uuid = p.p_obj.deviceUuid
        fc.clear_printer_data_flow(printer_uuid)
    request.addfinalizer(clear)

@pytest.fixture(scope="class")
def restore_devices_status(request, windows_test_setup, load_printers_session):
    driver = windows_test_setup
    p = load_printers_session
    ssid, password = c_misc.get_wifi_info(request)
    host = request.config.getoption("--mobile-device")
    user = "exec"
    def connect():
        if "DunePrinterInfo" in str(p.p_obj):
            p.pp_module._power_on()
        driver.connect_to_wifi(host, user, ssid, password)
    request.addfinalizer(connect)

@pytest.fixture(scope="class")
def check_bluetooth_network(request, windows_test_setup):
    driver = windows_test_setup
    check_bluetooth = driver.ssh.send_command('Get-NetAdapter | select-object Name')['stdout']
    if 'Bluetooth Network Connection' in check_bluetooth:
        driver.ssh.send_command('Disable-NetAdapter -Name "Bluetooth*" -Confirm:$false')
        def connect():
            driver.ssh.send_command('Enable-NetAdapter -Name "Bluetooth*"')
        request.addfinalizer(connect)

@pytest.fixture(scope="function", autouse=True)
def minimize_web_windows(windows_test_setup, utility_web_session):
    driver = windows_test_setup
    web_driver = utility_web_session
    try:
        web_driver.set_size("min")
    except Exception as e: 
        logging.warning(f"Unable to set size minimize")
