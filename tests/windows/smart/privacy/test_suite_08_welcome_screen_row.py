import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_08_Welcome_Screen_Row(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]


    def test_01_check_welcome_for_row(self):
        """
        Install the fresh app or upgrade, verify welcome screen for ROW shows
        (Only cover the fresh install part)
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223912
        """
        self.driver.ssh.send_command('Set-Culture en-GB')
        self.fc.reset_hp_smart() 
        self.welcome.verify_click_btn()
        self.welcome.verify_decline_all_btn()
        self.welcome.verify_manage_options()

    def test_02_check_welcome_for_us(self):
        """
        Check welcome screen for us
        """
        self.driver.ssh.send_command('Set-Culture en-US')
        self.fc.reset_hp_smart()
        self.welcome.verify_click_btn()
        self.welcome.verify_decline_all_btn()
        self.welcome.verify_manage_options()