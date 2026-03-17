import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.resources.const.ios.const import TEST_DATA
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_09_Shortcuts_Execution(object):
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
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061575
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13755128
        """
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
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
        self.shortcuts.click_email_toggle()
        self.shortcuts.enter_email_receiver(email_address)
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)

    def test_02_check_start_shortcut_screen(self):
        """
        Click on 3 vertical dotes on a Shortcut on Shortcut home screen to bring flyout menu.
        Click on "Start" from the flyout menu to execute the flow
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061544
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29151281
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061546
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061575
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29106081
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13943218
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061566(To do since GOTH-23126)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29202912 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061567
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
        self.scan.click_print_dialog_print_btn()
        if self.scan.verify_hp_smart_printing_dialog(raise_e=False):
            self.scan.click_hp_printing_print_btn()
        self.scan.verify_your_shortcut_dialog()
