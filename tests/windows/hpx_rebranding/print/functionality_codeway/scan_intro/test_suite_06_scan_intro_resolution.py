import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_06_Scan_Intro_Resolution(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_verify_scanner_intro_screen_C43738400(self):
        """
        [Basic Scan]Scan Intro UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738400
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scanner_screen(timeout=30)

    @pytest.mark.regression
    def test_02_check_glass_resolution_list_C43738425(self):
        """
        Check Resolution dropdown with Scanner Glass, verify only 5 possible dpi selections is available

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738425
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].GLASS)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].GLASS
        self.fc.fd["scan"].select_resolution_dropdown()
        self.fc.fd["scan"].verify_resolution_list_items()
        self.fc.fd["scan"].select_resolution_dropdown(close=True)

    @pytest.mark.parametrize("glass_dpi", ["75 dpi", "150 dpi", "300 dpi", "600 dpi", "1200 dpi"])
    @pytest.mark.regression
    def test_03_verify_glass_scan_resolution_C43738427(self, glass_dpi):
        """
        Run Scan with each supported Resolution, verify scan can be completed without any issue

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738427
        """
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, glass_dpi)
        assert glass_dpi == self.fc.fd["scan"].get_scan_resolution_value()
        self.fc.fd["scan"].click_scan_btn()
        if glass_dpi == self.fc.fd["scan"].DPI_1200:
            self.fc.fd["scan"].verify_scan_result_screen(timeout=300)
        else:
            self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_yes_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

    @pytest.mark.regression
    def test_04_check_adf_resolution_list_C43738426(self):
        """
        Check Resolution dropdown with ADF, verify only 3 possible dpi selections is available

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738426
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Test printer does not support ADF scan, please retest with a different printer again!")
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        self.fc.fd["scan"].select_resolution_dropdown()
        self.fc.fd["scan"].verify_resolution_list_items(glass_scan=False)
        self.fc.fd["scan"].select_resolution_dropdown(close=True)

    @pytest.mark.parametrize("adf_dpi", ["75 dpi", "150 dpi", "300 dpi"])
    @pytest.mark.regression
    def test_05_verify_adf_scan_resolution_C43738427(self, adf_dpi):
        """
        Run Scan with each supported Resolution, verify scan can be completed without any issue

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738427
        """
        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Test printer does not support ADF scan, please retest with a different printer again!")
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, adf_dpi)
        assert adf_dpi == self.fc.fd["scan"].get_scan_resolution_value()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_yes_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)