import pytest
from time import sleep
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_02_Potg_Optimized_Printer(object):
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

        Verify printer shows on main ui with a cloud icon
        Verify print shows the remote print UI
        Verify Print Settings shows limited tabs.

        https://hp-testrail.external.hp.com/index.php?/cases/view/24313600
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878721
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        sleep(2)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.home.select_navbar_back_btn()
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        sleep(5)
        check_event_list = ['"optimizedConnectivity":false', '"programLevel":"HpPlus"']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

        self.fc.check_task_scheduler()
        self.fc.verify_hp_smart_driver_install()

    def test_02_switch_both_toggles_turn_on(self):
        """
        "Allow printing from Anywhere" toggle: ON
        "Require Private Pickup" toggle: ON      
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.printer_settings.select_print_anywhere()
        self.printer_settings.verify_print_anywhere_screen()
        self.printer_settings.switch_private_pickup_toggle(toggle='on')
        self.printer_settings.switch_printing_anywhere_toggle(toggle='on')
        self.home.select_navbar_back_btn()

    def test_03_check_potg_dialog_not_dispaly(self):
        """
        Leave and come back to home.

        Verify POTG enablement dialog does not show immediately after the printer is added.
        Verify POTG enablement dialog shows after user left and return to home page.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/27960507
        """
        assert self.home.verify_print_anywhere_dialog(raise_e=False) is False
        self.fc.enable_print_anywhere_dialog()

    def test_04_click_optimized_printer_btn(self):
        """
        Click "Optimized Printer" button on the Optimize dialog.

        Verify POTG optimize dialog with "Updating settings..." display first.
        Verify the WebView that introduce what print anywhere is shows after the dialog disappear.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27894571 (#5)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27894565 (#5)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27894567 (#5)
        """
        self.home.select_paw_optimize_printers_btn()
        self.home.verify_paw_updating_settings_text()
        self.printer_settings.verify_how_to_use_paw_screen()
        self.printer_settings.select_next_button()
        self.printer_settings.verify_how_to_use_private_pickup_screen()
        self.printer_settings.select_next_button()
        self.printer_settings.verify_you_are_ready_to_paw_screen()
        self.printer_settings.select_done_button()
        self.home.verify_printer_add_to_carousel()

        check_event_list = ['"optimizedConnectivity":true', '"programLevel":"HpPlus"']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_05_close_and_relaunch_app(self):
        """
        Wait the WebView that introduce what print anywhere is shows display.
        Go back to Main UI.
        Go to other screen and then go back to Main UI.
        Close the App and then relaunch it.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27894572
        """
        self.home.select_navbar_back_btn()
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False
