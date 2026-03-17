import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_19_Shortcuts_printer_related_messages_remote_printer_1(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, clear_shortcuts_jobs):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
  
        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.printers = cls.fc.fd["printers"]
  
        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

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
        self.home.verify_home_screen()
        self.fc.select_a_remote_printer()
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
        
    def test_02_check_printer_problem_remote_printer(self):
        """
        Add a remote printer to main UI
        Execute Shortcut (Print destination only) from Scan Preview screen or from Shortcut home screen screen.
        Verify the "Printer problem" dialog shows with "Cancel" and "Return to Home" buttons.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14103128
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14103138
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14103129(low)
        """
        self.shortcuts.click_my_shortcuts_btn()     
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.shortcuts.verify_printer_problem_dialog("Print destination only")
        self.shortcuts.click_dialog_cancel_btn()
     