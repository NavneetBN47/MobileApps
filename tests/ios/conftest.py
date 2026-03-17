import logging
import pytest
import re
import threading
from SAF.misc.saf_misc import *
from SAF.misc.ssh_utils import SSH
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.resources.const.mac.const import BUNDLE_ID as BUNDLE_ID_MAC
from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from paramiko.ssh_exception import SSHException
from socket import gaierror
from MobileApps.libs.flows.mac.smart.utility import smart_utilities
from selenium.common.exceptions import NoSuchWindowException


def pytest_addoption(parser):
    argument_group = parser.getgroup('IOS/MAC Test Parameters')
    argument_group.addoption("--app-type", action="store", default="adhoc", help="The type of app you would like to run")
    argument_group.addoption("--app-build", action="store", default=None, help="The build version of the app you would like to run")
    argument_group.addoption("--app-version", action="store", default=None, help="Which daily build version you would like to run. NOTE: Setting this option overrides the test fixture marker for MAC")
    argument_group.addoption("--app-release", action="store", default="daily", help="Which app relese to use [daily, weekly] NOTE: Setting this option overrides the test fixture marker")
    argument_group.addoption("--client-ip", action="store", default=exec, help="Ip address of the client machine")

def pytest_sessionstart(session):
    device_name = session.config.getoption("--mobile-device")
    if not device_name or re.search(r"i.phone", device_name, re.IGNORECASE):
        pytest.platform = "IOS"
    else:
        try:
            ssh = SSH(device_name, "exec", timeout=5)
            pytest.platform = "MAC"
            BUNDLE_ID.SMART = BUNDLE_ID_MAC.SMART
            pytest.mac_os_version = ssh.send_command("sw_vers -productVersion")["stdout"].strip()
            smart_utilities.dismiss_wda_popup(ssh)
            ssh.close()
        except (SSHException, gaierror):
            pytest.platform = "IOS"

@pytest.fixture(scope="class", autouse=True)
def clear_system_alerts(require_driver_session, ssh_client):
    if pytest.platform == "IOS":
        driver = require_driver_session
        ios_system = ios_system_flow_factory(driver)
        ios_system.clear_popups()
    else:
        smart_utilities.clear_mac_popups(ssh_client)

@pytest.fixture(scope="session")
def ssh_client(request):
    if pytest.platform == "MAC":
        if request.config.getoption("--mobile-device") is None:
            raise ValueError("You need to pass in mobile-device for this to work.")
        ssh = SSH(request.config.getoption("--mobile-device"), "exec")
        def close():
            ssh.close()
        request.addfinalizer(close)
        return ssh

def keep_chrome_alive(driver, interval=60):
    logging.critical("KEEPING CHROME ALIVE")
    while True:
        try:
            driver.get_current_url()
            sleep(interval)
        except (pytest.PytestUnhandledThreadExceptionWarning, NoSuchWindowException):
            logging.critical("CHROME WINDOW CLOSED")
            break

def create_chrome_thread(driver):
    thread = threading.Thread(target=keep_chrome_alive, args=(driver,))
    thread.start()
    return thread

@pytest.fixture(scope="session")
def utility_web_session(request, ssh_client):
    if pytest.platform == "MAC":
        ssh = ssh_client
        if request.config.getoption("--mobile-device") is None:
            raise ValueError("You need to pass in mobile-device for this to work.")
        executor_url = request.config.getoption("--mobile-device")
        profile_path = "/Users/exec/Library/Application Support/Google/Chrome/Default"
        ssh.send_command('killall "Google Chrome"', raise_e=False)
        web_driver = c_misc.utility_web_driver(browser_type="chrome", executor_url=executor_url, executor_port=4444, profile_path=profile_path, request=request)
        keep_alive_thread = create_chrome_thread(web_driver)
        def close():
            web_driver.close()
            if keep_alive_thread.is_alive():
                keep_alive_thread.join()
                logging.critical("STOPPED CHROME ALIVE THREAD")
        request.addfinalizer(close)
        return web_driver