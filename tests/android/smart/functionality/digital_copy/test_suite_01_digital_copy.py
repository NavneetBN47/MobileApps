from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import PACKAGE


pytest.app_info = "SMART"

class Test_Suite_01_Digital_Copy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    @pytest.mark.parametrize("resize_type",["original_size", "fit_to_page", "fill_page"])
    def test_01_copy_resize_type(self, resize_type):
        """
        Description: C31297215, C31297158, C31297159, C31297183, C31297184, C31297185
         1. Load to Copy preview screen
         2. Click on Resize button
         3. Select Resize type on Resize screen
            + Original Size
            + Fit to page
            + Fill page
        Expected Result:
         2. Verify Resize screen with below points:
            + Original Size
            + Fit to page
            + Fill page
         3. Verify Copy screen
        """
        resize_types = {
            "original_size": self.digital_copy.ORIGINAL_SIZE,
            "fit_to_page": self.digital_copy.FIT_TO_PAGE,
            "fill_page": self.digital_copy.FILL_PAGE
        }
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.verify_copy_preview_screen()
        self.digital_copy.select_resize_btn()
        self.digital_copy.verify_resize_screen()
        self.digital_copy.select_resize_type(resize_types[resize_type])
        self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=True)

    def test_02_copy_add_more_page(self):
        """
        Description: C31297191, C31297180
         1. Load to Copy preview screen
         2. Click on Add more page button
         3. Click on Capture button with batch mode
         4. Click on Print Help button under 3 dot icon
         5. Check 2 boxes
         6. Check the 3rd boxes, and click on OK button
        Expected Result:
         2. Verify Capture screen with below points:
            + Paper Size dropdown menu cannot click
         3. Verify Copy screen with below points:
            + Left and Right arrow is visible and clickable
            + Page of number is visible
         4. Verify Print Help screen with below points:
            + Title
            + 3 checkboxes
         5. OK button isn't clickable
         6. OK button is clickable -> Copy Preview screen display
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_add_btn()
        self.digital_copy.verify_paper_size_dropbox(is_enabled=False)
        self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
        self.digital_copy.select_previous_page_btn()
        self.digital_copy.select_next_page_btn()
        self.digital_copy.verify_copy_page_number()
        self.digital_copy.select_print_help()
        self.digital_copy.verify_print_help_screen()
        self.digital_copy.toggle_cb_on_print_help(self.digital_copy.PRINT_PLUGIN_CB)
        self.digital_copy.toggle_cb_on_print_help(self.digital_copy.PRINTING_SETTINGS_CB)
        self.digital_copy.verify_ok_button(is_enabled=False)
        self.digital_copy.toggle_cb_on_print_help(self.digital_copy.PRINTER_SELECT_CB)
        self.digital_copy.verify_ok_button(is_enabled=True)
        self.digital_copy.select_printer_setup_help_ok_btn()
        self.digital_copy.verify_copy_preview_screen()

    @pytest.mark.parametrize("link_name",["open_google_play", "open_print_settings"])
    def test_03_copy_print_help_link_verify(self, link_name):
        """
        Description: C31297181, C31297182
         1. Load to Copy preview  screen
         2. Click on Print Help button under 3 dot icon
         3. Click on Links on Print Help screen:
            + Open Printing Settings link
            + Google Play link
        Expected Result:
         3. Verify the link we clicked
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_print_help()
        if link_name == "open_google_play":
            self.digital_copy.select_link_on_print_help(self.digital_copy.OPEN_GOOGLE_PLAY)
            self.digital_copy.verify_google_play_link()
        else:
            self.digital_copy.select_link_on_print_help(self.digital_copy.OPEN_PRINT_SETTINGS)
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.SETTINGS), "Android Settings is not launching"

    def test_04_copy_3_pages_delete_single_page(self):
        """
        Description: C31297179, C31297178, C31297192, C31297193, C31297160
        1. Load to Copy preview screen
        2. Click on Add more page button on Copy screen
        3. CLick on capture button with batch mode
        4. Click on Add more page button on Copy screen
        5. CLick on capture button with manual mode
        6. Click on x button on Copy screen
        7. Click on Back button
        8. Click on Cancel button
        9. Click Back button
        10. Click on LEAVE button

        Expected Result:
        6. Verify Copy screen with below points:
           + number of page is visible
           + previous and next page button are visible
        7. Verify are you sure popup screen
        8. Verify Copy screen
        10. Verify Home screen
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        # Digital copy with Batch mode on smart app is not ready for multi page function
        for _ in range(2):
            self.digital_copy.select_add_btn()
            self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
        self.digital_copy.select_delete_page_btn(num_of_del_pages=1)
        self.digital_copy.verify_previous_next_page_btn(invisible=False)
        self.digital_copy.verify_copy_page_number(invisible=False)
        self.fc.select_back()
        self.digital_copy.verify_are_you_sure_popup()
        self.digital_copy.select_cancel_btn()
        self.digital_copy.verify_copy_preview_screen()
        self.fc.select_back()
        self.digital_copy.verify_are_you_sure_popup()
        self.digital_copy.select_leave_btn()
        self.home.verify_home_nav()

    def test_05_copy_multi_pages_delete_all_pages(self):
        """
        Description: C31297194
        1. Load to Copy preview screen
        2. Click on Add more page button on Copy screen
        3. CLick on capture button with batch mode
        4. Click on x button on Copy screen
        5. Click on x button on Copy screen
        Expected Result:
        5. Verify Camera Capture screen with below points:
           + Paper Size button can be clickable
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_add_btn()
        self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
        self.digital_copy.select_delete_page_btn(num_of_del_pages=2)
        self.digital_copy.verify_paper_size_dropbox(is_enabled=True)

    @pytest.mark.parametrize("pages_number", ["1_copy_1_page", "1_copy_multi_pages", "multi_copies_1_page", "multi_copies_pages"])
    def test_06_start_color_copy_by_pages(self, pages_number):
        """
        Description: C31297187, C31297195, C31297196, C31297197,C31297188, C31297189, C31297190, C31297203, C31297391
        1. Load to Copy preview screen
        2. Please select copy page and numbers (X X) based on parameter of "pages_number"
           + 1 copy 1 page
           + 1 copy with multi pages:
               + click add more page button
               + click on capture button with batch mode
           + multi copies with 1 page:
               + click on Copies button
               + Select 2 copies
           + multi copies and pages:
               + click add more page button
               + click on capture button with batch mode
               + click on Copies button
               + select 3 copies
        3. Click on Start Color Copy button on Copy screen
        Expected Result:
        3. Verify Copy sent screen with below points:
           + Sent! Message
           + Home button
           + Back button
        :param pages_number:
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        if pages_number == "1_copy_multi_pages":
            self.digital_copy.select_add_btn()
            self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
        elif pages_number == "multi_copies_1_page":
            self.digital_copy.select_num_of_copies(copies_num=2)
        elif pages_number == "multi_copies_pages":
            self.digital_copy.select_add_btn()
            self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
            self.digital_copy.select_num_of_copies(copies_num=3)
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_type(self.digital_copy.FIT_TO_PAGE)
        self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=True)

    @pytest.mark.parametrize("pages_number", ["1_copy_1_page", "1_copy_multiple_pages", "multi_copies_pages", "multi_copies_1_page"])
    def test_07_start_black_copy_by_pages(self, pages_number):
        """
        Description: C31297198, C31297199, C31297200, C31297201, C31297392
        1. Load to Copy preview screen
        2. Please select copy page and numbers (X X) based on parameter of "pages_number"
           + 1 copy 1 page
           + 1 copy with multi pages:
               + click add more page button
               + click on capture button with batch mode
           + multi copies with 1 page:
               + click on Copies button
               + Select 2 copies
           + multi copies and pages:
               + click add more page button
               + click on capture button with batch mode
               + click on Copies button
               + select 3 copies
        3. Click on Start Color Copy button on Copy screen
        Expected Result:
        3. Verify Copy sent screen with below points:
           + Sent! Message
           + Home button
           + Back button
        :param pages_number:
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        if pages_number == "1_copy_multi_pages":
            self.digital_copy.select_add_btn()
            self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
        elif pages_number == "multi_copies_1_page":
            self.digital_copy.select_num_of_copies(copies_num=3)
        elif pages_number == "multi_copies_pages":
            self.digital_copy.select_add_btn()
            self.scan.start_capture(change_check=self.scan.COPY_CHANGE_CHECK)
            self.digital_copy.select_num_of_copies(copies_num=2)
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_type(self.digital_copy.FIT_TO_PAGE)
        self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=False)

    @pytest.mark.capture_screen
    def test_08_access_copy_without_printer_connected(self):
        """
        Description: C31298229, C31298230, C31297157
        1. Load to Home screen without printer connected
        2. Click on Copy Tile
        Expected Result:
        2. Verify popup screen with below points:
           + Feature Unavailable tile
           + Message
           + OK button
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.COPY), is_permission=False)
        self.home.dismiss_feature_unavailable_popup(is_checked=True)
        self.home.verify_home_nav()