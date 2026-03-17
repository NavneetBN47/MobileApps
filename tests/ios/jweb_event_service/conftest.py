import pytest
from MobileApps.libs.flows.ios.jweb_event_service.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_event_service_setup(request, session_setup):
    """
    This fixture is for iOS Event Service set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest iOS Event Service app
        - iOS Event Service System Settings do not provide Stack selection
    """
    driver = session_setup
    fc = FlowContainer(driver)
    return driver, fc 