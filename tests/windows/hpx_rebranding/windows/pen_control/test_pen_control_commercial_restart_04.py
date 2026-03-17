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
    def test_01_restart_scenario_global_apps_config_on_custom_apps_C53000296(self,request):
        try:
            self.fc.launch_myHP()
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["devicesMFE"].maximize_the_hpx_window()
            time.sleep(5)
            #customize buttons testing
            assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
            #click add button
            self.fc.fd["pen_control"].click_add_button()
            self.fc.fd["pen_control"].enter_app_name_in_add_app_search_bar_ltwo_page("Calculator")
            self.fc.fd["display_control"].select_display_control_calculator_app_on_add_application_popup_lthree_page()
            self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
            time.sleep(2)
            assert self.fc.fd["pen_control"].verify_calculator_app_on_carousel(), "Calculator app is not displayed on carousel"
            self.fc.fd["pen_control"].click_calculator_app_on_carousel()
            # change lower barrel action as productivity paste
            self.fc.fd["pen_control"].click_lower_barrel_button_commercial()
            self.fc.fd["pen_control"].click_pencontrol_lower_barrel_btn_prod_paste()
            self.fc.fd["pen_control"].click_customize_back_button()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "Lower barrel action for Calculator app is not retained"
            self.fc.fd["pen_control"].click_customize_back_button()
            #radial menu testing
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_calculator_app_on_carousel()
            #change slice 2 action as paste
            self.fc.fd["pen_control"].click_radial_slice2_button()
            self.fc.fd["pen_control"].click_radial_menu_slice2_paste_radio_btn()
            self.fc.fd["pen_control"].click_customize_back_button()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "slice 2 action for Calculator app is not retained"
            self.fc.fd["pen_control"].click_customize_back_button()
            #pen sensitivity testing
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            self.fc.fd["pen_control"].click_calculator_app_on_carousel()
            #increase tilt sensitivity to max
            self.fc.fd["pen_control"].set_slider_max("pen_sensitivity_tilt_slider")
            #restart machine
            restart_machine(self, request)
            time.sleep(5)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.check_and_navigate_to_my_pen_page()
            time.sleep(5)
            #customize buttons testing after restart
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_calculator_app_on_carousel()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "Lower barrel action for Calculator app is not retained"
            self.fc.fd["pen_control"].click_customize_back_button()
            #radial menu testing after restart
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_calculator_app_on_carousel()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_paste_text() == "Paste", "slice2 action for Calculator app is not retained"
            self.fc.fd["pen_control"].click_customize_back_button()
            #pen sensitivity testing after restart
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            self.fc.fd["pen_control"].click_calculator_app_on_carousel()
            assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "2", "tilt slider value is not retained after restart"
        
        finally:
            self.fc.close_myHP()
