import pytest

from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
 
pytest.app_info = "SMART"

class Test_Suite_01_Shortcuts_Ui(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.scribble = cls.fc.flow[FLOW_NAMES.SCRIBBLE]

        # Define Variable
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    @pytest.fixture()
    def get_to_scribble_new_mark_single_page(self):
        """
        C31299623: From the Camera Scan page, scan any document, go to Preview page, and verfiy scribble option
        C31299624: After selecting scribble option, verify Scribble Page loads for a single document
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages()
        assert self.preview.verify_top_toolbar(self.preview.SCRIBBLE_BTN)
        self.preview.select_top_toolbar_btn(self.preview.SCRIBBLE_BTN)
        self.scribble.select_new_mark_button()
        assert self.scribble.verify_new_mark_page()
        self.scribble.dismiss_welcome_to_scribble_pop_up()

    def test_01_new_mark_button(self, get_to_scribble_new_mark_single_page):
        '''
        C31299625: After selecting new mark button, verify Add a New Mark page
        C31299626: Verify different mark thicknesses
        '''
        blank_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        self.scribble.swipe_on_scribble_pad()
        thin_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        thin_signature_image_diff = saf_misc.img_comp(blank_signature_image, thin_signature_image)
        assert thin_signature_image_diff != 0.0
        self.scribble.select_trash_btn()
        self.scribble.select_scribble_option("medium")
        self.scribble.swipe_on_scribble_pad()
        medium_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        medium_signature_image_diff = saf_misc.img_comp(blank_signature_image, medium_signature_image)
        assert thin_signature_image_diff < medium_signature_image_diff
        self.scribble.select_trash_btn()
        self.scribble.select_scribble_option("thick")
        self.scribble.swipe_on_scribble_pad()
        thick_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        thick_signature_image_diff = saf_misc.img_comp(blank_signature_image, thick_signature_image)
        assert medium_signature_image_diff < thick_signature_image_diff
        self.scribble.select_trash_btn()

    def test_02_new_mark_add_text(self, get_to_scribble_new_mark_single_page):
        """
        C31299627: Add a text markup
        """
        self.scribble.select_scribble_option("text")
        self.scribble.send_text_to_markup_textbox("HP Rocks!")
        self.scribble.select_save_btn()
        assert self.scribble.verify_signature()

    def test_03_place_and_move_signature(self, get_to_scribble_new_mark_single_page):
        """
        C31299629: Verify coachmarks after first mark placement
        C31299632: User can delete signature and select a new one
        """
        self.scribble.swipe_on_scribble_pad()
        self.scribble.select_save_btn()
        self.scribble.move_signature(direction="left", distance=400)
        assert self.scribble.verify_and_close_move_mark_coachmark_pop_up()
        self.scribble.select_trash_btn()
        assert self.scribble.verify_signature() is False
        self.scribble.select_new_mark_button()
        self.scribble.swipe_on_scribble_pad()
        self.scribble.select_save_btn()
        assert self.scribble.verify_signature()

    def test_04_draw_multiple_marks(self, get_to_scribble_new_mark_single_page):
        """
        C31299637: Scrible end to end flow
        C31299633: Add more than one mark on the page
        """
        self.scribble.swipe_on_scribble_pad()
        self.scribble.select_save_btn()
        assert self.scribble.verify_signature()
        self.scribble.select_new_mark_button()
        self.scribble.select_scribble_option("thick")
        self.scribble.swipe_on_scribble_pad()
        self.scribble.select_save_btn()
        assert self.scribble.verify_signature(multiple=True)

    def test_05_manage_marks(self, get_to_scribble_new_mark_single_page):
        """
        C31299634: Use an existing signature from saved marks
        C31299635: Verify deleting a mark removes mark from saved marks list
        C31299636: Verify that deleting all marks clears marks from saved marks list
        """
        self.scribble.swipe_on_scribble_pad()
        self.scribble.select_save_btn()
        self.scribble.select_trash_btn()
        self.scribble.select_new_mark_button()
        self.scribble.swipe_on_scribble_pad()
        self.scribble.select_save_btn()
        self.scribble.select_trash_btn()
        self.scribble.select_saved_marks_btn()
        self.scribble.select_saved_mark()
        assert self.scribble.verify_signature()
        self.scribble.select_trash_btn()
        self.scribble.select_saved_marks_btn()
        self.scribble.select_saved_marks_select_btn()
        self.scribble.select_single_unchecked_saved_mark(displayed=False)
        self.scribble.select_delete_selected_btn()
        self.scribble.delete_all_marks(displayed=False)
        assert self.scribble.verify_empty_saved_marks_list()

    def test_06_scribble_for_multiple_files(self):
        """
        C31299638: After uploading multiple fules, verify user is redirected to full view of select page
        C31299639: Verify grid view button changes the page layout
        C31299640: Verify selecting a page from the grid view opens single page
        C31299641: Verify selecting page from fullscreen view opens single page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages(number_pages=2)
        assert self.preview.verify_top_toolbar(self.preview.SCRIBBLE_BTN)
        self.preview.select_top_toolbar_btn(self.preview.SCRIBBLE_BTN)
        assert self.scribble.verify_full_view_mode_multiple_pages()
        self.scribble.select_full_screen_page_image()
        assert self.scribble.verify_new_mark_page()
        self.scribble.select_navigate_back_btn()
        self.scribble.select_grid_option_multiple_pages()
        assert self.scribble.verify_grid_view_mode_mulitple_pages()
        self.scribble.select_grid_screen_first_page_image()
        assert self.scribble.verify_new_mark_page()