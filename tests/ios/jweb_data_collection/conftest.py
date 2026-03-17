import pytest
import logging
from MobileApps.libs.flows.ios.jweb_data_collection.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_data_collection_setup(request, session_setup):
    """
    This fixture is for Ios Data Collection set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest Ios Data Collection app
    """
    driver = session_setup
    fc = FlowContainer(driver)
    stack = request.config.getoption("--stack").lower()
    if stack != "dev":
        fc.fd["ios_system"].clear_popups()
        fc.fd["ios_system"].switch_app_stack(stack, i_const.BUNDLE_ID.JWEB_DATA_COLLECTION)
    return driver, fc