import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_18_Scan_Multiple_Pages(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_Perform_multipe_scan_jobs(self):
        """
        Perform 6 or more scan jobs
        Check the Preview screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13227882
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_add_pages_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_multi_scan_btn()
        self.scan.verify_multi_pages_scan_result_screen()
        for _ in range(4):
            self.scan.click_multi_add_pages_btn()
            self.scan.verify_scanner_screen()
            self.scan.click_multi_scan_btn()
            self.scan.verify_multi_pages_scan_result_screen()
        self.scan.verify_pages_num_value('6 of 6')
        