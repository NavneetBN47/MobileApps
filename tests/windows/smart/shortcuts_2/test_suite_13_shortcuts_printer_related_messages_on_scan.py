import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_13_Shortcuts_printer_related_messages_on_scan(object):
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
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)

    def test_02_check_printer_problem_without_printer_driver(self):
        """
        Execute Shortcut (Print destination only) from Scan Preview screen or from 
        Shortcut home screen
        Execute Shortcut (Print destination + Email/Save destination) from 
        Scan Preview screen or from Shortcut home screen.
        Click "Cancel" button on the native Print dialog.
        Click "Skip Printing" button
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14511957
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14511963
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14511964
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14511967
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14511959(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14511965(low)
        """
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_start_icon()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_cancel_btn()
        self.scan.verify_problem_shortcut_dialog()
        self.scan.click_problem_shortcut_dialog_cancel_btn()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_shortcut_screen_for_win()
        self.shortcuts.click_email_toggle()
        self.shortcuts.enter_email_receiver(self.login_info["email"])
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen()
        self.shortcuts.click_start_shortcut_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_start_icon()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_cancel_btn()
        self.scan.verify_problem_shortcut_dialog(print_destination_only=False)
        self.scan.click_problem_shortcut_dialog_cancel_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_start_icon()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_cancel_btn()
        self.scan.verify_problem_shortcut_dialog(print_destination_only=False)
        self.scan.click_problem_shortcut_dialog_skip_printing_btn()
        self.scan.verify_your_shortcut_dialog()
