import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "GOTHAM"
class Test_Suite_20_Scan_HK_Region(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.sf = SystemFlow(cls.driver)
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    
    def test_01_launch_app_with_hk_reigon(self):
        """
        launch app with HK/singapore
        """
        self.sf.change_pc_region_to_flip_region()
        self.fc.reset_hp_smart()
        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen(flip=True)
        self.ows_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        self.home.verify_home_screen()
    
    def test_02_check_ows_screen_shows_after_sign_out(self):
        """
        Verify OWS screen shows again as soon as you sign out.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777821
        """
        self.fc.sign_out(is_hk_region=True)

    def test_03_clean_env(self):
        self.sf.change_pc_region_to_us_region()