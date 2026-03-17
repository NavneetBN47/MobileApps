import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Print_Pdfs_File_Picker_Window(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_click_print_pdfs_tile_c43994680(self):
        """
        Click anywhere within the Print PDFs tile in printer device page.
        User should be able to click anywhere within the "Print PDFs" tile.      

        https://hp-testrail.external.hp.com/index.php?/cases/view/43994680
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_02_click_fp_outside_with_file_not_selected_c44253433(self):
        """
        In file picker window do not select the file.
        Then click on outside the file picker window.
        File picker window should not be closed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253433
        """
        self.fc.fd["devicesMFE"].click_myhp_window()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_03_check_minimize_maximize_close_button_c44253435(self):
        """
        Verify the screen, when user clicks on "<-Device Name/back", minimize, maximize and close button in the HPX app from "Print PDFs" screen
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253435
        """
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_maximize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_close_btn()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_04_close_fp_dialog_with_file_not_selected_c43999482(self):
        """
        In file picker opening screen click on Close button.
        User should be able to Close the file picker opening screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43999482
        """
        self.fc.fd["print"].select_file_picker_dialog_close_btn()
        assert self.fc.fd["print"].verify_file_picker_dialog(raise_e=False) is False

    @pytest.mark.regression
    def test_05_close_fp_dialog_with_file_not_selected_c44253431(self):
        """
        In file picker window do not select the Pdf file.
        Then click on close button.
        File picker window should be closed, and user should be navigated to the printer device page.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253431
        """
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.regression
    def test_06_able_to_select_pdf_file_c44247537(self):
        """
        Click on Print PDFs tile in printer device page.
        In file picker window select PDF file.
        User should be able to select the PDF file in file picker window.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44247537
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF, press_enter=False)

    @pytest.mark.regression
    def test_07_click_fp_outside_with_file_selected_c44253432(self):
        """
        In file picker window screen select Pdf file.
        Then click on outside the file picker window.
        File picker window should not be closed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253432
        """
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_maximize_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["devicesMFE"].click_top_close_btn()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_08_close_fp_dialog_with_file_selected_c44253408(self):
        """
        In file picker window screen select the Pdf file.
        Then click on close button.
        File picker window should be closed and user should be navigated to the printer device page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44253408
        """
        self.fc.fd["print"].select_file_picker_dialog_close_btn()
        assert self.fc.fd["print"].verify_file_picker_dialog(raise_e=False) is False
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.regression
    def test_09_click_fp_cancel_btn_with_file_not_selected_c44253407(self):
        """
        In file picker window do not select the file.
        Then click on cancel button.
        File picker window should be closed, and user should be navigated to the printer device page.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253407
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.fd["print"].select_file_picker_dialog_cancel_btn()
        assert self.fc.fd["print"].verify_file_picker_dialog(raise_e=False) is False
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_10_select_non_pdf_file_c44253699(self):
        """
        Click on print PDFs tile in printer device page.
        Verify the file picker window.
        Non-PDF file format "Ex: JPG, JPEG, Png, .bmp" should not be displayed in file picker window screen.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/44253699
        """
        file_list = ['*.jpg', '*.jpeg', '*.png', '*.bmp'] 
        self.fc.fd["print"].expand_all_files_combo(expand=True)
        for file in file_list: 
            assert self.fc.fd["print"].verify_files_format(file) is False
        self.fc.fd["print"].expand_all_files_combo(expand=False)

    @pytest.mark.regression
    def test_11_select_multi_pdf_files_c44256169(self):
        """
        In file picker window select multiple PDF files.
        Observe the file picker window.
        User should not be able to select multiple PDF files in file picker window.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44256169
        """
        self.fc.fd["print"].input_file_name('"' + w_const.TEST_DATA.COLOR_PDF + '"' + '"' + w_const.TEST_DATA.GREEN_PDF + '"') 
        self.fc.fd["print"].verify_simple_print_dialog()
        assert self.fc.fd["print"].get_total_page_num() == 8
    
    @pytest.mark.regression
    def test_12_close_simple_print_dialog(self):
        """
        Close the driver window screen
        """
        if self.fc.fd["print"].verify_simple_print_dialog(raise_e=False):
            self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
            self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
