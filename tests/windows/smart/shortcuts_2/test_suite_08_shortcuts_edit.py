import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_08_Shortcuts_Edit(object):
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

    
        
    def test_01_create_shortcut(self):
        """
        Create new shortcut for test     
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
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_00)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)

    def test_02_check_edit_shortcut_screen(self):
        """
        Select a shortcut from home screen, click on 3 vertical dots, click on "Edit" -> 
        "Edit Shortcut" screen shows.
        Change some settings and save -> "Shortcut Saved" screen shows.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943319
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13762550
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943296 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943311
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943315 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943316
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943317
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29151295 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943318
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943297
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943301
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943312
        """
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_edit_btn()
        self.shortcuts.verify_edit_shortcut_screen_for_win()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.select_copies(copies_num=self.shortcuts.MULTIPLE_COPIES_BTN)
        self.shortcuts.select_tile_color(3)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen()
        self.shortcuts.click_start_shortcut_btn()
        self.scan.verify_scanner_screen()
