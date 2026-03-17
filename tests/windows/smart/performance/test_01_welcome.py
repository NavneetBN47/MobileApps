import pytest
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_01_Welcome_Performance(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, record_testsuite_property, load_hpid_credentials):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.serial_number = cap if (cap:= cls.driver.wdvr.capabilities.get("applicationName", False)) else cls.driver.wdvr.capabilities["deviceName"]

        cls.home = cls.fc.fd["home"]
        cls.username, cls.password = cls.driver.session_data["hpid_user"], cls.driver.session_data["hpid_pass"]
        record_testsuite_property("suite_test_category", "HPID")
        record_testsuite_property("suite_test_app_info", cls.driver.session_data["app_info"][pytest.app_info])
        record_testsuite_property("suite_test_serial_number", cls.serial_number)

    def test_01_verify_welcome_flow_with_hpid(self):
        """
        Verify the app is installed and launched successfully
        For capture hpid login performance
        """
        self.driver.terminate_app()
        self.driver.performance.time_stamp("t0")
        self.driver.launch_app()
        self.fc.fd["gotham_utility"].click_maximize()   
        self.fc.go_home(username=self.username, password=self.password, skip_choose_printer_dialog=False)
        self.driver.performance.time_stamp("t11")
        self.home.verify_cec_banner()
        self.driver.performance.time_stamp("t12")
        self.driver.terminate_app()
        self.driver.performance.time_stamp("t13")
        sleep(2)
        self.driver.launch_app()
        self.driver.performance.time_stamp("t14")
        self.home.verify_home_screen(raise_e=True)
        self.driver.performance.time_stamp("t15")
        self.home.verify_cec_banner()
        self.driver.performance.time_stamp("t16")