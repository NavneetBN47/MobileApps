import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Hp_Go(object):

    def verify_images(self,image_compare_result):
        if image_compare_result is not None:
            assert image_compare_result, f"LOne image match with base line image."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    #this suite should only run on Lapaz platforms
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_hp_go_ui_page_C52101132(self):
        self.fc.maximize_and_verify_device_card()
        time.sleep(2)
        self.fc.fd["hp_go"].scroll_to_element("hp_go_card_on_pcdevice_page")
        self.fc.fd["devices_details_pc_mfe"].click_hp_go_card()
        for _ in range(5):
            if self.fc.fd["hp_go"].verify_hp_go_status_text():
                logging.info("HP Go status text is displayed successfully.")
                break
            else:
                logging.info("HP Go status text is not displayed.")
                self.fc.restart_app_navigate_to_hp_go()
        
        time.sleep(2)
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["hp_go"].verify_hp_go_image, machine_type="Lapaz")
        self.verify_images(image_compare_result)
    
    @pytest.mark.function
    def test_02_hp_go_color_filters_C52101128(self):
        try:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["hp_go"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            time.sleep(2)
            for _ in range(5):
                if self.fc.fd["hp_go"].verify_hp_go_status_text():
                    logging.info("HP Go status text is displayed successfully.")
                    break
                else:
                    logging.info("HP Go status text is not displayed.")
                    self.fc.restart_app_navigate_to_hp_go()
        
            time.sleep(2)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["hp_go"].verify_hp_go_image, machine_type="Lapaz_gray_scale_inverted")
            self.verify_images(image_compare_result)
        finally:
            if not self.fc.fd["hp_go"].verify_hp_go_title_on_hp_go_page():
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["hppk"].revert_system_color_filter() 
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_hpgo_high_contrast_theme_C52101130(self):
        try:
            self.fc.open_high_contrast_themes_settings()
            self.fc.fd["hp_go"].set_contrast_theme_from_settings("night_sky_contrast_theme")
            time.sleep(5)
            self.fc.close_windows_settings_panel()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            for _ in range(5):
                if self.fc.fd["hp_go"].verify_hp_go_status_text():
                    logging.info("HP Go status text is displayed successfully.")
                    break
                else:
                    logging.info("HP Go status text is not displayed.")
                    self.fc.restart_app_navigate_to_hp_go()
        
            time.sleep(2)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["hp_go"].verify_hp_go_image, machine_type="Lapaz_night_sky_contrast_theme")
            self.verify_images(image_compare_result)
            
        finally:
            if not self.fc.fd["hp_go"].verify_hp_go_title_on_hp_go_page():
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.open_high_contrast_themes_settings()
            self.fc.fd["hp_go"].set_contrast_theme_from_settings("none_contrast_theme")
            time.sleep(5)
            self.fc.close_windows_settings_panel()
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_hp_go_dark_mode_visibility_C52101744(self):
        try:
            self.fc.enable_dark_mode()
            for _ in range(5):
                if self.fc.fd["hp_go"].verify_hp_go_status_text():
                    logging.info("HP Go status text is displayed successfully.")
                    break
                else:
                    logging.info("HP Go status text is not displayed.")
                    self.fc.restart_app_navigate_to_hp_go()
            time.sleep(2)
            self.fc.enable_dark_mode()
            time.sleep(2)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["hp_go"].verify_hp_go_image, machine_type="Lapaz_dark_mode")
            self.verify_images(image_compare_result)
        finally:
            self.fc.disable_dark_mode()
