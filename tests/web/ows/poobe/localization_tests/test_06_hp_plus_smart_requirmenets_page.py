import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ows import ows_utility
import logging
import time
import datetime
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
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.connected_printing_services = self.fc.fd["connected_printing_services"]
        self.hp_plus_smart_printer_requirements = self.fc.fd["hp_plus_smart_printer_requirements"]
        self.file_key = ma_misc.load_json_file("resources/test_data/poobe/spec_key.json")
        self.hp_plus_countries = ["au_en","be_fr","be_nl","ca_en","ca_fr","dk_de","de_de","es_es","ee_et","fr_fr",
                                  "hr_hr","ie_en","it_it","lv_lv","lt_lt","lu_fr","hu_hu","mt_en","nl_nl","nz_en",
                                  "no_nb","pl_pl","pt_pt","ro_ro","ch_de","ch_fr","si_si","sk_sk","fi_fi","se_sv",
                                  "gb_en","us_en","at_de","cz_cs","gr_el","bg_bg"]
        
        self.sim_printer_info = ows_utility.create_simulated_gen2_printer(stack=self.stack, profile=self.printer_profile, biz_model=self.biz_model, offer=0)
        
        """
        HP Plus Smart Printer Requirements page only for activate flow and /onboard Flow E2E.
        """
    
    def test_01_iris_firmware_update_notice(self):
        if self.biz_model == "Flex" or self.locale not in self.hp_plus_countries:
            pytest.skip()
        file_name = ma_misc.web_localization_path_builder(self.driver, self.file_key["portal_oobe"]["hp+_smart_requirments_page"]["E2E_activate"])
        file_name = file_name.replace("bg-BG", self.spec_locale)
        spec_data = self.hp_plus_smart_printer_requirements.get_key_modified_dictionary_from_spec(file_name)
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
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.connected_printing_services.verify_connected_printing_services()
        self.connected_printing_services.click_connected_printing_services()
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        self.hp_plus_smart_printer_requirements.verify_hp_plus_smart_printer_requirements_page()
        res =[]
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "header", raise_e=False))
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "content[0]_block_copy_copy", raise_e=False))
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "content[1]_list_item_copy", raise_e=False))
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "content[2]_list_item_copy", raise_e=False))
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "content[3]_list_item_copy", raise_e=False))
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "content[4]_block_copy_copy", raise_e=False))
        res.append(self.hp_plus_smart_printer_requirements.string_validation(spec_data, "confirm_button_text", raise_e=False))
        logging.info("Current URL: {}".format(self.driver.get_current_url()))
        ows_utility.remove_printer(self.sim_printer_info['serial_number'])
        time.sleep(90) # Adding time delay to avoid 500 server error. wpp api will block calls if too many api calls done frequently.
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        assert False not in res, "one or multiple string validation failed Check test log for details"