import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Scan_Intro_Source(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_source_dropdown_C43738403(self):
        """
        Check Source dropdown on the Scan intro page with printer that supports (ADF+ Scanner glass), verify user is able to select the source

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738403
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Please retest with a printer that support Glass+ADF scan")
        self.fc.fd["scan"].select_source_dropdown()
        self.fc.fd["scan"].verify_source_list_items()

    @pytest.mark.regression
    def test_02_check_adf_two_sided_scan_C43738404(self):
        """
        Scan with ADF duplex supported printer, verify "2-Sided" checkbox is seen
        Verify the "2-Sided" checkbox is seen and not checked by default.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738404
        """
        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Please retest with a printer that support Glass+ADF scan")
        self.fc.fd["scan"].select_source_document_feeder()
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        
        if not self.fc.fd["scan"].verify_2_sided_item(raise_e=False):
            pytest.skip("Printer does not support ADF 2 Sided scan")
        else:
            self.fc.fd["scan"].verify_2_sided_checkbox_status()

    @pytest.mark.regression
    def test_03_check_detect_edges_checkbox_C43738406(self):
        """
        Select Source to Scanner Glass, verify "Detect Edges" checkbox is seen
        Verify "Detect Edges" checkbox is seen and not checked by default.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738406
        """
        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Please retest with a printer that support Glass+ADF scan")
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].GLASS)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].GLASS

        self.fc.fd["scan"].verify_detect_edges_item()
        assert self.fc.fd["scan"].verify_detect_edges_checkbox_status() == "0"

    @pytest.mark.regression
    def test_04_check_back_btn_shows_friendly_name_C43738428(self):
        """
        Verify Printer friendly name shows next to back arrow on scan intro page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738428
        """
        assert self.fc.fd["scan"].verify_back_arrow().text == "My Printer", "Back arrow text is not 'My Printer'"

    @pytest.mark.regression
    def test_05_click_back_btn_C43738412(self):
        """
        Click the back button on Scan Intro, verify arrow is clickable and user returns to Device detailed page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738412
        """
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)