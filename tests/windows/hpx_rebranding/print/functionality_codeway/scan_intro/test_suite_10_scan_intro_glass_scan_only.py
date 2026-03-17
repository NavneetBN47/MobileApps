import pytest
from time import sleep
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_10_Scan_Intro_Glass_Scan_Only(object):
    printer_profile = "HP Envy 6100e series"

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_custom_printer_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_custom_printer_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_scan_intro_screen_with_glass_only_C43738401_C43738431(self):
        """
        [Basic Scan]Scan intro Screen with Scanner Glass only printer UI
        Run a scan with a printer that only has a glass bed, verify scan is successful and can be saved

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738401
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738431
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Please retest with a printer that support Glass scan only")

        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].GLASS
        assert self.fc.fd["scan"].get_scan_presets_value() == self.fc.fd["scan"].PHOTO
        assert self.fc.fd["scan"].get_scan_area_value() == self.fc.fd["scan"].ENTIRE_SCAN_AREA
        assert self.fc.fd["scan"].get_scan_output_value() == self.fc.fd["scan"].COLOR
        assert self.fc.fd["scan"].get_scan_resolution_value() == self.fc.fd["scan"].DPI_300
        self.fc.fd["scan"].verify_detect_edges_item()
        self.fc.fd["scan"].verify_preview_button()

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)
        
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        logging.info(f"Saved Path: {file_path}")
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + file_path)


