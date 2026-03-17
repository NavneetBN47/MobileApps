import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Perform_AIC(object):

    #this suite should run on any commercial , consumer device with System must have >=8 GB of RAM platforms

    def test_01_send_query_with_respect_enter_key_C57033748(self):
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified, "HP AI Assistant button is not visible on header"
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(2)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(5)
        self.fc.fd["aic"].enter_text_in_search_box("What is AI ?")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
        time.sleep(10)
        response_page = self.fc.fd["aic"].verify_response_page()
        assert response_page, "Response page is not displayed after clicking the arrow button"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_02_copy_button_on_response_page_C57033754(self):
        copy_text = self.fc.fd["aic"].get_copy_text()
        assert copy_text == "Copy", "Copy text is not visible on AIC result page -{}".format(copy_text)
        self.fc.fd["devicesMFE"].maximize_app()  # Maximize again for focus
        self.fc.fd["devicesMFE"].maximize_app()  # Maximize again for focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(5)
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["aic"].click_copy_button()

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_stop_icon_button_C57033753(self):
        self.fc.reset_hp_application()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(2)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].enter_text_in_search_box("How can I connect external device?")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_ask_me_anything_searchbox_arrow_button_ltwo()
        self.fc.fd["aic"].click_stop_icon_button_ltwo()
        time.sleep(10)
        button_enabled = self.fc.fd["aic"].is_arrow_button_enabled()
        assert button_enabled == 'true', "Text box arrow is still disabled after entering text"

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_relaunch_C57033755(self):
        #previous script is closing myHP app, so relaunching it here and not repeating the same steps again
        self.fc.close_myHP()
        self.fc.launch_myHP()
        time.sleep(5)
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified, "HP AI Assistant button is not visible on header"
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        home_text = self.fc.fd["aic"].get_hello_text()
        assert home_text == "Hello", "Hello text is not visible on AIC home page -{}".format(home_text)
        how_can_i_help_you_text = self.fc.fd["aic"].get_how_can_i_help_you_text()
        assert how_can_i_help_you_text == "How can I help you today?", "How can I help you text is not visible on AIC home page - {}".format(how_can_i_help_you_text)
        wheel_of_fun_present = self.fc.fd["aic"].verify_wheel_of_fun_present_root_page()
        assert wheel_of_fun_present, "Wheel of Fun is not present on AIC home page"        

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_previous_data_stored_on_response_C57033756(self):
        self.fc.close_myHP()
        self.fc.launch_myHP()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(2)
        self.fc.fd["aic"].enter_text_in_search_box("What is AI ?")
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_aic_window(2)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
        time.sleep(10)
        response_page = self.fc.fd["aic"].verify_response_page()        
        assert response_page, "Response page is not displayed after clicking the arrow button"
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_aic_window(7)
        self.fc.fd["aic"].enter_text_in_search_box("How to turn on my wifi ?")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
        time.sleep(10)
        self.fc.fd['aic'].scroll_up_down(direction="down", distance=1)
        response_page = self.fc.fd["aic"].verify_response_page()        
        assert response_page, "Response page is not displayed after clicking the arrow button"

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_intent_titles_C57033759(self):
        self.fc.reset_hp_application()
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(2)
        self.fc.fd["aic"].enter_text_in_search_box("How to turn on my wifi ?")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
        time.sleep(10)
        intent_title = self.fc.fd["aic"].get_response_intent_title()        
        assert intent_title == "I found some resources that might help...", "AI Response Title is not correct - {}".format(intent_title)
        self.fc.close_myHP()  