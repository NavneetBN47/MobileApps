import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_01_HPID_IOS(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.cec_home = cls.fc.fd["cec_home"]
        cls.stack = request.config.getoption("--stack")
        cls.serial_number = cap if (cap:= cls.driver.wdvr.capabilities.get("applicationName", False)) else cls.driver.wdvr.capabilities["deviceName"]

        cls.username = ma_misc.get_hpid_account_info(cls.stack, a_type="ucde")['email']
        cls.password = ma_misc.get_hpid_account_info(cls.stack, a_type="ucde")['password']

        record_testsuite_property("suite_test_category", "HPID")
        record_testsuite_property("suite_test_app_info", cls.driver.session_data["app_info"][pytest.app_info])
        record_testsuite_property("suite_test_serial_number", cls.serial_number)

    def test_01_hpid_sign_in(self):
        self.fc.go_home(stack=self.stack, username=self.username, password=self.password)
        self.driver.performance.time_stamp("t11")
        self.driver.wait_for_context(WEBVIEW_URL.CEC, timeout=30)
        self.cec_home.verify_see_all_btn()
        self.driver.performance.time_stamp("t12")
        self.driver.terminate_app(BUNDLE_ID.SMART)
        self.driver.performance.time_stamp("t13")
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.driver.performance.time_stamp("t14")
        self.home.verify_hp_smart_nav_bar()
        self.driver.performance.time_stamp("t15")
        self.cec_home.verify_see_all_btn()
        self.driver.performance.time_stamp("t16")

    def test_02_hpid_sign_out(self):
        self.home.select_app_settings()
        self.app_settings.sign_out_from_hpc()

    def test_03_hpid_sign_up(self):
        self.fc.go_home(stack=self.stack, reset=True, create_account=True)