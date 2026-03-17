import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_05_Printer_and_Connection(object):

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
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINTER_AND_CONNECTION)
        self.help_center.verify_printer_and_connection_information()

    def test_01_printer_support(self):
        """
        C28387312: Verify 'Printer and Connection Information' page (hp+)
        C28387313: Verify 'Printer Support' link (hp+)
        C28715452: Verify 'Printer and Connection Information' page (ucde)
        C28715453: Verify 'Printer Support' link (ucde)
        """
        self.help_center.click_link_on_help_center_screen_native(self.help_center.PRINTER_SUPPORT)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4

    def test_02_finding_your_printer(self):
        """
        C28387635: Verify 'Finding Your Printer' option (hp+)
        C28715454: Verify 'Finding Your Printer' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.FINDING_YOUR_PRINTER)
        self.help_center.verify_finding_your_printer()

    def test_03_connecting_to_your_printer(self):
        """
        C28387638: Verify 'Connecting to Your Printer' option (hp+)
        C28715455: Verify 'Connecting to Your Printer' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.CONNECTING_TO_YOUR_PRINTER)
        self.help_center.verify_connecting_to_your_printer()

    def test_04_viewing_printer_information(self):
        """
        C28387639: Verify 'Viewing Printer Information' option (hp+)
        C28715456: Verify 'Viewing Printer Information' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.VIEWING_PRINTER_INFORMATION)
        self.help_center.verify_viewing_printer_information()

    def test_05_print_service_plugin(self):
        """
        C28387640: Verify 'Print Service Plugin' option (hp+)
        C28715457: Verify 'Print Service Plugin' option (ucde)
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINT_SERVICE_PLUGIN)
        self.help_center.verify_print_service_plugin()