import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


# pytest.app_info = "GOTHAM"
pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"

class Test_Suite_01_Diagnose_Fix_Hero_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.scan = cls.fc.fd["scan"]
     
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_complete_diagnose_fix_hero_flow(self):
        """
        Follow the attached flow chart to complete the flow

        Verify flow
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419939  
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419940 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554640
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14592256(low)
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721574(low)
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13043369
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_diagnose_and_fix_btn()
        self.home.select_diagnose_and_fix_start_btn()
        self.diagnose_fix.verify_diagnoseing_and_fixing_text_display()
        self.diagnose_fix.verify_no_issue_screen()
        self.diagnose_fix.click_test_print_btn()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_print_btn()
        self.diagnose_fix.verify_no_issue_screen()
        self.diagnose_fix.click_done_btn()
        self.home.verify_home_screen()
        