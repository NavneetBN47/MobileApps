import pytest
import time
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_PenControl_Restart(object):

    #this suite should run on commercial devices masadan with trio pen
       
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restart_scenario_custom_apps_C53000294(self,request):
        try:
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_my_pen_page()
            #customize buttons testing
            assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
            upper_barrel_action_global_app = self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page()
            lower_barrel_action_global_app = self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page()
            #add Access app on custom apps
            self.fc.fd["pen_control"].click_add_button()
            self.fc.fd["pen_control"].click_access_on_application_list_dialog()
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            time.sleep(2)
            assert self.fc.fd["pen_control"].verify_access_app_on_carousel(), "Access app is not displayed on carousel"
            if bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is False:
                self.fc.fd["pen_control"].click_access_app_on_carousel()
            upper_barrel_action_access_app = self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page()
            lower_barrel_action_access_app = self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page()
            assert upper_barrel_action_global_app == upper_barrel_action_access_app, "Upper barrel action for Access app is not retained"
            assert lower_barrel_action_global_app == lower_barrel_action_access_app, "Lower barrel action for Access app is not retained"
            self.fc.fd["pen_control"].click_customize_back_button()
            time.sleep(2)
            # radial menu testing
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_context_aware_all_app_button()
            assert self.fc.fd["pen_control"].get_pen_control_redial_menu_slice1_action_l_ltwo_page() == "Next track"," Next Track action in slice1 is not visible"
            assert self.fc.fd["pen_control"].get_web_browser_text_commercial() == "Web browser"," Web browser action in slice2 is not visible"
            assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio"," Mute Audio action in slice3 is not visible"
            assert self.fc.fd["pen_control"].get_email_text_commercial() == "E-mail"," E-mail action in slice4 is not visible"
            assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track"," Previous Track action in slice5 is not visible"
            assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down"," Volume Down action in slice6 is not visible"
            assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause"," Play/Pause action in slice7 is not visible"
            assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up"," Volume Up action in slice8 is not visible"
            self.fc.fd["pen_control"].click_access_app_on_carousel()
            assert self.fc.fd["pen_control"].get_pen_control_redial_menu_slice1_action_l_ltwo_page() == "Next track"," Next Track action in slice1 is not visible"
            assert self.fc.fd["pen_control"].get_web_browser_text_commercial() == "Web browser"," Web browser action in slice2 is not visible"
            assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio"," Mute Audio action in slice3 is not visible"
            assert self.fc.fd["pen_control"].get_email_text_commercial() == "E-mail"," E-mail action in slice4 is not visible"
            assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track"," Previous Track action in slice5 is not visible"
            assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down"," Volume Down action in slice6 is not visible"
            assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause"," Play/Pause action in slice7 is not visible"
            assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up"," Volume Up action in slice8 is not visible"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            time.sleep(2)
            #testing with pen sesitivity
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            self.fc.fd["pen_control"].click_context_aware_all_app_button()
            assert self.fc.fd["pen_control"].get_pen_sensitivity_pressure_slider_value() == "3"," Pen sensitivity slider is not at default position 3"
            assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "0", "Tilt slider value is not 0"
            self.fc.fd["pen_control"].click_access_app_on_carousel()
            assert self.fc.fd["pen_control"].get_pen_sensitivity_pressure_slider_value() == "3"," Pen sensitivity slider is not at default position 3"
            assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "0", "Tilt slider value is not 0"
            time.sleep(2)
            restart_machine(self, request)
            time.sleep(5)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.check_and_navigate_to_my_pen_page()
            time.sleep(5)
            #customize buttons testing after restart
            self.fc.fd["pen_control"].click_customize_buttons()
            assert self.fc.fd["pen_control"].verify_access_app_on_carousel(), "Access app is not displayed on carousel after restart"
            self.fc.fd["pen_control"].click_access_app_on_carousel()
            assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page() == "Universal select", "Upper barrel action for Access app is not retained after restart"
            assert self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page() == "Erase", "Lower barrel action for Access app is not retained after restart"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            #radial menu testing after restart
            time.sleep(2)            
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_access_app_on_carousel()
            assert self.fc.fd["pen_control"].get_pen_control_redial_menu_slice1_action_l_ltwo_page() == "Next track"," Next Track action in slice1 is not visible"
            assert self.fc.fd["pen_control"].get_web_browser_text_commercial() == "Web browser"," Web browser action in slice2 is not visible"
            assert self.fc.fd["pen_control"].get_mute_audio_text_commercial() == "Mute audio"," Mute Audio action in slice3 is not visible"
            assert self.fc.fd["pen_control"].get_email_text_commercial() == "E-mail"," E-mail action in slice4 is not visible"
            assert self.fc.fd["pen_control"].get_previous_track_text_commercial() == "Previous track"," Previous Track action in slice5 is not visible"
            assert self.fc.fd["pen_control"].get_volume_down_text_commercial() == "Volume down"," Volume Down action in slice6 is not visible"
            assert self.fc.fd["pen_control"].get_play_pause_text_commercial() == "Play/Pause"," Play/Pause action in slice7 is not visible"
            assert self.fc.fd["pen_control"].get_volume_up_text_commercial() == "Volume up"," Volume Up action in slice8 is not visible"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()            
            time.sleep(2)
            #pen sensitivity testing after restart
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            self.fc.fd["pen_control"].click_access_app_on_carousel()
            assert self.fc.fd["pen_control"].get_pen_sensitivity_pressure_slider_value() == "3"," Pen sensitivity slider is not at default position 3"
            assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "0", "Tilt slider value is not 0"
        
        finally:
            self.fc.close_myHP()
