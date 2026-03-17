import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA, WEBVIEW_URL

pytest.app_info = "SMART"


class Test_Suite_04_Compose_Fax_Screen(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.recipient_name = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]["name"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([TEST_DATA.ONE_PAGE_PDF, TEST_DATA.PDF_4PAGES_12MB,
                                             TEST_DATA.PDF_BIG_PDF_30MB, TEST_DATA.PDF_MORE_THAN_50PAGES])

        def clean_up_class():
            # Clean up Download and Pictures folders before testing
            cls.fc.clean_up_download_and_pictures_folders()
        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("file_name", [TEST_DATA.ONE_PAGE_PDF, TEST_DATA.PDF_4PAGES_12MB])
    def test_01_added_file_number_pages(self, file_name):
        """
        Description:
            1/ Load Compose Fax screen
            2/ Adding file with single page/multiple pages (2 pages)
        Expected Result:
            2/ Observe Compose Fax with page number
        """
        timeout = {TEST_DATA.ONE_PAGE_PDF: 10, TEST_DATA.PDF_4PAGES_12MB: 30}
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.__add_file_from_file_photos(file_name)
        # It take some time to load file to Softfax Compose fax screen
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=20)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=timeout[file_name])
        self.compose_fax.verify_added_pages_number(1 if file_name == TEST_DATA.ONE_PAGE_PDF else 4)

    @pytest.mark.parametrize("file_name", [TEST_DATA.PDF_BIG_PDF_30MB, TEST_DATA.PDF_MORE_THAN_50PAGES])
    def test_02_add_file_more_than_limited_size_page_from_compose_fax_screen(self, file_name):
        """
        Description: C31379753
            1/ Load Compose Fax screen
            2/ Adding file with  > 20 MB / > 50 pages
        Expected Result:
            2/ Error popup for size/pages of file
        """
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.__add_file_from_file_photos(file_name)
        self.preview.verify_fax_limit_popup()

    @pytest.mark.parametrize("file_name", [TEST_DATA.PDF_BIG_PDF_30MB, TEST_DATA.PDF_MORE_THAN_50PAGES])
    def test_03_add_file_more_than_limited_size_page_from_preview(self, file_name):
        """
        Description:
            1/ Load Compose Fax screen -> load Home screen -> Load Files & Photos
            2/ Click on PDFs button
            3/ Select file with  > 20 MB / > 50 pages
            4/ Click on Fax button on Preview screen
        Expected Result:
            4/ Error popup for size/pages of file
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_name)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        self.preview.verify_fax_limit_popup()

    def test_04_delete_some_pages_after_adding_multiple_pages_from_camera_scan(self):
        """
        Description:C31379810, C31379811
            1/ Load Compose Fax screen with logging in
            2/From Home screen, load Preview screen with multiple page (3 pages) from camera scan
            3/ Click on Fax button
            4/ Press Back button to Preview screen -> Delete 1 page
            5/ Click on Fax button again
        Expected Result:
            3/ Check 3 pages in added file in Files and Cover Page
            5/ Check 2 pages in added file in Files and Cover Page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages(from_tile=False, number_pages=3)
        self.preview.verify_preview_screen()
        assert self.preview.verify_preview_page_info()[1] == 3, "Page count should be 3"
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        #Todo: wait for designer's reply on timeout of uploading file on Softfax
        self.compose_fax.click_fax_feature_update_dismiss_btn(raise_e=False)
        self.compose_fax.verify_uploaded_file(timeout=60)
        self.compose_fax.verify_added_pages_number(3)
        self.compose_fax.delete_added_file()
        self.driver.press_key_back()
        self.preview.verify_preview_screen()
        self.preview.select_page_options_btn(self.preview.DELETE_BTN)
        assert self.preview.verify_preview_page_info()[1] == 2, "Page count should be 2"
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        #Todo: wait for designer's reply on timeout of uploading file on Softfax
        self.compose_fax.verify_uploaded_file(timeout=60)
        self.compose_fax.verify_added_pages_number(2)

    def test_05_add_file_after_deleting_file(self):
        """
        Description: C31379701, C24628885
            1/ Load Compose Fax screen wih logging in
            2/ Added a valid file ( < 20MB and < 50 pages)
            3/ Click on trash can icon to delete added file
            4/ Add a valid file again
        Expected Result:
            2/ file is added successfully
            3/ File is disappear by displaying 3 buttons in file and coverage page (files $ photos, camera, printer scan)
            4/ A file is added successfully
        """
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.__add_file_from_file_photos(TEST_DATA.ONE_PAGE_PDF)
        self.compose_fax.verify_compose_fax_screen()
        # Todo: wait for designer's reply for updating timeout.
        self.compose_fax.verify_uploaded_file(timeout=30)
        self.compose_fax.delete_added_file()
        self.compose_fax.verify_no_updated_file()
        self.__add_file_from_file_photos(TEST_DATA.ONE_PAGE_PDF)
        self.compose_fax.verify_compose_fax_screen()
        # Todo: wait for designer's reply for updating timeout.
        self.compose_fax.verify_uploaded_file(timeout=30)

    def test_06_menu_clear_all_fields(self):
        """
        Description: C31379704, C31379703, C31379873, C31379700, C31379702, C31379871, C24628887, C24628889
            1/ Load Compose Fax screen
            2/ Enter Recipient phone number
            3/ Click on Clear all fields on menu
            4/ Click on Home
        Expected Result:
            3/ Compose Fax screen with empty recipient phone number
            4/ Android Smart Home screen
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.compose_fax.enter_recipient_information("1234567890")  # any number
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)
        phone, name, code = self.compose_fax.get_recipient_information()
        assert (phone == ""), "Recipient phone number is not empty"
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_HOME_BTN)
        self.home.verify_home_nav()

    def test_07_save_this_contact(self):
        """
        Description: C31379717, C31379705, C31379706, C31379510, C31379509, C31379870, C31379876, C31379874, C24773509, C24773510
            1. Load Compose Fax screen
            2. Type fax number and name on To section
            3. Click on Save this contact
            4. Click on Home in menu
            5. Dismiss Exit without saving? popup by clicking on exit button
        Expected Result:
            2. Save this contact is visible
            3. - Save button is visible
               - Save this contact button is invisible
            4. Exit without saving? popup
            5. Home screen display
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"], self.recipient_name)
        self.compose_fax.verify_save_this_contact_btn()
        self.compose_fax.click_save_this_contact_btn()
        self.compose_fax.verify_save_this_contact_btn(invisible=True, raise_e=True)
        self.compose_fax.verify_saved_btn()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_HOME_BTN)
        self.compose_fax.handle_save_as_draft_popup("save_as_draft_popup_exit_bn")
        self.home.verify_home_nav()

    def test_08_add_optional_info(self):
        """
        Description: C31379728, C31379729, C31379707, C27725935
            1. Load Compose Fax screen
            2. Type fax number and name on To section
            3. Type fax number and name on From section
            4. Click on Add optional info button
            5. Click on Collapse
            6. Click on Three dot screen from Compose Fax screen
            7. Click on Home button
            8. Click on Cancel button

        Expected Result:
            4. Verify From section with:
               - Organization name displays
               - Email displays
            5. Organization name and Email part is invisible
            8. Verify Compose Fax screen

        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_compose_fax_with_information()
        self.compose_fax.click_add_optional_info_btn()
        self.compose_fax.verify_organization_name()
        self.compose_fax.verify_email()
        self.compose_fax.click_collapse_btn()
        self.compose_fax.verify_organization_name(invisible=True, raise_e=True)
        self.compose_fax.verify_email(invisible=True, raise_e=True)
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_HOME_BTN)
        self.compose_fax.handle_save_as_draft_popup("save_as_draft_popup_cancel_btn")
        self.compose_fax.verify_compose_fax_screen(timeout=10)

    def test_09_save_as_a_profile(self):
        """
        Description: C31379730, C31379731
            1. Load Compose Fax screen
            2. Type fax number and name on To section
            3. Type fax number and name on From section
            4. Click on Add optional info button
            5. Click on Save as profile button
            6. If btn_name == "cancel" button, then click on CANCEL button
               If btn_name == "save", then click on SAVE button
        Expected Result:
            5. Verify Name your Profile screen
            6. If btn_name == "cancel" button, then verify compose fax screen
               If btn_name == "save", then verify compose fax screen with profile name
        """
        profile_name = "test_09_{}".format(self.udid)
        self.__load_compose_fax_with_information()
        self.compose_fax.click_save_as_profile_btn()
        self.compose_fax.verify_name_your_profile_screen()
        self.compose_fax.click_cancel_btn()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_save_as_profile_btn()
        self.compose_fax.enter_profile_name(profile_name)
        self.compose_fax.click_save_btn()
        self.compose_fax.verify_profile_label()

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __add_file_from_file_photos(self, file_name):
        """
        - Click on File Photos button on Compose screen
        - Select file based oin PDFs
        - Verify compose screen with added file.
        :param file_name: file name
        """
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_name)
        self.preview.verify_title(self.preview.PREVIEW_TITLE)
        self.preview.select_fax_next()
    
    def __load_compose_fax_with_information(self):
        """
        1. Load Compose Fax screen
        2. Type fax number and name on To section
        3. Type fax number and name on From section
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,check_onboarding=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"], self.recipient_name)
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])