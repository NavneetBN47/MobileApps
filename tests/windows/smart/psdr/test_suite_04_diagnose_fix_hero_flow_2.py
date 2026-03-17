import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


# pytest.app_info = "GOTHAM"
pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"

class Test_Suite_04_Diagnose_Fix_Hero_Flow_2(object):
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


    def test_01_go_to_main_ui(self):
        """
        go to Main UI and select printer
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    @pytest.mark.parametrize("buttons", ["test_print","done"])
    def test_02_check_all_button_on_here_are_your_results_screen(self,buttons):
        """
        Click "Diagnose & Fix" icon on the navigation pane on Main UI (Win)/ Menu bar->Printers (Mac) -> 
        verify "Diagnose & Fix" screen shows
        Click "Start" button on the "Diagnose & Fix" button
        Diagnosing & fixing screen for a brief moment and eventually "Diagnosis complete. 
        Here are your results." will show
        Click "Test Print" button
        Verify native print dialog shows with the Canned PDF file to print.
        Click the "Print" button on the native print dialog
        Click the "Cancel" button on the native print
        verify user navigates to the (Did that solve the problem?) screen
        Click "Done" button
        Verify Main UI shows after clicking the "Done" button
        Click "Test Print" button on the "Did that solve the problem?" screen
        Verify native print dialog shows with the Canned PDF file to print.
        Click "Done" button on the "Did that solve the problem?" screen
        Verify user navigate to main UI
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33339368
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554638 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512813
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554643
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554642
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14591816
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33356556
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14592323
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14592258
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419929(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33356514(low)
        """
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.home.select_diagnose_and_fix_btn()
        self.home.select_diagnose_and_fix_start_btn()
        self.diagnose_fix.verify_diagnosis_complete_screen()
        self.diagnose_fix.verify_here_are_your_results_text_display()
        if buttons=="test_print":
            self.diagnose_fix.click_test_print_btn()
            self.scan.verify_print_dialog()
            self.scan.click_print_dialog_print_btn()
            self.diagnose_fix.verify_did_that_solve_the_problem_text_display()
            self.diagnose_fix.click_test_print_btn()
            self.scan.verify_print_dialog()
            self.scan.click_print_dialog_cancel_btn()
            self.diagnose_fix.verify_did_that_solve_the_problem_text_display()
            self.diagnose_fix.click_done_btn()
            self.home.verify_home_screen()
            self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
            self.home.select_diagnose_and_fix_btn()
            self.home.select_diagnose_and_fix_start_btn()
            self.diagnose_fix.verify_diagnosis_complete_screen()
            self.diagnose_fix.verify_here_are_your_results_text_display()
            self.diagnose_fix.click_test_print_btn()
            self.scan.verify_print_dialog()
            self.scan.click_print_dialog_cancel_btn()
            self.diagnose_fix.verify_did_that_solve_the_problem_text_display()
            self.home.select_navbar_back_btn()
            self.home.verify_home_screen()
        else:
            self.diagnose_fix.click_done_btn()
            self.home.verify_home_screen()
