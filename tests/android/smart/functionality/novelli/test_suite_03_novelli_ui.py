from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from SAF.misc import saf_misc
import time

import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Novelli_UI(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Loaded printer is not Novelli")

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.hpps = cls.fc.flow[FLOW_NAMES.HPPS]
        cls.hpps_trapdoor = cls.fc.flow[FLOW_NAMES.HPPS_TRAPDOOR]
        cls.hpps_job = cls.fc.flow[FLOW_NAMES.HPPS_JOB_NOTIFICATION]

        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    def test_01_duplex_print_end_to_end(self):
        """
        Description: C29099794, C29142885, C29074896, C29093895, C29092779, C29074900, C29142908 & C29776174
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select an image
         6. Select 4x6 Two-sided page size
         7. Select Print
         8. Select Print button
         9. Select Continue button
        Expected Results:
         6. Verify Two-sided preview page
          Verify Rotate button is invisible
         7. Verify PSP Two-sided Print Preview page
         8. Verify "This print requires two-sided..." popup
         9. Verify Print job was successful
        """
        self.fc.load_two_sided_preview_screen_for_novelli(self.p, self.bonjour_name)
        self.preview.verify_rotate_button(invisible=True)
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.hpps.agree_and_accept_terms_and_condition_if_present()
        self.hpps_trapdoor.verify_printer_preview_screen(two_sided=True)
        self.hpps_trapdoor.select_print()
        self.hpps_trapdoor.verify_requires_two_sided_paper_popup()
        self.hpps_trapdoor.select_requires_two_sided_paper_popup_btn("continue")
        self.fc.verify_print_job_success(self.p)

    @pytest.mark.parametrize("page_size", ["square", "panorama", "4x6", "5x7" , "5x11", "a4"])
    def test_02_one_side_end_to_end(self, page_size):
        """
        Description C29093894 & C29092778
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select an image
         6. Select page size based on page_size param
         7. Select Print
         8. Select Print on psp
        Expected Results:
         6. Verify single side preview screen
         7. Verify single side psp preview screen
         8. Verify Successful print job
        """
        page_size_map = {
            "square": self.preview.PRINT_SIZE_5x5,
            "panorama": self.preview.PRINT_SIZE_4x12, 
            "4x6": self.preview.PRINT_SIZE_4x6, 
            "5x7": self.preview.PRINT_SIZE_5x7, 
            "5x11": self.preview.PRINT_SIZE_5x11, 
            "a4": self.preview.PRINT_SIZE_A4
        }
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_recent_photo_by_index()
        self.preview.select_print_size(page_size_map[page_size])
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.hpps.agree_and_accept_terms_and_condition_if_present()
        self.hpps_trapdoor.verify_printer_preview_screen(two_sided=False)
        self.hpps_trapdoor.select_print()
        self.fc.verify_print_job_success(self.p)

    def test_03_flip_duplex(self):
        """
        Description: C29092782, C29099758, C29142901, C29142891, C29371527 & C29099744
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select an image
         6. Select 4x6 Two-sided page size
         7. Select Back button
         8. Select Front button
         9. Select Print and grant PSP consent
         10. Select Back button
         11. Set copy count to 3
         12. Set color to Black and White
         13. Select Front button
         14. Set copy count to 5
         15. Set color to Color
        Expected Results:
         7. Verify image changed
         8. Verify image changed
         10. Verify image changed
         11. Verify copy count changed to 3
         12. Verify color changed to Black and White
         14. Verify copy count changed to 5
         15. Verify color changed to Color
        """
        self.fc.load_two_sided_preview_screen_for_novelli(self.p, self.bonjour_name)
        init_img = self.preview.verify_two_sided_preview_img()
        self.preview.select_two_sided_page_btn("back")
        time.sleep(3)  # delay for flip animation to compelte
        back_img = self.preview.verify_two_sided_preview_img()
        assert saf_misc.img_comp(init_img, back_img) > 0.06, "Image should have changed when selecting back button"
        self.preview.select_two_sided_page_btn("front")
        time.sleep(3)  # delay for flip animation to complete
        front_img = self.preview.verify_two_sided_preview_img()
        assert saf_misc.img_comp(back_img, front_img) > 0.06, "Image should have changed when selecting front button"
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.hpps.agree_and_accept_terms_and_condition_if_present()
        self.hpps_trapdoor.verify_printer_preview_screen(two_sided=True)
        self.hpps_trapdoor.flip_two_sided_preview("back", verify=True)
        self.hpps_trapdoor.change_number_of_copies_to(3)
        self.hpps_trapdoor.change_color_mode("black_and_white")
        self.hpps_trapdoor.verify_selected_color_mode("black_and_white")
        self.hpps_trapdoor.flip_two_sided_preview("front", verify=True)
        self.hpps_trapdoor.change_number_of_copies_to(5)
        self.hpps_trapdoor.change_color_mode("color")
        self.hpps_trapdoor.verify_selected_color_mode("color")

    def test_04_psp_switch_paper(self):
        """
        Description: C29142905, C29099843, C29099842, C29371529, C29169659 & C29099841
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select an image
         6. Select 4x6 Two-sided page size
         7. Select Print
         8. Select Letter paper size
         9. Select x button on popup
         10. Select Letter paper size
         11. Select "Print Two-sided" button
         12. Select Letter paper size
         13. Select "Switch Paper" button
         14. Select 4x6 paper size
         15. Initiate print job
        Expected Results:
         7. Verify paper size is 4x6
         8. Verify PSP "Are you sure you want to switch paper?" popup
         9. Verify paper size is 4x6
         10. Verify PSP "Are you sure you want to switch paper?" popup
         11. Verify paper size is 4x6
         12. Verify PSP "Are you sure you want to switch paper?" popup
         13. Verify paper size is Letter
         14. Verify paper size is 4x6
         15. Verify print success
        """
        self.fc.load_two_sided_preview_screen_for_novelli(self.p, self.bonjour_name)
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.hpps.agree_and_accept_terms_and_condition_if_present()
        self.hpps_trapdoor.verify_printer_preview_screen(two_sided=True)
        self.hpps_trapdoor.verify_selected_paper_size("4x6")
        self.hpps_trapdoor.change_paper_size("letter")
        self.hpps_trapdoor.verify_switch_paper_popup()
        self.hpps_trapdoor.select_switch_paper_popup_btn("close")
        self.hpps_trapdoor.verify_selected_paper_size("4x6")
        self.hpps_trapdoor.change_paper_size("letter")
        self.hpps_trapdoor.verify_switch_paper_popup()
        self.hpps_trapdoor.select_switch_paper_popup_btn("print")
        self.hpps_trapdoor.verify_selected_paper_size("4x6")
        self.hpps_trapdoor.change_paper_size("letter")
        self.hpps_trapdoor.verify_switch_paper_popup()
        self.hpps_trapdoor.select_switch_paper_popup_btn("switch")
        self.hpps_trapdoor.verify_selected_paper_size("letter")
        self.hpps_trapdoor.change_paper_size("4x6")
        self.hpps_trapdoor.verify_selected_paper_size("4x6")
        self.hpps_trapdoor.select_print()
        self.hpps_trapdoor.verify_requires_two_sided_paper_popup()
        self.hpps_trapdoor.select_requires_two_sided_paper_popup_btn("continue")
        self.fc.verify_print_job_success(self.p)

    def test_05_preview_large_image(self):
        """
        Description: C29364549
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select an image from the jpeg_oversized album
         6. Select 4x6 Two-sided page size
        Expected Results:
         6. Verify Two-sided preview screen
        """
        self.fc.load_two_sided_preview_screen_for_novelli(self.p, self.bonjour_name, photo_album="jpeg_oversized")

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_06_save_duplex_images(self, file_type):
        """
        Description: C29776176, C29776167, C29776177 & C29776173
         1. Load Home screen
         2. Load Novelli Printer
         3. Select View & Print on Bottom navbar
         4. Select Photos
         5. Select the fish image from the jpg album(should be the first image)
         6. Select 4x6 Two-sided page size
         7. Select Save
         8. Change the filename
         9. Select Save
        Expected Results:
         7. Filename is "fish"
         8. Verify filename updated
         9. Verify front page jpg was saved as "$FILENAME-1.jpg"
          Verify back page jpg was saved as "$FILENAME-2.jpg"
        """
        file_name = self.test_06_save_duplex_images.__name__
        self.fc.load_two_sided_preview_screen_for_novelli(self.p, self.bonjour_name)
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        assert self.preview.verify_file_name() == "fish", 'filename should be "fish"'
        self.preview.rename_file(file_name)
        assert self.preview.verify_file_name() == file_name, f'filename should be "{file_name}"'
        self.preview.select_file_type(self.preview.BASIC_PDF if file_type == "pdf" else self.preview.IMAGE_JPG)
        self.preview.select_action_btn(change_check=None)
        if file_type == "pdf":
            self.local_files.save_file_to_downloads_folder(file_name)
            self.fc.verify_existed_file("{}/{}.pdf".format(TEST_DATA.MOBILE_DOWNLOAD, file_name))
        else:
            self.fc.verify_existed_file("{}/{}-1.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))
            self.fc.verify_existed_file("{}/{}-2.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))
