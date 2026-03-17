import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_Advance_Settings_Offline(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer = cls.fc.fd["printers"]
        cls.ews = cls.fc.fd["ews"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        cls.driver.ssh.send_command('Remove-PrinterDriver -Name "HP*"')

    def test_01_check_ews_with_offline_printer(self):
        """
        Go to "Advance Settings" with an offline applicable printer, verify "Can't open printer home or EWS page" dialog displays 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541075
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541076
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()

        self.p.pp_module._power_off()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_cant_open_ews_dialog()

    def test_02_click_ok_btn(self):
        """
        Click OK button on the "Can't open printer home or EWS page" dialog, verify the user navigates to the main UI with the offline applicable printer.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541078
        """
        self.ews.click_cant_open_ews_dialog_ok_btn()
        self.home.verify_home_screen()
        if not self.home.verify_carousel_finish_setup_btn(raise_e=False):
            self.home.verify_carousel_printer_offline_status()
        else:
            self.home.verify_carousel_finish_setup_subtitle()
            self.home.verify_get_support_btn()

    def test_03_turn_printer_on(self):
        """
        Turn on Printer
        """
        self.p.pp_module._power_on()
        if not self.home.verify_carousel_finish_setup_subtitle(raise_e=False):
            self.home.verify_carousel_printer_offline_status(timeout=120, invisible=True)
        else:
            self.home.verify_get_support_btn(invisible=True)
            self.home.verify_carousel_finish_setup_btn()

    def test_04_click_back_btn(self):
        """
        Click back icon on top left corner of the Gotham app when the "Can't open printer home or EWS page" display, verify Home page shows

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541079
        """
        self.home.select_printer_settings_tile()
        if self.printer.verify_pin_dialog(raise_e=False) is not False:
            if self.printer.input_pin(self.p.get_pin()) is True:
                self.printer.select_pin_dialog_submit_btn()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_advanced_settings_item()

        self.p.pp_module._power_off()
        self.printer_settings.select_advanced_settings_item()
        self.ews.verify_cant_open_ews_dialog()

        self.home.select_navbar_back_btn()

    def test_05_turn_printer_on(self):
        """
        Turn on Printer
        """
        self.p.pp_module._power_on()
        