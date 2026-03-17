import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import time

pytest.app_info = "GOTHAM"
class Test_Suite_17_Scanner_Problem_dialog(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)


    def test_01_go_to_scanner_screen(self):
        """
        Go to scanner screen.
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.verify_scanner_screen()

    def test_02_check_error_dialog_with_offline_printer(self):
        """
        Click the "Scan" button.
        Once the printer starts scanning, disconnect printer power          
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639467
        """
        self.scan.click_scan_btn()
        time.sleep(3)
        self.fc.trigger_printer_offline_status(self.p)
        self.scan.verify_scanner_problem_dialog()

    @pytest.mark.parametrize("buttons", ["close", "return_home", "get_more_help"])
    def test_03_check_each_button_on_scanner_not_found_dialog(self, buttons):
        """
        Click the "x" button.
        Click the "Get More Help" button
        Click the "Return Home" button
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639467
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639473
        """
        if buttons == "close":
            self.scan.click_scan_canceled_x_btn()
            self.fc.restore_printer_online_status(self.p)
        elif buttons == "return_home":
            self.scan.click_return_home_btn()
            self.home.verify_home_screen()
            self.fc.restore_printer_online_status(self.p)
            self.home.select_scan_tile()
        else:
            self.scan.click_get_more_help_btn()
            self.home.verify_help_and_support_page()
            self.fc.restore_printer_online_status(self.p)
            self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        time.sleep(1)
        self.fc.trigger_printer_offline_status(self.p)
        self.scan.verify_scanner_problem_dialog()  

    def test_04_click_scan_button_with_fix_error(self):
        """
        Reconnect printer power and then make sure printer in idle status
        Click the "Scan" button.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639468
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29639474
        """
        time.sleep(5)
        self.fc.restore_printer_online_status(self.p)
        self.scan.click_scan_canceled_x_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        