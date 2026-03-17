import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_03_Potg_Check_Updating_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        """
        Printer is remote
        Printer has Smart Driver capability
        Printer is not optimized
        Computer does not have smart driver installed
        User is HP+/UCDE
        """
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

    def test_01_sign_in_to_add_a_remote_printer(self):
        """
        Add the remote printer
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_02_click_optimize_printers_btn(self):
        """
        Click "Optimized Printer" button on the Optimize dialog.
        Wait Optimize dialog with "Updating setting..." screen display.
        Click "x" button.

        Verify the Optimize dialog disappear.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28256395
        """
        self.fc.enable_print_anywhere_dialog()
        self.home.select_paw_optimize_printers_btn()
        self.home.select_navbar_back_btn()
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False