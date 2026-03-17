import pytest
from MobileApps.libs.flows.mac.jweb.flow_container import FlowContainer
from MobileApps.libs.flows.mac.jweb.utility import jweb_utilities
from MobileApps.libs.app_package.app_class_factory import app_module_factory

@pytest.fixture(scope="session", autouse=True)
def mac_jweb_setup(install_app, start_driver):
    """
    This fixture is for Mac Jarvis Web set up :
        - Get driver instance
    :param start_driver:
    :return:
    """
    driver = start_driver
    fc = FlowContainer(driver)
    return driver, fc