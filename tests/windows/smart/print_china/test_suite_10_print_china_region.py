import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow


pytest.app_info = "GOTHAM"
class Test_Suite_10_Print_China_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]
        cls.sf = SystemFlow(cls.driver)

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        
    def test_01_go_home_and_add_printer(self):
        """
        Check main UI with any fax supported printer, under non mobile fax supported regions, verify "Mobile Fax" tile is hidden on the main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24799563
        """
        # Set pc region to China before launch HP Smart.
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 45')

        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()
        # App goes to home page for china region according to GOTH-24919
        self.home.verify_home_screen()

        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        assert self.home.verify_mobile_fax_tile(raise_e=False) is False

    def test_02_check_print_photos_functionality_china(self):
        """
        Click the Print Photos tile when user is not signed in, verify user can print photos without sign in 	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777808
        """
        self.home.select_print_photos_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            if self.home.verify_success_printer_installed_dialog(timeout=120, raise_e=False):
                self.home.select_success_printer_installed_ok_btn()
                self.home.verify_home_screen()
                self.home.select_print_photos_tile()
            else:
                self.home.verify_printer_driver_installed_failed_dialog(timeout=300)
                self.home.select_printer_driver_installed_failed_later_btn()
                self.home.verify_home_screen()
                pytest.skip("Printer driver could not be installed successfully, so skip this test and please retest")

        assert self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen(raise_e=False) is False
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        
        if not self.print.verify_print_dialog_print_btn_enabled():
            self.print.select_print_dialog_cancel_btn()
            pytest.skip('Printer Configuration Issue: Please retest with another printer')
        else:
            self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_03_check_print_documents_functionality_china(self):
        """
        Click the Print Documents tile when user is not signed in, verify user can Print Documents without sign in 	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777809
        """
        self.home.select_print_documents_tile()
        assert self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen(raise_e=False) is False
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.GREEN_PDF)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        if not self.print.verify_print_dialog_print_btn_enabled():
            self.print.select_print_dialog_cancel_btn()
            pytest.skip('Printer Configuration Issue: Please retest with another printer')
        else:
            self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_04_set_region_back_to_usa(self):
        self.sf.change_pc_region_to_us_region()