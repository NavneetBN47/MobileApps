import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_UI(object):

    #this suite for Trio-X pen on Masadanx tv
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_trio_pen_commercial_ui_C52240403(self):
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        self.fc.fd["devicesMFE"].click_pen_card()
       # 1) Header with the pen name
        assert self.fc.fd["pen_control"].get_trio_x_pen_name_lone_page() == "HP 705 Rechargeable Multi Pen", "Pen name is not correct"
        #2) Pen image should be displayed in the right side of the UI
        assert bool(self.fc.fd["pen_control"].verify_pen_lone_image(pen_type="trio")), "Pen image is not displayed"
        #3) Customize buttons card
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        #4) Pen sensitivity card
        assert self.fc.fd["pen_control"].verify_pen_sensitivity_card(), "Pen Sensitivity Card is not available"
        self.fc.swipe_window(direction="down",distance=8)
        #5) Product information card
        assert bool(self.fc.fd["pen_control"].verify_product_information_card_lone_page())is True, "Product information Label is not visible"
        #6) Restore default button
        assert self.fc.fd["pen_control"].get_restore_default_button_lone_page() == "Restore defaults", "Restore defaults button is not visible"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_trio_pen_commercial_C52235901(self):
        self.fc.swipe_window(direction="up",distance=8)
        assert self.fc.fd["pen_control"].get_trio_x_pen_name_lone_page() == "HP 705 Rechargeable Multi Pen", "Pen name is not correct"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_product_information_visible_C44672672(self):
        self.fc.swipe_window(direction="down",distance=8)
        assert bool(self.fc.fd["pen_control"].verify_product_information_card_lone_page())is True, "Product information Label is not visible"
        assert bool(self.fc.fd["pen_control"].verify_product_number_on_product_information_card_lone_page())is True, "Product number is not visible"
        self.fc.fd["pen_control"].scroll_to_element("firmware_version_on_product_information_card_lone_page")
        assert bool(self.fc.fd["pen_control"].verify_serial_number_on_product_information_card_lone_page())is True, "Serial number is not visible"
        assert bool(self.fc.fd["pen_control"].verify_firmware_version_on_product_information_card_lone_page())is True, "Firmware version is not visible"
