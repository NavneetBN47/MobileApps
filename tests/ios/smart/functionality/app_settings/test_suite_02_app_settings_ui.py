import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_app_settings_Ui(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_app_settings_unsigned_in(self):
        """
        IOS & MAC:
        C31297652, C31297654: Verify App Settings UI (not signed in)
        C31297235: Verify App settings from bottom action bar
        C31297659: Verify App Setting UI with HP account signed in and out
        C31297660: Verify Cancel option for HP account signed out
        C31297661: Verify "x" button when user goes to sign in page
        """
        self.fc.go_home(stack=self.stack, button_index=2)
        self.home.select_settings_icon()
        self.app_settings.verify_app_settings_screen()
        self.app_settings.verify_sign_in_btn()
        self.app_settings.verify_create_account_btn()
        self.app_settings.select_sign_in_option()
        if pytest.platform == "MAC":
            self.fc.switch_window_and_modify_wn("hpid", "web_login")
            self.web_driver.switch_window()
            self.web_driver.close_window("web_login")
            self.home.verify_home()
            self.home.select_settings_icon()
            self.app_settings.select_sign_in_option()
            self.fc.switch_window_and_modify_wn("hpid", "web_login")
        else:
            self.app_settings.select_cancel()
            self.app_settings.select_sign_in_option()
        self.hpid.login(self.driver.session_data["hpid_user"], self.driver.session_data["hpid_pass"])
        if pytest.platform == "MAC":
            self.fc.delete_window_and_activate_hp_smart("web_login")
            self.home.verify_home()
            self.home.select_settings_icon()
        self.app_settings.verify_successfull_sign_in_screen()
        self.app_settings.select_sign_out_btn()
        self.app_settings.verify_sign_out_confirmation_popup()
        self.app_settings.dismiss_sign_out_popup(signout=False)
        self.app_settings.sign_out_from_hpc()
        if pytest.platform == "MAC":
            self.home.verify_sign_in_icon()

    def test_02_app_settings_signed_in(self):
        """
        IOS & MAC:
        C31297653: Verify App Settings UI (signed in)
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_settings_icon()
        self.app_settings.verify_app_settings_screen()
        self.app_settings.verify_successfull_sign_in_screen()
        self.app_settings.select_my_hp_account()