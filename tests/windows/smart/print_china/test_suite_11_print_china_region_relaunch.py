import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "GOTHAM"
class Test_Suite_11_Print_China_Region_Relaunch(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]
        cls.sf = SystemFlow(cls.driver)

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

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
        Precondition
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

    def test_02_check_print_photos_functionality_china(self):
        """
        Change the region to China, Relaunch the app, Click on the Print Photos tile, verify Print Photos tile is unlocked 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777812
        """
        self.home.select_print_photos_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_success_printer_installed_dialog(timeout=120)
            self.home.select_success_printer_installed_ok_btn()
            self.home.verify_home_screen()
            self.home.select_print_photos_tile()

        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

        # Set pc region to China while HP Smart are on Main UI
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 45')

        self.fc.restart_hp_smart()
        self.home.verify_carousel_printer_image()


        self.home.select_print_photos_tile()
        assert self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen(raise_e=False) is False
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_03_check_print_documents_functionality_china(self):
        """
        Change the region to China, Relaunch the app, Click on the Print Documents tile, verify Print Documents tile is unlocked

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777811
        """
        self.home.select_print_documents_tile()
        
        assert self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen(raise_e=False) is False
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_04_check_print_functionality_hk(self):
        """
        Set region to HK Singapore, Check the Print Documents", "Print Photos" tiles, verify tiles are locked  	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777813
        """
        self.sf.change_pc_region_to_flip_region(104)

        self.fc.restart_hp_smart()
        self.home.verify_carousel_printer_image()

        self.home.select_print_photos_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

        self.home.select_print_documents_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

    def test_05_check_print_functionality_sgp(self):
        """
        Set region to HK Singapore, Check the Print Documents", "Print Photos" tiles, verify tiles are locked  	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777813
        """
        self.sf.change_pc_region_to_flip_region(215)

        self.fc.restart_hp_smart()
        self.home.verify_carousel_printer_image()

        self.home.select_print_photos_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

        self.home.select_print_documents_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
        self.home.verify_home_screen()

    def test_06_set_region_back_to_usa(self):
        self.sf.change_pc_region_to_us_region()