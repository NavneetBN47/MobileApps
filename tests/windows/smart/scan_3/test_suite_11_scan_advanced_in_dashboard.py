import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_11_Scan_Advanced_In_Dashborad(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.smart_dashboard = cls.fc.fd["smart_dashboard"]
        
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)
        cls.login_info_2 = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=False)
        cls.login_info_3 = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="basic", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_smart_dashboard_for_advanced(self):
        """
        Login with user account mosaic entitlements (hp smart advance)
        Click on person icon (initial) -> jweb HP Smart dashboard opens, 
        then select "Solutionns" from the left panel of jweb dashboard
        Click on "HP Smart Advanced" engagement in the CEC jweb area

        Verify "HP Smart Advanced" option is listed
        Verify "HP Smart Advanced page shows with all advanced scan features 
        after clicking on "HP Smart Advanced" option
        Verify correct subscription status shows in this page
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28780369
        """    
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.select_manage_hp_account_btn()
        self.smart_dashboard.verify_my_account_page()
        self.smart_dashboard.select_solutions_btn()
        self.smart_dashboard.select_hp_smart_advance_btn()
        self.home.select_navbar_back_btn()

    def test_02_check_smart_dashboard_for_non_user_account(self):
        """
        Login with non- user account mosaic entitlements (hp smart advance)
        Select printer under test from device picker (make sure it's a printer with Scan feature). (yeti or non-yeti printer)
        Click on person icon (initial) -> jweb HP Smart dashboard opens
        Check HP Smart dashboard

        Verify "HP Smart Advanced" is not listed
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28780940
        """    
        self.fc.sign_out()
        if self.stack == "stage":
            self.fc.sign_in(self.login_info_2["email"], self.login_info_2["password"])
        else:
            self.fc.sign_in(self.login_info_3["email"], self.login_info_3["password"])
        self.home.select_manage_hp_account_btn()
        self.smart_dashboard.verify_my_account_page()
        self.smart_dashboard.select_solutions_btn()
        self.smart_dashboard.verify_hp_smart_advance_btn_not_display()
  