import pytest
import logging
import time
import datetime
from MobileApps.resources.const.web.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = self.driver.session_data["stack"]
        self.request = self.driver.session_data["request"]
        self.portal_error_modal = self.fc.fd["portal_error_modal"]
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.iris_fw_update_notice = self.fc.fd["iris_fw_update_notice"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.browser = self.request.config.getoption("--browser-type")
        self.locale = self.request.config.getoption("--locale")
        self.ecp = False

        self.supported_locales_dict = ma_misc.load_json_file(TEST_DATA.PORTAL_OOBE_LOCALES)
        self.locals_show_unsupported_modal = self.supported_locales_dict["locals_show_unsupported_modal"]
        self.spec_language = self.supported_locales_dict["spec_language_from_figma"]
        self.fallback_languages = {"en-AG":"en-US"}
        
        self.test_fail = {} 
        self.value_prop_page_not_shown = {}

        if self.printer_profile in self.fc.ecp_printers:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True

        if self.printer_profile == "hulk":
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model, country="australia", language="en")
        
        """
        C37378164     https://hp-jira.external.hp.com/browse/ONBP-2895, https://hp-jira.external.hp.com/browse/ONBP-2952, https://hp-jira.external.hp.com/browse/ONBP-3026
        """

    def test_01_unsupported_locales(self):
        if self.printer_profile != "hulk":
            pytest.skip("This test is only for one printer profile; Don't need to run tests for all printers")
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        for locale in self.locals_show_unsupported_modal:
            logging.info(f"Testing unsupported language modal for locale:{locale}")
            if not self.ecp:
                self.driver.navigate(self.p_oobe.poobe_url.replace("us/en", self.get_locale(locale)))
            else:
                self.driver.navigate(self.fc.fd["ecp"].url.replace("us/en", self.get_locale(locale)))
            
            self.p_oobe.handle_browser_alert_present(accept=True)
            
            if self.portal_error_modal.verify_incorrect_flow_modal(raise_e=False, timeout=15):
                # Changing the command line value of --locale to the current locale this is to match the screenshot file name
                self.request.config.option.locale = locale  
                self.portal_error_modal.verify_unsupported_language_modal_header()
                self.portal_error_modal.verify_language_selector_dropbox()
                self.portal_error_modal.click_language_selector_dropbox()
                assert list(self.spec_language.values()) == self.portal_error_modal.get_language_from_dropdown_list(), "List of supported languages did not match the spec list"
                self.portal_error_modal.select_language_from_dropbox()
                self.portal_error_modal.click_unsupported_language_modal_continue_btn()
                time.sleep(3)
                assert "us/en" in self.driver.current_url, "user did not get redirected to selected language from the modal"            
            else:
                if not self.value_prop_page.verify_value_prop_page(raise_e=False):
                    self.value_prop_page_not_shown[locale] = False
                else:
                    self.test_fail[locale] = False
        
        if False in self.test_fail.values() or False in self.value_prop_page_not_shown.values():
            logging.info(f"Locales failed to show unsupported language modal: {self.test_fail.keys()} and Locales that do not show value Prop page: {self.value_prop_page_not_shown.keys()}")
            pytest.fail("For one or multiple country-language combo did not show unsupported language modal")

    def test_02_unsupported_locales_fallback_language(self):
        if self.biz_model == "E2E" or self.ecp: pytest.skip("HP+ is not supported in any of the fallback locales")
        if self.printer_profile != "hulk":
            pytest.skip("This test is only for one printer profile; Don't need to run tests for all printers")
        lng = list(self.fallback_languages.keys())
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.p_oobe.poobe_url.replace("us/en", self.get_locale(lng[0])))
        self.hpid.handle_privacy_popup(timeout=5)
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.click_landing_page_sign_in_btn()
        if self.hpid.verify_hp_id_sign_in(raise_e=False) is False:
            self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, self.biz_model)
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.biz_model == "Flex" and self.printer_profile not in self.fc.single_sku_printers:
            self.iris_fw_update_notice.verify_fw_update_modal_page()
            self.iris_fw_update_notice.click_accept_auto_fw_updates()
        if self.printer_profile != "beam" or self.ecp: # Beam LF /go flow does not includes Printer Name and Location page
            self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.printer_profile not in self.fc.single_sku_printers and self.biz_model == "E2E":
            self.p_oobe.click_continue_btn()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, False, False)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, False)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")

    ############################# Private Function #######################################

    def get_locale(self, str_list):
        str_list = str_list.split("-")
        return "/".join(str_list[::-1]).lower()    