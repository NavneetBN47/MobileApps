import pytest
import logging

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.jweb_value_store.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def android_jweb_value_store_setup(request, android_test_setup):
    """
    This fixture is for Android Jweb Value Store set up:
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = android_test_setup
    fc = FlowContainer(driver)
    fc.fd["value_store_dev_settings"].open_select_settings_page()
    fc.fd["value_store_dev_settings"].select_stack(request.config.getoption("--stack"))
    if request.config.getoption("--log-type") is not None:
        fc.fd["value_store_dev_settings"].check_log_unloggables_toggle()
    return driver, fc

@pytest.fixture(scope="function", autouse=True)
def android_jweb_value_store_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_app_log_and_publish("JWEB_VALUE_STORE", driver, attachment_root_path, request.node.name)  
        try:
            driver.wdvr.execute_script('mobile: shell', {'command': 'rm', 'args': ["-r", TEST_DATA.JWEB_VALUE_STORE_APP_LOG_PATH],'includeStderr': True})
        except Exception as e:
            logging.error(e)
    request.addfinalizer(get_app_log)