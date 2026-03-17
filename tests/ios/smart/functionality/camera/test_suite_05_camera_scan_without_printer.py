import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.preview import Preview
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_05_Camera_Scan_Without_Printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.preview_ui = cls.common_preview.PREVIEW_UI_ELEMENTS
        cls.preview_ui.remove(cls.common_preview.REORDER_BTN)
        cls.gmail = cls.fc.fd["gmail"]
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.files = cls.fc.fd["files"]
        cls.gmail_api = cls.fc.fd["gmail_api"]
        cls.share = cls.fc.fd["share"]
        cls.stack = request.config.getoption("--stack")
        cls.device_name = request.config.getoption("--mobile-device")
        cls.fc.go_home(stack=cls.stack)
        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    @pytest.fixture(scope="function", autouse="true")
    def return_home(self):
        self.fc.go_to_home_screen()
        self.fc.go_camera_screen_from_home(tile=True)
    
    def test_03_verify_manual_capture_print_preview(self):
        """
        C31299874
        1. Select any printer and tap the Scan tile, take a manual picture, and move past adjust boundaries
        Expected results:
            - verify print preview ui and there is no X button when only one scanned item
        """
        self.fc.multiple_manual_camera_capture(1, flash_option=i_const.FLASH_MODE.FLASH_AUTO)
        self.common_preview.verify_toolbar_icons()
        self.common_preview.verify_array_of_elements(self.preview_ui)
        self.common_preview.select_delete_page_icon()
        self.common_preview.verify_preview_edit_options(verify_delete_option=False)

    def test_04_verify_auto_capture_print_preview(self):
        """
        C31299875
        1. Select any printer and auto capture any image
        Expected results:
            - verify print preview ui
        """
        self.camera.select_auto_option()
        self.camera.capture_multiple_photos_by_auto_mode(device_name=self.device_name)
        self.common_preview.verify_preview_screen()
        self.common_preview.verify_toolbar_icons()
        self.common_preview.verify_array_of_elements(self.preview_ui)
    
    def test_06_verify_email_share_functionality(self):
        """
        C31299781 - Share captured image from camera scan
        C31299782 - Share multi page scan
        C31299886 - Share scanned image via email
        """
        self.camera.select_auto_option()
        self.camera.capture_multiple_photos_by_auto_mode(no_of_images=1, timeout=300, device_name=self.device_name)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        file_name = self.test_06_verify_email_share_functionality.__name__
        self.common_preview.rename_file(file_name)
        self.common_preview.select_file_type(self.common_preview.IMAGE_JPG)
        self.common_preview.verify_an_element_and_click(self.common_preview.SHARE_SAVE_BTN)
        self.share.select_gmail()
        subject = "{}_{}".format("test_06_verify_email_share", self.driver.driver_info["udid"])
        self.gmail.compose_and_send_email(self.email_address, subject_text=subject)
        msg_id = self.gmail_api.search_for_messages(q_from=self.email_address,
                                                             q_to=self.email_address, q_unread=True,
                                                             q_subject=subject, timeout=300)
        attachment_names = self.gmail_api.get_attachments(msg_id[0][u'id'])
        for index, name in enumerate(attachment_names):
            temp_name = name.split("-")
            attachment_names[index] = "_".join(temp_name)
        self.gmail_api.delete_email(msg_id)
        assert all([file_name in str(name) for name in attachment_names])
        assert len(attachment_names) == 1
    
    def test_09_save_functionality_for_multi_page_addition(self):
        """
        C31299787 - Save multi page scan in JPG format
        1. Add any printer and tap the scan tile
        2. Capture more than 6 images and save them to HP Smart
        3. Go to home screen and tap on "files & photos" icon and navigate to the saved folder
        Expected Results:
            - after step 3 verify the scanned results should be saved as multiple images in one folder
        :return:
        """
        number_of_images = 6
        self.fc.multiple_manual_camera_capture(number_of_images)
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        file_name = self.test_09_save_functionality_for_multi_page_addition.__name__
        self.common_preview.rename_file(file_name)
        self.common_preview.select_file_type(self.common_preview.IMAGE_JPG)
        self.common_preview.verify_an_element_and_click(self.common_preview.SHARE_SAVE_BTN)
        self.fc.save_file_and_handle_pop_up(go_home=True)
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.select_folder_from_list(f"{file_name}({number_of_images})")
        self.files.verify_file_name_exists("{}.jpg".format(file_name))
        for i in range(1, number_of_images):
            self.files.verify_file_name_exists("{}_{}.jpg".format(file_name, i))
    
    def test_11_verify_page_addition_functionality(self):
        """
        C14728098
        1. Add a printer and tap the scan tile
        2. Select camera as source and take a picture, proceed to print preview
        3. Tap add page icon in print preview and take another picture
        Expected Results:
            - verify that add page is working and pictures have x button
        """
        number_of_images = 2
        self.fc.multiple_manual_camera_capture(number_of_images)
        assert self.common_preview.verify_delete_page_x_icon()
        assert self.common_preview.verify_preview_page_info()[1] == number_of_images

    def test_15_verify_source_elements_without_printer(self):
        """
        Verify source elements for printer without scanner
        similar to testcase C37667651, C31299808
        """
        self.fc.go_to_home_screen()
        self.home.verify_rootbar_scan_icon()
        self.home.select_scan_icon()
        self.camera.select_allow_access_to_camera_on_popup()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.scan.select_source_button()
        self.scan.verify_source_options_for_printer_without_scanner()
        assert self.scan.get_number_of_available_sources() == 2, "Scanner source present with no printer added!"