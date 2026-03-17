import pytest
import requests
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.flows.web.poobe.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.web.hp_id.hp_id import HPID


@pytest.fixture(scope="class")
def olex_123_test_setup(web_session_setup, request):
    driver = web_session_setup
    driver.set_size("max")
    fc = FlowContainer(driver, None, None, "main")
    hpid = HPID(driver)
    try:
        driver.navigate(fc.fd["hp_123"].url_123)
    except:
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source.txt")
        c_misc.save_screenshot_and_publish(driver,"{}/screenshot_{}.png".format(attachment_root_path, request.node.name))
        if request.config.getoption("--har"):
            c_misc.save_har_and_publish(driver, attachment_root_path, file_name="poobe_har")
        raise AssertionError("Test Setup failed")
    
    return (driver, fc, hpid)