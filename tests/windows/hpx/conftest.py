import pytest
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import conftest_misc
import time
import shutil
import logging

class PlatformNotMarkedException(Exception):
    pass

def pytest_addoption(parser):
    test_option = parser.getgroup('Windows HPX Test Parameters')
    test_option.addoption("--app-type", action="store", default="integration", help="The type of app you would like to run")
    test_option.addoption("--app-env", action="store", default="stg", help="The env of app you would like to run")
    test_option.addoption("--languages", action="store", default="en-US", help="Specify a comma-separated list of language codes for testing")
    test_option.addoption("--screenshot-workspace", action="store", default=None, help="Copy screenshot zip file to jenkins workspace")
    test_option.addoption("--sanity-check", action="store", default=None, help="Select cases for sanity check")
    test_option.addoption("--ota-test", action="store", default=None, help="HPX OTA tesing")
    

@pytest.fixture(scope="session")
def language(request):
    language_codes = request.config.getoption("--languages")
    return language_codes

def pytest_runtest_setup(item):
    platform_path = "C:\\Users\\exec\\platform.txt"
    stack = item.config.getoption("--stack")
    mobile_device = item.config.getoption("--mobile-device")
    ssh = SSH(mobile_device, "exec")
    if not (platform := ssh.send_command(f"cat {platform_path}", raise_e=False)):
        raise PlatformNotMarkedException(f"The machine: {mobile_device} is not marked with a platfrom at {platform_path}")
    
    stack_mark = [mark.args[0] for mark in item.iter_markers(name="require_stack")]
    exclude_platform_mark = [mark.args[0] for mark in item.iter_markers(name="exclude_platform")]
    require_platform_mark = [mark.args[0] for mark in item.iter_markers(name="require_platform")]
    sanity_test_mark = [mark.args[0] for mark in item.iter_markers(name="require_sanity_check")]

    platform = platform["stdout"].rstrip()

    if item.config.getoption("--sanity-check") is not None:
        try:
            sanity_test_mark[0] != ["sanity"]
        except IndexError:
            pytest.skip(f"Test does not run with sanity check test")

    if stack_mark and stack not in stack_mark[0]:
        pytest.skip(f"Test does not run on stack: {stack}")
    
    if exclude_platform_mark and platform in exclude_platform_mark[0]:
        pytest.skip(f"Test does not run on platform: {exclude_platform_mark} current platform: {platform}")

    if require_platform_mark and platform not in require_platform_mark[0]:
        pytest.skip(f"Test only run on platfrom: {require_platform_mark} current platform: {platform}")



@pytest.fixture(scope="session")
def publish_hpx_localization_screenshot(request, screenshot_folder_name):
    yield "Compress screenshot files."
    workspace = request.config.getoption("--screenshot-workspace")
    time.sleep(2)
    attachment_path = conftest_misc.get_attachment_folder()
    conftest_misc.save_localization_screenshot_and_publish(attachment_path + screenshot_folder_name + "/", attachment_path + screenshot_folder_name + ".zip")

    if workspace is not None:
        try:
            shutil.copy(attachment_path + screenshot_folder_name + ".zip", workspace + "/" + screenshot_folder_name + ".zip")
        except Exception as e:
            logging.info(f"Error occurred while creating copy file: {e}")   


def pytest_deselected(items):
    if not items:
        return
    config = items[0].session.config
    reporter = config.pluginmanager.getplugin("terminalreporter")
    reporter.ensure_newline()
    for item in items:
        reporter.line(f"skipped: {item.nodeid}", yellow=True, bold=True)
