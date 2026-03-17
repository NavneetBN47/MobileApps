import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_07_Coachmark(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_coachmark_notification_is_invisible_second_time(self):
        """
        Coachmark notification when sign In - C28044108
        Coachmark notification is not shown when sign in for 2-nd time- C28044100
        Coachmark for AIOI-19664
        """
        login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_02"]
        username, password = login_info["username"], login_info["password"]
        self.fc.go_home(button_index=2, stack=self.stack)
        self.home.select_create_account_icon()
        self.driver.wait_for_context(self.fc.hpid_url, timeout=20)
        self.hpid.verify_hp_id_sign_up()
        self.hpid.click_sign_in_link_from_create_account()
        self.hpid.login(username, password)
        self.fc.clear_popups_on_first_login(smart_task=True, coachmark=False)
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is not False
        self.home.dismiss_tap_account_coachmark()
        self.home.select_app_settings()
        self.app_settings.sign_out_from_hpc()
        self.home.select_home_icon()
        self.home.select_sign_in_btn()
        self.hpid.login(username, password)
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is False

    def test_02_coachmark_invisible_for_new_user_after_signout(self):
        """
        Coachmark notification for new user- C28044099
        Coachmark is not shown when sign out- C28044101
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_create_account_icon()  
        self.fc.create_new_user_account(coachmark=False)
        self.home.verify_tap_account_coachmark_popup()
        self.home.dismiss_tap_account_coachmark()
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is False
        self.home.select_app_settings()
        self.app_settings.sign_out_from_hpc()
        self.home.select_home_icon()
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is False