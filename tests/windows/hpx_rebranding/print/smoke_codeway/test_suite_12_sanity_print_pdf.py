import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_12_Sanity_Print_PDF(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.serial_number=cls.p.get_printer_information()["serial number"]
        # cls.hostname = cls.p.get_printer_information()['host name'][-6:]


    @pytest.mark.smoke
    def test_01_check_print_pdfs_tile_C43994038(self):
        """
        Verify the display of "Print PDFs" tile in printer device page of HPX app.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43994038
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.smoke
    def test_02_check_file_picker_dialog_C43998689(self):
        """
        Verify the screen transition, when user clicks on "Print PDFs" tile.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43998689
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        # HPXAPPS-50260
        # self.fc.fd["devicesDetailsMFE"].verfiy_back_btn_text()

    @pytest.mark.smoke
    def test_03_check_file_picker_dialog_C44003634(self):
        """
        Verify the screen transition, after observing the file picker opening screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44003634
        """
        self.fc.fd["print"].verify_file_picker_dialog()
        # The "Print" and "Cancel" button on file picker screen can not be located
        # self.fc.fd["print"].verfiy_file_picker_dialog_buttons()

    @pytest.mark.smoke
    def test_04_click_print_btn_without_file_selected_C44253434(self):
        """
        Verify the file picker window, when user clicks on Print button without selecting the Pdf file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44253434
        """
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        self.fc.fd["print"].verify_file_picker_dialog()
        assert self.fc.fd["print"].verify_simple_print_dialog(raise_e=False) is False

    @pytest.mark.smoke
    def test_05_click_cancel_btn_on_file_picker_dialog_C44247597(self):
        """
        Verify the screen transition, when user clicks on cancel button after adding pdf file in file picker window.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44247597
        """
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF, press_enter=False)
        self.fc.fd["print"].select_file_picker_dialog_cancel_btn()
        assert self.fc.fd["print"].verify_file_picker_dialog(raise_e=False) is False
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.smoke
    def test_06_check_simple_pdf_print_dialog_C44247566(self):
        """
        Verify the screen transition, when user clicks on Print button after selecting a file in file picker window.
        File picker window should be closed and user should be navigated to driver window opening screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44247566
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF, press_enter=False)
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        # HPXAPPS-50260
        # self.fc.fd["devicesDetailsMFE"].verfiy_back_btn_text()
        assert self.fc.fd["print"].verify_file_picker_dialog(raise_e=False) is False
        self.fc.fd["print"].verify_simple_print_dialog()

    @pytest.mark.smoke
    def test_07_click_cancel_btn_on_simple_print_dialog_C44253542(self):
        """
        Verify the functionality of "Print PDFs" tile, when user click on cancel button in driver window screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44253542
        """
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()

    @pytest.mark.smoke
    def test_08_click_print_btn_on_simple_print_dialog_C44253541(self):
        """
        Verify the functionality of "Print PDFs" tile, when user clicks on print button in driver window screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44253541
        """
        self.fc.fd["devicesDetailsMFE"].click_print_pdfs_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.COLOR_PDF_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.serial_number)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()