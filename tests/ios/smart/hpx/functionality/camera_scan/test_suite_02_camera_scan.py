import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import FLASH_MODE
from SAF.misc import saf_misc 

pytest.app_info = "SMART"

class Test_Suite_02_Camera_Scan:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.photos = cls.fc.fd["photos"]
        cls.fc.hpx = True
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.camera = cls.fc.fd["camera"]
        cls.preview = cls.fc.fd["preview"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.copy = cls.fc.fd["copy"]
        cls.edit = cls.fc.fd["edit"]

    def test_01_verify_document_preset(self):
        """
        Description: C44018885
                1. Tap scan action tile.
                2. Select 'Document' preset.
                3. Capture a photo and go to preview screen.
            Expected Result:
                Verify:
                    1. The "Auto" option is off by default.
                    2. The scan job with 'Document' preset can be captured successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.camera.verify_default_capture_mode(capture_mode="Auto")
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_nav()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

    def test_02_verify_photo_preset(self):
        """
        Description: C44018886
                1. Tap scan action tile.
                2. Select 'Photo' preset.
                3. Capture a photo and go to preview screen.
            Expected Result:
                Verify:
                    1. The "Auto" option is off by default.
                    2. The scan job with 'Photo' preset can be captured successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.camera.verify_default_capture_mode(capture_mode="Manual")
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_nav()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

    def test_03_verify_batch_preset(self):
        """
        Description: C44018887
                1. Tap scan action tile.
                2. Select 'Batch' preset.
                3. Capture a photo and go to preview screen.
            Expected Result:
                Verify:
                    1. The "Auto" option is off by default.
                    2. The scan job with 'Batch' preset can be captured successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_preset_mode(self.camera.BATCH)
        self.camera.verify_default_capture_mode(capture_mode="Auto")
        self.camera.select_capture_btn()
        self.camera.click_images_on_camera_scan_batch_mode()
        self.camera.verify_adjust_boundaries_nav()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

    def test_04_verify_camera_scan_landing_page_ui(self):
        """
        Description: C44018865
                1. Tap Scan action tile for the first time to trigger camera access dialog.
                2. Select 'Batch' preset.
                3. Capture a photo and go to preview screen.
            Expected Result:
                Verify:
                    1. The "Auto" option is off by default.
                    2. The scan job with 'Batch' preset can be captured successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_source_button()
        self.camera.verify_camera_source_mode_selected()

    def test_05_verify_access_camera_dialog(self):
        """
        Description: C44018867
                1.Tap Scan action tile for the first time to trigger camera access dialog.
                2.Tap "Allow" button.
            Expected Result:
                Verify the HP Smart would like to access the camera dialog with "Don't Allow" & "Allow" buttons pops up.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()

    def test_06_verify_no_camera_access(self):
        """
        Description: C44018868
                1.Tap Scan action tile for the first time to trigger camera access dialog.
                2.Tap "Don't Allow" button.
            Expected Result:
                Verify:
                    Verify the camera scan UI as per design.
                    Tap "Allow camera access" button can go to HP Smart settings.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup(allow_access=False)
        self.copy.select_enable_access_to_camera_link_text()

    def test_07_verify_allow_access_to_photos(self):
        """
        Description: C44018871
                1.Tap Scan action tile for the first time to trigger camera access dialog.
                2.Tap "Don't Allow" button.
            Expected Result:
                Verify:
                    Verify the camera scan UI as per design.
                    Tap "Allow camera access" button can go to HP Smart settings.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_FILES)
        self.photos.select_allow_access_to_photos_popup(allow_access=False)
        self.photos.select_albums_tab()
        self.photos.select_set_photos_access_btn()

    def test_08_adjust_boundaries_auto_option(self):
        """
        Description: C44018892
                1.Tap "Camera Scan" tile.
                2.Capture a photo to next screen
            Expected Result:
                Verify:
                1. The "Auto" option is selected by default and the app automatically adjusted the boundaries(detect edges).
                2. Tap "Next" button to preview screen, and the auto detected edges can show on preview screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_nav()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

    def test_09_adjust_boundaries_full_option(self):
        """
        Description: C44018893
                1.Tap "Camera Scan" tile.
                2.Capture a photo to next screen
                3.Select "Full" option. and Tap "Next" button.
            Expected Result:
                Verify:
                1. The edge changes to the full image captured.
                2. The preview matches with the adjusted image from the adjusted boundaries (Detect Edges) screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_nav()
        self.camera.select_adjust_boundaries_full()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

    def test_10_tap_x_button_on_camera_screen(self):
        """
        Description: C44018896
                1.Tap "Camera Scan" tile.
                2.Tap 'X' button.
            Expected Result:
                Verify:
                1. The edge changes to the full image captured.
                2. The preview matches with the adjusted image from the adjusted boundaries (Detect Edges) screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.verify_camera_screen()

    def test_11_camera_screen_edit_functionality(self):
        """
        Description: C50821409
                1.Launch the application.
                2.Navigate to the HP Settings tab.
                3.Enable the "Reskin UI for HPX" debug setting.
                4.Restart the application.
                5.Initiate the camera scan by clicking the camera scan button.
                6.After the scan completes, click on the "..." (Edit) button to access the editing options.
                7.Review the displayed edit options.
                8.Modify all available options (e.g., text, color, alignment, etc.) and apply changes.
            Expected Result:
                The UI should reflect all changes made to the options, demonstrating that the functionality is working correctly and the UI adapts to the changes.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        self.preview.select_delete_page_icon()
        self.preview.select_edit_btn_on_preview_screen()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_flip()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_done()
        self.preview.verify_preview_screen()

    def test_12_camera_screen_filter_functionality(self):
        """
        Description: C47933521
                1.Tap on the Camera Scan tile on the dashboard.
                2.Select the Document type and take a photo.In the Adjust Boundaries section, tap the Next button.
                3.Go to edit option there click on filters. Scanned photo/document should filter multiple times.
                4.Observe the UI and functionality of the filters.
            Expected Result:
                Scanned photo/document should filter multiple times while editing without any crashes.
        """
        self.preview.select_delete_page_icon()
        self.preview.select_edit_btn_on_preview_screen()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.verify_screen_title(self.edit.FILTERS)
        self.edit.select_edit_main_option(self.edit.FILTER_DOCUMENT)
        selected_filter_document_options = ['B/W', 'B/W 2', 'Greyscale', 'Alabaster']
        for document_type in selected_filter_document_options:
            original_img = self.edit.edit_img_screenshot()
            self.edit.select_edit_child_option(document_type, direction="left", check_end=False)
            self.edit.verify_and_swipe_adjust_slider(per_offset=0.15)
            new_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(original_img, new_image) != 0), "Filters document type {} didn't change successfully".format(document_type)
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()

    def test_13_camera_scan_preferences(self):
        """
        Description: C44018876
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Tap the gear button to show "Preferences" screen.
            Expected Result:
                3. The Preferences UI as per Figma.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_gear_setting_btn()
        assert self.camera.verify_capture_preference_screen(raise_e=False)
        self.camera.verify_capture_preference_options()

    def test_14_verify_files_and_photos(self):
        """
        Description: C44018861
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. click on files and photos in source.
            Expected Result:
                3. verify the Figma design.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_FILES)
        self.photos.select_allow_access_to_photos_popup(allow_access=False)
        self.photos.select_albums_tab()
        self.photos.verify_albums_tab()

    def test_15_default_source_camera(self):
        """
        Description: C44018863
                1. Tap Scan action tile for the first time to trigger camera access dialog.
                2. select source and verify camera
            Expected Result:
                Verify:default camera source should be selected.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.app_settings.select_sign_in_btn()
        self.hpid.login()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_to_view_device_page_from_home()
        self.home.close_use_bluetooth_pop_up()
        self.app_settings.select_ok()
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.clear_tips_pop_up()
        self.camera.select_source_button()
        self.camera.verify_camera_source_mode_selected()