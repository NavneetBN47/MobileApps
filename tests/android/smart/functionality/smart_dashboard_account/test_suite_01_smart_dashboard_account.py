from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_01_Load_Smart_Dashboard_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.hp_connect_account = cls.fc.flow[FLOW_NAMES.HP_CONNECT_ACCOUNT]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.set_hpid_account(a_type=account_type, claimable=False, ii_status=True, force_reset=True)
        self.fc.flow_home_smart_dashboard_account_menu()

    def test_01_account_profile(self):
        """
        Description: C28353796, C28353799, C28698894
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Account Profile button

        Expected Result:
          5. Verify Account Profile screen
        """
        self.hp_connect_account.click_account_profile_btn()
        self.hp_connect_account.verify_profile_screen(timeout=15)

    def test_02_view_notifications(self):
        """
        Description: C28353800, C28698895
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on View Notifications button

        Expected Result:
          5. Verify View Notification screen
        """
        self.hp_connect_account.click_view_notifications_btn()
        self.hp_connect_account.verify_view_notifications_screen()

    def test_03_shipping_billing_info(self):
        """
        Description: C28353797, C28698892, C28353798
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Shipping & Billing button

        Expected Result:
          5. Verify Billing screen
        """
        self.hp_connect_account.click_shipping_billing_btn()
        self.hp_connect_account.verify_shipping_billing_screen()