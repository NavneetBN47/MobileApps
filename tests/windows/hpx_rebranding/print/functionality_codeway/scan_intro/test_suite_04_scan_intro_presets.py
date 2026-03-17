import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_04_Scan_Intro_Presets(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.adf_scan_support = {}

        
    @pytest.mark.regression
    def test_01_check_presets_glass_C43738407(self):
        """
        Select source to Scanner glass, verify Presets/Advance Presets value can be change and changes are reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738407
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        # Verify Advance Presets is set to "Photo" option by default.
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.adf_scan_support['status'] = True
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].GLASS)
        else:
            self.adf_scan_support['status'] = False
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].GLASS
        assert self.fc.fd["scan"].get_scan_presets_value() == self.fc.fd["scan"].PHOTO

    # More Advanced Presets (Multi-Item, Book, ID Card) need to be added after the feature implement
    @pytest.mark.parametrize("glass_presets", ["Photo", "Documents"])
    @pytest.mark.regression
    def test_02_check_preview_and_scan_glass_C43738407(self, glass_presets):
        """
        Select source to Scanner glass, verify Presets/Advance Presets value can be change and changes are reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738407
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, glass_presets)
        assert self.fc.fd["scan"].get_scan_presets_value() == glass_presets

        self.fc.fd["scan"].click_preview_btn()
        # self.fc.fd["scan"].verify_previewing_screen()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].verify_scanner_preview_screen()

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

    @pytest.mark.regression
    def test_03_check_presets_adf_C43738409(self):
        """
        Select source to Document Feeder, verify different Presets/Advance Presets value can be selected and reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738409
        """
        if not self.adf_scan_support['status']:
            pytest.skip("Test printer does not support ADF scan, please retest with a different printer again!")
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        # Verify Advance Presets is set to "Document" option by default.
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        assert self.fc.fd["scan"].get_scan_presets_value() == self.fc.fd["scan"].DOCUMENTS

    @pytest.mark.parametrize("adf_presets", ["Photo", "Documents"])
    @pytest.mark.regression
    def test_04_check_scan_adf_C43738409(self, adf_presets):
        """
        Select source to Document Feeder, verify different Presets/Advance Presets value can be selected and reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738409
        """
        if not self.adf_scan_support['status']:
            pytest.skip("Test printer does not support ADF scan, please retest with a different printer again!")
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF

        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, adf_presets)
        assert self.fc.fd["scan"].get_scan_presets_value() == adf_presets

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)


