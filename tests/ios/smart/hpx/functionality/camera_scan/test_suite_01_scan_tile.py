import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import FLASH_MODE

pytest.app_info = "SMART"

class Test_Suite_01_Scan_Tile:

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

    def test_01_verify_user_can_allow_camera_access_tile(self):
        """
        Description: C44018859
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Tap on the allow option on the screen
                4. Tap on "Allow" option on the system pop to take pictures and videos
            Expected Result:
                4. Verify that the camera access screen should be displayed for the first time install and the UI is as per Figma
                verify that camera scan screen should be displayed with "manual" capture mode option chosen by default and flash mode chosen as "Auto" by default
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

    def test_02_verify_source_ui_when_scan_supported_printer_selected(self):
        """
        Description: C44018857
                1. Install and launch the app
                2. Add a scan supported printer to the device list
                3. Navigate to Device detail page
                4. Tap on camera scan or Printer Scan and Tap on Source icon
            Expected Result:
                4. Verify the Source UI is as per the Figma Source menu should have Camera, Printer and Files& Photos option
        """
        self.camera.clear_tips_pop_up()
        self.camera.select_source_button()
        self.camera.verify_source_menu_ui()

    def test_03_verify_default_source_user_tap_on_scan(self):
        """
        Description: C44018860
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Tap on the allow option on the screen
                4. Tap on "Allow" option on the system pop to take pictures and videos
            Expected Result:
                4. Verify that the camera access screen should be displayed for the first time install and the UI is as per Figma
                verify that camera scan screen should be displayed with "manual" capture mode option chosen by default and flash mode chosen as "Auto" by default
        """
        self.camera.verify_flash_mode_state(FLASH_MODE.FLASH_AUTO)
        self.camera.verify_default_capture_mode(capture_mode="manual")

    def test_04_verify_camera_scan_auto_features(self):
        """
        Description: C44018873
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Check "Auto" option on camera scan screen.
            Expected Result:
                Verify:
                    1. "Auto" option is disabled by default for "Photo"/"Document" presets.
                    2. "Auto" option is enabled by default for "Batch" preset.
                    3. When Auto" option is enabled, it will show coach marks: "Searching...", "Scanning...", "Processing...".
                    4. A thumbnail will displays at bottom right corner after captured a photo.
                    5. Tap the thumbnail will processing to preview screen. (For iOS)
        """
        self.camera.select_preset_mode(self.camera.DOCUMENT)
        self.camera.verify_default_capture_mode(capture_mode="Manual")
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.camera.verify_default_capture_mode(capture_mode="Manual")
        self.camera.select_preset_mode(self.camera.BATCH)
        self.camera.verify_default_capture_mode(capture_mode="Auto")
        self.camera.verify_batch_ui()

    def test_05_verify_camera_scan_flash_modes(self):
        """
        Description: C44018874
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Check "Flash" option on camera scan screen.
            Expected Result:
                3. Verify:
                    1. The "Flash" option has 4 modes: Flash off, Fill Flash, Auto Flash, Torch Flash.
                    2. Each flash mode can works well.
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
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_AUTO)
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_TORCH)
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_ON)
        self.camera.select_and_verify_flash_mode(FLASH_MODE.FLASH_OFF)

    def test_06_verify_camera_scan_preferences(self):
        """
        Description: C44018875
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

    def test_07_verify_preferences_btn_behaviour(self):
        """
        Description: C44018877
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
        self.camera.select_auto_enhancements()
        self.camera.select_auto_orientation()

    def test_08_verify_camera_scan_detect_edges(self):
        """
        Description: C44018879
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Tap on the allow option on the screen
                4. Capture a photo and process to "Detect Edges" screen.
            Expected Result:
                4. Verify:
                    1. The "Detect Edges" screen UI as per design.
                    2. Tap "Next" button will show "Processing ..." message.
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
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_nav()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()

    def test_09_exit_scan_from_preview(self):
        """
        Description: C44018880
                1. Click Scan tile on printer detail page
                2. Observe the allow access UI
                3. Tap on Camera Scan and navigate to Preview screen.
                4. Tap on Back arrow on Preview screen.
            Expected Result:
                4.Verify the the pop up for Exit Scan appears. Compare the UI as shown in Figma.
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
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()
        self.preview.select_preview_back()
        self.preview.verify_scan_exit_screen()

    def test_10_print_preview_from_camera_scan(self):
        """
        Description: C44018883
                1. Click Scan tile on printer detail page
                2. Capture a photo and process to preview screen.
                3. Tap "Print Preview" button.
            Expected Result:
                3. Swipe up or down can show the whole print settings. Verify print preview UI show as per design.
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
        self.camera.select_capture_btn()
        self.camera.select_adjust_boundaries_next()
        self.preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.PRINT_PREVIEW_BTN)
        self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)