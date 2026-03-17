import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"

class Test_Suite_03_Novelli_UI(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Loaded printer is not Novelli")

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.preview = cls.fc.fd["preview"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.share = cls.fc.fd["share"]
        cls.files = cls.fc.fd["files"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.printer_info = cls.p.get_printer_information()
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=False, instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(stack=cls.stack)

    def test_01_duplex_print_end_to_end(self):
        """
        Description: C29099794, C29142885, C29074896, C29093895, C29092779, C29074900, C29142908 & C29776174, C29142861, C29142862
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select an image
         6. Select 4x6 Two-sided page size
         7. Dismiss coachmark message
         8. Select Print Preview button
         9 Select Print button

        Expected Results:
         6. Verify Two-sided preview page
          Verify Rotate button is invisible
         8. Verify Two-sided Print Preview page
         9. Verify "This print requires two-sided..." popup
        """
        self.fc.load_two_sided_preview_screen_for_novelli(self.p)
        self.common_preview.verify_rotate_btn(invisible=True)
        self.preview.select_toolbar_icon(Preview.PRINT)
        self.preview.verify_preview_screen_title(Preview.PRINT_PREVIEW_TITLE)
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_button(Preview.PRINT)
        self.preview.verify_requires_two_sided_paper_popup()

    @pytest.mark.parametrize("page_size", ["5x5_square", "4x12_panorama", "4x6_standard", "5x7" , "letter", "a4"])
    def test_02_one_side_end_to_end(self, page_size):
        """
        Description C29093894 & C29092778
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos/Recent photos
         5. Select an image
         6. Select page size based on page_size param
         7. Select Print Preview
         8. Select Print on psp
        Expected Results:
         6. Verify single side preview screen
         7. Verify single side Print preview screen
         8. Dismissing the Print popup
        """
        page_size_map = {
            "5x5_square": Preview.PRINT_SIZE_5x5,
            "4x12_panorama": Preview.PRINT_SIZE_4x12,
            "4x6_standard": Preview.PRINT_SIZE_4x6,
            "5x7": Preview.PRINT_SIZE_5x7,
            "letter": Preview.PRINT_SIZE_5x11,
            "a4": Preview.PRINT_SIZE_A4
        }
        self.fc.go_to_home_screen()
        self.fc.add_printer_by_ip(printer_ip=self.printer_info["ip address"])
        self.fc.dismiss_tap_here_to_start()
        self.home.close_smart_task_awareness_popup()
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.verify_select_photos_btn()
        self.photos.select_multiple_photos(end=1)
        self.photos.select_next_button()
        self.preview.verify_print_size_screen()
        self.preview.select_print_size_btn(page_size_map[page_size])
        self.preview.verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.preview.select_print_preview_button()
        self.preview.verify_preview_screen_title(Preview.PRINT_PREVIEW_TITLE)
        self.preview.dismiss_print_preview_coach_mark()
        self.preview.select_toolbar_icon(Preview.PRINT)
        self.preview.dismiss_print_preview_coach_mark()

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_03_save_duplex_images(self, file_type):
        """
        Description: C29776176, C29776167, C29776177 & C29776173
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select the fish image from the jpg album(should be the first image)
         6. Select 4x6 Two-sided page size
         7. Select Share/Save
         8. Change the filename
         9. Select Save
        Expected Results:
         8. Verify filename updated
         9. Verify front page jpg was saved as "$FILENAME-1.jpg"
            Verify back page jpg was saved as "$FILENAME-2.jpg"
            Verify PDF file can be saved success
        """
        file_name = "{}_{}".format(self.test_03_save_duplex_images.__name__, file_type)
        self.fc.load_two_sided_preview_screen_for_novelli(self.p)
        self.preview.select_toolbar_icon(Preview.SHARE_AND_SAVE_BTN)
        self.common_preview.rename_file(file_name)
        self.common_preview.select_file_type(self.common_preview.BASIC_PDF if file_type == "pdf" else self.common_preview.IMAGE_JPG)
        self.preview.verify_file_type_selected("Basic PDF" if file_type == "pdf" else file_type, raise_e=True)
        self.preview.select_button(Preview.SHARE_AND_SAVE_BTN)
        self.fc.save_file_and_handle_pop_up(go_home=True)
        self.fc.go_hp_smart_files_screen_from_home(select_tile=True)
        if file_type == "pdf":
            self.files.verify_file_name_exists("{}.pdf".format(file_name))
        else:
            folder_name = "{}({})".format(file_name, 2)
            self.files.select_folder_from_list(folder_name)
            self.files.verify_file_name_exists("{}_1.jpg".format(file_name))
            self.files.verify_file_name_exists("{}_2.jpg".format(file_name))

    def test_04_multiple_images(self):
        """
        Description: C29636132, C29392407, C29392406 & C29136373, C29392408
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Two images from Photo folder
         5. Select 4x6 Two-sided page size
         6. Select 4x6 Standard size
         7. Delete one page
         8. Click on Back button
        Expected Results:
         4. Verify page size screen
            Verify "This format is only available..." text
         5. Verify page size screen
         6. Verify Preview screen
         8. Verify page size screen
            Verify "This format is only available..." text
        """
        self.fc.go_to_home_screen()
        self.fc.add_printer_by_ip(printer_ip=self.printer_info["ip address"])
        self.fc.dismiss_tap_here_to_start()
        self.home.close_smart_task_awareness_popup()
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_multiple_photos(end=3)
        self.photos.verify_multi_selected_photos_screen()
        self.photos.select_next_button()
        self.preview.verify_print_size_screen()
        self.common_preview.verify_two_side_print_unavailable()
        self.preview.select_print_size_btn(Preview.PRINT_SIZE_4x6_TWO_SIDED, change_check=None)
        self.preview.verify_print_size_screen()
        self.preview.select_print_size_btn(Preview.PRINT_SIZE_4x6)
        self.preview.verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.preview.select_delete_page_icon()
        self.preview.select_delete_btn()
        self.preview.select_navigate_back()
        self.preview.verify_print_size_screen()
        self.common_preview.verify_two_side_print_unavailable()

    def test_05_verify_transform_function(self):
        """
        Description: C29142882, C29092782, C291492865, C29142876
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select a photo
         5. Select on 4x6 2-Sided size
         6. Click on Back button
         7. Click on Front button
         8. Click on Print Preview button
         7. Click on Transform button
         9. Click on Rotate button
         10. Select different rotate type (Left / Right / Flip H / Flip V)
         11. Click on Done button
         12. Click on Resize & Move button
         13. Select different resize type (Original / Fit to Page / Fill Page)
         14. Click on Done button
         15. Click on Done button

        Expected Results:
         6. Back Preview screen is selected
         7. Front Preview screen is selected
         8. Verify Transform button displays on screen
         9. Verify Transform screen
         10. Verify Rotate screen
         11. Verify rotate type select success
         12.Verify Resize & Move screen
         13.Verify each resize type is selected success
         15. Verify Print Preview screen
        """
        self.fc.load_two_sided_preview_screen_for_novelli(self.p)
        self.common_preview.verify_rotate_btn(invisible=True)
        self.preview.select_print_preview_button()
        self.preview.verify_preview_screen_title(Preview.PRINT_PREVIEW_TITLE)
        self.preview.dismiss_print_preview_coach_mark()
        self.common_preview.select_preview_pan_view()
        self.preview.verify_an_element_and_click(Preview.PAPER)
        self.preview.select_navigate_back(index=1)
        preview_before_edit = self.preview.preview_img_screenshot()
        self.preview.select_transform_options(Preview.PREVIEW_IMAGE)
        transform_img_before_edit = self.preview.preview_img_screenshot()
        self.preview.select_transform_options(Preview.TF_RESIZE_TXT, tf_option_select=Preview.TF_RESIZE_MOVE_OPTIONS[1])
        self.preview.select_done()
        image_after_resize_edit = self.preview.preview_img_screenshot()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_resize_edit) > 0
        self.preview.select_transform_options(Preview.TF_ROTATE_TXT, tf_option_select=Preview.TF_ROTATE_OPTIONS[2])
        self.preview.select_done()
        image_after_rotate_edit = self.preview.preview_img_screenshot()
        self.preview.select_done()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_rotate_edit) > 0
        assert saf_misc.img_comp(image_after_resize_edit, image_after_rotate_edit) > 0
        preview_after_edit = self.preview.preview_img_screenshot()
        assert saf_misc.img_comp(preview_before_edit, preview_after_edit) > 0