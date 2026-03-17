import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_Hide_Printer_Printer_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.username, cls.password = cls.login_info["email"], cls.login_info["password"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        

    def test_01_check_hide_printer_flow_not_sign_in(self):
        """
        Hide a printer from Printer settings (non- Owner version), verify flow
        Click Printer setting tile, verify "Hide Printer" shows under the "Manage" section
        Click "Hide Printer" option on the list view, verify Hide this printer screen shows on the detail view
        Click Hide This Printer button on the detail view , verify correct version of confirmation modal shows
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538511
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538518
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538519
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538506

        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_hide_printer_item()
        self.printer_settings.verify_hide_this_printer_screen()
        self.printer_settings.select_hide_this_printer_btn()
        self.home.verify_home_screen()
        assert self.home.verify_carousel_printer_image(timeout=10, raise_e=False) is False

    def test_02_check_hide_printer_flow_not_owner(self):
        """
        Hide a printer from Printer settings (non- Owner version), verify flow
        Click Printer setting tile, verify "Hide Printer" shows under the "Manage" section
        Click "Hide Printer" option on the list view, verify Hide this printer screen shows on the detail view
        Click Hide This Printer button on the detail view , verify correct version of confirmation modal shows
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538511
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538518
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538519
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29538506

        """
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.fc.sign_in(self.username, self.password)
        self.home.verify_home_screen(timeout=60)
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_hide_printer_item()
        self.printer_settings.verify_hide_this_printer_screen()
        self.printer_settings.select_hide_this_printer_btn()
        self.home.verify_home_screen()
        assert self.home.verify_carousel_printer_image(timeout=10, raise_e=False) is False

