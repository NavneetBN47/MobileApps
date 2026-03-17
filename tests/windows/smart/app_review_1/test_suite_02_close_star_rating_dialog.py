import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_02_Close_Star_Rating_Dialog(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, microsoft_account_cleanup):
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

    def test_02_go_to_scan_preview_screen(self):
        """
        Perform a scan job

        https://hp-testrail.external.hp.com/index.php?/cases/view/15959347
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
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/15959347
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

        self.scan.verify_are_you_enjoying_dialog()
        self.scan.click_are_you_dialog_yes_btn()

    def test_04_skip_microsoft_account(self):
        """
        if the Microsoft screen popup, login the account

        https://hp-testrail.external.hp.com/index.php?/cases/view/15959347
        """        
        if self.scan.verify_write_review_dialog(raise_e=False) is False:
            self.sf.microsoft_login(self.ms_login_info["username"], self.ms_login_info["password"])

    def test_05_close_start_rating_dialog(self):
        """
        Choose a rating and click Add a review button
        Click the X button at the top right

        Pop up should say "Are you enjoying the HP smart app?"
        "Choose a star rating" dialog box should appear after hitting yes
        Window changes to Review for HP Smart
        User should be returned to Scan Results page after hitting X button.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15959347
        """
        self.scan.close_review_dialog()
        self.scan.verify_review_dialog_disappear()
        self.scan.verify_scan_result_screen()
