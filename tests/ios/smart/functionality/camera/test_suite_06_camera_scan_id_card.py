import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_06_Camera_Scan_Id_Card(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.home = cls.fc.fd["home"]
        cls.photos = cls.fc.fd["photos"]
        cls.stack = request.config.getoption("--stack")
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(stack=cls.stack, username=cls.username, password=cls.password, remove_default_printer=False)
    
    @pytest.fixture(scope="function", autouse="true")
    def go_camera_screen(self):
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_screen()

    def test_01_capture_id_card_ui(self):
        """
        C31299302: Verify "ID Card" option on camera scan carousal
        C31299303: "X" button behavior on ID Card screen
        C31299304: Capturing ID Card process
        C31299306: Verify messages on ID Card scanning
        C31299305: Capturing back side of ID Card
        C31299321: X Button behavior on New ID Card Front Capture
        C31299322: X Button behavior on New ID Card Back Capture
        C31299307: Back button behavior on back ID Card capturing screen
        """
        self.camera.select_preset_mode(self.camera.ID_CARD)
        self.camera.verify_id_front()
        self.camera.select_capture_btn()
        self.camera.verify_id_back()
        self.camera.select_cancel()
        self.camera.verify_id_front()
        self.camera.select_capture_btn()
        self.camera.verify_id_back()
        self.camera.select_capture_btn()
        self.common_preview.verify_id_card_front_screen()
        self.common_preview.select_navigate_back()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()
        self.camera.select_cancel()
        self.home.verify_home()

    def test_02_id_card_scan_preview_ui(self):
        """
        C31299308: "Next" button behavior on ID Card Front screen
        C31299309: "Next" button behavior on ID Card Back screen
        C31299312: Replace button behavior from preview page
        C31299319: Rotate button display for Front and Back
        C31299320: Edit button displays for Front and Back
        """
        self.camera.capture_id_card_by_camera()
        self.common_preview.verify_id_card_front_screen()
        self.common_preview.verify_delete_page_x_icon()
        self.common_preview.verify_rotate_right_icon()
        self.common_preview.select_next()
        self.common_preview.verify_id_card_back_screen()
        self.common_preview.verify_delete_page_x_icon()
        self.common_preview.verify_rotate_upsidedown_icon()
        self.common_preview.select_next()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_delete_page_icon()
        self.common_preview.select_replace_btn()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()
    
    def test_03_id_card_front_preview(self):
        """
        C31299314: Returning to scan flow from front ID Card preview
        C31299313: Getting to Preview after scanning front ID Card
        """
        self.camera.select_preset_mode(self.camera.ID_CARD)
        self.camera.verify_id_front()
        self.camera.select_capture_btn()
        self.camera.select_auto_image_collection_view()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_navigate_back()
        self.common_preview.verify_exit_popup()
        self.common_preview.select_exit_popup_btn("add")
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()

    @pytest.mark.parametrize("button", ["yes_go_home_btn", "yes_new_scan_btn", "no_add_img_btn", "cancel_btn"])
    def test_04_exit_without_saving(self, button):
        """
        C31299327: Exit from Preview screen by selecting "Yes, Start New Scan" on the popup
        C31299328: Exit from Preview screen by selecting "No, Add images" on the popup
        C31299329: Exit from Preview screen by selecting "Yes, Go Home" on the popup
        C31299330, C31299789: Exit from Preview screen by selecting "Cancel" on the popup 
        """
        self.__capture_id_card_from_camera_and_go_to_preview()
        self.common_preview.select_navigate_back()
        self.common_preview.verify_exit_popup()
        if button == "yes_go_home_btn":
            self.common_preview.select_exit_popup_btn("home")
            self.home.verify_home()
        elif button == "yes_new_scan_btn":
            self.common_preview.select_exit_popup_btn("scan")
            if self.camera.verify_second_close_btn():
                self.camera.select_second_close_btn()
            self.camera.verify_id_front()
        elif button == "no_add_img_btn":
            self.common_preview.select_exit_popup_btn("add")
            if self.camera.verify_second_close_btn():
                self.camera.select_second_close_btn()
            self.camera.verify_id_front()
        elif button == "cancel_btn":
            self.common_preview.select_exit_popup_btn("cancel")
            self.common_preview.verify_preview_screen()

    def test_05_id_card_from_file(self):
        """
        C31299323: Select file from Files&Photos when ID Card is selected (Front)
        C31299324: Select file from Files&Photos when ID Card os selected (Back)
        """
        self.camera.select_preset_mode(self.camera.ID_CARD)
        self.camera.verify_id_front()
        self.__select_one_photo_from_source()
        self.camera.verify_id_back()
        self.__select_one_photo_from_source()
        self.common_preview.verify_id_card_front_screen()
        self.common_preview.select_next()
        self.common_preview.verify_id_card_back_screen()
        self.common_preview.select_next()
        self.common_preview.verify_preview_screen()
    
    @pytest.mark.parametrize("page", ["front", "back"])
    def test_06_replace_id_card(self, page):
        """
        C31299317: Each side can be replaced on preview pages (front)
        C31299318: Each side can be replaced on preview pages (back)
        """
        self.camera.capture_id_card_by_camera()
        self.common_preview.verify_id_card_front_screen()
        if page == "front":
            self.common_preview.select_delete_page_icon()
            self.common_preview.select_replace_btn()
            if self.camera.verify_second_close_btn():
                self.camera.select_second_close_btn()
            self.camera.select_capture_btn()
            self.common_preview.verify_id_card_front_screen()
            return
        self.common_preview.select_next()
        self.common_preview.verify_id_card_back_screen()
        if page == "back":
            self.common_preview.select_delete_page_icon()
            self.common_preview.select_replace_btn()
            if self.camera.verify_second_close_btn():
                self.camera.select_second_close_btn()
            self.camera.select_capture_btn()
            self.common_preview.verify_id_card_back_screen()
            return
    
    @pytest.mark.parametrize("source", ["camera", "files"])
    def test_07_replace_id_card_at_the_start(self, source):
        """
        C31299331: Replace ID Card which is at the start
        """
        if source == "camera":
            self.__capture_id_card_from_camera_and_go_to_preview()
        elif source == "files":
            self.__capture_id_card_from_photo_and_go_to_preview()
        self.common_preview.select_add_page()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.camera.capture_manual_photo_by_camera()
        self.common_preview.verify_preview_screen()
        self.driver.swipe(direction="left")
        self.common_preview.select_delete_page_icon()
        self.common_preview.select_replace_btn()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()
    
    @pytest.mark.parametrize("source", ["camera", "files"])
    def test_08_replace_id_card_at_the_middle(self, source):
        """
        C31299332: Replace ID Card which is at the middle
        """
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.camera.capture_manual_photo_by_camera()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_add_page()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        if source == "camera":
            self.__capture_id_card_from_camera_and_go_to_preview()
        elif source == "files":
            self.__capture_id_card_from_photo_and_go_to_preview()
        self.common_preview.select_add_page()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.camera.capture_manual_photo_by_camera()
        self.common_preview.verify_preview_screen()
        self.driver.swipe(direction="left")
        self.common_preview.select_delete_page_icon()
        self.common_preview.select_replace_btn()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()
    
    @pytest.mark.parametrize("source", ["camera", "files"])
    def test_09_replace_id_card_at_the_end(self, source):
        """
        C31299333: Replace ID Card which is at the end
        """
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.camera.capture_manual_photo_by_camera()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_add_page()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        if source == "camera":
            self.__capture_id_card_from_camera_and_go_to_preview()
        elif source == "files":
            self.__capture_id_card_from_photo_and_go_to_preview()
        self.common_preview.select_delete_page_icon()
        self.common_preview.select_replace_btn()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()
    
    @pytest.mark.parametrize("source", ["camera", "files"])
    def test_10_replace_id_card_from_multiple(self, source):
        """
        C31299334: Replace an ID card in preview from Multiple ID Cards
        """
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        if source == "camera":
            self.__capture_id_card_from_camera_and_go_to_preview()
        elif source == "files":
            self.__capture_id_card_from_photo_and_go_to_preview()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_add_page()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        if source == "camera":
            self.__capture_id_card_from_camera_and_go_to_preview()
        elif source == "files":
            self.__capture_id_card_from_photo_and_go_to_preview()
        self.common_preview.verify_preview_screen()
        self.driver.swipe(direction="left")
        self.common_preview.select_delete_page_icon()
        self.common_preview.select_replace_btn()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_id_front()

    def test_11_id_card_rotate_btn_functionality(self):
        """
        C31299316: ID Back rotates to 180 degrees
        """
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.capture_id_card_by_camera()
        self.common_preview.verify_id_card_front_screen()
        init_front_img = self.common_preview.verify_preview_img()
        self.common_preview.select_rotate_right_icon()
        rotated_front_img = self.common_preview.verify_preview_img()
        self.common_preview.select_next()
        init_back_img = self.camera.return_capture_image()
        self.common_preview.select_rotate_upsidedown_icon()
        rotated_back_img = self.camera.return_capture_image()
        assert saf_misc.img_comp(init_front_img, rotated_front_img) > 0.06, "Init front and rotated front image should not match"
        assert saf_misc.img_comp(init_back_img, rotated_back_img) > 0.06, "Init back and rotated back image should not match"

    def __capture_id_card_from_camera_and_go_to_preview(self):
        self.camera.capture_id_card_by_camera()
        self.common_preview.verify_id_card_front_screen()
        self.common_preview.select_next()
        self.common_preview.verify_id_card_back_screen()
        self.common_preview.select_next()
        self.common_preview.verify_preview_screen()
    
    def __capture_id_card_from_photo_and_go_to_preview(self):
        self.camera.select_preset_mode(self.camera.ID_CARD)
        self.camera.verify_id_front()
        self.__select_one_photo_from_source()
        self.camera.verify_id_back()
        self.__select_one_photo_from_source()
        self.common_preview.verify_id_card_front_screen()
        self.common_preview.select_next()
        self.common_preview.verify_id_card_back_screen()
        self.common_preview.select_next()
        self.common_preview.verify_preview_screen()
    
    def __select_one_photo_from_source(self):
        self.camera.select_source_button()
        self.camera.verify_source_options()
        self.camera.select_source_option(self.camera.OPTION_FILES)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_albums_tab()
        self.photos.select_recents_or_first_option()
        self.photos.select_photo_by_index()
        self.photos.select_next()