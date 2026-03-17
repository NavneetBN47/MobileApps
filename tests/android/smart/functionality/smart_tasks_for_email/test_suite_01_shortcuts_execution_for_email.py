from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
import datetime

pytest.app_info = "SMART"


class Test_Suite_01_Shortcuts_Execution_For_Email(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.photo = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_execute_smart_tasks_with_email_through_camera(self):
        """
        Requirements:
          1. C31461717	'Camera' button redirection from Select a Source pop-up 
          2. C31461723	"Home" button behavior from Your file is processing pop up 
          3. 
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Shortcuts tile
          4. Create a Shortcuts with single email
          5. Select new Shortcuts from step 4
          6. Select Camera
          7. Select Allow Access to Camera, and capture with manual mode
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

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
          9. Verify Home screen
        """
        shortcuts_name = "{}_{:%d_%H_%M_%S}".format("camera_email", (datetime.datetime.now()))
        self.__load_shortcuts_source_files_screen(self.email_address, shortcuts_name, is_invisible=False)
        self.shortcuts.click_camera_btn()
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT, mode="document")
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_next_btn()
        self.shortcuts.verify_shortcuts_start_preview_screen()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen()
        self.shortcuts.click_shortcuts_home_btn()
        self.home.verify_home_nav()

    def test_02_execute_shortcut_with_email_through_photos(self):
        """
        Requirements:
          1. C33559183	Add shortcut screen after tapping create your own shortcuts
          2. C31461666	Add shortcut screen after tapping create your own shortcuts
          3. C31461719	'Files&Photos' button redirection from Select a Source pop-up 
          4. C31461722	"Continue" button behavior from Your file is processing pop up
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Shortcuts tile
          4. Create a Shortcuts with single email
          5. Select new Shortcuts from step 4
          6. Select Files & Photos
          7. Select My Photo - > Any photo
          8. Click on Start button
          9. Click on More Option button

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
          9. Verify Preview  screen
        """
        shortcuts_name = "{}_{:%H_%M_%S}".format("files_photo_email", (datetime.datetime.now()))
        self.__load_shortcuts_source_files_screen(self.email_address, shortcuts_name, is_invisible=False)
        self.shortcuts.click_files_photo_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.photo.select_recent_photo_by_index()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen()
        self.shortcuts.click_more_options_btn()
        self.preview.verify_bottom_nav(self.preview.SHARE_BTN)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_shortcuts_source_files_screen(self, email_address, shortcuts_name, is_invisible=False):
        """
        - Load Home screen.
        - CLick on Shortcuts tile on Home screen
        - Click on Add Shortcut button
        - Click on Create your own Shortcut button
        - Click on Email button
        - Type Email address
        - Click on Add to Shorcut button
        - Click on Add to Shortctu button
         Save new smart task
        - Select this smart task
        :param shortcuts_name
        :param email_address
        :param invisible: True or False for source file from Scanner
        """
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_email(email_address)
        self.fc.flow_save_shortcuts(invisible=is_invisible, shortcuts_name=shortcuts_name)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()