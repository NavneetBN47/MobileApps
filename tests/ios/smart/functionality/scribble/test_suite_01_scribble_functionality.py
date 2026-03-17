import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES
 
pytest.app_info = "SMART"

class Test_Suite_01_Scribble_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.account = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)
        cls.fc.go_home(reset=False, stack=cls.stack, username=cls.account["email"], password=cls.account["password"])

    @pytest.fixture()
    def get_to_scribble_new_mark_single_page(self):
        """
        C31299623: From the Camera Scan page, scan any document, go to Preview page, and verfiy scribble option
        C31299624: After selecting scribble option, verify Scribble Page loads for a single document
        """
        self.fc.go_to_home_screen()
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fc.fd["camera"].clear_tips_pop_up()
        self.fc.fd["camera"].select_source_button()
        self.fc.fd["camera"].select_files_and_photos_option()
        self.fc.select_photo_from_photo_picker(select_all_files=False)
        self.driver.click("next_btn")
        self.driver.click("next_btn")
        self.fc.fd["camera"].dismiss_feedback_pop_up()
        assert self.fc.fd["common_preview"].verify_top_toolbar(self.fc.fd["common_preview"].SCRIBBLE_BTN)
        self.fc.fd["common_preview"].select_top_toolbar_btn(self.fc.fd["common_preview"].SCRIBBLE_BTN)
        self.fc.fd["scribble"].select_new_mark_button()
        assert self.fc.fd["scribble"].verify_new_mark_page()
        self.fc.fd["scribble"].dismiss_welcome_to_scribble_pop_up()

    def test_01_new_mark_button(self, get_to_scribble_new_mark_single_page):
        '''
        C31299625: After selecting new mark button, verify Add a New Mark page
        C31299626: Verify different mark thicknesses
        '''
        blank_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        thin_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        thin_signature_image_diff = saf_misc.img_comp(blank_signature_image, thin_signature_image)
        assert thin_signature_image_diff > 0.2
        self.fc.fd["scribble"].select_trash_btn()
        self.fc.fd["scribble"].select_scribble_option("medium")
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        medium_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        medium_signature_image_diff = saf_misc.img_comp(blank_signature_image, medium_signature_image)
        assert thin_signature_image_diff < medium_signature_image_diff
        self.fc.fd["scribble"].select_trash_btn()
        self.fc.fd["scribble"].select_scribble_option("thick")
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        thick_signature_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        thick_signature_image_diff = saf_misc.img_comp(blank_signature_image, thick_signature_image)
        assert medium_signature_image_diff < thick_signature_image_diff
        self.fc.fd["scribble"].select_trash_btn()
    
    def test_02_new_mark_add_text(self, get_to_scribble_new_mark_single_page):
        """
        C31299627: Add a text markup
        """
        self.fc.fd["scribble"].select_scribble_option("text")
        self.fc.fd["scribble"].send_text_to_markup_textbox("HP Rocks!")
        self.fc.fd["scribble"].select_save_btn()
        assert self.fc.fd["scribble"].verify_signature() is not False

    def test_03_place_and_move_signature(self, get_to_scribble_new_mark_single_page):
        """
        C31299629: Verify coachmarks after first mark placement
        C31299631: Move/minimize the signature on the page
        C31299632: User can delete signature and select a new one
        """
        if self.fc.fd["scribble"].get_header_height() >= 30:
            pytest.skip("Cannot scale signature on iPhone with FaceID + Notch")
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        self.fc.fd["scribble"].select_save_btn()
        before_move_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        self.fc.fd["scribble"].move_signature(direction="left")
        assert self.fc.fd["scribble"].verify_and_close_move_mark_coachmark_pop_up()
        self.fc.fd["scribble"].move_signature(direction="up")
        after_move_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        assert saf_misc.img_comp(before_move_image, after_move_image) > 0.08
        self.fc.fd["scribble"].scale_signature()
        after_scale_image = saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())
        assert saf_misc.img_comp(after_move_image, after_scale_image) > 0.08
        self.fc.fd["scribble"].select_trash_btn()
        assert self.fc.fd["scribble"].verify_signature() is False
        self.fc.fd["scribble"].select_new_mark_button()
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        self.fc.fd["scribble"].select_save_btn()
        assert self.fc.fd["scribble"].verify_signature() is not False

    def test_04_draw_multiple_marks(self, get_to_scribble_new_mark_single_page):
        """
        C31299637: Scribble end to end flow
        C31299633: Add more than one mark on the page
        """
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        self.fc.fd["scribble"].select_save_btn()
        assert self.fc.fd["scribble"].verify_signature() is not False
        self.fc.fd["scribble"].select_new_mark_button()
        self.fc.fd["scribble"].select_scribble_option("thick")
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        self.fc.fd["scribble"].select_save_btn()
        assert self.fc.fd["scribble"].verify_signature(multiple=True)

    def test_05_manage_marks(self, get_to_scribble_new_mark_single_page):
        """
        C31299634: Use an existing signature from saved marks
        C31299635: Verify deleting a mark removes mark from saved marks list
        C31299636: Verify that deleting all marks clears marks from saved marks list
        """
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        self.fc.fd["scribble"].select_save_btn()
        self.fc.fd["scribble"].select_trash_btn()
        self.fc.fd["scribble"].select_new_mark_button()
        self.fc.fd["scribble"].swipe_on_scribble_pad()
        self.fc.fd["scribble"].select_save_btn()
        self.fc.fd["scribble"].select_trash_btn()
        self.fc.fd["scribble"].select_saved_marks_btn()
        self.fc.fd["scribble"].select_saved_mark()
        assert self.fc.fd["scribble"].verify_signature()
        self.fc.fd["scribble"].select_trash_btn()
        self.fc.fd["scribble"].select_saved_marks_btn()
        first_signature_image_data = self.fc.fd["scribble"].get_first_saved_mark_data()
        self.fc.fd["scribble"].select_saved_marks_select_btn()
        self.fc.fd["scribble"].select_single_unchecked_saved_mark()
        self.fc.fd["scribble"].select_delete_selected_btn()
        updated_first_signature_image_data = self.fc.fd["scribble"].get_first_saved_mark_data()
        assert updated_first_signature_image_data != first_signature_image_data
        self.fc.fd["scribble"].delete_all_marks()
        assert self.fc.fd["scribble"].verify_empty_saved_marks_list()

    def test_06_scribble_for_multiple_files(self):
        """
        C31299638: After uploading multiple files, verify user is redirected to full view of select page
        C31299639: Verify grid view button changes the page layout
        C31299640: Verify selecting a page from the grid view opens single page
        C31299641: Verify selecting page from fullscreen view opens single page
        """
        self.fc.go_to_home_screen()
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fc.fd["camera"].clear_tips_pop_up()
        self.fc.fd["camera"].select_source_button()
        self.fc.fd["camera"].select_files_and_photos_option()
        self.fc.select_photo_from_photo_picker(no_of_photos=2, select_all_files=False)
        self.fc.fd["camera"].dismiss_feedback_pop_up()
        self.fc.fd["common_preview"].select_top_toolbar_btn(self.fc.fd["common_preview"].SCRIBBLE_BTN)
        assert self.fc.fd["scribble"].verify_full_view_mode_multiple_pages()
        self.fc.fd["scribble"].select_full_screen_page_image()
        assert self.fc.fd["scribble"].verify_new_mark_page()
        self.fc.fd["scribble"].select_navigate_back_btn()
        self.fc.fd["scribble"].select_grid_option_multiple_pages()
        assert self.fc.fd["scribble"].verify_grid_view_mode_mulitple_pages()
        self.fc.fd["scribble"].select_grid_screen_first_page_image()
        assert self.fc.fd["scribble"].verify_new_mark_page()