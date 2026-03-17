import pytest
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_02_Ete_Printer_Settings_And_Diagnostics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"] 
        cls.param_list = ['diagnostics', 'diagnosticsandfix', 'quality', 'ews']
        cls.fc.fd["hpx_rebranding_common"].check_flag_param(cls.param_list)

    @pytest.mark.regression
    def test_01_add_a_printer(self):
        """
        Add a printer
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_02_verify_printer_settings_C59058265(self):
        """
        Verify Printer Settings

        View All button from PDP should navigate to the Printer Information screen.
        The left pane in the Printer Settings screen should be visible with all options enabled and clickable.
        Each clickable item in the left pane of the Printer Settings screen should navigate to its corresponding screen.
        The back button on the Printer Settings screen should be labeled with "Back", and should navigate to the PDP screen when clicked.

        https://hp-testrail.external.hp.com/index.php?/cases/view/59058265
        """
        # View All button from PDP should navigate to the Printer Information screen.
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].verify_printer_info_simple_page()

        # The left pane in the Printer Settings screen should be visible with all options enabled and clickable.
        self.fc.fd["printersettings"].verify_top_back_text()
        self.fc.fd["printersettings"].verify_status_tile()
        self.fc.fd["printersettings"].verify_information_tile()
        self.fc.fd["printersettings"].verify_settings_tile()
        self.fc.fd["printersettings"].verify_tools_tile()

        # Each clickable item in the left pane of the Printer Settings screen should navigate to its corresponding screen.
        self.fc.fd["printersettings"].select_printer_status_item()
        self.fc.fd["printer_status"].verify_ps_ioref_list()
        self.fc.fd["printersettings"].verify_top_back_text()

        self.fc.fd["printersettings"].select_printer_information()
        self.fc.fd["printersettings"].verify_printer_info_simple_page()
        self.fc.fd["printersettings"].verify_top_back_text()

        self.fc.fd["printersettings"].select_network_information()
        self.fc.fd["printersettings"].verify_network_info_simple_page()
        self.fc.fd["printersettings"].verify_top_back_text()

        self.fc.fd["printersettings"].select_printer_reports()
        if not self.fc.fd["printersettings"].verify_this_feature_is_not_available_screen():
            self.fc.fd["printersettings"].verify_printer_reports_page()
        self.fc.fd["printersettings"].verify_top_back_text()

        self.fc.fd["printersettings"].select_print_quality_tools()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()
        self.fc.fd["printersettings"].verify_top_back_text()

        self.fc.fd["printersettings"].select_advanced_settings_item()
        if self.fc.fd["printersettings"].verify_continuing_to_your_printer_settings_dialog():
            self.fc.fd["printersettings"].click_the_pin_ok_btn()
        self.fc.fd["printersettings"].verify_ews_page()
        self.fc.fd["printersettings"].verify_top_back_text()

        # The back button on the Printer Settings screen should be labeled with "Back", and should navigate to the PDP screen when clicked.
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_view_all_button()

    @pytest.mark.regression
    def test_03_verify_diagnostics_C61200134(self):
        """
        Verify Diagnostics tile

        1.The "Diagnose and Fix" screen should be displayed.
        2.Clicking the Back button should navigate to the PDP screen.
        3.Clicking Print Quality Tools should display the Print Quality Tools screen.
        4.Clicking the Back button on the Print Quality Tools screen navigates to the PDP screen.
        5.Clicking View All under Diagnostics displays the EWS Home page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/61200134
        """
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("diagnostics_title", direction="up")
        self.fc.fd["devicesDetailsMFE"].verify_diagnositcs_part()
        self.fc.fd["devicesDetailsMFE"].verify_diagnose_and_fix_item()
        self.fc.fd["devicesDetailsMFE"].verify_print_quality_tools_item()
        self.fc.fd["devicesDetailsMFE"].verify_diagnostics_view_all_item()

        # 1.The "Diagnose and Fix" screen should be displayed.
        self.fc.fd["devicesDetailsMFE"].click_diagnose_and_fix_btn()
        self.fc.fd["diagnosefix"].verify_diagnose_and_fix_screen()

        # 2.Clicking the Back button should navigate to the PDP screen.
        self.fc.fd["diagnosefix"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_diagnositcs_part()

        """ Simulator printer(8020/6100) doesn't support printer quality reports and EWS page."""
        # 3.Clicking Print Quality Tools should display the Print Quality Tools screen.
        self.fc.fd["devicesDetailsMFE"].click_print_quality_tools_btn()
        self.fc.fd["printersettings"].verify_print_quality_tools_page()
        self.fc.fd["printersettings"].verify_top_back_text()

        # 4.Clicking the Back button on the Print Quality Tools screen navigates to the PDP screen.
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_diagnositcs_part()

        # 5.Clicking View All under Diagnostics displays the EWS Home page.
        self.fc.fd["devicesDetailsMFE"].click_diagnostics_view_all_button()
        if self.fc.fd["printersettings"].verify_continuing_to_your_printer_settings_dialog():
            self.fc.fd["printersettings"].click_the_pin_ok_btn()
        self.fc.fd["printersettings"].verify_ews_page()
        self.fc.fd["printersettings"].verify_top_back_text()
        
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_diagnositcs_part()


    
