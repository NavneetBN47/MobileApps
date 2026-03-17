import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_changing_switching_display_modes_thorugh_windows_settings_C52983149(self):
        self.fc.close_myHP()
        self.fc.open_system_settings_display()
        assert bool(self.fc.fd["display_control"].verify_color_profile_in_display_setting()) == True, "Color profile is not present"
        #Chang/Switch Display modes from color profile
        self.fc.fd["display_control"].select_native_color_profile_in_setting()
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        #Display modes should Change/Switch from color profile
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        #Click on see more hyper link of inline notification--5.App settings not synchronized, prompt messege should be display and with 3 options,a) Discard changes,b) Keep new changes,c)Cancel button
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page() == "Keep new changes", "Keep new changes button is not present"
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page() == "Discard changes", "Discard changes button is not present"
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page() == "Cancel", "Cancel button is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Color profile is not Native"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        self.fc.fd["display_control"].select_default_color_profile_in_setting()
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Color profile is not Native"
