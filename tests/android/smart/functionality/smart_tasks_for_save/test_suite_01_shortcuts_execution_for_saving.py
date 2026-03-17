from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import *
import datetime

pytest.app_info = "SMART"


class Test_Suite_01_Shortcuts_Execution_For_Saving(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.photo = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    def test_01_execute_shortcuts_with_saving_for_dropbox(self):
        """
        Requirements:
          1. C31461712	"Start Shortcut" button behavior after creating a shortcut for 1-st time 
          2. C31461735	Source selection dialog when Printer is NOT selected
          3. C31461724	"Activity" button behavior from Your file is processing pop up
          
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for saving with dropbox
          5. Start a smart task from step4
          6. Click Files, then select PDFs, and select a .pdf file from PDFs
          7. Click on Start button

        Expected Result:
          7. Verify the Smart Task complete popup
        """
        shortcuts_name = "{}_{:%d_%H_%M_%S}".format("saving_dropbox", (datetime.datetime.now()))
        self.__load_shortcuts_source_files_screen(False, shortcuts_name, is_invisible=False)
        self.shortcuts.click_files_photo_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.files.load_downloads_folder_screen()
        self.files.select_file(self.pdf_fn)
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen(timeout=20)
        self.shortcuts.click_activity_btn()
        self.notification.verify_mobile_fax_option()
        self.notification.verify_shortcuts_option()

    def test_02_execute_shortcuts_with_saving_for_googledrive(self):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for saving with dropbox
          5. Start a smart task from step4
          6. - Click Scanner, then select Scan
             - Click Photos, then select My Photo, and select a photo
          7. Click on Start button

        Expected Result:
          7. Verify the Smart Task complete popup
        """
        shortcuts_name = "{}_{:%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.__load_shortcuts_source_files_screen(True, shortcuts_name, is_invisible=False)
        self.shortcuts.click_files_photo_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.photo.select_recent_photo_by_index()
        self.shortcuts.click_start_btn()
        self.shortcuts.verify_your_shortcut_is_in_progress_screen(timeout=20)
        self.shortcuts.click_activity_btn()
        self.notification.verify_mobile_fax_option()
        self.notification.verify_shortcuts_option()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_shortcuts_source_files_screen(self, is_google_drive, shortcuts_name, is_invisible=False):
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
        self.fc.add_create_you_own_shortcuts_for_saving(is_new=True, is_google_drive=is_google_drive)
        self.fc.flow_save_shortcuts(invisible=is_invisible, shortcuts_name=shortcuts_name)
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()