import pytest
from MobileApps.libs.flows.ios.jweb_value_store.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_value_store_setup(request, session_setup):
    """
    This fixture is for iOS Value Store set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest iOS Value Store app
        - iOS Value Store System Settings do not provide Stack selection
    """
    driver = session_setup
    fc = FlowContainer(driver)
    return driver, fc 