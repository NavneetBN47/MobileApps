import pytest
from MobileApps.libs.flows.ios.jweb_service_routing.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_service_routing_setup(request, session_setup):
    """
    This fixture is for iOS Service Routing set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest iOS Service Routing app
    """
    driver = session_setup
    fc = FlowContainer(driver)
    stack = request.config.getoption("--stack").lower()
    if stack != "mock":
        fc.fd["ios_system"].clear_popups()
        fc.fd["ios_system"].switch_app_stack(stack, i_const.BUNDLE_ID.JWEB_SERVICE_ROUTING)
    return driver, fc 