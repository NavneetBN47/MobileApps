import os
import pytest
import traceback

from SAF.misc.saf_misc import *
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc

pytest.platform = "MAC"
pytest.mac_os_version = os.popen("sw_vers -productVersion").read(5)

def pytest_addoption(parser):
    mac_argument_group = parser.getgroup('Mac Test Parameters')
    mac_argument_group.addoption("--app-build", action="store", default="debug", help="Which app build to use [debug, release, ga] NOTE: Setting this option overrides the test fixture marker")
    mac_argument_group.addoption("--app-release", action="store", default="daily", help="Which app relese to use [daily, weekly] NOTE: Setting this option overrides the test fixture marker")
    mac_argument_group.addoption("--app-version", action="store", default=None, help="Which app-version to use. NOTE: Setting this option overrides the test fixture marker")
    mac_argument_group.addoption("--client-ip", action="store", default=exec, help="Ip address of the client machine")

# ----------------      FUNCTION     ---------------------------
@pytest.fixture(scope="session")
def start_driver(request, session_setup, require_driver_session, ssh_client):
    """
    Test general precondition for Mac test
        + Create log file which store log of test script
        + Updating list when adding new precondition into this fixture
        + Change language

    :param request:
    """
    try:
        system_config = ma_misc.load_system_config_file()
        driver = require_driver_session

        # Change OS language and region
        # lang = request.config.getoption("--lang")
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment + "/mac_test_setup_failed.png")
        c_misc.save_source_and_publish(driver, session_attachment + "/", file_name="mac_test_setup_failed_page_source.txt")
        traceback.print_exc()
        raise

    return driver

@pytest.fixture(scope="session")
def ssh_client(request):
    if request.config.getoption("--mobile-device") is None:
        raise ValueError("You need to pass in mobile-device for this to work.")
    ssh = SSH(request.config.getoption("--mobile-device"), "exec")
    def close():
        ssh.close()
    request.addfinalizer(close)
    return ssh

# Mac Install App
@pytest.fixture(scope="session")
def install_app(request, ssh_client):
    app_url, file_name = c_misc.get_package_url(request, _os="MAC", project=pytest.app_info)
    ssh = ssh_client
    unique_file_path = download_file(app_url, save_path='/tmp/temp_package')
    ssh.send_file(unique_file_path, './Downloads/{}'.format(file_name))
    if '.zip' in file_name:
        ssh.send_command('unzip -qq -o ./Downloads/{} -d /Users/exec/Applications/'.format(file_name))
    elif '.pkg' in file_name:
        ssh.send_command('installer -pkg ./Downloads/{} -target CurrentUserHomeDirectory'.format(file_name))
    ssh.send_command('rm -r ./Downloads/{}'.format(file_name))
    