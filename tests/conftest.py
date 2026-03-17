import os
import sys
import uuid
import json
import base64
import shutil
import pytest
import traceback
import logging
import logging.config

from time import sleep
from SAF.misc import saf_misc
from collections import OrderedDict
from SPL.driver import driver_factory
from datetime import datetime, timedelta
from SPL.printer_misc import printer_misc

from MobileApps.libs.ma_misc import ma_misc

from SPL.driver.reg_printer import PrinterNotReady
import MobileApps.libs.ma_misc.conftest_misc as c_misc
import MobileApps.resources.const.ios.const as i_const
from MobileApps.libs.ma_misc.conftest_exceptions import *
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.testrail.testrail_misc import TestRailMisc
from MobileApps.libs.flows.android.android_flow import android_system_ui_flow
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory
from MobileApps.libs.one_simulator.printer_simulation import create_simulator_printer_from_api
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer
from MobileApps.libs.ma_misc.live_printer import LivePrinter

if (sys.version_info < (3, 0)):
     # Python 2 code in this block
    str = unicode

def pytest_addoption(parser):
    test_option = parser.getgroup("Test Parameters")
    test_option.addoption("--executor-url", action="store", default=False, help="Overload executor-url in system_config.json")
    test_option.addoption("--executor-port", action="store", default=False, help="Overload executor-port in system_config.json")
    test_option.addoption("--locale", action="store", default="en", help="Locale of the test")
    test_option.addoption("--stack", action="store", default="pie", help="Which stack to run the test on")
    test_option.addoption("--mobile-device", action="store", help="Which phone to test")
    test_option.addoption("--platform-version", action="store", help="Test on a specific platform version")
    test_option.addoption("--printer-model", action="store", default=None, help="Which printer model to test with")   
    test_option.addoption("--printer-serial", action="store", default=None, help="Printer Serial Number (FOR DEBUGGING ONLY DO NOT USE FOR PRODUCTION CODE)")   
    test_option.addoption("--analytics", action="store_true", default=False, help="Enable the analytics module in SAF")
    test_option.addoption("--log-type", action="store", default=None, help="log type [debug/info/None] which will be displayed in log file")
    test_option.addoption("--wifi-ssid", action="store", default=None, help="The ssid used by the test")
    test_option.addoption("--wifi-pass", action="store", default=None, help="The password for the default ssid")
    test_option.addoption("--skip-power-cycle-printer", action="store_true", default=False, help="Whether to powercycle or not")
    test_option.addoption("--printer-mech", action="store_true", default=False, help="Set printer mech mode")
    test_option.addoption("--capture-video", action="store_true", default=False, help="Enable video capture")
    test_option.addoption("--context-manager", action="store", default=False, help="Options[False: disabled, 'gather': gather the ss, 'verify': validate screenshots against golden]")
    test_option.addoption("--ss-sequence", action="store_true", default=False, help="Adding a number sequence to the screenshot that is gathered by the context manager")
    test_option.addoption("--imagebank-path", action="store", default=None, help="Root path of image bank, should use system config as default")
    test_option.addoption("--email-verification", action="store_true", default=False, help="To toggle on/off email verification, default is off")
    test_option.addoption("--performance", action="store_true", default=False, help="To toggle on/off performance testing")
    test_option.addoption("--testrail", action="store_true", default=False, help="To enable uploading test results to testrail.")
    test_option.addoption("--tr-name", action="store", default=None, help="Overrides the auto-generated name for TestRail test runs.")
    test_option.addoption("--tr-close", action="store_true", default=False, help="Close test rail runs that are opened.")
    test_option.addoption("--printer-hostname", action="store", default=None, help="The Dune printer's hostname")
    test_option.addoption("--printer-ip", action="store", default=None, help="Live printer IP address")
    test_option.addoption("--local-build", action="store", help="DEBUG PURPOSE ONLY pass in a file path to something local or an url")
    test_option.addoption("--appbundle-install", action="store_true", default=None, help="Install appbundle to test")
    test_option.addoption("--user", action="store", default=None, help="Overload default exec user")
    test_option.addoption("--portal-env", action="store", default=None, help="Which portal hpx support point to")
    test_option.addoption("--printer-profile", action="store", default=None, help="Printer Profile to use for the test")
    test_option.addoption("--tr-milestone", action="store", default=None, help="Test milestone for testrail auto update")
    test_option.addoption("--browser-size", action="store", default=None, help="Screen size for web tests (desktop, mobile, tablet)")
    test_option.addoption("--onesim-server-ip", action="store", default=None, help="IP address of the OneSim server for LEDM/CDM simulations")

def pytest_sessionstart(session):
    session.results = dict()
    session.testrail = { 
        "run_name": None,  # the name to give to the testrail run(s). Required for posting testrail results
        "application_version": None,  # version string of the application that is being tested.
        "run_info": OrderedDict(),  # stores additional info to be included in testrail run description. Optional
        "test_info": OrderedDict()  # stores additional info to be included in testrail test comments. Optional
    }

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        item.session.results[item] =  rep
    return

# ------------------------      SESSION SCOPE       ---------------------------------

@pytest.fixture(scope="session")
def require_driver_session(request, record_testsuite_property):

    #Fixture only for driver instantiation.
    #NOTHING ELSE GOES IN HERE
    try:
        os = pytest.platform
        driver = c_misc.create_driver(request, os)
        record_testsuite_property("suite_test_platform_version", driver.platform_version)
    except:
        traceback.print_exc()
        raise
        #This doesn't give any reporting
        #pytest.exit("REQUIRE_DRIVER_SESSION FAILED")        
    return driver

@pytest.fixture(scope="session")
def require_web_session(request):
    try:
        driver = c_misc.create_web_driver(request)
    except:
        traceback.print_exc()
        raise
    return driver

@pytest.fixture(scope="session")
def load_hpx_printers_session(request):
    system_cfg = ma_misc.load_system_config_file()
    pp_info = system_cfg["printer_power_config"]
    file = printer_misc.get_hpx_printer(pp_info["instance"], debug=False)
    printer_serial = file.split("_")[-1].split(".")[0]
    return file
    request.addfinalizer(printer_misc.release_hpx_printer(printer_serial, debug=False))

@pytest.fixture(scope="session")
def load_printers_session(request):
    """
     Load printer object.
        - Power cycle printer for new execution of test if type is pdu
        - Check whether printer is ready for testing
        - Connect printer to target network (from argument or in system_config.json - default value)
    Note: in config/system_config.json, comment out the "printer_power_config" that are not used.
                                        pcs_url should be "pcs://<ip>:<port>"
    :param request:
     :return:
    """
    system_cfg = ma_misc.load_system_config_file()
    p = None
    if "printer_power_config" in system_cfg:
        pp_info = system_cfg["printer_power_config"]
        db_info = system_cfg.get("database_info", None)
        if db_info is None and pp_info["type"] != "manual":
            raise PDUPrinterError("You need the section 'database_info' in the system_cfg file for a PDU power setup")
        p = driver_factory.get_printer(pp_info,
                                        printer_serial=request.config.getoption("--printer-serial"),
                                        printer_hostname = request.config.getoption("--printer-hostname"),
                                        product_name=request.config.getoption("--printer-model"),
                                        printer_feature=getattr(pytest, "printer_feature", {}),
                                        db_info = db_info,
                                        mech=request.config.getoption("--printer-mech"),
                                        power_cycle_printer= not request.config.getoption("--skip-power-cycle-printer"))
                                       
        if not p.is_printer_status_ready(timeout=120):
            raise PrinterNotReady("Printer with serial: " + str(p.get_printer_information()["serial number"]) + " have status: " + str(p.get_printer_status()))
        p_info = p.get_printer_information()
 
        ssid, passwd = c_misc.get_wifi_info(request, raise_e=False)
        if ssid is None or passwd is None:
            logging.info("Wifi info was not provided skipping putting the printer on the wifi network")
            # return p
        else:
            if not p.connect_to_wifi(ssid, passwd):
                raise PrinterNotReady("Print with Serial #: " + str(p_info["serial number"]) +  " cannot connect to wifi: " + ssid + " password: " + passwd)
            # Print printer information
            logging.info("Printer Information:\n {}".format(p_info))
            # return p
    elif "oneSimulator" in system_cfg:
        pp_info = system_cfg["oneSimulator"]
        oneSimulatorServer = pp_info.get("server_ip")
        if  request.config.getoption('--printer-profile') is None:
            logging.info(f"Using profile: {pp_info.get('printer-profile')}")
            printer_profile = pp_info.get("printer-profile")
        else:
            logging.info(f"Using printer_profile: {request.config.getoption('--printer-profile')}")
            printer_profile = request.config.getoption("--printer-profile")

        if request.config.getoption('--onesim-server-ip') is not None:
            logging.info(f"Using oneSimulator server ip from command line: {request.config.getoption('--onesim-server-ip')}")
            oneSimulatorServer = str(request.config.getoption('--onesim-server-ip'))

        # if pp_info["type"] == "server":
        #     # Send a REST API call to the simulator server to get printer information
        #     oneSimulatorServer = pp_info.get("server_ip")
        #     modelName = pp_info.get("profile")
        #     isUSB = pp_info.get("isUSB", False)
           
        #     p = create_simulator_printer_from_api(oneSimulatorServer, modelName, isUSB)
        if pp_info["type"] == "server":
            # Send a REST API call to the simulator server to get printer information
            isUSB = pp_info.get("isUSB", False)
            p = create_simulator_printer_from_api(oneSimulatorServer, printer_profile, isUSB)
            # return p
            
    elif "livePrinter" in system_cfg:
        pp_info = system_cfg["livePrinter"]
        # Create a live/manual printer object using CLI overrides first, then config defaults
        p = LivePrinter.create_printer_object(
            ip_address=request.config.getoption("--printer-ip") or request.config.getoption("--printer-hostname") or pp_info.get("printer_ip"),
            product_name=request.config.getoption("--printer-model") or pp_info.get("printer_name"),
        )
        p_info = p.get_printer_information()
        logging.info("Printer Information:\n {}".format(p_info))

    def clean_up():
        try:
            if p is not None:
                if "oneSimulator" in system_cfg:
                    printer_ip = p.get_printer_information().get("ip address")
                    printer_serial_number = p.get_printer_information().get("serial number")
                    delete_simulator_printer(printer_ip, printer_serial_number)
                else:
                    p.close()
        except:
            logging.info("Printer object either doesn't exist or cannot be cleaned up")
            
    request.addfinalizer(clean_up)

    return p      
    
@pytest.fixture(scope="session")
def load_printer_session_without_manager(request):
    """
    This is only for Portal OOBE onboarding.
    This bypasses printer allocation
    """
    system_cfg = ma_misc.load_system_config_file()
    pp_info = pp_info = system_cfg["printer_power_config"]
    db_info = system_cfg.get("database_info", None)
    connection_string = 'dune://' + request.config.getoption("--printer-hostname") + '/' + request.config.getoption("--printer-serial")
    p = driver_factory.printer_driver_factory(connection_string, pp_info, db_info)
                                    
    if not p.is_printer_status_ready(timeout=120):
        raise PrinterNotReady("Printer with serial: " + str(p.get_printer_information()["serial number"]) + " have status: " + str(p.get_printer_status()))
    p_info = p.get_printer_information(max_attempts=5)
    p.get_printer_uuid()
    logging.info("Printer Information:\n {}".format(p_info))
    return p


@pytest.fixture(scope="session")
def prep_results_folder(request):
    if not os.path.isdir(ma_misc.get_abs_path("/results")):
        os.mkdir(ma_misc.get_abs_path("/results"))   
    return True

@pytest.fixture(scope="session")
def session_setup(request, prep_results_folder, require_driver_session):
    driver = require_driver_session
    pytest.session_result_folder = c_misc.get_session_result_folder_path(driver)
    ma_misc.delete_content_of_folder(pytest.session_result_folder)
    logging.info("Session Results Folder: " + pytest.session_result_folder)
    return driver

@pytest.fixture(scope="session")
def web_session_setup(request, prep_results_folder, require_web_session):
    driver = require_web_session
    pytest.session_result_folder = c_misc.get_web_session_result_folder_path(request)
    ma_misc.delete_content_of_folder(pytest.session_result_folder+".." , time_delta=timedelta(days=7), everything=False, recreate=False)
    ma_misc.create_dir(pytest.session_result_folder)
    return driver

@pytest.fixture(scope="class")
def load_hpid_credentials(request, require_driver_session):
    driver = require_driver_session
    ma_misc.get_hpid_account_info(request.config.getoption("--stack"), "ucde", claimable=False, instant_ink=True, driver=driver)

@pytest.fixture(scope="session", autouse=True)
def log_results_to_testrail(request):
    yield
    if not request.config.getoption("--testrail"):
        return
    run_name = request.session.testrail["run_name"]
    if override_run_name := request.config.getoption("--tr-name"):
        run_name = override_run_name
    try:
        run_milestone = request.config.getoption("--tr-milestone")
    except:
        run_milestone = None
    assert isinstance(run_name, str) and len(run_name) > 0, "Requires a name for the TestRail run"
    run_info = request.session.testrail["run_info"]
    test_info = request.session.testrail["test_info"]
    version = request.session.testrail["application_version"]
    tr_misc = TestRailMisc()
    tr_misc.push_results_to_testrail(run_name, request.session.results, run_milestone=run_milestone, version=version, run_info=run_info if len(run_info) > 0 else None, test_info=test_info if len(test_info) > 0 else None, close_run=request.config.getoption("--tr-close"))
    return

# ------------------------ Class Scope --------------------------- #

@pytest.fixture(scope="class", autouse=True)
def global_class_setup(request):
    pytest.test_result_folder = test_result_folder = c_misc.get_test_result_folder_path(pytest.session_result_folder, request.cls.__name__)
    config_logging(request, test_result_folder)
    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

#Auto use not enabled right now, still need to do more testing here
@pytest.fixture(scope="class")
def class_setup_clean_up(request):
    yield

    def clean_up():
        if request.session.testsfailed > 0 and not request.session.results:
            clean_up_utility_method(request)

    request.addfinalizer(clean_up)
    return True


# ------------------------      FUNCTION SCOPE      ---------------------------------
@pytest.fixture(scope="function", autouse=True)
def test_case_clean_up(request):

    def clean_up():
        if hasattr(request.node, "rep_call"):
            #This attribute only shows up when setup finishes
            failed = request.node.rep_call.failed
        elif hasattr(request.node, "rep_setup"):
            #This attribute is needed when a function setup fails
            failed = request.node.rep_setup.failed
        if failed:
            clean_up_utility_method(request)

    request.addfinalizer(clean_up)
    return True

@pytest.fixture(scope="class", autouse=True)
def save_cms_results(request):
    def save_results():
        driver = request.cls.driver
        if driver.session_data["context_manager_mode"] == "verify":
            attachment_root_path = c_misc.get_attachment_folder()
            c_misc.save_cms_results_and_publish(driver, attachment_root_path, "cms_results")
            c_misc.save_cms_failed_images_and_publish(driver, attachment_root_path, "cms_failed_img")
    request.addfinalizer(save_results)

@pytest.fixture(scope="function", autouse=True)
def capture_video(request):
    attachment_root_path = c_misc.get_attachment_folder()
    if request.config.getoption("--capture-video"):
        if pytest.platform == "MAC":
            request.cls.driver.wdvr.start_recording_screen(deviceId=0, timeLimit=600)
        else:
            request.cls.driver.wdvr.start_recording_screen(videoType="mpeg4", timeLimit=600)
        logging.debug("Started video record")
        def stop_video():
            if request._parent_request.scope == "session":
                file_name = request._parent_request.fixturename
            elif request._parent_request.scope == "function":
                file_name = request.node.name
            c_misc.save_video_and_publish(request.cls.driver, attachment_root_path, file_name)
            logging.debug("Stopped video record")
        request.addfinalizer(stop_video)

@pytest.fixture(scope="function", autouse=True)
def inject_test_case_name_to_performance(request):
    if request.config.getoption("--performance"):
        request.cls.driver.performance.set_cur_test_case_name(request.node.name)

@pytest.fixture(scope="session", autouse=True)
def inject_data_to_junit(request, record_testsuite_property):
    record_testsuite_property("suite_test_stack", request.config.getoption("--stack"))
    record_testsuite_property("performance", request.config.getoption("--performance"))
    record_testsuite_property("suite_test_platform", pytest.platform)
    record_testsuite_property("suite_test_client", getattr(pytest, "app_info", None))

# ---------------------- Utility --------------------#
def config_logging(request, test_result_folder):
    if test_result_folder[-1] != "/":
        test_result_folder += "/"
    log_path = test_result_folder + "log/logging.log"

    if not os.path.isdir("/".join(log_path.split("/")[:-1])):
        os.makedirs("/".join(log_path.split("/")[:-1]))

    ma_misc.create_file(log_path)
    logging.config.fileConfig(ma_misc.get_abs_path("/config/logging.cfg"),
                              defaults={"log_file_name": log_path})
    log_types = {"debug": logging.DEBUG, "info": logging.INFO}
    log_type = request.config.getoption("--log-type")
    logging.getLogger().setLevel(log_types[log_type] if log_type else logging.NOTSET)

def clean_up_utility_method(request):
    driver = request.cls.driver
    attachment_root_path = c_misc.get_attachment_folder()

    logging.error("Test failed. Cleaning up...")
    sleep(1)
    try:
        p = request.cls.p
    except AttributeError:
        logging.warning("Cannot find printer object in class")
    else:
        logging.debug("Printer object found in class take printer front panel image")
        try:
            c_misc.save_printer_fp_and_publish(p, attachment_root_path + "/" + p.get_printer_information()[
                "serial number"] + "_front_panel" + ".png")
        except:
            logging.warning("Printer front panel capture failed!")

    if pytest.platform.lower() == "web":
        driver.wdvr.switch_to.default_content()

    if driver.driver_class == "selenium":
        for window, _ in driver.session_data["window_table"].items():
            driver.switch_window(window)
            logging.debug("Window: " + str(window) + " URL: " + driver.current_url)
            c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source_{}.txt".format(window))
            c_misc.save_screenshot_and_publish(driver,
                                        "{}/screenshot_{}_{}.png".format(attachment_root_path, request.node.name, window))
        if request.config.getoption("--har"):
            c_misc.save_har_and_publish(driver, attachment_root_path, request.node.name + ".har")  
    else:
        try:
            c_misc.save_source_and_publish(driver, attachment_root_path)
            c_misc.save_screenshot_and_publish(driver,
                                        "{}/screenshot_{}.png".format(attachment_root_path, request.node.name))
        except WebDriverException:
            if driver.context != "NATIVE_APP":
                logging.info("Webview teardown capture failed, switching to native")
                driver.switch_to_webview(webview_name="NATIVE_APP")
                c_misc.save_source_and_publish(driver, attachment_root_path)
                c_misc.save_screenshot_and_publish(driver,
                                        "{}/screenshot_{}.png".format(attachment_root_path, request.node.name))                        

    if pytest.platform.lower() in ["android", "ios"]:
        driver.switch_to_webview(webview_name="NATIVE_APP")
        c_misc.save_log_and_publish(driver, attachment_root_path, request.node.name)

        # Dismiss app crash popup for android platform. It is in this fixture because it is following capturing screen-shot
        if pytest.platform.lower() == "android":
            c_misc.save_mem_stat_and_publish(driver, attachment_root_path)
            android_system = android_system_flow_factory(driver)
            android_system.dismiss_app_crash_popup()
            
    if pytest.platform.lower() in ["windows"]:
        #TODO need to finish the log capturing module
        if pytest.app_info == "DESKTOP":
            pytest.default_info = pytest.set_info
        else:
            pytest.default_info = pytest.app_info
        c_misc.save_windows_app_log_and_publish(pytest.default_info, driver, attachment_root_path, request.node.name)

    return True