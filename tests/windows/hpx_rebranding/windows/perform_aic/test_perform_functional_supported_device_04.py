import time
import pytest
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


def assert_ai_prompt_response(self, question_asked=None,index=0, expected_text=""):
    time.sleep(5)
    self.fc.fd["aic"].click_aic_window(7)
    time.sleep(2)
    self.fc.fd["aic"].enter_text_in_search_box(question_asked)
    self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
    self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
    self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
    time.sleep(10)
    if expected_text:        
        self.fc.fd['aic'].scroll_up_down(direction="down", distance=5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_copy_button(index)
        ai_prompt_response = self.fc.get_clipboard_content()
        assert expected_text in ai_prompt_response, "AI Response is not correct - {}".format(ai_prompt_response)
        logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Perform_AIC(object):
    

    #this suite should run on any commercial , consumer device with System must have >=8 GB of RAM platforms
    def test_01_experience_mode_movie_opting_settings_to_be_applied_based_on_serial_numbers_C57033807(self): 
        platform = self.platform.lower()        
        # self.fc.reopen_hp_app_for_blank_screen()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(7)
        time.sleep(2)
        self.fc.fd["aic"].enter_text_in_search_box("Setup my screen for a movie")
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].press_enter_on_arrow_button_ltwo()
        time.sleep(10)
        response_page = self.fc.fd["aic"].get_response_intent_title()
        assert response_page, "AI Response Title is not correct after retry - {}".format(response_page)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        time.sleep(5)
        self.fc.fd["aic"].click_copy_button()
        ai_prompt_response = self.fc.get_clipboard_content()
        options = ai_prompt_response.split("\n")
        logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response.split("\n")}")

        assert_ai_prompt_response(self,"activate all settings",1, "All done! **Movie mode** is now **activated**.")
        logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")

        assert_ai_prompt_response(self,"Setup my screen for a movie")

        assert_ai_prompt_response(self,"1",3, "All done! **Movie mode** is now **activated**.")
        logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")

        assert_ai_prompt_response(self,"Setup my screen for a movie")

        assert_ai_prompt_response(self,"2",5, "All done! **Movie mode** is now **activated**.")
        logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")

        assert_ai_prompt_response(self,"Setup my screen for a movie")

        assert_ai_prompt_response(self,"1,2",7, "All done! **Movie mode** is now **activated**.")
        logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")

        if platform not in ["turbine","divinity"]: # 3rd option is not available on arm or consumer devices
            assert_ai_prompt_response(self,"Setup my screen for a movie")

            assert_ai_prompt_response(self,"3",9, "All done! **Movie mode** is now **activated**.")
            logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")            

            assert_ai_prompt_response(self,"Setup my screen for a movie")

            assert_ai_prompt_response(self,"1,3",11, "All done! **Movie mode** is now **activated**.")
            logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")

            assert_ai_prompt_response(self,"Setup my screen for a movie")

            assert_ai_prompt_response(self,"2,3",13, "All done! **Movie mode** is now **activated**.")
            logging.info(f"AI Prompt Response copied to clipboard: {ai_prompt_response}")
        self.fc.close_myHP()