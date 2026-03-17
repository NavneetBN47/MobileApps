import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Potg_Check_Smart_Driver_Awareness(object):
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

    def test_02_click_opt_x_btn_and_check(self):
        """
        Wait Optimize dialog display.
        Click "X" button on the Optimize dialog.
        Go to other screen and go back Main UI.
        Close the app and then relaunch it.
        Go to other screen and go back Main UI.

        Verify the POTG optimize dialog doesn't show again after cancel it.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27975158
        """
        self.fc.enable_print_anywhere_dialog()
        self.home.select_paw_x_btn()
        assert self.home.verify_print_anywhere_dialog(raise_e=False) is False
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()
        assert self.home.verify_print_anywhere_dialog(raise_e=False) is False    

    def test_03_restart_app_to_check_sd_awareness(self):
        """
        Close POTG optimize dialog with "Optimize Printers" button if it pops up.
        Use the app without closing it
        Restart app
        Go to any other page and land back on the Main UI

        POTG optimize dialog with "Optimize Printers" button will show if the "Optimize Printers" button is not clicked for the account.
        Verify Smart Driver awareness modal is only displayed after app was restarted.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28716337
        https://hp-testrail.external.hp.com/index.php?/cases/view/28564484
        https://hp-testrail.external.hp.com/index.php?/cases/view/28716342
        """
        self.fc.restart_hp_smart()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()
        assert self.home.verify_print_anywhere_dialog(raise_e=False) is False
        self.home.verify_smart_driver_dialog()

    def test_04_click_sd_x_button_and_check(self):
        """
        Dismiss the modal by clicking on the x icon
        Leave and return to home page
        Verify Smart driver awareness modal doesn't show again.
        https://hp-testrail.external.hp.com/index.php?/cases/view/28716338

        Close and relaunch the app
        Go to other page and land on the Main UI again
        Verify Smart driver awareness modal shows again after coming back to the Main page.
        https://hp-testrail.external.hp.com/index.php?/cases/view/28800009
        """
        self.home.click_smart_driver_x_btn()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()
        assert self.home.verify_smart_driver_dialog(raise_e=False) is False
        self.fc.restart_hp_smart()
        self.home.verify_smart_driver_dialog()

    def test_05_click_install_smart_printing_driver_button_and_check(self):
        """
        click "install smart printing driver" button on modal
        Accept UAC

        Verify Smart driver installs within a few min
        Verify Smart driver awareness modal does not show either case.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28716339
        https://hp-testrail.external.hp.com/index.php?/cases/view/28716341
        """
        self.home.click_install_smart_printing_driver_btn()
        sleep(180)
        assert self.fc.verify_hp_smart_driver_install() is True
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.home.select_navbar_back_btn()
        assert self.home.verify_smart_driver_dialog(raise_e=False) is False
        self.fc.restart_hp_smart()
        assert self.home.verify_smart_driver_dialog(raise_e=False) is False
