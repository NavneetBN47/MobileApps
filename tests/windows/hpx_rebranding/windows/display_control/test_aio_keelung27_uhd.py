import logging
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control(object):

    #this suite should run on Keelung 27 UHD 
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_default_value_for_all_modes_for_first_launch_on_keelung_27_uhd_C53000458(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."        
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        time.sleep(5)
        list_of_options = ["Neutral","Warm","Cool","HP enhance+","Native"]
        brightness_slider_value = [62,14,42,62,100]
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        time.sleep(3)
        options = [
            "display_modes_select_box_option_neutral_ltwo_page_keelung27",
            "display_modes_select_box_option_warm_ltwo_page_keelung27",
            "display_modes_select_box_option_cool_ltwo_page_keelung27",
            "display_modes_select_box_option_hp_enhance_ltwo_page_keelung27",
            "display_modes_select_box_option_native_ltwo_page_keelung27"
        ]
        # Verify and validate brightness values for each mode
        for i in range(4):
            logging.info(f"Checking brightness value for {list_of_options[i]} mode")
            self.fc.fd["display_control"].select_display_modes_dropdown_value(options[i])
            time.sleep(4)
            silder_value = int(self.fc.fd["display_control"].get_brightness_slider_value())
            time.sleep(3)
            assert silder_value == brightness_slider_value[i], f"Brightness value for {list_of_options[i]} mode is not matching."
            self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
            time.sleep(3)
            self.fc.fd["display_control"].scroll_modes(direction="up",desired_mode_name=list_of_options[i],desired_mode_id=options[i])
            time.sleep(2)
