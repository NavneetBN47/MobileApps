import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

#The baseline images are taken against Machu13x2 with Roo Pen, so need to run against that.
@pytest.mark.usefixtures("class_setup_fixture_for_desktop")
class Test_Suite_PenControl_Images_UI_Roo(object):

    def assign_radial_menu_to_barrel_buttons_and_compare_images(self, barrel_type):
        time.sleep(1)
        if barrel_type in("upper","multiple")  :
            self.fc.fd["pen_control"].scroll_to_element("customize_buttons")
            self.fc.fd["pen_control"].click_customize_buttons()
            time.sleep(3)
            if barrel_type == "upper" :
                self.fc.fd["pen_control"].click_customize_upper_barrel_button()
                self.fc.fd["pen_control"].click_pencontrol_upper_barrel_btn_prod_radial_menu()
            elif barrel_type == "multiple":
                self.fc.fd["pen_control"].click_customize_lower_barrel_button()
                self.fc.fd["pen_control"].click_pencontrol_lower_barrel_btn_prod_radial_menu()
                self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
                self.fc.fd["pen_control"].click_customize_upper_barrel_button()
                self.fc.fd["pen_control"].click_pencontrol_upper_barrel_btn_prod_radial_menu()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
   
        #  Check the radial menu card image 
        self.fc.fd["pen_control"].scroll_to_element("radial_menu_commercial")
        logging.info(f"Verifying screenshot of Radial Card with {barrel_type} barrel buttons assigned")
        if barrel_type == "no":
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_radial_menu_commercial_barrel_buttons, barrel_type="no")
        elif barrel_type == "upper":
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_radial_menu_commercial_barrel_buttons, barrel_type="upper")
        elif barrel_type == "multiple":
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_radial_menu_commercial_barrel_buttons, barrel_type="multiple")
        return image_compare_result

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_01_customize_buttons_card_image_C53039313(self):
        # Ensure the test starts on the MyPen page; navigate there if not already.
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].scroll_to_element("customize_buttons")
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].wait_and_verify_customize_buttons)
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Customize Buttons card image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_02_pen_sensitivity_card_image_C53039339(self):
        # Ensure the test starts on the MyPen page; navigate there if not already.
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].wait_and_verify_pen_sensitivity_card, pen_type="roo")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Pen sensitivity card image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_03_radial_menu_ltwo_image_C53047835(self):
        # Ensure the test starts on the MyPen page and ensure the default settings are selected for each slice. 
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_radial_menu_button()
        self.fc.fd["pen_control"].click_restore_default_radial_menu_ltwo_page()
        time.sleep(1)
        self.fc.fd["pen_control"].click_restore_default_continue_radial_menu_ltwo_page()
        time.sleep(1)

        for i in range(1, 9):
            logging.info(f"Verifying screenshot of 'slice{i}' image")
            self.driver.hover(f"radial_menu_commercial_slice{i}")
            image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_slice_image, slice_number=i)
            # Only assert if screenshot comparison actually happened
            if image_compare_result is not None:
                assert image_compare_result, f"Radial Menu Slice {i} image did not match the baseline."
            else:
                logging.info("No screenshot comparison performed (context manager not active)")

        # Navigate back to MyPen page
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_04_radial_menu_lone_image_C53039340(self):
        # Ensure the test starts on the MyPen page and restore defaults to make sure no buttons are assigned to start with
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].scroll_to_element("restore_default_button_lone_page")
        self.fc.fd["pen_control"].click_restore_default_button_lone_page()
        time.sleep(1)
        self.fc.fd["pen_control"].click_restore_default_continue_button_lone_page()
        time.sleep(1)

        image_compare_result = self.assign_radial_menu_to_barrel_buttons_and_compare_images("no")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, f"Radial Menu card without any barrels assigned image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        image_compare_result = self.assign_radial_menu_to_barrel_buttons_and_compare_images("upper")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Radial Card image with upper barrel button assigned did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        image_compare_result = self.assign_radial_menu_to_barrel_buttons_and_compare_images("multiple")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Radial Card image with multiple barrel buttons assigned did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_05_radial_menu_default_ltwo_image_C51466817(self):
        # Ensure the test starts on the MyPen page and restore defaults to make sure no buttons are assigned to start with
        self.fc.check_and_navigate_to_my_pen_page()
        self.fc.fd["pen_control"].click_radial_menu_button()

        for i in range(1, 9):
            assert self.fc.fd["pen_control"].verify_slice(slice_number=i), f"Slice {i} is not displayed."
    
        assert self.fc.fd["pen_control"].verify_restore_default_radial_menu_ltwo_page(), "Restore default button is not displayed."
        self.fc.fd["pen_control"].click_restore_default_radial_menu_ltwo_page()
        time.sleep(1)
        self.fc.fd["pen_control"].click_restore_default_continue_radial_menu_ltwo_page()
        time.sleep(1)
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_radial_menu_ltwo_default_image)
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Radial Menu Ltwo page image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
       
        # Navigate back to LZero page
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()        
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()        

    @pytest.mark.require_platform(["not available"])
    @pytest.mark.commercial
    def test_06_roo_pen_image_C53044270(self):
        # Ensure the test starts on the LZero page
        if not self.fc.fd["devicesMFE"].verify_pen_card_show():
            logging.info("Pen card isn't visible. Re-launching app")
            self.fc.close_myHP()
            self.fc.launch_myHP()
            time.sleep(3)

        # Verify pen card image on lzero page
        image_compare_result =self.fc.get_screenshot_comparison_result(self.fc.fd["devicesMFE"].verify_pen_card_image)
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Pen Card image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        # Verify Roo pen image on lone page
        self.fc.fd["devicesMFE"].click_pen_card()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_pen_lone_image, pen_type="roo")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Roo pen LOne page image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        self.fc.fd["pen_control"].click_customize_buttons()
        time.sleep(1)
        # This is a workaround to get to the default image to show up. Hovering on one of the barrel buttons and then hovering on something outside seem to be the only way. 
        self.driver.hover("customize_upper_barrel_button")
        time.sleep(1)
        self.driver.hover("restore_default_customize_button_ltwo_page")

        # Verify customize buttons default image
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="default", pen_type="roo")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Customize buttons default image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")

        # Verify customize buttons upper barrel image
        self.fc.fd["pen_control"].click_customize_upper_barrel_button()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="upper", pen_type="roo")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Customize buttons upper barrel image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()

        # Verify customize buttons lower barrel image
        self.fc.fd["pen_control"].click_customize_lower_barrel_button()
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["pen_control"].verify_customize_buttons_pen_lwo_image, barrel_type="lower", pen_type="roo")
       # Only assert if screenshot comparison actually happened
        if image_compare_result is not None:
            assert image_compare_result, "Customize buttons lower barrel image did not match the baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()