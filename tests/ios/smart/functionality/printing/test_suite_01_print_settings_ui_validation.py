import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from time import sleep

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_01_Print_Settings_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        # Define flows
        cls.common_preview = cls.fc.fd["common_preview"]

        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(printer_ip=cls.p.get_printer_information()["ip address"])

    def test_01_verify_print_preview_ui(self):
        """
        Verifies print preview ui elements - C25341390
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.common_preview.go_to_print_preview_pan_view(pan_view=False)
        self.common_preview.verify_print_preview_ui_elements(self.p.get_printer_information()["bonjour name"])

    def test_02_verify_transform_resize_move_function(self):
        """
        Description:  C31297367, C31297369, C31297368, C31297370, C31297371, C31297372, C31297374, C33516190
         1. Load Home screen
         2. Connect to target printer
         3. Click on View & Print folder
         4. Click on Albums -> Recents -> Select a photo from Recents folder
         5. Click on Print Preview button
         6. Click on Image icon
         7. Click on Resize & Move button
         8. Click on Cancel button
         9. click on Resize & Move button -> Origin Size button
         10. Click on Done button
         11. Click on Done button
         12. Click on Image icon
         13. Click on Resize & Move button
         14. Click on Fit to Page option
         15. Click on Done button
         16. Click on Done button
         17. Click on Image icon
         18. Click on Resize & Move button
         19. Click on Fill Page option
         20. Click on Done button
         21. Click on Done button
         22. Click on Print button

         Expected Results:
         5. Verify "Select to transform" message shows
         6. Verify Transform screen
         7. Verify Resize & Move screen
         8. Verify App goes back to Transform screen
         10. Verify the picture size change success on Print Preview screen
         11.Verify the picture size change success on Print Preview screen
         14.Verify the picture size change success on Print Preview screen
         15.Verify the picture size change success on Print Preview screen
         21.Verify the picture size change success on Print Preview screen
         22.Printing job is success
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.navigate_to_transform_screen()
        self.common_preview.verify_transform_screen()
        self.common_preview.verify_array_of_elements([self.common_preview.PREVIEW_IMAGE, self.common_preview.CANCEL_BUTTON, self.common_preview.DONE_BUTTON])
        transform_img_before_edit = self.common_preview.verify_preview_img()
        self.common_preview.select_resize_move_btn()
        self.common_preview.verify_resize_move_screen()
        self.common_preview.select_cancel()
        self.common_preview.verify_transform_screen()
        self.common_preview.select_resize_move_btn()
        self.common_preview.select_resize_move_original_size_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_resize_edit = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_resize_edit) > 0
        self.common_preview.select_transform_options(self.common_preview.PREVIEW_IMAGE)
        self.common_preview.select_resize_move_btn()
        self.common_preview.select_resize_move_fit_to_page_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_resize_with_fit_to_page_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(image_after_resize_edit, image_after_resize_with_fit_to_page_option) > 0
        self.common_preview.select_transform_options(self.common_preview.PREVIEW_IMAGE)
        self.common_preview.select_resize_move_btn()
        self.common_preview.select_resize_move_fill_page_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_resize_with_fill_page_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(image_after_resize_with_fit_to_page_option, image_after_resize_with_fill_page_option) > 0
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_resize_move_manual_function(self):
        """
        Description:  C31297373
         1. Load Home screen
         2. Connect to target printer
         3. Click on View & Print folder
         4. Click on Albums -> Recents -> Select a photo from Recents folder
         5. Click on Print Preview button
         6. Click on Image icon
         7. Click on Resize & Move button
         8. Click on Manual option
         9. Click on Done button
         10. Click on Done button
         11. Click on Print button

         Expected Results:
         10.Verify the picture size change success on Print Preview screen
         11. Printing job is success
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.navigate_to_transform_screen()
        self.common_preview.verify_transform_screen()
        transform_img_before_edit = self.common_preview.verify_preview_img()
        self.common_preview.select_resize_move_btn()
        self.common_preview.select_resize_move_manual_option()
        img_before_manual_resize = self.common_preview.verify_preview_img()
        self.common_preview.manual_resize_image()
        sleep(1)
        img_after_manual_resize_left = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(img_before_manual_resize, img_after_manual_resize_left) > 0
        self.common_preview.manual_resize_image(direction="right", per_offset=0.45)
        sleep(1)
        img_after_manual_resize_right = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(img_after_manual_resize_left, img_after_manual_resize_right) > 0
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_manual_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_manual_option) > 0
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_transform_rotate_function(self):
        """
        Description:  C31297375, C31297376, C31297377, C31297378, C31297379, C31297380
         1. Load Home screen
         2. Connect to target printer
         3. Click on View & Print folder
         4. Click on Albums -> Recents -> Select a photo from Recents folder
         5. Click on Print Preview button
         6. Click on Image icon
         7. Click on Rotate button
         8. Click on Left option
         9. Click on Cancel button
         10. Click on Rotate button
         11. Click on Right option
         12. Click on Done button
         13. Click on Done button
         14. Click on Rotate button
         15. Click on Left option
         16. Click on Done button
         17. Click on Done button
         18. Click on Rotate button
         19. Click on Flip H option
         20. Click on Done button
         21. Click on Done button
         22. Click on Rotate button
         23. Click on Flip V option
         24. Click on Done button
         25. Click on Done button
         26. Click on Print button

         Expected Results:
         7. Verify Rotate screen
         9. Verify Transform screen
         13. Verify the image is rotated success
         17. Verify the image is rotated success
         21. Verify the image is rotated success
         25. Verify the image is rotated success
         26. Verify the print job is success
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.navigate_to_transform_screen()
        self.common_preview.verify_transform_screen()
        transform_img_before_edit = self.common_preview.verify_preview_img()
        self.common_preview.select_rotate_btn()
        self.common_preview.verify_rotate_screen()
        self.common_preview.select_rotate_left_option()
        self.common_preview.select_cancel()
        self.common_preview.verify_transform_screen()
        image_after_rotate_cancel_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_rotate_cancel_option) == 0
        self.common_preview.select_rotate_btn()
        self.common_preview.select_rotate_left_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_rotate_left_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_rotate_left_option) > 0
        self.common_preview.select_transform_options(self.common_preview.PREVIEW_IMAGE)
        self.common_preview.select_rotate_btn()
        self.common_preview.select_rotate_right_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_rotate_right_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(image_after_rotate_left_option, image_after_rotate_right_option) > 0
        self.common_preview.select_transform_options(self.common_preview.PREVIEW_IMAGE)
        self.common_preview.select_rotate_btn()
        self.common_preview.select_rotate_flip_h_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_rotate_flip_h_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(image_after_rotate_right_option, image_after_rotate_flip_h_option) > 0
        self.common_preview.select_transform_options(self.common_preview.PREVIEW_IMAGE)
        self.common_preview.select_rotate_btn()
        self.common_preview.select_rotate_flip_v_option()
        self.common_preview.select_done()
        self.common_preview.select_done()
        image_after_rotate_flip_v_option = self.common_preview.verify_preview_img()
        assert saf_misc.img_comp(image_after_rotate_flip_h_option, image_after_rotate_flip_v_option) > 0
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_05_verify_reorder_screen_ui(self):
        """
        Description:  C31297381, C31297383
        1. Load Home screen
        2. Connect to target printer
        3. Click on View & Print folder
        4. Click on Albums -> Recents -> Select 2 photos from Recents folder
        5. Click on Print Preview button
        6. Click on Reorder button
        7. Click on Cancel button
        8. Click on Reorder button

        Expected Results:
        6. Verify Reorder screen
        7. Verify Preview screen
        8. Verify Reorder screen
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=2)
        self.common_preview.verify_an_element_and_click(self.common_preview.REORDER_TITLE)
        self.common_preview.verify_title(self.common_preview.REORDER_TITLE)
        self.common_preview.verify_array_of_elements([self.common_preview.CANCEL_BUTTON, self.common_preview.DONE_BUTTON])
        self.common_preview.select_cancel()
        self.common_preview.verify_preview_screen()
        self.common_preview.verify_an_element_and_click(self.common_preview.REORDER_TITLE)
        pages = self.common_preview.get_print_page_collection_view_cell()
        while '' in pages:
            pages.remove('')
        assert pages == ['1', '2']
        assert len(self.common_preview.verify_delete_page_x_icon()) == 2