import time
import pytest

pytest.app_info = "OWS"

class Test_OWS_Yeti(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc, self.yeti_fc, self.status_and_login_info = ows_test_setup
        if self.status_and_login_info: ows_status, self.access_token, self.id_token = self.status_and_login_info

    def test_01_yeti_flow(self):
        self.yeti_fc.navigate_yeti(self.profile, self.biz_model)

        #test_04_complete_activation 
        self.ows_printer.login(self.access_token, self.id_token)
        redirect_url_1 = self.ows_printer.get_console_data("PUT - ForceSignInHp")["params"]["continuationUrl"]+ "&completionCode=0"
        self.driver.switch_window()
        self.driver.navigate(redirect_url_1)
        self.ows_printer.send_action("SignInHp")
        redirect_url = self.ows_printer.get_console_data("GET - SignInHp")["params"]["continuationUrl"] + "&completionCode=0"
        self.driver.switch_window()
        self.driver.navigate(redirect_url)
        time.sleep(10)
        #self.ows_printer.click_enable_ws()

        #test_05_verify_ucde_privacy
        self.yeti_fc.flow["ucde_privacy"].skip_ucde_privacy_screen(timeout=20)

        #test_06_verify_ucde_activation
        self.yeti_fc.flow["ucde_activation_success"].verify_ucde_activation_success(timeout=120)
        self.yeti_fc.flow["ucde_activation_success"].click_continue(raise_e=False)
    
        #test_07_verify_instant_ink(self):
        self.yeti_fc.flow["value_proposition"].verify_value_proposition_page(timeout=40)
        self.yeti_fc.flow["value_proposition"].skip_value_proposition_page()
        time.sleep(100)