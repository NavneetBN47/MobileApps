import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "SMART"

class Test_Suite_02_Smart_Dashboard_Hp_Plus_User(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.hp_connect = cls.fc.fd["hp_connect"]
        cls.hpc_printers_users = cls.fc.fd["hpc_printers_users"]
        cls.home = cls.fc.fd["home"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self):
        self.fc.load_account_and_go_to_smart_dashboard(stack=self.stack, account_type="hp+")
        self.hp_connect.click_menu_toggle()
        self.hp_connect.verify_smart_dashboard_menu_screen()

    def test_01_toggle_and_close_button(self):
        """
        C28340770: Smart Dashboard for HP+ account with Printers- Account Summary
        C28340772: Verify behavior of close button
        C28340778: Verify menu items for Smart Dashboard for HP+ user
        """
        self.hp_connect.click_menu_toggle()
        self.hp_connect.verify_account_summary()
        self.hp_connect.click_close_btn()
        self.home.verify_home()
    
    def test_02_hp_support(self):
        """
        C28353791: Verify Users screen (hp+)
        C28340774: Verify HP Support link works as expected
        """
        self.hp_connect.click_users_btn()
        self.hpc_printers_users.verify_users_screen()
        self.hp_connect.click_link_native(link=self.hp_connect.HELP_SUPPORT_LINK)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4
    
    def test_03_end_user_license_agreement(self):
        """
        C28340775: Verify End User License Agreement link works as expected
        """
        self.hp_connect.click_users_btn()
        self.hp_connect.click_link_native(link=self.hp_connect.ENDER_USER_LICENSE_AGREEMENT_LINK)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4
    
    def test_04_hp_privacy(self):
        """
        C28340776: Verify HP Privacy link works as expected
        """
        self.hp_connect.click_users_btn()
        self.hp_connect.click_link_native(link=self.hp_connect.HP_PRIVACY_LINK, scroll=True)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4
    
    def test_05_hp_smart_terms_of_use(self):
        """
        C28340777: Verify HP Smart Terms of Use link works as expected
        """
        self.hp_connect.click_users_btn()
        self.hp_connect.click_link_native(link=self.hp_connect.HP_SMART_TERMS_OF_USE_LINK, scroll=True)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4