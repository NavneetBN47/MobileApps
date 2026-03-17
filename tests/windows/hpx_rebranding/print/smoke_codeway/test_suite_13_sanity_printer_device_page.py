import pytest
import logging
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_13_Sanity_Printer_Device_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.serial_number=cls.p.get_printer_information()["serial number"]
        cls.build_version = cls.driver.session_data["app_info"][pytest.app_info].split('_')[1]


    @pytest.mark.smoke
    def test_01_verify_printer_device_page_C44004362_C44025906(self):
        """
        Verify 'Device name' and 'Product name' should be displayed.
        Verify the 'Title' and the 'Position' in the printer device page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44004362
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44025906
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        assert self.fc.fd["devicesDetailsMFE"].verfiy_hpx_title() == "HP", "HP title does not display at the top bar"
        if self.stack not in ["rebrand_production"]:
            assert self.fc.fd["devicesDetailsMFE"].verfiy_hpx_version_on_title() == self.build_version, "App version mismatch"
        else:
            logging.info(f"Skipping version verification on production stack")
    
    @pytest.mark.smoke
    def test_02_verify_all_tiles_C44209592_C44209660_C44210169_C44210312_C57351442(self):
        """
        Verify the "Tile's" in the printer device page.
        Verify the 'Scan' tile.
        Verify the 'Print PDFs' tile.
        Verify the 'Print Photos' tile.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44209592
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44209660
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44210169
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44210312
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/57351442
        """
        self.fc.fd["devicesDetailsMFE"].verify_scan_tile()
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()
        self.fc.fd["devicesDetailsMFE"].verify_all_tiles_printer_device_page(check_flag=False)

    @pytest.mark.smoke
    def test_03_check_product_information_card_serial_number_C44223739(self):
        """
        Verify the 'Serial number' in the product information card.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44223739
        """
        self.fc.fd["devicesDetailsMFE"].verify_serial_number_info(self.serial_number)

    @pytest.mark.smoke
    def test_04_check_product_information_card_printer_name_C44223740(self):
        """
        Verify the 'Printer name' in the product information card

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44223740
        """
        self.fc.fd["devicesDetailsMFE"].verify_network_discovery_name_info(self.printer_name)

    @pytest.mark.smoke
    def test_05_verify_scan_functionality_C44209689(self):
        """
        Verify the 'Scan' functionality.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44209689
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

    @pytest.mark.smoke
    def test_06_verify_print_photos_functionality_C44223649(self):
        """
        Verify the 'Print Photos' functionality.	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44223649
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.FISH_PNG, w_const.TEST_DATA.FISH_PNG_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.smoke
    def test_07_verify_print_pdfs_functionality_C44210305(self):
        """
        Verify the 'Print PDFs' functionality.	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44210305
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)