import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_System_Control(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)

    def test_01_verify_system_control_analytics_C33694795(self):
        #Open HP privacy settings in app,Click yes to all,Navigate to Programmable key page,Perform some actions in Programmable key
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        time.sleep(5)
        state = self.fc.fd["settings"].click_click_here_link()
        self.fc.fd["settings"].click_yes_to_all()
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        self.fc.fd["devices"].click_prog_key_card()
        self.fc.fd["hppk"].click_supportkey_icon()
        self.fc.fd["hppk"].click_save_button()
        time.sleep(4)
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_progkey-core")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"] == "Navigation","EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged","EventName field name did not generate"
        assert event["11"] == "pcdevice-core","ScreenName field name  did not generate"
        assert event["12"] == "AUID_PCDevicePage_FeatureCard_progkey-core","AUID Field did not generate"