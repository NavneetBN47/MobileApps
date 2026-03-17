import time
import pytest
import logging
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import windows_utils
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import os


pytest.platform = "WINDOWS"

def pytest_addoption(parser):
    test_option = parser.getgroup("HPX Test Parameters")

@pytest.fixture(scope="class", autouse=True)
def win_hpx_cleanup(request, windows_test_setup, utility_web_session):
    """
    Clean up 'C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\LocalState'
    """
    driver = windows_test_setup
    web_driver = utility_web_session
    fc = FlowContainer(driver)
    fc.disable_dark_mode()
    fc.enable_location_access()
    fc.web_password_credential_delete()

    try:
        web_driver.set_size("min")
        process_names = ["*Store*", "*SystemSettings*", "*onenote*"]
        for pname in process_names:
            request.cls.driver.ssh.send_command(f'Stop-Process -Name "{pname}"')

    except Exception as e: 
        logging.warning(f"Unable to set size minimize: {e}.")

    def cleanup():
        fc.close_myHP()
        time.sleep(2)
        remote_artifact_path = "{}\\{}\\LocalState".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        if windows_utils.check_path_exist(driver.ssh, remote_artifact_path) is True:
            driver.ssh.send_command('Get-ChildItem {} | Remove-Item -Recurse -Force'.format(remote_artifact_path), raise_e=False)
            time.sleep(3)
            logging.info(f"Clean up HPX LocalState successfully.")
    request.addfinalizer(cleanup)
   
@pytest.fixture(scope="class")
def temp_files_cleanup(request):
    """
    Clean up temp files
    """
    root_path = ma_misc.get_abs_path("/resources", False)
    temp_path = str("{}/test_data/hpx_rebranding/screenshot/temp".format(root_path))
    if not os.path.isdir(temp_path):
        os.makedirs(temp_path)
    def cleanup():
        try:
            ma_misc.delete_content_of_folder(temp_path)
            logging.info(f"Clean up temp files successfully.")
        except Exception as e: 
            logging.warning(f"Clean up failed due to: {e}.")
    request.addfinalizer(cleanup)

@pytest.fixture(scope="class", autouse=True)
def printer_driver_cleanup(request, windows_test_setup):
    """
    Clean up printer drivers installed on windows.
    """
    driver = windows_test_setup

    def printer_driver_delete():
        keywords = ["hp", "OneSimulator"]
        for keyword in keywords:
            printer = driver.ssh.send_command(f'Get-Printer -Name "*{keyword}*"')
            if printer["stdout"]:
                print_job = driver.ssh.send_command('Get-WmiObject Win32_PrintJob')
                if print_job["stdout"]:
                    driver.ssh.send_command('Stop-Service -Name Spooler -Force')
                    time.sleep(1)
                    driver.ssh.send_command('Get-ChildItem "C:\\Windows\\System32\\spool\\PRINTERS\\" | Remove-Item -Recurse -Force', raise_e=False)
                    time.sleep(1)
                    driver.ssh.send_command('Start-Service -Name Spooler')

                driver.ssh.send_command(f'Remove-Printer -Name "*{keyword}*"', timeout=20, raise_e=False)
                time.sleep(1)
                driver.ssh.send_command(f'Remove-PrinterDriver -Name "{keyword}*"', timeout=20, raise_e=False)
    request.addfinalizer(printer_driver_delete)

@pytest.fixture(scope="class")
def logout_cleanup(request, windows_test_setup):
    """
    logout from HPX app after test case execution
    """
    driver = windows_test_setup
    fc = FlowContainer(driver)
    def cleanup():
        fc.restart_hpx()
        if fc.fd["devicesMFE"].verify_login_successfully(timeout=20, raise_e=False) is not False:
            logging.info("logging out from HPX app...")
            fc.sign_out(hpx_logout=True)
        else:
            logging.info("HPX app has been logged out.")
        fc.web_password_credential_delete()
    request.addfinalizer(cleanup)

@pytest.fixture(scope="class")
def chrome_account_data_cleanup(request, windows_test_setup):
    """
    Clean up Chrome account data.
    """
    driver = windows_test_setup
    def cleanup():
        driver.ssh.send_command('Stop-Process -Name "chrome" -Force -ErrorAction SilentlyContinue', raise_e=False)
        commands = [
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\*"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Storage\\*"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"',
            '"C:\\Users\\exec\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data"'
        ]
        for cmd in commands:
            driver.ssh.send_command('Remove-Item -Path ' + cmd + ' -Recurse -Force')
            time.sleep(1)
        logging.info("Chrome user data cleanup complete.")
    request.addfinalizer(cleanup)
