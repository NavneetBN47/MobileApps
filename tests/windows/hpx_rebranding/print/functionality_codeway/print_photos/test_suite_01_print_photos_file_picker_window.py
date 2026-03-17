import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Print_Photos_File_Picker_Window(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_verify_print_photos_tile(self):
        """
        Verify the Print photos tile in Printer device page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_02_verify_file_picker_opening_screen_C44256245(self):
        """
        Verify the behavior of "Print Photos" tile, when user clicks anywhere within the tile.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44256245
        """  
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_03_click_close_btn_on_file_picker_opening_screen_C44258259(self):
        """
        click close button without selecting file in file picker window.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258259
        """  
        self.fc.fd["print"].select_file_picker_dialog_close_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_04_click_close_btn_on_file_picker_opening_screen_with_file_C44258130(self):
        """
        In file picker opening screen click on close button with selecting the file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258130
        """  
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP, press_enter=False)
        self.fc.fd["print"].select_file_picker_dialog_close_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_05_click_cancel_btn_on_file_picker_opening_screen_with_file_C44257557(self):
        """
        In file picker opening screen click on cancel button with selecting file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44257557
        """  
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP, press_enter=False)
        self.fc.fd["print"].select_file_picker_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_06_click_cancel_btn_on_file_picker_opening_screen_without_file_C44258128(self):
        """
        In file picker opening screen click on cancel button without selecting file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258128
        """  
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].select_file_picker_dialog_cancel_btn()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_07_click_select_photos_to_print_btn_on_file_picker_opening_screen_without_selecting_file_C44258551(self):
        """
        click select photos to print btn on file picker without selecting the file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44258551
        """  
        self.fc.fd["devicesDetailsMFE"].click_print_photos_tile()
        self.fc.fd["print"].select_file_picker_dialog_print_btn()
        self.fc.fd["print"].verify_file_picker_dialog()

    @pytest.mark.regression
    def test_08_select_file_on_file_picker_opening_screen_C44256891(self):
        """
        select file on file picker opening screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44256891
        """
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["print"].input_file_name(w_const.TEST_DATA.WOMAN_BMP, press_enter=False)
        self.fc.fd["print"].select_file_picker_dialog_cancel_btn()



