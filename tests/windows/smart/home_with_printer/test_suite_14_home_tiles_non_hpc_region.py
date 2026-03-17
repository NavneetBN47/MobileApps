import pytest
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow


pytest.app_info = "GOTHAM"
class Test_Suite_14_Home_Tiles_Non_Hpc_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.sf = SystemFlow(cls.driver)

        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_check_tiles_non_hpc_region_without_printer(self):
        """
        Check bell icon (non-HPC region, signed in), verify bell icon is not available on Navigation Pane 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17361151
        """
        self.sf.change_pc_region_to_non_hpc_region()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        assert self.home.verify_activity_btn(raise_e=False) is False

    def test_02_check_tiles_non_hpc_region_without_printer(self):
        """
        Verify main page (with no printer selected in non-HPC region) UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890659
        """
        self.home.verify_shortcuts_tile(invisible=True)
        self.home.verify_mobile_fax_tile(invisible=True)
        self.home.verify_printables_tile()

    def test_03_check_tiles_non_hpc_region_with_printer(self):
        """
        Select any printer to main UI (non-HPC region), verify "Shortcuts" tile does not show on main UI
        Verify main page (with printer selected in non-HPC region) UI
        Check "Printables" tile in Non-HPC region, verify tile is available

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235484
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24810630
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890661
        """
        self.fc.select_a_printer(self.p)

        self.home.verify_shortcuts_tile(invisible=True)
        self.home.verify_mobile_fax_tile(invisible=True)
        self.home.verify_printables_tile()

    def test_04_restore_region(self):
        self.sf.change_pc_region_to_us_region()
