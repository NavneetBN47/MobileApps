import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_03_Shortcuts_Create_Save_Only(object):
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


    def test_01_create_shortcuts_by_save_only(self):
        """
        Try enable different destinations to save a Shortcut.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792468   
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_empty_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_00)
        self.shortcuts.click_save_toggle()
        self.shortcuts.click_one_drive_checkbox()
        self.shortcuts.click_save_shortcut_btn()
        self.shortcuts.verify_shortcut_saved_screen(is_first_time=True)

    def test_02_execute_shortcut_no_printer_driver(self):
        """
        Click on Scan tile, navigate to Scan Preview
        Click on "Shortcut" button to bring up Shortcuts flyout
        Select the Shortcut with Save destination to execute the Shortcut 
        User should not be prompted with "Install to Print" dialogue
        User should be able to complete the execution flow.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16890380(To do since GOTH-23126)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16890382
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29202913
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
        self.scan.verify_your_shortcut_dialog()
     