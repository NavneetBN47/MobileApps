import pytest
import datetime
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Scan_Import(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_verify_scan_intro_page_C49106794(self):
        """
        Verify the scan intro page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/49106794
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile() 
        self.fc.fd["scan"].verify_scanner_screen(timeout=30)

    @pytest.mark.regression
    def test_02_verify_default_setting_scan_intro_page_C49108279(self):
        """
        Verify the default settings in the scan into page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/49108279
        """
        self.fc.fd["scan"].click_reset_settings_btn()
        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)
        expected_scan_settings = [self.fc.fd["scan"].GLASS, self.fc.fd["scan"].PHOTO, self.fc.fd["scan"].ENTIRE_SCAN_AREA, self.fc.fd["scan"].COLOR, self.fc.fd["scan"].DPI_300]
        default_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        assert default_scan_settings == expected_scan_settings

    @pytest.mark.regression
    def test_03_import_file_C48412690_C48469764(self):
        """
        Verify user can import file and verify the detect edges default option.
        Verify the user can import file and change the detect edges options .

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48412690
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/48469764
        """
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["scan"].verify_detecting_edges_screen()
        self.fc.fd["scan"].verify_import_screen()
        select = self.fc.fd["hpx_rebranding_common"].compare_image_diff("import_screen_auto_group", folder_n="scan", image_n="select_auto.png")
        assert select < 0.05
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_04_import_and_save_C48471773(self):
        """
        Import the file, edit and then save to default setting .

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48471773
        """
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        # Get current date from remote Windows machine
        formatted_date = self.driver.ssh.send_command("Get-Date -Format 'yyyy-MM-dd_'")["stdout"].strip()
        assert formatted_date in file_name
        self.fc.fd["scan"].click_dialog_save_btn()
        assert file_name in self.fc.fd["scan"].get_save_as_dialog_current_file_name()
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        #delete file
        self.driver.ssh.send_command("del " + file_path)
    
    @pytest.mark.regression
    def test_05_click_replace_btn_after_import_C48412691(self):
        """
        Verify the replace button behavior after importing a file from the import hyperlink text

        TestRails ->https://hp-testrail.external.hp.com/index.php?/cases/view/48412691
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()
        self.fc.fd["scan"].click_image_replace_btn()
        # HPXG-5601
        self.fc.fd["scan"].verify_replace_screen()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(timeout=180)
        self.fc.fd["scan"].verify_scan_result_screen()
