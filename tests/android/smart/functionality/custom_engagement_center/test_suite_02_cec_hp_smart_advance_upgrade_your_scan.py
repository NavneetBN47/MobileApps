from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_CEC_HP_Smart_Advance_Upgrade_Your_Scan(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.cec = cls.fc.flow[FLOW_NAMES.CUSTOM_ENGAGEMENT_CENTER]
        cls.stack = request.config.getoption("--stack")
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_try_camera_scan_learn_more(self):
        """
        Description:
         1. Load Home screen with HPID sigin
         2. Click on See all button from Home screen
         3. Click on Try Camera scan tile

        Expected Result:
         2. Verify below tiles shows on CEC section:
            + Try camera scan tile
            Verify that below tile won't be displayed on CEC section
            + Unlock cloud feature tile
         3. Verify Try camera scan tile disappear on the screen
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer(invisible=False)
        self.cec.click_see_all()
        self.cec.verify_unlock_cloud_features_tile(invisible=True, displayed=False)
        self.cec.verify_try_camera_scan_tile(invisible=False)
        self.cec.click_try_camera_scan_tile()
        self.cec.verify_try_camera_scan_screen()

    def test_02_close_btn(self):
        """
        Description:
         1. Load Home screen HPID sigin
         2. Click on See all button from Home screen
         3. Click on close button from Try Camera scan tile
         4. Click on close button from Shortcuts Save time tile

        Expected Result:
         2. Verify below tiles shows on CEC section:
            + Try camera scan tile
            + Shortcuts save time tile
         3. Verify Try camera scan tile disappear on the screen
         4. Verify Shortcuts Save time tile disappear on the screen
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer(invisible=False)
        self.cec.click_see_all()
        self.cec.verify_try_camera_scan_tile(invisible=False)
        self.cec.verify_shortcuts_save_time_tile(invisible=False)
        self.cec.click_try_camera_scan_close_btn()
        self.cec.verify_try_camera_scan_tile(invisible=True)
        self.cec.click_shortcuts_save_time_close_btn()
        self.cec.verify_shortcuts_save_time_tile(invisible=True)

    def test_03_shortcut_save_time_learn_more(self):
        """
        Description:
         1. Load Home screen with HPID sigin
         2. Click on See all button from Home screen
         3. Click on Shortcuts Save time tile

        Expected Result:
         2. Verify below tiles shows on CEC section:
            + Shortcuts Save time tile
         3. Verify Shortcut save time screen displays
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer(invisible=False)
        if self.stack == "pie":
            pytest.skip("On pie stack, HP Smart app crashed by defect AIOA-19135")
        self.cec.click_see_all()
        self.cec.verify_shortcuts_save_time_tile(invisible=False)
        self.cec.click_shortcuts_save_time_tile()
        self.cec.verify_shortcut_save_time_screen()