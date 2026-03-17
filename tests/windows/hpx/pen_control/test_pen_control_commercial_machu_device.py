from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Pen_Control_Machu_Device(object):
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

    def test_01_pen_settings_ui_C48460055(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(8)
        self.fc.fd["pen_control"].click_pen_settings_button()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_setting_notification_header(), "Notification", "Notification header is not visible")
        soft_assertion.assert_equal(str(self.fc.fd["pen_control"].get_pen_not_detected_alert_title()).lstrip(), "Alert when pen is not detected", "Alert when pen is not detected text is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_not_detected_toggle_is_visible(),"Pen not detected toggle is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_power_saving_header(), "Power saving", "Power Saving text is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_power_saving_desc(), "Pen will start sleep mode when it is idle", "Power will start text is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_power_saving_toggle_is_visible(),"Power saving toggle is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_one_step_inking_header(), "One step inking", "One step inking text is not visible")
        soft_assertion.assert_equal(str(self.fc.fd["pen_control"].get_one_step_inking_desc()).lstrip(), "When pen is detached, launch", "When step is detached text is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_one_step_inking_dropdown_is_visible(),"One step inking dropdown is not visible")
        soft_assertion.raise_assertion_errors()

    def test_02_verify_one_step_inking_dropdown_values_C48586325(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(8)
        self.fc.fd["pen_control"].click_pen_settings_button()
        soft_assertion = SoftAssert()
        self.fc.fd["pen_control"].click_one_step_inking_dropdown()
        soft_assertion.assert_equal(str(self.fc.fd["pen_control"].verify_inking_dropdown_value_one_note()).strip(), "One Note", "One Note dropdown valueis not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_inking_dropdown_value_microsoft_whiteboard(), "Microsoft Whiteboard", "Microsoft Whiteboard dropdown value is not visible")
        soft_assertion.assert_equal(str(self.fc.fd["pen_control"].verify_inking_dropdown_value_snipping_tool()).strip(), "Snipping Tool", "Snipping tool dropdown value is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_inking_dropdown_value_disabled(), "Disabled", "None dropdown value is not visible")
        soft_assertion.raise_assertion_errors()

    def test_03_verify_pen_seetings_default_values_C48586762(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(8)
        self.fc.fd["pen_control"].click_pen_settings_button()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_pen_not_detected_toggle_status(), "1", "Pen not detected toggle is not on")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_power_saving_toggle_status(), "1", "Power saving toggle is not on")
        soft_assertion.raise_assertion_errors()

    def test_04_verify_pen_is_not_detected_toggle_btn_status_C48589446(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(8)
        self.fc.fd["pen_control"].click_pen_settings_button()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_pen_not_detected_toggle_status(),"1","Pen not detected toggle is not on")
        self.fc.fd["pen_control"].click_pen_not_detected_toggle_button()
        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_pen_not_detected_toggle_status(),"0","Pen not detected toggle is not off")
        self.fc.fd["pen_control"].click_pen_not_detected_toggle_button()
        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_pen_not_detected_toggle_status(),"1","Pen not detected toggle is not on")
        soft_assertion.raise_assertion_errors()

    def test_05_verify_power_saving_toggle_btn_status_C48587432(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(8)
        self.fc.fd["pen_control"].click_pen_settings_button()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_power_saving_toggle_status(), "1", "Power saving toggle is not on")
        self.fc.fd["pen_control"].click_power_saving_toggle_button()
        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_power_saving_toggle_status(), "0", "Power saving toggle is not off")
        self.fc.fd["pen_control"].click_power_saving_toggle_button()
        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_power_saving_toggle_status(), "1", "Power saving toggle is not on")
        soft_assertion.raise_assertion_errors()
