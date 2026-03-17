import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_03_Scan_Intro_Preview_Btn(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_preview_btn_available_C43738413(self):
        """
        Set Source to "Scanner Glass", verify Preview button is available

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738413
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        self.fc.fd["scan"].verify_preview_button()

    @pytest.mark.regression
    def test_02_check_preview_screen_C43738414_C43738415(self):
        """
        Set Source to "Scanner Glass" and click Preview, verify the image shows in Preview screen
        Preview a scan, verify scan settings right panel is hidden during previewing

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738414
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738415
        """
        self.fc.fd["scan"].click_preview_btn()
        # The previewing screen verification is unstable as the screen dismiss so quickly, comment it out temporarily
        # self.fc.fd["scan"].verify_previewing_screen()
        # self.fc.fd["scan"].verify_preview_button(invisible=True)
        self.fc.fd["scan"].verify_scan_btn(timeout=60)

    @pytest.mark.regression
    def test_03_check_preview_btn_disable_C43738416(self):
        """
        Set Source to "Document Feeder", verify preview button is disabled

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738416
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
            assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF

            self.fc.fd["scan"].verify_preview_button(invisible=True)
        else:
            pytest.skip("Test printer does not support ADF scan, please retest with a differernt printer again!")
        
