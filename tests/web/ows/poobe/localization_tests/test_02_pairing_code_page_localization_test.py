import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ows import ows_utility
import logging
import time
pytest.app_info = "POOBE"

class Test_01_Portal_OOBE_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.printer_type = request.config.getoption("--printer-operation")
        self.stack = request.config.getoption("--stack")
        self.locale = request.config.getoption("--locale")
        self.invalid_code = "ssdfsdgs"
        self.spec_locale = self.locale.split("_")
        self.spec_locale = ''.join(self.spec_locale[1]+"-"+self.spec_locale[0].upper())
        if self.biz_model == "E2E":
            self.key = self.biz_model+"_activate"
        if self.biz_model == "Flex":
            self.key = self.biz_model+"_connect"
        self.file_key = ma_misc.load_json_file("resources/test_data/poobe/spec_key.json")
        self.pairing_code_page = self.fc.fd["pairing_code_page"]
        self.poobe_error_modal = self.fc.fd["portal_error_modal"]

        self.sim_printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        
        """
        Currently only Implemented for E2E /activate and Flex /connect
        """
    
    def test_01_pairing_code_page(self):
        file_name = ma_misc.web_localization_path_builder(self.driver, self.file_key["portal_oobe"]["pairing_code_page"][self.key])
        file_name = file_name.replace("bg-BG", self.spec_locale)
        spec_data = self.pairing_code_page.get_key_modified_dictionary_from_spec(file_name)
        self.fc.landing_page(biz = self.biz_model)
        self.fc.fd["value_prop_page"].verify_landing_page_create_account_btn()
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.pairing_code_page.verify_pairing_code_screen()
        tess = self.driver.get_current_url().replace("us/en", self.locale.replace("_", "/").lower())
        self.driver.navigate(tess)
        if self.driver.check_if_browser_alert_present(raise_e=False):
            self.driver.accept_or_dismiss_browser_alert(accept=True)
        self.pairing_code_page.verify_pairing_code_screen()
        res=[]
        res.append(self.pairing_code_page.string_validation(spec_data, "header", raise_e= False))
        res.append(self.pairing_code_page.string_validation(spec_data, "description", raise_e=False))
        res.append(self.pairing_code_page.string_validation(spec_data, "pairing_input_label", raise_e=False))
        res.append(self.pairing_code_page.string_validation(spec_data, "notes", raise_e=False))
        self.pairing_code_page.click_cant_find_pairing_code_btn()
        res.append(self.pairing_code_page.string_validation(spec_data, "can_t_find_pairing_code_modal_body", raise_e=False))
        res.append(self.pairing_code_page.string_validation(spec_data, "can_t_find_pairing_code_modal_close_button_text", raise_e=False))
        self.pairing_code_page.click_cant_find_pairing_code_modal_close_btn()
        self.pairing_code_page.input_pairing_code(self.invalid_code)
        self.pairing_code_page.click_continue_btn()
        res.append(self.pairing_code_page.string_validation(spec_data, "invalid_code_text", raise_e=False))
        self.pairing_code_page.click_continue_btn()
        self.pairing_code_page.click_continue_btn()
        self.pairing_code_page.click_continue_btn()
        # For retry_warning_text and retry_limit_text two separate keys are used in spec file
        warning_msg = spec_data['invalid_code_text']+' '+spec_data["retry_warning_text"]
        limit_msg = spec_data['invalid_code_text']+' '+spec_data["retry_limit_text"]
        res.append(self.pairing_code_page.validate_retry_warning_string(warning_msg))
        self.pairing_code_page.click_continue_btn()
        res.append(self.pairing_code_page.validate_retry_limit_string(limit_msg))
        logging.info("Current URL: {}".format(self.driver.get_current_url()))
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        assert False not in res, "one or multiple string validation failed Check test log for details"

    def test_02_pairing_code_page_expired_error(self):
        file_name = ma_misc.web_localization_path_builder(self.driver, self.file_key["portal_oobe"]["pairing_code_page_expired_code"][self.key])
        file_name = file_name.replace("bg-BG", self.spec_locale)
        spec_data = self.pairing_code_page.get_key_modified_dictionary_from_spec(file_name)
        self.pairing_code = ows_utility.get_pairing_code(self.printer_profile, stack = self.stack, post_card= self.sim_printer_info['claim_postcard'], finger_print=self.sim_printer_info['fingerprint'], 
                                                        model_number=self.sim_printer_info['model_number'],uuid= self.sim_printer_info['uuid'])
        self.pairing_code_page.verify_pairing_code_screen()
        self.p_oobe.verify_left_panel_printer_container(self.biz_model)
        time.sleep(300) # Takes about 5 mins for code to Expired. A random code does not work to cause a Expired Code error
        self.pairing_code_page.input_pairing_code(code=self.pairing_code['user_code'])
        self.pairing_code_page.click_continue_btn()
        res=[]
        res.append(self.poobe_error_modal.string_validation(spec_data, "header", raise_e=False))
        res.append(self.poobe_error_modal.string_validation(spec_data, "body", raise_e=False))
        res.append(self.poobe_error_modal.string_validation(spec_data, "primary_button_text", raise_e=False))
        logging.info("Current URL: {}".format(self.driver.get_current_url()))
        assert False not in res, "one or multiple string validation failed for Expired Code Error modal Check test log for details"