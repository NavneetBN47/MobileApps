import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_02_Scan_Share_Compression(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)       
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_scan_share_compression_option_C43738693(self):
        """
        Select different Compression from Share flyout, verify user is able to select each

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738693
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=60)
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()

        assert "None" == self.fc.fd["scan"].get_compression_dropdown_value()

        self.fc.fd["scan"].select_compression_listitem("Low")
        logging.info(f"Saved Compression set to: Low")

        self.fc.fd["scan"].select_compression_listitem("Medium")
        logging.info(f"Saved Compression set to: Medium")

        self.fc.fd["scan"].select_compression_listitem("High")
        logging.info(f"Saved Compression set to: High")
