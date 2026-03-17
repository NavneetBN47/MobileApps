from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_01_Load_Smart_Dashboard_Features(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.hp_connect_features = cls.fc.flow[FLOW_NAMES.HP_CONNECT_FEATURES]

        # Define the variable
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_hp_smart_advance(self):
        """
        Description: C28353792, C28353795, C28590357
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Features button
          5. Click on HP Smart Advance button

        Expected Result:
          5. Verify HP Smart Advance screen
        """
        self.fc.flow_home_smart_dashboard_features_menu()
        self.hp_connect_features.click_hp_smart_advance_btn()
        self.hp_connect_features.verify_hp_smart_advance_screen()

    def test_02_smart_security(self):
        """
        Description: C28353793, C28590358
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Features button
          5. Click on Smart security button

        Expected Result:
          5. Verify Privacy Settings screen
        """
        self.fc.reset_app()
        self.fc.flow_home_smart_dashboard_features_menu()
        self.hp_connect_features.click_smart_security_btn()
        self.hp_connect_features.verify_smart_security_screen()