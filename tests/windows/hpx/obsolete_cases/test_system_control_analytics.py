import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_System_Control_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)

    @pytest.mark.require_platform(["willie"])
    def test_01_verify_system_control_analytics_on_consumer_C33694795(self):
        #Open HP privacy settings in app,Click yes to all,Navigate to Programmable key page,Perform some actions in Programmable key
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        time.sleep(5)
        self.fc.fd["settings"].click_privacy_tab()
        time.sleep(1)
        self.fc.fd["settings"].click_click_here_link()
        self.fc.fd["settings"].click_yes_to_all()
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        #verify system control card
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True, "System control card not available."
        self.fc.fd["devices"].click_system_control_card()
        #click smart sense and verify it's AUID analytics call
        self.fc.fd["system_control"].click_smart_sense_consumer()
        time.sleep(4)
        event = self.fc.capture_analytics_event("AUID_PCSystemControl_thermalOption_consumer_5")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"] == "Navigation","EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged","EventName field name did not generate"
        assert event["11"] == "pcsystemcontrol-core","ScreenName field name  did not generate"
        assert event["12"] == "AUID_PCSystemControl_thermalOption_consumer_5"
        
        #click on Balanced mode and verify it's AUID analytics call
        self.fc.fd["system_control"].click_balanced_consumer()
        time.sleep(4)
        event = self.fc.capture_analytics_event("AUID_PCSystemControl_thermalOption_consumer_1")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"] == "Navigation","EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged","EventName field name did not generate"
        assert event["11"] == "pcsystemcontrol-core","ScreenName field name  did not generate"
        assert event["12"] == "AUID_PCSystemControl_thermalOption_consumer_1"

        #click on cool mode and verify it's AUID analytics call
        self.fc.fd["system_control"].click_cool_consumer()
        time.sleep(4)
        event = self.fc.capture_analytics_event("AUID_PCSystemControl_thermalOption_consumer_2")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"] == "Navigation","EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged","EventName field name did not generate"
        assert event["11"] == "pcsystemcontrol-core","ScreenName field name  did not generate"
        assert event["12"] == "AUID_PCSystemControl_thermalOption_consumer_2"
        
        #click on quiet mode and verify it's AUID analytics call
        self.fc.fd["system_control"].click_quiet_consumer()
        time.sleep(4)
        event = self.fc.capture_analytics_event("AUID_PCSystemControl_thermalOption_consumer_3")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"] == "Navigation","EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged","EventName field name did not generate"
        assert event["11"] == "pcsystemcontrol-core","ScreenName field name  did not generate"
        assert event["12"] == "AUID_PCSystemControl_thermalOption_consumer_3"
        
        #click on performance mode and verify it's AUID analytics call
        self.fc.fd["system_control"].click_performance_consumer()
        time.sleep(4)
        event = self.fc.capture_analytics_event("AUID_PCSystemControl_thermalOption_consumer_0")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"] == "Navigation","EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged","EventName field name did not generate"
        assert event["11"] == "pcsystemcontrol-core","ScreenName field name  did not generate"
        assert event["12"] == "AUID_PCSystemControl_thermalOption_consumer_0"