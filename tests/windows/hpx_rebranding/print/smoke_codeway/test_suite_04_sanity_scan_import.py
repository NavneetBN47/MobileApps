import pytest
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_04_Sanity_Scan_Import(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_check_file_picker_open_C48412688(self):
        """
        Verify the 'import' functionality from the scan intro screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48412688
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile() 
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()

    @pytest.mark.smoke
    def test_02_check_detect_edge_screen_C48468026(self):
        """
        Verify the user can import a file using the 'import' hyperlink text.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48468026
        """
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["scan"].verify_import_screen()

    @pytest.mark.smoke
    def test_03_import_edit_save_to_basic_pdf_C48471764(self):
        """
        Import the file, edit and then save to "Basic PDF"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48471764
        """
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_adjust_item()
        self.fc.fd["scan"].change_adjust_contrast_edit_value("50")
        self.fc.fd["scan"].click_edit_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        sleep(1)
        self.fc.fd["scan"].select_file_type_listitem(self.fc.fd["scan"].BASIC_PDF)
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("Remove-Item -Path {} -Force -Recurse".format(file_path))
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.smoke
    def test_04_verify_file_format_error_C48412692(self):
        """
        Verify the "File format error" pop up when invalid file is imported
 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48412692
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.CORRUPTED_JPEG, w_const.TEST_DATA.CORRUPTED_JPEG_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.CORRUPTED_JPEG)
        self.fc.fd["scan"].verify_file_format_error_dialog()
        self.fc.fd["scan"].click_file_format_error_close_btn()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.smoke
    def test_05_turn_on_auto_ori_and_check_image_rotated_C53532695(self):
        """
        Auto-orientation on, Verify the image is rotated in preview screen

        TestRails ->https://hp-testrail.external.hp.com/index.php?/cases/view/53532695
        """
        self.fc.fd["scan"].select_auto_enhancement_icon()
        self.fc.fd["scan"].verify_auto_enhancement_panel()
        sleep(5)
        assert self.fc.fd["scan"].verify_auto_orientation_state() == '0'
        self.fc.fd["scan"].click_auto_orientation_toggle()
        assert self.fc.fd["scan"].verify_auto_orientation_state() == '1'

        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.INVERTED_JPG, w_const.TEST_DATA.INVERTED_JPG_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.INVERTED_JPG)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        auto_ori_rotate = self.fc.fd["hpx_rebranding_common"].compare_image_diff("body_area", folder_n="scan", image_n="auto_ori_rotate.png", pre=True)
        assert auto_ori_rotate < 0.1

    @pytest.mark.smoke
    def test_06_verify_add_scan_C43738622(self):
        """
        Click '+ Add', verify user is taken to Scan screen and able to add more scans
 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738622
        """
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=2)

