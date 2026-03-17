import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Context_Aware_OTA(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        time.sleep(10)
        cls.fc.fd["home"].click_to_install_signed_build()
        time.sleep(60)
        cls.fc.launch_myHP()
        time.sleep(5)

    def test_01_upgrade_from_ms_store_C36768124(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calculator")), True, "Calculator is not present")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")
        self.fc.ota_app_after_update()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calculator")), True, "Calculator is not present")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")
        self.fc.exit_hp_app_and_msstore()