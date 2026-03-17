import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_13_Print_Error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.printer_status = cls.p.get_printer_status()
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_sent_print_job_with_error_status(self):
        """
        The printer must be installed on the computer
        The printer must be added to the carousel
        Generate the error
        Verify print job is sent
        Verify print job is not printed if a blocking error.
        Verify print error shows on app main UI or printer status.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585507
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        if self.home.verify_carousel_finish_setup_btn(raise_e=False):
            pytest.skip("Skip this test as the selected printer does not suit for faking status")
        else:
            self.p.fake_action_door_open()
            self.home.verify_carousel_printer_status("Door Open", timeout=30)
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
            self.print.select_print_dialog_print_btn()
            self.home.verify_home_screen()
            self.home.verify_carousel_printer_status("Door Open", timeout=30)

    def test_02_fixed_error_status(self):
        """
        Fix the error
        Verify printer status shows ready on the main UI
        Verify Print job is resumed if the error is out of paper or cartridges missing
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585508
        """
        if self.home.verify_carousel_finish_setup_btn(raise_e=False):
            pytest.skip("Skip this test as the selected printer does not suit for faking status")
        else:
            self.p.fake_action_door_close()
            self.home.verify_carousel_printer_status(self.printer_status.capitalize(), timeout=30)
            self.home.select_print_photos_tile()
            self.print.verify_file_picker_dialog()
            self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
            self.print.verify_simple_print_dialog()
            self.print.select_printer(self.hostname)
            self.print.verify_simple_photo_print_dialog()
            self.print.select_print_dialog_print_btn()
            self.home.verify_home_screen()
            self.home.verify_carousel_printer_status(self.printer_status.capitalize(), timeout=30)



