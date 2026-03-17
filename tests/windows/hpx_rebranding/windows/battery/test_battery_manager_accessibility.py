import logging
import pytest
import time
from selenium.webdriver.common.keys import Keys

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Battery_Accessibility(object):
    # Should be run on MasadaNX
    
    def verify_images(self,image_compare_result,image):
        if image_compare_result is not None:
            assert image_compare_result, f"{image} image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    @pytest.mark.function
    def test_01_battery_enable_color_filter_verify_all_elements_work_well_C60186376(self):
        try:
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            time.sleep(2)        
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["battery"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            for _ in range(3):
                if self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial():
                    break
                else:
                    self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_color_filter)
            self.verify_images(image_compare_result, "verify_color_filter")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["battery"].revert_system_color_filter()
    
    @pytest.mark.function
    def test_02_battery_manageability_modify_the_registry_to_enable_the_battery_manager_ui_C60208812(self):
        try:
            platform = self.platform.lower()
            logging.info(f"Starting battery manageability test for platform: {platform}")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_ui, machine_type=platform, reg="before_reg_set")
            self.verify_images(image_compare_result, "verify_battery_ui")
            self.fc.close_myHP()
            self.fc.add_registry_key_for_battery_manager(self.driver.ssh)
            self.fc.launch_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["battery"].verify_battery_ui, machine_type=platform, reg="after_reg_set")
            self.verify_images(image_compare_result, "verify_battery_ui")
            
        finally:
            self.fc.remove_registry_key_for_battery_manager(self.driver.ssh)
