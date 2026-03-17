import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from SAF.misc import saf_misc

pytest.app_info = "SMART"


class Test_Suite_03_My_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.stack = request.config.getoption("--stack")

        # Define flows
        cls.photos = cls.fc.fd["photos"]
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.printers = cls.fc.fd["printers"]
        cls.gmail_api = cls.fc.fd["gmail_api"]
        cls.share = cls.fc.fd["share"]
        if pytest.platform == "IOS":
            cls.gmail = cls.fc.fd["gmail"]
            cls.ios_system = cls.fc.fd["ios_system"]
        cls.sys_config = ma_misc.load_system_config_file()

        # Define variables
        cls.email_address = \
        saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(i_const.TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]

    def test_01_my_photos_share_to_gmail(self):
        """
        IOS & MAC: Description: C31297247, C34267312
        IOS only: C31297251 - share photo to gmail
        1. Load to Home screen
        2. Click on View & Print icon from Home screen
        3. Click on Continue button
        4. Allow permission to access Photos
        5. Click on Albums button
        6. Click on Recents folder, and select a photo from the list
        7. Click on Share/Save button
        8. Click on Share/Save button
        9. Select gmail from the app list

        Expected Result:
        5. Verify Albums item shows on View & Print screen
        9. Verify image can be shared success to gmail
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next_button()
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        if pytest.platform == "IOS":
            self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
            self.common_preview.verify_title(self.common_preview.SHARE_SAVE_TITLE, use_str_id=True)
        else:
            self.common_preview.verify_an_element_and_click(self.common_preview.SHARE_BTN)
            self.common_preview.verify_title(self.common_preview.SHARE_TITLE)
        self.common_preview.select_action_btn()
        if pytest.platform == "IOS":
            self.share.select_gmail()
            subject = "{}_{}".format("test_01_my_photos_share_to_gmail", self.driver.driver_info["udid"])
            self.gmail.compose_and_send_email(self.email_address, subject_text=subject)
            msg_id = self.gmail_api.search_for_messages(q_from=self.email_address,
                                                        q_to=self.email_address, q_unread=True,
                                                        q_subject=subject, timeout=300)
            attachment_names = self.gmail_api.get_attachments(msg_id[0][u'id'])
            for index, name in enumerate(attachment_names):
                temp_name = name.split("-")
                attachment_names[index] = "_".join(temp_name)
            self.gmail_api.delete_email(msg_id)
            assert len(attachment_names) == 1

    def test_02_my_photos_select_images(self):
        """
        IOS & MAC:
        Description: C31297249, C31297250
            1. Load to Home screen
            2. Click on View & Print icon from Home screen
            3. Click on Continue button
            4. Allow permission to access Photos
            5. Select a photo from Recent album
            6. Select 4 photos from the list
            7. Click on Next button
            8. Click on Back button
            9. Select multiple photos from screen again, and click on Cancel button after that

         Expected Result:
            5. Verify Recents photo screen
            6. Verify multiple photos selected on the screen
            7. Verify Preview screen
            9. Verify Photos list screen
        """
        if pytest.platform == "MAC":
            # Defect link: https://hp-jira.external.hp.com/browse/AIOI-21057
            pytest.skip("Skip this test on MAC platform because of defect while selecting multiple photos")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.verify_photos_screen()
        self.photos.select_multiple_photos(end=4)
        self.photos.verify_multi_selected_photos_screen()
        self.photos.select_next_button()
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        self.common_preview.select_navigate_back()
        self.photos.verify_photos_screen()
        self.photos.select_multiple_photos(end=4)
        self.photos.select_navigate_back()
        self.photos.verify_photos_screen()

    def test_03_simplified_flow_without_printer_connected(self):
        """
        Description: C33416533, C36943848, C39447198, C36316295, C34206153, C40488785, C40488803, C40666524, C40666525
            1. Load to Home screen
            2. Click on Print Photos tile
            3. Click on Continue button
            4. Allow permission to access Photos
            5. Click on Cancel button
            6. Click on Print Photos tile
            7. Click on My Photos button
            8. Click on Albums option
            9. Click on Recents option
            10. Select a photo and click on Next button
            11. Click on Close button
            12. Click on Back button three times
            13. Click on Print Photos tile
            14. Select two photos from the Photo list
            15. Deselect one photo from the list
            16. Click on Next button
            17. Choose the first printer from the list
            18. Click on Next button

         Expected Result:
            4. Verify no photo selected screen
            5. Verify Home screen
            7. Verify My Photos screen
            10 Verify Choose the printer popup
            12.Verify Home screen
            14.Verify 2 photos selected from the screen
            15.Verify 1 photo selected from the screen
            16.Verify Print Preview screen without printer connected (Choose your printer popup)
            17. Verify DS screen
            18. Verify the Print Preview screen
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.select_continue()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.verify_no_photos_selected_screen()
        self.photos.select_cancel()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.select_continue()
        self.photos.select_navigate_back()
        self.photos.verify_my_photos_screen()
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next_button()
        self.photos.select_close_btn()
        self.photos.select_navigate_back()
        self.photos.select_navigate_back()
        self.photos.select_navigate_back()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.select_continue()
        self.photos.select_multiple_photos(end=2)
        assert self.photos.get_number_from_photo_selected_screen() == 2, "It should have 2 images get selected"
        self.photos.select_photo_by_index(index=1)
        assert self.photos.get_number_from_photo_selected_screen() == 1, "It should have one image get selected"
        self.photos.select_next_button()
        self.photos.verify_choose_printer_popup()
        self.photos.select_first_printer_in_popup()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_preview_btn()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)

    def test_04_simplified_flow_with_printer_connected(self):
        """
        Description: C33416532, C33416534, C33568582, C33569062, C33569066
            1. Load to Home screen, and select a printer to carousel
            2. Click on Print Documents icon
            3. Allow permission to access Photos
            4. Select a photo from Recent album
            5. Click on Print Preview button from Preview screen
            6. Click on the image from Print Preview screen
            7. Click on Done button
            8. Click on Paper Size option from Print Preview screen

         Expected Result:
            3. Verify user only can select one photo from the Photos list screen
            4. Verify Print size screen if novelli printer gets selected to carousel
            5. Verify Print Preview screen
            6. Verify Image layout screen
            8. Verify  Paper size list screen with items:
               - Paper ready to use
               - Additional paper options
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_albums_tab()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next_button()
        self.common_preview.select_print_size(self.common_preview.DOCUMENT_SIZE_8x11, raise_e=False)
        self.common_preview.verify_title(self.common_preview.PREVIEW_TITLE)
        self.common_preview.select_bottom_nav_btn(self.common_preview.PRINT_PREVIEW_BTN)
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
        self.common_preview.select_preview_image()
        self.common_preview.verify_transform_screen()
        self.common_preview.select_done()
        self.common_preview.select_print_preview_pan_option_screen()
        self.common_preview.verify_an_element_and_click(self.common_preview.PAPER)
        self.common_preview.verify_paper_screen()

    def test_05_my_photos_back_key(self):
        """
        Description: C33569058, C33569059, C31297254, C31297248
            1. Load to Home screen
            2. Click on Print Photos tile
            3. Click on Back button
            4. Click on Print Document tile
            5. Click on Back button

         Expected Result:
            3. Verify Home screen is displayed
            4. Verify Files & Photos screen
            5. Verify Home screen is displayed
        """
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.home.select_continue()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_photo_by_index(index=1)
        self.photos.select_next_button()
        self.common_preview.select_close()
        self.photos.select_cancel()
        self.home.verify_home()
        if pytest.platform == "MAC":
            self.home.dismiss_tap_account_coachmark()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_DOCUMENTS)
        self.home.select_continue()
        self.files.verify_files_screen()
        self.home.select_home_icon()
        if self.home.verify_close(raise_e=False):
            self.home.select_close()
        self.home.verify_home()

    @pytest.mark.parametrize("allow_access", ["select_photos", "dont_allow", "allow"])
    def test_06_verify_access_photos_popup(self, allow_access):
        """
        C36943866 - Verify the behavior of Don't Allow option on Access your photos pop up
        C36943869 - Verify the behavior of Back Arrow button on Access your photos pop up
        C36943873 - Verify the behavior of Select Photos option on Access your photos pop up
        C36257273 - Verify the behavior when User has not agreed to access the photos option
        C36279990 - Verify user is directed to Recents screen on tapping Print photos tile
        C36940686 - Verify Print Preview screen UI
        C36941647 - Verify that Printer/Paper selection is not allowed on Print Preview screen
        C36941942, C38975024 - Verify the Share option on Print Preview screen
        C36960621 - Verify the Printer settings drawer menu UI when printer is ready
        C36941982 - Verify the Print button on Print Preview screen
        C36941943 - Verify the back arrow button on Print Preview screen
        C34215961 - Verify the behavior of Back button on Recents screen
        C34215963 - Verify behavior of Back button on Albums screen
        C33594516 - Verify Albums screen UI when User has accepted access all photos option
        C33490915 - Verify the user can select only one picture from My Photos when tapped on Print Photos tile
        C36829556, C36829557 - Top Navigation: tap on Preview, tap on back arrow
        C39365702 - Verify the Done button on Print Preview screen.
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        # limit_access popup is also handled here
        if allow_access == "select_photos":
            self.photos.verify_select_photos_btn()
            self.photos.click_select_photos_option()
            self.photos.verify_select_photos_page_after_popup()
        elif allow_access == "dont_allow":
            self.photos.select_allow_access_to_photos_popup(allow_access=False)
            assert self.photos.verify_set_photo_access_btn(raise_e=False), "Allow Photo Access screen was not displayed"
            self.photos.select_navigate_back()
            self.files.verify_my_photos_files_screen()
            self.files.select_navigate_back()
            if self.home.verify_close(raise_e=False):
                self.home.select_close()
            self.home.verify_home()
            self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
            self.photos.select_set_photos_access_btn()
            self.ios_system.verify_hp_smart_title()
        else:
            self.photos.select_allow_access_to_photos_popup()
            self.photos.verify_0_selected_title()
            self.photos.select_photo_by_index(index=1)
            sleep(2)
            self.photos.select_next_button()
            self.common_preview.select_preview_btn()
            self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
            self.common_preview.select_navigate_back()
            self.common_preview.verify_dynamic_studio_screen()
            self.common_preview.select_navigate_back()
            self.photos.verify_0_selected_title()
            self.photos.select_navigate_back()
            self.files.verify_my_photos_files_screen()
            self.files.select_albums()
            self.photos.verify_albums_screen()
            self.photos.select_navigate_back()
            self.files.verify_my_photos_files_screen()
            self.files.select_albums()
            self.photos.select_recents_or_first_option()
            self.photos.select_photo_by_index(index=1)
            self.common_preview.select_preview_btn()
            self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
            self.common_preview.verify_print_preview_ui_elements(self.printer_name)
            self.common_preview.verify_an_element_and_click(self.common_preview.PREVIEW_IMAGE)
            self.common_preview.verify_print_preview_ui_elements(self.printer_name)
            self.common_preview.select_print_preview_pan_option_screen()
            self.common_preview.select_print_preview_share_btn()
            self.share.verify_share_popup()
            self.share.select_close()
            self.common_preview.PRINT_SETTINGS_UI_ELEMENTS.remove(self.common_preview.PAGE_RANGE)
            self.common_preview.PRINT_SETTINGS_UI_ELEMENTS.remove(self.common_preview.TWO_SIDED)
            self.common_preview.verify_an_element_and_click(self.common_preview.PAPER, click=False)
            self.common_preview.select_done()
            self.home.close_organize_documents_pop_up()
            self.home.close_print_anywhere_pop_up()
            self.home.verify_home()

    def test_07_select_photos_functionality(self):
        """
        C34267573 - Verify Albums screen UI when user has accepted access Selected photos option.
        C34267586 - Verify the behavior of Access button on Recents screen when user accepted access Selected photos option.
        C40666526 - Verify DS screen UI when multiple images are selected
        C40666948 - Verify the behavior of image navigation bar (or carousel)
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.verify_0_selected_title()
        self.photos.select_multiple_photos(end=4) # select multiple photos
        self.photos.verify_multi_selected_photos_screen()
        assert self.photos.get_number_from_photo_selected_screen() == 4, "The Photos displayed are not the ones selected"
        self.photos.select_next_button()
        self.common_preview.select_ds_paper_btn() # verify dynamic studio screen
        self.common_preview.select_landscape_orientation_button()
        self.common_preview.select_undo_btn()
        self.common_preview.select_potrait_orientation_button()
        self.common_preview.select_redo_btn()
        self.photos.select_navigate_back()
        self.common_preview.verify_exit_without_saving_popup()
        self.common_preview.select_yes_btn()
        self.photos.verify_0_selected_title()
        assert self.photos.get_number_from_photo_selected_screen() == 4, "The Photos displayed are not the ones selected"
        self.photos.select_cancel()
        if self.home.verify_close(raise_e=False):
            self.home.select_close()
        self.home.verify_home()
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.verify_0_selected_title()
        assert self.photos.get_number_from_photo_selected_screen() == 0, "The Photos displayed are not the ones selected"

    def test_08_paper_setting_screen_shows_extended_available_options(self):
        """
        Descriptions: C33569066, C36681685, C36829553, C36829554, C36829557, C36829564, C36941943, C36829560, C36864172,
                      C36829558, C36829556, C36829561, C36829562, C37856759, C37407430, C36829568, C36829559, C36862944,
                      C36829563, C36829565, C36864126, C37378149, C37407416, C36829550, C36864174, C36864173, C37459402,
                      C36875979, C36829551, C36829566, C36829567, C37823696, C41118232, C40807141
            1. Launch Smart app, and select a printer from Printers list
            2. Click on Print Photos tile
            3. Select a photo from any album
            4. Select the picture. If the printer is novelli printer, then select Cards option first
            5. Click on Printer title
            6. Click on Close button
            7. Click on Layout button
            8. Click on i icon
            9. Click on Paper Option button, then click on Landscape orientation button, redo button, Potrait orentation button, undo button
            10. Click on Next/Preview button
            11. Click on Back button
            12. Click on Back button
            13. Click on No button
            14. Click on Back button
            15. Click on Yes button

        Expected Result:
            4. Verify DS screen with:
               - Next/Preview button on the screen
               - Main Tray shows on screen for non-novelli printers
               - Photo Tray shows on screen for non-novelli printers if the printer supports photos tray
               - Cards option shows on screen for novelli Printer
               - Verify the themes show when Card tab is tapped.
            5. Verify Select Printer screen
            6. Verify DS screen with Preview button shows on screen
            7. Verify the Layout option screen
               Verify the information icon shows on screen
            8. Verify tooltip information
            9. The button on Paper Option screen works
            10. Verify Print Preview screen
            11. Verify DS screen
            12. Verify Exit without saving? popup
            13. Verify DS screen
            15. Verify Home screen
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_photo_by_index()
        self.photos.select_next_button()
        self.common_preview.verify_retrieving_page_size_popup(timeout=5, raise_e=False)
        self.common_preview.verify_dynamic_studio_screen(timeout=15)
        if "novelli" in self.p.p_obj.projectName:
            self.common_preview.verify_cards_options(invisible=False)
            self.common_preview.select_ds_cards_btn()
            self.common_preview.verify_paper_main_tray_option(invisible=True)
            self.common_preview.verify_paper_photo_tray_option(invisible=True)
            self.common_preview.verify_cards_screen()
            self.common_preview.verify_mothers_day_template_option()
            self.common_preview.verify_graduation_template_option()
        else:
            self.common_preview.verify_cards_options(invisible=True)
            self.common_preview.verify_paper_main_tray_option(timeout=15)
            self.common_preview.verify_paper_photo_tray_option(raise_e=False)
        self.common_preview.select_printer_title(self.printer_name)
        self.common_preview.verify_select_printer_screen()
        self.common_preview.select_close()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_ds_layout_btn()
        self.common_preview.verify_layout_options()
        self.common_preview.verify_info_btn()
        self.common_preview.select_info_btn()
        self.common_preview.dismiss_tooltip(raise_e=True)
        self.common_preview.select_ds_paper_btn()
        self.common_preview.select_landscape_orientation_button()
        self.common_preview.select_undo_btn()
        self.common_preview.select_potrait_orientation_button()
        self.common_preview.select_redo_btn()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_preview_btn()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
        self.common_preview.select_navigate_back()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_navigate_back()
        self.common_preview.verify_exit_without_saving_popup()
        self.common_preview.select_no()
        self.common_preview.verify_dynamic_studio_screen()
        self.common_preview.select_navigate_back()
        self.common_preview.select_yes()
        self.photos.verify_multi_selected_photos_screen()

    def test_09_simplified_flow_layout_function(self):
        """
        Descriptions: C36863429, C36863527, C36864177, C36863575, C36864178, C36863576, C36864179, C36864180, C39745331, C40672411, C36863433, C36902339
        1. Launch Smart app, and select a printer from Printers list
        2. Click on Print Photos tile
        3. Select a photo from any album
        4. Select the picture
        5. Click on Layout button
        6. Click on i icon
        7. Click on Crop button and resize the picture
        8. Click on Fit/ Fill / Rotate/ Flip H option from Layout options
        9. Click on Paper button
        10. Click on Preview button
        11. Click on Share button

        Expected Result:
        5. Verify Layout screen, also verify the information icon shows on the screen
        6. Verify the tooltip information message displays quickly
        7. Verify the picture has changed
        8. Verify the image changed after each option
        9. Verify i icon doesn't show on the screen
        10. Verify Print Preview screen
        11. Verify the photo can be shared to gmail success
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        file_name = self.test_09_simplified_flow_layout_function.__name__
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_photo_by_index()
        self.photos.select_next_button()
        self.common_preview.verify_dynamic_studio_screen(timeout=20)
        self.common_preview.select_ds_layout_btn()
        self.common_preview.verify_layout_options()
        self.common_preview.verify_info_btn()
        self.common_preview.select_info_btn()
        self.common_preview.verify_tooltip()
        original_image = self.common_preview.screenshot_ds_image()
        self.common_preview.select_crop_btn()
        x, y = self.common_preview.get_ds_image_coordinates()
        self.common_preview.resize_image_on_ds_screen([x, y], [x, y + 100])
        image_after_crop = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(original_image, image_after_crop) > 0.02, "The image should has change after click on Crop button"
        self.common_preview.select_fit_btn()
        image_after_fit = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_crop, image_after_fit) > 0.02, "The image should has change after click on Fit button"
        self.common_preview.select_ds_rotate_btn()
        image_after_rotate = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_fit, image_after_rotate) > 0.02, "The image should has change after click on Rotate button"
        self.common_preview.select_fill_btn()
        image_after_fill = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_rotate, image_after_fill) > 0.02, "The image should has change after click on Fill button"
        self.common_preview.select_flip_h_btn()
        self.common_preview.select_ds_paper_btn()
        self.common_preview.verify_info_btn(invisible=True)
        self.common_preview.select_preview_btn()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
        self.common_preview.select_print_preview_pan_option_screen()
        self.common_preview.select_print_preview_share_btn()
        self.share.verify_share_popup()
        self.share.select_gmail()
        self.fc.send_and_verify_email(from_email_id=self.email_address, to_email_id=self.email_address, subject=file_name)

    @pytest.mark.parametrize("functionality", ["tap", "doubleTap"])
    def test_10_simplified_flow_resize_and_crop_functionality(self, functionality):
        """
        C37373896 - Verify manual scaling functionality on Layout screen
        C37294744 - Verify image gets in resize mode when tapped once on image
        C37294745 - Verify the image gets in cropped mode when tapped twice on image
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_photo_by_index()
        self.photos.select_next_button()
        self.common_preview.verify_dynamic_studio_screen(timeout=20)
        if not self.common_preview.verify_potrait_orientation_button_selected(raise_e=False):
            self.common_preview.select_potrait_orientation_button()
        self.common_preview.select_ds_layout_btn()
        self.common_preview.verify_ds_image(timeout=15)
        if functionality == "tap":
            self.common_preview.select_ds_image()
        else:
            self.common_preview.double_tap_ds_image()
        original_image = self.common_preview.screenshot_ds_image()
        x, y = self.common_preview.get_ds_image_coordinates()
        self.common_preview.resize_image_on_ds_screen([x, y], [x, y + 100])
        resized_image = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(original_image, resized_image) != 0.0, "The image was not resized"
        self.common_preview.select_ds_paper_btn()
        paper_screen_image = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(paper_screen_image, original_image) != 0.0, "The image was not resized"

    def test_11_select_photos_functionality(self):
        """
        C40666526 - Verify DS screen UI when multiple images are selected
        C40666948 - Verify the behavior of image navigation bar (or carousel)
        C40674387 - Verify the behavior of undo/Redo button - multiple photos
        C40674555 - Verify the Print Preview for multiple images
        C41118165 - Verify the Cards tab is not available when the user selects multiple images.

        Steps:
        1. Launch Smart app, and select a printer from Printers list
        2. Click on Print Photos tile
        3. Select any two photos from any album
        4. Click on Next button
        5. Do some changes on the DS screen for the first image
        6. Click on Right arrow button
        7. Do some changes for the second images
        8. Type on Undo button
        9. Type on Redo button
        10. Click on Next button

        Expected Result:
        4. Verify DS screen with below options:
            - Page number
            - A carousel with left and right arrows with the image count
            - Cards option doesn't show on the screen
        8. Image changed after clicking on Undo button
        9. Image changed after clicking on Redo button
        10. Verify the Print Preview screen with multiple images selected
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_multiple_photos(end=2)
        self.photos.select_next_button()
        self.common_preview.verify_dynamic_studio_screen(timeout=15)
        self.common_preview.verify_cards_options(invisible=True)
        self.common_preview.verify_left_arrow_btn()
        self.common_preview.verify_right_arrow_btn()
        self.common_preview.select_potrait_orientation_button()
        self.common_preview.click_right_arrow_btn()
        original_image = self.common_preview.screenshot_ds_image()
        self.common_preview.select_potrait_orientation_button()
        self.common_preview.select_ds_layout_btn()
        self.common_preview.select_ds_rotate_btn()
        image_after_rotate = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(original_image, image_after_rotate) > 0.02, "The image should be changed"
        self.common_preview.select_undo_btn()
        image_after_undo_option = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_rotate, image_after_undo_option) > 0.02, "The edits of image should be removed"
        self.common_preview.select_redo_btn()
        image_after_redo_option = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_undo_option, image_after_redo_option) > 0.02, "The edits of image should be implemented the removed edit changes"
        self.common_preview.select_preview_btn()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)

    def test_12_end_to_end_duplex_printing_functionality(self):
        """
        C41189574 - End to end Duplex printing
        C41189556 - Verify the Tooltip on Print Preview screen when template is applied to an image
        C41117045 - Verify the behavior of Front and Back buttons on the Print preview Screen.
        C40922721 - Verify that 2 pages (front side and back side) are shown in Print Preview.
        C41060966 - Verify the behavior of front and back buttons for Card.
        C41117733 - Verify the templates list changes according to the Orientation of the paper - Portrait / landscape
        C41061388 - Verify the templates open up when user taps on a theme
        C40805300 - Verify the templates reset when the orientation is changed
        C41139369 - Verify the templates reset when the paper size is changed
        C41117049 - Verify that Zoom in/Zoom out function on Print Preview screen
        C41139368 - Verify the paper and tray type is changed to Photo when cards tab is tapped..

        Steps:
        1. Launch Smart app, and select a printer from Printers list
        2. Click on Print Photos tile
        3. Select a photo from any album
        4. Click on Next button
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
        17. Click on Zoom in/out button

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
        17. Verify the Zoom in/out functin works well
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_PRINT_PHOTOS)
        self.photos.select_allow_access_to_photos_popup()
        self.photos.select_photo_by_index()
        self.photos.select_next_button()
        self.common_preview.verify_dynamic_studio_screen(timeout=15)
        if "novelli"  not in self.p.p_obj.projectName:
            self.common_preview.verify_cards_options(invisible=True)
            pytest.skip("Non novelli printer doesn't support Cards function")
        self.common_preview.verify_cards_options(invisible=False)
        self.common_preview.select_ds_cards_btn()
        self.common_preview.verify_cards_screen()
        image_with_front_option = self.common_preview.screenshot_ds_image()
        self.common_preview.select_cards_back_btn()
        image_after_back_option = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_with_front_option, image_after_back_option) > 0.02, "The image should be changed"
        self.common_preview.select_mothers_day_template()
        image_after_mothers_day_template = self.common_preview.screenshot_ds_image()
        self.common_preview.select_ds_paper_btn()
        self.common_preview.select_potrait_orientation_button()
        image_after_paper_orientation_option = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_mothers_day_template, image_after_paper_orientation_option) > 0.02, "The image should be changed"
        self.common_preview.select_ds_cards_btn()
        self.common_preview.select_graduation_template()
        image_after_graduation_template = self.common_preview.screenshot_ds_image()
        self.common_preview.select_ds_paper_btn()
        self.common_preview.verify_paper_photo_tray_selected()
        self.common_preview.select_ds_paper_main_tray_option()
        self.common_preview.verify_paper_main_tray_selected()
        self.common_preview.select_paper_size(size="a4")
        image_after_paper_size_option = self.common_preview.screenshot_ds_image()
        assert saf_misc.img_comp(image_after_graduation_template, image_after_paper_size_option) > 0.02, "The image should be changed"
        self.common_preview.select_ds_paper_photo_tray_option()
        self.common_preview.select_ds_cards_btn()
        self.common_preview.select_graduation_template()
        self.common_preview.select_cards_back_btn()
        self.common_preview.select_mothers_day_template()
        self.common_preview.select_preview_btn()
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)
        self.common_preview.verify_zoom_in_btn()
        self.common_preview.verify_zoom_out_btn()
        image_before_zoom_in = self.common_preview.screenshot_print_preview_image()
        self.common_preview.select_zoom_in_btn()
        self.common_preview.select_zoom_in_btn()
        image_after_zoom_in = self.common_preview.screenshot_print_preview_image()
        assert saf_misc.img_comp(image_before_zoom_in, image_after_zoom_in) > 0.02, "The image should be changed"
        self.common_preview.select_zoom_out_btn()
        self.common_preview.select_zoom_out_btn()
        image_after_zoom_out = self.common_preview.screenshot_print_preview_image()
        assert saf_misc.img_comp(image_after_zoom_out, image_after_zoom_in) > 0.02, "The image should be changed"
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)