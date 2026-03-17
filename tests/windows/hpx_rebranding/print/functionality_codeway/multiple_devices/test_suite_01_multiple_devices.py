import pytest
from time import sleep
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "HPX"
class Test_Suite_01_Multiple_Devices(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]
        cls.ip = cls.p.get_printer_information()["ip address"]

        # Initializing Printer2
        cls.p2 = cls.fc.initialize_printer(printer_config="HP Envy 6100e series")
        cls.printer_name2 = cls.p2.get_printer_information()["model name"]
        cls.serial_number2 = cls.p2.get_printer_information()["serial number"]
        cls.ip2 = cls.p2.get_printer_information()["ip address"]

        yield
        # Cleanup simulator printer2 after all tests in the class complete
        delete_simulator_printer(cls.ip2, cls.serial_number2)

    @pytest.mark.regression
    def test_01_add_multiple_printers(self):
        """
        Add multiple printers to the application.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.add_a_printer(self.p2)

    @pytest.mark.regression
    def test_02_verify_scan_import_and_print_features_C55106655_C53430154(self):
        """
        Add both printers, then verify scan/import and print PDF/photos for each printer.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/55106655
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/53430154
        """
        printers = [
            (self.p, self.printer_name),
            (self.p2, self.printer_name2)
        ]
        # Then verify scan/import and print features for each printer
        for _, printer_name in printers:
            self._scan_import_function(printer_name)
            self._print_pdf_and_photos(printer_name)

    @pytest.mark.regression
    def test_03_verify_supply_gauge_icon_C58675870(self):
        """
        Verify the supply gauge icon functionality for both printers.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/58675870
        """
        printers = [
            (self.p, self.printer_name),
            (self.p2, self.printer_name2)
        ]
        for _, printer_name in printers:
            self._supply_guage_icon(printer_name)

    def _scan_import_function(self, printer_name):
        """Verify the scan and import functionality for both printers.
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()   
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=60)
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].click_dialog_save_btn()
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        self.fc.fd["scan"].click_dialog_close_btn()
        self.fc.fd["scan"].click_back_btn()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].click_dialog_save_btn()
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        self.fc.fd["scan"].click_dialog_close_btn()
        self.fc.fd["scan"].click_back_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()

    def _print_pdf_and_photos(self, printer_name):
        """
        Verify the print PDF and photos functionality.
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()

    def _supply_guage_icon(self, printer_name):
        """
        Verify the supply gauge icon functionality.
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(printer_name)
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie"]:
            self.fc.fd["devicesDetailsMFE"].click_supply_levels_link()
            if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10):
                self.fc.fd["printersettings"].click_top_back_arrow()
            else:
                self.web_driver.add_window_and_switch("supply_levels")
                sleep(2)
                current_url = self.web_driver.get_current_url()
                assert "https://www.hp.com/" in current_url
                sleep(2)
                self.web_driver.set_size('min')
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()
