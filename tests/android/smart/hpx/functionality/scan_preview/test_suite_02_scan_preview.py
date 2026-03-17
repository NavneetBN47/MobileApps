import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_02_Scan_Preview:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.home = cls.fc.fd[FLOW_NAMES.HOME]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.edit = cls.fc.fd["edit"]
        cls.fc.hpx = True

    def test_01_file_saving_defaults_screen_ui(self):
        """
        C44018898 - Verify File Saving Defaults screen UI from Scan Preview
        Test Steps:
        1.Tap scan action tile.
        2.Capture a photo and process to "Preview" screen.
        expected:Verify:
        1. When only one photo is captured, it show "+ Add", "Rotate" buttons on the top of the screen.
        2. When two or more photos are captured, it show "+ Add", "Reorder", "Rotate" buttons on the top of the screen. (The "Text Extract", "Scribble", "Redaction" buttons depend on the account level).
        3. Tap the "..." button on the photo can launch the context menu.
        4. Tap the "..." button on the top navigation bar can launch "Print Format" option; tap the option can launch print format menu.
        5. Tap back button on the top navigation bar can show "Do you want to exit scan?" dialog.
        6. Text wrapping of buttons and strings is correct on the Preview screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False, create_acc=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.verify_app_page_btn()
        self.print_preview.verify_rotate_page_btn()
        self.print_preview.click_app_page_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.verify_add_rotate_reorder_btn()

    def test_02_exit_scan_and_start_new_scan(self):
        """
        C44018900 - Do you want to exit scan - Yes, start new scan
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "Yes, Start New Scan".
        Expected:
        1. App navigates back to the capture scan screen.
        2. Once a new scan job has been captured and goes to the preview screen, only the new scanned photo is displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.print_preview.verify_exit_screen_dialog()
        self.print_preview.click_start_new_scan_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()

    def test_03_exit_scan_and_exit_scan(self):
        """
        C44018901 - Do you want to exit scan - Yes, exit scan
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "Yes, Exit Scan".
        Expected:Verify:
        App back to root view.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.print_preview.verify_exit_screen_dialog()
        self.print_preview.click_exit_scan_go_home_btn()

    def test_04_exit_scan_and_add_images(self):
        """
        C44018902 - Do you want to exit scan - No, Add Images
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "No, Add Images".
        Expected:Verify:
        1. App back to capture scan screen.
        2. Once a new scan job has been captured and go to preview screen, both previous scanned photo and the new scanned photo are displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.print_preview.verify_exit_screen_dialog()
        self.print_preview.click_no_add_images_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.verify_more_page_numbers_display()

    def test_05_exit_scan_and_cancel(self):
        """
        C44018903 - Do you want to exit scan - cancel
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap back button to show "Do you want to exit scan?" dialog.
        4. Tap "Cancel".
        Expected:
        Verify: App stay on preview screen without any changes.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_navigate_back()
        self.print_preview.verify_exit_screen_dialog()
        self.home.click_cancel_btn()
        self.preview.verify_preview_screen()

    def test_06_scan_preview_rotate_ui(self):
        """
        C44018904 - Rotate UI (Scan Preview)
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the "Rotate" button on the top of preview screen.
        Expected Result:
        1. The Rotate UI shows as per design.
        2. When some items are selected, the "x item Selected" message displays on the top of rotate screen; the "Rotate" & "Delete" button displays on bottom of the screen.
        3. When rotate or delete any item, the "Reset" button becomes available.
        """
        self.preview.verify_preview_screen()
        self.print_preview.click_rotate_page_btn()
        self.print_preview.click_on_image_selected_to_rotate()
        self.print_preview.verify_rotate_delete_btn()
        self.print_preview.click_rotate_page_btn()
        self.print_preview.click_on_delete_btn()
        self.print_preview.click_on_delete_btn()
        self.print_preview.verify_reset_enabled_btn()

    def test_07_reorder_ui(self):
        """
        C44018905 - Reorder UI
        1. Tap scan action tile.
        2. Capture multiple photos and process to preview screen.
        3. Tap the "Reorder" button on the top of preview screen.
        Expected:
        1. The Reorder UI shows as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_app_page_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_reorder_btn()
        self.print_preview.click_on_image_selected_to_rotate()
        self.print_preview.verify_page_option_delete_btn()

    def test_08_discard_modal_ui(self):
        """
        C44018906 - Discard modal UI
        1. Tap scan action tile.
        2. Capture some photos and process to preview screen.
        3. Tap "Reorder" or "Rotate" button.
        4. Make some changes.
        5. Tap back or cancel button. (Android is back and iOS is cancel button)
        Expected:
        Verify: The Discard modal UI shows as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_rotate_page_btn()
        self.print_preview.click_on_image_selected_to_rotate()
        self.print_preview.verify_rotate_delete_btn()
        self.print_preview.click_rotate_page_btn()
        self.preview.select_navigate_back()
        self.print_preview.verify_yes_and_no_btn()

    def test_09_delete_modal_ui(self):
        """
        C44018907 - Delete modal UI
        1. Tap scan action tile.
        2. Capture some photos and process to preview screen.
        3. Tap "Reorder" or "Rotate" button.
        4. Select any item and tap "Delete" button.
        Expected:
        Verify: The Delete modal UI shows as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_rotate_page_btn()
        self.print_preview.click_on_image_selected_to_rotate()
        self.print_preview.verify_rotate_delete_btn()
        self.print_preview.click_rotate_page_btn()
        self.print_preview.click_on_delete_btn()
        self.print_preview.verify_delete_cancel_popup()

    def test_10_edit_ui(self):
        """
        C44018908 - Edit UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Make some changes on the screen.
        Expected:
        1. The edit screen shows as per design.
        2. If tap done button, the processing modal can display (depends on the design).
        3. If tap back or cancel button, the "Discard Edits" modal can display (Android may not have this modal in Figma).
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_crop_btn()
        self.edit.apply_crop_rotate()
        self.edit.select_edit_done()
        self.fc.select_back()
        self.edit.verify_discard_edits_screen()

    def test_11_crop_ui(self):
        """
        C44018909 - Edit - Crop UI
        Steps:
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Crop" button.
        Expected Result:
        Verify: The Crop UI appears as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_crop_btn()
        self.edit.verify_screen_title(self.edit.CROP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.verify_edit_ui_elements(self.edit.CROP_BUTTONS)
        crop_options = self.edit.get_elements_in_collection_view(self.edit.CROP, self.edit.CROP_OPTIONS, "transform")
        assert set(crop_options) == set(self.edit.CROP_OPTIONS)

    def test_12_edit_adjust_ui(self):
        """
        C44018910 - Edit - Adjust UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Adjust" button.
        Expected Result:
        Verify: The Adjust UI appears as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_adjust_btn()
        self.edit.verify_screen_title(self.edit.ADJUST)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        adjust_options = self.edit.get_elements_in_collection_view(self.edit.ADJUST, self.edit.ADJUST_OPTIONS, "adjustments")
        assert set(adjust_options) == set(self.edit.ADJUST_OPTIONS)

    def test_13_filters_ui(self):
        """
        C44018911 - Edit - Filters UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Filters" button.
        Expected Result:
        Verify: The filters UI appears as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.driver.swipe()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_filter_btn()
        self.edit.verify_screen_title(self.edit.FILTERS)
        self.edit.verify_edit_ui_elements(self.edit.FILTER_OPTIONS)
        filters_document_options = self.edit.get_elements_in_collection_view(self.edit.FILTER_DOCUMENT, self.edit.FILTER_DOCUMENT_OPTIONS, "filter")
        filters_photo_options = self.edit.get_elements_in_collection_view(self.edit.FILTER_PHOTO, self.edit.FILTER_PHOTO_OPTIONS, "filter")
        self.edit.select_edit_cancel()
        assert set(filters_photo_options) == set(self.edit.FILTER_PHOTO_OPTIONS)
        assert set(filters_document_options) == set(self.edit.FILTER_DOCUMENT_OPTIONS)

    def test_14_text_ui(self):
        """
        C44018912 - Edit - Text UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Text" button.
        Expected Result:
        1. The "Add Text" screen shows as per design.
        2. If some text is added, the "Text Option" screen shows as per design.
        3. The "Fonts", "Color", "BG Color", "Alignment" buttons can work well.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_text_btn()
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        self.edit.verify_edit_ui_elements(self.edit.TEXT_OPTIONS)
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

    def test_15_markup_ui(self):
        """
        C44018913 - Edit - Markup UI
        1. Tap scan action tile.
        2. Capture a photo and process to preview screen.
        3. Tap the photo to enter Edit screen.
        4. Tap "Markup" button.
        Expected Result:
        Verify: The Markup UI shows as per design.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.click_edit_screen_markup_btn()
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        for color in self.edit.BRUSH_COLORS:
            brush_numb = self.edit.BRUSH_COLOR_FMT[color]
            self.edit.select_brush(brush_numb)