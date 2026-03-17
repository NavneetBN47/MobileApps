import pytest
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_suite_01_ios_smart_app_settings_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.fc.go_home(verify_ga=True)

    def test_01_app_settings_max_ga(self):
        self.fc.go_app_settings_screen_from_home()
        self.app_settings.sign_in_and_verify_hpc_account()
        self.app_settings.send_feedback_from_app_settings()
        self.app_settings.contact_fb_messenger_from_feedback()
        self.app_settings.contact_fb_messenger_from_app_settings()
        self.app_settings.app_settings_ga()
        self.app_settings.sign_out_from_hpc()

    def test_02_app_settings_coverage_flow1_ga(self):
        self.fc.go_app_settings_screen_from_home()