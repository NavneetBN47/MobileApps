import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_27_Sanity_Print_Quality_Tools(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_go_to_print_quality_tools_screen(self):
        """
        Add a printer
        Select "Print Quality Tools" under Tools.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].verify_printer_information_opt()
        sleep(2)
        self.fc.fd["printersettings"].select_print_quality_tools()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()

    @pytest.mark.smoke
    def test_02_verify_view_all_print_quality_tools_func_c53589303(self):
        """
        Verify the "View all print quality tools" functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/53589303
        """
        if self.fc.fd["printersettings"].verify_view_all_part(raise_e=False) is False:
            pytest.skip("View all print quality tools option is not available.")
        
        self.fc.fd["printersettings"].click_view_all_arrow()
        self.fc.fd["printersettings"].verify_ews_page()
        self.fc.fd["printersettings"].select_exit_setup_arrow()
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_printer_information_opt()
        self.fc.fd["printersettings"].select_print_quality_tools()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()

    @pytest.mark.smoke
    def test_03_verify_clean_printheads_func_c53590087(self):
        """
        Verify the end-to-end flow for "Clean Printheads" functionality.

        https://hp-testrail.external.hp.com/index.php?/cases/view/53590087
        """
        if self.fc.fd["printersettings"].verify_clean_printheads_part(raise_e=False) is False:
           pytest.skip("Clean Printheads option is not available.")
        # Click on "Clean Printheads".
        # The user should be navigated to the Cleaning screen as shown below:
        self.fc.fd["printersettings"].click_clean_arrow()
        self.fc.fd["printersettings"].verify_cleaning_dialog()

        # The user should be navigated to the Printing Cleaning screen as shown below:
        self.fc.fd["printersettings"].verify_printing_dialog()

        # Once the printing is done, the user will be navigated to the "Cleaning Complete" screen.
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog()

        # Click the "Clean Again" button to restart the process.
        self.fc.fd["printersettings"].click_clean_again_btn()
        self.fc.fd["printersettings"].verify_cleaning_dialog()
        self.fc.fd["printersettings"].verify_printing_dialog()

        # Click on the "Done" button to go back to the "Print Quality Tools" screen.
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog()
        self.fc.fd["printersettings"].click_cleaning_done_btn()
        self.fc.fd["printersettings"].verify_cleaning_complete_dialog_dismiss()
