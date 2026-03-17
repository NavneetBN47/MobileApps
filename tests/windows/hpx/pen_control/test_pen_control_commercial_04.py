from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Pen_Control_Commercial(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            cls.fc.close_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_tilt_sensitivity_slider_values_C38313886(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_sensivity_slider_visible(), "Pen sensivity slider is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "1", "Pen sensitivity slider value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_max_value("tilt_sensitivity_slider"), "2", "Pen sensitivity max slider value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_min_value("tilt_sensitivity_slider"), "0", "Pen sensitivity min slider value is not correct")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_tip_pressure_slider_values_C38313921(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pressure_title_text(), "Pressure", "Pressure title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_tip_pressure_slider_visible(), "Pen tilt pressure slider is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "3", "Pen tip pressure slider value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_max_value("tip_pressure_slider"), "6", "Pen tip pressure slider max value is not correct")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_min_value("tip_pressure_slider"), "0", "Pen tip pressure slider min value is not correct")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_pressure_tip_slider_dragdrop_C38313885(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pressure_title_text(), "Pressure", "Pressure title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_tip_pressure_slider_visible(), "Pen tip pressure slider is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "3", "Pen tip pressure slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_increase(1,"tip_pressure_slider")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "4", "Pen tip pressure max slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_decrease(2,"tip_pressure_slider")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tip_pressure_slider"), "2", "Pen tip pressure min slider value is not correct")
        soft_assertion.raise_assertion_errors()
    
    def test_04_proximity_icon_C42320654(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        soft_assertion = SoftAssert()
        soft_assertion.assert_true ( self.fc.fd["pen_control"].verify_proximity_icon()), "Proximity icon is not visible"
        self.fc.fd["pen_control"].click_proximity_icon()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_proximity_icon_tooltip_text(), "Connection Proximity", "Connection Proximity icon text is not visible")
        soft_assertion.raise_assertion_errors()

    def test_05_launch_via_deeplink_C39690878(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pencontrol")
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_pen_is_selected_from_navbar()), "pen is not selected from navbar")
        soft_assertion.raise_assertion_errors()
