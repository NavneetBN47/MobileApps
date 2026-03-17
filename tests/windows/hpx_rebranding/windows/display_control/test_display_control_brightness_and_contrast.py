import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Display_control(object):
    
    #this suite should be run on bopeep platform
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_default_brighntess_value_for_all_modules_for_first_launch_C52982169(self):
        time.sleep(3)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        list_of_options = ["Neutral", "Gaming", "Reading", "Night", "Movie", "HP enhance+","Native"]
        br_value = ["76","84","52","28","20","76","100"]
        options = ["display_modes_select_box_option_neutral_ltwo_page","display_modes_select_box_option_gaming_ltwo_page","display_modes_select_box_option_reading_ltwo_page","display_modes_select_box_option_night_ltwo_page","display_modes_select_box_option_movie_ltwo_page","display_modes_select_box_option_hp_enhance_ltwo_page"]

        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        for i in range(6):
            self.fc.fd["display_control"].scroll_dropdown_by_key(desired_mode_id=options[i])
            self.fc.fd["display_control"].select_display_modes_dropdown_value(options[i])
            time.sleep(2)
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == list_of_options[i], "mode is not matching."
            assert self.fc.fd["display_control"].get_brightness_slider_value() == br_value[i], f"Brightness value for {list_of_options[i]} mode is not matching."
            self.fc.fd["display_control"].get_focus_on_app("display_control_display_modes_select_box_ltwo_page")
            time.sleep(2)
            self.fc.fd["display_control"].scroll_up_display_modes_list_window()
            time.sleep(3)
