import os
import uuid
import pytest
import MobileApps.libs.ma_misc.conftest_misc as c_misc

pytest.platform = "WEB"

def pytest_addoption(parser):
    web_argument_group = parser.getgroup('Web Test Parameters')
    web_argument_group.addoption("--browser-type", action = "store", default="firefox", help="Chose which type of browser you want to test with")
    web_argument_group.addoption("--platform", action="store", default="ANY", help="Specifiy what platform you want to run on")
    web_argument_group.addoption("--uuid", action="store", default=str(uuid.uuid4()), help="UUID associated with each pytest session (For jenkins)")
    web_argument_group.addoption("--detach", action="store_true", default=False, help="Detaches the browser from the driver, used for leaving browsers open after script")
    web_argument_group.addoption("--har", action="store_true", default=False, help="Enable har file capturing")
    web_argument_group.addoption("--proxy-device", action="store", default="VNBEA00043", help="Serial Number of the Proxy Device to run the test on")

@pytest.fixture(scope="function", autouse=True)
def web_capture_har(request):
    """
    Clean up all following popup before and after executing each test:
        - App crash
    """
    def get_har():
        if not request.config.getoption("--har") or request.node.rep_call.failed:
            return True
        driver = request.cls.driver
        del driver.wdvr.requests
    request.addfinalizer(get_har)
