import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_02_Scan_E2E_Adf(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        # cls.hostname = cls.p.get_printer_information()['host name'][-6:]


    @pytest.mark.regression
    def test_01_go_to_scanner_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        
    @pytest.mark.regression
    def test_02_adf_scan_import_flow_c43738399(self):
        """
        Add adf scan e2e, Id print, files & photos flow, printer scan flow , camera scan flow

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738399
        """
        # Click on the scan tile.
        self.fc.fd["devicesDetailsMFE"].click_scan_tile() 
        self.fc.fd["scan"].verify_scan_btn()

        if self.fc.fd["scan"].verify_source_dropdown_enabled() is False:
            pytest.skip("ADF scan is not supported by the printer.")

        # Select the ADF option.
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF

        # Load documents into the ADF.
        # Start the scan job.
        # Verify that the preview screen is displayed with the scanned documents.
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)      
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # save
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        flie_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + flie_path)

        # print
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        # self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # share
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.fc.fd["scan"].click_dialog_cancel_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
