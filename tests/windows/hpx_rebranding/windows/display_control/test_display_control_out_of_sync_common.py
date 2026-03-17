import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Display_control(object):
    
    #this suite should be run on all platform
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_brightness_slider_with_respective_windows_settings_C52983146(self):
        self.fc.close_myHP()
        #Launch the Windows settings application-windows settings application should be launch
        self.fc.open_system_settings_display()
        assert bool(self.fc.fd["display_control"].verify_system_setting_brightness_slider()) == True, "Brightness slider is not present"
        #change the Brightness value from Windows settings application-Brightness value should change from Windows
        self.fc.fd["display_control"].set_slider_value("system_setting_brightness_slider",70)
        assert self.fc.fd["display_control"].get_system_setting_brightness_slider() == "70", "Brightness value is not 70"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        #.verify Display control module should open and inline notification for out of sync should Display
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        #Click on see more hyper link of inline notification--5.App settings not synchronized, prompt messege should be display and with 3 options,a) Discard changes,b) Keep new changes,c)Cancel button
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_keep_changes_button_ltwo_page() == "Keep new changes", "Keep new changes button is not present"
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_discard_changes_button_ltwo_page() == "Discard changes", "Discard changes button is not present"
        assert self.fc.fd["display_control"].verify_display_control_out_of_synch_cancel_button_ltwo_page() == "Cancel", "Cancel button is not present"
        #If we click on Keep New changes button-changes are made in the Windows settings application should be synchronized to HPX application
        self.fc.fd["display_control"].click_display_control_out_of_synch_keep_new_changes_button_ltwo_page()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "70", "Brightness value is not 70"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.fd["display_control"].click_setting_on_taskbar()
        self.fc.fd["display_control"].set_slider_value("system_setting_brightness_slider",65)
        self.fc.close_windows_settings_panel()
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        self.fc.fd["display_control"].click_display_control_out_of_synch_see_more_link_ltwo_page()
        self.fc.fd["display_control"].click_display_control_out_of_synch_discard_changes_button_ltwo_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "70", "Brightness value is not 70"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_relaunching_the_display_control_module_C52983164(self):
        self.fc.close_myHP()
        self.fc.open_system_settings_display()
        assert bool(self.fc.fd["display_control"].verify_system_setting_brightness_slider()) == True, "Brightness slider is not present"
        self.fc.fd["display_control"].set_slider_value("system_setting_brightness_slider",65)
        assert self.fc.fd["display_control"].get_system_setting_brightness_slider() == "65", "Brightness value is not 65"
        self.fc.fd["devicesMFE"].click_top_minimize_btn()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
        self.fc.restart_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.fd["display_control"].scroll_to_element("display_control_card_lone_page")
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        assert bool(self.fc.fd["display_control"].verify_display_control_out_of_synch_see_more_link_ltwo_page()) == True, "See more link is not present"
