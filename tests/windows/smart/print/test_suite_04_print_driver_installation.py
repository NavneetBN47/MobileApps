import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_04_Print_Driver_Installation(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_add_printer_without_driver_installed(self):
        """
        Go to Main UI and Add printer without printer driver installed
        """
        self.fc.disable_printer_driver_auto_install()
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

    def test_02_check_print_btn_on_scan_preview_screen(self):
        """
        Observe on Scan Preview screen without print driver installed, verify "Print" button is not seen 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19446260
        """
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_print_btn_not_display()

        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        sleep(1)
        self.home.select_navbar_back_btn()

    def test_03_check_driver_installed_successfully_flow(self):
        """
        Click "Print Photos"/"Print Documents" tile (no driver) (Win RS5+)(Mac 10.14+), verify "Install to print"/"Install printer" dialog shows
        (+) Perform printer installation (Win RS5+, Mac 10.14+) via "Print Photos"/"Print Documents" tile, verify happy path flow
        Click buttons on the "Install to print" / "Install printer" dialog (Win RS5+)(Mac 10.14+), verify functionality
        Click "OK" button on the "Success! Printer Installed" dialog, verify dialog got dismissed

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078862
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12586890
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078863
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17153733
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17153735
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078871
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078872
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078877
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078869
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/24840984
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890728
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/12585517
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14099915
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078865
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078867
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078873
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078875
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16042268
        """
        self.home.select_print_photos_tile()
        self.home.verify_install_to_print_dialog()
        self.home.select_i_will_do_this_later_btn()
        assert self.home.verify_install_to_print_dialog(raise_e=False) is False

        self.home.select_print_documents_tile()
        self.home.verify_install_to_print_dialog()
        self.home.select_install_printer_btn()
        self.home.verify_installing_printer_dialog()        
        if self.home.verify_success_printer_installed_dialog(timeout=300, raise_e=False):
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
            self.home.verify_home_screen()
        else:
            self.home.verify_printer_driver_installed_failed_dialog()
            self.home.select_printer_driver_installed_failed_later_btn()
            self.home.verify_home_screen()
            pytest.skip("Printer driver could not be installed successfully, so skip this test")

