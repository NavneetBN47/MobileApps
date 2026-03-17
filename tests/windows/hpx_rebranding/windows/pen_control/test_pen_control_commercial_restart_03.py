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
    def test_01_restart_scenario_global_apps_C53000295(self,request):
        try:
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            #customize buttons testing
            assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
            #select Disney+ global app
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
            self.fc.fd["pen_control"].click_pencontrol_upper_barrel_btn_prod_radial_menu()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_radial_menu_text() == "Radial menu", "Upper barrel action for Disney+ global app is not retained after restart"
            self.fc.fd["pen_control"].click_customize_back_button()
            self.fc.fd["pen_control"].click_customize_back_button()
            #testing with radial menu
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_radial_slice1_button()
            #update slice1 action as paste
            self.fc.fd["pen_control"].click_radial_menu_slice1_paste_radio_btn()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "Slice1 action for Disney+ global app is not retained after restart"
            self.fc.fd["pen_control"].click_customize_back_button()
            self.fc.fd["pen_control"].click_customize_back_button()
            #testing with pen sensitivity
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            #select Disney+ global app
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            #incraese tilt sensitivity to max
            self.fc.fd["pen_control"].set_slider_max("pen_sensitivity_tilt_slider")
            assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "2", "Tilt slider value is not retained after restart"
            #select access custom app
            self.fc.fd["pen_control"].click_access_app_on_carousel()
            assert bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is True, "Access app was not selected"
            #restart machine
            restart_machine(self, request)
            time.sleep(5)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.check_and_navigate_to_my_pen_page()
            time.sleep(5)
            self.fc.fd["pen_control"].click_customize_buttons()
            time.sleep(3)
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_radial_menu_text() == "Radial menu", "Upper barrel action for Disney+ global app is not retained after restart"
            self.fc.fd["pen_control"].click_customize_back_button()
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "Slice1 action for Disney+ global app is not retained after restart"
            self.fc.fd["pen_control"].click_customize_back_button()
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            self.fc.fd["display_control"].click_display_control_disney_plus_app()
            assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "2", "Tilt slider value is not retained after restart"
        
        finally:
            self.fc.close_myHP()
