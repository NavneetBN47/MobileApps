import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Display_control(object):

    def verify_images(self, image_compare_result, image_name):
        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
       
    #this suite should run on all platform where display control is available
    
    @pytest.mark.require_platform(["not available"])
    @pytest.mark.function
    def test_01_keyboard_dismiss_alt_f4_C51600929(self):
        time.sleep(3)
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=4)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        self.fc.fd["display_control"].send_alt_f4_to_active_element()
        time.sleep(10)
        assert bool(self.fc.fd["display_control"].verify_display_control_all_application_button_ltwo_page()) is False, "Application not closed properly"
    
    @pytest.mark.require_platform(["not available"])
    @pytest.mark.function
    def test_02_display_settings_C51600930(self):      
        self.fc.fd["display_control"].send_shift_f10_on_desktop()
        assert bool(self.fc.fd["display_control"].verify_color_profile_in_display_setting()) is True, "Color profile is not present"

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.function
    def test_03_turn_on_color_filter_verify_hpx_shows_correctly_C51600933(self):
        try:
            self.fc.restart_myHP()
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["display_control"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=2)
            assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
            time.sleep(3)
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_color_filter)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, "LOne image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["display_control"].revert_system_color_filter()

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.function
    def test_04_dark_mode_visibility_C51600932(self):
        platform =  platform = self.platform.lower()
        logging.info(f"Platform: {platform}")
        #------------------------------------------------------
        #    verify all images in dark mode on non portrait platform-thompson
        #------------------------------------------------------
        try:
            if platform == "thompson":#image 3 not able to verify coz it is not displayed when app selected
                self.fc.fd["dock_station"].select_system_color_mode("dark_mode")
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=1,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page1_dark_mode")
                #click restire default btn
                self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=2,element="display_control_restore_defaults_cancel_onpopup_window_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page2_dark_mode")
                #click cancel on popup
                self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_ltwo_page()
                #verify if access app not in app list then add and get restore popup
                if self.fc.fd["display_control"].is_display_control_access_app_ltwo_page_visible():
                    self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
                else:
                    self.fc.fd["display_control"].click_display_control_add_application_button_ltwo_page()
                    self.fc.fd["display_control"].enter_app_name_in_display_control_add_app_search_bar_ltwo_page("Access")
                    self.fc.fd["display_control"].select_display_control_access_app_on_add_application_popup_lthree_page()
                    self.fc.fd["display_control"].click_display_control_add_app_continue_button_ltwo_page()
                    assert "Access" in self.fc.fd["display_control"].verify_display_control_access_app_ltwo_page(), "Access app is not present"
                    self.fc.fd["display_control"].click_display_control_access_app_ltwo_page()
                #click restire default btn
                self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=3,element="display_control_restore_defaults_cancel_onpopup_window_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page3_dark_mode")
                #click cancel on popup
                self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_ltwo_page()
                #make hdr toggle on
                if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "0":
                    self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page()
                assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch state is not 1 on the L2 page."
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=4,element="display_control_hdr_toggle_switch_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page4_dark_mode")
                #--------------------
                #   verify all images in dark mode on herbie platform
                #--------------------
            elif platform == "herbie":#image 4 not able to verify coz popup not displayed
                self.fc.fd["dock_station"].select_system_color_mode("dark_mode")
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                #select photo & video mode from display mode dropdown
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                self.fc.fd["display_control"].scroll_modes(direction="up",desired_mode_name="Photos and Videos (P3 D65)",desired_mode_id="display_modes_select_box_option_photos_videos_ltwo_page")
                if self.fc.fd["display_control"].is_item_onscreen("display_modes_select_box_option_photos_videos_ltwo_page") == True:
                    self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_photos_videos_ltwo_page")
                assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Photos and Videos (P3 D65)", "Photos and Videos mode is not selected."
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=1,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page1_dark_mode")
                #click display mode
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=2,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page2_dark_mode")
                #click restore default btn
                self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=3,element="display_control_restore_defaults_cancel_onpopup_window_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page3_dark_mode")
                #click cancel on popup
                self.fc.fd["display_control"].click_display_control_restore_defaults_cancel_onpopup_window_ltwo_page()
                #click on disney+oobe app then click restore default btn
                assert self.fc.fd["display_control"].validate_display_control_disney_plus_app_ltwo_page(), "Disney+ OOBE app is not present"
                self.fc.fd["display_control"].click_display_control_disney_plus_app()
                self.fc.fd["display_control"].click_display_control_advanced_settings_restore_defaults_button_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=4,element="display_control_restore_defaults_cancel_onpopup_window_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page4_dark_mode")
                #click hdr toggle on and verify
                for _ in range(5): 
                    if self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1":
                        break
                    else:
                        self.fc.fd["display_control"].click_display_control_hdr_toggle_btn_ltwo_page()
                assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch state is not 1 on the L2 page."
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=5,element="display_control_hdr_toggle_switch_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page5_dark_mode")
                #--------------------
                #   verify all images in dark mode on keelung32 platform
                #--------------------
            elif platform == "keelung32":
                self.fc.fd["dock_station"].select_system_color_mode("dark_mode")
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()                
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=1,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page1_dark_mode")
                #click display mode
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=2,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page2_dark_mode")
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                #click advanced display settings to go lthree
                self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
                self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=3,element="display_control_restore_defaults_button_lthree_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page3_dark_mode")
                #hover over color adjusment tooltip
                self.fc.fd["display_control"].click_display_control_low_blue_light_color_adjustment_tooltip_info_lthree_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=4,element="display_control_low_blue_light_color_adjustment_tooltip_info_lthree_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page4_dark_mode")
                #hover over input switch tooltip
                self.fc.fd["display_control"].click_display_control_input_switch_tooltip_lthree_page_keelung32()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=5,element="display_control_input_switch_tooltip_lthree_page_keelung32",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page5_dark_mode")

                #--------------------
                #   verify all images in dark mode on bopeep platform
                #--------------------
            elif platform == "bopeep":#image 11,13 not displayed due to bug
                self.fc.fd["dock_station"].select_system_color_mode("dark_mode")
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                #select native mode from display mode dropdown
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                self.fc.fd["display_control"].scroll_modes_native(direction="down",desired_mode_name="Native",desired_mode_id="display_modes_select_box_option_native_ltwo_page")
                if self.fc.fd["display_control"].is_item_onscreen("display_modes_select_box_option_native_ltwo_page") == True:
                    self.fc.fd["display_control"].select_display_modes_dropdown_value("display_modes_select_box_option_native_ltwo_page")
                assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Native", "Native mode is not selected."
                #turn on contrast toggle if off
                self.fc.fd["display_control"].click_display_control_contrast_toggle_to_on()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=1,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page1_dark_mode")
                #hover over adjust contrast tooltip
                self.fc.fd["display_control"].click_display_control_adjust_contrast_tooltip_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=2,element="display_control_adjust_contrast_tooltip_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page2_dark_mode")
                #click display mode dropdown
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=3,element="display_control_advanced_settings_restore_defaults_button_ltwo_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page3_dark_mode")
                self.fc.fd["display_control"].click_display_control_display_modes_select_box_ltwo_page()
                #click advanced display settings btn
                self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
                self.fc.fd["display_control"].click_display_control_advanced_settings_card_ltwo_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=4,element="display_control_restore_defaults_button_lthree_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page4_dark_mode")
                #hover over color adjusment tooltip
                self.fc.fd["display_control"].click_display_control_low_blue_light_color_adjustment_tooltip_info_lthree_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=5,element="display_control_low_blue_light_color_adjustment_tooltip_info_lthree_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page5_dark_mode")
                #hover over use hdmi input tooltip
                self.fc.fd["display_control"].click_use_hdmi_input_tooltip()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=6,element="use_hdmi_input_tooltip",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page6_dark_mode")
                #click link hdmi input osd help
                self.fc.fd["display_control"].click_display_control_hdmi_link("display_control_advancedsettings_hdmi_link_lthree_page")
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=7,element="display_control_advancedsettings_hdmi_link_skip_button",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page7_dark_mode")
                #click next on osd popup
                logging.info("Clicking next btn usng co-ordinates.")
                self.fc.fd["display_control"].get_focus_on_app("display_control_next_btn_hdmi_popup_window")
                self.driver.click_by_coordinates(x=1394, y=934)

                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=8,element="display_control_previous_btn_hdmi_popup_window",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page8_dark_mode")
                #click next on osd popup
                self.fc.fd["display_control"].get_focus_on_app("display_control_next_btn_hdmi_popup_window")
                self.driver.click_by_coordinates(x=1394, y=934)


                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=9,element="display_control_close_btn_hdmi_popup_window",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page9_dark_mode")
                #click close on osd popup
                self.fc.fd["display_control"].click_display_control_close_btn_hdmi_popup_window()
                #click on switch btn
                self.fc.fd["display_control"].click_display_control_switch_btn_lfour_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=10,element="display_control_hdmi_popup_page_continue_button",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page10_dark_mode")
                #click continue btn on popup
                self.fc.fd["display_control"].click_display_control_hdmi_popup_continue_text()
                #click restore default btn
                self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
                for _ in range(3):
                    if self.fc.fd["display_control"].verify_display_control_restore_defaults_continue_onpopup_window_page_lthree_page():
                        break
                    else:
                        self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=11,element="display_control_restore_defaults_continue_onpopup_window_page_lthree_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page11_dark_mode")
                #click coninue on popup
                self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()
                #click on disney+oobe app then click restore default btn
                assert self.fc.fd["display_control"].validate_display_control_disney_plus_app_ltwo_page(), "Disney+ OOBE app is not present"
                self.fc.fd["display_control"].click_display_control_disney_plus_app()
                self.fc.fd["display_control"].click_display_control_restore_defaults_button_lthree_page()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["display_control"].verify_display_lone_page,machine_name=platform,page_number=12,element="display_control_restore_defaults_continue_onpopup_window_page_lthree_page",scale="dark_mode")
                self.verify_images(image_compare_result,"display_lone_page12_dark_mode")
                #click continue btn on popup
                self.fc.fd["display_control"].click_display_control_restore_defaults_continue_onpopup_window_page_lthree_page()                
            else:
                logging.info(f"No dark mode image verification steps defined for platform: {platform}")

        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["wellbeing"].revert_system_color_mode()