import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_01_Dashboard_Hp_Instant_Ink(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.instant_ink = cls.fc.fd["hpc_instant_ink"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_hp_instant_ink_menu(self, account_type):
        self.fc.load_smart_dashboard_hp_instant_ink(self.stack, account_type)

    def test_01_plan_overview(self):
        """
        C28340779: Verify menu items for HP+ Print Plans (hp+)
        C28702701; Verify menu items for HP Instant Ink (ucde)
        C28702702: Verify Plan Overview page (ucde)
        C28340780: Verify Plan Overview page (hp+)
        """
        self.instant_ink.click_plan_overview_btn()
        self.instant_ink.verify_plan_overview_screen()
    
    def test_02_change_plan(self):
        """
        C28353786: Verify Change Plan Page (hp+)
        C28702703: Verify Change Plan page (ucde)        
        """
        self.instant_ink.click_change_plan_btn()
        self.instant_ink.verify_change_plan_screen()

    def test_03_print_history(self):
        """
        C28353787: Verify Print History page (hp+)
        C28702708: Verify Print History page (ucde)        
        """
        self.instant_ink.click_print_history_btn()
        self.instant_ink.verify_print_history_screen()
    
    def test_04_shipping_tracking(self):
        """
        C28353788: Verify Shipment Tracking page  (hp+)
        C28702712: Verify Shipment Tracking page (ucde)        
        """
        self.instant_ink.click_shipping_tracking_btn()
        self.instant_ink.verify_shipping_tracking_screen()