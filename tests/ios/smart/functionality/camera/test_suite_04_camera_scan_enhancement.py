import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from SAF.misc import saf_misc

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_04_Camera_Scan_Enhancement(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.home = cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.scan = cls.fc.fd["scan"]
        cls.stack = request.config.getoption("--stack")
        cls.device_name = request.config.getoption("--mobile-device")
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_coach_mark(self):
        """
        test cases regarding coach marks:
        C31299204: verify coach mark
        C31299206: coach mark 2-nd page
        C31299207: coach mark 3-rd page
        C31299208: coach mark 4-th page
        C31299209: coach mark (X) button behavior
        C31299209: coach mark (tapping anywhere on screen behavior)
        C31299211: coach mark "<" back button
        C31299212: coach mark only show once
        C31299213: next coach mark page show up after dismissing previous
        """
        # TODO: the coach marks did not show in 1st time launch the camera scan, instead the 2nd time.
        # waiting for the issue to be fixed
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup()
        # verify coach mark first page
        assert self.camera.verify_adjust_scan_coach_mark(raise_e=False)
        # verify tap anywhere will ignore previous coach marks
        self.driver.click_by_coordinates(area="mm")
        self.fc.go_to_home_screen()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        # verify second coach mark
        assert self.camera.verify_preset_coach_mark(raise_e=False)
        self.camera.select_next()
        # verify back button
        assert self.camera.verify_capture_coach_mark(raise_e=False)
        self.camera.select_navigate_back()
        assert self.camera.verify_preset_coach_mark(raise_e=False)
        # verify third and fouth page
        self.camera.select_next()
        assert self.camera.verify_capture_coach_mark(raise_e=False)
        self.camera.select_next()
        assert self.camera.verify_source_coach_mark(raise_e=False)
        self.camera.select_next()
        # coach mark should disappear
        self.camera.verify_camera_screen()
        # restart and coach mark never show again
        self.driver.restart_app(i_const.BUNDLE_ID.SMART)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        assert self.camera.verify_adjust_scan_coach_mark(timeout=3, raise_e=False) is False
        assert self.camera.verify_capture_coach_mark(timeout=3, raise_e=False) is False
        assert self.camera.verify_preset_coach_mark(timeout=3, raise_e=False) is False
        assert self.camera.verify_source_coach_mark(timeout=3, raise_e=False) is False

    def test_02_verify_batch_auto_manual_functionality(self):
        """
        C31299219: Auto capture is enabled by default in Batch ( iOS ONLY )
        C31299202: Verify 'Auto' capture option is available on replace flow for Batch
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_preset_mode(self.camera.BATCH)
        # batch default "auto" mode, the button will be marked as blue
        self.camera.verify_auto_btn()
        assert self.camera.verify_auto_capture_mode()
        # switch to "manual", only "auto" button is displayed
        self.camera.select_manual_option()
        assert self.camera.verify_manual_capture_mode()
        # capture image on manual mode
        self.camera.select_capture_btn()
        self.camera.select_auto_image_collection_view()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_delete_page_icon()
        self.common_preview.select_replace_btn()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_auto_btn()

    def test_03_verify_document_photo_auto_manual_functionality(self):
        """
        C31299222: Verify Auto (Default - OFF) and Manual toggle - available for Document mode
        C31299223: Verify Auto (Default mode - OFF) and Manual toggle - available for Photo mode
        """
        self.fc.go_camera_screen_from_home(tile=True)
        # auto and manual capture in Document
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        assert self.camera.verify_manual_capture_mode()
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_ui_elements()
        self.camera.select_navigate_back()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_auto_btn()
        assert self.camera.verify_auto_capture_mode()
        # auto and manual capture in photo
        self.camera.select_preset_mode(self.camera.PHOTO)
        assert self.camera.verify_manual_capture_mode()
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_ui_elements()
        self.camera.select_navigate_back()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_auto_btn()
        assert self.camera.verify_auto_capture_mode()
        self.camera.capture_multiple_photos_by_auto_mode(device_name=self.device_name)

    def test_04_verify_setting_capture_preference_ui(self):
        """
        C31299197: Validate "Auto Enhancement" Feature under new "Capture Preferences" dialog
        Verify that tapping on the Gear settings should open the "Camera Preferences" screen to enable Page Lift Enhancement options
        Verify Camera Preferences Screen displays the following options (auto-enhancement, auto-heal, auto-orientation) with a toggle switch
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_gear_setting_btn()
        assert self.camera.verify_capture_preference_screen(raise_e=False)
        self.camera.verify_capture_preference_options()

    def test_05_verify_auto_orientation_behavior(self):
        """
        C31299367: Rotate button behavior - when Auto-Orientation ON
        C31299383: Rotate button behavior - when Auto-Orientation OFF
        C31299377: Done button behavior after tapping on Rotate and making a change
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_gear_setting_btn()
        self.camera.verify_is_toggled("auto_orientation_switch", is_toggled=False)
        self.camera.select_done()
        self._load_image()
        auto_rotated_img = self.common_preview.verify_preview_img()
        self.common_preview.select_rotate_btn()
        self.common_preview.select_auto_rotate_reset_button()
        self.common_preview.select_auto_rotate_done_button()
        assert saf_misc.img_comp(auto_rotated_img, self.common_preview.verify_preview_img()) < 0.1, "Image is not auto rotated"
        self.common_preview.select_navigate_back()
        self.common_preview.select_exit_popup_btn("scan")
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_gear_setting_btn()
        self.camera.verify_is_toggled("auto_orientation_switch", toggle_on_after_check=False)
        self.camera.select_done()
        self._load_image()
        upside_down_img = self.common_preview.verify_preview_img()
        self.common_preview.select_rotate_btn()
        self.common_preview.select_auto_rotate_done_button()
        assert saf_misc.img_comp(upside_down_img, self.common_preview.verify_preview_img()) > 0.1, "Auto-Orientation wasn't applied as specified in C31299383"

    def _load_image(self, index=1):
        self.camera.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_FILES)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_albums_tab()
        self.photos.select_automation_text_album()
        self.photos.select_photo_by_index(index=index)
        self.photos.select_next()
        self.scan.select_next_on_coachmark() # click on Next button on the Import photo screen
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
