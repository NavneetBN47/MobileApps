import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Perform_AIC(object):

    #this suite should run on any commercial , consumer device with System must have >=8 GB of RAM platforms

    def test_01_restart_myhp_C57033779(self,request):
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
        assert self.fc.fd["aic"].is_arrow_button_enabled(), "Arrow button is not enabled"
        restart_machine(self, request)        
        self.fc.launch_myHP()
        time.sleep(5)
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified, "HP AI Assistant button is not visible on header"
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(3)
        time.sleep(5)
        home_text = self.fc.fd["aic"].get_hello_text()
        assert home_text == "Hello", "Hello text is not visible on AIC home page -{}".format(home_text)
        how_can_i_help_you_text = self.fc.fd["aic"].get_how_can_i_help_you_text()
        assert how_can_i_help_you_text == "How can I help you today?", "How can I help you text is not visible on AIC home page - {}".format(how_can_i_help_you_text)
