import pytest
from MobileApps.libs.flows.ios.jweb.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_setup(request, session_setup):
    """
    This fixture is for Ios Jarvis set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest Ios Reference app
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = session_setup
    fc = FlowContainer(driver)
    stack = request.config.getoption("--stack").lower()
    if stack != "pie":
        fc.fd["ios_system"].clear_popups()
        fc.fd["ios_system"].switch_app_stack(stack, i_const.BUNDLE_ID.JWEB)
    return driver, fc