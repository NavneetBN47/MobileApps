from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
import datetime


pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_07_Shortcuts(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, record_testsuite_property, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define the variable
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)
        record_testsuite_property("suite_test_category", "SmartTask")

    def test_01_shortcuts_for_saving(self):
        """
        Description:
          1. Load to Home screen
          2. Select a target printer from Printer lists
          3. Login in HPID in App Settings
          4. Click on Smart Tasks tile on Home screen (Enable Smart Task file from Personalize if Smart Tasks tile not on Home screen)
          5. Click on Add Shortcuts button
          6, Create a Shortcut for saving option
          7. Click on Start this Shortcuts button
          8. Click on My Photos, and select a photo from any album
          9. Click on Start button

        Expected Result:
          9. Verify Shortcuts send success screen popup
        """
        shortcuts_name = "{}_{:%d_%H_%M_%S}".format("saving", (datetime.datetime.now()))
        self.fc.reset_app()
        self.fc.flow_home_load_shortcuts_screen(create_acc=False, printer_obj=self.p)
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_saving()
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcuts_name)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_scanner_btn()
        self.scan.dismiss_coachmark()
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.shortcuts.verify_shortcuts_start_preview_screen()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen(timeout=25)

    def test_02_smart_task_for_email(self):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Shortcuts tile
          4. Create a Shortcuts with single email
          5. Select new Shortcuts from step 4
          6. Select Camera
          7. Select Allow Access to Camera, and capture with manual mode
          8. Click on Start button

        Expected Result:
          5. Verify Shortcuts source images or documents screen
             - Camera item
             - Files & Photos item
             - Scanner item is invisible
          8. Verify Shortcuts send success screen popup:
             - Message
             - Home button
             - More Option button
             - Activity button
        """
        shortcuts_name = "{}_{:%d_%H_%M_%S}".format("email", (datetime.datetime.now()))
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_email(self.email_address)
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name=shortcuts_name)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
        self.shortcuts.click_camera_btn()
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT, mode="document")
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.shortcuts.verify_shortcuts_start_preview_screen()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen(timeout=25)