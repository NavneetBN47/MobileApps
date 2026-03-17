import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from time import sleep

pytest.app_info = "SMART"

class Test_Suite_01_Image_Export_To_Other_Formats(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Define flows
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.files = cls.fc.fd["files"]
        cls.share = cls.fc.fd["share"]
        cls.home = cls.fc.fd["home"]
        cls.photo = cls.fc.fd["photos"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True, smart_advance=True)
        cls.username, cls.password = cls.login_info["email"], cls.login_info["password"]

        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    def test_01_verify_share_as_original_functionality(self):
        """
        C31299832 - Share scanned image with default format
        verify 'Share as Original' functionality - C27655335
        """
        file_name = 'scan_image_JPG'
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.create_and_save_file_using_camera_scan_and_go_home(file_name)
        self.fc.select_a_file_and_go_to_preview_screen(file_name = file_name, file_type='jpg')
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        # Turning on the share as original button
        self.common_preview.toggle_share_as_original_btn(uncheck=False)
        assert self.common_preview.verify_an_element_and_click(self.common_preview.FORMAT, click=False) is False
        assert self.common_preview.verify_an_element_and_click(self.common_preview.FILE_SIZE, click=False) is False
        # Turning off the share as original button
        self.common_preview.toggle_share_as_original_btn(uncheck=True)
        assert self.common_preview.verify_an_element_and_click(self.common_preview.FORMAT, click=False)
        assert self.common_preview.verify_an_element_and_click(self.common_preview.FILE_SIZE, click=False)
        # Turning on the share as original button
        self.common_preview.toggle_share_as_original_btn(uncheck=True)
        self.common_preview.select_button(self.common_preview.SHARE_SAVE_BTN)
        self.fc.save_file_and_handle_pop_up()
        self.common_preview.select_navigate_back()
        self.home.select_cancel()
        self.files.verify_file_name_exists(file_name + "_1.jpg")

    def test_02_verify_image_export_to_pdf(self):
        """
        verify image export to pdf - C27655339
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.save_file_to_hp_smart_files_and_go_home("scan_image_from_camera_PDF", self.common_preview.SHARE_SAVE_TITLE, file_type="PDF", go_home=False)
        self.fc.go_hp_smart_files_screen_from_home(select_tile=False)
        self.files.verify_file_name_exists("scan_image_from_camera_PDF.pdf")

    @pytest.mark.parametrize("image_format", ["png", "tif", "heif"])
    def test_03_verify_export_image_to_other_formats(self, image_format):
        """
        verify image export from PNG to other formats - C27655336
        verify image export from TIF to other formats - C27655337
        verify image export from HEIF to other formats - C27655338
        """
        images_types = {
            "png": "PNG",
            "heif": "HEIF",
            "tif": "TIF"
        }
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.create_and_save_file_using_camera_scan_and_go_home(file_name=images_types[image_format], file_type=images_types[image_format])
        self.fc.select_a_file_and_go_to_preview_screen(file_name=images_types[image_format], file_type=image_format)
        self.common_preview.dismiss_feedback_popup()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        file_types = {
            "jpg": self.common_preview.IMAGE_JPG,
            "PDF": self.common_preview.BASIC_PDF,
            "PNG": self.common_preview.IMAGE_PNG,
            "TIF": self.common_preview.IMAGE_TIF,
            "HEIF": self.common_preview.IMAGE_HEIF
        }
        file_names = []
        for file_type in file_types.keys():
            file_name = 'format_'+ image_format + "_to_" + file_type
            self.common_preview.rename_file(file_name)
            self.common_preview.select_file_type(file_types[file_type])
            self.common_preview.select_button(self.common_preview.SHARE_SAVE_BTN)
            self.share.verify_share_popup()
            self.fc.save_file_and_handle_pop_up()
            file_names.append(file_name + "." + file_type.lower())
            self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.fc.go_hp_smart_files_screen_from_home()
        for file_name in file_names:
            # Validate file saved with selected format
            self.files.verify_file_name_exists(file_name)

    def test_04_verify_image_export_to_pdf(self):
        """
        Description: C35948894
         1. Load Home screen
         2. At Home screen, Click on View & Print button
         3. Click on Albums -> Recents button
         4. Select a photo from the list
         5. Click on More Option button on Preview screen
         6. Click on Replace button
         7. Click on Albums button -> Recents -> Select a Photo

         Expected Results:
         6. Verify Files & Photos screen
         7. Verify Preview screen
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.common_preview.verify_an_element_and_click(self.common_preview.DELETE_PAGE_ICON)
        self.common_preview.select_replace_btn()
        self.photo.select_albums_tab()
        self.photo.verify_albums_screen()
        self.photo.select_recents_or_first_option()
        self.photo.verify_photos_screen()
        self.photo.select_photo_by_index(index=1)
        sleep(2)
        self.common_preview.select_print_size(raise_e=False)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE, use_str_id=True)