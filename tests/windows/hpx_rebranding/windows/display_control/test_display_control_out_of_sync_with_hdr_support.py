import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):
    
    #this method can run on willie,keelung32,bucky,thompson(platforms that have HDR toggle button in windows settings)
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_hdr_toggle_button_on_with_respective_windows_settings_C52983159(self):
        self.fc.close_myHP()
        self.fc.open_hdr_settings()
        assert self.fc.fd["display_control"].verify_display_control_use_hdr_in_system_settings() == "Use HDR","HDR settings text is not matching"
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0":
            self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle button is not off"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        time.sleep(3)
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        #Click on see more hyper link of inline notification--5.App settings not synchronized, prompt messege should be display and with 3 options,a) Discard changes,b) Keep new changes,c)Cancel button
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page() == "Keep new changes", "Keep new changes button is not present"
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page() == "Discard changes", "Discard changes button is not present"
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page() == "Cancel", "Cancel button is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle button is not on"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle button is not off"
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle button is not on"

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_hdr_toggle_button_off_with_respective_windows_settings_C52983160(self):
        self.fc.close_myHP()
        self.fc.open_hdr_settings()
        assert self.fc.fd["display_control"].verify_display_control_use_hdr_in_system_settings() == "Use HDR","HDR settings text is not matching"
        if self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1":
            self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "0", "HDR toggle button is not off"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
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
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not on"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        self.fc.fd["display_control"].click_display_control_hdr_toggle_window_setting()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_toggle_state() == "1", "HDR toggle button is not off"
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0", "HDR toggle button is not on"
