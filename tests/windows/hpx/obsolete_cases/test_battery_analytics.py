from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Context_Aware_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.delete_capture_analytics_files()
        cls.fc.launch_app()
    
    
    @pytest.mark.require_stack(["pie"])
    def test_01_analytics_C37962114(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].click_maximize_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_maximize_charging_box()

        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCBatteryManager_CharginOptions_MaximizeBatteryHealth")
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcbatterymanager-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCBatteryManager_CharginOptions_MaximizeBatteryHealth","AUID Field did not generate"

    
    @pytest.mark.require_stack(["pie"])
    def test_02_analytics_radio_buttons_C37962120(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].click_maximize_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_optimize_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_maximize_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        self.fc.fd["battery"].click_optimize_charging_box()

        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCBatteryManager_CharginOptions_MaximizeBatteryHealth")
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcbatterymanager-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCBatteryManager_CharginOptions_MaximizeBatteryHealth","AUID Field did not generate"

        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCBatteryManager_CharginOptions_optimizeBatteryPerformance")
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcbatterymanager-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCBatteryManager_CharginOptions_optimizeBatteryPerformance","AUID Field did not generate"

        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCBatteryManager_CharginOptions_ScheduleBatteryCharging")
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcbatterymanager-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCBatteryManager_CharginOptions_ScheduleBatteryCharging","AUID Field did not generate"


    @pytest.mark.require_stack(["pie"])
    def test_03_analytics_battery_dropdown_C37962225(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=4)
        time.sleep(2)
        self.fc.fd["battery"].click_start_charge_dropdown_list()
        time.sleep(2)
        self.fc.fd["battery"].click_battery_thirty_percent()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCBatteryManager_SchedulerWeek_Start_Battery_Charge")
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcbatterymanager-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCBatteryManager_SchedulerWeek_Start_Battery_Charge","AUID Field did not generate"


    @pytest.mark.require_stack(["pie"])
    def test_04_analytics_battery_clear_schedule_button_C37962229(self):

        time.sleep(3)
        self.fc.restart_app()

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_battery_module()

        self.fc.fd["battery"].verify_battery_title_show()

        time.sleep(2)
        self.fc.fd["battery"].click_schedule_charging_box()

        time.sleep(2)
        self.driver.swipe(direction="down", distance=4)
        self.fc.fd["battery"].click_sunday_dropdown()
        time.sleep(2)
        self.fc.fd["battery"].click_three_am_item()
        time.sleep(2)
        self.driver.swipe(direction="down", distance=4)
        self.fc.fd["battery"].click_clear_schedule()

        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCBatteryManager_SchedulerWeek_ClearSchedule_Button")
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcbatterymanager-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCBatteryManager_SchedulerWeek_ClearSchedule_Button","AUID Field did not generate"

    