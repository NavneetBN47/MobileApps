import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_08_Not_Enjoying_Click_Not_Now_Time_Back(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_system_time):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.ms_login_info = ma_misc.get_microsoft_account_info()

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        
    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.sf.reset_system_time()

    def test_02_go_to_scan_preview_screen(self):
        """
        Perform a scan job
        """
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

    def test_03_save_twice(self):
        """
        Try to save it twice.
        On the pop up, click the Yes button
        Pop up should say "Are you enjoying the HP smart app?"
        """     
        for _ in range(2):
            self.scan.click_save_btn()
            self.scan.verify_save_dialog()
            self.scan.click_save_dialog_save_btn()

            sleep(1)
            self.scan.click_save_as_dialog_save_btn()
            file_path = self.scan.get_the_saved_file_path()
            self.scan.click_dialog_close_btn()
            self.driver.ssh.send_command("del " + file_path)
            sleep(1)

    def test_04_sorry_to_hear_flow(self):
        """
        Time has been moved back at least 6 months

        On the pop up, click the No button
        Click Not now button

        Pop up should say "Are you enjoying the HP smart app?"
        Not now button should close the dialogue and return user to Scan Results page

        https://hp-testrail.external.hp.com/index.php?/cases/view/15959366
        https://hp-testrail.external.hp.com/index.php?/cases/view/15959360
        https://hp-testrail.external.hp.com/index.php?/cases/view/15959354
        """
        self.scan.verify_are_you_enjoying_dialog()
        self.scan.click_are_you_dialog_not_now_btn()
        self.scan.verify_are_you_enjoying_dialog_disappear()
        self.scan.verify_sorry_to_hear_dialog()
        self.scan.click_sorry_to_dialog_not_now_btn()
        self.scan.verify_sorry_to_hear_dialog_disappear()
        self.scan.verify_scan_result_screen()
