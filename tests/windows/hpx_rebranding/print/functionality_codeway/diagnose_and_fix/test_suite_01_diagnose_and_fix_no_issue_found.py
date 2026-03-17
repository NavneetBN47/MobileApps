import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_01_Diagnose_And_Fix_No_Issue_Found(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_verify_diagnose_and_fix_flow_C60951283_C60951286(self):
        """
        verify No issue was found screen displayed.
        Verify native print dialog shows after clicking Test Print button.
        HPXG-3701 [UI] The positions of buttons on some screen are inconsistent with the Figma design.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951283
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/60951286
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.fc.fd["diagnosefix"].click_start_btn()
        self.fc.fd["diagnosefix"].verify_diagnosing_and_fixing_screen_display()
        self.fc.fd["diagnosefix"].verify_no_issue_screen(raise_e=False)
        # HPXG-4351 [UI] The positions of buttons on some screen are inconsistent with the Figma design.
        self.fc.fd["diagnosefix"].click_test_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
