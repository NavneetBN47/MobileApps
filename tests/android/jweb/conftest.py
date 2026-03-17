import pytest
import logging

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.jweb.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def android_jweb_setup(request, android_test_setup):
    """
    This fixture is for Android Jweb set up :
        - Get driver instance
        - Get FlowContainer instance
        - HPPS Installation Setup
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = android_test_setup
    fc = FlowContainer(driver)
    fc.fd["jweb_dev_settings"].open_select_settings_page()
    fc.fd["jweb_dev_settings"].select_stack(request.config.getoption("--stack"))
    if request.config.getoption("--log-type") is not None:
        fc.fd["jweb_dev_settings"].check_log_unloggables_toggle()
    return driver, fc    

@pytest.fixture(scope="function", autouse=True)
def android_jweb_reference_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_app_log_and_publish("JWEB", driver, attachment_root_path, request.node.name)  
        try:
            driver.wdvr.execute_script('mobile: shell', {'command': 'rm', 'args': ["-r", TEST_DATA.JWEB_APP_LOG_PATH],'includeStderr': True})
        except Exception as e:
            logging.error(e)
    request.addfinalizer(get_app_log)