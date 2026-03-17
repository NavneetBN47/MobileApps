import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import WebDriverException

pytest.app_info = "GOTHAM"
class Test_Suite_01_Error_Con_Printer_Offline(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.printer_opt = {'printer_status':'ready'}

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")
        
        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_turn_off_printer_wireless(self):
        """
        An offline printer.
        Computer is network connected.
        """
        self.fc.trigger_printer_offline_status(self.p)
        if self.home.verify_carousel_printer_offline_status():
            self.printer_opt['printer_status'] = 'offline'
        
    def test_03_check_get_supplies_flow(self):
        """
        Click on Get Supplies/Ink tile

        Verify DSP-P2 page shows for II printer and DSP-Sure Supply page shows for Non-II printer.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16901192
        """
        if self.printer_opt['printer_status'] == 'offline':
            self.home.select_get_supplies_tile()

            if self.dedicated_supplies_page.verify_hp_instant_ink_page():
                self.dedicated_supplies_page.select_back_btn()

            else:
                self.web_driver.add_window("get_supplies")
                sleep(3)
                self.web_driver.switch_window("get_supplies")
                current_url = self.web_driver.get_current_url()
                if "hp.com" not in current_url and "hp-mns.com" not in current_url:
                    raise WebDriverException("The webpage shows incorrect")

                self.web_driver.set_size('min')

            self.home.verify_home_screen()

    def test_04_check_supply_status_flow(self):
        """
        Click on Printer Settings
        Click on Supply Status

        LEDM: Verify P2 page shows
        Non-LEDM: The DSP-Sure Supply page shows for Non-LEDM printer.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16901193
        """
        if self.printer_opt['printer_status'] == 'offline':
            sleep(5)
            self.home.select_printer_settings_tile()
            self.printer_settings.verify_printer_settings_page()
            sleep(2)
            self.printer_settings.select_supply_status_option()
            if self.printer_settings.verify_supply_status_page():
                self.home.select_navbar_back_btn()
            else:
                self.web_driver.add_window("supply_status_page")
                sleep(3)
                self.web_driver.switch_window("supply_status_page")
                sleep(3)
                current_url = self.web_driver.get_current_url()
                assert "hp.com" in current_url
                self.web_driver.set_size('min')
