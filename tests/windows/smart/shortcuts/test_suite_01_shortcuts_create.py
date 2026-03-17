import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_01_Shortcuts_Create(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, clear_shortcuts_jobs):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        
    def test_01_create_shortcuts_first_time(self):
        """
        Complete create shortcuts flow
        
        Verify Shortcut Saved screen with with "You just created a Shortcut!" and 
        1st time creating shortcut animation shows.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792460
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13453237   
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13755166
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13755127 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29136288
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792461
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17397950
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943205
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

    def test_02_create_secound_shortcut(self):
        """
        Complete create shortcuts flow
        
        Verify Shortcut Saved screen shows and non-1st time creating shortcut animation shows.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792464   
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29106044  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29142910
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29142906
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792463
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792465
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24336947
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24336949
        """
        self.shortcuts.click_home_btn()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_not_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_file_already_exists_dialog()
        self.shortcuts.click_already_exists_rename_btn()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_02)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen()
        self.shortcuts.click_home_btn()
        self.home.verify_home_screen()

    def test_03_shortcuts_order(self):
        """
        Click Scan tile and send a scan job to go to the Scan Preview screen.
        Check the order of the Shortcuts.
        Verify the order of the Shortcuts is consistent with each other. 
        Verify shortcuts are ordered with oldest first, newest last
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/29141315
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/29141316
        """
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog()
        self.scan.verify_shortcuts_order(w_const.TEST_TEXT.TEST_TEXT_01, w_const.TEST_TEXT.TEST_TEXT_02)

    def test_04_execute_shortcut(self):
        """
        Execute shortcut
        Go back to main after 1st shortcut execution is done
        Execute a different shortcut
        Check the execution results    
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/29215179
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_not_empty_shortcuts_screen()
        self.shortcuts.click_edits_more_option_btn()
        self.shortcuts.click_start_opt_btn()
        # self.scan.verify_scan_intro_page()
        # self.scan.click_get_started_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen() 
        self.scan.click_start_icon()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_print_btn()
        if self.scan.verify_hp_smart_printing_dialog(raise_e=False):
            self.scan.click_hp_printing_print_btn()
        self.scan.verify_your_shortcut_dialog()
        self.scan.click_home_btn()
        self.home.verify_home_screen()
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_edits_more_option_another_btn()
        self.shortcuts.click_start_opt_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_start_icon()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_print_btn()
        if self.scan.verify_hp_smart_printing_dialog(raise_e=False):
            self.scan.click_hp_printing_print_btn()
        self.scan.verify_your_shortcut_dialog()
        self.scan.click_home_btn()
        self.home.verify_home_screen()

    def test_05_check_shortcut_item_in_printer_settings(self):
        """
        Click on Printer Settings tile and check the Printer settings entries.   
        Verify "Shortcut" entry doesn't show
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/29149228
        -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943221
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_shortcuts_item(invisible=True)
            