import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_04_Additional_Help_And_Support(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.help_center = cls.fc.fd["hpc_help_center"]
        cls.hp_connect = cls.fc.fd["hp_connect"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self, account_type):
        self.fc.load_smart_dashboard_help_center(stack=self.stack, account_type=account_type)
        self.help_center.click_link_on_help_center_screen(self.help_center.ADDITIONAL_HELP_AND_SUPPORT)
        self.help_center.verify_additional_help_and_support()

    def test_01_print_anywhere_online_support(self):
        """
        C28387647: Verify 'Additional Help and Support' page (hp+)
        C28387648: Verify 'Print Anywhere Online Support' link (hp+)
        C28717662: Verify 'Additional Help and Support' page (ucde)
        C28717663: Verify 'Print Anywhere Online Support' link (ucde)
        """
        self.help_center.click_link_on_help_center_screen_native(self.help_center.PRINT_ANYWHERE_ONLINE_SUPPORT)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4

    def test_02_shortcuts_online_support(self):
        """
        C28387649: Verify 'Smart Tasks Online Support' link (hp+)
        C28717664: Verify 'Smart Tasks Online Support' link (ucde)
        """
        self.help_center.click_link_on_help_center_screen_native(self.help_center.SHORTCUTS_SUPPORT)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4

    def test_03_hp_mobile_printing(self):
        """
        C28387650: Verify 'HP Mobile Printing' link (hp+)
        C28717665: Verify 'HP Mobile Printing' link (ucde)
        """
        self.help_center.click_link_on_help_center_screen_native(self.help_center.HP_MOBILE_PRINTING)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4