import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_01_Send_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([TEST_DATA.ONE_PAGE_PDF, TEST_DATA.PDF_1PAGE_1MB, TEST_DATA.PDF_1PAGE_3MB,
                                             TEST_DATA.PDF_2PAGES_20MB, TEST_DATA.PDF_4PAGES_12MB])

        def clean_up_class():
            cls.fc.clean_up_download_and_pictures_folders()
        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("number", [1, 2])
    def test_01_send_fax_from_camera(self, number):
        """
        Description:
            C31379764, C31379765, C31379763, C31379766, C31379767
            1/ Load to Compose Fax screen
            2/ In Add Files, select file via camera
            3/ Enter valid information for recipient and sender
            4/ Click on Send fax button
            5/ Click on View Status
            6/ Observe for sending fax successfully
        Expected result:
            4/ Popup "Your fax is on its way!"
            5/ Send Fax Details:
                - Processing Documents text with recipient phone number
                - Sending document
                - Send Fax again and Cancel Fax button
            6/ Same screen on step 5 with:
                - Processing Documents text with recipient phone number
                - Fax sent success
                - Send Fax again button
        """
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.CAMERA_BTN)
        self.fc.flow_scan_capture(self.scan.SOURCE_CAMERA_OPT)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen(chk_bottom_navbar=False)
        if number == 2:
            self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
            self.scan.start_capture(change_check=self.scan.CAPTURE_CHANGE_CHECKS["document"], timeout=30)
            self.scan.select_adjust_next_btn()
            self.preview.verify_preview_screen(chk_bottom_navbar=False)
            self.preview.verify_preview_page_info()
        self.__navigate_to_send_fax_detail_screen()

    @pytest.mark.parametrize("file_names", [TEST_DATA.ONE_PAGE_PDF, TEST_DATA.PDF_1PAGE_3MB, TEST_DATA.PDF_4PAGES_12MB])
    def test_02_send_fax_from_file_photos_local_file(self, file_names):
        """
            Description: C31379748, C31379741, C31379749, C31379750, C31379754, C31379752, C31379738
                1/ Load to Compose Fax screen
                2/ In Add Files, select file from Files & Photos/Scanned Files
                3/ Enter valid information for recipient and sender
                4/ Click on Send fax button
                5/ Click on View Status
                6/ Observe for sending fax successfully
            Expected result:
                4/ Popup "Your fax is on its way!"
                6/ Same screen on step 5 with:
                    - Processing Documents text with recipient phone number
                    - Fax sent success
                    - Send Fax again button
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_names)
        self.__navigate_to_send_fax_detail_screen()

    def test_03_send_fax_from_file_photos_local_photo(self):
        """
            Description: C31379742, C31379743, C31379751
                1/ Load to Compose Fax screen
                2/ In Add Files, select file from Files & Photos/My Photos
                3/ Enter valid information for recipient and sender
                4/ Click on Send fax button
                5/ Click on View Status
                6/ Observe for sending fax successfully
            Expected result:
                4/ Popup "Your fax is on its way!"
                6/ Same screen on step 5 with:
                    - Processing Documents text with recipient phone number
                    - Fax sent success
                    - Send Fax again button
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_recent_photo_by_index()
        self.__navigate_to_send_fax_detail_screen()

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __navigate_to_send_fax_detail_screen(self):
        """
        Enter required information for recipient and sender, then navigate to Softfax details screen
        """
        self.preview.verify_title(self.preview.PREVIEW_TITLE)
        self.preview.select_fax_next()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=60)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_send_fax()
        self.send_fax_details.verify_send_fax_detail_screen()