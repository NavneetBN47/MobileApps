import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import random
from time import sleep
import logging


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_10_Sanity_Scan_E2E_Flow_2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_happy_path_scan_edit_print_C43738393(self):
        """
        [Happy path] Scan, edit and then print. 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738393
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.go_through_flow_to_scanner_screen()
        self.__randomize_scanner_source()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.__randomize_scan_pages()
        self.__randomize_edit_image()

        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.printer_name)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.smoke
    def test_02_happy_path_scan_edit_share_C43738394(self):
        """
        [Happy path] Scan, edit and then share.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738394
        """
        self.fc.restart_hpx()
        self.go_through_flow_to_scanner_screen()
        self.__randomize_scanner_source()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.__randomize_scan_pages()
        self.__randomize_edit_image()

        self.__scan_share_flow()

    @pytest.mark.smoke
    def test_03_happy_path_scan_edit_save_pdf_C43738396(self):
        """
        [Happy path] Scan and import, edit and then save/share/print.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738396
        """
        self.fc.restart_hpx()
        self.go_through_flow_to_scanner_screen()

        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_markup_item()
        self.fc.fd["scan"].verify_edit_makup_setting_screen()
        self.fc.fd["scan"].click_red_pen_btn()
        self.fc.fd["scan"].click_edit_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        self.__scan_save_flow(file_type=self.fc.fd["scan"].BASIC_PDF)

        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.printer_name)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        self.__scan_share_flow()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def go_through_flow_to_scanner_screen(self):
        """
        Go through flow to Scanner Intro screen from Device card screen.
        """
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()

    def __randomize_scanner_source(self):
        """
        Randomize the scanner sources to be: Scanner Glass, or Document Feeder if applicable.
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            source_list = [self.fc.fd["scan"].ADF, self.fc.fd["scan"].GLASS]
            random_source = random.choice(source_list)
            logging.info("Scanner Source: {}".format(random_source))
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, random_source)

    def __randomize_scan_pages(self):
        """
        Randomize the number of scan jobs to be: 1, or 2-10, or 10 plus.
        job_num: 1, or 2-10, or 10 plus
        """
        scan_pages_list = [1, random.randint(2, 10), random.randint(11, 13)]
        random_scan_pages = random.choice(scan_pages_list)
        logging.info("Scan Pages: {}".format(random_scan_pages))
            
        if random_scan_pages == 1:
            self.fc.fd["scan"].verify_preview_with_single_image()
        else:
            for _ in range(random_scan_pages-1):
                self.fc.fd["scan"].click_add_pages_btn()
                self.fc.fd["scan"].verify_scan_btn()
                self.fc.fd["scan"].click_scan_btn()
                self.fc.fd["scan"].verify_scan_result_screen()
            assert self.fc.fd["scan"].get_scan_job_num() == random_scan_pages

    def __randomize_edit_image(self):
        """
        Randomize crop item from Edit screen.
        """
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        crop_list = ['Custom', 'Letter', 'Square', 'A4', '5:7', '4:6', '3.5:5']
        random_crop = random.choice(crop_list)
        logging.info("Edit Crop: {}".format(random_crop))
        self.fc.fd["scan"].click_crop_item_btn(random_crop)
        sleep(1)
        self.fc.fd["scan"].click_edit_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    def __randomize_file_type(self):
        """
        Randomize file type for Save and Share dialog.
        """
        file_type_list = [self.fc.fd["scan"].BASIC_PDF, self.fc.fd["scan"].IMAGE_JPG]
        random_file_type = random.choice(file_type_list)
        logging.info("File Type: {}".format(random_file_type))
        self.fc.fd["scan"].select_file_type_listitem(random_file_type)

    def __randomize_compression(self):
        """
        Randomize compression for the PDF\image file(s).
        """
        compression_list = ["None", "Low", "Medium", "High"]
        random_compression = random.choice(compression_list)
        logging.info("Compression: {}".format(random_compression))
        self.fc.fd["scan"].select_compression_listitem(random_compression)

    def __scan_share_flow(self):
        """
        Share flow from Scan Preview screen.
        """
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.__randomize_file_type()
        self.__randomize_compression()
        self.fc.fd["scan"].click_dialog_share_btn()
        self.fc.fd["scan"].verify_share_picker_popup()
        self.fc.fd["scan"].dismiss_share_picker_popup()
        self.fc.fd["scan"].verify_share_picker_popup(invisible=True)

    def __scan_save_flow(self, file_type):
        """
        Save flow from Scan Preview screen.
        """
        if self.fc.fd["scan"].verify_thumbnail_icon(raise_e=False):
            multi_scans = True
        else:
            multi_scans = False
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        logging.info(f"Selected File Type: {file_type}")
        self.fc.fd["scan"].select_file_type_listitem(file_type)

        self.__randomize_compression()

        # Review the saved file.
        if multi_scans and file_type == self.fc.fd["scan"].IMAGE_JPG:
            multi_files = True
        else:
            multi_files = False
        self.__review_saved_file(multi_files)

    def __review_saved_file(self, multi_files):
        """
        Review the saved file.
        """
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(3)
        if multi_files:
            self.fc.fd["scan"].enter_folder_save_path(w_const.TEST_DATA.PICTURE_FOLDER_PATH)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name, multi_files)
        logging.info("Saved Path: {}".format(file_path))
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("Remove-Item -Path {} -Force -Recurse".format(file_path), timeout=30)

  