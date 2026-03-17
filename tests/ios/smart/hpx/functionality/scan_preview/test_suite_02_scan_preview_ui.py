import pytest
from MobileApps.resources.const.ios import const as i_const
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_02_Scan_Preview_Ui():
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = None
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.fc.hpx = True
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.camera = cls.fc.fd["camera"]
        cls.copy = cls.fc.fd["copy"]
        cls.preview = cls.fc.fd["preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.cpreview = cls.fc.fd["common_preview"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.edit = cls.fc.fd["edit"]

    def test_01_scan_photo(self):
        """
        C44018899
        1.Click on scan tile.
        2.Capture photo and process to preview screen.
        Expected: Verify:
        1. When only one photo is captured, it show "+ Add", "Rotate" buttons on the top of the screen.
        2. When two or more photos are captured, it show "+ Add", "Reorder", "Rotate" buttons on the top of the screen. (The "Text Extract", "Scribble", "Redaction" buttons depend on the account level).
        3. Tap the "..." button on the photo can launch the context menu.
        4. Tap back button on the top navigation bar can show "Do you want to exit scan?" dialog.
                """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.verify_add_page()
        self.preview.verify_rotate_btn()
        self.preview.select_three_dots_icon()
        self.preview.verify_preview_more_options()
        self.preview.select_edit_on_three_dots()
        self.preview.select_cancel_btn_on_edit()
        self.preview.select_add_page()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_add_roatate_reorder_btn()
        self.preview.select_navigate_back()
        self.preview.verify_preview_navigate_back_popup()

    def test_02_exit_scan_yes_start_new_scan(self):
        """
        C44018900: Do you want to exit scan – Yes, start new scan
        Steps:
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "Yes, Start New Scan".
        Verify:
        1. App back to capture scan screen.
        2. Once a new scan job has been captured and go to preview screen, only the new scanned photo is displayed.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_new_scan_btn()
        self.scan.click_close_button_on_scan_screen()
        self.scan.verify_scan_button()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        assert self.preview.verify_pages_option() == False, "only the new scanned photo should be displayed"

    def test_03_exit_scan_yes_exit_scan(self):
        """
        C44018901: Do you want to exit scan – Yes, exit scan
        Steps:
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "Yes, exit scan".
        Verify:
        1. App back to capture scan screen.
        2. Once a new scan job has been captured and go to preview screen, only the new scanned photo is displayed.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_yes_go_home_btn()
        self.home.verify_device_details_page()

    def test_04_exit_scan_no_add_images(self):
        """
        C44018902: Do you want to exit scan – No, add images
        Steps:
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "No, add images".
        Verify:
        1. App back to capture scan screen.
        2. Once a new scan job has been captured and go to preview screen, both previous scan photo and new scan photo should be displayed.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.preview.select_no_add_img_btn()
        self.scan.click_close_button_on_scan_screen()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        assert self.preview.verify_pages_option() == True, "both previous scan photo and new scan photo should be displayed"

    def test_05_exit_scan_cancel(self):
        """
        C44018903: Do you want to exit scan No, add images
        Steps:
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "Cancel".
        Verify:
        1. Once a new scan job has been captured and go to preview screen, App stay on preview screen without any changes.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.preview.click_cancel_on_popup()
        self.preview.verify_preview_screen()

    def test_06_scan_rotate_ui(self):
        """
        C44018904: Rotate UI
        Steps:
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap "Rotate" button on the top of preview screen.
        Verify:
        1. The Rotate UI shows as per design.
        2. When some items are selected, the "x item Selected" message displays on the top of rotate screen; the "Rotate" & "Delete" button displays on bottom of the screen.
        3. When rotate or delete any item, the "Reset" button becomes available.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.select_add_page()
        self.scan.click_close_button_on_scan_screen()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_rotate_btn()
        self.cpreview.select_auto_rotate_image(index=1)
        self.cpreview.verify_is_image_selected()
        self.preview.verify_rotate_screen_tray_options()
        self.preview.select_rotate_btn()
        self.preview.verify_reset_button()

    def test_07_scan_reorder_ui(self):
        """
        C44018905: Reorder UI
        Steps:
        1. Tap scan action tile.
        2. Capture multiple photos and process to preview screen.
        3. Tap the "Reorder" button on the top of preview screen.
        Verify:
        1. The Reorder UI shows as per design.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.select_add_page()
        self.scan.click_close_button_on_scan_screen()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_reorder_btn()
        self.preview.verify_delete_page_icon()

    def test_08_scan_discard_modal_ui(self):
        """
        C44018906: Discard modal UI
        Steps:
        1. Tap scan action tile.
        2. Capture multiple photos and process to preview screen.
        3. Tap the "delete" button on the top of preview screen.
        4. Tap the cancel button on the popup.
        Verify:
        1. The Reorder UI shows as per design.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.select_add_page()
        self.scan.click_close_button_on_scan_screen()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_rotate_btn()
        self.cpreview.select_auto_rotate_image(index=1)
        self.preview.select_rotate_btn()
        self.preview.click_cancel_on_popup()
        self.preview.verify_cancel_btn_popup()

    def test_09_scan_delete_modal_ui(self):
        """
        C44018907: Delete modal UI
        Steps:
        1. Tap scan action tile.
        2. Capture multiple photos and process to preview screen.
        3. Tap the "Reorder" button on the top of preview screen.
        Verify:
        1. The Reorder UI shows as per design.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.select_add_page()
        self.scan.click_close_button_on_scan_screen()
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_rotate_btn()
        self.cpreview.select_auto_rotate_image(index=1)
        self.preview.select_rotate_btn()
        self.preview.select_delete_btn_on_delete()
        self.preview.click_cancel_on_popup()
        self.preview.verify_delete_popup()

    def test_10_edit_screen_and_discard_edits_modal(self):
        """
        Steps: C44018908: Edit UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Make some changes on the screen.
        Verify:
        1. The edit screen shows as per design.
        2. If tap done button, the processing modal can display (depends on the design).
        3. If tap back or cancel button, the "Discard Edits" modal can display.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_crop_btn_on_edit()
        self.preview.select_roate_on_edit()
        self.preview.select_done_button_on_preview()
        self.preview.click_cancel_on_popup()
        self.preview.verify_cancel_btn_popup()

    def test_11_edit_screen_and_verify_crop_screen(self):
        """
        Steps: C44018909: Edit- Crop UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Crop" button.
        Verify:
        The Crop UI as per design
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_crop_btn_on_edit()
        self.edit.verify_screen_title(self.edit.CROP)
        crop_options = self.edit.get_elements_in_collection_view(self.edit.CROP, self.edit.CROP_OPTIONS, "transform")
        assert set(crop_options) == set(self.edit.CROP_OPTIONS)
        self.preview.select_done_button_on_preview()

    def test_12_edit_screen_and_verify_adjust_screen(self):
        """
        Steps: C44018910: Edit- Adjust UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "ADJUST" button.
        Verify:
        The ADJUST UI as per design
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_adjust_btn_on_edit()
        self.edit.verify_screen_title(self.edit.ADJUST)
        adjust_options = self.edit.get_elements_in_collection_view(self.edit.ADJUST, self.edit.ADJUST_OPTIONS, "adjustments")
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_cancel()
        assert set(adjust_options) == set(self.edit.ADJUST_OPTIONS)

    def test_13_edit_screen_and_verify_filter_screen(self):
        """
        Steps: C44018911: Edit- Filter UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Filter" button.
        Verify:
        The Filter UI as per design
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_filters_btn_on_edit()
        self.edit.verify_screen_title(self.edit.FILTERS)
        self.edit.verify_edit_ui_elements(self.edit.FILTER_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        filters_document_options = self.edit.get_elements_in_collection_view(self.edit.FILTER_DOCUMENT, self.edit.FILTER_DOCUMENT_OPTIONS, "filter")
        filters_photo_options = self.edit.get_elements_in_collection_view(self.edit.FILTER_PHOTO, self.edit.FILTER_PHOTO_OPTIONS, "filter")
        self.edit.select_edit_cancel()
        assert set(filters_photo_options) == set(self.edit.FILTER_PHOTO_OPTIONS)
        assert set(filters_document_options) == set(self.edit.FILTER_DOCUMENT_OPTIONS)
        self.edit.select_edit_cancel()

    def test_14_edit_screen_and_verify_text_ui(self):
        """
        Steps: C44018912: Edit- Text UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Text" button.
        Verify:
        The Text UI as per design
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_text_btn_on_edit()
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        self.edit.verify_edit_ui_elements(self.edit.TEXT_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        text_font_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_FONTS, self.edit.TEXT_FONT_OPTIONS, "text")
        self.edit.select_edit_cancel()
        text_color_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_COLOR, self.edit.TEXT_COLOR_OPTIONS, "textColor")
        self.edit.select_edit_cancel()
        text_bg_color_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_BGCOLOR, self.edit.TEXT_BGCOLOR_OPTIONS, "textColor")
        self.edit.select_edit_cancel()
        self.edit.select_edit_main_option(self.edit.TEXT_ALIGNMENT)
        assert self.edit.verify_undo_button_enabled() == 'true'
        assert set(text_font_options) == set(self.edit.TEXT_FONT_OPTIONS)
        assert set(text_color_options) == set(self.edit.TEXT_COLOR_OPTIONS)
        assert set(text_bg_color_options) == set(self.edit.TEXT_BGCOLOR_OPTIONS)

    def test_15_edit_screen_and_verify_markup_screen(self):
        """
        Steps: C44018913: Edit- Markup UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Markup" button.
        Verify:
        The Markup UI as per design
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_markup_btn_on_edit()
        self.edit.verify_screen_title(self.edit.MARKUP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        for color in self.edit.BRUSH_COLORS:
            brush_numb = self.edit.BRUSH_COLOR_FMT[color]
            self.edit.select_brush(brush_numb)

    def test_16_edit_screen_and_verify_auto_screen(self):
        """
        Steps: C44018914: Edit- Auto UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Auto" button.
        Verify:
        The Auto UI as per design
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.driver.scroll("_shared_scan_tile", click_obj=True)
        self.scan.click_close_button_on_scan_screen()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.scan.select_scan_job_button()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_auto_btn_on_edit()
        assert self.edit.verify_undo_button_enabled() == 'true'