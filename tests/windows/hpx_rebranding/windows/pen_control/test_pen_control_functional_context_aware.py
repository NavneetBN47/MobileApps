import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_PenControl_UI(object):

    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_context_aware_availability_on_pen_module_C52990436(self):
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        self.fc.fd["devicesMFE"].click_pen_card()
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.navigate_to_pen_control_lone_page_and_click_restore_default_btn()
        self.fc.swipe_window(direction="up", distance=4)
        #Consumer Only
        self.fc.fd["pen_control"].click_customize_buttons()
        assert self.fc.fd["pen_control"].verify_add_button(), "Add button is not available"
        assert self.fc.fd["pen_control"].verify_context_aware_all_app_button(), "Context Aware All App button is not available"
        self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()

        #Commercial Only
        if self.platform.lower() in ("machu13x","ernesto","masadaNX", "masdanxsku4"):
            self.fc.swipe_window(direction="down", distance=4)
            self.fc.fd["pen_control"].click_radial_menu_button()
            assert self.fc.fd["pen_control"].verify_add_button(), "Add button is not available"
            assert self.fc.fd["pen_control"].verify_context_aware_all_app_button(), "Context Aware All App button is not available"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            self.fc.swipe_window(direction="down", distance=4)
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            assert self.fc.fd["pen_control"].verify_add_button(), "Add button is not available"
            assert self.fc.fd["pen_control"].verify_context_aware_all_app_button(), "Context Aware All App button is not available"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_click_cancel_on_adding_application_context_aware_C52992701(self):
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_add_button()
        self.fc.fd["pen_control"].click_access_on_application_list_dialog()
        self.fc.fd["pen_control"].click_pen_cancel_onpopup_window_page()
        assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is False, "Access app was added"
        self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()

        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["pen_control"].click_radial_menu_button()
        self.fc.fd["pen_control"].click_add_button()
        self.fc.fd["pen_control"].click_access_on_application_list_dialog()
        self.fc.fd["pen_control"].click_pen_cancel_onpopup_window_page()
        assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is False, "Access app was added"
        self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["pen_control"].click_pen_sensitivity_card()
        self.fc.fd["pen_control"].click_add_button()
        self.fc.fd["pen_control"].click_access_on_application_list_dialog()
        self.fc.fd["pen_control"].click_pen_cancel_onpopup_window_page()
        assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is False, "Access app was added"
        self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()


    @pytest.mark.function
    @pytest.mark.ota
    def test_03_pen_configuration_while_adding_new_application_C52992557(self):
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["pen_control"].verify_customize_buttons()

        if self.platform.lower() in ("machu13x","ernesto","masadaNX", "masdanxsku4"):
            assert self.fc.fd["pen_control"].verify_radial_menu_commercial(), "Radial Menu is not available"
            assert self.fc.fd["pen_control"].verify_external_display_card(), "External Display Card is not available"
            assert self.fc.fd["pen_control"].verify_pen_sensitivity_card(), "Pen Sensitivity Card is not available"
        
        if self.platform.lower() in ("machu13x","ernesto"):
            assert self.fc.fd["pen_control"].verify_external_display_card_context_aware(),  "External Display Card is not context aware"
            external_context_aware_text = self.fc.fd["pen_control"].get_external_display_card_context_aware_text()

            assert  self.fc.fd["pen_control"].verify_radial_menu_card_context_aware(),  "Radial Menu Card is not context aware"
            radial_context_aware_text = self.fc.fd["pen_control"].get_radial_menu_card_context_aware_text()
            

        self.fc.fd["pen_control"].click_customize_buttons()
        self.fc.fd["pen_control"].click_add_button()
        self.fc.fd["pen_control"].click_access_on_application_list_dialog()
        self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
        self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
        self.fc.swipe_window(direction="down", distance=4)
        if self.platform.lower() in ("machu13x","ernesto","masadaNX", "masdanxsku4"):
            self.fc.fd["pen_control"].click_radial_menu_button()
            self.fc.fd["pen_control"].click_add_button()
            self.fc.fd["pen_control"].click_access_on_application_list_dialog()
            self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            self.fc.swipe_window(direction="down", distance=4)
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            self.fc.fd["pen_control"].click_add_button()
            self.fc.fd["pen_control"].click_access_on_application_list_dialog()
            self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["pen_control"].verify_customize_buttons(), "Customize buttons is not available"

        if self.platform.lower() in ("machu13x","ernesto","masadaNX", "masdanxsku4"):
            assert self.fc.fd["pen_control"].verify_radial_menu_commercial(), "Radial Menu is not available"
            assert self.fc.fd["pen_control"].verify_external_display_card(), "External Display Card is not available"
            assert self.fc.fd["pen_control"].verify_pen_sensitivity_card(), "Pen Sensitivity Card is not available"
        
        if self.platform.lower() in ("machu13x","ernesto"):
            assert self.fc.fd["pen_control"].verify_external_display_card_context_aware(),  "External Display Card is not context aware"
            assert external_context_aware_text == self.fc.fd["pen_control"].get_external_display_card_context_aware_text(), "External Display Card context aware text is not matching"

            assert  self.fc.fd["pen_control"].verify_radial_menu_card_context_aware(),  "Radial Menu Card is not context aware"
            assert radial_context_aware_text == self.fc.fd["pen_control"].get_radial_menu_card_context_aware_text(), "Radial Menu Card context aware text is not matching"

    
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_adding_an_application_which_is_already_added_to_context_aware_C52994236(self):
        #consumer only
        if self.platform.lower() in ("willie"):
            self.fc.fd["pen_control"].click_customize_buttons()
            upper_barrel_button_text = self.fc.fd["pen_control"].get_right_click_text_commercial()
            lower_barrel_button_text = self.fc.fd["pen_control"].get_lower_barrel_button_erase_text()
            for i in range(6):
                self.fc.fd["pen_control"].click_add_button()
                assert self.fc.fd["pen_control"].get_customize_button_add_application_text_on_add_application_popup() == "Add Application" , "add application title on add application popup not available"
                self.fc.fd["pen_control"].click_access_on_application_list_dialog()
                self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
                assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is True, "Access app was not added"
                assert bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is True, "Access app was not selected"
                #verify upper barrel button action
                assert self.fc.fd["pen_control"].get_right_click_text_commercial() == upper_barrel_button_text, "upper barrel button action not available"
                assert self.fc.fd["pen_control"].get_lower_barrel_button_erase_text() == lower_barrel_button_text , "lower barrel button action not available"
                #verify lower barrel button action

        #commercial only
        if self.platform.lower() in ("machu13x","ernesto","masadaNX", "masdanxsku4"):
            self.fc.fd["pen_control"].click_customize_buttons()
            upper_barrel_button_text = self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page()
            lower_barrel_button_text = self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page()
            for i in range(6):
                self.fc.fd["pen_control"].click_add_button()
                assert self.fc.fd["pen_control"].get_customize_button_add_application_text_on_add_application_popup() == "Add Application" , "add application title on add application popup not available"
                self.fc.fd["pen_control"].click_access_on_application_list_dialog()
                self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
                assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is True, "Access app was not added"
                assert bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is True, "Access app was not selected"
                assert self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page() == upper_barrel_button_text, "upper barrel button action not available"
                assert self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page() == lower_barrel_button_text , "lower barrel button action not available"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            self.fc.fd["pen_control"].click_radial_menu_button()
            slice1_text = self.fc.fd["pen_control"].get_pen_control_redial_menu_slice1_action_l_ltwo_page()
            for i in range(6):
                self.fc.fd["pen_control"].click_add_button()
                assert self.fc.fd["pen_control"].get_customize_button_add_application_text_on_add_application_popup() == "Add Application" , "add application title on add application popup not available"
                self.fc.fd["pen_control"].click_access_on_application_list_dialog()
                self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
                assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is True, "Access app was not added"
                assert bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is True, "Access app was not selected"
                assert self.fc.fd["pen_control"].get_pen_control_redial_menu_slice1_action_l_ltwo_page() == slice1_text, "next track action not available"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()
            self.fc.swipe_window(direction="down", distance=4)
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            pressure_slider_value=self.fc.fd["pen_control"].get_pen_sensitivity_pressure_slider_value()
            for i in range(6):
                self.fc.fd["pen_control"].click_add_button()
                assert self.fc.fd["pen_control"].get_customize_button_add_application_text_on_add_application_popup() == "Add Application" , "add application title on add application popup not available"
                self.fc.fd["pen_control"].click_access_on_application_list_dialog()
                self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
                assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is True, "Access app was not added"
                assert bool(self.fc.fd["pen_control"].is_access_app_on_carousel_selected()) is True, "Access app was not selected"
                assert self.fc.fd["pen_control"].get_pen_sensitivity_pressure_slider_value() == pressure_slider_value, "pressure slider value not available"
            self.fc.fd["display_control"].click_back_arrow_to_navigate_to_previous_page()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_deleting_a_profile_application_which_was_added_to_ca_from_non_pen_control_page_C53000172(self):
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        self.fc.fd["audio"].click_add_application_button()
        self.fc.fd["audio"].search_apps_on_search_frame("clock")
        time.sleep(2)
        self.fc.fd["audio"].click_searched_app_on_search_frame()
        time.sleep(3)
        self.fc.fd["audio"].click_continue_button_on_dialog()
        time.sleep(2)
        self.fc.fd["audio"].click_back_button_on_audio_page()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_pen_card()
        self.fc.fd["pen_control"].click_customize_buttons()
        assert bool(self.fc.fd["context_aware"].verify_clock_app_carousel()) is True,"clock app was not added"
        self.fc.fd["context_aware"].click_clock_app_carousel()
        self.fc.fd["pen_control"].click_delete_profile_btn_on_carousel()
        self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
        assert bool(self.fc.fd["context_aware"].verify_clock_app_carousel()) is False, "calendar app was not deleted"

    @pytest.mark.function
    @pytest.mark.ota
    def test_06_changing_config_in_global_apps_to_check_on_profiles_not_changed_in_custom_applications_C53000343(self):
        #select global application and it's settings
        self.fc.fd["pen_control"].click_context_aware_all_app_button()
        upper_barrel_button_text = self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page()
        assert upper_barrel_button_text == "Universal select", "Universal select is not available"
        lower_barrel_button_text = self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page()
        assert lower_barrel_button_text == "Erase", "Erase is not available"
        self.fc.fd["pen_control"].click_add_button()
        assert self.fc.fd["pen_control"].get_customize_button_add_application_text_on_add_application_popup() == "Add Application" , "add application title on add application popup not available"
        self.fc.fd["pen_control"].click_access_on_application_list_dialog()
        time.sleep(2)
        self.fc.fd["pen_control"].click_pen_continue_onpopup_window_page()
        assert bool(self.fc.fd["pen_control"].verify_access_app_on_carousel()) is True, "Access app was not added"
        self.fc.fd["pen_control"].click_access_app_on_carousel()
        upper_barrel_button_text = self.fc.fd["pen_control"].get_pen_control_customize_btn_upper_barrel_btn_action_ltwo_page()
        assert upper_barrel_button_text == "Universal select", "Universal select is not available"
        lower_barrel_button_text = self.fc.fd["pen_control"].get_pen_control_customize_btn_lower_barrel_btn_action_ltwo_page()
        assert lower_barrel_button_text == "Erase", "Erase is not available"
        self.fc.navigate_to_pen_control_lone_page_and_click_restore_default_btn()
