import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_32_Sanity_Diagnose_And_Fix(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.ip = cls.p.get_printer_information()["ip address"]


    @pytest.mark.smoke
    def test_01_verify_diagnose_and_fix_screen_C53556387(self):
        """
        Diagnose and Fix screen after clicking on Diagnose & Fix button on PDP.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53556387
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.fc.fd["diagnosefix"].verify_diagnose_and_fix_screen()

    @pytest.mark.smoke
    def test_02_verify_diagnose_and_fix_flow_C60951280_C60951282_C60951287(self):
        """
        verify Diagnose & Fix flow for no issue was found.
        Verify PDP shows after clicking done button.
        HPXG-3701 [UI] The positions of buttons on some screen are inconsistent with the Figma design.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951280
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951282
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951287
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.fc.fd["diagnosefix"].click_start_btn()
        self.fc.fd["diagnosefix"].verify_no_issue_screen()
        self.fc.fd["diagnosefix"].click_done_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page()

    @pytest.mark.smoke
    def test_03_verify_diagnose_and_fix_flow_for_issue_was_found_and_fixed_C60951290_C60951291(self):
        """
        verify Diagnose & Fix flow for issue was found and fixed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951290
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951291
        """
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        sleep(5)
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.fc.fd["diagnosefix"].click_start_btn()
        self.fc.fd["diagnosefix"].verify_diagnosing_and_fixing_screen_display()
        self.fc.fd["diagnosefix"].verify_diagnosis_complete_fixed_screen()

    @pytest.mark.smoke
    def test_04_verify_user_navigate_to_pdp_C60951716(self):
        """
        Verify user navigate to PDP after clicking Done button on If you're still having… screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951716
        """
        self.fc.fd["diagnosefix"].click_done_btn()
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        sleep(5)
        self.fc.fd["diagnosefix"].click_start_btn()
        try:
            self.fc.trigger_printer_offline_status(self.p)
            self.fc.fd["diagnosefix"].verify_diagnosing_and_fixing_screen_display()
            self.fc.fd["diagnosefix"].verify_here_are_your_results_not_fixed_screen()
            # HPXG-4058
            self.fc.fd["diagnosefix"].click_next_btn()
            self.fc.fd["diagnosefix"].verify_if_you_are_still_having_problems_screen()
            self.fc.fd["diagnosefix"].click_done_btn()
            self.fc.fd["devicesDetailsMFE"].verify_printer_device_page()
        finally:
            self.fc.restore_printer_online_status(self.p)