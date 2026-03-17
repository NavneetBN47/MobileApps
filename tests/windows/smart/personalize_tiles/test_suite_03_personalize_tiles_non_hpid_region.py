import pytest
import time
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Personalize_Tiles_Non_Hpid_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.sf = SystemFlow(cls.driver)

        cls.home = cls.fc.fd["home"]
        cls.per_tiles = cls.fc.fd["personalize_tiles"]

        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        time.sleep(3)

    def test_01_relaunch_app_with_china_reigon(self):
        """
        Change computer region to China
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.driver.terminate_app()
        self.sf.change_pc_region_to_non_hpc_region()
        self.driver.launch_app()
        self.home.verify_home_screen()

    def test_02_check_smart_tasks_tile(self):
        """
        Go to "Personalize Tile" screen

        Verify "Smart Tasks" tile is not listed in the "Personalize Tile" screen
        Verify "Mobile Fax" option is not listed

        https://hp-testrail.external.hp.com/index.php?/cases/view/16932056
        https://hp-testrail.external.hp.com/index.php?/cases/view/17361149
        https://hp-testrail.external.hp.com/index.php?/cases/view/27836980
        https://hp-testrail.external.hp.com/index.php?/cases/view/27836982
        """
        self.home.select_app_settings_btn()
        self.home.select_personalize_tiles_listview()
        self.per_tiles.verify_personalize_tiles_screen(hpid_region=False)

    def test_03_restore_region(self):
        self.sf.change_pc_region_to_us_region()
