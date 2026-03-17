import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_01_Camera_Scan(object):

    @pytest.fixture(scope="class", autouse= True)
    def class_setup(cls, request, android_hpx_flow_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_hpx_flow_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_fle_marks_camera_scan(self):
        """
        Description: C44018870
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
        Expected Result:
            Check the FLE marks one by one.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        # Verifying the 1st coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Adjust scan settings and auto enhancements.', f"Expected 'Adjust scan settings and auto enhancements.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '1 of 4', f"Expected '1 of 4' but got {self.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 2nd coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Select the preset you would like to use.', f"Expected 'Select the preset you would like to use.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '2 of 4', f"Expected '2 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 3rd coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Tap here to capture a camera scan.', f"Expected 'Tap here to capture a camera scan.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '3 of 4', f"Expected '3 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        self.camera_scan.click_coarchmark_next_btn()
        # Verifying the 4th coachmark
        assert self.camera_scan.get_coarchmark_titles() == 'Tap to change the source of your scan.', f"Expected 'Tap to change the source of your scan.' but got {self.camera_scan.get_coarchmark_titles()}"
        assert self.camera_scan.get_coarchmark_status() == '4 of 4', f"Expected '4 of 4' but got {self.camera_scan.get_coarchmark_status()}"
        # Verifying the backward Navigations of coachmark
        for _ in range(3):
            self.camera_scan.click_coarchmark_back_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.driver.back()
        self.hpx_printer_details.click_camera_scan_tile()
        self.camera_scan.verify_camera_scan_capture_mode()

    def test_02_camera_scan_auto_features(self):
        """
        Description: C44018873
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
        Expected Result:
            Check "Auto" option on camera scan screen for 'Document', 'Photo', Batch'.
        """
        assert not self.camera_scan.verify_auto_is_selected(), f"Expected 'Auto' to be not selected but got {self.camera_scan.verify_auto_is_selected()}"
        self.camera_scan.click_photo_mode_btn()
        assert not self.camera_scan.verify_auto_is_selected(), f"Expected 'Auto' to be not selected but got {self.camera_scan.verify_auto_is_selected()}"
        self.camera_scan.click_batch_mode_btn()
        assert not self.camera_scan.verify_auto_is_selected(), f"Expected 'Auto' to be not selected but got {self.camera_scan.verify_auto_is_selected()}"

    def test_03_camera_scan_with_document_preset(self):
        """
        Description: C44018885
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
            Select 'Document' preset.
            Capture a photo and go to preview screen.
        Expected Result:
            The "Auto" option is off by default.
        """
        self.camera_scan.document_mode_btn()
        assert not self.camera_scan.verify_auto_is_selected(), f"Expected 'Auto' to be not selected but got {self.camera_scan.verify_auto_is_selected()}"
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()

    def test_04_camera_scan_with_photo_preset(self):
        """
        Description: C44018886
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
            Select 'Photo' preset.
            Capture a photo and go to preview screen.
        Expected Result:
            The "Auto" option is off by default.
            Verify the preview screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_photo_mode_btn()
        self.camera_scan.click_shutter()
        assert not self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.verify_print_preview_screen()

    def test_05_camera_scan_with_batch_reset(self):
        """
        Description: C44018887
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
            Select 'Batch' preset.
            Capture a photo and go to preview screen.
        Expected Result:
            The "Auto" option is off by default.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_batch_mode_btn()
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.verify_print_preview_screen()

    def test_06_verify_camera_scan_landing_page_ui(self):
        """
        Description: C44018865
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
            Observe the camera scan screen UI
            Tap on source button
        Expected Result:
            verify "Camera" is selected default
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        assert self.camera_scan.get_capture_mode_text() == "Auto", f"Expected 'Auto' but got {self.camera_scan.get_capture_mode_text()}"
        assert self.camera_scan.get_camera_scan_flash_mode() == "Flash Off", f"Expected 'Flash Off' but got {self.camera_scan.get_camera_scan_flash_mode()}"
        assert self.camera_scan.verify_camera_bottom_status_message()
        self.camera_scan.click_camera_scan_source()
        assert self.camera_scan.verify_is_camera_source_selected()

    def test_07_camera_scan_flash_features(self):
        """
        Description: C44018874
            Install and launch app.
            Sign in and go to root view.
            Add printer as device.
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile and allow access if needed.
            Check "Flash" option on camera scan screen.
        Expected Result:
            The "Flash" option has 4 modes: Flash off, Fill Flash, Auto Flash, Torch Flash
        """
        modes = ['Auto Flash', 'Flash On', 'Flash Off','Fill Flash']
        for _ in range(3):
            assert self.camera_scan.get_camera_scan_flash_mode() in modes
            self.camera_scan.click_camera_scan_flash_mode()


    def test_08_cameara_scan_ui_no_camera_access(self):
        """
        Description: C44018869
            Install and launch app.
            Sign in and go to root view.
            Add printer as device.
            Tap on Printer card and navigate to Device Details page.
            Tap camera scan action tile
            Tap on camera access button
            Select "Deny" on camera access popup.
        Expected Result:
            The No camera access message title should be displayed
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_deny_btn()
        self.camera_scan.verify_no_camera_access_title()

    def test_09_disabled_camera_item_in_source_menu(self):
        """
        Description: C44018872
            Tap Scan action tile.
            Make sure the camera permission is not allowed.
            Tap "Source" button.
        Expected Result:
            The Camera item in source menu is disabled state.
        """
        self.camera_scan.click_camera_scan_source()
        assert not self.camera_scan.is_source_camera_scan_area_enabled(), "Expected 'Camera Scan Area' to be disabled but got enabled"

    def test_10_camera_scan_preferences_for_ucde_users(self):
        """
        Description: C44018875
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap scan action tile. 
            Tap the gear button to show "Preferences" screen.
        Expected Result:
            Verifies the "Preferences" screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.select_settings_button()
        self.camera_scan.verify_preference_screen()

    def test_11_camera_scan_adjust_boundaries_screen(self):
        """
        Description: C44018878
            Navigate back to the camera scan screen.
            Capture a photo and process to "Adjust Boundaries" screen.
        Expected Result:
            Verify the "Adjust Boundaries" screen,
            Verify tap "Next" button will show "Cropping and enhancing the document..." message.
        """
        self.driver.back()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_full_option_btn()
        self.camera_scan.select_adjust_next_btn()
        self.camera_scan.verify_invisible_crop_enhance_popup()
        self.camera_scan.verify_print_preview_screen()

    def test_12(self):
        """
        Description: C44018883
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap scan action tile.
            Capture a photo and process to preview screen.
            Tap "Print Preview" button.
        Expected Result:
            Swipe up or down can show the whole print settings.
            Verify the print preview screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.camera_scan.verify_invisible_crop_enhance_popup()
        self.print_preview.verify_print_preview_screen()
        self.print_preview.click_print_preview_button()
        self.driver.swipe()
        assert self.print_preview.verify_printer_item()
        assert self.print_preview.verify_copies_item()
        assert self.print_preview.verify_paper_size_item()
        assert self.print_preview.verify_color_mode_item()

    def test_13_adjust_boundaries_auto_option(self):
        """
        Description: C44018892
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap scan action tile.
            Capture a photo and process to preview screen.
        Expected Result:
            The "Auto" option is selected by default and the app automatically adjusted the boundaries(detect edges).
            Tap "Next" button to preview screen, and the auto detected edges can show on preview screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        assert self.camera_scan.verify_is_auto_crop_selected_after_scan()
        self.camera_scan.select_adjust_next_btn()
        self.camera_scan.verify_invisible_crop_enhance_popup()
        self.print_preview.verify_print_preview_screen()

    def test_14_adjust_boundaries_full_option(self):
        """
        Description: C44018893
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap scan action tile.
            Capture a photo and process to preview screen.
        Expected Result:
            Select "Full" option to adjust the boundaries.
            Tap "Next" button to preview screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.click_full_crop_option()
        self.camera_scan.click_adjust_next_btn()
        self.camera_scan.verify_invisible_crop_enhance_popup()
        self.print_preview.verify_print_preview_screen()

    def test_15_tap_x_button_on_camera_scan_screen(self):
        """
        Description: C44018896
            Install and launch app. 
            Sign in and go to root view. 
            Add printer as device. 
            Tap on Printer card and navigate to Device Details page.
            Tap scan action tile.
            Tap 'X' button.
        Expected Result:
            The camera scan screen can be closed after tapped 'X' button on camera scan screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.select_x_button()
        self.hpx_printer_details.verify_camera_scan_tile()

    def test_16_camera_scan_edit_functionality_testing(self):
        """
        Description: C50821409
            Install and launch app.
            Sign in and go to root view.
            Add printer as device.
            Tap on Printer card and navigate to Device Details page.
            Tap scan action tile.
            Capture a photo and process to preview screen.
            After the scan completes, click on the "..." (Edit) button to access the editing options.
            Modify the image by rotating it.
            Save the changes.
        Expected Result:
            The user should be navigated back to the print preview screen after saving the changes.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_coarchmark_close_btn()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        assert self.print_preview.verify_edit_screen_title()
        self.print_preview.click_crop_btn()
        self.print_preview.click_img_rotate_btn()
        self.print_preview.click_crop_screen_done_btn()
        self.print_preview.click_edit_screen_done_btn()
        self.print_preview.verify_print_preview_screen()