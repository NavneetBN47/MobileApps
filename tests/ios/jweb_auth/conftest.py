import pytest
import logging
from MobileApps.libs.flows.ios.jweb_auth.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_auth_setup(request, session_setup):
    """
    This fixture is for iOS Auth Reference App set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest iOS Auth Reference App
    """
    driver = session_setup
    fc = FlowContainer(driver)
    stack = request.config.getoption("--stack").lower()
    if stack == "pie":
        logging.info("{} does not have a pie stack to switch to".format(i_const.BUNDLE_ID.JWEB_AUTH))
    if stack not in ["pie", "dev"]:
        fc.fd["ios_system"].clear_popups()
        fc.fd["ios_system"].switch_app_stack(stack, i_const.BUNDLE_ID.JWEB_AUTH)
    return driver, fc