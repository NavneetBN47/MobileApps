from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import logging
import time

pytest.app_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Pen_Control_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()

    def test_01_edit_button_analytics_C32548859(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_edit_button()
        event = self.fc.capture_analytics_event("AUID_PenControl_DeviceName_DeviceNameEditBtn")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DeviceName_DeviceNameEditBtn", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_02_restore_deafaul_button_analytics_C32548864(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(3)
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_RestoreSettings_RestoreButton")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_RestoreSettings_RestoreButton", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_03_top_button_single_press_analytics_C32594229(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        self.driver.swipe(direction="up", distance=3)
        time.sleep(5)
        self.fc.fd["pen_control"].click_single_press_dd()
        self.fc.fd["pen_control"].click_ms_white_board()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_SinglePress_TrackedDropdown")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_SinglePress_TrackedDropdown", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_04_top_button_double_press_analytics_C32594230(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.driver.swipe(direction="up", distance=3)
        self.fc.fd["pen_control"].click_double_press_dd()
        self.fc.fd["pen_control"].click_double_press_touch_on_off()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_DoublePress_TrackedDropdown")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DoublePress_TrackedDropdown", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_05_top_button_long_press_analytics_C32594231(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.driver.swipe(direction="up", distance=2)
        self.fc.fd["pen_control"].click_long_press_dd()
        self.fc.fd["pen_control"].click_long_press_previous_track()
        event = self.fc.capture_analytics_event("AUID_PenControl_LongPress_TrackedDropdown")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_LongPress_TrackedDropdown", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_06_upper_barrel_button_press_analytics_C32594238(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        self.driver.swipe(direction="up", distance=3)
        self.fc.fd["pen_control"].click_upper_barrel_dropdown()
        self.fc.fd["pen_control"].click_upper_barrel_erase()
        event = self.fc.capture_analytics_event("AUID_PenControl_UpperBarrelButton_TrackedDropdown")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_UpperBarrelButton_TrackedDropdown", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_07_lower_barrel_button_press_analytics_C32594239(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        self.fc.fd["pen_control"].click_lower_barrel_dropdown()
        self.fc.fd["pen_control"].click_lower_barrel_right_click()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_LowerBarrelButton_TrackedDropdown")
        logging.info("{}".format(event))

        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_LowerBarrelButton_TrackedDropdown", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_08_lower_barrel_hover_toggle_click_analytics_C35864587(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_off()
        event = self.fc.capture_analytics_event("AUID_PenControl_HoverToggle_LowerBarrelHoverToggle")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_HoverToggle_LowerBarrelHoverToggle", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_09_upper_barrel_hover_toggle_click_analytics_C35864607(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["pen_control"].click_restore_button()
        self.driver.swipe(direction="up", distance=3)
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_off()
        event = self.fc.capture_analytics_event("AUID_PenControl_HoverToggle_UpperBarrelHoverToggle")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onValueChange", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_HoverToggle_UpperBarrelHoverToggle", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_10_device_info_button_click_analytics_C35864680(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_info_icon()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_DeviceInfoList_InfoPopOver")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onOpen", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DeviceInfoList_InfoPopOver", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_11_copy_product_number_analytics_C32548860(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_info_icon()
        self.fc.fd["pen_control"].click_product_number_copy_icon()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_CopyableInfoValue_productNumber_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_CopyableInfoValue_productNumber_InfoValueCopied_CopyIcon", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_12_copy_serial_number_analytics_C32548861(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_info_icon()
        self.fc.fd["pen_control"].click_serial_number_copy_icon()
        event = self.fc.capture_analytics_event("AUID_PenControl_CopyableInfoValue_serialNumber_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_CopyableInfoValue_serialNumber_InfoValueCopied_CopyIcon", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_13_copy_wireframe_version_analytics_C32548862(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(3)
        self.fc.fd["pen_control"].click_info_icon()
        self.fc.fd["pen_control"].click_firmware_version_copy_icon()
        event = self.fc.capture_analytics_event("AUID_PenControl_CopyableInfoValue_firmwareVersion_InfoValueCopied_CopyIcon")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_CopyableInfoValue_firmwareVersion_InfoValueCopied_CopyIcon", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
