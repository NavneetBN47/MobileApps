import pytest

from MobileApps.libs.flows.windows.jweb.flow_container import FlowContainer

@pytest.fixture(scope="session")
def jweb_test_setup(windows_test_setup):
    driver = windows_test_setup
    fc = FlowContainer(driver)
    return driver, fc