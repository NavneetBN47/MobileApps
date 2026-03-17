import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_02_Print_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_simple_print_dialog(self):
        """
        Click "Print Photo" tile on main UI, verify native dialog shows
        Load a photo to print, verify print preview shows in the native print dialog
        Print photo locally, verify output and that Simple PDF Print dialog is received
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585496
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585497
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585498
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585500
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064333
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14087476
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27894499
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.select_print_photos_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=120)
            self.home.select_success_printer_installed_ok_btn()
            self.home.verify_home_screen()
            
            self.home.select_print_photos_tile()
        
        self.print.verify_file_picker_dialog()
        
        self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.verify_simple_photo_print_dialog()

    def test_02_check_native_dialog_settings(self):
        """
        View the value in the dropdown on native dialog, verify settings show correctly 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585499
        """
        self.print.verify_orientation_setting()
        self.print.verify_paper_size_setting()
        self.print.verify_photo_size_setting()
        self.print.verify_select_a_layout_setting()
        self.print.verify_borderless_printing_setting()
        self.print.verify_scaling_setting()
        self.print.verify_paper_type_setting()
        self.print.verify_output_quality_setting()

        self.print.change_orientation_setting(w_const.ORIENTATION.LANDSCAPE)

    def test_03_check_more_settings_link(self):
        """
        Install only printer driver, verify more settings is working on native print dialog
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16890361
        """
        self.print.select_more_settings_link()
        self.print.verify_more_settings_menu_dialog()
        self.print.select_more_settings_menu_dialog_ok_btn()
        self.print.verify_more_settings_menu_dialog(invisible=True)

    def test_04_cancel_flow_on_simple_print_dialog(self):
        """
        Click "Cancel" on native print dialog, verify print job is cancelled

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585509
        """
        self.print.select_print_dialog_cancel_btn()
        assert self.print.verify_simple_print_dialog(raise_e=False) is False
        self.home.verify_home_screen()

    def test_05_print_multiple_photos(self):
        """
        Print photo via "Print Photos" tile on the main UI, verify Photo is printed
        Select multiple photos to print, verify print is successful
        Install only printer driver, verify user can send print job via print Photos/Print Documents
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12341709
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585511
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16890360

        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()

        self.print.input_file_name('"' + w_const.TEST_DATA.WOMAN_BMP + '"' + '"' + w_const.TEST_DATA.AUTUMN_JPG + '"')
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    @pytest.mark.parametrize("file_type", ["BMP", "JPG", "PNG", "JPEG", "CORRUPTED"])
    def test_06_print_different_supported_file_type(self, file_type):
        """
        Load different photos to print, verify print preview shows correctly
        Send print jobs with all supported file type, verify print is successful
        Load an error format file to print, verify proper error dialog shows
        Click "OK" button on "File format error" dialog, verify dialog is dismissed and main UI shows
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585501
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585505
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585506
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585510
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585512
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585513
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585522
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13281202

        """
        file_types = {"BMP": w_const.TEST_DATA.WOMAN_BMP,
                    "JPG": w_const.TEST_DATA.AUTUMN_JPG,
                    "PNG": w_const.TEST_DATA.FISH_PNG,
                    "JPEG": w_const.TEST_DATA.WORM_JPEG,
                    "CORRUPTED": w_const.TEST_DATA.CORRUPTED_JPEG}

        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()

        self.print.input_file_name(file_types[file_type])
        if file_type != "CORRUPTED":
            self.print.verify_simple_print_dialog()
            self.print.select_printer(self.hostname)
            self.print.select_print_dialog_print_btn()
            self.home.verify_home_screen(timeout=30)
        else:
            self.print.verify_file_format_error_dialog()
            self.print.select_dialog_ok_btn()
            self.home.verify_home_screen()
