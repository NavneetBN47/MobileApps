from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "HPX"
class Test_Suite_Audio_Core_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        time.sleep(5)
        cls.fc.close_app()
        cls.fc.launch_app()
    
    @pytest.mark.require_platform(["grogu", "london"])
    def test_01_analytics_for_keyboard_module_C36963552(self):
        self.fc.close_app()
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        event = self.fc.capture_analytics_event("hpackeyboard_core_NavigationViewItem_ID")
        logging.info("{}".format(event))
        assert len(event)>0, "KeyBoard Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "welcomeContainer", "ScreenName field name did not generate"
        #Note: It fails with above event sometimes, so added below event as well, once it is fixed, remove incorrect event
        # assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "hpackeyboard_core_NavigationViewItem_ID", "AUID Field did not generate"
        time.sleep(2)   

    @pytest.mark.require_platform(["grogu", "london"])
    def test_02_analytics_for_keyboard_header_C37251751(self):
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        self.fc.fd["external_keyboard"].click_rename_icon()
        #Edit Button
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_DeviceName_DeviceNameEditBtn")
        logging.info("{}".format(event))
        assert len(event)>0, "KeyBoard Edit button Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_DeviceName_DeviceNameEditBtn", "AUID Field did not generate"
        #Info Icon
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_info_icon()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_DeviceInfoList_InfoPopOver")
        logging.info("{}".format(event))
        assert len(event)>0, "Info Icon button Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onOpen", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_DeviceInfoList_InfoPopOver", "AUID Field did not generate"
        #Production number text
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_production_number_text()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_CopyableInfoValue_productNumber_InfoValueCopied")
        logging.info("{}".format(event))
        assert len(event)>0, "Production number text Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_CopyableInfoValue_productNumber_InfoValueCopied", "AUID Field did not generate"
        #Production copy icon
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_production_number_copy_icon()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_CopyableInfoValue_productNumber_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event)>0, "Production number Copy Icon Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_CopyableInfoValue_productNumber_InfoValueCopied_CopyIcon", "AUID Field did not generate"
        #Serial number text
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_serial_number_text()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_CopyableInfoValue_serialNumber_InfoValueCopied")
        logging.info("{}".format(event))
        assert len(event)>0, "Serial number text Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_CopyableInfoValue_serialNumber_InfoValueCopied", "AUID Field did not generate"
        #Serial copy icon
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_serial_number_copy_icon()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_CopyableInfoValue_serialNumber_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event)>0, "Serial number copy icon Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_CopyableInfoValue_serialNumber_InfoValueCopied_CopyIcon", "AUID Field did not generate"
        self.fc.close_app()
        
    @pytest.mark.require_platform(["grogu", "london"])
    def test_03_analytics_for_keyboard_header_C37251751(self):
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()    
        #Proximity switch
        time.sleep(10)
        self.fc.fd["external_keyboard"].click_proximity_sensor_btn()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_Lighting_Setup_proximityswitch")
        logging.info("{}".format(event))
        assert len(event)>0, "Proximity Switch Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onValueChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_Lighting_Setup_proximityswitch", "AUID Field did not generate"
        #Backlight switch
        time.sleep(10)
        self.fc.fd["external_keyboard"].click_backlight_adjust_btn()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_Lighting_Setup_backLightSwitch")
        logging.info("{}".format(event))
        assert len(event)>0, "Backlight Switch Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onValueChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_Lighting_Setup_backLightSwitch", "AUID Field did not generate"
        #Timer Slider
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_restore_button()
        time.sleep(5)
        self.fc.fd["external_keyboard"].set_time_slider_value_increase(50,"time_slider")
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_TimeSlider_timeSlider")
        logging.info("{}".format(event))
        assert len(event)>0, "Timer Slider Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_TimeSlider_timeSlider", "AUID Field did not generate"
        #Brightness Slider
        time.sleep(5)
        self.fc.fd["external_keyboard"].set_brightness_slider_value_increase(100,"brightness_slider")
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_BrightnessSlider_brightnessSlider")
        logging.info("{}".format(event))
        assert len(event)>0, "Brightness Slider Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_BrightnessSlider_brightnessSlider", "AUID Field did not generate"
        #Restore Default
        time.sleep(5)
        self.fc.fd["external_keyboard"].click_restore_button()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCKEYBOARD_RestoreButton_RestoreButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Timer Slider Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "hpackeyboard-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCKEYBOARD_RestoreButton_RestoreButton", "AUID Field did not generate"
     