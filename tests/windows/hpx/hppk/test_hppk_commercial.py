from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

# Modifer key supported devices are Medusa, Ultron
class Test_Suite_HPPK_Commercial(object):
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
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    def test_01_default_programmable_modified_key_ui_C39482970(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        soft_assertion = SoftAssert()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(programmable_key_heading, "Create personalized shortcuts with the press of a button","personalized shortcuts text is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_shift_hppk_icon(), "Shift hppk icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_ctrl_hppk_icon(), "Ctrl hppk icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_alt_hppk_icon(), "Alt hppk icon is not visible")
        # automation, key sequence, text input, myHP programmable key text verify
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_myhp_programmable_key_radio_btn(), "myHP Programmable Key", "myHP Programmable Key radio button is not visible")
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_programmable_key_radio_button_is_selected()))
        soft_assertion.raise_assertion_errors()

    def test_02_alt_programmable_key_C39482974(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        self.fc.fd["hppk"].click_alt_hppk_btn()
        soft_assertion = SoftAssert()
        # automation, key sequence, text input verify
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.raise_assertion_errors()

    def test_03_ctrl_programmable_key_C39482973(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        self.fc.fd["hppk"].click_ctrl_hppk_btn()
        soft_assertion = SoftAssert()
        # automation, key sequence, text input verify
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.raise_assertion_errors()

    def test_04_shift_programmable_key_C39482972(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        self.fc.fd["hppk"].click_shift_hppk_btn()
        soft_assertion = SoftAssert()
        # automation, key sequence, text input verify
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.raise_assertion_errors()
