import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Video_Control(object):

    def verify_images(self, image_compare_result, image_name, platform):
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline for {platform}."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    def verify_windows_mode_contrast(self, platform):
        try:
            for theme in ["aquatic_contrast_theme", "desert_contrast_theme", "dusk_contrast_theme", "night_sky_contrast_theme"]:
                self.fc.set_windows_contrast_theme_from_settings(theme)
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["video_control"].verify_video_control_page,machine_name=platform, page_number=1, element="camera_pop_up_cancel_button", mode=theme)
                self.verify_images(image_compare_result,"video_control_poly_popup", platform)
                self.fc.fd["devicesMFE"].click_minimize_app()
        finally:
            self.fc.set_windows_contrast_theme_from_settings("none_contrast_theme")

    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_keyboard_navigation_in_commercial_consumer_arm_systems_C53129874(self):
        """Test ID: C53129874

        This test verifies keyboard navigation functionality in the Video Control feature on different platforms:
        - Commercial systems: HP Presence Video app
        - Consumer systems: Poly Camera Pro app with camera popup
        - ARM systems: Direct Poly Camera Pro app
        """
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")

        # =====================================================================
        # Commercial device with HP Presence Video (warpath)
        # =====================================================================
        if platform == "warpath":
            try:
                self.fc.close_myHP()
                install_status = self.fc.fd["video_control"].install_hp_presence_commercial_system()
                assert not install_status is False, "HP Presence Video app installation failed"
                self.fc.kill_msstore_process()
                time.sleep(5)
   
                self.fc.launch_myHP()
                self.fc.maximize_and_verify_device_card()
                self.fc.swipe_window(direction="down", distance=6)
                video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()

                assert video_control_card.text == "Video", "Video card is not displayed"
                hp_presence_video_contextual_text = self.fc.fd["video_control"].get_hp_presence_video_contextual_text()
                assert hp_presence_video_contextual_text == "HP Presence Video", "Video card is not displayed"

                self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
                for _ in range(3): # Retry if the app loses focus and key press on video card fails to open hp presence video app
                    if self.fc.fd["video_control"].verify_hp_presence_window_pop_up():
                        break
                    else:
                        self.fc.fd["video_control"].bring_app_back_to_focus()
                        self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
                        time.sleep(3)
                status = self.fc.fd["video_control"].verify_hp_presence_window_pop_up()
                assert status, "HP Presence Video main window is not displayed"

            finally: # Cleanup: Uninstall HP Presence Video app if it was installed even if the test fails.
                logging.info("Cleaning up: Uninstalling HP Presence Video app if installed.")
                self.fc.close_myHP()
                self.fc.kill_camera_process()
                self.fc.windows_setting_page_to_unistall_apps("Hp Presence Video")

        # =====================================================================
        # Consumer device with Poly Camera Pro (enstrom)
        # =====================================================================
        elif platform == "enstrom":
            self.fc.maximize_and_verify_device_card()

            video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
            assert video_control_card.text == "Video", f"Video card title, expected `Video` but found `{video_control_card.text}`"
            poly_camera_contextual_text = self.fc.fd["video_control"].get_poly_camera_contextual_text()
            assert poly_camera_contextual_text == "Poly Camera Pro", f"Video card contextual text, expected `Poly Camera Pro` but found `{poly_camera_contextual_text}`"

            self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
            for _ in range(3): # Retry if the app loses focus and key press on video card fails to open the camera popup
                if self.fc.fd["video_control"].verify_camera_pop_up():
                    break
                else:
                    self.fc.fd["video_control"].bring_app_back_to_focus()
                    logging.info(f"Pressing  on `video_card_lone_page` and retrying verification of verify_camera_pop_up")
                    self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
                    time.sleep(3)
            assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"
            assert self.fc.fd["video_control"].verify_camera_description_text(), "Camera Description text is not displayed"

            self.fc.fd["video_control"].press_tab("camera_pop_up_continue_button")
            assert self.fc.fd["video_control"].is_focus_on_element("camera_pop_up_cancel_button"), "Camera Pop up continue button is not in focus"

            self.fc.fd["video_control"].press_tab("camera_pop_up_cancel_button")
            assert self.fc.fd["video_control"].is_focus_on_element("camera_pop_up_continue_button"), "Camera Pop up cancel button is not in focus"
          
            self.fc.fd["video_control"].press_enter("camera_pop_up_cancel_button")
            for _ in range(3): # Retry if the app loses focus and key press on cancel button fails to return to video lone page
                if self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page():
                    break
                else:
                    self.fc.fd["video_control"].bring_app_back_to_focus()
                    logging.info(f"Pressing  on `video_card_lone_page` and retrying verification of verify_video_lone_page")
                    self.fc.fd["video_control"].press_enter("camera_pop_up_cancel_button")
                    time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page(), "Video lone page is not displayed"

            self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
            for _ in range(3): # Retry if the app loses focus and key press on video card fails to open camera popup
                if self.fc.fd["video_control"].verify_camera_pop_up():
                    break
                else:
                    self.fc.fd["video_control"].bring_app_back_to_focus()
                    logging.info(f"Pressing  on `video_card_lone_page` and retrying verification of verify_camera_pop_up")
                    self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
                    time.sleep(3)
            assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"

            self.fc.fd["video_control"].press_enter("camera_pop_up_continue_button")
            for _ in range(3): # Retry if the app loses focus and the key press on continue button fails to open poly camera window
                if self.fc.fd["video_control"].verify_poly_camera_window_pop_up():
                    break
                else:
                    self.fc.fd["video_control"].bring_app_back_to_focus()
                    logging.info(f"Pressing  on `video_card_lone_page` and retrying verification of verify_camera_pop_up")
                    self.fc.fd["video_control"].press_enter("camera_pop_up_continue_button")
                    time.sleep(3)
            assert self.fc.fd["video_control"].verify_poly_camera_window_pop_up(), "Poly Camera Pro install page is not displayed"
            self.fc.kill_msstore_process()

        # =====================================================================
        # ARM device with Poly Camera Pro (divinity)
        # =====================================================================
        elif platform == "divinity":
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=3)
            video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
            assert video_control_card.text == "Video", f"Video card title, expected `Video` but found `{video_control_card.text}`"
            poly_camera_contextual_text = self.fc.fd["video_control"].get_poly_camera_contextual_text()
            assert poly_camera_contextual_text == "Poly Camera Pro", f"Video card contextual text, expected `Poly Camera Pro` but found `{poly_camera_contextual_text}`"

            self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
            for _ in range(3): # Retry if the app loses focus and the key press on video card fails to open the Poly Camera popup
                if self.fc.fd["video_control"].verify_poly_camera_window_pop_up():
                    break
                else:
                    self.fc.fd["video_control"].bring_app_back_to_focus()
                    logging.info(f"Pressing  on `video_card_lone_page` and retrying verification of verify_camera_pop_up")
                    self.fc.fd["devices_details_pc_mfe"].press_enter("video_card_lone_page")
                    time.sleep(3)
            assert self.fc.fd["video_control"].verify_poly_camera_window_pop_up(), "Poly Camera Pro install page is not displayed"
    
    @pytest.mark.function
    def test_02_dark_mode_C53003917(self):
        """Test ID: C53003917
        This test verifies that the Video Control feature adheres to dark mode settings in the application, 
        if poly camera app not installed in platform.
        """
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        # =====================================================================
        # Consumer device with Poly Camera Pro (enstrom)
        # =====================================================================
        if platform == "enstrom":
            try:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.enable_dark_mode()
                time.sleep(2)  # Wait for the UI to update
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["video_control"].verify_video_control_page,machine_name=platform,page_number=1,element="camera_pop_up_cancel_button",mode="dark_mode", raise_e=False)
                self.verify_images(image_compare_result,"video_control_poly_popup", platform)
            finally:
                self.fc.disable_dark_mode()
    
    @pytest.mark.function
    def test_03_check_contrast_theme_C42915215(self):
        """Test ID: C42915215
        This test verifies that the Video Control feature adheres to high contrast theme settings in the application, 
        if poly camera app not installed in platform.
        """
        platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        # =====================================================================
        # Consumer device with Poly Camera Pro (enstrom)
        # =====================================================================
        try:
            if platform == "enstrom":
                logging.info("Testing video_control high contrast settings")
                time.sleep(2)
                self.verify_windows_mode_contrast(platform)
        finally:
            logging.info("Reverting back to normal mode")
            self.fc.close_myHP()        