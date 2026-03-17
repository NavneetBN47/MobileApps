import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_Potg_Learn_More_With_Shared_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", shared=True)

    def test_01_add_a_shared_printer(self):
        """
        Launch Device Picker to add the shared printer.
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        self.fc.restart_hp_smart()
        check_event_list = ['"optimizedConnectivity":false', '"programLevel":"HpPlus"']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_02_click_learn_more_btn(self):
        """
        Wait the Optimize dialog with "Learn More" button screen display.
        Click the "Learn More" button on the user version of optimizing dialog.

        Verify POTG web view launched.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28217254
        https://hp-testrail.external.hp.com/index.php?/cases/view/28217257  (#1)
        """
        self.fc.enable_print_anywhere_dialog()
        self.home.select_paw_learn_more_btn()
        self.printer_settings.verify_print_anywhere_screen()

    def test_03_close_and_relaunch_app(self):
        """
        Go back to Main UI.
        Go to other screen and then go back to Main UI.
        Close the App and then relaunch it.
        """
        self.home.select_navbar_back_btn()
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False
        self.fc.restart_hp_smart()
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False
  