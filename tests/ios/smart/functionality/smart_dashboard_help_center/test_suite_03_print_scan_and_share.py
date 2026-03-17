import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_03_Print_Scan_and_Share(object):

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
        C28387642: Verify 'Print, Scan, and Share' page (hp+)
        C28715517: Verify 'Print, Scan, and Share' page (ucde)
        :param account_type:
        """
        self.fc.load_smart_dashboard_help_center(stack=self.stack, account_type=account_type)
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINT_SCAN_AND_SHARE)
        self.help_center.verify_print_scan_and_share()

    def test_01_printing(self):
        """
        C28387643: Verify 'Printing' option (hp+)
        C28715518: Verify 'Printing' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINTING)
        self.help_center.verify_printing()

    def test_02_scanning(self):
        """
        C28387644: Verify 'Scanning' option (hp+)
        C28715519: Verify 'Scanning' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SCANNING)
        self.help_center.verify_scanning()

    def test_03_fax(self):
        """
        C28387645: Verify 'Fax' option (hp+)
        C28715522: Verify 'Fax' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.FAX)
        self.help_center.verify_fax()

    def test_04_shortcuts(self):
        """
        C28386114: Verify 'Shortcuts' option (hp+)
        C28715521: Verify 'Shortcuts' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SHORTCUTS)
        self.help_center.verify_shortcuts()