import pytest
from MobileApps.libs.flows.web.wex.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def wex_setup(request, web_session_setup):
    """
    This fixture is for WEX set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param web_session_setup:
    :return:
    """
    driver = web_session_setup
    fc = FlowContainer(driver)
    return driver, fc