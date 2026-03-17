import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_05_Hide_Printer_Main_UI_Offline(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    @pytest.mark.parametrize("login", ["no", "yes"])
    def test_01_check_hide_printer_flow(self, login):
        """
        Right click on printer in printer card (offline printer), select Hide Printer, verify the printer is removed from main UI
        1. User is not signed in + printer is not claimed
        2. User is signed in + printer is not claimed
        Printer status - Local
        Account level - UCDE
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388316
        """
        if login == "no":
            self.fc.go_home()
        else:
            self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
            self.fc.sign_in(self.login_info["email"], self.login_info["password"])
            self.home.verify_home_screen(timeout=60)

        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        try:
            self.fc.trigger_printer_offline_status(self.p)             
            self.home.verify_carousel_printer_offline_status()

            self.home.right_click_printer_carousel()
            self.home.verify_hide_printer_list_item_load()
            self.home.click_hide_printer_list_item()
            self.home.verify_hide_this_printer_dialog_load()
            self.home.click_hide_this_printer_dialog_hide_printer_btn()
            assert self.home.verify_carousel_printer_image(timeout=10, raise_e=False) is False

        finally:
            self.fc.restore_printer_online_status(self.p)