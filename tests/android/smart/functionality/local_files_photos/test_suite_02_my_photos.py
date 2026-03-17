from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest
import time

pytest.app_info = "SMART"


class Test_Suite_02_My_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.print_preview = cls.fc.flow[FLOW_NAMES.PRINT_PREVIEW]
        cls.dev_settings = cls.fc.flow[FLOW_NAMES.DEV_SETTINGS]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_my_photos_share_gmail(self):
        """
        Descriptions: C31297247, C31297251, C31297250
            1.Load Photos screen via tiles or icon
            2. Click on My Photos
            3. Select first photo in album which name is corresponding image type
            4. Make a share via gmail

        Expected Result:
            Verify:
                3.Landing Page:
                         - Edit button
                4. At Landing Page for sharing tab,
                         - file name text box is not display
                         - Share button display
                    Then, Share gmail successul
        """
        # Make sure, not affect by previous test as this one no need to connect to printers
        self.fc.reset_app()
        self.__load_my_photos_screen(from_tile=False)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address, "{}".format(self.test_01_my_photos_share_gmail.__name__), from_email=self.email_address)

    def test_02_my_photos_select_unsupported_photo(self):
        """
        Descriptions: C31297253, C39432332
            1.Load Photos screen via tiles or icon
            2. Click on My Photos
            3. CLick on Album button
            4. Select an unsupported photo from "jpeg_corrupted" / bmp / gif / webp folder
            5. Click on X button on Select a photo screen

        Expected Result:
            4.Verify Select a Photo screen
            5. Verify files & photo screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.verify_files_photos_screen()
        for album in ["jpeg_corrupted", "bmp", "gif", "webp"]:
            self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
            time.sleep(3)
            if self.local_photos.verify_photo_picker_optional_screen(raise_e=False):
                self.driver.press_key_back()
                pytest.skip("New image photo picker doesn't support albums feature according to the eamil from developers")
            else:
                # new image picker is available as it comes with the google play service not based on OS version. Some device still use old image picker. This is confirmed by Android smart developer team
                self.local_photos.select_album_photo_by_index(album_name=album, change_check=None)
                self.local_photos.verify_select_photo_screen()
                self.fc.select_back()
                self.files_photos.verify_files_photos_screen()

    def test_03_my_photos_back_key(self):
        """
        Description: C33569058, C33569059, C31297248, C31297254, C36683791, C36691553
            1. Load Photos screen from Home
            2. Click on My Photos button
            3. Click Back key (app/mobile device)
            4. Click on My Photos
            5. Select any supported image to go to Landing Page
            6. At Preview screen, click on back (app/mobile device)

        Expected Result:
            3. Photos screen
            6. Files & Photos screen
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.driver.press_key_back()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_recent_photo_by_index()
        self.preview.verify_preview_screen()
        self.fc.select_back()
        self.files_photos.verify_files_photos_screen()
        self.fc.select_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.driver.press_key_back()
        self.home.verify_home_nav()

    def test_04_simplified_flow_without_printer_on_carousel(self):
        """
        Descriptions: C33416533, C33569063, C36681686, C36770446, C36770448, C36770457, C36862944, C37856760
            1. Load Photos screen via tiles
            2. Select a photo from any album
            3. Select a printer from Printer list
            4. Click on Print button

        Expected Result:
            2. Verify Printer list screen displays
            4. Print job can be done success
        """
        self.__load_my_photos_screen(from_tile=True)
        self.preview.verify_select_printer_screen()

    def test_05_paper_setting_screen_shows_extended_available_options(self):
        """
        Descriptions: C33569066, C36681685, C36829553, C36829554, C36829557, C36829564, C36941943, C36829560, C36864172,
                      C36829558, C36829556, C36829561, C36829562, C37856759, C37407430, C36829568, C36829559,
                      C36829563, C36829565, C36864126, C37378149, C37407416, C36829550, C36864174, C36864173, C36681685, C40805300, C40807141, C36863433, C36902339, C39745331, C40672411, C41118232
            1. Launch Smart app, and select a printer from Printers list
            2. Click on Print Photos tile
            3. Select a photo from any album
            4. Select the picture
            5. If the printer is Novelli printer, then click on Cards option
            6. Click on Printer's bonjour name from the top
            7. Click on Close button from Select printer screen
            8. Click on Layout button
            9. Click on i icon
            10. Click Paper Button
            11. Click on Landscape orientation button
            12. Click on Undo button
            13. Click on potrait orientation button
            14. Click on Redo button
            15. Click on Preview button
            16. Click on Back button
            17. Click on Back button
            18. Click on No button
            19. Click on Back button
            20. Click on Yes button

        Expected Result:
            4. Verify DS screen
            5. Verify the Cards option screen if printer is Novelli printer. Otherwise the Cards option is invisible for non-novelli printers
            6. Verify the Select Printer screen
            7. Verify DS screen
            8. Verify Layout option screen
            9. Verify tooltip information screen
            10. Verify the Paper option screen with tooltip icon is invisible
            15. Verify Print Preview screen
            16. Verify DS screen
            17. Verify Exit without saving? popup
            18. Verify DS screen
            20. Verify Home screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_more_options_debug_settings()
        self.dev_settings.toggle_duplex_photo_printing()
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.local_photos.select_recent_photo_by_index()
        if self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.select_photo_picker_add_btn()
        if self.local_photos.verify_photo_picker_closed_option(raise_e=False):
            self.local_photos.select_photo_picker_done_btn()
        self.preview.verify_dynamic_studio_screen(timeout=15)
        self.preview.verify_paper_main_tray_option()
        #This verification depends on printers. some printers doesn't support on Photo Tray
        self.preview.verify_paper_photo_tray_option(raise_e=False)
        if "novelli" in self.p.p_obj.projectName:
            self.preview.verify_cards_options(invisible=False)
            self.preview.select_ds_cards_btn()
            self.preview.verify_paper_main_tray_option(invisible=True)
            self.preview.verify_paper_photo_tray_option(invisible=True)
        else:
            self.preview.verify_cards_options(invisible=True)
        self.preview.select_printer_title()
        self.preview.verify_select_printer_screen()
        self.fc.select_back()
        self.preview.verify_dynamic_studio_screen()
        self.preview.select_ds_layout_btn()
        self.preview.verify_layout_options()
        self.preview.verify_info_btn()
        self.preview.select_info_btn()
        self.preview.verify_tooltip()
        original_img = self.preview.capture_crop_image()
        self.preview.select_crop_btn()
        crop_after_img = self.preview.capture_crop_image()
        assert saf_misc.img_comp(original_img, crop_after_img) > 0.01, "DS image should not match original image after crop option"
        self.preview.select_fill_btn()
        fill_after_img = self.preview.capture_crop_image()
        assert saf_misc.img_comp(crop_after_img, fill_after_img) > 0.01, "DS image should not match image after fill option"
        self.preview.select_ds_rotate_btn()
        rotate_after_img = self.preview.capture_crop_image()
        assert saf_misc.img_comp(fill_after_img, rotate_after_img) > 0.01, "DS image should not match image after rotate option"
        self.preview.select_flip_h_btn()
        flip_h_after_img = self.preview.capture_crop_image()
        assert saf_misc.img_comp(rotate_after_img, flip_h_after_img) > 0.01, "DS image should not match image after flip h option"
        self.preview.select_ds_paper_btn()
        self.preview.verify_info_btn(invisible=True)
        self.preview.select_landscape_orientation_button()
        self.preview.select_undo_btn()
        self.preview.select_ds_paper_btn()
        self.preview.select_potrait_orientation_button()
        self.preview.select_redo_btn()
        self.preview.verify_dynamic_studio_screen()
        self.preview.select_preview_btn()
        self.print_preview.verify_print_preview_screen()
        self.fc.select_back()
        self.fc.select_back()
        self.preview.verify_exit_without_saving_popup()
        self.preview.select_no_btn()
        self.fc.select_back()
        self.preview.select_yes_btn()
        self.home.verify_home_nav()

    def test_06_my_photos_print(self):
        """
        Descriptions: C33416532, C33568582, C33416534, C33569062, C31297252, C36941982, C31297388, C34347729, C31297402, C31297403
            1.Load Photos screen via tiles or icon
            2. Click on My Photos
            3. Select first photo in album which name is corresponding image type
            4. Make a printing job

        Expected Result:
            Verify:
                3.Landing Page:
                    - Edit button
                4. Printing job should be successful
        """
        self.fc.reset_app()
        self.__load_my_photos_screen(is_printer=True, from_tile=True)
        self.preview.verify_dynamic_studio_screen(timeout=20)
        self.preview.select_preview_btn()
        self.fc.flow_preview_make_printing_job(self.p, is_from_print_photo_tile=True)

    def test_07_simplified_flow_from_print_document_tile(self):
        """
        Descriptions: C36684014
            1. Load Smart app to Home screen wth HPID login
            2. Click on Print Document tile from Home screen
            3. Click on My Photo screen

        Expected Result:
            3. Verify My Photos screen with new UI if the android device has support latest google play services, otherwise verify My Photo function with old UI
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_DOCUMENTS))
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        if not self.local_photos.verify_select_photo_screen(raise_e=False):
            self.local_photos.verify_photo_picker_optional_screen(raise_e=True)

    def test_08_simplified_flow_layout_function(self):
        """
        Descriptions: C36863429, C36863527, C36864177, C36863575, C36864178, C36863576, C36864179, C36864180, C36940686, C36941942
        1. Launch Smart app, and select a printer from Printers list
        2. Click on Print Photos tile
        3. Select a photo from any album
        4. Select the picture
        5. Click on Layout button
        6. Click on Fit/ Fill / Rotate/ Border/ Flip H and V option from Layout options
        7. Click on Preview button
        8. Click on Share button

        Expected Result:
        5. Verify Layout screen
        7. Verify Print Preview screen
        8. Verify the photo can be shared to gmail success
        """
        self.fc.reset_app()
        file_name = self.test_08_simplified_flow_layout_function.__name__
        self.__load_my_photos_screen(is_printer=True, from_tile=True)
        self.preview.verify_dynamic_studio_screen(timeout=20)
        self.preview.select_ds_layout_btn()
        self.preview.verify_layout_options()
        self.preview.select_fit_btn()
        self.preview.select_ds_rotate_btn()
        self.preview.select_fill_btn()
        self.preview.select_border_btn()
        self.preview.select_flip_h_btn()
        self.preview.select_preview_btn()
        self.print_preview.verify_print_preview_screen()
        self.driver.swipe()
        self.print_preview.select_share_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, "{}".format(file_name), from_email=self.email_address)

    def test_09_verify_ds_screen_with_multiple_photos_selected(self):
        """
        Descriptions: C40666526, C36941647, C40674555, C40666948, C37727555, C40488785, C40488803, C40666525, C40666524, C41118165
        1. Launch Smart app, and select a printer from Printers list
        2. Click on Print Photos tile
        3. Select a single photo from any album, and click on Done or add button according to the photo picker version
        4. Click on Preview button
        5. Click on Back button until the photo picker screen displays again
        6. Select 2 images, and click on Done or add button according to the photo picker version
        7. Tap the left arrow or right arrow
        8. Click on Preview button

        Expected Result:
        4. Verify the Print Preview screen with single photo selected
        6. Verify DS screen with below points:
           - A carousel with left and right arrows with the image count as shown
           - Redo & Undo buttons
           - Next button
           - Verify Cards option is invisible on the screen
        7. - Verify the left and right arrow are tappable
            - Verify the next image displays in the carousel
        8. Verify the Print Preview screen with 2 photos displays on screen
        """
        self.fc.reset_app()
        self.__load_my_photos_screen(is_printer=True, from_tile=True)
        self.preview.verify_dynamic_studio_screen(timeout=20)
        self.preview.select_preview_btn()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.verify_print_preview_image_info(is_one_image=True)
        self.print_preview.select_back_btn()
        self.fc.select_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.local_photos.select_multiple_photos(num=2)
        if self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.select_photo_picker_add_btn()
        if self.local_photos.verify_photo_picker_closed_option(raise_e=False):
            self.local_photos.select_photo_picker_done_btn()
        self.preview.verify_dynamic_studio_screen(timeout=20)
        self.preview.verify_cards_options(invisible=True)
        self.preview.select_preview_btn()
        self.print_preview.verify_print_preview_screen()
        assert self.print_preview.verify_print_preview_image_info(is_one_image=False)[1] == 2, "Image count should be two"

    def test_10_verify_clicking_a_selected_image_again_deselects_it(self):
        """
        Descriptions: C40666524
        1. Launch Smart app, and select a printer from Printers list
        2. Click on Print Photos tile
        3. Select a single photo from any album
        4. Deselect the photo
        5. Select 2 images
        6. Deselect one image

        Expected Result:
        3. Verify the Done button or Add button shows on the screen
        4. Verify the Done button or Add button disappears on the screen
        6. Verify only one image selected
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.files_photos.verify_limited_access_popup()
        self.files_photos.select_continue_btn()
        self.local_photos.select_recent_photo_by_index()
        if not self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.verify_multi_selection_screen()
            assert self.local_photos.get_number_selection() == "1", "it should have one image selected"
        self.local_photos.select_recent_photo_by_index()
        if not self.local_photos.verify_photo_picker_optional_screen(raise_e=False):
            assert self.local_photos.get_number_selection() == "Select photos", "no images selected"
        self.local_photos.select_cancel_btn()
        if self.home.verify_home_nav(raise_e=False):
            self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
            self.files_photos.verify_limited_access_popup()
            self.files_photos.select_continue_btn()
        self.local_photos.select_multiple_photos(num=2)
        if not self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.verify_multi_selection_screen()
            assert self.local_photos.get_number_selection() == "2", "it should have two images selected"
        self.local_photos.select_recent_photo_by_index()
        if not self.local_photos.verify_photo_picker_optional_screen(raise_e=False):
            assert self.local_photos.get_number_selection() == "1", "it should have one image selected"

    def test_11_end_to_end_duplex_printing_functionality(self):
        """
        C41189574, C41189556, C41117045, C40922721, C41060966, C41117733, C41061388, C40805300, C41139369, C41139368
        Steps:
        1. Launch Smart app, and select a novelli printer from Printers list
        2. Click on Print Photos tile
        3. Select a photo from any album
        4. Click on Done button
        5. Click on Cards option
        6. Click on Front and Back button
        7. Select any template from the template list
        8. Click on Paper Option
        9. Change the paper Orientation
        10. Click on Cards option again
        11. Select any template from the template list
        12. Click on Paper option
        13. Select any non-photo duplex paper
        14. Click on Preview button
        15. Click on Front and Back button
        16. Click on Print button

        Expected Result:
        5. Verify DS screen with Cards option:
            - Front button
            - Back button
        6. Verify the image changed after clicking on Front and Back button
        7. Verify the template list on the screen
        9. Template get reset after changing the paper orientation
        10. Verify the template list get changed after the paper orientation is changed
        12. Verify the selected tray is changed to Photo Tray and paper selected is Photo Paper
        13. Verify the template get reset after changing the paper size
        14. Verify the 2 images displays on Print Preview screen
        15. Verify the Front and Back image on Print Preview screen
        16. Verify the print job is printed success
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_more_options_debug_settings()
        self.dev_settings.toggle_duplex_photo_printing()
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.local_photos.select_recent_photo_by_index()
        if self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.select_photo_picker_add_btn()
        if self.local_photos.verify_photo_picker_closed_option(raise_e=False):
            self.local_photos.select_photo_picker_done_btn()
        self.preview.verify_dynamic_studio_screen(timeout=20)
        if "novelli" not in self.p.p_obj.projectName:
            self.preview.verify_cards_options(invisible=True)
            pytest.skip("Non novelli printer doesn't support Cards function")
        self.preview.verify_cards_options(invisible=False)
        self.preview.select_ds_cards_btn()
        self.preview.verify_cards_screen()
        image_with_front_option = self.preview.capture_crop_image()
        self.preview.select_cards_back_btn()
        image_after_back_option = self.preview.capture_crop_image()
        assert saf_misc.img_comp(image_with_front_option, image_after_back_option) > 0.02, "The image should be changed"
        self.preview.select_mothers_day_template()
        image_after_mothers_day_template = self.preview.capture_crop_image()
        self.preview.select_ds_paper_btn()
        self.preview.select_potrait_orientation_button()
        image_after_paper_orientation_option = self.preview.capture_crop_image()
        assert saf_misc.img_comp(image_after_mothers_day_template, image_after_paper_orientation_option) > 0.02, "The image should be changed"
        self.preview.select_ds_cards_btn()
        self.preview.select_graduation_template()
        self.preview.select_ds_paper_btn()
        self.preview.select_ds_paper_photo_tray_option()
        self.preview.select_ds_cards_btn()
        self.preview.select_graduation_template()
        self.preview.select_cards_back_btn()
        self.preview.select_mothers_day_template()
        self.preview.select_preview_btn()
        self.print_preview.verify_print_preview_screen()
        self.fc.flow_preview_make_printing_job(self.p, is_from_print_photo_tile=True)

    # -----------------         PRIVATE FUNCTIONS       ---------------------------------
    def __load_my_photos_screen(self, is_printer=False, from_tile=True):
        """
        From Home screen:
            - Select target printer if is_printer = True
            - Click on Print Photos tile for photos icon
            - Click on MY Photos button
        :param is_printer: Loads the SPL printer in the smart app before navigating to photos screen
        :param from_tile: Navigates to photos screen by tile instead of bottom navbar button
        :param remove_printers: Removes all loaded printers before navigating to photos screen. SPL printer
            will still be loaded after printer removal if is_printer=True
        """
        self.fc.flow_load_home_screen()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p)
        if from_tile:
            self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        else:
            self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if not is_printer:
            self.files_photos.verify_limited_access_popup()
            self.files_photos.select_continue_btn()
        if from_tile:
            self.local_photos.verify_photo_picker_optional_screen(raise_e=False)
        else:
            self.files_photos.verify_files_photos_screen()
            self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_recent_photo_by_index()
        if self.local_photos.verify_photo_picker_view_selected_option(raise_e=False):
            self.local_photos.select_photo_picker_add_btn()
        if self.local_photos.verify_photo_picker_closed_option(raise_e=False):
            self.local_photos.select_photo_picker_done_btn()