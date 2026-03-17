import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_01_About_Hp_Smart(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.help_center = cls.fc.fd["hpc_help_center"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self, account_type):
        """
        C28353803: Verify menu items for Help Center (hp+)
        C28715443: Verify menu items for Help Center (ucde)
        C28353804: Verify About HP Smart page (hp+)
        C28715444: Verify About HP Smart page (ucde)
        :param account_type:
        """
        self.fc.load_smart_dashboard_help_center(stack=self.stack, account_type=account_type)
        self.help_center.click_link_on_help_center_screen(self.help_center.ABOUT_HP_SMART)
        self.help_center.verify_about_hp_smart()

    def test_01_about_hp_smart(self):
        """
        C28386109: Verify Getting to Know HP Smart (hp+)
        C28715445: Verify Getting to Know HP Smart (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.GETTING_TO_KNOW_HP_SMART)
        self.help_center.verify_getting_to_know_hp_smart()

    def test_02_about_hp_smart_starting_off(self):
        """
        C28386111: Verify Starting Off (hp+)
        C28715446: Verify Starting Off (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.STARTING_OFF)
        self.help_center.verify_starting_off()

    def test_03_about_hp_smart_sharing_file(self):
        """
        C28386113: Verify Sharing Files (hp+)
        C28715447: Verify Sharing Files (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SHARING_FILES)
        self.help_center.verify_sharing_file()