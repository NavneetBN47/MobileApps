import pytest
import logging
import random
from time import sleep
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_02_Sanity_Scan_Intro(object):
    printer_profile = "HP OfficeJet Pro 9130b Series"

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_custom_printer_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_custom_printer_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.adf_scan_support = {}

        
    @pytest.mark.smoke
    def test_01_verify_scanner_intro_screen_C43738429(self):
        """
        Click on the 'Import' hyperlink on the Scan Intro page and verify that the Import flow is initiated.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738429
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scanner_screen(timeout=30)
        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.adf_scan_support['status'] = False
            logging.info("Selected printer does not support ADF scan.")
        else:
            self.adf_scan_support['status'] = True
            logging.info("Selected printer supports ADF scan.")

        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.fd["scan"].select_file_picker_dialog_cancel_btn()

    @pytest.mark.smoke
    def test_02_verify_reset_settings_btn_C43738419(self):
        """
        Click "Reset Settings", verify the functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738419
        """
        self.fc.fd["scan"].verify_scanner_screen(timeout=30)
        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)
        original_scan_settings = self.fc.fd["scan"].get_all_scan_settings()

        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_150)
        sleep(1)
        self.fc.fd["scan"].verify_reset_settings_btn()
        updated_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        assert updated_scan_settings != original_scan_settings

        self.fc.fd["scan"].click_reset_settings_btn()
        scan_settings_after_reset = self.fc.fd["scan"].get_all_scan_settings()
        assert scan_settings_after_reset == original_scan_settings

        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)

    @pytest.mark.smoke
    def test_03_verify_adf_2_sided_scan_C43738405(self):
        """
        Run a scan jobs with ADF 2-sided supported printer, verify scan job is successful

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738405
        """
        self.fc.fd["scan"].verify_scanner_screen(timeout=30)
        if not self.adf_scan_support['status']:
            pytest.skip("Skip this test case as selected printer does not support ADF scan.")
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        if not self.fc.fd["scan"].verify_2_sided_item(raise_e=False):
            pytest.skip("Printer does not support ADF 2 Sided scan")
        self.fc.fd["scan"].verify_2_sided_checkbox_status()
        self.fc.fd["scan"].click_2_sided_item()
        self.fc.fd["scan"].verify_2_sided_checkbox_status(off=False)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

    @pytest.mark.smoke
    def test_04_check_scan_save_C43738430(self):
        """
        Run a scan with a printer that has both glass bed and document feeder, verify scan is successful and can be saved

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738430
        """
        if self.fc.fd["scan"].verify_scan_result_screen(timeout=10, raise_e=False):
            self.fc.fd["scan"].click_back_arrow()
            self.fc.fd["scan"].verify_exit_without_saving_dialog()
            self.fc.fd["scan"].click_yes_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if self.adf_scan_support['status']:
            source_list = [self.fc.fd["scan"].GLASS, self.fc.fd["scan"].ADF]
            set_source = random.choice(source_list)
            logging.info("Scanner Source: {}".format(set_source))
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, set_source)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=2)

        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        type_list = [self.fc.fd["scan"].IMAGE_JPG, self.fc.fd["scan"].BASIC_PDF]
        set_type = random.choice(type_list)
        self.fc.fd["scan"].select_file_type_listitem(set_type)
        sleep(2)
        self.fc.fd["scan"].click_dialog_save_btn()
        if self.fc.fd["scan"].IMAGE_JPG == self.fc.fd["scan"].get_file_type():
            multi_i = True
            self.fc.fd["scan"].enter_folder_save_path(w_const.TEST_DATA.PICTURE_FOLDER_PATH)
        else:
            multi_i = False

        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()

        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name, multi_i=multi_i)
        logging.info("Saved Path: {}".format(file_path))
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("Remove-Item -Path {} -Force -Recurse".format(file_path))
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

    @pytest.mark.smoke
    @pytest.mark.parametrize("source, output", [("Scanner Glass", "Color"), ("Scanner Glass", "Grayscale"), ("Document Feeder", "Color"), ("Document Feeder", "Grayscale")])
    def test_05_check_output_C43738420(self, source, output):
        """
        Select Output type from dropdown, verify values can be changed and changes are reflected in scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738420
        """
        if not self.adf_scan_support['status'] and source == self.fc.fd["scan"].ADF:
            pytest.skip("Skip this test case as selected printer does not support ADF scan.")
        if self.adf_scan_support['status']:
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, source)
        assert self.fc.fd["scan"].get_scan_source_value() == source
        logging.info(f"Scan Source set to: {source}")
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].OUTPUT, output)
        assert self.fc.fd["scan"].get_scan_output_value() == output
        logging.info(f"Scan Output set to: {output}")

        if source == self.fc.fd["scan"].GLASS:
            self.fc.fd["scan"].click_preview_btn()
            self.fc.fd["scan"].verify_previewing_screen(raise_e=False)
            self.fc.fd["scan"].verify_scan_btn(timeout=30)
            self.fc.fd["scan"].verify_scanner_preview_screen()

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_yes_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
