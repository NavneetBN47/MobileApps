from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import logging
import time

pytest.app_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Pen_Control_Analytics_Commercial(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.delete_capture_analytics_files()
        cls.fc.close_app()
        cls.fc.launch_app()

    def test_01_edit_button_analytics_C38325130(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_edit_button()
        event = self.fc.capture_analytics_event("AUID_PenControl_DeviceName_DeviceNameEditBtnv4")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DeviceName_DeviceNameEditBtnv4", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_02_restore_deafaul_button_analytics_C38328726(self):
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

    def test_03_top_button_single_press_analytics_C38325204(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_SinglePress_Button")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_SinglePress_Button", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_04_top_button_double_press_analytics_C38325206(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PenControl_DoublePress_Button")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DoublePress_Button", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_05_top_button_long_press_analytics_C38325220(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        event = self.fc.capture_analytics_event("AUID_PenControl_LongPress_Button")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_LongPress_Button", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
    

    def test_06_right_click_button_analytics_C38325234(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_right_click_commercial()
        event = self.fc.capture_analytics_event("AUID_PenControl_UpperBarrel_Button")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_UpperBarrel_Button", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
    

    def test_07_erase_button_analytics_C38328718(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_erase_btn_commercial()
        event = self.fc.capture_analytics_event("AUID_PenControl_LowerBarrel_Button")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_LowerBarrel_Button", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    
    def test_08_pen_sensitivity_button_analytics_C38328721(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        event = self.fc.capture_analytics_event("AUID_PenControl_PenSensitivity_Button")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_PenSensitivity_Button", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_09_info_icon_C39892018(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_device_info()
        event = self.fc.capture_analytics_event("AUID_PenControl_InfoPopOver_v4")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_InfoPopOver_v4", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_10_pen_upper_barrel_hover_click_on_analytics_C38328769(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_off()
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_on()
        event = self.fc.capture_analytics_event("AUID_PenControl_HoverToggle_UpperBarrelHoverToggle")
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_Upper Barrel Switch_true", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_11_pen_upper_barrel_hover_click_off_analytics_C38328782(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_upper_barrel_button_hover_toggle_off()
        event = self.fc.capture_analytics_event("AUID_PenControl_HoverToggle_UpperBarrelHoverToggle")
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_HoverToggle_UpperBarrelHoverToggle", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_12_product_number_copyicon_C39901907(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_info_icon()
        self.fc.fd["pen_control"].click_product_number_copy_icon()
        event = self.fc.capture_analytics_event("AUID_PenControl_DeviceInfo_CopyIcon_productNumber_v4")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DeviceInfo_CopyIcon_productNumber_v4", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_13_serial_number_copyicon_C39901910(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_info_icon()
        self.fc.fd["pen_control"].click_serial_number_copy_icon()
        event = self.fc.capture_analytics_event("AUID_PenControl_DeviceInfo_CopyIcon_serialNumber_v4")
        logging.info("{}".format(event))
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onPress", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_DeviceInfo_CopyIcon_serialNumber_v4", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()

    def test_14_pen_Lower_barrel_hover_click_on_analytics_C38328842(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()  
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_off()
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_on()
    
        event = self.fc.capture_analytics_event("AUID_PenControl_HoverToggle_LowerBarrelHoverToggle")
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_HoverToggle_LowerBarrelHoverToggle", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
		
    def test_15_pen_Lower_barrel_hover_click_off_analytics_C38328850(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()  
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_off()
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_on()
        self.fc.fd["pen_control"].click_lower_barrel_button_hover_toggle_off()

        event = self.fc.capture_analytics_event("AUID_PenControl_HoverToggle_LowerBarrelHoverToggle")
        assert len(event) > 0, "Analytics Event not found."
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pencontrol-core", "ScreenName name  did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PenControl_HoverToggle_LowerBarrelHoverToggle", "AUID Field did not generate")
        soft_assertion.raise_assertion_errors()
