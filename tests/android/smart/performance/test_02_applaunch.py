import time
import pytest
from MobileApps.resources.const.android.const import LAUNCH_ACTIVITY

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_01_App_Launch_Android(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # Define variables
        cls.home = cls.fc.fd["home"]
        cls.serial_number, cls.model_str = cap.split("_", 1) if (
            cap := cls.driver.wdvr.capabilities.get("applicationName", False)) else \
            cls.driver.wdvr.capabilities["desired"]["deviceName"].split("_", 1)
        record_testsuite_property("suite_test_category", "HPID")
        record_testsuite_property("suite_test_app_info", cls.driver.session_data["app_info"][pytest.app_info])
        record_testsuite_property("suite_test_serial_number", cls.serial_number)
        record_testsuite_property("suite_test_model_string", cls.model_str)
        cls.pkg_name = cls.fc.pkg_name
        cls.smart_context = cls.fc.smart_context

    def test_01_app_launch_android(self):
        self.fc.flow_load_home_screen(skip_value_prop=True, accept_all_change_check=False)
        self.driver.terminate_app(self.pkg_name)
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.performance.time_stamp("t22")
        self.home.verify_home_nav()
        self.driver.performance.time_stamp("t-warmlaunch")
