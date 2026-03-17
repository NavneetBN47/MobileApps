import pytest
import time
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_Restart(object):

    #this suite sould run on commercail devices only as Machu 13x with moon racer pen
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_consistency_invoke_after_s2_restart_C55483271(self,request):
        try:
            self.fc.check_and_navigate_to_my_pen_page()
            assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
            self.fc.fd["pen_control"].click_customize_buttons()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
            time.sleep(2)
            self.fc.fd["pen_control"].click_single_press_button_commercial()
            self.fc.fd["pen_control"].scroll_to_element("customize_topbutton_single_press_screensnipping_radio_button")
            self.fc.fd["pen_control"].click_customize_topbutton_single_press_screensnipping_radio_button()
            self.fc.fd["pen_control"].scroll_to_element("pen_ltwo_page_title")
            self.fc.check_and_navigate_to_customize_buttons_page()
            assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen Snipping action is not visible"
            time.sleep(2)
            self.fc.fd["pen_control"].click_double_press_button_commercial()
            self.fc.fd["pen_control"].scroll_to_element("customize_topbutton_double_press_mswhiteboard_radio_button")
            self.fc.fd["pen_control"].click_customize_topbutton_double_press_mswhiteboard_radio_button()
            self.fc.fd["pen_control"].scroll_to_element("pen_ltwo_page_title")
            self.fc.check_and_navigate_to_customize_buttons_page()
            assert self.fc.fd["pen_control"].get_ms_whiteboard_text_commercial() == "MS Whiteboard", "MS Whiteboard action is not visible"
            time.sleep(2)
            self.fc.fd["pen_control"].click_long_press_button_commercial()
            self.fc.fd["pen_control"].scroll_to_element("customize_topbutton_long_press_screen_snipping_radio_button")
            self.fc.fd["pen_control"].click_customize_topbutton_long_press_screen_snipping_radio_button()
            self.fc.fd["pen_control"].scroll_to_element("pen_ltwo_page_title")
            self.fc.check_and_navigate_to_customize_buttons_page()
            assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen Snipping action is not visible"
            time.sleep(2)
            self.fc.fd["pen_control"].click_customize_upper_barrel_button()
            self.fc.fd["pen_control"].scroll_to_element("customize_upper_barrel_erase_radio_button")
            self.fc.fd["pen_control"].click_customize_upper_barrel_erase_radio_button()
            self.fc.fd["pen_control"].scroll_to_element("pen_ltwo_page_title")
            self.fc.check_and_navigate_to_customize_buttons_page()
            assert self.fc.fd["pen_control"].get_erase_text_commercial() == "Erase", "Erase action is not visible"
            time.sleep(2)
            self.fc.fd["pen_control"].click_customize_lower_barrel_button()
            self.fc.fd["pen_control"].scroll_to_element("customize_lower_barrel_right_click_radio_button")
            self.fc.fd["pen_control"].click_customize_lower_barrel_right_click_radio_button()
            self.fc.fd["pen_control"].scroll_to_element("pen_ltwo_page_title")
            self.fc.check_and_navigate_to_customize_buttons_page()
            assert self.fc.fd["pen_control"].get_upper_barrel_button_right_click_text() == "Right click", "Right Click action is not visible" 
            
            restart_machine(self, request)
            
            self.fc.restart_myHP()
            time.sleep(2)
            self.fc.check_and_navigate_to_my_pen_page()
            assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
            self.fc.fd["pen_control"].click_customize_buttons()
            #verify all actions that were set before restart
            time.sleep(2)
            assert self.fc.fd["pen_control"].get_erase_text_commercial() == "Erase", "Erase action is not visible"
            assert self.fc.fd["pen_control"].get_upper_barrel_button_right_click_text() == "Right click", "Right Click action is not visible"
            assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen Snipping action is not visible"
            assert self.fc.fd["pen_control"].get_ms_whiteboard_text_commercial() == "MS Whiteboard", "MS Whiteboard action is not visible"
            assert self.fc.fd["pen_control"].get_screen_snipping_text_commercial() == "Screen snipping", "Screen Snipping action is not visible"
        
        finally:
            self.fc.close_myHP()