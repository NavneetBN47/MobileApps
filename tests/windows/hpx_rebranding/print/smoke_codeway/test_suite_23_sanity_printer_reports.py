import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import logging
import random


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_23_Sanity_Printer_Reports(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]

        """
        Check the test printer with the feature of printing reports feature.
        If the printer doesn't support this feature, skip all tests.
        """
        cls.fc.launch_hpx_to_home_page()
        cls.fc.add_a_printer(cls.p)
        cls.fc.fd["devicesMFE"].click_windows_dummy_printer(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].verify_printer_device_page(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].click_view_all_button() 
        cls.fc.fd["printersettings"].verify_progress_bar()
        cls.fc.fd["printersettings"].select_printer_reports()
        check_feature = cls.fc.fd["printersettings"].verify_this_feature_is_not_available_screen()
        if check_feature:
            pytest.skip("Skip all tests as the printer has no this feature")

    @pytest.mark.smoke
    def test_01_verify_printer_report_options_c57707027(self):
        """
        Click on Print Reports, verify report options on the right

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707027
        """
        Test_Suite_23_Sanity_Printer_Reports.report_list = self.fc.fd["printersettings"].verify_printer_reports_page()

    @pytest.mark.smoke
    def test_02_check_printer_status_report_c57707030_c57707031_c57707032(self):
        """
        Click Printer Status Report Print button, verify report is printed and accurate
        Click Close button on Status Report Complete dialogue, verify dialogue closes
        Click Cancel button on Printing Status Report dialogue, verify job is cancelled

        https://hp-testrail.external.hp.com/index.php?/cases/view/57707030
        https://hp-testrail.external.hp.com/index.php?/cases/view/57707031
        https://hp-testrail.external.hp.com/index.php?/cases/view/57707032
        """
        if "STATUS" not in Test_Suite_23_Sanity_Printer_Reports.report_list:
            pytest.skip("Skip this test as STATUS report is not supported")
        self.fc.fd["printersettings"].select_report_opt('STATUS')
        self.fc.fd["printersettings"].click_report_print_btn()
        printing_dialog = self.fc.fd["printersettings"].verify_report_printing_dialog('STATUS', timeout=10, raise_e=False)
        if printing_dialog is False:
            unknown_dialog = self.fc.fd["printersettings"].verify_print_status_unknown_dialog(raise_e=False)
            if unknown_dialog:
                self.fc.fd["printersettings"].click_report_ok_btn()
                pytest.skip("Printer Status Unknown")
            else:
                raise NoSuchElementException("Printing dialog or unknown status dialog is not displayed")
        self.fc.fd["printersettings"].verify_printing_is_completed_dialog('STATUS')

        if self.fc.fd["printersettings"].click_report_ok_btn(raise_e=False) is False:
            pytest.skip("Skip this test as OK button is missing")
        assert self.fc.fd["printersettings"].verify_printing_is_completed_dialog('STATUS', timeout=3, raise_e=False) is False
        sleep(3)

        self.fc.fd["printersettings"].select_report_opt('STATUS')
        self.fc.fd["printersettings"].click_report_print_btn()
        printing_dialog = self.fc.fd["printersettings"].verify_report_printing_dialog('STATUS', timeout=10, raise_e=False)
        if printing_dialog is False:
            unknown_dialog = self.fc.fd["printersettings"].verify_print_status_unknown_dialog(raise_e=False)
            if unknown_dialog:
                self.fc.fd["printersettings"].click_report_ok_btn()
                pytest.skip("Printer Status Unknown")
            else:
                raise NoSuchElementException("Printing dialog or unknown status dialog is not displayed")
        self.fc.fd["printersettings"].click_dialog_cancel_btn()
        assert self.fc.fd["printersettings"].verify_report_printing_dialog('STATUS', raise_e=False) is False

    @pytest.mark.smoke
    @pytest.mark.parametrize("opt", ["DIAGNOSTIC", "NETWORK", "WIRELESS", "QUALITY", "WEB", "DEMO"])
    def test_03_verify_e2e_flow_c53576684_c53575841(self, opt):
        """
        Verify E2E "Printer Reports" flow

        https://hp-testrail.external.hp.com/index.php?/cases/view/53576684

        Verify "Printer Reports" functionality
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/53575841
        """
        if opt not in Test_Suite_23_Sanity_Printer_Reports.report_list:
            pytest.skip(f"Skip this test as {opt} report is not supported")
        self.fc.fd["printersettings"].select_report_opt(opt)
        self.fc.fd["printersettings"].click_report_print_btn()
        if self.fc.fd["printersettings"].verify_report_printing_dialog(opt, timeout=10, raise_e=False) is False:
            unknown_dialog = self.fc.fd["printersettings"].verify_print_status_unknown_dialog(raise_e=False)
            if unknown_dialog:
                self.fc.fd["printersettings"].click_report_ok_btn()
                pytest.skip("Printer Status Unknown")
            else:
                raise NoSuchElementException("Printing dialog or unknown status dialog is not displayed")
        else:
            self.fc.fd["printersettings"].verify_report_printing_dialog_dismiss(timeout=300)
            if self.fc.fd["printersettings"].verify_printing_is_completed_dialog(opt, raise_e=False):
                self.fc.fd["printersettings"].click_report_ok_btn()
                assert self.fc.fd["printersettings"].verify_printing_is_completed_dialog(opt, timeout=3, raise_e=False) is False
                sleep(8)
            elif self.fc.fd["printersettings"].verify_print_status_unknown_dialog(raise_e=False):
                self.fc.fd["printersettings"].click_report_ok_btn()
                pytest.skip("Printer Status Unknown")

    def test_04_verify_error_e2e_flow_c53577821(self):
        """
        Verify the error scenario of E2E "Printer Reports" flow

        https://hp-testrail.external.hp.com/index.php?/cases/view/53577821
        """
        self.fc.trigger_printer_offline_status(self.p)
        opt = random.choice(Test_Suite_23_Sanity_Printer_Reports.report_list)
        self.fc.fd["printersettings"].select_report_opt(opt)
        self.fc.fd["printersettings"].click_report_print_btn()
        self.fc.fd["printersettings"].verify_unable_to_connect_dialog()
        self.fc.fd["printersettings"].click_dialog_cancel_btn()

    def test_05_restore_printer_online_status(self):
        self.fc.restore_printer_online_status(self.p)
