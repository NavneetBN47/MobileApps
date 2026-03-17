import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_08_Print_Quality_Tools_Clean_Printheads(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        """
        Check the test printer support cleaning printhead or not.
        
        """
        cls.fc.launch_hpx_to_home_page()
        cls.fc.add_a_printer(cls.p)
        cls.fc.fd["devicesMFE"].verify_windows_dummy_printer(cls.printer_name, timeout=30)
        cls.fc.fd["devicesMFE"].click_windows_dummy_printer(cls.printer_name)
        cls.fc.fd["devicesDetailsMFE"].click_view_all_button()
        cls.fc.fd["printersettings"].verify_progress_bar()
        cls.fc.fd["printersettings"].select_print_quality_tools()
        if not cls.fc.fd["printersettings"].verify_clean_printheads_part(raise_e=False):
            pytest.skip("Skipping clean printheads flow: not a clean printheads printer.")

    @pytest.mark.regression
    def test_01_verify_clean_printheads_dialog_C57706966_C57706967(self):
        """
        Clean Printheads and then Close button afterwards, verify user returns to Print Quality Tools.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706966 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706967          
        """
        self.fc.fd["printersettings"].click_clean_arrow()
        self._clean_printhead_flow()
        self.fc.fd["printersettings"].click_cleaning_done_btn()
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog_dismiss()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()

    @pytest.mark.regression
    def test_02_verify_clean_printheads_dialog_2en_level_screen_C57706968(self):
        """
        Select Clean Printheads, Second Level Clean is performed with results page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706968
        """
        self.fc.fd["printersettings"].click_clean_arrow()
        self._clean_printhead_flow()
        # Second Level Clean dialogue
        self.fc.fd["printersettings"].click_clean_again_btn()
        self._clean_printhead_flow()
        self.fc.fd["printersettings"].click_cleaning_done_btn()
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog_dismiss()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()

    @pytest.mark.regression
    def test_03_verify_clean_printheads_dialog_C57706969(self):
        """
        Select Clean Printheads>Second>Third Level Clean, Third Level Clean is performed with results page.
        Failed with HPXG-2854.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57706969
        """
        self.fc.fd["printersettings"].click_clean_arrow()
        self._clean_printhead_flow()
        # Second Level Clean dialogue.
        self.fc.fd["printersettings"].click_clean_again_btn()
        self._clean_printhead_flow()
        # Third Level Clean Dialogue.
        self.fc.fd["printersettings"].click_clean_again_btn()
        self._clean_printhead_flow()
        self.fc.fd["printersettings"].click_cleaning_done_btn()
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog_dismiss()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def _clean_printhead_flow(self):
        self.fc.fd["printersettings"].verify_cleaning_dialog()
        self.fc.fd["printersettings"].verify_cleaning_dialog_dismiss(timeout=90)
        self.fc.fd["printersettings"].verify_printing_dialog()
        self.fc.fd["printersettings"].verify_printing_dialog_dismiss()
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog()
