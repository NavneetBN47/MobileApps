import time
import pytest
from MobileApps.resources.const.android.const import PACKAGE, WEBVIEW_CONTEXT, LAUNCH_ACTIVITY

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_01_HPID_Android(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define variables
        cls.home = cls.fc.fd["home"]
        cls.cec = cls.fc.fd["custom_engagement_center"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.serial_number, cls.model_str =cap.split("_", 1) if (cap:= cls.driver.wdvr.capabilities.get("applicationName", False)) else cls.driver.wdvr.capabilities["desired"]["deviceName"].split("_", 1)

        record_testsuite_property("suite_test_category", "HPID")
        record_testsuite_property("suite_test_app_info", cls.driver.session_data["app_info"][pytest.app_info])
        record_testsuite_property("suite_test_serial_number", cls.serial_number)
        record_testsuite_property("suite_test_model_string", cls.model_str)
        cls.pkg_name = cls.fc.pkg_name
        cls.smart_context = cls.fc.smart_context  
        
    def test_01_hpid_sign_in(self):
        self.fc.flow_load_home_screen(home_nav_timeout=3, skip_hpid_popup=True, accept_all_change_check=False)
        time.sleep(2)
        self.driver.wait_for_context(self.smart_context, timeout=30)
        self.cec.verify_see_all_btn()
        #self.fc.fd["custom_engagement_center"].verify_never_run_out_save_tile()
        self.driver.performance.time_stamp("t12")
        self.driver.terminate_app(self.pkg_name)
        self.driver.performance.time_stamp("t13")
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.performance.time_stamp("t14")
        self.home.verify_nav_logo()
        self.driver.performance.time_stamp("t15")
        self.cec.verify_see_all_btn()
        self.driver.performance.time_stamp("t16")

    def test_02_hpid_sign_out(self):
        self.fc.flow_load_home_screen(verify_signin=False)
        self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN)
        self.app_settings.sign_out_hpc_acc()

    def test_03_hpid_sign_up(self):
        self.fc.reset_app()
        self.fc.flow_load_home_screen(create_acc=True, home_nav_timeout=3, skip_hpid_popup=True, accept_all_change_check=False)