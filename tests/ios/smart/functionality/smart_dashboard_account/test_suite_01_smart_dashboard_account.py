import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_01_Smart_Dashboard_Account(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self, account_type):
        self.fc.load_account_and_go_to_smart_dashboard(stack=self.stack, account_type=account_type)
        self.fc.fd["hp_connect"].click_menu_toggle()
        self.fc.fd["hpc_account"].click_account_btn()
        self.fc.fd["hpc_account"].verify_account_menu_screen()

    def test_01_account_profile(self):
        """
        C28353796: Verify menu items for Account (hp+)
        C28353799: Verify Account Profile page (hp+)
        C28698894: Verify Account Profile page (ucde)
        """
        self.fc.fd["hpc_account"].click_account_profile_btn(delay=2)
        self.fc.fd["hp_connect"].verify_account_profile_screen(timeout=15)

    def test_02_view_notifications(self):
        """
        C28353800: Verify View Notifications page (hp+)
        C28698895: Verify View Notifications page (ucde)
        """
        self.fc.fd["hpc_account"].click_view_notifications_btn()
        self.fc.fd["hpc_account"].verify_view_notifications_screen()

    def test_03_shipping_billing_info(self):
        """
        C28353797: Verify Shipping & Billing page (hp+)
        C28698892: Verify Shipping & Billing page (ucde)
        C28353798: Verify Shipping & Billing page (hp+)
        C28698893: Verify Shipping & Billing page (ucde)
        """
        self.fc.fd["hpc_account"].click_shipping_billing_btn()
        self.fc.fd["hpc_account"].verify_shipping_billing_screen(timeout=25)