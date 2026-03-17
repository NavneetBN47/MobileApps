import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "GOTHAM"
class Test_Suite_19_Scan_China_region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.sf = SystemFlow(cls.driver)
  
        cls.stack = request.config.getoption("--stack")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    
    def test_01_relaunch_app_with_china_reigon(self):
        """
        Change computer region to China
        Verify user can use Scan functionality without being signed in
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777820
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777816
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.driver.terminate_app()
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 45')
        self.driver.launch_app()
        self.home.verify_home_screen()
        self.gotham_utility.click_maximize()
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.verify_scanner_screen()

    def test_02_some_button_not_show_in_preview_screen(self):
        """
        Observe scan result screen for "MObile Fax" button
        Observe scan result screen for "shortcuts" button
        Verify these buttons is hidden when user is not signed in even though scan tile is open
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777817
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777818
        """
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_mobile_fax_btn_does_not_show()
        self.scan.verify_shortcuts_btn_does_not_show()

    def test_03_clean_env(self):
        self.sf.change_pc_region_to_us_region()
