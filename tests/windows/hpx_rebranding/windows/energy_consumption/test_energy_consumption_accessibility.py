import logging
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Energy_Consumption_Accessibility(object):
    # Should be run on MasadaNX

    @pytest.mark.function
    def test_01_color_filter_grayscale_C51250983(self):
        try:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["energy_consumption"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.maximize_and_verify_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Energy consumption card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_color_filter)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["energy_consumption"].revert_system_color_filter()    

    #@pytest.mark.function
    # def test_02_magnifier_energy_consumption_C51250989(self):
    #     try:
    #         platform=self.platform.lower()
    #         self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
    #         time.sleep(2)
    #         self.fc.fd["energy_consumption"].click_search_bar_on_windows()
    #         self.fc.fd["energy_consumption"].search_bar_on_windows("Magnifier")
    #         self.fc.swipe_to_top()

    #         self.fc.fd["energy_consumption"].reset_zoom()
    #         logging.info("reset to 100%")
    #         time.sleep(10)

    #         self.fc.fd["energy_consumption"].zoom_in()
    #         logging.info("Magnify 200%")
    #         time.sleep(2)
    #         self.fc.swipe_to_top()
    #         image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_magnifier, machine_type=platform, percent="200")
    #         # Only assert if screenshot comparison actually happened
    #         if image_compare_result is not None:
    #             assert image_compare_result, "LOne image did not match the baseline."
    #         else:
    #             logging.info("No screenshot comparison performed (context manager not active)")

    #         self.fc.fd["energy_consumption"].reset_zoom()
    #         logging.info("reset to 100%")
    #         time.sleep(2)
    #         self.fc.swipe_to_top()
    #         image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["energy_consumption"].verify_magnifier, machine_type=platform, percent="100")
    #         # Only assert if screenshot comparison actually happened
    #         if image_compare_result is not None:
    #             assert image_compare_result, "LOne image did not match the baseline."
    #         else:
    #             logging.info("No screenshot comparison performed (context manager not active)")

    #     finally:
    #         self.fc.fd["energy_consumption"].close_magnifier()
    #         self.fc.close_myHP()