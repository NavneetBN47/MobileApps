import pytest

from MobileApps.libs.ma_misc import ma_misc
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_04_Home_Coach_Mark(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
    
    def test_01_check_coach_mark_via_tile(self):
        """
        Sign in after Sign out into UCDE or HP+ account, verify Coach Mark for Portal shows again
        Sign in with UCDE or HP+ account (via tile), verify Coach Mark for Portal shows
        click any where on the main UI, verify coachmark got dismissed
        Sign in with UCDE or HP+ account (via person icon), verify Coach Mark for Portal shows
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28046041
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28046044
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28890498
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28046034
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28046037
        """
        self.fc.go_home()

        self.home.select_scan_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        self.scan.verify_new_scan_auto_enhancements_dialog()
        self.home.select_navbar_back_btn()
        self.home.verify_coach_mark_for_portal()

        self.home.click_coach_mark_text()
        assert self.home.verify_coach_mark_for_portal(timeout=3, raise_e=False) is False

        self.fc.sign_out()
        sleep(5)
        assert self.home.verify_logged_in() is False

        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen(timeout=30)
        self.home.verify_coach_mark_for_portal(timeout=30)

    def test_02_check_coach_mark_after_relaunch(self):
        """
        Re-launch app after Coach Mark is dismissed, verify Coach Mark for Portal doesn't show again
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28052921
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])

        self.home.verify_home_screen(timeout=30)
        self.home.verify_coach_mark_for_portal(timeout=30)
        self.home.click_coach_mark_text()
        assert self.home.verify_coach_mark_for_portal(timeout=3, raise_e=False) is False

        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        assert self.home.verify_coach_mark_for_portal(raise_e=False) is False

        self.fc.sign_out()
        sleep(5)
        assert self.home.verify_logged_in() is False
