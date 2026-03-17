from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest
import time

pytest.app_info = "SMART"


class Test_Suite_01_Camera_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"]["username"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    def test_01_camera_scan_app_permission_deny_first_and(self):
        """
        Description:
         1. Install and Launch app for the first time
         2. Click on Camera Scan tile
         3. Select Allow on No Camera Access screen
         4. Deny OS Permission popup
         5. Select Allow on No Camera Access screen

        Expected Result:
         2. Verify No Camera Access screen
         3. Verify permission popup
         5. Verify permission popup
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        self.scan.verify_no_camera_access_screen()
        self.scan.grant_camera_permissions()
        assert self.home.is_app_permission_popup(), "App Permission popup is not displayed"
        self.home.check_run_time_permission(accept=False)
        self.scan.verify_no_camera_access_screen()
        self.scan.grant_camera_permissions()
        assert self.home.is_app_permission_popup(), "App Permission popup is not displayed"

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_02_camera_scan_share_single_page(self, file_type):
        """
        Description: C31298928, C31298930, C31299872, C31299882
        1. Launch app to Home screen, and click on Camera Scan tile
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on share button:
        7. Select share file type:
           - JPG file
           Or:
           - PDF file
        8. Click on Share button
        9. Select Gmail
        Expected Result:
        4. Verify Tips for Camera Capture screen
        9. Verify that the email is sent to Gmail account
        """
        file_name = "{}_{}".format(self.test_02_camera_scan_share_single_page.__name__, file_type)
        self.fc.reset_app()
        self.__camera_scan_load_landing_page(is_multiple_page=False, btn_name=self.preview.SHARE_BTN)
        self.preview.verify_title(self.preview.SHARE_TITLE)
        self.preview.select_file_type(self.preview.IMAGE_JPG if file_type == "jpg" else self.preview.BASIC_PDF)
        self.preview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_03_camera_scan_share_multiple_page(self, file_type):
        """
        Description: C31299880, C31299182
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on "Add More page" button
        7. Take picture with manual mode
        8. Click on Next button
        9. Click on share button:
        10. Select share file type:
           - JPG file
           Or:
           - PDF file
        11. Click on Share button
        12. Select Gmail
        Expected Result:
        8. Verify Preview screen with multiple pictures displays
        12. Verify that the email is sent to Gmail account
        """
        file_name = "{}_{}".format(self.test_03_camera_scan_share_multiple_page.__name__, file_type)
        self.__camera_scan_load_landing_page(is_multiple_page=True, btn_name=self.preview.SHARE_BTN)
        self.preview.verify_title(self.preview.SHARE_TITLE)
        self.preview.select_file_type(self.preview.IMAGE_JPG if file_type == "jpg" else self.preview.BASIC_PDF)
        self.preview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    def test_04_camera_scan_save_multiple_page(self):
        """
        Description: C31299785, C31299894, C31299895, C31299879, C31297328
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. CLick on Full option
        6. Click on Next button
        7. Click on "+" button on preview screen
        8. Take picture with manual mode
        9. Click on Next button
        10. Click on Save button:
        11. Select Save file type:
           - JPG file
           Or:
           - PDF file
        12. Click on Save button
        13. Click on OK button
        Expected Result:
        12. Verify Save successfully popup
        13. Verify Preview screen
        """
        file_name = "{}_{}".format(self.test_04_camera_scan_save_multiple_page.__name__, "pdf")
        #save file as JPG type
        self.__camera_scan_load_landing_page(is_multiple_page=True, btn_name=self.preview.SAVE_BTN)
        self.preview.select_file_type(self.preview.IMAGE_JPG)
        self.preview.select_action_btn()
        self.preview.dismiss_file_saved_popup()
        self.preview.verify_preview_screen()
        # save file as Basic PDF type
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_file_saved_popup()
        self.preview.verify_preview_screen()

    def test_05_camera_scan_are_you_sure_popup(self):
        """
        Description: C31299789, C31299788
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on Back button on Preview screen
        7. - If cancel_btn option: click on Cancel button
           - If leave_btn option, click on LEAVE button
        Expected Result:
        6. Verify popup with:
           - Title
           - CANCEL and LEAVE button
        7. - cancel_btn: verify preview screen
           - leave_btn: verify home screen
        """
        self.__camera_scan_load_landing_page()
        self.fc.select_back()
        self.preview.verify_exit_popup()
        self.preview.select_exit_popup_btn("cancel")
        self.preview.verify_preview_screen()
        self.fc.select_back()
        self.preview.select_exit_popup_btn("home")
        if self.home.verify_feature_popup(raise_e=False):
            self.home.select_feature_popup_close()
        self.home.verify_home_nav()

    def test_06_camera_scan_adjust_boundaries_screen_with_photo_from_gallery(self):
        """
        Description: C31298929, C31298931, C31299871
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Click on Photo Gallery option
        4. Select any photo
        5. Click on Next button
        Expected Result:
        3. Verify Select a photo screen with:
           - Title
           - album lists
        4. Verify Adjust Boundaries screen
        5. Verify rotate button on Preview screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        if self.fc.flow_grant_camera_scan_permissions():
            self.scan.dismiss_coachmark()
        self.scan.select_source(self.scan.SOURCE_FILES_PHOTOS)
        self.local_photos.select_recent_photo_by_index()
        self.scan.dismiss_camera_capture_tips_popup()
        self.scan.verify_adjust_screen()
        self.scan.select_adjust_size_option(option="full")
        self.scan.select_adjust_next_btn()
        self.preview.verify_rotate_btn()

    def test_07_capture_mode_retained(self):
        """
        Description: C31299169, C31298989, C31299180
         1. Launch Smart app and Sign in
         2. Load Camera Scan screen
         3. Grant Permissions and Dismiss Coachmarks
         4. Select Photo mode
         5. Go back to home screen
         6. Load Camera Scan screen
         7. Relaunch app
         8. Load Camera Scan screen
        Expected Results:
         6. Verify Photo mode is selected
         8. Verify Photo mode is selected
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(verify_signin=False)
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.fc.flow_grant_camera_scan_permissions():
            self.scan.dismiss_coachmark()
        self.scan.select_capture_mode("photo")
        self.scan.select_exit_btn()
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.scan.verify_selected_capture_mode("photo")
        self.fc.flow_load_home_screen(verify_signin=False)
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.scan.verify_selected_capture_mode("photo")
    
    def test_08_book_mode_ui(self):
        """
        Description: C31298997, C31299245. C31299246, C31299247, C31299252
         1. Launch Smart app and Sign in with HP+
         2. Load Camera Scan screen
         3. Grant Permissions and Dismiss Coachmarks
         4. Select Book Mode
         5. Select Page Order button
         6. Select Page Order Switch button
        Expected Results:
         4. Verify "Capture all four corners..." message
          Verify Page Order buton
          Verify Page Order Switch button is invisible
         5. Verify Page Order button icon changes
          Verify 1 and 2 Page numbers appear and 1 is above 2
          Verify Line appears between 1 and 2 page numbers
          Verfy Page Order Switch button appears
         6. Verify Page Order switch button icon changed
          Verify 2 is above page number 1
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.fc.flow_grant_camera_scan_permissions():
            self.scan.dismiss_coachmark()
        self.scan.select_capture_mode("book")
        self.scan.verify_bubble_msg(message="book_corners")
        self.scan.verify_book_page_switch_button(invisible=True)
        init_page_order_icon = self.scan.verify_book_page_order_button(screenshot=True)
        self.scan.select_book_page_order_button()
        time.sleep(1)  # delay to allow button to appear
        init_page_switch_icon = self.scan.verify_book_page_switch_button(screenshot=True)
        assert saf_misc.img_comp(init_page_order_icon, self.scan.verify_book_page_order_button(screenshot=True)) != 0.00, "Book Page Order button icon should have changed"
        self.scan.verify_book_page_guides(reordered=False)
        self.scan.select_book_page_order_switch_button()
        time.sleep(1)  # delay for swapping animation to complete
        self.scan.verify_book_page_guides(reordered=True)
        assert saf_misc.img_comp(init_page_switch_icon, self.scan.verify_book_page_switch_button(screenshot=True)), "Book Page Order switch button icon should have changed"

    # ---------------     PRIVATE FUNCTIONS     ----------------------
    def __camera_scan_load_landing_page(self, create_acc=False, verify_signin=True, is_multiple_page=False, btn_name=None):
        """
        1. Click on Camera Scan tile on Home screen
        2. Capture page/pages
        5. Click on navigation button, like:
           - PRINT_BTN
           - SAVE_BTN
           - SHARE_BTN
        :param is_printer: True or False
        :param is_multiple_page: True or False
        :param btn_name:
        """
        self.fc.flow_load_home_screen(create_acc=create_acc, verify_signin=verify_signin)
        self.fc.flow_home_camera_scan_pages(number_pages= 2 if is_multiple_page else 1)
        self.preview.verify_preview_page_info()[1] == (2 if is_multiple_page else 1)
        if btn_name:
            self.preview.select_bottom_nav_btn(btn_name)