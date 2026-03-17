import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
import re


pytest.app_info = "HPX"
class Test_Suite_03_Scan_Save_File_Name(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)       
        cls.printer_name = cls.p.get_printer_information()["model name"]

        cls.files = {"photo" : w_const.TEST_DATA.AUTUMN_JPG,
                     "doc" : w_const.TEST_DATA.Document_JPG, 
                     "receipt" :w_const.TEST_DATA.RECEIPT_PNG,
                     "business" :w_const.TEST_DATA.BUSINESSCARD_JPG,
                     "hand" :w_const.TEST_DATA.HANDWRITTEN_JPG
                       }

        cls.files_path = {"photo_path" : w_const.TEST_DATA.AUTUMN_JPG_PATH,
                     "doc_path" : w_const.TEST_DATA.Document_JPG_PATH, 
                     "receipt_path" :w_const.TEST_DATA.RECEIPT_PNG_PATH,
                     "business_path" :w_const.TEST_DATA.BUSINESSCARD_JPG_PATH,
                     "hand_path" :w_const.TEST_DATA.HANDWRITTEN_JPG_PATH
                       }

        
    @pytest.mark.regression
    def test_01_go_to_scan_intro_screen(self):
        """
        Scan intro screen display 
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

    test_options = [("photo", "photo_path"),
                ("doc", "doc_path"),
                ("receipt", "receipt_path"),
                ("business", "business_path"),
                ("hand", "hand_path")]
    @pytest.mark.parametrize("file, file_path", test_options)
    @pytest.mark.regression
    def test_02_scan_a_file_to_check_file_name_text_c43738464(self, file, file_path):
        """
        Check File Name Text box from Save flyout, verify correct file name shows

        Scan a Photo image and then click "Save" button on "Preview" screen to check File Name Text box from Save flyout.
        Scan a Document file and check File Name from Save flyout.
        Scan a Receipt file and check File Name from Save flyout.
        Scan a BusinessCard and check File Name from Save flyout.
        Scan a Handwritten file and check File Name from Save flyout.

        Verify "Photo_YYYY-MM-DD_HHMMSS" shows when first file is image.
        Verify "Document_YYYY-MM-DD_HHMMSS" shows when first file is Document.
        Verify "Receipt_YYYY-MM-DD_HHMMSS" shows when first file is receipt.
        Verify "BusinessCard_YYYY-MM-DD_HHMMSS" shows when first file is DocumentBusiness card
        Verify "Handwritten_YYYY-MM-DD_HHMMSS" shows when first file is Handwritten file.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738464 (a file)
        """
        self.fc.check_files_exist(self.files[file], self.files_path[file_path])
        self.__scan_file_and_check_file_name_text(self.files[file], add=False)

    test_options = [("photo", "photo_path"),
                ("doc", "doc_path"),
                ("receipt", "receipt_path"),
                ("business", "business_path"),
                ("hand", "hand_path")]
    @pytest.mark.parametrize("file, file_path", test_options)
    @pytest.mark.regression
    def test_03_scan_mixed_files_to_check_file_name_text_c43738464(self, file, file_path):
        """
        Check File Name Text box from Save flyout, verify correct file name shows

        Scan mixed files, and the first file is Photo image, check File Name from Save flyout.
        Scan mixed files, and the first file is Document file, check File Name from Save flyout.
        Scan mixed files, and the first file is Receipt file, check File Name from Save flyout.
        Scan mixed files, and the first file is BusinessCard, check File Name from Save flyout.
        Scan mixed files, and the first file is handwritten file, check File Name from Save flyout.

        Verify "Photo_YYYY-MM-DD_HHMMSS" shows when first file is image.
        Verify "Document_YYYY-MM-DD_HHMMSS" shows when first file is Document.
        Verify "Receipt_YYYY-MM-DD_HHMMSS" shows when first file is receipt.
        Verify "BusinessCard_YYYY-MM-DD_HHMMSS" shows when first file is DocumentBusiness card
        Verify "Handwritten_YYYY-MM-DD_HHMMSS" shows when first file is Handwritten file.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738464 (mixed files)
        """
        self.fc.check_files_exist(self.files[file], self.files_path[file_path])
        self.__scan_file_and_check_file_name_text(self.files[file], add=True)

    def __scan_file_and_check_file_name_text(self, file, add=True):
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.fd["scan"].input_file_name(file)
        self.fc.fd["scan"].verify_import_screen()
        sleep(2)
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        if add == True:
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].select_import_text()
            self.fc.fd["scan"].verify_file_picker_dialog()
            self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
            self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
            self.fc.fd["scan"].verify_import_screen()
            sleep(2)
            self.fc.fd["scan"].click_import_full_option()
            self.fc.fd["scan"].click_import_done_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
            self.fc.fd["scan"].select_gallery_item('1')

        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()

        pattern = r'\d{4}-((0[1-9])|(1[0-2]))-(([0][1-9])|([1-2][0-9])|(3[0-1]))_\d{6}'
        if file == w_const.TEST_DATA.AUTUMN_JPG:
            start_s = 'Photo'
        elif file == w_const.TEST_DATA.Document_JPG:
            start_s = 'Document'
        elif file == w_const.TEST_DATA.RECEIPT_PNG:
            start_s = 'Receipt'
        elif file == w_const.TEST_DATA.BUSINESSCARD_JPG:
            start_s = 'BussinessCard'
        elif file == w_const.TEST_DATA.HANDWRITTEN_JPG:
            start_s = 'Handwritten'
        try:
            assert re.match('^{}_{}$'.format(start_s, pattern), file_name) is not None, "File name does not match expected pattern"
        finally:
            self.fc.fd["scan"].click_dialog_cancel_btn()
            sleep(2)
            self.fc.fd["scan"].click_back_arrow()
            self.fc.fd["scan"].verify_exit_without_saving_dialog()
            self.fc.fd["scan"].click_yes_btn()
            self.fc.fd["scan"].verify_scan_btn()


