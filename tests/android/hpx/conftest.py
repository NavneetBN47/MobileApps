import pytest
import traceback
import os
from MobileApps.libs.flows.android.hpx.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc

@pytest.fixture(scope="session")
def android_hpx_setup(request, android_test_setup):
    """
    This fixture is for Android HPX set up :
        - Get driver & FlowContainer instance
        - Need to Update here for future HPX setup
    """
    try:
        driver = android_test_setup
        driver.session_data["pkg_type"] = request.config.getoption("--app-type")
        fc = FlowContainer(driver)
        
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment, exist_ok=True)
        c_misc.save_app_log_and_publish("SMART",driver, session_attachment, request.node.name)  
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/android_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "android_test_setup_failed_page_source.txt")
        traceback.print_exc()  

    return driver, fc

# kept a class level fixture for future use
# @pytest.fixture(scope="class")
# def android_hpx_flow_setup(android_hpx_setup):
#     return android_hpx_setup

@pytest.fixture(scope="function")
def function_setup_terminate_relaunch_hpx(request):
    """
    Function setup to terminate and relaunch HPX app before each test function.
    """
    request.cls.driver.press_key_home()
    request.cls.fc.terminate_and_relaunch_hpx()
