import pytest
from time import sleep
import logging

from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_05_Print_Driver_Installation_Failed(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.sf = SystemFlow(cls.driver)
        cls.host_name = cls.p.get_printer_information()['host name']

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.system_preferences = cls.fc.fd["system_preferences"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_check_driver_installed_failed_flow(self):
        """
        (+) Perform printer installation (Win RS5+, Mac 10.14+) via "Print Photos"/"Print Documents" tile, verify the alternative(Manual) install flow
        (+) Click buttons on "There was a problem during installation..." dialog, verify functionality
        (RS5/higher)Click "Print Photos"/"Print Documents" on the Main UI(PSDr fail case), verify "There was a problem during installation.." dialog shows when PSDr fails
        [RS5/higher] Follow the instructions on the "There was a problem during installation..." dialog, verify printer added successfully.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078870
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17153872
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14062596
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16042271
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078882
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/17153897
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14062590
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16048655
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14062591
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078881
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15078878
        """
        self.fc.disable_printer_driver_auto_install()
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        try:
            self.home.select_print_documents_tile()
            self.home.verify_install_to_print_dialog()
            
            self.p.pp_module._power_off()
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()

            self.home.verify_printer_driver_installed_failed_dialog(timeout=300)
            self.home.verify_printer_driver_installed_failed_later_btn()
            self.home.select_printer_driver_installed_failed_later_btn()
            assert self.home.verify_printer_driver_installed_failed_dialog(raise_e=False) is False

            self.home.select_print_documents_tile()
            self.home.verify_install_to_print_dialog()
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_printer_driver_installed_failed_dialog(timeout=300)
            self.home.select_printer_driver_installed_failed_printers_scanners_btn()

            self.driver.ssh.send_command("taskkill /f /im SystemSettings.exe")

            self.home.verify_printer_driver_installed_failed_close_btn()
            assert self.home.verify_printer_driver_installed_failed_later_btn(raise_e=False) is False        
            self.home.select_printer_driver_installed_failed_close_btn()
            assert self.home.verify_printer_driver_installed_failed_dialog(raise_e=False) is False
            self.home.verify_home_screen()

        except NoSuchElementException as e:
            raise NoSuchElementException("Failed to check Print driver installed failed flow...")

        finally:
            self.p.pp_module._power_on()
