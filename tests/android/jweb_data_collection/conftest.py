import pytest
import logging

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.jweb_data_collection.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def android_jweb_data_collection_setup(request, android_test_setup):
    """
    This fixture is for Android Jweb Data Collection set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = android_test_setup
    fc = FlowContainer(driver)
    fc.flow_load_home_screen()
    fc.fd["data_collection_service"].select_settings_button()
    fc.fd["data_collection_settings"].select_data_valve_and_ingress_stack_values(request.config.getoption("--stack"))
    fc.fd["data_collection_dev_settings"].open_select_settings_page()
    fc.fd["data_collection_dev_settings"].select_stack(request.config.getoption("--stack"))
    if request.config.getoption("--log-type") is not None:
        fc.fd["data_collection_dev_settings"].check_log_unloggables_toggle()
    return driver, fc

@pytest.fixture(scope="function", autouse=True)
def android_jweb_data_collection_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        if request.config.getoption("--log-type") is not None:
            attachment_root_path = c_misc.get_attachment_folder()
            c_misc.save_app_log_and_publish("JWEB_DATA_COLLECTION", driver, attachment_root_path, request.node.name)  
            try:
                driver.wdvr.execute_script('mobile: shell', {'command': 'rm', 'args': ["-r", TEST_DATA.JWEB_DATA_COLLECTION_APP_LOG_PATH],'includeStderr': True})
            except Exception as e:
                logging.error(e)
    request.addfinalizer(get_app_log)