import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):
    
    #this suite should run on willie,grogu, testudo(portrait consumer tv)
    
    @pytest.mark.function
    def test_01_changing_switching_display_modes_thorugh_windows_settings_w_r_t_selecting_lbl_work_and_low_light_modes_form_window_settings_C61426273(self):
        self.fc.close_myHP()
        time.sleep(5)
        self.fc.open_system_settings_display()
        assert bool(self.fc.fd["display_control"].verify_color_profile_in_display_setting()) == True, "Color profile is not present"
        #select any one LBL, work and low light Display mode from color profile
        self.fc.fd["display_control"].select_mode_low_blue_light_in_display_setting()
        assert self.fc.fd["display_control"].get_color_profile_dd_mode_select_box_setting() == "Low Blue Light", "Color profile is not Low blue light"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == False, "See more link is present when it should not be"
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Select mode", "Select mode not displayed in display modes select box"
        #close app and setting so next suite should run smoothly
        self.fc.close_myHP()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        #need to set other mode to avoid failure in next run
        self.fc.fd["display_control"].select_mode_low_light_color_profile_in_setting()
        self.fc.close_windows_settings_panel()
