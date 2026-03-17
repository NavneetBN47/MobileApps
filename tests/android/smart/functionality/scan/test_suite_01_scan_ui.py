from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from selenium.common.exceptions import InvalidElementStateException
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Scan_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_01_scan_screen(self, account_type):
        """
        Description: C31297213, C31299839, C31299416, C31299406, C31299416, C31299398, C31299408, C31299396
            1. Load Home screen
            2. Select a target printer on Printer screen
            3. Select Scan tile (if it is not visible, enable it in Personalize screen)
                 if App Permission displays, allow it
            4. Select Gear Icon
            5. Reload Home screen
            6. Select Camera scan on bottom navbar
            7. Select Gear button
            8. Enable Auto-Orientation
            9. Reload Home screen
            10. Select Camera scan on bottom navbar
            11. Select Gear button
        Expected Result:
            Verify:
            1. Scan tile is invisible.
            3. Scan screen:
                - Scan settings button
                - exit button
                - Preview and Scan buttons
                - Gear button
                - "Place content on the scanner..." message
                - Scan source button
             Scan Types
              - Photo
              - Document
              - Batch
              - Book for HP+
              - ID Card for HP+
              - Multi Item for HP+
             Default Scan mode is Document

            4. Verify Enhancement options and default states
            - Auto-Orientation - disabled
            - Auto-Enhancements - enabled
            - Auto-Heal for hp+ - enabled
            - Flatten Book Pages for hp+ - disabled
            7. Verify Enhancement options
            - Auto-Orientation
            - Auto-Enhancements
            - Auto-Heal for hp+
            - Flatten Book Pages for hp+
            Verify Auto-Orientation is off by default
            11. Verify Auto-Orientation is on
        """
        self.fc.set_hpid_account(account_type, claimable=False, ii_status=True, force_reset=True)
        self.fc.flow_home_load_scan_screen(self.p, from_tile=True)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.verify_selected_capture_mode()
        self.scan.verify_capture_modes(advanced=account_type=="hp+")
        self.scan.select_enhancements_btn()
        self.scan.verify_enhancements_screen(advanced=account_type == "hp+")
        self.scan.verify_enhancement_state("auto_orientation", False)
        self.scan.verify_enhancement_state("auto_enhancements", True)
        if account_type == "hp+":
            self.scan.verify_enhancement_state("flatten_book_pages", True)
            self.scan.verify_enhancement_state("auto_heal", True)
        self.fc.flow_load_home_screen(verify_signin=False)
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.fc.flow_grant_camera_scan_permissions():
            self.scan.dismiss_coachmark()
        self.scan.select_enhancements_btn()
        self.scan.verify_enhancements_screen(advanced=account_type == "hp+")
        self.scan.verify_enhancement_state("auto_orientation", False)
        self.scan.toggle_enhancement("auto_orientation", enable=True)
        self.scan.verify_enhancement_state("auto_orientation", True)

    def test_02_scan_settings(self):
        """
        Description: C31299840, C31299841, C31299411, C31299412, C31299447, C31299414, C31299448
         1. Load Scan screen via Scan icon on bottom navigation at Home screen
         2. Click on Scan Settings icon button
         3. For each Setting in Scan Settings:
          a. Select Setting
          b. Select a Different Option
          c. Press back button
         4. Press Back button
         5. Click on Source button, and select Printer Scan option

        Expected Results:
         2. Verify Scan Settings screen
            - "Scan Settings" title text
            - Paper Size item
            - Source item
            - Resolution item
            - Color item
         3a. Verify for each option in Scan Settings, if:
          - Source: Scanner Glass
          - Color: Black and Color
          - Resolution: 75, 100, 200, 300 dpi
          - Page Size: 3x5, 4x6, 5x7, Letter, A4
         3c. Verify selected option is present on scan setting screen
         5. Verify Scan Screen
        """
        self.fc.flow_home_load_scan_screen(self.p, from_tile=True)
        self.scan.select_scan_settings_btn()
        self.scan.verify_scan_settings_screen()
        for setting, option in [("color", "color"), ("resolution", "200_dpi"), ("source", "scanner"), ("page_size", "3.5x5")]:
            self.scan.select_scan_setting(setting, option=option)
            self.scan.verify_scan_setting_options(screen=setting)
            self.driver.press_key_back()
            self.scan.verify_selected_scan_setting_option(setting, option)
        self.driver.press_key_back()
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.select_source(self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)

    def test_03_scan_coachmarks(self):
        """
        Description: C31299429, C31299430, C31299431, C31299432, C31299437, C31299433, C31299435, C31299436
         1. Reset app
         2. Launch Smart app and Sign in
         3. Load printer
         4. Select Printer Scan on bottom navbar button
         5. Select Next on Coachmark
         6. Select Back on Coachmark
         7. Select Next on Coachmark
         8. Select Next on Coachmark
         9. Select Next on Coachmark
         10. Select X button on Coachmark
         11. Restart app and load home screen
         12. Load Printer
         13. Select Printer Scan on bottom navbar button
        Expected Results:
         4. Verify First Coachmark
         5. Verify Second Coachmark
         6. Verify First Coachmark
         7. Verify Second Coachmark
         8. Verify Third Coachmark
         9. Verify Fourth Coachmark
         10. Verify Coachmark is invisible
         13. Verify Coachmark is invisible
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.scan.verify_coachmark(coach_num=1)
        self.scan.select_coachmark_btn()
        self.scan.verify_coachmark(coach_num=2)
        self.scan.select_coachmark_btn(btn="back")
        self.scan.verify_coachmark(coach_num=1)
        self.scan.select_coachmark_btn()
        self.scan.verify_coachmark(coach_num=2)
        self.scan.select_coachmark_btn()
        self.scan.verify_coachmark(coach_num=3)
        self.scan.select_coachmark_btn()
        self.scan.verify_coachmark(coach_num=4)
        self.scan.select_coachmark_btn(btn="close")
        self.scan.verify_coachmark(invisible=True)
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.scan.verify_coachmark(invisible=True)

    def test_04_dismiss_coachmark(self):
        """
        Description: C31299434
         1. Reset app
         2. Launch Smart app and Sign in
         3. Load printer
         4. Select Printer Scan on Bottom navbar
         5. Tap anywhere on the screen

        Expected Results:
         4. Verify Coachmark
         5. Verify Coachmark is invisible
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.scan.verify_coachmark()
        try:
            self.driver.click_by_coordinates(area="mm")
        except InvalidElementStateException:
            pass
        self.scan.verify_coachmark(invisible=True)

    def test_05_capture_mode_retained(self):
        """
        Description:
         1. Launch Smart app and Sign in
         2. Load Printer
         3. Load Scan screen
         4. Select Photo mode
         5. Go back to Home screen
         6. Load Scan screen
         7. Select X button on top left
        Expected Result:
         6. Verify current capture mode is Photo
         7. Verify Home screen
        """
        self.fc.flow_home_load_scan_screen(self.p)
        self.scan.select_capture_mode("photo")
        self.driver.press_key_back()
        self.home.verify_home_nav()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.scan.verify_selected_capture_mode(mode="photo")
        self.scan.select_exit_btn()
        self.home.verify_home_nav()