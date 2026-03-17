import pytest
import logging

import MobileApps.libs.ma_misc.conftest_misc as c_misc

@pytest.fixture(scope="session", autouse=True)
def inos_setup(request, hpps_setup):
    """
    This fixture is for inOS Jweb set up:
        - Calls hpps_setup from /android/conftest.py
        - Get FlowContainer instance
    :param request:
    :param hpps_setup:
    :return: driver, fc from
    """
    return hpps_setup

# Customized parametrize based on the command line option
def pytest_generate_tests(metafunc):
    if "non_pdf_file_format" in metafunc.fixturenames:
        metafunc.parametrize("non_pdf_file_format", metafunc.config.getoption("hpps_document_type").split('+'))
    if "photo_file_format" in metafunc.fixturenames: 
        metafunc.parametrize("photo_file_format", metafunc.config.getoption("hpps_image_type").split('+'))

@pytest.fixture(scope="function", autouse=True)
def android_smart_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_app_log_and_publish("HPPS", driver, attachment_root_path, request.node.name)  
        #Delete the folder for next test
        try:
            driver.wdvr.execute_script('mobile: shell', {'command': 'rm', 'args': ["-r", TEST_DATA.APP_LOG_PATH],'includeStderr': True})
        except Exception:
            logging.error("Cannot delete log folder for some reason !!!!")
    request.addfinalizer(get_app_log)
