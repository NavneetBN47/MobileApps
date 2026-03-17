import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_12_Scan_Detect_Edges_For_Advance_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]
        
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_to_scaner_screen(self):
        """
        go to scaner screen
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()   
        self.scan.click_get_started_btn()

    def test_02_checkout_flatten_btn_not_show(self):
        """
        Set the Source to "Scanner Glass"
        Turn Detect Edges On from scan setting panel
        Perform scan job
        Click on Scan
        Check Detect Edges screen
        Verify the 'Flatten' button doesn't show to the left side of the Detect Edges screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29908331
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29707831
        """
        self.scan.click_detect_edges_box()   
        self.scan.click_scan_btn()
        self.scan.verify_import_screen()
        assert self.scan.verify_flatten_btn_shows(raise_e=False) is False

    def test_03_checkout_flatten_btn_show(self):
        """
        Turn Detect Edges On from scan setting panel
        Perform 1 scan job from one of the following flow with target scan is curved

        a) Camera tab (if pc support camera)
        b) Import a photo image from Import

        Select "Flatten" from Detect Edges screen
        Verify the 'Flatten' button show to the left side of the Detect Edges screen.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29707830
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12961696
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/31344328
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29707828(high)
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.select_import_btn()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.scan.verify_import_screen()
        self.scan.verify_flatten_btn_shows()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()
