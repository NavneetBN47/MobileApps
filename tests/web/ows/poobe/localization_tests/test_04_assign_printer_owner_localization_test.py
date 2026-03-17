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
        self.spec_locale = self.locale.split("_")
        self.spec_locale = ''.join(self.spec_locale[1]+"-"+self.spec_locale[0].upper())
        if self.biz_model == "E2E":
            self.key = self.biz_model+"_activate"
        if self.biz_model == "Flex":
            self.key = self.biz_model+"_connect"
        self.file_key = ma_misc.load_json_file("resources/test_data/poobe/spec_key.json")
        
        self.sim_printer_info = ows_utility.create_simulated_gen2_printer(stack=self.stack, profile=self.printer_profile, biz_model=self.biz_model, offer=0)
        
        """
        Currently only Implemented for E2E /activate
        """
    
    def test_01_assign_printer_organization(self):
        if self.biz_model == "Flex":
            pytest.skip()
        file_name = ma_misc.web_localization_path_builder(self.driver, self.file_key["portal_oobe"]["assign_organization_page"][self.key])
        file_name = file_name.replace("bg-BG", self.spec_locale)
        spec_data = self.fc.fd["assign_printer_organization"].get_key_modified_dictionary_from_spec(file_name)
        self.fc.landing_page(biz = self.biz_model)
        self.fc.fd["value_prop_page"].verify_landing_page_create_account_btn()
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.fc.fd["pairing_code_page"].verify_pairing_code_screen()
        tess = self.driver.get_current_url().replace("us/en", self.locale.replace("_", "/").lower())
        self.driver.navigate(tess)
        if self.driver.check_if_browser_alert_present(raise_e=False):
            self.driver.accept_or_dismiss_browser_alert(accept=True)
        
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.sim_printer_info, biz = self.biz_model)
        self.fc.select_how_to_setup_printer_company_or_personal(self.printer_profile, self.biz_model, self.printer_type)
        self.fc.fd["assign_printer_organization"].verify_assign_printer_owner_page()
        web_str_object = ["header","subheader","organization_labels_name", 
                          "organization_labels_invalid_name_text","organization_labels_country",
                          "organization_labels_country_error_text","organization_labels_description","agreement_terms",
                          "continue_button_text"]
        res = []
        for i in web_str_object:
            if i == "organization_labels_name":
                self.driver.send_keys("organization_name_box", "<>.#")
                result = self.fc.fd["assign_printer_organization"].string_validation(spec_data, i, raise_e= False)
            elif  i == "organization_labels_country_error_text":
                self.fc.fd["assign_printer_organization"].select_organization_country_region_seclector()
                self.fc.fd["assign_printer_organization"].select_trinidad_and_tobago_country_region()
                result = self.fc.fd["assign_printer_organization"].string_validation(spec_data, i, raise_e= False)
            elif i == "continue_button_text":
                self.fc.fd["assign_printer_organization"].select_organization_country_region_seclector()
                self.fc.fd["assign_printer_organization"].select_united_states_country_region()
                self.driver.send_keys("organization_name_box", "random_valid_name")
                result = self.fc.fd["assign_printer_organization"].string_validation(spec_data, i, raise_e= False)
            else:
                result = self.fc.fd["assign_printer_organization"].string_validation(spec_data, i, raise_e= False)
            res.append(result)
        logging.info("Current URL: {}".format(self.driver.get_current_url()))
        ows_utility.remove_printer(self.sim_printer_info['serial_number'])
        time.sleep(90) # Adding time delay to avoid 500 server error. wpp api will block calls if too many api calls done frequently.
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        assert False not in res, "one or multiple string validation failed Check test log for details"