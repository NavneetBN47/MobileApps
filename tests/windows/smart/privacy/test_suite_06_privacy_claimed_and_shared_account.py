import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_06_Privacy_Claimed_And_Shared_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_sign_in_and_add_a_remote_printer(self):
        """
        Verify OWS value prop shows after clicking the "Accept All" button in welcome page.
        Add a claimed printer to the carousel
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29223891 
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_remote_printer()

    def test_02_check_owner_account_pivacy_preference(self):
        """
        Click on the printer settings tile
        Observe "Privacy preference" option in the master view

        Verify "Privacy preferences" option is available when signed in with owner account and claimed printer added to the carousel

        https://hp-testrail.external.hp.com/index.php?/cases/view/29224231
        https://hp-testrail.external.hp.com/index.php?/cases/view/29309032
        https://hp-testrail.external.hp.com/index.php?/cases/view/29224233
        https://hp-testrail.external.hp.com/index.php?/cases/view/29224237
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_privacy_preferences_tile()
        self.home.select_navbar_back_btn()

    def test_03_sign_out(self):
        """
        Sign out from the owner account
        """
        self.fc.sign_out()
        self.fc.restart_hp_smart()
        self.home.verify_carousel_printer_offline_status()

    def test_04_sign_in_with_a_shared_user_account(self):
        """
        Sign in with a shared user account
        """
        self.login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="hp+", shared=True)
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        sleep(10)

    def test_05_check_shared_account_pivacy_preference(self):
        """
        Click on the printer settings tile
        Observe the "Privacy preference" option in the master view

        Verify "Privacy preferences" option is not available when signed in with shared user account and shared printer added to the carousel
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29224232
        https://hp-testrail.external.hp.com/index.php?/cases/view/29224234
        https://hp-testrail.external.hp.com/index.php?/cases/view/29224252
        """
        self.home.select_printer_settings_tile()
        assert self.printer_settings.verify_privacy_preferences_tile(raise_e=False) is False
        self.home.select_navbar_back_btn()
    
        
