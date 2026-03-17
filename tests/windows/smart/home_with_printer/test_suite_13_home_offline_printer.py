import pytest
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_13_Home_Offline_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_check_printer_card_with_offline_printer(self):
        """
        Disconnect the network/Turn off the printer, verify printer shows as offline
        Disconnect and reconnect the network, verify printer shows as online 
        Printer card with offline printer UI
        Make printer goes offline, wait 60 seconds, verify "Get Support" button shows on the printer card
        Make printer that is not setup complete goes offline, wait 60 seconds, verify "Finish Setup" button gets replaced by "Get Support" button on the printer card

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14757426
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14757431
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27563133
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890704
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28517130
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28517133
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28517134
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28517132
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32759526
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32755713
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32759527
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        if self.home.verify_carousel_estimated_supply_image(raise_e=False):
            printer_status_before = self.home.get_carousel_printer_status_text()
            try:
                self.fc.trigger_printer_offline_status(self.p)
                self.home.verify_carousel_printer_offline_status()
                self.home.verify_carousel_estimated_supply_image(invisible=True)
                self.home.verify_get_support_btn()

            finally:
                self.fc.restore_printer_online_status(self.p)

            self.home.verify_carousel_printer_offline_status(timeout=60, invisible=True)
            self.home.verify_get_support_btn(invisible=True)
            self.home.verify_carousel_estimated_supply_image(timeout=120)
            self.home.verify_carousel_printer_status(printer_status_before, timeout=60)
        else:
            self.home.verify_carousel_finish_setup_btn()

            self.fc.trigger_printer_offline_status(self.p)
            self.home.verify_carousel_printer_offline_status()
            self.home.verify_carousel_finish_setup_btn(invisible=True)
            self.home.verify_get_support_btn()

            self.fc.restore_printer_online_status(self.p)

            self.home.verify_carousel_printer_offline_status(timeout=60, invisible=True)
            self.home.verify_carousel_finish_setup_btn()
