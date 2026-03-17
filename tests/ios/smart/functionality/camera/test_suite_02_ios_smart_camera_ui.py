import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner":True}

@pytest.mark.skipif(pytest.platform == "MAC", reason="Camera scan is not supported on MAC")
class Test_Suite_02_Ios_Smart_Camera_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.files = cls.fc.fd["files"]
        cls.share = cls.fc.fd["share"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_verify_adjust_boundaries_ui(self):
        """
        C31299871
        1. Launch app for the first time and go to the camera screen and take a picture with camera
        Expected Results:
            Verify adjust boundaries ui
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_manual_option()
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_ui_elements()
        self.camera.select_navigate_back()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.verify_camera_screen()

    def test_02_verify_exit_without_saving_popup(self):
        """
        C31299877, C31299182, C31297717 Precondition: fresh install, printer with scanner
        Steps:
            1 - Install and launch HP Smart app for the first time
            2 - Tap the Scan tile after selecting a printer
            3 - Choose the "scanner" option and perform scan job from the scanner
            4 - From the preview screen, tap on add page icon
            5 - choose "Camera" option
            6 - Tap on "Don't Allow" option
            7 - Tap on the link "Enable Access to Camera"
            8 - Tap "No" on the pop up
            9 - Tap on "X" icon to close the screen
            10 - Tap on "No" option
            11 - Tap on Save and save the scan to Smart app files
        Expected Results:
            1 - For step 5, Verify that camera Access permission pop up "HP Smart would like to Access the Camera" should be displayed with "OK" and "Don't Allow" options
            2 - For step 6, Verify that Allow Access to the Camera screen should be displayed with the link to "Enable Access to Camera"
            3 - For step 7, Verify that "Unsaved pages will be lost" pop up should be displayed with the options "Yes" and "No"
            4 - For step 8, Verify that the pop up should be closed and the app remains in the "Allow Access to the Camera" screen
            5 - For step 9, verify "Exit without saving?" pop up should be displayed with "Yes" & "No" options
            6 - For step 10, Verify scan Preview screen should be displayed with the scanned page at step 3
            7 - for step 11, verify that the scanned output should be saved successfully inside the app in " HP Smart Files"
        """
        file_name = "test_02_verify_exit_without_saving_popup"
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_add_page()
        if self.scan.verify_second_close_btn():
            self.scan.select_second_close_btn()
        self.scan.verify_source_button()
        self.scan.select_source_button()
        self.scan.select_camera_option()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=False)
        self.camera.verify_allow_access_to_camera_ui_elements()
        self.camera.select_enable_access_to_camera_link()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.camera.verify_allow_access_to_camera_ui_elements()
        self.camera.select_close()
        self.camera.verify_popup_message(popup_title=self.camera.POPUP_EXIT_WITHOUT_SAVING)
        self.camera.select_exit_without_saving_popup(allow_save=False)
        self.common_preview.verify_preview_img(screenshot=False)
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.common_preview.SHARE_SAVE_TITLE, "jpg")
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists(file_name)
        self.fc.go_hp_smart_files_and_delete_all_files()

    def test_03_file_type_selection(self):
        """
        C31299476, C31299478, C31299477 - Verify file types of scanned Photo
        C31299786, C31299783 - share and save scan with pdf format
        C31297711 - select pdf files
        """
        file_name = self.test_03_file_type_selection.__name__
        self.fc.go_camera_screen_from_home()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.camera.verify_manual_capture_mode()
        self.camera.select_capture_btn()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.select_file_types_dropdown()
        self.common_preview.verify_file_types([self.common_preview.IMAGE_JPG, self.common_preview.BASIC_PDF,
                                               self.common_preview.IMAGE_PNG, self.common_preview.IMAGE_TIF,
                                               self.common_preview.IMAGE_HEIF])
        self.common_preview.select_navigate_back()
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.common_preview.SHARE_SAVE_TITLE, file_type="PDF")
        self.fc.go_hp_smart_files_screen_from_home(select_tile=False)
        self.files.verify_file_name_exists(f"{file_name}.pdf")
        self.fc.go_hp_smart_files_and_delete_all_files()

    def test_04_print_with_hp_smart(self):
        """
        C31299890 - Verify Print with HP Smart option on the share screen
        """
        self.fc.go_camera_screen_from_home()
        self.camera.select_capture_btn()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.dismiss_file_types_coachmark()
        self.common_preview.select_button(self.common_preview.SHARE_SAVE_BTN)
        self.share.verify_share_popup()
        if not self.share.verify_option_present("print_with_hp_smart_option"):
            self.share.select_edit_actions()
            self.share.toggle_option_on_actions_screen("print_with_hp_smart_switch", enable=True)
            self.share.select_done_btn()
        self.share.select_print_with_hp_smart()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)

    def test_05_verify_multi_scan_with_different_modes(self):
        """
        C31299237 - [REORDER screen] Two photo scanned auto and manual mode on the camera scan screen at the same time.
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_capture_btn()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()
        self.common_preview.select_add_page()
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.camera.select_gear_setting_btn()
        self.camera.verify_is_toggled("auto_enhancements_switch", toggle_on_after_check=False, raise_e=False)
        self.camera.verify_is_toggled("auto_orientation_switch", toggle_on_after_check=False, raise_e=False)
        self.camera.select_done()
        self.camera.select_auto_btn()
        self.camera.capture_multiple_photos_by_auto_mode()
        self.common_preview.verify_preview_screen()
        self.common_preview.verify_an_element_and_click(self.common_preview.REORDER_BTN)
        self.common_preview.verify_title(self.common_preview.REORDER_TITLE)
        self.common_preview.select_done()
        self.common_preview.verify_preview_screen()
