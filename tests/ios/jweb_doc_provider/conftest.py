import pytest
from MobileApps.libs.flows.ios.jweb_doc_provider.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_doc_provider_setup(request, session_setup):
    """
    This fixture is for iOS Doc Provider set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest iOS Doc Provider app
        - iOS Doc Provider System Settings do not provide Stack selection
    """
    driver = session_setup
    fc = FlowContainer(driver)
    return driver, fc 