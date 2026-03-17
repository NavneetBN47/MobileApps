import pytest
from time import sleep

from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.ios.const import TEST_DATA


pytest.app_info = "GOTHAM"
class Test_Suite_16_Shortcuts_printer_related_messages_not_install_driver_2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, clear_shortcuts_jobs):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_create_job(self):
        """
        Create new shortcut job
        """
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        sleep(60)
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_email_toggle()
        self.shortcuts.enter_email_receiver(email_address)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)
        
    def test_02_check_printer_problem_without_printer_driver(self):
        """
       Execute Shortcut (Print destination + Email/Save destination) from Scan Preview screen or from Shortcut home screen screen.
       Verify the "Printer problem" dialog shows with "Return to Home", "Cancel" and "Skip Printing" buttons.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14103081
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14103094
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14103085(low)
        """
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.shortcuts.verify_printer_problem_dialog()
        self.shortcuts.click_dialog_cancel_btn()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.shortcuts.verify_printer_problem_dialog()
        self.shortcuts.click_skip_printing_btn()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_start_icon()
        self.scan.verify_your_shortcut_dialog()
        self.scan.click_home_btn()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.shortcuts.verify_printer_problem_dialog()
        self.shortcuts.click_dialog_return_to_home_btn()
        self.home.verify_install_to_print_dialog()

    def test_03_fix_issue_re_execute_shortcut(self):
        """
        Fix the print problem issue
        Verify the printer driver installed successfully.
        Verify the execution is successful.
        """
        self.home.select_install_printer_btn()
        self.home.verify_installing_printer_dialog()
        self.home.verify_success_printer_installed_dialog(timeout=300)
        self.home.select_success_printer_installed_ok_btn()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_start_icon()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_print_btn()
        if self.scan.verify_hp_smart_printing_dialog(raise_e=False):
            self.scan.click_hp_printing_print_btn()
        self.scan.verify_your_shortcut_dialog()
