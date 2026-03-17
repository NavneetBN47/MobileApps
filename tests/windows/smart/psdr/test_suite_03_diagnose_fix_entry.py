import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import NoSuchElementException
import MobileApps.resources.const.windows.const as w_const
from time import sleep


pytest.app_info = "GOTHAM"
class Test_Suite_03_Diagnose_Fix_Entry(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.help_support = cls.fc.fd["help_support"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
     
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.fc.go_home()
        cls.fc.sign_in(cls.login_info["email"], cls.login_info["password"])
        cls.fc.select_a_printer(cls.p)


    @pytest.mark.parametrize("buttons", ["exit", "continue"])
    def test_01_check_exit_diagnose_fix_dialog(self, buttons):
        """
        Click "Diagnose & Fix" icon on the navigation pane on Main UI (Win) -> verify "Diagnose & Fix" screen shows -> Diagnose and Fix screen shows with Start button
        Click 'Start' button to initiate Diagnose and Fix test
        Click back arrow (win) while Diagnose and Fix still processing
        Click "Continue" button on "Exit Diagnose and Fix?" dialog
        Click "Exit" button on "Exit Diagnose and Fix?" dialog

        Verify Diagnose and Fix screen shows
        Check "Exit Diagnose and Fix?" dialog UI
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27429619 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29887468
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29887469
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29887470
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29887471
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419924(low)
        """
        self.home.select_diagnose_and_fix_btn()
        self.home.select_diagnose_and_fix_start_btn()
        self.home.select_navbar_back_btn(return_home=False)
        self.diagnose_fix.verify_exit_diagnose_and_fix_dialog()
        if buttons == "exit":
            self.diagnose_fix.click_exit_btn()
            self.home.verify_home_screen()
        else:
            self.diagnose_fix.click_continue_btn()
            self.diagnose_fix.verify_diagnoseing_and_fixing_text_display()
            self.diagnose_fix.verify_no_issue_screen()
            self.home.select_navbar_back_btn()

    def test_02_click_diagnose_fix_link_via_help_support(self):
        """
        Click on Help & Support tile
        Click on "Printing" list item under Help & Support
        Click on Diagnose and Fix link
        Check logs HP Smart log after PSDr is launched
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715637
        """
        self.home.select_help_and_support_tile()
        self.home.verify_help_and_support_page()
        self.help_support.swipe_and_click_item(self.help_support.PRINTING_ITEM)
        self.help_support.swipe_and_click_item(self.help_support.DIAGNOSE_FIX_LINK)
        self.diagnose_fix.verify_diagnoseing_and_fixing_text_display()
        self.diagnose_fix.verify_no_issue_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_help_and_support_page()
        self.home.select_navbar_back_btn()
        event_msg_1 = "//callback/?Action=launchPSDr"
        event_msg_2 = "|DiagnoseAndFixViewModel:Initialize|"
        f = self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH)
        data = f.read().decode("utf-8")
        f.close()
        if str(event_msg_1) and str(event_msg_2) in data:
            return True
        raise NoSuchElementException(
            "Fail to found {} or {}".format(event_msg_1, event_msg_2))
 
    def test_03_check_diagnose_fix_btn_with_different_printer_status(self):
        """
        Printer is offline and installed
        Printer is offline and not installed
        Click on Printer icon for Printer status
        Click Wrench icon(Diagnose & Fix) on the side navigation panel
        Verify offline troubleshooting support page opens
        Diagnose and Fix button is displayed
        Diagnose and Fix button is hidden
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14595661
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14595662
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27429619
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419923
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715637
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/15962759(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/41622757
        """
        try:
            self.fc.trigger_printer_offline_status(self.p)
            self.home.verify_carousel_printer_offline_status()
            sleep(10)
            self.home.click_printer_image()
            self.printer_settings.verify_printer_status_page(is_printer_online=False)
            self.home.select_navbar_back_btn()
            self.home.select_diagnose_and_fix_btn()
            self.home.verify_connect_to_your_printer_screen()
            self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
            sleep(10)
            self.home.select_navbar_back_btn()
            self.home.click_printer_image()
            self.printer_settings.verify_printer_status_page(is_printer_online=False, is_installed=False)
            self.home.select_navbar_back_btn()
        except NoSuchElementException:
            raise NoSuchElementException("verify printer status page flow is failed! plz check the log")
        finally:
            self.fc.restore_printer_online_status(self.p)
