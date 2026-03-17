import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_06_HP_Instant_Ink(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.help_center = cls.fc.fd["hpc_help_center"]
        cls.hp_connect = cls.fc.fd["hp_connect"]
        cls.home = cls.fc.fd["home"]
        

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self, account_type):
        self.fc.load_smart_dashboard_help_center(stack=self.stack, account_type=account_type)
        self.help_center.click_link_on_help_center_screen(self.help_center.HP_INSTANT_INK)

    def test_01_hp_instant_ink(self):
        '''
        C28387131: Verify 'HP Instant Ink' option (hp+)
        C28715520: Verify 'HP Instant Ink' option (ucde)
        '''
        self.help_center.verify_hp_instant_ink()
        self.hp_connect.click_close_btn()
        self.home.verify_home()               