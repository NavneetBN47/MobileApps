from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "SMART"


class Test_Suite_07_Preview_Auto_Orientation(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.cpreview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        cls.auto_orient_state = None
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_auto_orientation_end_to_end(self):
        """
        Description: C31299365, C31299366, C31299369, C31299384, C31299370, C31299372, C31299377, C31299385
         1. Load HP Smart app and Sign in to HPID
         2. Select Camera Scan on bottom navbar
         3. Select Document Mode
         4. Toggle auto-orientation off
         5. Load upright text image 3 times
          - Select gallery option
          - Select upright text image(first image in Downloads)
          - Select next on adjust screen
          - if another image is needed select add
         6. Select Rotate button(on preview screen)
         7. Select first image
         8. Deselect selected image
         9. Select second image
         10. Select delete
         11. Select Done
        Expected Results:
         6. Verify rotate screen
         8. Verify tray disappeared
         11. Verify page count is now 2
        """
        self.__load_images(image_count=3, load_rotate=False)
        self.cpreview.swipe_to_page(1)
        self.cpreview.select_top_toolbar_btn(self.cpreview.ROTATE_BTN)
        self.cpreview.verify_title(self.cpreview.ROTATE_TITLE)
        self.cpreview.verify_auto_rotate_screen()
        self.cpreview.select_auto_rotate_image(1)
        self.cpreview.select_auto_rotate_image(1, select=False)
        self.cpreview.verify_auto_rotate_screen()
        self.cpreview.select_auto_rotate_image(2)
        self.cpreview.select_auto_rotate_option("delete")
        self.cpreview.select_auto_rotate_done_button()
        assert self.cpreview.verify_preview_page_info()[1] == 2, "Page count should be 2"

    def test_02_reset_button(self):
        """
        Description:  C31299373, C31299374, C31299375
         1. Load HP Smart app and Sign in to HPID
         2. Select Camera Scan on bottom navbar
         3. Select Document mode
         4. Toggle auto-orientation off
         5. Load upright text image 2 times
          - Select gallery option
          - Select upright-text image(first image in Downloads)
          - Select next on adjust screen
          - if another image is needed select add
         6. Select Rotate button(on preview screen)
         7. Select first image
         8. Select Rotate button
         9. Deselect first image
         10. Select second image
         11. Select delete button
         12. Select reset button
        Expected Results:
         9. Verify image 1 changed
          Verify reset button is active
         11. Verify number of image is 1
         12. Verify image 1 matches original image 1
          Verify number of images is 2
          Verify reset button is inactive
        """
        self.__load_images(image_count=2)
        init_img = self.cpreview.verify_auto_rotate_image(1)
        self.cpreview.select_auto_rotate_image(1)
        self.cpreview.select_auto_rotate_option("rotate")
        self.cpreview.select_auto_rotate_image(1, select=False)
        time.sleep(1)  # allow check mark to disappear before screenshot
        self.cpreview.verify_auto_rotate_reset_btn(active=True)
        assert saf_misc.img_comp(self.cpreview.verify_auto_rotate_image(1), init_img) != 0.00, "Expected image 1 to change"
        self.cpreview.select_auto_rotate_image(2)
        self.cpreview.select_auto_rotate_option("delete")
        time.sleep(1)  # allow deletion to complete
        self.cpreview.verify_auto_rotate_image_count(1)
        self.cpreview.select_auto_rotate_reset_button()
        time.sleep(3)  # allow reset to complete
        self.cpreview.verify_auto_rotate_reset_btn(active=False)
        self.cpreview.verify_auto_rotate_image_count(2)
        assert saf_misc.img_comp(self.cpreview.verify_auto_rotate_image(1), init_img) < 0.06, "Expected image 1 to match original"

    @pytest.mark.parametrize("auto_orient", [True, False])
    def test_03_auto_orientation_behavior(self, auto_orient):
        """
        Description: C31299383, C31299367
         1. Load HP Smart app and Sign in to HPID
         2. Select Camera Scan on bottom navbar
         3. Select Document mode
         4. Toggle auto-orientation on or off depending on auto_orient param
         5. Load inverted text image 2 times
          - Select gallery option
          - Select inverted text image(second image in Downloads)
          - Select next on adjust screen
          - if another image is needed select add
         6. Select Rotate button(on preview screen)
        Expected Results:
         6. Verify rotate screen with Reset button is inactive
        """
        self.__load_images(auto_orientation=auto_orient, image_count=2)
        self.cpreview.verify_auto_rotate_screen()
        time.sleep(10)  # wait for rotation to complete
        self.cpreview.verify_auto_rotate_reset_btn(active=False)

    @pytest.mark.parametrize("screen,btn", [("rotate", "yes"), ("rotate", "no"), ("reorder", "yes"), ("reorder", "no")])
    def test_04_discard_changes_popup(self, screen, btn):
        """
        Description: C31299368, C31299379, C31299380, C31299381, C31299382, C31299237, C31297724, C31297725
         1. Load HP Smart app and Sign in to HPID
         2. Select Camera Scan on bottom navbar
         3. Select Document mode
         4. Toggle auto-orientation off
         5. Load upright text image 2 times
          - Select gallery option
          - Select upright text image(second image in Downloads)
          - Select next on adjust screen
          - if another image is needed select add
         6. Select Rotate or Reorder button based on screen param
         7. Reorder an image or Rotate an image depending on screen
         8. Tap on Back(<-) button
         9. Select yes or no based on btn param
        Expected Result:
         8. Verify Discard Changes popup
         9. If btn == "yes"
             Verify preview screen
             Verify Images did not change
            If btn == "no"
             Verify screen based on screen param
        """
        self.__load_images(image_count=2, load_rotate=False)
        if btn == "yes":  # capture images to verify they dont change after discarding changes
            init_imgs = self.cpreview.screenshot_all_preview_images()
        if screen == "rotate":
            self.cpreview.select_top_toolbar_btn(self.cpreview.ROTATE_BTN)
            self.cpreview.verify_auto_rotate_screen()
            self.cpreview.select_auto_rotate_image(2)
            time.sleep(4)
            self.cpreview.select_auto_rotate_option("rotate")
        else:
            self.cpreview.select_top_toolbar_btn(self.cpreview.REORDER_BTN)
            self.cpreview.reorder_image(1, 2)
        self.fc.select_back()
        if screen == "rotate":
            self.cpreview.select_auto_rotate_discard_option(btn)
        else:
            self.cpreview.select_reorder_discard_option(btn)
        if btn == "yes":
            self.cpreview.verify_preview_screen()
            for i in range(2):
                self.cpreview.swipe_to_page(i + 1)
                assert saf_misc.img_comp(self.cpreview.verify_preview_img(), init_imgs[i]) < 0.06, "Expected image {} to be unchanged".format(i + 1)
        else:
            if screen == "rotate":
                self.cpreview.verify_auto_rotate_screen(image_selected=True)
            else:
                self.cpreview.verify_reorder_screen()

    def test_05_rotate_multiple_images(self):
        """
        Description: C31299371
         1. Load HP Smart app and Sign in to HPID
         2. Select Camera Scan on bottom navbar
         3. Select Document mode
         4. Toggle auto-orientation off
         5. Load upright text image 3 times
          - Select gallery option
          - Select upright text image(first image in Downloads)
          - Select next on adjust screen
          - if another image is needed select add
         6. Select Rotate button(on preview screen)
         7. Select all images
         8. Select Rotate
         9. Deselect all images
        Expected Results:
         9. Verify all images changed
        """
        self.__load_images(image_count=3)
        capture_images = lambda count: [self.cpreview.verify_auto_rotate_image(i + 1) for i in range(count)]
        init_imgs = capture_images(3)
        for i in range(3):
            self.cpreview.select_auto_rotate_image(i + 1)
        self.cpreview.select_auto_rotate_option("rotate")
        for i in range(3):
            self.cpreview.select_auto_rotate_image(i + 1, select=False)
        time.sleep(3)
        end_imgs = capture_images(3)
        for i in range(3):
            assert saf_misc.img_comp(init_imgs[i], end_imgs[i]) != 0.00, "Image {} should have changed".format(i + 1)

    def test_06_exit_without_rotation(self):
        """
        Description: C31299376
         1. Load HP Smart app and Sign in to HPID
         2. Select Camera Scan on bottom navbar
         3. Select Document mode
         4. Toggle auto-orientation off
         5. Capture an image
         6. Select Next button
         7. Select Rotate button(on preview screen)
         8. Select Back(<-) button

         9. Select Rotate button(on preview screen)
         10. Select the image
         11. Swipe the slide bar down

        Expected Results:
         7. Verify rotate screen
         8. Verify preview screen
         10. Verify Rotate screen with slide bar
          Verify "1 Item Selected" title
         11. Verify Rotate slide bar is hidden
          Verify "Rotate" title
        """
        self.__load_images()
        self.cpreview.verify_auto_rotate_screen()
        self.fc.select_back()
        if self.cpreview.verify_discard_changes_popup(raise_e=False):
            self.cpreview.select_auto_rotate_discard_option("yes")
        self.cpreview.verify_preview_screen()
        self.cpreview.select_top_toolbar_btn(self.cpreview.ROTATE_BTN)
        self.cpreview.select_auto_rotate_image(1)
        self.cpreview.verify_auto_rotate_screen(image_selected=True)
        self.cpreview.select_auto_rotate_image(1, select=False)
        self.cpreview.verify_auto_rotate_screen(image_selected=False)

    def __load_images(self, auto_orientation=False, image_count=1, load_rotate=True):
        """
        Loads the Smart app, opens camera scan, toggles auto_orientation and loads images. Ends at rotate screen if load_rotate == True else ends at preview screen
        :param image: The image to load. Possible values: "scan", "inverted_text", "upright_text"
        :param auto_orientation: Toggle auto-orientation on if True else toggle it off
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(verify_signin=False)
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.scan.dismiss_coachmark(screen="scanner")
        self.scan.select_enhancements_btn()
        if self.auto_orient_state != auto_orientation:
            self.scan.toggle_enhancement("auto_orientation", enable=auto_orientation)
            self.auto_orient_state = auto_orientation
        self.fc.select_back()
        for i in range(image_count):
            self.fc.flow_scan_capture(self.scan.SOURCE_PRINTER_SCAN_OPT, mode="document")
            self.scan.select_adjust_next_btn(timeout=20)
            if i < image_count - 1:
                self.cpreview.select_top_toolbar_btn(self.cpreview.ADD_BTN)
        self.cpreview.verify_preview_screen()
        assert self.cpreview.verify_preview_page_info()[1] == image_count, f"Page count should be {image_count}"
        if load_rotate:
            self.cpreview.select_top_toolbar_btn(self.cpreview.ROTATE_BTN)
