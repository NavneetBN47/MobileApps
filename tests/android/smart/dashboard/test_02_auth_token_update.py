import pytest
import datetime
from MobileApps.resources.const.android.const import *
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES

pytest.app_info = "SMART"

class Test_Suite_01_Android_Welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        cls.dev_settings = cls.fc.flow[FLOW_NAMES.DEV_SETTINGS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        yield None
        # Clean up Download and Pictures folders after testing
        cls.fc.clean_up_download_and_pictures_folders()

    def test_01_auth_token_update(self):
        """
        The explicit goal of the this test is to sign in, wait 30 minutes, and execute a Cloud related Shortcut to see 
        if we're prompted with a login page after our waiting period. 

        Steps:
        - Open, Sign-In to App
        - Close App wait for 30 minutes
        - Create File Upload to Google Drive Shortcut and execute Shortcut 
        - Navigate back to Homescreen and validate that we are signed in
        """
        self.dev_settings.open_select_settings_page()
        self.dev_settings.toggle_shortened_token_lifespan()
        self.fc.flow_load_home_screen(create_acc=True)
        self.driver.terminate_app(self.fc.pkg_name)
        self.driver.active_sleep(300)
        self.fc.flow_home_load_shortcuts_screen()
        self.fc.load_create_you_own_shortcuts_screen()
        self.fc.add_create_you_own_shortcuts_for_saving(is_new=True, is_google_drive=True)
        self.fc.flow_save_shortcuts(invisible=False, shortcuts_name="{}_{:%d_%H_%M_%S}".format("saving_google_drive", (datetime.datetime.now())))
        self.shortcuts.click_start_shortcut_btn()
        self.shortcuts.verify_source_select_popup()
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
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.verify_nav_logo()
