import pytest
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import random
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_01_Scan_E2E_Import(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        # cls.hostname = cls.p.get_printer_information()['host name'][-6:]


    @pytest.mark.regression
    def test_01_go_to_scanner_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile() 
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_02_import_randomize_to_save_share_print_c43738395(self):
        """
        Import and randomize the number of scan jobs to be: 1, or 2-10, or 10 plus.
        Randomize the image file types to import.
        Edit the scanned result(s).
        Randomize to save, share and print.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738395
        """
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        image_list = [
            {"file": w_const.TEST_DATA.WOMAN_BMP, "path": w_const.TEST_DATA.WOMAN_BMP_PATH},
            {"file": w_const.TEST_DATA.AUTUMN_JPG, "path": w_const.TEST_DATA.AUTUMN_JPG_PATH},
            {"file": w_const.TEST_DATA.FISH_PNG, "path": w_const.TEST_DATA.FISH_PNG_PATH},
            {"file": w_const.TEST_DATA.WORM_JPEG, "path": w_const.TEST_DATA.WORM_JPEG_PATH}
        ]
        image_info = random.choice(image_list)
        self.fc.check_files_exist(image_info["file"], image_info["path"])
        self.fc.fd["scan"].input_file_name(image_info["file"])
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # save
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        flie_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + flie_path)

        # print
        job_num = random.randint(2, 5)
        self.__randomize_the_import_job(job_num)
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        # self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # share
        job_num = random.randint(6, 11)
        self.__randomize_the_import_job(job_num)
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.fc.fd["scan"].click_dialog_cancel_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    def __randomize_the_import_job(self, job_num):
        """
        Import and randomize the number of scan jobs to be: 1, or 2-10, or 10 plus.
        Randomize the image file types to import.

        job_num: 1, or 2-10, or 10 plus
        """
        for _ in range(job_num):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].select_import_text()
            image_list = [
                {"file": w_const.TEST_DATA.WOMAN_BMP, "path": w_const.TEST_DATA.WOMAN_BMP_PATH},
                {"file": w_const.TEST_DATA.AUTUMN_JPG, "path": w_const.TEST_DATA.AUTUMN_JPG_PATH},
                {"file": w_const.TEST_DATA.FISH_PNG, "path": w_const.TEST_DATA.FISH_PNG_PATH},
                {"file": w_const.TEST_DATA.WORM_JPEG, "path": w_const.TEST_DATA.WORM_JPEG_PATH}
            ]
            image_info = random.choice(image_list)
            self.fc.check_files_exist(image_info["file"], image_info["path"])
            self.fc.fd["scan"].input_file_name(image_info["file"])  
            self.fc.fd["scan"].verify_import_screen()
            self.fc.fd["scan"].click_import_done_btn()
            self.fc.fd["scan"].verify_scan_result_screen()

