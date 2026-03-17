import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from SAF.misc import saf_misc
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "GOTHAM"
class Test_Suite_22_Shortcuts_printer_related_messages_offline_printer_2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status, clear_shortcuts_jobs):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=True)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

    def test_01_create_job(self):
        """
        Create new shortcut job
        """
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.fc.trigger_printer_offline_status(self.p)
        self.home.verify_carousel_printer_offline_status()
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
        
    def test_02_check_printer_problem_with_offline_printer(self):
        """
        Add a printer to main UI and make it goes offline.
        Execute Shortcut (Print destination + Email/Save destination) from Scan Preview screen or from Shortcut home screen.
        Verify the "Printer is offline" dialog shows with "Cancel" and "Skip Printing" button.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419919
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419922
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419920(low)
        """
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.shortcuts.verify_printer_offline_dialog()
        self.shortcuts.click_dialog_cancel_btn()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        self.shortcuts.verify_printer_offline_dialog()
        self.shortcuts.click_skip_printing_btn()
        self.scan.click_get_started_btn(timeout=30)
        self.scan.verify_scanning_unavailable_screen()

    def test_03_connect_wifi(self):
        self.fc.restore_printer_online_status(self.p)
