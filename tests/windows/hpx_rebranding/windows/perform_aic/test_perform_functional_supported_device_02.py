import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Perform_AIC(object):

       
    #this suite should run on any commercial , consumer device with System must have >=8 GB of RAM platforms
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_keyboard_dismiss_altf4_C57033768(self):
        self.fc.fd["aic"].press_keyboard_to_close_app()
        time.sleep(5)

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_queries_to_same_topic_C57033752(self):
        self.fc.launch_myHP_and_skip_fuf()
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified, "HP AI Assistant button is not visible on header"
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        # Check if system brightness is 0 and set to 100 if needed for better visibility.
        # Note : this step is not in test rail but I added it in case if any other test case has decreased the system brightness it might cause the failure
        current_brightness = int(self.fc.get_system_brightness_value())
        if current_brightness == 0:
            self.fc.driver.ssh.send_command('(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, 100)', timeout=30)
            time.sleep(2)
        self.fc.fd["aic"].click_aic_window(5)
        time.sleep(5)
        self.fc.fd["aic"].enter_text_in_search_box("decrease brightness by 10 % ")
        self.fc.fd["aic"].get_focus_on_app("ask_me_anything_searchbox_arrow_button_ltwo")
        time.sleep(10)
        intent_title = self.fc.fd["aic"].get_response_intent_title()
        assert intent_title == "Sure! Let me adjust that for you", "AI Response Title is not correct - {}".format(intent_title)
        brightness_pattern_valid = self.fc.fd["aic"].validate_brightness_response_pattern()
        assert brightness_pattern_valid, "AI Response Results don't match expected brightness pattern"
        self.fc.fd["aic"].click_search_box_result_page(7)
        time.sleep(5)
        self.fc.fd["aic"].enter_text_in_search_box("decrease brightness by 10 % ")
        self.fc.fd["aic"].get_focus_on_app("ask_me_anything_searchbox_arrow_button_ltwo")
        time.sleep(10)
        intent_title = self.fc.fd["aic"].get_response_intent_title()
        assert intent_title == "Sure! Let me adjust that for you", "AI Response Title is not correct - {}".format(intent_title)
        brightness_pattern_valid = self.fc.fd["aic"].validate_brightness_response_pattern()
        assert brightness_pattern_valid, "AI Response Results don't match expected brightness pattern"
        self.fc.fd["aic"].click_search_box_result_page(7)
        self.fc.fd["aic"].enter_text_in_search_box("increase brightness by 20 % ")
        self.fc.fd["aic"].get_focus_on_app("ask_me_anything_searchbox_arrow_button_ltwo")
        time.sleep(10)
        intent_title = self.fc.fd["aic"].get_response_intent_title()
        assert intent_title == "Sure! Let me adjust that for you", "AI Response Title is not correct - {}".format(intent_title)
        brightness_pattern_valid = self.fc.fd["aic"].validate_brightness_response_pattern()
        assert brightness_pattern_valid, "AI Response Results don't match expected brightness pattern"
        self.fc.fd["aic"].focus_collapse_expand_chevron_lthree_page()
        self.fc.fd["aic"].get_focus_on_app("aic_windows")
        self.fc.fd["aic"].click_collapse_expand_chevron_lthree_page()
        response_card_valid = self.fc.fd["aic"].validate_different_response_card()
        assert response_card_valid, "AI Response Card is in same card instead of 2 cards"

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_verify_aic_visibilty_on_supported_platform_C57033740(self):
        self.fc.reset_hp_application()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        home_text = self.fc.fd["aic"].get_hello_text()
        assert home_text == "Hello", "Hello text is not visible on AIC home page -{}".format(home_text)
        how_can_i_help_you_text = self.fc.fd["aic"].get_how_can_i_help_you_text()
        assert how_can_i_help_you_text == "How can I help you today?", "How can I help you text is not visible on AIC home page - {}".format(how_can_i_help_you_text)
        wheel_of_fun_present = self.fc.fd["aic"].verify_wheel_of_fun_present_root_page()
        assert wheel_of_fun_present, "Wheel of Fun is not present on AIC home page"

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_input_prompt_C57033745(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        assert self.fc.fd["aic"].is_arrow_button_enabled() == 'false', "Text box arrow is enabled by default"
        self.fc.fd["aic"].enter_text_in_search_box("How to turn on my wifi ?")

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_enabling_of_send_query_button_C57033746(self):
        time.sleep(5)
        assert self.fc.fd["aic"].is_arrow_button_enabled() == 'true', "Text box arrow is still disabled after entering text"

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_send_query_behaviour_with_send_with_mouse_to_click_C57033747(self):
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_aic_window(5)
        time.sleep(5)
        self.fc.fd["aic"].get_focus_on_app("ask_me_anything_searchbox_arrow_button_ltwo")
        time.sleep(10)
        response_page = self.fc.fd["aic"].verify_response_page()
        assert response_page, "Response page is not displayed after clicking the arrow button"
        self.fc.close_myHP()    