from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.vcosmos_utilities import VcosmosUtilities
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_Display_Control(object):
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_brightness_slider_with_respective_to_key_board_funtion_key_C52983147(self):
        self.fc.check_and_navigate_to_display_control_page()
        assert 90 == int(self.fc.fd["display_control"].get_brightness_slider_value()), "Brightness slider value is not 90"
        self.vcosmos.press_decrease_brightness_button()
        assert 75 <= int(self.fc.fd["display_control"].get_brightness_slider_value()) <= 85, "Brightness slider value is not between 50 and 70"
        if (self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link() is not False):
            self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page() == "Keep new changes", "Keep new changes button is not present"
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page() == "Discard changes", "Discard changes button is not present"
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page() == "Cancel", "Cancel button is not present"
            self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page() is False, "See more link is present"
        assert 75 <= int(self.fc.fd["display_control"].get_brightness_slider_value()) <= 85, "Brightness slider value is not between 50 and 70"
        self.vcosmos.press_decrease_brightness_button()
        assert 65 <= int(self.fc.fd["display_control"].get_brightness_slider_value()) <= 75, "Brightness slider value is not 20 to 40"
        if (self.fc.fd["display_control"].verify_display_control_out_of_sync_see_more_link() is not False):
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page() == "Keep new changes", "Keep new changes button is not present"
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page() == "Discard changes", "Discard changes button is not present"
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page() == "Cancel", "Cancel button is not present"
            self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
            assert 75 <= int(self.fc.fd["display_control"].get_brightness_slider_value()) <= 85, "Brightness slider value is not between 50 and 70"
            assert self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page() is False, "See more link is present"
        #restoring the value for upcoming tc 
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        self.vcosmos.clean_up_logs()