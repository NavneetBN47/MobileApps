
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Display_control(object):

    #this suite should run on park
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_control_and_hdr_while_battery_options_is_unchecked_and_on_ac_mode_C52975788(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.open_hdr_settings()
        time.sleep(4)
        self.fc.click_uncheck_allow_hdr_games_video_chkbox_in_setting()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_enabled_disable() == "true","HDR toggle is disabled"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "true", "HDR toggle is disabled in display control page"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_display_control_and_hdr_while_battery_options_is_checked_and_on_AC_mode_C52975789(self):
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        time.sleep(4)
        self.fc.fd["display_control"].click_turn_off_hdr_chk_box_in_system_settings()
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_window_setting_enabled_disable() == "true","HDR toggle is disabled"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert self.fc.fd["display_control"].display_control_hdr_toggle_switch_ltwo_page_is_enabled() == "true", "HDR toggle is disabled in display control page"
        self.fc.close_myHP()
        self.fc.close_windows_settings_panel()
