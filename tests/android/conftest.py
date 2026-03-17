import os
import pytest
import logging
import traceback

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.morelangs.morelangs import MoreLangs
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory
from MobileApps.resources.const.android import const
from MobileApps.libs.ma_misc.conftest_misc import get_package_url
from MobileApps.libs.flows.android.hpps.flow_container import Flow_Container

pytest.platform = "ANDROID"

def pytest_addoption(parser):
    android_argument_group = parser.getgroup('Android Test Parameters')
    android_argument_group.addoption("--app-type", action="store", default="debug", help="The type of app you would like to run")
    android_argument_group.addoption("--app-build", action="store", default=None, help="The build number of the app you would like to run")
    android_argument_group.addoption("--app-version", action="store", default=None, help="The app version you would like to run")
    android_argument_group.addoption("--app-release", action = "store", default="daily", help="Which app relese to use daily or stable")

    # For changing wifi during test setup
    android_argument_group.addoption("--change-wifi", action="store_true", help="change wifi to system configured wifi during test setup(from system_config.json)")
    android_argument_group.addoption("--skip-reinstall", action="store_true", help="Skip reinstalling app, this will set noReset to true and fullReset to false")

    hpps_argument_group = parser.getgroup('HPPS Test Parameters')
    hpps_argument_group.addoption("--hpps-app-type", action = "store", default="debug", help="Which hpps build to use")
    hpps_argument_group.addoption("--hpps-app-release", action = "store", default="daily", help="Which hpps release to use")
    hpps_argument_group.addoption("--hpps-app-version", action="store", default=None, help="The app version you would like to run")
    hpps_argument_group.addoption("--hpps-app-build", action="store", default=None, help="The build number of the app you would like to run")

    hpps_argument_group.addoption("--hpps-protocol", action = "store", default="Default", help="hpps protocol parameter")
    hpps_argument_group.addoption("--hpps-copies", action = "store", default="Default", help="hpps copies parameter")
    hpps_argument_group.addoption("--hpps-color", action = "store", default="Default", help="hpps color parameter")
    #Not added in jenkins
    hpps_argument_group.addoption("--hpps-paper-size", action = "store", default="Default", help="hpps pclm compress parameter")
    hpps_argument_group.addoption("--hpps-orientation", action = "store", default="Default", help="hpps orientation parameter")
    hpps_argument_group.addoption("--hpps-two-sided", action = "store", default="Default", help="hpps two sided parameter")
    hpps_argument_group.addoption("--hpps-quality", action = "store", default="Default", help="hpps quality parameter")
    hpps_argument_group.addoption("--hpps-scaling", action = "store", default="Default", help="hpps scaling parameter")
    #Not added in jenkins
    hpps_argument_group.addoption("--hpps-file-size", action = "store", default="Default", help="hpps file size parameter")
    hpps_argument_group.addoption("--hpps-borderless", action = "store", default="Default", help="hpps borderless parameter")
    hpps_argument_group.addoption("--hpps-PCLm-compress", action = "store", default="Default", help="hpps pclm compress parameter")
    # For generating specific test cases
    hpps_argument_group.addoption("--hpps-document-type", action = "store", default="Random", help="hpps non-pdf file format parameter")
    hpps_argument_group.addoption("--hpps-image-type", action = "store", default="Random", help="hpps image file format parameter")

# ----------------      FUNCTION     ---------------------------

@pytest.fixture(scope="session")
def android_test_setup(request, session_setup, require_driver_session):
    """
    Test general precondition for Android test
        + Create log file which store log of test script
        + Updating list when adding new precondition into this fixture
        + Change language
        + Change wifi to default wifi
        + Install and get string table of latest HPPS for Android SMART
    Test general post test for Android test:
        + Delete all Gmail from inbox
        + Updating list when adding new precondition into this fixture
    :param request:
    """
    try:
        system_config = ma_misc.load_system_config_file()
        driver = require_driver_session
        driver.press_key_home()

        # Change wifi
        if request.config.getoption("--change-wifi"):
            ssid = request.config.getoption("--wifi-ssid") if request.config.getoption("--wifi-ssid") else system_config["default_wifi"]["ssid"]
            passwd = request.config.getoption("--wifi-pass") if request.config.getoption("--wifi-pass") else system_config["default_wifi"]["passwd"]
            android_system = android_system_flow_factory(driver)
            android_system.change_wifi(ssid, passwd, connect_timeout=60)
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment, exist_ok=True)
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/android_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "android_test_setup_failed_page_source.txt")
        traceback.print_exc()
        raise
        #This doesn't give any reporting
        #pytest.exit("ANDROID TEST SETUP FAILED")
    return driver

@pytest.fixture(scope="function")
def android_cleanup_popup(request):
    """
    Clean up all following popup before and after executing each test:
        - App crash
    """
    driver = request.cls.driver

    # Dismiss popups at setup
    android_system = android_system_flow_factory(driver, skip_close=True)
    android_system.dismiss_app_crash_popup()

@pytest.fixture(scope="session")
def hpps_setup(request, android_test_setup, require_driver_session):
    try:
        driver = require_driver_session
        driver.session_data["test_params"] = request.config.option
        driver.clear_app_cache("com.android.printspooler")

        hpps_build = request.config.getoption("--hpps-app-build")
        hpps_release = request.config.getoption("--hpps-app-release")
        package_info = get_package_url(request, _os="ANDROID", project="HPPS", app_type=hpps_build, app_release= hpps_release)
        driver.install_app(package_info[0], "HPPS", const.PACKAGE.HPPS, uninstall=True)
        driver.load_app_strings("hpps", driver.pull_package_from_device("com.android.printspooler"), driver.session_data["language"], append=True, add_array=True) 
        fc = Flow_Container(driver)
        driver.terminate_app(const.PACKAGE.SETTINGS)        
        fc.turn_on_hpps()
        fc.set_protocol()
        fc.flow["android_system"].clear_notifications()
    except:
        logging.error("HPPS_SETUP FAILED!")
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_app_log_and_publish("SMART",driver, session_attachment, request.node.name)  
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/hpps_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "hpps_setup_failed_page_source.txt")
        traceback.print_exc()
        raise
        #This doesn't give any reporting
        #pytest.exit("HPPS_SETUP FAILED!")

    return driver, fc