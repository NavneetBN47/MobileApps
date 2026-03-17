import pytest

from MobileApps.libs.flows.windows.jweb_doc_provider.flow_container import FlowContainer

@pytest.fixture(scope="session")
def jweb_doc_provider_test_setup(windows_test_setup):
    driver = windows_test_setup
    fc = FlowContainer(driver)
    return driver, fc