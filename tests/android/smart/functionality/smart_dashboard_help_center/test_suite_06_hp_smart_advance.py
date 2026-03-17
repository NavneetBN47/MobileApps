from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_06_Hp_Smart_Advance(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

        # Define the variable
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True, force_reset=True)

    def test_01_hp_smart_advance(self):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP Smart Advance

        Expected Result:
          3. Verify HP Smart Advance screen
        """
        self.fc.load_smart_dashboard_help_center_hp_smart_advance()

    def test_02_what_is_hp_smart_advance(self):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP Smart Advance item
          6. Click on What is HP Smart Advance?

        Expected Result:
          3. Verify What is HP Smart Advance screen
        """
        self.fc.load_smart_dashboard_help_center_hp_smart_advance()
        self.help_center.click_link_on_help_center_screen(self.help_center.WHAT_IS_HP_SMART_ADVANCE)
        self.help_center.verify_what_is_hp_smart_advance()

    def test_03_print_anywhere(self):
        """
        Description: C28387282
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP Smart Advance item
          6. Click on Print Anywhere

        Expected Result:
          3. Verify Print Anywhere screen
        """
        self.fc.load_smart_dashboard_help_center_hp_smart_advance()
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINT_ANYWHERE)
        self.help_center.verify_print_anywhere()