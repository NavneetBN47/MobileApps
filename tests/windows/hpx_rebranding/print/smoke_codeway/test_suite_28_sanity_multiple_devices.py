import pytest
import logging
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "HPX"
class Test_Suite_28_Sanity_Multiple_Devices(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
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
        delete_simulator_printer(cls.ip2, cls.serial_number2)


    @pytest.mark.smoke
    def test_01_add_multi_printers_on_printer_card_C53430270_C53430211(self):
        """
        Ensure that the selected printer's details are accurately displayed on the Printer Device Page.
        The selected printer's details should be displayed correctly on the Printer Device Page in HPX.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53430270
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/53430211

        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.product_number = self.fc.get_printer_info_from_xml_file()[self.serial_number]['ProductNumber']
        
        self.fc.add_a_printer(self.p2)
        self.product_number2 = self.fc.get_printer_info_from_xml_file()[self.serial_number2]['ProductNumber']

        printers = [
            (self.printer_name, self.product_number, self.serial_number),
            (self.printer_name2, self.product_number2, self.serial_number2)
        ]

        for printer_name, product_number, serial_number in printers:
            logging.info(f"Start to verify printer details for: {printer_name}")
            self.fc.fd["devicesMFE"].click_windows_dummy_printer(printer_name)
            self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(printer_name)
            self.fc.fd["devicesDetailsMFE"].verify_all_tiles_printer_device_page(check_flag=False)
            self.fc.fd["devicesDetailsMFE"].verify_printer_settings_part()
            self.fc.fd["devicesDetailsMFE"].verify_settings_view_all_item()
            self.fc.fd["devicesDetailsMFE"].verify_product_number_info(product_number)
            self.fc.fd["devicesDetailsMFE"].verify_serial_number_info(serial_number)
            self.fc.fd["devicesDetailsMFE"].verify_network_discovery_name_info(printer_name)
            self.fc.fd["devicesDetailsMFE"].verify_warranty_status_info()
            self.fc.fd["devicesDetailsMFE"].verify_more_info_and_reports_info()
            self.fc.fd["devicesDetailsMFE"].click_top_back_btn()

    @pytest.mark.smoke
    def test_02_add_multi_printers_on_printer_card_C53336322(self):
        """
        The scan and print functionalities should work correctly for all printers in HPX

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53336322
        Failed with HPXG-4076.
        
        """
        self._test_printer_features(self.printer_name)
        self._test_printer_features(self.printer_name2)


    def _test_printer_features(self, printer_name):
        """
        Perform scan/import for both printers.
        """
        logging.info(f"Start to check Scan/Print function for: {printer_name}")
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(printer_name)
        self._scan_import_function()
        # Perform print PDF and photos for both printers.
        self._print_pdf_and_photos(printer_name)

    def _scan_import_function(self):
        """Verify the scan and import functionality for both printers.
        """
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
        self.fc.check_files_exist(w_const.TEST_DATA.AUTUMN_JPG, w_const.TEST_DATA.AUTUMN_JPG_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()