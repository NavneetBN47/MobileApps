import pytest
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow


pytest.app_info = "GOTHAM"
class Test_Suite_05_CEC_No_Sign_In_No_Printer_Non_Hpc(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)

        cls.home = cls.fc.fd["home"]
        cls.cec = cls.fc.fd["cec"]

        cls.stack = request.config.getoption("--stack")

    def test_01_check_cec_jweb_area_non_hpc_region(self):
        """
        Check CEC Jweb area (w/internet, not signed in, non-II region, no printer), verify related engagements in CEC Jweb area

        -verify signin/create account related engagement along with Shortcuts related engagement show in CEC Jweb area
        -verify DSP related engagement doesn't show in CEC Jweb area

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749316
        """
        self.sf.change_pc_region_to_non_hpc_region()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)
        self.fc.go_home()

        if self.stack == "pie":
            pytest.skip("Only check this test point for stage Stack, Skip for pie and production stack.")
        self.home.verify_cec_banner()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)  
        self.cec.verify_unlock_cloud_features_tile()
        self.cec.verify_shortcuts_save_time_tile()
        self.cec.verify_never_run_out_save_tile(invisible=True)
        if self.cec.verify_do_more_with_hp_smart_screen(raise_e=False):
            self.cec.click_back_btn_do_more_with_hp_smart_screen()
        self.home.verify_home_screen()

    def test_02_restore_region(self):
        self.sf.change_pc_region_to_us_region()