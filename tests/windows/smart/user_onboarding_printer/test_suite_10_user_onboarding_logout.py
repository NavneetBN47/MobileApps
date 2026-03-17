import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_10_User_Onboarding_Logout(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.username, cls.password = cls.login_info["email"], cls.login_info["password"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_add_a_printer(self):
        """
        Add a printer to carousel
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

    @pytest.mark.parametrize("tiles", ["scan", "print_documents", "print_photos"])
    def test_02_check_before_sign_in(self, tiles):
        """
        Install new app : After login and logout local printing/scanning becomes permanently available
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550536
        """
        if tiles == "scan":
            self.home.select_scan_tile()
        elif tiles == "print_documents":
            self.home.select_print_documents_tile()
        elif tiles == "print_photos":
            self.home.select_print_photos_tile()

        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

    def test_03_sign_in_account(self):
        self.fc.sign_in(self.username, self.password)
        self.home.verify_home_screen(timeout=60)

    @pytest.mark.parametrize("tiles", ["scan", "print_documents", "print_photos"])
    def test_04_check_after_sign_in(self, tiles):
        """
        Install new app : After login and logout local printing/scanning becomes permanently available
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550536
        """
        if tiles == "scan":
            self.home.select_scan_tile()
            self.scan.verify_new_scan_auto_enhancements_dialog(timeout=60)
            self.home.select_navbar_back_btn()

        elif tiles == "print_documents":
            self.home.select_print_documents_tile()
            if self.home.verify_install_to_print_dialog(raise_e=False):
                self.home.select_i_will_do_this_later_btn()
            else:
                self.print.verify_supported_document_file_types_dialog()
                self.home.select_navbar_back_btn()
            
        elif tiles == "print_photos":
            self.home.select_print_photos_tile()
            if self.home.verify_install_to_print_dialog(raise_e=False):
                self.home.select_i_will_do_this_later_btn()
            else:
                self.print.verify_file_picker_dialog()
                self.print.select_file_picker_dialog_cancel_btn()

        self.home.verify_home_screen()

    def test_05_sign_out_account(self):
        self.fc.sign_out()
        assert self.home.verify_logged_in() is False

    @pytest.mark.parametrize("tiles", ["scan", "print_documents", "print_photos"])
    def test_06_check_after_sign_out(self, tiles):
        """
        Install new app : After login and logout local printing/scanning becomes permanently available
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33550536
        """
        if tiles == "scan":
            self.home.select_scan_tile()
            self.scan.verify_scanner_screen()
            self.home.select_navbar_back_btn()

        elif tiles == "print_documents":
            self.home.select_print_documents_tile()
            if self.home.verify_install_to_print_dialog(raise_e=False):
                self.home.select_i_will_do_this_later_btn()
            else:
                self.print.verify_supported_document_file_types_dialog()
                self.home.select_navbar_back_btn()
            
        elif tiles == "print_photos":
            self.home.select_print_photos_tile()
            if self.home.verify_install_to_print_dialog(raise_e=False):
                self.home.select_i_will_do_this_later_btn()
            else:
                self.print.verify_file_picker_dialog()
                self.print.select_file_picker_dialog_cancel_btn()

        self.home.verify_home_screen()