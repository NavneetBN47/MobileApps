from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_01_Load_Smart_Dashboard_HP_Instant_Ink(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.hp_instant_ink = cls.fc.flow[FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=False, ii_status=True)
        self.fc.flow_home_smart_dashboard_hp_instant_ink()

    def test_01_plan_overview(self):
        """
        Description: C28340779, C28340780, C28702701, C28702702
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on HP Instant Ink button
          5. Click on Plan Overview button

        Expected Result:
          4. Verify Plan Overview screen
        """
        self.hp_instant_ink.click_plan_overview_btn()
        self.hp_instant_ink.verify_plan_overview_screen()

    def test_02_change_plan(self):
        """
        Description: C28353786, C28702703
        1. Load to Home screen with hp plus account
        2. Click on Account button on navigation bar of Home screen
        3. Click on More option
        4. Click on HP Instant Ink button
        5. Click on Update Plan button

        Expected Result:
        5. Verify Update Plan screen
        """
        self.hp_instant_ink.click_change_plan_btn()
        self.hp_instant_ink.verify_change_plan_screen()

    def test_03_print_and_payment_history(self):
        """
        Description: C28353787, C28702708
        1. Load to Home screen with hp plus account
        2. Click on Account button on navigation bar of Home screen
        3. Click on More option
        4. Click on HP Instant Ink button
        5. Click on Print and Payment History button

        Expected Result:
        5. Verify Print and Payment History screen
        """
        self.hp_instant_ink.click_print_history_btn()
        self.hp_instant_ink.verify_print_history_screen()

    def test_04_shipping_tracking(self):
        """
        Description: C28353788, C28702712
        1. Load to Home screen with hp plus account
        2. Click on Account button on navigation bar of Home screen
        3. Click on More option
        4. Click on HP Instant Ink button
        5. Click on Shipping Tracking button

        Expected Result:
        5. Verify Shipping Tracking screen
        """
        self.hp_instant_ink.click_shipping_tracking_btn()
        self.hp_instant_ink.verify_shipping_tracking_screen()