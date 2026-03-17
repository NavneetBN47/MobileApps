import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Smart_Dashboard_Ucde_User(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.hp_connect = cls.fc.fd["hp_connect"]

    def test_01_verify_hamburger_menu_and_chat_with_virtual_agent(self):
        """
        C27268589: Virtual Agent
        C28734590 - verify menu items for flex user
        C28746932 - chat with virtual agent -> cancel
        """
        self.fc.load_account_and_go_to_smart_dashboard(stack=self.stack, account_type="ucde")
        self.hp_connect.click_menu_toggle()
        self.hp_connect.verify_smart_dashboard_menu_screen(timeout=15)
        self.hp_connect.select_chat_with_virtual_agent()
        self.hp_connect.verify_virtual_chat_popup()
        self.hp_connect.select_virtual_agent_cancel()
        self.hp_connect.verify_account_summary(timeout=25)