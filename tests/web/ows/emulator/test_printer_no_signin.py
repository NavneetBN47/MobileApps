import pytest
import time

pytest.app_info = "OWS"

class Test_Printer_NO_Signin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_emulator_init):
        self = self.__class__
        self.driver, self.ows_emulator, self.config_option, *_ = ows_emulator_init
        self.url = self.driver.get_current_url()
        
    def test_printer_no_signin_back_to_account_01(self, ows_test_setup_no_signin, clean_up):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        
        # click Skip account activation link
        self.ows_fc.flow["ucde_safety_net"].click_skip_account_activation()
        
        # click Back to account button
        self.ows_fc.flow["ucde_safety_net"].click_back_to_account_btn()
        
        # assert load account page is visible
        assert self.ows_fc.flow["ucde_safety_net"].verify_load_account_visible()
        
        # clean_up and back to home page
        clean_up(self.url)
        
    def test_printer_no_signin_create_account_02(self, ows_test_setup_no_signin, clean_up):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        
        # click create account button
        self.ows_fc.flow["ucde_safety_net"].click_create_account()
        
        # assert load account page is visible
        assert self.ows_fc.flow["ucde_safety_net"].verify_load_account_visible()
        
        # clean_up and back to home page
        clean_up(self.url)
        
    def test_verify_printer_no_signin_readmore_03(self, ows_test_setup_no_signin, clean_up):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        
        # click Read More link
        self.ows_fc.flow["ucde_safety_net"].click_read_more()
        
        # click Read More OK button
        self.ows_fc.flow["ucde_safety_net"].click_read_more_ok()
        
        # clean_up and back to home page
        clean_up(self.url)
        
    def test_printer_no_signin_sign_in_04(self, ows_test_setup_no_signin, clean_up):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        
        # click create account button
        self.ows_fc.flow["ucde_safety_net"].click_sign_in()
        
        # assert load account page is visible
        assert self.ows_fc.flow["ucde_safety_net"].verify_load_account_visible()
        
        # clean_up and back to home page
        clean_up(self.url)
    
    def test_printer_no_signin_skip_account_activation_05(self, ows_test_setup_no_signin, clean_up):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        
        # click Skip account activation link
        self.ows_fc.flow["ucde_safety_net"].click_skip_account_activation()
        
        # click Skip account activation link again
        self.ows_fc.flow["ucde_safety_net"].click_skip_warrenty_and_account_activation()
        
        # assert load paper is visible
        assert self.ows_fc.flow["ucde_safety_net"].verify_load_paper_visible()
        
        # clean_up and back to home page
        clean_up(self.url)