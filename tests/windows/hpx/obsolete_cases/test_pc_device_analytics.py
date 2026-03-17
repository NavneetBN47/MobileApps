from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import pytest
import logging

pytest.app_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_PC_Device_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()

    def test_01_analytics_infopopover_C36088029(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        assert bool(self.fc.fd["devices"].verify_presenceOf_info_icon_devicepage()) is True
        self.fc.fd["devices"].click_info_icon_devicepage()
        event = self.fc.capture_analytics_event("AUID_pcdevice-core_DeviceInfoList_InfoPopOver")
        logging.info("{}".format(event))
        assert len(event) > 0, "info icon event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onOpen", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_pcdevice-core_DeviceInfoList_InfoPopOver", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
  
    def test_02_analytics_productnumber_infovaluecopied_C36088002(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].verify_click_on_product_number()
        event = self.fc.capture_analytics_event("AUID_pcdevice-core_CopyableInfoValue_ProductNumber_InfoValueCopied")
        logging.info("{}".format(event))
        assert len(event) > 0, "product number event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_pcdevice-core_CopyableInfoValue_ProductNumber_InfoValueCopied", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_03_analytics_serialnumber_infovaluecopied_C36088030(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].verify_click_on_serial_number()
        event = self.fc.capture_analytics_event("AUID_pcdevice-core_CopyableInfoValue_SerialNumber_InfoValueCopied")
        logging.info("{}".format(event))
        assert len(event) > 0, "serial number event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_pcdevice-core_CopyableInfoValue_SerialNumber_InfoValueCopied", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
    
    def test_04_analytics_productnumber_copyicon_C36120992(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].verify_click_on_productnumber_copyicon()
        event = self.fc.capture_analytics_event("AUID_pcdevice-core_CopyableInfoValue_ProductNumber_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event) > 0, "product number copy icon event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_pcdevice-core_CopyableInfoValue_ProductNumber_InfoValueCopied_CopyIcon", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
    
    def test_05_analytics_serialnumber_copyicon_C36120993(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].verify_click_on_serialnumber_copyicon()
        event = self.fc.capture_analytics_event("AUID_pcdevice-core_CopyableInfoValue_SerialNumber_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event) > 0, "serial number copy icon event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_pcdevice-core_CopyableInfoValue_SerialNumber_InfoValueCopied_CopyIcon", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.require_platform(["grogu"])
    def test_06_analytics_progkey_C36088036(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_HPPK_card_visible()
        self.fc.fd["devices"].click_prog_key_card()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_progkey-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "Programmable Key event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_progkey-core", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()  
    
    @pytest.mark.require_platform(["on hold"])
    def test_07_analytics_rgbkeyboard_C36088037(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_rgb_keyword()
        self.fc.fd["rgb_keyboard"].click_rgb_keyboard()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_rgbkeyboard-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation","EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged","EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core","ScreenName field name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_rgbkeyboard-core","AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.require_platform(["grogu"])
    def test_08_analytics_smartcam_C36088034(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_video_control_card_visible()
        self.fc.fd["devices"].click_video_control()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_smartcam-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "video control card event not found"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_smartcam-core", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_09_analytics_support_C36088039(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_support_action_card()
        self.fc.fd["devices"].click_support_btn()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_support-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "AUID_PCDevicePage_FeatureCard_support-core"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_support-core", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_10_analytics_pcaudio_C36088032(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_audio_card_on_pcdevice()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_pcaudio-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "AUID_PCDevicePage_FeatureCard_pcaudio-core"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_pcaudio-core", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_11_analytics_pcdisplay_C36088035(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control_card_pcdevice()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_pcdisplay-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "AUID_PCDevicePage_FeatureCard_pcdisplay-core"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_pcdisplay-core", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_12_analytics_pcconnect_C36088038(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_5g_card()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_pcconnect-core")
        logging.info("{}".format(event))
        assert len(event) > 0, "AUID_PCDevicePage_FeatureCard_pcconnect-core"
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcdevice-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCDevicePage_FeatureCard_pcconnect-core", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()