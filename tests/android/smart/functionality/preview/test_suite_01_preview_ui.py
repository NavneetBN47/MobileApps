from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import TEST_DATA
import time

pytest.app_info = "SMART"

class Test_Suite_01_Preview_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.print_preview = cls.fc.flow[FLOW_NAMES.PRINT_PREVIEW]
        cls.job_notification = cls.fc.flow[FLOW_NAMES.JOB_NOTIFICATION]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"]["username"]

        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_preview_ui_single_page_from_camera(self):
        """
        Description: C31299874, C31299236, C31297718, C31956361
         1. Load to Home screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. source == "camera" Click on Camera Scan on Home Screen
         5. Click on Scan button
         6. Select the Page Options(...) button
       Expected Results:
         4. Verify Preview screen with:
           + Preview title
           + Back button
           + Edit button displays
           + Save button displays (source == "camera")
           + Share button displays (source == "camera")
           + "+" button displays
         6. Verify the page options buttons
           + Replace button
           + Edit button
           + Delete button
        """
        self.__load_preview_screen(is_multiple=False, source="camera")
        self.preview.verify_bottom_nav(btns=[self.preview.SAVE_BTN, self.preview.SHARE_BTN])
        self.preview.verify_top_toolbar(btns=self.preview.ADD_BTN)
        self.preview.select_page_options_btn()
        self.preview.verify_preview_edit_options()

    def test_02_preview_ui_multiple_page(self):
        """
        Description: C31299403, C31299404
         1. Load to Hom screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Scan
         5. Click on Scan button
         6. Click on "+" button on Preview screen
         7. Click on Scan button
         8. Select the Page Options(...) button

        Expected Results:
         7. Verify Preview screen with:
           + number of page "2/2" displays
           + Reorder button displays
           + Preview title
           + Back button
           + Edit button displays
           + Save button displays (source == "scanner")
           + Share button displays (source == "scanner")
           + "+" button displays
         8. Verify the page options buttons
           + Replace button
           + Edit button
           + Delete button
        """
        self.__load_preview_screen(is_multiple=True, source="scanner")
        self.preview.verify_bottom_nav(btns=[self.preview.SAVE_BTN, self.preview.SHARE_BTN])
        self.preview.verify_top_toolbar(btns=self.preview.ADD_BTN)
        self.preview.verify_top_toolbar(btns=[self.preview.REORDER_BTN])
        assert self.preview.verify_preview_page_info()[1] == 2, "Page count should be 2"
        self.preview.select_page_options_btn()
        self.preview.verify_preview_edit_options()

    @pytest.mark.parametrize("file_name", ["all_charcters", "2020_02_20_13"])
    def test_03_share_option_file_name(self, file_name):
        """
        Description: C31299893, C31299851, C31297309, C31297314, C31297315, C31297317, C31297318, C31297319
          1. Load to Home screen
          2. Click on Add icon to access printers list
          3. Select a target printer
          4. Click on Printer Scan on Home screen
          5. Click on Scan button on Scan screen
          6. Click on Share button on Preview screen
          7. Click on Name field to rename the filename
          8. Click on Back button from App
          9. Click on Share button on Preview screen
          10. Click on file name to rename file name
          11. Click on Share button
          12. Click on Gmail

        Expected Results:
           8. Verify Preview screen:
             + Title
             + "+" button
             + Print/Share/Save/Smart Tasks/Fax button
          12. Make sure file can be shared success
        :param file_name:
        """
        self.__load_preview_screen(is_multiple=False, source="scanner")
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.rename_file(self.test_03_share_option_file_name.__name__)
        self.fc.select_back()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.select_file_size(self.preview.FILE_SIZE_ACTUAL)
        self.preview.verify_file_size(self.preview.FILE_SIZE_ACTUAL)
        self.preview.select_file_size(self.preview.FILE_SIZE_MEDIUM)
        self.preview.verify_file_size(self.preview.FILE_SIZE_MEDIUM)
        self.preview.select_file_size(self.preview.FILE_SIZE_SMALL)
        self.preview.verify_file_size(self.preview.FILE_SIZE_SMALL)
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    def test_04_save_option_screen(self):
        """
        Description: C31299240, C31297323
          1. Load to Home screen
          2. Click on Camera Scan on Home screen
          3. Click on Capture button on Camera scan screen, and click Next button to preview screen
          4. Click on Save button
          5. Select format type

        Expected Results:
          5. If format type = "JPG", then verify Save Option screen:
               + Title
               + Save button
               + Document size is invisible
           If format type = "PDF", then verify Save Option screen:
               + Title
               + Save button
               + Document size is visible
        """
        self.fc.flow_load_home_screen(verify_signin=False)
        self.fc.flow_home_camera_scan_pages()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.select_file_type(file_type=self.preview.BASIC_PDF)
        self.preview.verify_action_screen()
        self.preview.verify_document_size(invisible=False)
        self.preview.select_file_type(file_type=self.preview.IMAGE_JPG)
        self.preview.verify_action_screen()

    def test_05_delete_single_page(self):
        """
        Description: C31297719, C31297721
        1. Load to preview  screen from printer scan
        2. Click on x button on preview screen
        Expected Result:
        2. verify printer scan screen
        """
        self.__load_preview_screen(is_multiple=False, source="scanner")
        self.preview.select_page_options_btn(self.preview.DELETE_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)

    def test_06_delete_all_pages(self):
        """
        Description: C31297722, C31297723
        1. Load to preview  screen from printer scan
        2. Click on "+" button
        3. Click on Scan button
        4. Click on x button 2 times

        Expected Results:
        4. Pictures deleted success, and go back to Scan screen
        """
        self.__load_preview_screen(is_multiple=True, source="scanner")
        self.preview.select_page_options_btn(self.preview.DELETE_BTN)
        assert self.preview.verify_preview_page_info()[1] == 1, "Page count should be 1"
        self.preview.select_page_options_btn(self.preview.DELETE_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)

    @pytest.mark.parametrize("back_btn", ["app", "mobile"])
    def test_07_preview_back_btn(self, back_btn):
        """
        Description:
         1. Load to preview  screen from printer scan
         2. Click on back button on preview screen
         3. if back_btn: then click on Leave button
        Expected Result:
         3. verify Home screen
        """
        self.__load_preview_screen(is_multiple=False, source="scanner")
        if back_btn == "app":
            self.fc.select_back()
        else:
            self.driver.press_key_back()
        self.preview.verify_exit_popup()
        self.preview.select_exit_popup_btn("home")
        if self.home.verify_feature_popup(raise_e=False):
            self.home.select_feature_popup_close()
        self.home.verify_home_nav()

    def test_08_rotate_button(self):
        """
        Description: C31299225, C31299227
         1. Load to preview screen from camera scan
         2. Repeat 4 Times
          a. Capture preview image
          b. Select Rotate Button
          c. Capture preview image
        Expected Results:
         2b. Verify Rotate image and Page options buttons are invisible
            Verify Rotate image and Page options buttons become visible
         4. Verify Screenshots from steps 2a/2c do not match
            For final rotation verify the current preview image is same as the original preview image
        """
        self.__load_preview_screen(source="scanner")
        init_img = self.preview.verify_preview_img()
        for i in range(4):
            prerotated_img = init_img if i == 0 else self.preview.verify_preview_img()
            self.preview.select_rotate_btn()
            rotated_img = self.preview.verify_preview_img()
            if i == 3:
                assert saf_misc.img_comp(init_img, rotated_img) < 0.06, "Image should match initial image after full rotation"
            else:
                assert saf_misc.img_comp(prerotated_img, rotated_img) != 0.00, "Image should change after rotation"

    @pytest.mark.parametrize("option", ["edit", "replace", "delete"])
    def test_09_page_options_menu(self, option):
        """
        Description: C31299184, C35948894
         1. Load preview screen through scaner
          - If option == "delete" load a second image
         2. Select page options(...) button
         3. Select option on page options menu
         If option == "replace" continue
         4. Select Capture button
        Expected Results:
         3. If option == "delete" Verify Page count is one
            If option == "edit" Verify edit screen
         4. Verify preview screen
          Verify Page count is one
        """
        options_btn_map = {
            "edit": self.preview.EDIT_BTN,
            "replace": self.preview.REPLACE_BTN,
            "delete": self.preview.DELETE_BTN
        }
        self.__load_preview_screen(is_multiple=option=="delete")
        self.preview.select_page_options_btn(options_btn_map[option])
        if option == "delete":
            assert self.preview.verify_preview_page_info()[1] == 1, "Page count should be 1"
        elif option == "edit":
            self.edit.verify_edit_page_title()
        else:
            self.scan.start_capture(change_check=self.scan.DOCUMENT_CHANGE_CHECK)
            self.scan.select_adjust_next_btn(timeout=20)
            assert self.preview.verify_preview_page_info()[1] == 1, "Page count should be 1"

    def test_10_more_option_print_format(self):
        """
        Description: C31297335
        1. Load to Hom screen
        2. Click on Add icon to access printers list
        3. Select a target printer
        4. Click on Scan tile on Home screen
        5. Click on Scan button
        6. Click on More Option screen
        7. Click on Print Format
        8. Click on Print as JPG (print_as_type = "jpg"):
        Or
           Click on Print as PDF (print_as_type = "pdf"):

      Expected Results:
        6. Verify More Option screen
        7. Verify Print Format screen with:
           + Print Format title
           + Print as JPG item
           + Print as PDF item
        8. Make sure app go back to Preview screen
        """
        self.__load_preview_screen(source="camera")
        self.preview.select_more_options_btn(self.preview.FORMAT_BTN)
        self.preview.verify_print_format_screen()
        self.preview.select_print_format_option("pdf")
        self.preview.verify_preview_screen()
        self.preview.select_more_options_btn(self.preview.FORMAT_BTN)
        self.preview.select_print_format_option("jpg")
        self.preview.verify_preview_screen()

    def test_11_print_preview_print_settings(self):
        """
        Description: C31297357, C31297358, C31297362, C31297363, C31297364, C37837664, C37837665, C37839000, C37857577, C37857578, C37857579
                     C34652241, C34652243, C34652242, C34670420, C34670433, C34670434, C34693840
         1. Load to Hom screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Scan
         5. Click on Scan button
         6. Click on "+" button on Preview screen
         7. Click on Scan button
         8. Click on Print button
         9. Click on Page Range dropdown button
         10. Input invalid range value
         11. Input valid range value
         12. Click on 2-sided option, and choose different value, like: 1-sided, 2-sided (long-edge), 2-sided (short-edge)
         13. Click on Color Mode option, and choose different value
         14. Click on Orientation option, and choose different value
         15. Click on More Options button
         16. Click on Quality dropdown button
         17. Click on PHOTO tabc
         18. Click on Quality
         19. Toggle on/off Borderless option
         20. Click on Scaling option
         21. Click on Back button
         22. Click on Print button

        Expected Results:
         7. Verify Preview screen with:
         8. Verify Print Preview screen with:
            - Page Range option displays
            - Copies option displays
            - Color Mode option displays
            - Orientation option displays
            - Print Quality option doesn't display
         10. Verify Print button is disabled
         11. Verify Print button is enabled
         12. 2-sided option can be chosen success with different values
         13. Color Mode option can be chosen success with different values
         14. Verify Orientation option can be chosen success with different values
         15. Verify More Options screen
         16. Verify Quality options can be chosen success with different values
         17. Verify Photo tab with different options
         18. Verify Quality options can be chosen success with different values
         19. Verify Borderless toggle works correctly
         20. Verify Scaling option can be chosen success with different values
         21. Verify Print Preview screen
         22. Job can be printed success
        """
        self.__load_preview_screen(is_multiple=True, source="scanner")
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.print_preview.verify_print_preview_screen()
        self.print_preview.verify_printer_item()
        self.print_preview.verify_copies_item()
        self.print_preview.verify_color_mode_item()
        self.print_preview.verify_print_quality_item()
        self.print_preview.verify_orientation_item()
        self.print_preview.select_range_page_option(self.print_preview.SPECIFIC_RANGE_PAGE_OPTION, "2")
        if self.print_preview.verify_2_sided_item(raise_e=False):
            self.print_preview.select_2_sided_option(self.print_preview.TWO_SIDED_SHORT_EDGE_OPTION)
            assert self.print_preview.get_2_sided_selected_value() == "2-sided (short-edge)"
            self.print_preview.select_2_sided_option(self.print_preview.TWO_SIDED_LONG_EDGE_OPTION)
            assert self.print_preview.get_2_sided_selected_value() == "2-sided (long-edge)"
            self.print_preview.select_2_sided_option(self.print_preview.ONE_SIDED_OPTION)
            assert self.print_preview.get_2_sided_selected_value() == "1-sided"
        self.print_preview.select_color_mode_option(self.print_preview.COLOR_OPTION)
        assert self.print_preview.get_color_selected_value() == "Color"
        self.print_preview.select_orientation_option(self.print_preview.ORIENTATION_LANDSCAPE_OPTION)
        assert self.print_preview.get_orientation_selected_value() == "Landscape"
        self.print_preview.select_orientation_option(self.print_preview.ORIENTATION_PORTRAIT_OPTION)
        assert self.print_preview.get_orientation_selected_value() == "Portrait"
        self.print_preview.select_orientation_option(self.print_preview.ORIENTATION_AUTO_OPTION)
        assert self.print_preview.get_orientation_selected_value() == "Automatic"
        self.print_preview.select_more_options_btn()
        self.print_preview.verify_more_options_screen()
        self.print_preview.select_quality_option(self.print_preview.QUALITY_DRAFT_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Draft"
        self.print_preview.select_quality_option(self.print_preview.QUALITY_NORMAL_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Normal"
        self.print_preview.select_quality_option(self.print_preview.QUALITY_BEST_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Best"
        self.print_preview.select_quality_option(self.print_preview.QUALITY_AUTO_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Automatic"
        self.print_preview.select_photo_btn()
        self.print_preview.verify_options_on_photo_tab()
        self.print_preview.select_quality_option(self.print_preview.QUALITY_NORMAL_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Normal"
        self.print_preview.select_quality_option(self.print_preview.QUALITY_BEST_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Best"
        self.print_preview.select_quality_option(self.print_preview.QUALITY_AUTO_OPTION)
        assert self.print_preview.get_quality_selected_value() == "Automatic"
        self.print_preview.select_scaling_option(self.print_preview.SCALING_FILL_OPTION)
        assert self.print_preview.get_scaling_selected_value() == "Fill Page"
        self.print_preview.select_scaling_option(self.print_preview.SCALING_FIT_OPTION)
        assert self.print_preview.get_scaling_selected_value() == "Fit to Page"
        self.print_preview.select_back_btn()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.select_print_btn()
        time.sleep(5)
        self.preview.select_bottom_nav_btn(self.preview.PRINT_PREVIEW_BTN)
        self.print_preview.verify_print_preview_screen()
        self.print_preview.select_print_job_list_btn()
        self.job_notification.verify_print_jobs_screen()
        self.job_notification.verify_print_job_on_the_list()

    def test_12_print_preview_ui_from_single_photo(self):
        """
        Description: C31297359, C31297360, C31297361, C37459402
         1. Load to Home screen
         2. Click on Print Photos tile
         3. Select a photo from the list
         4. Click on Next button

       Expected Results:
         3. Verify DS Preview screen with tooltips icon shows on the screen
         4. Verify Print Preview screen with:
             - Print Quality option displays
             - Orientation option doesn't display
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.dismiss_print_anywhere_popup()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.local_photos.verify_photo_picker_optional_screen(raise_e=False)
        self.local_photos.select_recent_photo_by_index()
        if self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.select_photo_picker_add_btn()
        if self.local_photos.verify_photo_picker_closed_option(raise_e=False):
            self.local_photos.select_photo_picker_done_btn()
        if self.preview.verify_title(self.preview.PRINT_SIZE_TITLE, raise_e=False):
            pytest.skip("Novelli printer is not available for simplified photo feature with print quality option on Print Preview screen")
        self.preview.verify_dynamic_studio_screen(timeout=20)
        self.preview.select_ds_layout_btn()
        self.preview.verify_info_btn()
        self.preview.select_preview_btn()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.verify_printer_item()
        self.print_preview.verify_print_quality_item(invisible=False)
        self.print_preview.select_print_quality_option(self.print_preview.QUALITY_DRAFT_OPTION)
        assert self.print_preview.get_print_quality_selected_value() == "Draft"
        self.print_preview.select_print_quality_option(self.print_preview.QUALITY_NORMAL_OPTION)
        assert self.print_preview.get_print_quality_selected_value() == "Normal"
        self.print_preview.select_print_quality_option(self.print_preview.QUALITY_BEST_OPTION)
        assert self.print_preview.get_print_quality_selected_value() == "Best"
        self.print_preview.select_print_quality_option(self.print_preview.QUALITY_AUTO_OPTION)
        assert self.print_preview.get_print_quality_selected_value() == "Automatic"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_preview_screen(self, is_multiple=False, source="scanner"):
        """
        1. Load App to Home screen
        2. Connect a target printer
        3. Click on Scan from Home screen
        4. Click on Scan button

        :param is_multiple: scan one more page if it is true
        :param source: What to source images form. "scanner", "camera" or "file"
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        if source == "scanner":
            self.fc.flow_home_scan_single_page(self.p, from_tile=True)
            self.scan.select_adjust_next_btn(timeout=20)
        elif source == "camera":
            self.fc.flow_home_camera_scan_pages(number_pages=2 if is_multiple else 1)
        else:
            self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
            self.file_photos.verify_limited_access_popup()
            self.file_photos.select_continue_btn()
            self.file_photos.select_local_item(self.file_photos.MY_PHOTOS_TXT)
            self.local_photos.select_recent_photo_by_index()
            self.preview.select_print_size(self.preview.PRINT_SIZE_4x6, raise_e=False)
        self.preview.verify_preview_screen()
        if is_multiple and source != "camera":
            self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
            self.fc.flow_scan_capture(self.scan.SOURCE_PRINTER_SCAN_OPT, mode="document")
            self.scan.select_adjust_next_btn(timeout=20)
            self.preview.verify_preview_screen()
            assert self.preview.verify_preview_page_info()[1] == 2, "Page count should be 2"