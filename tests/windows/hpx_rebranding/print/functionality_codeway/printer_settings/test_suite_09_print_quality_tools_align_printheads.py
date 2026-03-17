import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_09_Print_Quality_Tools_Align_Printheads(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name = cls.p.get_printer_information()["model name"]
        
        """
        Check the test printer support align printhead or not.
        
        """
        cls.fc.launch_hpx_to_home_page()
        cls.fc.add_a_printer(cls.p)
        cls.fc.fd["devicesMFE"].verify_windows_dummy_printer(cls.printer_name, timeout=30)
        cls.fc.fd["devicesMFE"].click_windows_dummy_printer(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].click_view_all_button()
        cls.fc.fd["printersettings"].verify_progress_bar()
        cls.fc.fd["printersettings"].select_print_quality_tools()
        if not cls.fc.fd["printersettings"].verify_align_printheads_part(raise_e=False):
            pytest.skip("Skipping align printheads flow: not an align printheads printer.")

    @pytest.mark.regression
    def test_01_add_printer(self):
        """
        add a printer and navigate to print quality tools align printheads page.
        """
        self.fc.fd["printersettings"].click_align_arrow()
        
    @pytest.mark.regression
    def test_02_verify_align_printheads_dialog_with_auto_alignment_printer_C57706748_C57706749_C57706750(self):
        """
        Align Printheads disappear when click done or cancel button.
        Alignment Complete dialog appears after alignment is done with auto alignment printer.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706748
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706749
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706750 

        """
        if self.get_alignment_type() != "auto":
            pytest.skip("Skipping auto alignment flow: not an auto alignment printer.")
        else:
           self.fc.fd["printersettings"].click_quality_cancel_btn()
           assert not self.fc.fd["printersettings"].verify_alignment_dialog( raise_e=False)
           self.fc.fd["printersettings"].verify_print_quality_tools_page()
           self.fc.fd["printersettings"].click_align_arrow()
           self.fc.fd["printersettings"].verify_alignment_dialog()
           self.fc.fd["printersettings"].verify_align_printheads_finished_dialog()
           self.fc.fd["printersettings"].click_done_btn_on_alignment_dialog()
           assert not self.fc.fd["printersettings"].verify_align_printheads_finished_dialog(raise_e=False)

    @pytest.mark.regression
    def test_03_verify_align_printheads_dialog_with_semi_alignment_printer_C57706950_C57706951_C57706954_C57706955_C57706956(self):
        """
        Align printhead with semi_printers flow.
        Can't load align page into scanner.
        Some cases need update with QAMA-8734.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706950 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706951
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706954
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706955
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706956
        """
        if self.get_alignment_type() != "semi":
           pytest.skip("Skipping semi alignment flow: not a semi alignment printer.")
        else:
           self.fc.fd["printersettings"].click_quality_cancel_btn()
           assert not self.fc.fd["printersettings"].verify_align_printheads_dialog(raise_e=False)
           self.fc.fd["printersettings"].verify_print_quality_tools_page()
           self.fc.fd["printersettings"].click_align_arrow()
           self.fc.fd["printersettings"].verify_align_printheads_dialog()
           self.fc.fd["printersettings"].click_print_alignment_page_btn()
           self.fc.fd["printersettings"].verify_align_printheads_printing_dialog()
           self.fc.fd["printersettings"].verify_align_printheads_place_dialog()
           self.fc.fd["printersettings"].click_align_scan_page_btn()
           self.fc.fd["printersettings"].verify_align_printheads_scanning_dialog()
           
    @pytest.mark.regression
    def test_04_verify_unable_to_align_diaglog_shows_C57706958(self):
        """
        Scan page is loaded into scan bed with some printers.
        Align Complete dialogue displays after scanning.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706958

        """
        result = self.get_alignment_scan_result()
        if result == "success":
            self.fc.fd["printersettings"].click_done_btn_on_alignment_dialog()
        elif result == "failed":
            pytest.skip("Unable to align dialog shows, skipping success flow.")
        else:
            pytest.fail("Neither 'success' nor 'failed' dialog appeared after alignment scan.")

    @pytest.mark.regression
    def test_05_verify_alignment_complete_dialogue_displays_C57706957(self):
        """
        Unable to align flow shows when perform scan page flow without no align page on scanner.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706957
        
        """
        self.fc.fd["printersettings"].click_align_arrow()
        if self.get_alignment_type() != "semi":
            pytest.skip("Skipping semi alignment flow: not a semi alignment printer.")
        else:
            self.fc.fd["printersettings"].click_print_alignment_page_btn()
            self.fc.fd["printersettings"].verify_align_printheads_printing_dialog()
            self.fc.fd["printersettings"].verify_align_printheads_place_dialog()
            self.fc.fd["printersettings"].click_align_scan_page_btn()
            self.fc.fd["printersettings"].verify_align_printheads_scanning_dialog()
            result = self.get_alignment_scan_result()
            if result == "failed":
                self.fc.fd["printersettings"].verify_unable_to_align_dialog()
                self.fc.fd["printersettings"].click_back_btn_on_dialog()
                self.fc.fd["printersettings"].verify_align_printheads_place_dialog()
            elif result == "success":
                pytest.skip("Scan did not fail, skipping failed flow.")
            else:
                pytest.fail("Neither 'success' nor 'failed' dialog appeared after alignment scan.")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def get_alignment_type(self):
        """
        Determine the type of alignment based on the first align dialog.
        """
        if self.fc.fd["printersettings"].verify_alignment_dialog(raise_e=False):
           return "auto"
        elif self.fc.fd["printersettings"].verify_align_printheads_dialog(raise_e=False):
           return "semi"
        else:
           return "unknown"   

    def get_alignment_scan_result(self):
        """
        Scan failed or successfully during semi alignment flow.
        Returns 'failed', 'success', or 'none' if neither dialog is found.
        """
        if self.fc.fd["printersettings"].verify_unable_to_align_dialog(raise_e=False):
            return "failed"
        elif self.fc.fd["printersettings"].verify_align_printheads_finished_dialog(raise_e=False):
            return "success"
