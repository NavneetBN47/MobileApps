import pytest, re
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"


class Test_Suite_07_add_files_send_fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.welcome = cls.fc.fd["welcome"]
        cls.photos = cls.fc.fd["photos"]
        cls.files = cls.fc.fd["files"]
        cls.camera = cls.fc.fd["camera"]
        cls.scan = cls.fc.fd["scan"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_files_and_photos_ui(self):
        """
        Load to Compose fax screen and verify files and photos ui
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.verify_add_your_files_options()
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.photos.select_allow_access_to_photos_popup()
        self.files.verify_files_screen()
        self.files.verify_google_drive_image()
        self.files.verify_google_photos()
        self.files.verify_drop_box_image()
        self.files.verify_box_image()
        self.files.verify_ever_note_image()
        self.files.verify_other_image()

    def test_02_add_multiple_images(self):
        """
        C31379767 - Upload multi-page file by Camera under Add Files section
        Requirements:
            1.Launch the app and sign in into App Settings with valid credentials
            2.Add printer to the carousel
            3.Tap on on Mobile Fax tile (Enable the tile from Personalize if not present in Home screen) 
              and navigate to "Compose Fax" screen
            4.Insert recipient's and sender's details as asked
            5.Tap on "Camera" under Add files section
            6.Tap on source and select Files & Photos
            7.Choose any image
            8.Adjust the boundaries and tap on Next from top right corner of the screen
            9.Tap on "+" button from preview screen to add more images.
            10.Select image (Repeat step 2,3 for image selection)
            11.Tap on "Next" (for Android)/ Tap on ""Continue to Fax" (for iOS) from preview screen
            12.Tap on "Send Fax" button
        Verify:
            1.Verify that the file has been uploaded successfully under "Files and Cover page" 
              section of Compose Fax screen.
            2.Fax should be sent successfully.
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.verify_add_your_files_options()
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.photos.select_allow_access_to_photos_popup()
        self.fc.select_photo_from_photo_picker(no_of_photos=2, select_all_files=False)
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        sleep(2)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_file_item_magnifier()
        self.compose_fax.click_close_preview()

    @pytest.mark.parametrize("pages", [1,3])
    def test_03_add_camera_images_and_send_fax(self, pages):
        """
        C31379763 - Camera
        C31379764 - send fax from camera with 1 photo capture
        C31379765 - send fax from camera with multiple photos capture
        Requirements:
            1.Launch the app and tap on Send Fax tile and navigate to "Compose Fax" screen
            2.Tap on "Camera" under Add files section
            3.Capture a new image with Manual mode
            4.Adjust the boundaries and tap on Next from top right corner of the screen
            5'.Tap on "+" button from "Preview" screen and Capture image
            6'.Repeat above steps (2,3,4) two more time (Total 3 captured images)
            7.From Preview screen tap on "Next" button
            8.Tap on Magnifier glass icon under "Files and Cover page" section which opens preview screen
            9.Close the preview screen and tap on "Send Fax" button
        Verify:
            1.Verify that camera scan screen of smart app should be displayed
            2.Verify that the file has been uploaded successfully under "Files and Cover page" 
             section of Compose Fax screen.
            3.Fax should be sent successfully.
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.CAMERA_BTN)
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_btn()
        self.fc.multiple_manual_camera_capture(number=pages, preview_title="fax_preview")
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        sleep(2)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_file_item_magnifier()
        self.compose_fax.click_close_preview()
        sleep(1)
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_status(timeout=600)

    def test_04_add_scan_images_and_send_fax(self):
        """
        C31379771 - Scan and upload multi-page file on Compose Fax page
        Requirements:
            1.Launch HP Smart, add Printer
            2.Go to Compose Fax and Perform a single page / multi-page file scan
            3.Tap on "Send Fax" button
        Validate:
            1. Verify that "Add Files" section should have the file captured from printer scanner
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.welcome.allow_notifications_popup(raise_e=False)
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.SCANNER_BTN)
        self.scan.select_scanner_if_first_time_popup_visible()
        if self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_COACH_MARK, raise_e=False):
            self.driver.click_by_coordinates(area="mm")
        assert not self.scan.verify_scan_not_available(), "Scan Not Available message for printer: {}".format(self.p.get_printer_information())
        self.scan.select_scan_job()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.select_add_page()
        self.scan.select_scan_job()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        assert self.preview.get_no_pages_from_preview_label() == 2
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        sleep(5)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_status(timeout=600)
    
    def test_05_delete_files_from_camera_scan(self):
        """
        C31379810 - Delete Captured Images In Hp Smart Preview Screen
        C31379811 - Attach Camera Scan to Fax
        Requirements:
            1.Launch HP Smart
            2.Perform a multi-page scan from the Camera
            3.From Preview screen choose Fax option
            4.In the Compose Fax screen, the file captured should be under Add Files section
            5.Go Back to the Preview Screen
            6.Delete one image and tap on Fax button
            5'.Tap on Delete Button on the Compose Fax page under Add Files section
        Validate:
            1.Verify that Preview Screen should be displayed
            2.Verify that Compose Fax screen now has one image lesser than the total images captured in the Add Files section
            1'.Verify that all the files uploaded to the Fax page should be deleted
        """
        self.fc.go_camera_screen_from_home()
        self.fc.multiple_manual_camera_capture(3)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_button(self.common_preview.FAX_BTN)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=90)
        self.compose_fax.verify_compose_fax_screen()
        _, _number_pages = self.compose_fax.get_added_file_information()
        assert _number_pages == "3 pages", f"Pages count should be 3 pages"
        self.compose_fax.delete_added_file()
        self.compose_fax.verify_no_updated_file()
        self.compose_fax.click_back_btn()
        # Back once more to Preview (from Fax Preview)
        self.preview.select_navigate_back()
        self.common_preview.verify_preview_screen()
        self.preview.select_delete_pages_in_current_job(no_of_pages_to_delete=1)
        self.common_preview.select_button(self.common_preview.FAX_BTN)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=90)
        self.compose_fax.verify_compose_fax_screen()
        _, _number_pages = self.compose_fax.get_added_file_information()
        assert _number_pages == "2 pages", f"Pages count should be 2 pages"
        self.compose_fax.delete_added_file()
        self.compose_fax.verify_no_updated_file()
        
    @pytest.mark.parametrize("number", [1, 2])
    def test_06_upload_file_from_printer_scan(self, number):
        """
        C31379770 - Send Fax From Scanner Single Page 
        C31379771 - Scan and upload multi-page file on Compose Fax page
        C31379772 - Verify the uploaded file name from Printer Scanner
        Requirements: 
            1.Install and launch HP Smart
            2.Add a printer which has scanner glass
            3.Go to App Settings and log in     	
            4.Tap on "Printer Scan" from bottom action bar of the Home screen and complete scan job
            5.Tap on "Fax" from preview page
            6.Observe the file name
        Validate:
            1.User should navigate to "Compose Fax"
            2.The filename should be in the form YYYY-MM-DD_HHMM{2 rand char}
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.welcome.allow_notifications_popup(raise_e=False)
        self.fc.go_scan_screen_from_home(self.p)
        self.scan_nav_to_preview()
        if number == 2:
            self.common_preview.select_add_page()
            self.scan_nav_to_preview()
        self.common_preview.select_button(self.common_preview.FAX_BTN)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=90)
        self.compose_fax.verify_compose_fax_screen()
        file_name, _ = self.compose_fax.get_added_file_information()
        assert re.search("\d{4}-\d{2}-\d{2}_\d{6}", file_name), f"File name should match regex (e.g. Document_2024-01-15_062446, 2024-01-15_062446). Actual value: {file_name}"

    def scan_nav_to_preview(self):
        self.scan.select_scan_job_button()
        sleep(2)
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
