from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import PACKAGE
pytest.app_info = "SMART"


class Test_Suite_02_Preview_More_Option(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_print_help(self):
        """
        Description: C31297331, C31297326
        1. Load to Hom screen
        2. Click on Copy tile
        3. Click on Capture button
        4. Click on More Option icon

      Expected Results:
        4. Verify Print Help option display on the screen
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.preview.select_more_options_btn()
        self.preview.verify_more_options_btns(btns=[self.preview.HELP_BTN])
        self.preview.verify_more_options_btns(btns=[self.preview.FORMAT_BTN], invisible=True)

    @pytest.mark.parametrize("link_name", ["google_play", "settings"])
    def test_02_print_help_link_verify(self, link_name):
        """
        Description: C31297333, C31297334, C31297332
        1. Load to Hom screen
        2. Click on Copy tile
        3. Click on Capture button
        4. Click on More Option icon
        5. Click on Print Help item
        6. Check 2 boxes
        7. Check the 3rd boxes, and click on OK button
        8. Click on Print Help item
        9. Click on Links on Print Help screen:
           + Open Printing Settings link
           + Google Play link
      Expected Results:
        5. Verify Print Help screen with:
           + 3 checkboxs
           + Title
        6. OK button isn't clickable
        7. Verify Copy Preview screen
        9. Verify the link we clicked
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.verify_copy_preview_screen()
        self.preview.select_more_options_btn(self.preview.HELP_BTN)
        self.preview.verify_print_help_screen()
        self.preview.toggle_print_help_option(self.preview.PRINT_PLUGIN_CB)
        self.preview.toggle_print_help_option(self.preview.PRINT_SETTINGS_CB)
        self.preview.verify_ok_btn(False)
        self.preview.toggle_print_help_option(self.preview.PRINTER_SELECT_CB)
        self.preview.verify_ok_btn(True)
        self.preview.select_ok_btn()
        self.digital_copy.verify_copy_preview_screen()
        self.preview.select_more_options_btn(self.preview.HELP_BTN)
        self.preview.select_print_help_link(link_name)
        if link_name == "google_play":
            self.digital_copy.verify_google_play_link()
        else:
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.SETTINGS), "Android Settings is not launching"

    def test_03_more_option_from_scanner(self):
        """
        Description:C31297330
        1. Load to Hom screen, and add a printer to the carousel
        2. Click on Scan tile
        3. Scan a picture
        4. Click on Next button
        5. Click on More Option icon on Preview screen
        6. Click on Print Format button

        Expected Results:
        4. Verify Preview screen with:
           + Preview title
           + Save button displays
        5. Verify More Option screen with:
           + Print Help
           + Print Format displays
        6. Verify Print Format screen
        """
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn(timeout=20)
        self.preview.verify_preview_screen()
        self.preview.verify_bottom_nav(self.preview.SAVE_BTN, invisible=False)
        self.preview.select_more_options_btn()
        self.preview.verify_more_options_btns(btns=[self.preview.HELP_BTN], invisible=True)
        self.preview.verify_more_options_btns(btns=[self.preview.FORMAT_BTN], invisible=False)