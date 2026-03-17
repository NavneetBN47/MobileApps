from flask import logging
import pytest
from MobileApps.libs.flows.web.poobe.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from SAF.misc.ssh_utils import SSH
import logging


@pytest.fixture(scope="class")
def ssh_client(request):
    """SSH client for web tests to access the test machine"""
    test_machine = request.config.getoption("--mobile-device")
    if test_machine is None:
        raise ValueError("You need to pass --mobile-device to enable SSH access")
    
    ssh = SSH(test_machine, "exec")
    
    def close():
        ssh.close()
    
    request.addfinalizer(close)
    return ssh

@pytest.fixture(scope="class")
def olex_123_psw_test_setup(web_session_setup, ssh_client, request):
    driver = web_session_setup
    screen_size = request.config.getoption("--browser-size") or "max"
    driver.set_size(screen_size)
    printer_profile = request.config.getoption("--printer-profile")
    locale = request.config.getoption("--locale")
    if locale:
        locale = locale.replace("_", "/") # us_en
    fc = FlowContainer(driver, None, printer_profile)
    hpid = fc.fd["hpid"]
    try:
        driver.navigate(fc.fd["traffic_director"].td_url)
        hpid.verify_privacy_popup(timeout=15)
    except:
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source.txt")
        c_misc.save_screenshot_and_publish(driver,"{}/screenshot_{}.png".format(attachment_root_path, request.node.name))
        if request.config.getoption("--har"):
            c_misc.save_har_and_publish(driver, attachment_root_path, file_name="poobe_har")
        raise AssertionError("Test Setup failed")
    
    return (driver, fc, printer_profile, hpid, ssh_client)