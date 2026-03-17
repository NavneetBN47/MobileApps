import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_UI(object):
    
    #this suite should run for moonracer on commercial platform
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_pressure_sensitivity_C44262457(self):
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        self.fc.fd["devicesMFE"].click_pen_card()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        self.fc.fd["pen_control"].scroll_to_element("restore_default_button_lone_page")
        self.fc.fd["pen_control"].click_restore_default_button_lone_page()
        time.sleep(1)
        self.fc.fd["pen_control"].click_restore_default_continue_button_lone_page()
        time.sleep(1)
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        assert  self.fc.fd["pen_control"].verify_pen_sensitivity_card(), "Pen Sensitivity card is not visible"
        self.fc.fd["pen_control"].click_pen_sensitivity_card()
        assert self.fc.fd["pen_control"].get_pressure_sensitivity_text() == "Pressure", "Pressure is not visible"
        assert self.fc.fd["pen_control"].verify_pen_sensitivity_pressure_low_indicator(), "Low Pressure on slider is not visible"
        assert self.fc.fd["pen_control"].verify_pen_sensitivity_pressure_high_indicator(), "High Pressure on slider is not visible"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_moonracer_pen_commercial_ui_C52240401(self):
        #click back btn to reach lone page
        self.fc.fd["pen_control"].click_customize_back_button()
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize buttons Label is not visible"
        #1) Header should be shown with the pen name and the connected status
        assert self.fc.fd["pen_control"].get_hp_rechargeable_active_pen_g3pencontrol() == "HP Rechargeable Active Pen G3", "HP Rechargeable Active Pen G3 is not visible"
        time.sleep(3)
        assert "Connected" in self.fc.fd["pen_control"].get_connected_text_lone_page(), "Connected status is not visible"
        #2) Pen image should be shown in the right side
        assert bool(self.fc.fd["pen_control"].verify_pen_image_lone_page()) is True, "Pen image is not visible"
        #3) Customize button card
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        #4) Radial menu card
        assert self.fc.fd["pen_control"].verify_radial_menu_commercial(), "Radial Menu is not available"
        self.fc.fd["pen_control"].scroll_to_element("notification_tab_text_lone_page")
        #5)  Pen for external display card
        assert self.fc.fd["pen_control"].verify_external_display_card(), "External Display Card is not available"
        #6) Pen sensitivity card
        assert  self.fc.fd["pen_control"].verify_pen_sensitivity_card(), "Pen Sensitivity card is not visible"
        #7)Notification tab which includes "Alert when pen is out of range" text with a toggle switch
        assert self.fc.fd["pen_control"].get_notification_tab_text_lone_page() == "Alert when pen is out of range", "Alert when pen is out of range is not visible"
        toggle_state = self.fc.fd["pen_control"].get_toggle_state_pen_out_of_range_alert()
        assert toggle_state == "0", f"Toggle switch default state: expected `0` actual `{toggle_state}`"
        self.fc.fd["pen_control"].scroll_to_element("restore_default_button_lone_page")
        #8) Product information card
        assert bool(self.fc.fd["pen_control"].verify_product_information_card_lone_page()) is True, "Product Information card is not visible"
        #9) Restore default button
        assert self.fc.fd["pen_control"].get_restore_default_button_lone_page() == "Restore defaults", "Restore defaults button is not visible"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_pen_for_external_display_C51466830(self):
        self.fc.fd["pen_control"].scroll_to_element("external_display_card")
        assert "External display" in (self.fc.fd["pen_control"].verify_external_display_card()), "Pen for external display card is not visible"
        assert bool(self.fc.fd["pen_control"].verify_desktop_icon_on_pen_external_display_lone_page()) is True, "Pen for external display icon is not visible"
        self.fc.fd["pen_control"].click_external_display_card()
        #1) Pen for external display card should be opened.
        assert bool(self.fc.fd["pen_control"].verify_pen_ltwo_page_title()) is True, "Pen for external display title is not visible on LTwo page"
        #2) Below features should be present in this card:
        #a) Display Selection for input with a dropdown box in the right side should be present.
        assert "Display selection for input" in self.fc.fd["pen_control"].get_external_display_display_selection_for_input_txt() , "Display Selection for input is not visible"
        assert bool(self.fc.fd["pen_control"].verify_display_selection_dd_ltwo_page()) is True , "Display Selection is not visible"
        # The External Card Display feature requires the external monitor to be set to “Extend” mode. 
        # The feature will only be enabled when the display is configured as an extended screen
        if self.fc.fd["pen_control"].verify_enable_this_feature_text_ltwo_page() is False:
            #minimize app
            self.fc.fd["devicesMFE"].click_minimize_app()
            #set external monitor as extended if that set as duplicate        
            self.fc.fd["pen_control"].set_external_monitor_as_extended()
            #maximize app
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            for _ in range(3):
                if self.fc.fd["pen_control"].verify_external_display_title_text() is True:
                    break
                else:
                    time.sleep(2)
                    self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        #b) Enable this feature string with a toggle in the right side should be present.
        assert bool(self.fc.fd["pen_control"].verify_enable_this_feature_text_ltwo_page()) is True, "Enable this feature is not visible"
        #assert self.fc.fd["pen_control"].get_state_enable_this_feature_toggle_switch_ltwo_page() == "Enable this feature is off", "Enable this feature is not visible"
        if self.fc.fd["pen_control"].get_toggle_state_enable_this_feature_toggle_switch_ltwo_page() == "0":
            assert self.fc.fd["pen_control"].get_state_enable_this_feature_toggle_switch_ltwo_page() == "Enable this feature is off", "Enable this feature toggle is not off"
            self.fc.fd["pen_control"].click_enable_this_feature_toggle_switch_ltwo_page()
        else:
            assert self.fc.fd["pen_control"].get_state_enable_this_feature_toggle_switch_ltwo_page() == "Enable this feature is on", "Enable this feature toggle is not on"
            
        time.sleep(8)#when toggle turn off/on ,screen got black for few seconds
        #c) Device orientation, Input mode and Display mapping categories actions should be present.with actions should be present.
        assert bool(self.fc.fd["pen_control"].verify_device_orientation_ltwo_page()) is True, "Device orientation is not visible"
        assert self.fc.fd["pen_control"].get_landscape_ltwo_page() == "Landscape", "Landscape is not visible"
        assert self.fc.fd["pen_control"].get_landscape_flipped_ltwo_page() == "Landscape flipped", "Landscape flipped is not visible"
        assert self.fc.fd["pen_control"].get_portrait_ltwo_page() == "Portrait", "Portrait is not visible"
        assert self.fc.fd["pen_control"].get_portrait_flipped_ltwo_page() == "Portrait flipped", "Portrait flipped is not visible"
        assert bool(self.fc.fd["pen_control"].verify_input_mode_ltwo_page()) is True, "Input mode is not visible"
        assert self.fc.fd["pen_control"].get_pen_only_ltwo_page() == "Pen only", "Pen only is not visible"
        assert self.fc.fd["pen_control"].get_pen_and_touch_ltwo_page() == "Pen and touch", "Pen and touch is not visible"
        assert bool(self.fc.fd["pen_control"].verify_display_mapping_ltwo_page()) is True, "Display mapping is not visible"
        self.fc.fd["pen_control"].scroll_to_element("restore_default_external_display_ltwo_page")
        assert self.fc.fd["pen_control"].get_scale_ltwo_page() == "Scale", "Scale is not visible"
        assert self.fc.fd["pen_control"].get_stretch_ltwo_page() == "Stretch", "Stretch is not visible"
        #3) Restore default button should be present.
        assert self.fc.fd["pen_control"].get_external_display_restore_defaults_button_text() == "Restore defaults", "Restore defaults button is not visible"
        #4) Desktop image with a hand and pen should be present in the right side of the UI.
        assert bool(self.fc.fd["pen_control"].verify_desktop_icon_on_pen_external_display_ltwo_page()) is True, "Desktop image with hand and pen is not visible"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_reassignment_button_C53023960(self):
        self.fc.fd["pen_control"].scroll_to_element("customize_back_buttons")
        self.fc.fd["pen_control"].click_customize_back_button()
        #Click on any card which contains the action list-Customize buttons card/ Radial menu card / One step inking card
        self.fc.fd["pen_control"].click_customize_buttons()
        #Note- make sure this MS whiteboard application is assigned with only one btn/barrel.
        #default action on top button single press-ms white board "that need to be change"
        self.fc.fd["pen_control"].get_focus_on_app("customize_top_button_single_press")
        #some time single press btn not clicked at one click so added loop
        for _ in range(3):
            if self.fc.fd["pen_control"].verify_pen_control_customize_btn_top_btn_single_press_title_text_lthree_page() is True:
                break
            else:
                self.fc.fd["pen_control"].click_single_press_button_commercial()

        self.fc.fd["pen_control"].click_pen_control_customize_btn_top_btn_single_press_pen_menu_action_lthree_page()
        self.fc.fd["pen_control"].click_customize_back_button()
        #Uninstall any of the application from system which is present in that action list.For eg: MS Whiteboard application can be uninstalled.
        self.fc.uninstall_msboard_app()
        #Now select the application which is uninstalled in the action list.
        self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
        #1) Uninstalled application should be selected as action in the list
        self.fc.fd["pen_control"].scroll_to_element("customize_buttons_upper_barrel_mswhiteboard_lthree_page")
        time.sleep(3)
        self.fc.fd["pen_control"].click_customize_buttons_upper_barrel_mswhiteboard_lthree_page()
        if self.fc.fd["pen_control"].is_selected_customize_buttons_upper_barrel_mswhiteboard_lthree_page() == "false":
            self.fc.fd["pen_control"].click_customize_buttons_upper_barrel_mswhiteboard_lthree_page()
        #2) Assigned app not available" message should be shown below the button name.
        self.fc.fd["pen_control"].get_focus_on_app("customize_buttons_upper_barrel_mswhiteboard_lthree_page")
        time.sleep(2)
        self.fc.fd["pen_control"].scroll_to_element("assign_app_not_available_lthree_page")
        time.sleep(3)
        #Navigate to L1 page and check the header section
        assert self.fc.fd["pen_control"].get_assign_app_not_available_lthree_page() == "Assigned app not available", "Assigned app not available is not visible"        
        self.fc.fd["pen_control"].click_customize_back_button()
        self.fc.fd["pen_control"].click_customize_back_button()
        # If the action is selected in Customize buttons card --> Button needs reassignment button with a pen icon should be present.
        assert self.fc.fd["pen_control"].get_button_need_reassignment_lone_page() == "Button needs reassignment", "Button needs reassignment is not visible"
        #Click on the Reassignment button from the L1 page
        self.fc.fd["pen_control"].click_button_need_reassignment_lone_page()
        #This should navigate to action list page where the reassignment of the action is required.
        assert self.fc.fd["pen_control"].get_assign_app_not_available_lthree_page() == "Assigned app not available", "Assigned app not available is not visible"        
        self.fc.fd["pen_control"].click_customize_back_button()
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_assigned_app_not_available_message_C53023933(self):
        #Click on any card which contains the action list-Customize buttons card/ Radial menu card / One step inking card should be clicked.
        self.fc.check_and_navigate_to_customize_buttons_page()       
        #Uninstall any of the application from system which is present in that action list.For eg: MS Whiteboard application can be uninstalled-
        self.fc.uninstall_msboard_app()
        #Now select the application which is uninstalled in the action list.
        self.fc.fd["pen_control"].click_upper_barrel_button_commercial()
        self.fc.fd["pen_control"].scroll_to_element("customize_buttons_upper_barrel_mswhiteboard_lthree_page")
        self.fc.fd["pen_control"].click_customize_buttons_upper_barrel_mswhiteboard_lthree_page()
        if self.fc.fd["pen_control"].is_selected_customize_buttons_upper_barrel_mswhiteboard_lthree_page() == "false":
            self.fc.fd["pen_control"].click_customize_buttons_upper_barrel_mswhiteboard_lthree_page()
        #2) Assigned app not available" message should be shown below the button name.
        self.fc.fd["pen_control"].scroll_to_element("assign_app_not_available_lthree_page")
        time.sleep(3)
        #Navigate to L1 page and check the header section
        assert self.fc.fd["pen_control"].get_assign_app_not_available_lthree_page() == "Assigned app not available", "Assigned app not available is not visible"        
        self.fc.fd["pen_control"].click_customize_back_button()
        self.fc.fd["pen_control"].click_customize_back_button()
        #click radial card
        self.fc.fd["pen_control"].click_radial_menu_button()
        #click slice 1 button
        self.fc.fd["pen_control"].click_radial_slice1_button()
        self.fc.fd["pen_control"].scroll_to_element("radial_menu_commercial_slice1_mswhiteboard_radio_button")
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_menu_commercial_slice1_mswhiteboard_radio_button()
        if self.fc.fd["pen_control"].is_selected_radial_menu_commercial_slice1_mswhiteboard_radio_button() == "false":
            self.fc.fd["pen_control"].click_radial_menu_commercial_slice1_mswhiteboard_radio_button()
        #Now navigate to the action list page and verify the message displayed for uninstalled application
        self.fc.fd["pen_control"].scroll_to_element("assign_app_not_available_lthree_page")
        #2) "Assigned app not available" message should be displayed in all the buttons where the uninstalled application is selected.
        assert self.fc.fd["pen_control"].get_assign_app_not_available_lthree_page() == "Assigned app not available", "Assigned app not available is not visible"        
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Assigned app not available" in self.fc.fd["pen_control"].get_radial_menu_commercial_slice1(), "Assigned app not available is not visible"        
        #click slice 2 and select uninstalled app
        self.fc.fd.get("pen_control").click_radial_slice2_button()
        self.fc.fd["pen_control"].scroll_to_element("radial_menu_commercial_slice2_mswhiteboard_radio_button")
        self.fc.fd["pen_control"].click_radial_menu_commercial_slice2_mswhiteboard_radio_button()
        if self.fc.fd["pen_control"].is_selected_radial_menu_commercial_slice2_mswhiteboard_radio_button() == "false":
            self.fc.fd["pen_control"].click_radial_menu_commercial_slice2_mswhiteboard_radio_button()
        self.fc.fd["pen_control"].scroll_to_element("assign_app_not_available_lthree_page")
        assert self.fc.fd["pen_control"].get_assign_app_not_available_lthree_page() == "Assigned app not available", "Assigned app not available is not visible"        
        self.fc.fd["pen_control"].click_customize_back_button()
        assert "Assigned app not available" in self.fc.fd["pen_control"].get_radial_menu_commercial_slice2() , "Assigned app not available is not visible"
        # Navigate back to Radial Menu
        self.fc.fd["pen_control"].click_customize_back_button()       
        # Navigate back to My Pen Page
        self.fc.fd["pen_control"].click_customize_back_button() 
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_alert_when_pen_is_out_of_range_toggle_status_C53003656(self):
        self.fc.check_and_navigate_to_my_pen_page() # Ensures the test starts on the MyPen page even if the previous test navigated away.        
        assert "Connected" in self.fc.fd["pen_control"].get_connected_text_lone_page() ,"Connected status is not visible"
        self.fc.fd["pen_control"].scroll_to_element("notification_tab_text_lone_page")
        toggle_state = self.fc.fd["pen_control"].get_toggle_state_pen_out_of_range_alert()
        assert toggle_state == "0", f"Toggle switch default state: expected `0` actual `{toggle_state}`"

        self.fc.fd["pen_control"].click_notification_tab_toggle_off_switch_lone_page() # Turn the toggle ON
        toggle_state = self.fc.fd["pen_control"].get_toggle_state_pen_out_of_range_alert()
        assert toggle_state == "1", f"Toggle switch state after click: expected `1` actual `{toggle_state}`"
        # Revert after test completed
        self.fc.fd["pen_control"].click_notification_tab_toggle_switch_lone_page() # Turn the toggle OFF
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_tilt_sensitivity_C44262844(self):
        self.fc.check_and_navigate_to_my_pen_page() # Ensures the test starts on the MyPen page even if the previous test navigated away.
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        self.fc.fd["pen_control"].click_pen_sensitivity_card()
        assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "0", "Tilt slider value is not 0"
        self.fc.fd["pen_control"].set_slider_max("pen_sensitivity_tilt_slider")
        assert self.fc.fd["pen_control"].get_pen_sensitivity_tilt_slider_value() == "2", "Tilt slider value is not 2"
