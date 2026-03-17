import pytest
import logging
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_08_Scan_Intro_Auto_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.adf_scan_support = {}

        
    @pytest.mark.regression
    def test_01_check_auto_enhance_setting_C43738423(self):
        """
        Verify Auto Enhance toggle button by default "ON" in Scan tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738423
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.adf_scan_support['status'] = True
        else:
            self.adf_scan_support['status'] = False

        self.fc.fd["scan"].select_auto_enhancement_icon()
        self.fc.fd["scan"].verify_auto_enhancement_panel_setting_by_default()

    @pytest.mark.parametrize("source, enhancement, orientation", [("Scanner Glass", "1", "0"), ("Document Feeder", "1", "0"),
                                                                ("Scanner Glass", "1", "1"), ("Document Feeder", "1", "1"),
                                                                ("Scanner Glass", "0", "0"), ("Document Feeder", "0", "0"),
                                                                ("Scanner Glass", "0", "1"), ("Document Feeder", "0", "1"),])
    @pytest.mark.regression
    def test_02_change_enhancement_and_orientation_C43738424(self, source, enhancement, orientation):
        """
        Change Orientation and Enhancement 'on' and 'off' in auto enhancement panel, verify values can be changed and changes are reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738424
        """
        if not self.adf_scan_support['status'] and source == "Document Feeder":
            pytest.skip("Test printer does not support ADF scan. Skip this test!")
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=20)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        #Select corresponding scan source
        if self.adf_scan_support['status']:
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, source)
        assert self.fc.fd["scan"].get_scan_source_value() == source
        logging.info(f"Scan Source set to: {source}")

        #Set corresponding Auto enhancement and Auto orientation toggle status
        sleep(2)
        self.fc.fd["scan"].select_auto_enhancement_icon()
        self.fc.fd["scan"].verify_auto_enhancement_panel()
        if enhancement != self.fc.fd["scan"].verify_auto_enhancement_state():
            self.fc.fd["scan"].click_auto_enhancements_toggle()
        auto_enhancement_state = self.fc.fd["scan"].verify_auto_enhancement_state()
        logging.info(f"Current Auto enhancement toggle status is: {auto_enhancement_state}")
        if orientation != self.fc.fd["scan"].verify_auto_orientation_state():
            self.fc.fd["scan"].click_auto_orientation_toggle()
        auto_orientation_state = self.fc.fd["scan"].verify_auto_orientation_state()
        logging.info(f"Current Auto orientation toggle status is: {auto_orientation_state}")

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)