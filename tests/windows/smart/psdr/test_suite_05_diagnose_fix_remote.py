import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_05_Diagnose_Fix_Remote(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
     
        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_diagnose_fix_btn_disabled_with_remote_printer(self):
        """
        Remote printer must be added to the main UI
        check "Diagnose & Fix" icon on the navigation pane on Main UI (Win)/ Menu bar->Printers (Mac)
        Verify diagnose & Fix is grayed out

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419938
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_remote_printer()
        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()
        self.home.verify_carousel_printer_status_text(timeout=120)
        self.home.verify_carousel_printer_security_text()
        assert self.home.verify_diagnose_and_fix_btn(raise_e=False) is False
