import logging
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Dock_Station_Accessibility(object):
# Runs on machu machine with dock

    def verify_images(self,image_compare_result):
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"Dock module image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    @pytest.mark.function
    def test_01_change_system_color_mode_verify_ui_shows_correctly_C52835945(self):
        try:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["dock_station"].select_system_color_mode("light_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
                self.fc.fd["devicesMFE"].maximize_app()
            assert bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is True, "Dock station card is not displayed"
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_dock_station_card()
            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["dock_station"].verify_get_help_card_show_up, mode="light_mode")
            self.verify_images(image_compare_result)
            self.fc.fd["dock_station"].swipe_down_to_product_warranty_details()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["dock_station"].verify_get_warranty_details_show_up, mode="light_mode")
            self.verify_images(image_compare_result)
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["dock_station"].select_system_color_mode("dark_mode")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["dock_station"].verify_get_help_card_show_up, mode="dark_mode")
            self.verify_images(image_compare_result)
            self.fc.fd["dock_station"].swipe_down_to_product_warranty_details()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["dock_station"].verify_get_warranty_details_show_up, mode="dark_mode")
            self.verify_images(image_compare_result)
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["dock_station"].revert_system_color_mode()
    
    @pytest.mark.function
    def test_02_press_alt_f4_from_keyboard_verify_hpx_will_close_C52835946(self):
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        time.sleep(2)
        self.fc.fd["dock_station"].press_alt_f4_to_close_app()
        time.sleep(3)
        assert bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is False, "Dock station card is still displayed after closing HPX"
