from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_04_Scan_Unavailable(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        
        # Define variables
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_scan_feature_unavailable_from_tile_and_action_bar(self):
        """
        Description: C31299808
            1/ Load Home Screen
            2/ Select "Printer Scan" tile
            3/ Dismiss "Feature Unavailable" popup
            4/ Select "Printer Scan" button on action bar
            5/ Dismiss "Feature Unavailable" popup
        Expected Result:
            "Feature Unavailable" popup appears and is dismissable
            Verify:
                1/ Feature Unavailable popup
                2/ Home screen is present after dismissing popup
                4/ Feature Unavailable popup
                5/ Home screen is present after dismissing popup
        """
        # remove printer function sometimes doesn't work, and we already have CR for tracking this information
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.home.dismiss_feature_unavailable_popup()
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.home.dismiss_feature_unavailable_popup()
        self.home.verify_home_nav()
