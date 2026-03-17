import pytest, os
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA, BUNDLE_ID

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Send_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.files = cls.fc.fd["files"]
        cls.photos = cls.fc.fd["photos"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        """
        Pre-requirements:
            1. Launch the app and sign in into App Settings with valid credentials
            2. Tap on on Mobile Fax tile and navigate to "Compose Fax" screen
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_app_settings()
        self.app_settings.select_mobile_fax()
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    def test_01_compose_and_send_fax(self):
        """
        C31379766 - Upload one-page file by Camera under Add Files section
        Requirements:
            1.Launch the app and sign in into App Settings with valid credentials
            2.Tap on on Mobile Fax tile (Enable the tile from Personalize if not present in Home screen)
            and navigate to "Compose Fax" screen
            3.Insert recipient's and sender's details as asked
            4.Tap on "Camera" under Add files section
            5.Tap on source and select Files & Photos
            6.Choose any image
            7.Adjust the boundaries and tap on Next from top right corner of the screen
            8.Tap on ""Continue to Fax" (for iOS) from preview screen
            9.Tap on "Send Fax" button
        Validate:
            1.Verify that the file has been uploaded successfully under "Files and Cover page" section of Compose Fax screen.
6.          2.Fax should be sent successfully.
        """
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_photo_from_photo_picker(select_all_files=False)
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        sleep(5)
        # @TODO:  Webview button click did not work so using native button click
        self.compose_fax.click_send_fax_native_btn()
        #TODO: Added timeout using Android test example
        self.send_fax_details.verify_send_fax_status(timeout=600)

    @pytest.mark.parametrize("file_type, file_name, number", [("pdf", TEST_DATA.PDF_1PAGE_1MB, 1), ("pdf", TEST_DATA.PDF_1PAGE_3MB, 1), 
                                                              ("pdf", TEST_DATA.PDF_4PAGES_12MB, 4), ("jpg", TEST_DATA.JPG_TEST, 1), 
                                                              ("png", TEST_DATA.PNG_TEST, 1)])
    def test_02_send_fax_with_local_file_uploaded(self, file_type, file_name, number):
        """
        C31379748, C31379741, C31379749, C31379750, C31379754, C31379755, C31379742, 
        C31379743, C31379751, C31379752 - Verify PNG / JPG / PDF attached on Fax
        Requirements:
            3. Insert recipient's and sender's details
            4. Tap on "Files & Photos" under Add files section
            5. Choose a file of `file_type` with name `file_name` and `number` page/s
            6. Tap on Next button and navigate to compose fax screen
            7. Tap on Magnifier glass icon
            8. Close the preview and tap on Send Fax button
        Validate:
            1. Fax should sent successfully
        """
        self.upload_file(file_type, file_name)
        sleep(2)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_file_from_hp_smart_files(file_name.split(".")[0], file_type)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        sleep(10) # The processing... message
        self.compose_fax.verify_compose_fax_screen()
        _file_name, _number_pages = self.compose_fax.get_added_file_information()
        assert file_name == _file_name, f"File name should be {file_name}"
        assert _number_pages == f"{number} page{'s' if number != 1 else ''}", f"Pages count should be {number} page{'s' if number != 1 else ''}"
        self.compose_fax.click_file_item_magnifier()
        self.compose_fax.click_close_preview()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_send_fax_status(timeout=600)

    def test_03_send_fax_with_pdf_uploaded_too_big(self):
        """
        C31379753 - Verify Softfax file size limitation popup
        Requirements:
            3. Insert recipient's and sender's details
            4. Tap on "Files & Photos" under Add files section
            5. Choose a file of size exceeding 20 MB
            6. Tap on Send Fax button
        Validate:
            1. Verify Softfax file limitation popup displays, eg: Your file must be a total of 20mb or less
        """
        self.upload_file("pdf", TEST_DATA.PDF_BIG_PDF_30MB)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_file_from_hp_smart_files(TEST_DATA.PDF_BIG_PDF_30MB.split(".")[0])
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.files.verify_file_size_exceeded_popup()

    def upload_file(self, file_type, file_name):
        """
        Upload file to Local Storage
        """
        if file_type == "pdf":
            self.driver.push_file(BUNDLE_ID.SMART, ma_misc.get_abs_path(os.path.join(TEST_DATA.DOCUMENTS_PDF_FOLDER, file_name)))
        elif file_type == "png":
            self.driver.push_file(BUNDLE_ID.SMART, ma_misc.get_abs_path(os.path.join(TEST_DATA.IMAGES_PNG_FOLDER, file_name)))
        elif file_type == "jpg":
            self.driver.push_file(BUNDLE_ID.SMART, ma_misc.get_abs_path(os.path.join(TEST_DATA.IMAGES_JPG_FOLDER, file_name)))
