import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_UI(object):

    #this suite for Roo pen on Machu tv
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_roo_pen_commercial_ui_C52240402(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        self.fc.fd["devicesMFE"].click_pen_card()
        #Header with the pen name 
        pen_name = self.fc.fd["pen_control"].get_nested_pen_name_lone_page()
        assert pen_name == "HP Nested Pen", f"Pen name expected: HP Nested Pen, actual:{pen_name}"
        #2) Pen image should be displayed in the right side of the UI
        assert bool(self.fc.fd["pen_control"].verify_pen_image_lone_page()), "Pen image is not displayed"
        #3) Customize buttons card
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        #4) Radial menu card
        assert self.fc.fd["pen_control"].verify_radial_menu_commercial(), "Radial Menu is not available"
        #5) One step inking card
        #6) Pen for external display card
        assert self.fc.fd["pen_control"].verify_external_display_card(), "External Display Card is not available"
        self.fc.fd["pen_control"].scroll_to_element("pen_sensitivity_card")
        #7) Pen sensitivity card
        assert self.fc.fd["pen_control"].verify_pen_sensitivity_card(), "Pen Sensitivity Card is not available"
        #8) Pen settings tab with 2 options:
        #a) Alert when pen is not detected with a toggle switch
        #b) Power saving when pen is idle with a toggle switch
        self.fc.fd["pen_control"].scroll_down_to_element("product_information_card_lone_page")
        #9) Product information card
        assert bool(self.fc.fd["pen_control"].verify_product_information_card_lone_page()) is True, "Product Information Card is not available"
        self.fc.fd["pen_control"].scroll_down_to_element("restore_default_button_lone_page")
        #10) Restore default button
        assert self.fc.fd["pen_control"].get_restore_default_button_lone_page() == "Restore defaults", "Restore defaults button is not visible"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_roo_pen_commercial_C52235900(self):
        self.fc.fd["pen_control"].scroll_to_element("pen_control_one_step_ink_card_image_lone_page")
        assert self.fc.fd["pen_control"].get_nested_pen_name_lone_page() == "HP Nested Pen", "Pen name is not correct"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_one_step_inking_card_C53039381(self):
        self.fc.fd["pen_control"].scroll_to_element("pen_control_one_step_ink_card_image_lone_page")
        assert bool(self.fc.fd["pen_control"].verify_pen_control_one_step_ink_card_image_ltwo_page()) is True, "One step inking card is not available"
        self.fc.fd["pen_control"].click_one_step_inking_card()
        #Select any action from the action list of one step inking---The selected action should be displayed in the one step inking card in L1 page.(select screen snipping action for example)
        self.fc.fd["pen_control"].click_one_step_inking_screen_snipping()
        self.fc.fd["pen_control"].click_my_pen_button()
        self.fc.fd["pen_control"].scroll_to_element("pen_control_one_step_ink_subheader_text_lone_page")
        assert "Screen Snipping" in self.fc.fd["pen_control"].get_pen_control_one_step_ink_subheader_text_lone_page(), "One step inking card sub header is not visible"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_one_step_inking_action_list_C53039927(self):
        assert "One step inking" in self.fc.fd["pen_control"].get_one_step_inking_card(), "One step inking card is not visible"
        self.fc.fd["pen_control"].click_one_step_inking_card()
        assert bool(self.fc.fd["pen_control"].verify_one_step_inking_pen_menu()) is True, "One step inking card-pen menu is not available"
        assert bool(self.fc.fd["pen_control"].verify_one_step_inking_one_note()) is True, "One step inking card - one note is not available"
        assert bool(self.fc.fd["pen_control"].verify_one_step_inking_ms_white_board()) is True, "One step inking card- ms white board is not available"
        assert bool(self.fc.fd["pen_control"].verify_one_step_inking_snipping_tool()) is True, "One step inking card- snipping tool is not available"
        assert bool(self.fc.fd["pen_control"].verify_one_step_inking_open_app()) is True, "One step inking card- open app is not available"
        assert bool(self.fc.fd["pen_control"].verify_one_step_inking_disabled()) is True, "One step inking card- disabled is not available"
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_module_launch_from_windows_settings_C53020053(self):
        self.fc.close_myHP()# close app require to go to setting and verify next step verification
        self.fc.fd["pen_control"].click_more_settings_via_blutooth_devices()
        time.sleep(5)
        assert self.fc.fd["pen_control"].get_customize_buttons_text() == "Customize buttons", "Customize button Label is not visible"
        self.fc.uninstall_app()
        self.fc.fd["pen_control"].click_more_settings_via_blutooth_devices()
        assert bool(self.fc.fd["pen_control"].verify_get_an_app_open_this_hpx_link_popup()) is True, "Get an app to open this hpx link popup is not visible"
