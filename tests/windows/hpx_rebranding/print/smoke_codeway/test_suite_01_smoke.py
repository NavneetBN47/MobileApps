import pytest
from time import sleep
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Smoke(object):
    printer_profile = "HP OfficeJet Pro 9130b Series"

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_custom_printer_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_custom_printer_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_verify_device_added_C44682366(self):
        """
        Verify the added device is listed in the Home page-Single Printer

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682366
        """
        self.fc.launch_hpx_to_home_page()
        assert self.fc.is_app_open() is True, "My HP App does not launch successfully!"
        self.fc.add_a_printer(self.p)

    @pytest.mark.smoke
    def test_02_verify_device_name_status_ink_levels_C44682367(self):
        """
        Verify the device name ,status and Ink levels are displayed properly-Single Printer 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682367
        """
        self.fc.fd["devicesMFE"].verify_supply_levels_card()

    @pytest.mark.smoke
    def test_03_verify_printer_device_page_C44682368(self):
        """
        Verify Printer Device Page displayed properly when device is selected

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682368
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
    
    @pytest.mark.smoke
    def test_04_verify_tiles_list_C44682369(self):
        """
        Verify the Printer Tiles are listed as expected

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682369
        """
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
        self.fc.fd["devicesDetailsMFE"].verify_scan_tile()
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()

    @pytest.mark.smoke
    def test_05_verify_top_back_btn_C44682370(self):
        """
        Verify the Back Button is navigating back to Home/Root screen 	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682370
        """
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
    
    @pytest.mark.smoke
    def test_06_verify_basic_flatbed_scan_C44682371(self):
        """
        Verify user able to perfom Basic Flatbed Scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682371
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scanner_screen(timeout=120)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

    @pytest.mark.smoke
    def test_07_verify_adf_scan_C48337792(self):
        """
        Verify User is able perform scan job using 'ADF'  	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48337792
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=120)
        if not self.fc.fd["scan"].verify_source_dropdown_enabled():
            pytest.skip("Printer does not support ADF Scan. NA this test case!")
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        sleep(1)
        # self.fc.fd["scan"].verify_scanner_screen(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

    @pytest.mark.smoke
    def test_08_verify_scan_import_C48841544(self):
        """
        Verify the user can import a file using the 'import button'.	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48841544
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=120)
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.FISH_PNG, w_const.TEST_DATA.FISH_PNG_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

    @pytest.mark.smoke
    def test_09_verify_print_photos_C44682372(self):
        """
        Verify user able to print photos	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682372
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.FISH_PNG, w_const.TEST_DATA.FISH_PNG_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.smoke
    def test_10_verify_print_pdf_C44682373(self):
        """
        Verify user able to print PDFs

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44682373
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)


