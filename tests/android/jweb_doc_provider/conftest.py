import pytest
import logging

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.jweb_doc_provider.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def android_jweb_doc_provider_setup(request, android_test_setup):
    """
    This fixture is for Android Jweb Doc Provider set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = android_test_setup
    fc = FlowContainer(driver)
    fc.fd["doc_provider_dev_settings"].open_select_settings_page()
    fc.fd["doc_provider_dev_settings"].select_stack(request.config.getoption("--stack"))
    return driver, fc

@pytest.fixture(scope="function", autouse=True)
def android_jweb_doc_provider_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_app_log_and_publish("JWEB_DOC_PROVIDER", driver, attachment_root_path, request.node.name)  
    request.addfinalizer(get_app_log)