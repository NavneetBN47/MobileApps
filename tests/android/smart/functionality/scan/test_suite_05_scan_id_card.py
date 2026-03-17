from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
import pytest

pytest.app_info = "SMART"


class Test_Suite_05_Scan_ID_Card(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

        cls.source_map = {
            "scanner": {
                "front_msg": "id_front_scanner",
                "back_msg": "id_back_scanner",
                "change_checks": cls.scan.ID_CARD_CHANGE_CHECK,
                "source_const": cls.scan.SOURCE_PRINTER_SCAN_OPT,
                "navigation_button": cls.home.NAV_PRINTER_SCAN_BTN
            },
            "camera": {
                "front_msg": "id_front",
                "back_msg": "id_back",
                "change_checks": cls.scan.ID_CARD_CAMERA_CHANGE_CHECK,
                "source_const": cls.scan.SOURCE_CAMERA_OPT,
                "navigation_button": cls.home.NAV_CAMERA_SCAN_BTN
            }
        }
    
    @pytest.mark.parametrize("source", ["scanner", "camera"])
    def test_01_capture_id_card(self, source):
        """
        Description: C31299304, C31299305, C31299302, C31299308, C31299309, C31299306, C31299320 & C31299319, C31299314 & C31299313, C31298999
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan or Printer Scan
          - If printer scan make sure printer is loaded
         3. Select ID Card Mode
         4. Select shutter button to capture ID Front
         5. Select shutter button to capture ID Back
         6. Select Next
         7. Select Next
        Expected Results:
         3. Verify ID Front bubble message
         4. Verify D Back bubble message
         5. Verify ID Front Preview screen
          - "ID Card Front" title text
          - Page options(...) button
          - Rotate image button
          - Next button
         6. Verify ID Back Preview screen
          - "ID Card Back" title text
          - Page options(...) button
          - Rotate image button
          - Next button
         7. Verify Preview screen
        """
        source_info = self.source_map[source]
        self.__load_id_capture(source)
        self.scan.verify_bubble_msg(source_info["front_msg"])
        self.scan.start_capture(change_check=source_info["change_checks"][0])
        self.scan.verify_bubble_msg(source_info["back_msg"])
        self.scan.start_capture(change_check=source_info["change_checks"][1])
        self.scan.verify_id_preview_screen("front")
        self.scan.select_id_next_btn()
        self.scan.verify_id_preview_screen("back")
        self.scan.select_id_next_btn()
        self.preview.verify_preview_screen()

    @pytest.mark.parametrize("source", ["camera", "scanner"])
    def test_02_cancel_id_capture(self, source):
        """
        Description: C31299307, C29519831, C31299303, C29519834, C31299322, C31299321
         1. Open Smart app and Sign in with HP+
         2. Select Printer Scan or Camera Scan
         3. Select ID Card Mode
         4. If "cancel_at" == "no_capture" then select x button else continue to next step
         5. Select shutter button to capture ID front
         6. If "cancel_at" == "front" then select back button else continue to next step
         7. Select shutter button to capture ID back
         8. Click back button

        Expected Results:
         4. if cancel_at == "no_capture" Verify "Place the front of..." message
         6. if cancel_at == "front" Verify Home screen
         8. Verify ID Front bubble message
        """
        source_info = self.source_map[source]
        self.__load_id_capture(source)
        self.scan.verify_bubble_msg(source_info["front_msg"])
        self.scan.select_exit_btn()
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(source_info["navigation_button"])
        self.scan.start_capture(change_check=source_info["change_checks"][0])
        self.scan.verify_bubble_msg(message=source_info["back_msg"])
        self.scan.select_exit_btn()
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(source_info["navigation_button"])
        self.scan.start_capture(change_check=source_info["change_checks"][0])
        self.scan.verify_bubble_msg(message=source_info["back_msg"])
        self.scan.start_capture(change_check=source_info["change_checks"][1])
        self.fc.select_back()
        self.scan.verify_bubble_msg(message=source_info["front_msg"])

    def test_03_id_card_from_file(self):
        """
        Description: C31299323 & C31299324
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan on bottom navbar
         3. Select ID Card Mode
         4. Select Gallery button
         5. Select an image
         6. Select Gallery button
         7. Select an image
         8. Select Next button
         9. Select Next button
        Expected Results:
         5. Verify ID Back message
         7. Verify ID Card Front preview screen
         8. Verify ID Card Back preview screen
         9. Verify preview screen
        """
        self.__load_id_capture(source="camera")
        self.scan.select_source(self.scan.SOURCE_FILES_PHOTOS)
        self.local_photos.select_recent_photo_by_index()
        self.scan.verify_bubble_msg(message="id_back")
        self.scan.select_source(self.scan.SOURCE_FILES_PHOTOS)
        self.local_photos.select_recent_photo_by_index()
        self.scan.verify_id_preview_screen("front")
        self.scan.select_id_next_btn()
        self.scan.verify_id_preview_screen("back")
        self.scan.select_id_next_btn()
        self.preview.verify_preview_screen()

    @pytest.mark.parametrize("to_replace", ["front", "back"])
    def test_04_replace_id_capture(self, to_replace):
        """
        Description: C31299317 & C31299318
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan on bottom navbar
         3. Select ID Card Mode
         4. Select shutter button to capture ID Front
         5. Select shutter button to capture ID Back
         6. If "to_replace" == "back" Select Next button
         7. Select Page Options(...) button
         8. Select Replace
        Expected Results:
         8. Verify bubble message
          - "to_replace" == "front" verify ID Front message
          - "to_replace" == "back" verify ID Back message
        """
        self.__load_id_capture(source="camera", capture=True)
        if to_replace == "back":
            self.scan.select_id_next_btn()
        self.scan.select_id_page_options_btn("replace")
        self.scan.verify_bubble_msg("id_" + to_replace)

    @pytest.mark.parametrize("id_source", ["camera", "gallery"])
    def test_05_replace_id_capture_with_extra_images(self, id_source):
        """
        Description: C29685807 & C31299312, C31299331, C31299332, C31299333
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan or Printer Scan on bottom navbar
          - If printer scan make sure printer is loaded
         3. if id_position == "middle" or "end"
          a. Select Document mode
          b. Select Capture button
          c. Select Next button
          d. Select Add button
         4. Select ID Card Mode
         5. if id_source == "camera" Capture ID front and back
            if id_source == "gallery" Select gallery button and pick an image twice
         6. Select next button
         7. Select next button
         8. if id_position == "middle"
          a. Select add button
          b. Select Document mode
          c. Select Capture button
          d. Select Next button
         9. Swipe to ID image
         10. Select replace on Page options menu
         11. if id_source == "camera" Capture ID front and back
             if id_source == "gallery" Select gallery button and pick an image twice
         12. Select next button
         13. Select next button
        Expected Results:
         8. Verify number of pages matches expectation
          - 2 pages for start and end id_position
          - 3 pages for middle id_position
         10. Verify ID Front message
         13. Verify number of pages matches expectation
          - 2 pages for start and end id_position
          - 3 pages for middle id_position
        """
        self.fc.reset_app()
        page_count = 1
        if id_source == "gallery":
            self.fc.flow_home_scan_single_page(self.p, from_tile=False, mode="document")
            self.scan.select_adjust_next_btn()
        else:
            self.fc.flow_load_home_screen()
            self.fc.flow_home_camera_scan_pages(from_tile=False)
        self.preview.verify_preview_screen()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        page_count += 1
        self.__capture_id(id_source)
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        if id_source == "gallery":
            self.fc.flow_scan_capture(self.scan.SOURCE_PRINTER_SCAN_OPT, mode="document")
            self.scan.select_adjust_next_btn()
        else:
            self.__capture_id(id_source)
        page_count += 1
        assert self.preview.verify_preview_page_info()[1] == page_count, f"Page count should be {page_count}"
        self.preview.verify_preview_screen()
        self.preview.swipe_to_page(3)
        self.preview.select_page_options_btn(self.preview.REPLACE_BTN)
        self.__capture_id(id_source, is_replace=True)
        assert self.preview.verify_preview_page_info()[1] == page_count, f"Page count should be {page_count}"

    def test_06_replace_reordered_id_capture(self):
        """
        Description: C31299334
         1. Open Smart app and Sign in with HP+
         2. Load Scan screen
         3. Capture Two Documents
         4. Select Add button
         5. Select ID Card Mode
         6. Capture ID Front and Back
         7. Select Next button
         8. Select Next button
         9. Select Reorder on ID Card page
         10. Move ID Card to first position
         11. Select Done button
        Expected Results:
         11. Verify Page count is 3
        """
        self.fc.flow_home_load_scan_screen(self.p)
        self.fc.flow_scan_capture(self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.select_adjust_next_btn()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.fc.flow_scan_capture(self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.select_adjust_next_btn()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.__capture_id("scanner")
        self.preview.select_top_toolbar_btn(self.preview.REORDER_BTN)
        self.preview.reorder_image(3, 1)
        self.preview.select_reorder_done()
        self.preview.verify_preview_screen()
        assert self.preview.verify_preview_page_info()[1] == 3, f"Page count should be 3"

    def test_07_rotate_id_card_back(self):
        """
        Description: C31299316
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan on bottom navbar
         3. Select ID Card Mode
         4. Select shutter button to capture ID Front
         5. Select shutter button to capture ID Back
         6. Select next button
         7. Select rotate button
        Expected Results:
         7. Verify 180 degree rotation
          - image dimensions are the same
          - image content changed
        """
        self.__load_id_capture(source="camera", capture=True)
        self.scan.select_id_next_btn()
        self.scan.verify_id_preview_screen("back")
        init_img = saf_misc.load_image_from_base64(self.scan.capture_id_preview_img())
        self.scan.select_id_rotate_btn(verify=False)
        rotated_img = saf_misc.load_image_from_base64(self.scan.capture_id_preview_img())
        assert saf_misc.img_comp(init_img, rotated_img) > 0.06, "Initial image and rotated image should not match"

    @pytest.mark.parametrize("degrees", [90,  180])
    def test_08_rotate_id_card_in_sync(self, degrees):
        """
        Description: C31299315, C31299310 & C31299311
         1. Open Smart app and Sign in with HP+
         2. Select Camera Scan on bottom navbar
         3. Select ID Card Mode
         4. Select shutter button to capture ID Front
         5. Select shutter button to capture ID Back
          - capture id front preview image for verification
         6. Select Next Button
          - capture id back preview image for verification
         7. Press back button
         8. Select rotate button, click again if rotation == 180
         9. Select Next Button
        Expected Results:
         8. Verify rotate and page options button disappear and reappear
         9. Verify front and back preview image dimensions
          - if rotation == 180 dimensions should have not changed
          - if rotation == 90 dimensions should have changed
          Verify front and back preview images changed
        """
        self.__load_id_capture(source="camera", capture=True)
        init_front_img = saf_misc.load_image_from_base64(self.scan.capture_id_preview_img())
        self.scan.select_id_next_btn()
        init_back_img = saf_misc.load_image_from_base64(self.scan.capture_id_preview_img())
        self.fc.select_back()
        self.scan.select_id_rotate_btn(verify=False)
        if degrees == 180:
            self.scan.select_id_rotate_btn(verify=False)
        rotated_front_img = saf_misc.load_image_from_base64(self.scan.capture_id_preview_img())
        self.scan.select_id_next_btn()
        rotated_back_img = saf_misc.load_image_from_base64(self.scan.capture_id_preview_img())
        assert saf_misc.img_comp(init_front_img, rotated_front_img) > 0.06, "Init front and rotated front image should not match"
        assert saf_misc.img_comp(init_back_img, rotated_back_img) > 0.06, "Init back and rotated back image should not match"

    def __load_id_capture(self, source="camera", capture=False):
        """
        Load ID Card Capture screen
        :param source: Capture source. "camera" or "scanner"
        """
        if source == "scanner":
            self.fc.flow_home_load_scan_screen(self.p, from_tile=False)
        elif source == "camera":
            self.fc.reset_app()
            self.fc.flow_load_home_screen()
            self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
            if self.fc.flow_grant_camera_scan_permissions():
                self.scan.dismiss_coachmark()
        else:
            raise ValueError('source must be "camera" or "scanner"')
        if capture:
            self.__capture_id(source, to_preview=False)
        else:
            self.scan.select_capture_mode("id_card")

    def __capture_id(self, source, to_preview=True, is_replace=False):
        """
        Captures an ID Card from the scan/camera scan screen
        :param source: The capture source to use. "camera", "scanner" or "gallery".
        :param to_preview: End at preview screen.
        :param is_replace: Is replacement capture screen, scan modes recycler is invisible.
        """
        if not is_replace:
            self.scan.select_capture_mode("id_card")
        source_info = self.source_map.get(source, self.source_map["scanner"])
        if source == "gallery":
            self.scan.select_source(self.scan.SOURCE_PRINTER_SCAN_OPT)
            self.scan.select_source(self.scan.SOURCE_FILES_PHOTOS)
            self.local_photos.select_recent_photo_by_index()
            self.scan.select_adjust_next_btn(change_check=None, raise_e=False)
            self.scan.select_source(self.scan.SOURCE_FILES_PHOTOS)
            self.local_photos.select_recent_photo_by_index()
        elif source in ["camera", "scanner"]:
            self.scan.start_capture(change_check=source_info["change_checks"][0])
            self.scan.start_capture(change_check=source_info["change_checks"][1])
        else:
            raise ValueError('Source must be "scanner", "camera" or "gallery"')
        self.scan.verify_id_preview_screen("front")
        if to_preview:
            self.scan.select_id_next_btn()
            self.scan.verify_id_preview_screen("back")
            self.scan.select_id_next_btn()
            self.preview.verify_preview_screen()