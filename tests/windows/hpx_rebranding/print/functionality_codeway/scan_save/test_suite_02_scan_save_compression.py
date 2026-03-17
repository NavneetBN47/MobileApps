import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
import logging


pytest.app_info = "HPX"
class Test_Suite_02_Scan_Save_Compression(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.parametrize("compression", ["None", "Low", "Medium", "High"])
    @pytest.mark.regression
    def test_01_check_scan_save_compression_option_C43738421_C43738467(self, compression):
        """
        verify compression option while saving a scanned document
        select different Compression from Save flyout, verify user is able to select each

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738421
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738467
        """
        if compression == "None":
            self.fc.launch_hpx_to_home_page()
            self.fc.add_a_printer(self.p)
        else:
            self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=60)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()

        assert "None" == self.fc.fd["scan"].get_compression_dropdown_value()

        self.fc.fd["scan"].select_compression_listitem(compression)
        logging.info(f"Saved Compression set to: {compression}")

        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        logging.info(f"Saved Path: {file_path}")
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + file_path)

