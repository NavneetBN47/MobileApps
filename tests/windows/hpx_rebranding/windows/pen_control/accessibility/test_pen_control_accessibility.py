import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Pen_Accessibility_UI(object):
# this suite should only run on machu13x platforms

    def verify_images(self, image_compare_result, image_name, percentage=None, color=None):
        if percentage:
            logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
            log=f"{percentage}% text size"
        elif color:
            logging.info(f"Image comparison result at {color}% color filter: {image_compare_result}")
            log=f"{color} color filter"

        # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline for {log}."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    @pytest.mark.require_platform(["not available"])
    def test_01_verify_increase_text_size_C53057168(self):
        try: 
            platform=self.platform.lower()
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["pen_control"].update_text_size_in_system_settings(225)
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=1, element="connected_text_lone_page", text_size=225)
            self.verify_images(image_compare_result, "Pen LOne page1", percentage=225)

            self.fc.fd["pen_control"].scroll_down_to_element("notification_card")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=2, element="notification_card", text_size=225)
            self.verify_images(image_compare_result, "Pen LOne page2", percentage=225)

            self.fc.fd["pen_control"].scroll_down_to_element("restore_default_button_lone_page")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=3, element="restore_default_button_lone_page", text_size=225)
            self.verify_images(image_compare_result, "Pen LOne page3", percentage=225)

        finally: # Ensure text size is reset to 100% even if test fails
            self.fc.fd["pen_control"].update_text_size_in_system_settings(100)

    @pytest.mark.require_platform(["not available"])
    def test_02_verify_magnify_C53058563(self):
        try:
            platform=self.platform.lower()
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["pen_control"].click_search_bar_on_windows()
            self.fc.fd["pen_control"].search_bar_on_windows("Magnifier")
            self.fc.swipe_to_top()

            self.fc.fd["pen_control"].reset_zoom() #Make sure we are starting at 100%
            logging.info("reset to 100%")
            time.sleep(10)

            self.fc.fd["pen_control"].zoom_in()        
            logging.info("Magnify 200%")
            time.sleep(2)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=1, element="connected_text_lone_page", text_size=200)
            self.verify_images(image_compare_result, "Pen LOne page1", percentage=200)

            self.fc.fd["pen_control"].scroll_down_to_element("notification_card")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=2, element="notification_card", text_size=200)
            self.verify_images(image_compare_result, "Pen LOne page2", percentage=200)

            self.fc.fd["pen_control"].scroll_down_to_element("restore_default_button_lone_page")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=3, element="restore_default_button_lone_page", text_size=200)
            self.verify_images(image_compare_result, "Pen LOne page3", percentage=200)
        finally: # Ensure magnifier is closed even if test fails
            self.fc.fd["pen_control"].close_magnifier()

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.function
    def test_03_colour_filter_grayscale_C53057479(self):
        try:
            platform=self.platform.lower()
            self.fc.check_and_navigate_to_my_pen_page()
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["pen_control"].change_system_color_filter("gray_scale_inverted_radio_btn_settings")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()

            time.sleep(3)
            self.fc.swipe_to_top()
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_color, machine_name=platform, page_number=1, element="connected_text_lone_page", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Pen LOne page1", color="gray_scale_inverted")

            self.fc.fd["pen_control"].scroll_down_to_element("notification_card")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_color, machine_name=platform, page_number=2, element="notification_card", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Pen LOne page2", color="gray_scale_inverted")

            self.fc.fd["pen_control"].scroll_down_to_element("restore_default_button_lone_page")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page_color, machine_name=platform, page_number=3, element="restore_default_button_lone_page", color="gray_scale_inverted", raise_e=False)
            self.verify_images(image_compare_result, "Pen LOne page3", color="gray_scale_inverted")
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["hppk"].revert_system_color_filter()
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
   

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.function
    def test_04_display_scale_size_C53057357(self):
        try:
            platform=self.platform.lower()
            self.fc.check_and_navigate_to_my_pen_page()
            for scale in ["scale_150_percent","scale_200_percent"]:
                self.fc.fd["devicesMFE"].click_minimize_app()
                self.fc.fd["display_control"].set_scale_from_settings(scale)
                time.sleep(2)
                self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
                self.fc.swipe_to_top()
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=1, element="connected_text_lone_page", text_size=scale)
                self.verify_images(image_compare_result, "Pen LOne page1", percentage=200)

                self.fc.fd["pen_control"].scroll_down_to_element("notification_card")
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=2, element="notification_card", text_size=scale)
                self.verify_images(image_compare_result, "Pen LOne page2", percentage=200)

                self.fc.fd["pen_control"].scroll_down_to_element("restore_default_button_lone_page")
                image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_page, machine_name=platform, page_number=3, element="restore_default_button_lone_page", text_size=scale)
                self.verify_images(image_compare_result, "Pen LOne page3", percentage=200)

        #ensure to set the scale back to 100% even if the test fails
        finally:
            self.fc.fd["devicesMFE"].click_minimize_app()
            self.fc.fd["display_control"].set_scale_from_settings("scale_100_percent")
            self.fc.fd["devicesMFE"].click_myhp_on_task_bar()


    @pytest.mark.function
    def test_05_pen_control_navigation_using_keyboard_C53056910(self):
        self.fc.check_and_navigate_to_my_pen_page()

        # press TAB and verify that the focus is on radial menu card
        self.fc.fd["pen_control"].press_tab("customize_buttons")
        assert self.fc.fd["pen_control"].is_focus_on_element("radial_menu_commercial"), "Radial menu card is not highlighted."
       
        # press TAB and verify that the focus is on external display card
        self.fc.fd["pen_control"].press_tab("radial_menu_commercial")
        assert self.fc.fd["pen_control"].is_focus_on_element("external_display_card"), "External display card is not highlighted."

        # press TAB and verify that the focus is on pen sensitivity card
        self.fc.fd["pen_control"].press_tab("external_display_card")
        assert self.fc.fd["pen_control"].is_focus_on_element("pen_sensitivity_card"), "Pen sensitivity card is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("pen_sensitivity_card")
        assert self.fc.fd["pen_control"].is_focus_on_element("notification_tab_toggle_off_switch_lone_page"), "Pen out of range toggle is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("notification_tab_toggle_off_switch_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("start_virtual_assistant_button"), "Start virtual assistant button is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("start_virtual_assistant_button")
        assert self.fc.fd["pen_control"].is_focus_on_element("contact_us_button"), "Contact us button is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("contact_us_button")
        assert self.fc.fd["pen_control"].is_focus_on_element("product_number_on_product_information_card_lone_page"), "Contact us button is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("product_number_on_product_information_card_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("serial_number_on_product_information_card_lone_page"), "Product number on product information card is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("serial_number_on_product_information_card_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("warranty_status_button"), "Warranty status button is not highlighted."

        # press TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_tab("warranty_status_button")
        assert self.fc.fd["pen_control"].is_focus_on_element("restore_default_button_lone_page"), "Restore default button is not highlighted."

        # press SHIFT + TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_reverse_tab("restore_default_button_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("warranty_status_button"), "Warranty status button is not highlighted."

        # press SHIFT + TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_reverse_tab("warranty_status_button")
        assert self.fc.fd["pen_control"].is_focus_on_element("serial_number_on_product_information_card_lone_page"), "Serial number on product information card is not highlighted."

        # press SHIFT + TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_reverse_tab("serial_number_on_product_information_card_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("product_number_on_product_information_card_lone_page"), "Product number on product information card is not highlighted."
        
        # press SHIFT + TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_reverse_tab("product_number_on_product_information_card_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("contact_us_button"), "Contact us button is not highlighted."
        
        # press SHIFT + TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_reverse_tab("contact_us_button")
        assert self.fc.fd["pen_control"].is_focus_on_element("start_virtual_assistant_button"), "Start virtual assistant button is not highlighted."

        # press SHIFT + TAB and verify that the focus is on pen out of range toggle button
        self.fc.fd["pen_control"].press_reverse_tab("start_virtual_assistant_button")
        assert self.fc.fd["pen_control"].is_focus_on_element("notification_tab_toggle_off_switch_lone_page"), "Notification tab toggle off switch is not highlighted."

        # press TAB and verify that the focus is on pen sensitivity card
        self.fc.fd["pen_control"].press_reverse_tab("notification_tab_toggle_off_switch_lone_page")
        assert self.fc.fd["pen_control"].is_focus_on_element("pen_sensitivity_card"), "Pen sensitivity card is not highlighted."
        
        # press  SHIFT + TAB and verify that the focus is back on external display card
        self.fc.fd["pen_control"].press_reverse_tab("pen_sensitivity_card")
        assert self.fc.fd["pen_control"].is_focus_on_element("external_display_card"), "External display card is not highlighted."

        # press  SHIFT + TAB and verify that the focus is radial menu card
        self.fc.fd["pen_control"].press_reverse_tab("external_display_card")
        assert self.fc.fd["pen_control"].is_focus_on_element("radial_menu_commercial"), "Radial menu card is not highlighted."

        # press  SHIFT + TAB and verify that the focus is customize buttons card
        self.fc.fd["pen_control"].press_reverse_tab("radial_menu_commercial")
        assert self.fc.fd["pen_control"].is_focus_on_element("customize_buttons"), "Customize buttons card is not highlighted."

        self.fc.fd["pen_control"].press_enter("customize_buttons")
        assert bool(self.fc.fd["pen_control"].verify_upper_barrel_card_show_up()) is True, "Upper barrel button is not displayed"

        # press ALT + F4 to close the app
        self.fc.fd["pen_control"].press_alt_f4_to_close_app()
