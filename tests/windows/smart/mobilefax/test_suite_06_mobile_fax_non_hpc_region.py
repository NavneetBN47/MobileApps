import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "GOTHAM"
class Test_Suite_06_Mobile_Fax_Non_HPC_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.sf = SystemFlow(cls.driver)
  
        cls.stack = request.config.getoption("--stack")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    
    def test_01_launch_app_with_non_hpc_reigon(self):
        """
        launch app with non-hpc region
        """
        self.sf.change_pc_region_to_non_hpc_region()
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_check_mobile_fax_behavior(self):
        """
        Verify the "Mobile Fax" button on the scan preview screen is hidden.
        Verify "Mobile Fax" tile is not available on the main UI
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17361150
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17261143 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14061549
        OWS-68808 User can sign in by "Use HP Smart" button on OWS value prop screen (following pepto screen) on 
        non-HPC region but account doesn't show on main UI.      
        """
        self.home.verify_home_screen()
        self.home.verify_mobile_fax_tile_not_show()
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.verify_mobile_fax_btn_does_not_show()
        self.scan.verify_shortcuts_btn_does_not_show()

    def test_03_clean_env(self):
        self.sf.change_pc_region_to_us_region()
        