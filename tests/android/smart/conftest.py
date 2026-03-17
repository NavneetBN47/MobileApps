import os
import pytest
import logging
import traceback
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.android.const import PACKAGE
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FlowContainer, FLOW_NAMES
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory


def pytest_addoption(parser):
    android_sf_argument_group = parser.getgroup('Android Smart SoftFax testing')
    android_sf_argument_group.addoption("--recipient-phone", action="store", default=None, help="custom recipient phone number")
    android_sf_argument_group.addoption("--output", action="store", default=None, help="custom .xls output file (under result folder) for performance sending fax")
    android_sf_argument_group.addoption("--recipient-code", action="store", default=None, help="custom recipient code")

@pytest.fixture(scope="session", autouse=True)
def set_testrail_info(request, android_smart_flow_setup):
    if not request.config.getoption("--testrail"):
        return
    driver = android_smart_flow_setup[0]  # get driver from android setup fixture to make sure apps are installed

    get_pkg_version = lambda pkg: driver.execute_script("mobile: shell", {"command": "dumpsys package {} | grep versionName".format(pkg)}).strip().split("=")[1]
    smart_version = get_pkg_version(PACKAGE.SMART(request.config.getoption("--app-build")))

    request.session.testrail["run_name"] = "Automated Smart Test Run for Android {}".format(driver.driver_info["platformVersion"])
    request.session.testrail["application_version"] = "HP Smart {}".format(smart_version)

    request.session.testrail["run_info"]["Platform"] = "Android {}".format(int(driver.driver_info["platformVersion"]))
    request.session.testrail["run_info"]["Stack"] = request.config.getoption("--stack")

    request.session.testrail["test_info"]["Device"] = " ".join([driver.driver_info["deviceManufacturer"].capitalize(), driver.driver_info["deviceModel"], driver.driver_info["deviceName"]])
    request.session.testrail["test_info"]["HPPS Version"] = get_pkg_version(PACKAGE.HPPS)

@pytest.fixture(scope="session")
def android_smart_flow_setup(request, android_test_setup):
    """
    This fixture is for Android HP Smart set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest HPPS app
    :param request:
    :param android_test_setup:
    :return:
    """
    try:
        driver = android_test_setup
        # add pkg_type as Smart app need test both debuggable and debug build
        driver.session_data["pkg_type"] = request.config.getoption("--app-type")
        fc = FlowContainer(driver)

        # Uninstall WPrintTestApp plugin to make sure no WPrintTestApp plugin on mobile device before run HP Smart testing
        driver.wdvr.remove_app(PACKAGE.WPRINT_TEST)
        driver.wdvr.remove_app(PACKAGE.HPPS)

        # Guard code for dismissing crash popup which affects to next lines of code
        android_system = android_system_flow_factory(driver)
        android_system.dismiss_app_crash_popup()

        # Change stack based on parameter
        # Loggable build doesn't have the debug activity
        if request.config.getoption("--app-type") != "loggable":
            fc.flow_home_change_stack_server(fc.stack)
            # Enable Log Unloggables
            fc.flow_home_enable_log_unloggables()

        # Make sure Google Chrome App load to Home screen
        # Avoid some tests in Android Smart loads Google Chrome apps
        fc.fd[FLOW_NAMES.GOOGLE_CHROME].open_google_chrome(timeout=5)

        def clean_up():
            # Make sure Google Chrome App load to Home screen
            # Avoid to affect to another project.
            fc.fd[FLOW_NAMES.GOOGLE_CHROME].open_google_chrome()

        request.addfinalizer(clean_up)
        return driver, fc
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_app_log_and_publish("SMART",driver, session_attachment, request.node.name)  
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/android_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "android_test_setup_failed_page_source.txt")
        traceback.print_exc()   
        raise     

@pytest.fixture(scope="class")
def android_smart_setup(android_smart_flow_setup):
    return android_smart_flow_setup

@pytest.fixture(scope='function', autouse=True)
def android_smart_cleanup_printer(request):
    """
    Clean up printer for each test case:
        - check core dump. If it exists, power cycle
    :param request:
    """
    try:
        p = request.cls.p
        p.check_init_coredump()
    except AttributeError:
        logging.warning("Class doesn't have printer object")

#------------------------------------------------------------------
#                               SOFTFAX
#------------------------------------------------------------------
@pytest.fixture(scope="session")
def get_softfax_output_file_path(request):
    """
    If output is not None, then output path is from "../results/<custom output from argument".
    Otherwise, output path is "../results/android/<device name>/performance/sending_fax_result.xls
    :param request:
    :return:
    """
    if request.config.getoption("--output"):
        path = os.path.join(ma_misc.get_abs_path("/results", False), request.config.getoption("--output"))
        if not os.path.isdir(path[:path.rfind("/")]):
            os.makedirs(path[:path.rfind("/")])
        return path
    else:
        return os.path.join(pytest.session_result_folder, "performance/sending_fax_result.xls")

@pytest.fixture(scope="class")
def softfax_class_cleanup(request):
    def clean_up_class():
        fc = request.cls.fc
        fc.flow_home_log_out_hpid_from_app_settings()
    request.addfinalizer(clean_up_class)

@pytest.fixture(scope="function", autouse=True)
def android_smart_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_app_log_and_publish("SMART", driver, attachment_root_path, request.node.name)  
        #Delete the folder for next test
        try:
            driver.wdvr.execute_script('mobile: shell', {'command': 'rm', 'args': ["-r", TEST_DATA.SMART_APP_LOG_PATH],'includeStderr': True})
        except Exception as e:
            logging.error(e)
    request.addfinalizer(get_app_log)
