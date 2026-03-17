import pytest
import time
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe_robotics")
class Test_Suite_PenControl_UI(object):

    #this suite should run on willie with trio pen and robotic introduction

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_restart_scenario_custom_apps_C53000294(self,request):
        try:
            self.vcosmos.introduce_pen()
            self.vcosmos.clean_up_logs()
            self.fc.fd["devicesMFE"].click_back_button_rebranding()   
            self.fc.fd["devicesMFE"].verify_pen_card_show()   
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_pen_card()
            time.sleep(10)
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
            #testing with customize buttons-upper and lower barrel actions(default-right click, erase)
            self.fc.fd["pen_control"].click_customize_upper_barrel_button()
            #add application as access app
            self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Access", "access_app_on_install_modal")
            assert self.fc.fd["pen_control"].verify_access_app_on_carousel(), "Access app is not displayed on carousel"
            if bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is False:
                self.fc.fd["pen_control"].click_access_app_on_carousel()
            #set upper barrel action as undo
            self.fc.fd["pen_control"].click_undo_radio_btn_upper_barrel()
            self.fc.fd["pen_control"].click_customize_back_button()
            assert self.fc.fd["pen_control"].verify_access_app_on_carousel(), "Access app is not displayed on carousel"
            if bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is False:
                self.fc.fd["pen_control"].click_access_app_on_carousel()

            #verify upper barrel button action as undo
            assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_undo_action_lthree_page() == "Undo"," Upper barrel button action is not set to Undo"
            #click lower barrel button
            self.fc.fd["pen_control"].click_customize_lower_barrel_button()
            #select undo action for lower barrel button
            self.fc.fd["pen_control"].click_pen_control_customize_btn_lower_barrel_btn_undo_radio_btn_lthree_page()
            self.fc.fd["pen_control"].click_customize_back_button()
            #verify  barrel button action as undo
            assert self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_undo_action_lthree_page() == "Undo"," Lower barrel button action is not set to Undo"

            #restart the device
            restart_machine(self, request)
            time.sleep(5)
            self.fc.restart_myHP()
            time.sleep(5)
            self.fc.fd["devicesMFE"].click_pen_card()
            time.sleep(10)
            self.fc.fd["pen_control"].click_customize_buttons()
            assert self.fc.fd["pen_control"].verify_access_app_on_carousel(), "Access app is not displayed on carousel"
            if bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is False:
                self.fc.fd["pen_control"].click_access_app_on_carousel()

            assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_undo_action_lthree_page() == "Undo"," Upper barrel button action is not set to Undo"
            assert self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_undo_action_lthree_page() == "Undo"," Lower barrel button action is not set to Undo"
        finally:
            self.fc.close_myHP()
