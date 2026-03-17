import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Perform_AIC(object):

    # this suite should run on any commercial , consumer device with System must have >=8 GB of RAM platforms
    def test_01_fusion_service_stopping_C57033758(self):
        self.fc.close_myHP()
        self.fc.stop_hp_hsaserivce()
        time.sleep(5)
        self.fc.launch_myHP_and_skip_fuf()
        self.fc.reopen_hp_app_for_blank_screen()
        time.sleep(5)
        button_verified = self.fc.fd["aic"].verify_aic_app_in_lzero_header()
        assert button_verified == False, "HP AI Assistant button is visible on header"
        time.sleep(5)
        self.fc.close_myHP()
        time.sleep(5)
        self.fc.start_hp_hsaserivce()
        time.sleep(10)
        self.fc.launch_myHP_and_skip_fuf()
        time.sleep(5)
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified, "HP AI Assistant button is not visible on header"

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_wheel_of_fun_C57033744(self):
        self.fc.reset_hp_application()
        time.sleep(5)
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified, "HP AI Assistant button is not visible on header"
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(5)
        time.sleep(5)
        self.fc.fd["aic"].click_wheel_of_fun_item_on_home_page("wheel_of_fun_item_on_home_page")
        time.sleep(5)
        intent_title = self.fc.fd["aic"].get_response_intent_title()
        logging.info(f"Retry result: {intent_title}")
        assert intent_title, "AI Response Title is not correct - {}".format(intent_title)

        for _ in range(4):
            self.fc.fd["aic"].click_wheel_of_fun_item_on_result_page("wheel_of_fun_item_on_result_page")
            time.sleep(5)
            intent_title = self.fc.fd["aic"].get_response_intent_title()
            logging.info(f"Retry result: {intent_title}")
            assert intent_title, "AI Response Title is not correct - {}".format(intent_title)
            time.sleep(2)

    def test_03_system_control_performance_mode_radio_button_C57297358(self):
        self.fc.reset_hp_application()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(2)
        self.fc.fd["aic"].enter_text_in_search_box("Set/Turn on performance mode")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
        time.sleep(10)
        response_page = self.fc.fd["aic"].get_response_intent_title()
        assert response_page, "AI Response Title is not correct after retry - {}".format(response_page)
        power_mode = self.fc.get_system_control_mode()
        logging.info(f"Power mode detected: {power_mode}")
        assert "Best Performance" == power_mode, "Power mode is not set to Best Performance, current mode: {}".format(power_mode)

    def test_04_system_control_balanced_mode_radio_button_C57297420(self):
        self.fc.reset_hp_application()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(5)
        self.fc.fd["aic"].enter_text_in_search_box("Set/Turn on Balanced mode")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_ask_me_anything_searchbox_arrow_button_ltwo()
        response_page = self.fc.fd["aic"].get_response_intent_title()
        assert response_page, "AI Response Title is not correct after retry - {}".format(response_page)
        power_mode = self.fc.get_system_control_mode()
        logging.info(f"Power mode detected: {power_mode}")
        assert "Balanced" == power_mode, "Power mode is not set to Balanced, current mode: {}".format(power_mode)

    def test_05_system_control_power_saver_mode_radio_button_C57297418(self):
        self.fc.reset_hp_application()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(5)
        self.fc.fd["aic"].enter_text_in_search_box("Set/Turn on power saver mode")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_ask_me_anything_searchbox_arrow_button_ltwo()
        response_page = self.fc.fd["aic"].get_response_intent_title()
        assert response_page, "AI Response Title is not correct after retry - {}".format(response_page)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(5)        
        # Platform-specific search box inputs
        platform_inputs = {
            'snowwhite': "6",
            'turbine': "5", 
            'divinity': "5",
            'testudo': "3"
        }
        
        platform_key = self.platform.lower()
        if platform_key in platform_inputs:
            logging.info(f"Platform {self.platform.lower()}")
            search_input = platform_inputs[platform_key]
            self.fc.fd["aic"].enter_text_in_search_box(search_input)
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["aic"].click_ask_me_anything_searchbox_arrow_button_ltwo()
            power_mode = self.fc.get_system_control_mode()
            logging.info(f"Power mode detected: {power_mode}")
            assert "Best Power Efficiency" == power_mode, "Best Power Efficiency mode is not set to Power Efficiency, current mode: {}".format(power_mode)
        else:
            pytest.skip(f"Platform '{platform_key}' not supported for this test")
        self.fc.close_myHP()