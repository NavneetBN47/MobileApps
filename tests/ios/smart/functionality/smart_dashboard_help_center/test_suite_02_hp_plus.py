import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_02_Hp_Plus(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.help_center = cls.fc.fd["hpc_help_center"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.load_smart_dashboard_help_center(stack=self.stack, account_type="hp+")
        self.help_center.click_link_on_help_center_screen(self.help_center.HP_PLUS)
        self.help_center.verify_hp_plus()

    def test_01_what_is_hp_plus(self):
        """
        C28364111: Verify HP+ page
        C28387128: Verify 'What is HP+ ? ' page
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.WHAT_IS_HP_PLUS)
        self.help_center.verify_what_is_hp_plus()
    
    def test_02_hp_smart_security(self):
        """
        C28387132: Verify 'HP Smart Security' page
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.HP_SMART_SECURITY)
        self.help_center.verify_hp_smart_security()