import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_02_Diagnose_And_Fix_With_Issue_Found(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_verify_diagnose_and_fix_with_issue_found_flow_C60951292_C60951293_C60951294_C60951295_C60953454(self):
        """
        Verify Diagnosing & fixing screen shows as design.
        verify back button is disabled.
        Verify "Done" and "Test Print" buttons shows in "Diagnosis complete. Here are your results".
        Verify the "Diagnosis complete. Here are your results." screen is as design.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951292
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951293
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951294
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951295
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60953454

        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.fc.fd["diagnosefix"].click_start_btn()
        self.fc.fd["diagnosefix"].verify_diagnosing_and_fixing_screen_display()
        self.fc.fd["diagnosefix"].verify_back_btn_is_disabled()
        self.fc.fd["diagnosefix"].verify_diagnosis_complete_fixed_screen()

    @pytest.mark.regression
    def test_02_verify_here_are_your_results_button_C60951296(self):
        """
        Verify native print dialog shows with the Canned PDF file to print when "Test print" button is clicked.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951296
        """
        self.fc.fd["diagnosefix"].click_print_test_page_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
 
    @pytest.mark.regression
    def test_03_verify_back_to_pdp_after_clicking_done_btn_C60951297(self):
        """
        Verify user navigates to PDP screen when "Done" button is clicked.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951297
        """
        self.fc.fd["diagnosefix"].click_done_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)