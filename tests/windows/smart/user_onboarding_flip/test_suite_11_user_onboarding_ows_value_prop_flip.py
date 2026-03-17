import pytest

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow


pytest.app_info = "GOTHAM"
class Test_Suite_11_User_Onboarding_OWS_Value_Prop_Flip(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.home = cls.fc.fd["home"]
        cls.account = cls.fc.fd["account"]
        cls.printers = cls.fc.fd["printers"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_check_ows_flip_value_prop_screen(self):
        """
        (Flip) Switch from non-SGP/HP region to SGP/HP region (new user), verify returned user is forced to signin/signup during app launch
        (Flip) Set PC region to SGP/HK, verify new app user is forced to signin/signup during app launch

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29903172
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/29903166
        """
        self.sf.change_pc_region_to_flip_region()

        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen(flip=True)
        self.ows_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        assert self.home.verify_logged_in() is True

    def test_02_check_ows_flip_value_prop_screen_relaunch(self):
        """
        (Flip) Exit the app (signed in to SGP/HK), relaunch app, verify OWS Flip value prop doesn't show

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29903170
        """
        self.fc.restart_hp_smart()
        assert self.home.verify_logged_in() is True

    def test_03_check_ows_flip_value_prop_screen_sign_out(self):
        """
        (Flip) Set PC region to SGP/HK, verify new app user is forced to signin after signout

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29903167
        """
        self.home.select_app_settings_btn()
        self.home.select_sign_out_listview()
        self.account.verify_sign_out_dialog()
        self.account.select_sign_out_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen(flip=True)

    def test_04_set_region_back_to_usa(self):
        self.sf.change_pc_region_to_us_region()
        self.fc.reset_hp_smart()

