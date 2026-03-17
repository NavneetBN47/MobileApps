import pytest
import time
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_Control(object):
    
    #this suite should run on willie,herbie robotics with HDR portrait
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_display_control_and_hdr_hdr_vs_appsettings_C42891436(self,request):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        #click restore defaults
        self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
        self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_ltwo_page()
        #adding access application in context aware
        self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
        self.fc.fd["display_control"].enter_app_name_in_display_control_add_app_search_bar_ltwo_page("Access")
        self.fc.fd["display_control"].select_display_control_access_app_on_add_application_popup_lthree_page()
        self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
        assert "Access" in self.fc.fd["display_control"].verify_display_control_access_app_ltwo_page(), "Access app is not present"
        self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
        #select mode as native and hdr as on for access app with restart myHP
        self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
        self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
        self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_willie_native_ltwo_page")
        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page("1")

        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Native mode is not selected for Access app"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR is not ON for Access app"

        self.fc.restart_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()

        if self.fc.fd["display_control"].verify_is_display_control_access_app_selected() == "false":
            self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Native mode is not selected for Access app"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR is not ON for Access app"
        
        #restart tv
        restart_machine(self, request)
        self.fc.restart_myHP()
        time.sleep(5)

        self.fc.maximize_and_verify_device_card()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        if self.fc.fd["display_control"].verify_is_display_control_access_app_selected() == "false":
            self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
        time.sleep(5)
        assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Native mode is not selected for Access app"
        assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR is not ON for Access app"
