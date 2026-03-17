import pytest
import logging
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_02_Print_Pdfs_Simple_Pdf_Print(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.hostname = cls.p.get_printer_information()['serial number']

        
    @pytest.mark.regression
    def test_01_verify_selected_file_in_file_picker_window_c44253452(self):
        """
        Click on print PDFs tile
        In file picker window select pdf file to print.
        The selected file should be displayed in the driver window preview screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253452
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF, press_enter=False)

    @pytest.mark.regression
    def test_02_go_to_simple_pdf_print_dialog_c44247570(self):
        """
        In file picker window, select PDF file.
        Then click on Open button.
        File picker window should be closed and user should be navigated to driver window opening screen.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44247570
        """
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()

    @pytest.mark.regression
    def test_03_add_printer_in_printer_dropdown_c44255490(self):
        """
        Verify the display of printer dropdown when the user selects the added printer in driver window.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44255490
        """
        self.fc.fd["print"].select_printer(self.hostname)

    @pytest.mark.regression
    def test_04_click_top_close_btn_c44253544(self):
        """
        In driver window screen click on minimize button.
        User should not be able to minimize the driver window screen.
        In driver window screen click on maximize button.
        User should not be able to maximize the driver window screen.
        In driver window screen click on Close button.
        User should not be able to Close the driver window screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253544
        """
        org_size = self.fc.fd["print"].get_simple_print_window_size()
        self.fc.fd["devicesMFE"].click_top_maximize_btn()
        max_size = self.fc.fd["print"].get_simple_print_window_size()
        assert org_size == max_size
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        min_size = self.fc.fd["print"].get_simple_print_window_size()
        assert org_size == min_size
        self.fc.fd["devicesMFE"].click_top_close_btn()
        self.fc.fd["print"].verify_simple_print_dialog()

    @pytest.mark.regression
    def test_05_click_sp_outside_c44253698(self):
        """
        In driver windows screen click outside the driver settings screen.
        Driver window screen should not be closed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253698
        """
        self.fc.fd["devicesMFE"].click_myhp_window()
        self.fc.fd["print"].verify_simple_print_dialog()

    @pytest.mark.regression
    def test_06_go_to_sp_dialog_close_btn_c44253570(self):
        """
        Click on close button of driver settings screen.
        User should be able to close the driver settings.
        User should be navigated to printer device page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253570
        """
        self.fc.fd["print"].select_simple_print_dialog_close_btn()
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.regression
    def test_07_select_diff_pdf_file_and_print_c44253700(self):
        """       
        Verify the functionality of "Print PDF" tile, when user prints the PDF file with different file size.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253700
        """
        pdf_list = [w_const.TEST_DATA.TEST_30KB_PDF, w_const.TEST_DATA.TEST_260KB_PDF, w_const.TEST_DATA.TEST_1MB_PDF, w_const.TEST_DATA.TEST_3MB_PDF]
        for pdf in pdf_list:
            self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
            self.fc.fd["print"].verify_file_picker_dialog()
            self.fc.fd["print"].input_file_name(pdf)
            logging.info("pdf file: {}".format(pdf))
            self.fc.fd["print"].verify_simple_print_dialog()
            self.fc.fd["print"].select_printer(self.hostname)
            self.fc.fd["print"].select_simple_print_dialog_print_btn(del_file=False)
            self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)

    @pytest.mark.regression
    def test_08_del_print_output_file(self):
        """
        Delete print output files
        """
        self.fc.close_myHP()
        self.fc.fd["print"].del_print_output_file()
