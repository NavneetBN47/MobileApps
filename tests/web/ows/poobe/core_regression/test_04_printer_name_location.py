import pytest
import time
import datetime
pytest.app_info = "POOBE"
pytest.localization = []

class Test_04_Printer_Name_Location_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.ecp = False
        self.stack = request.config.getoption("--stack")
        self.browser = request.config.getoption("--browser-type")
        self.printer_type = request.config.getoption("--printer-operation")
        self.printer_name_and_location = self.fc.fd["printer_name_location_page"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts

        if self.printer_profile not in self.fc.smb_lf_printer:
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        else:
            self.printer_info = None

        if self.biz_model == "Flex" and self.printer_profile in self.fc.smb_flowers: self.fc.add_translations_to_app_strings("printer_name_and_location_page", self.biz_model)

        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True
        
    def test_01_printer_name_location_page(self):
        if self.printer_info is None: pytest.skip()
        self.email, self.pwd = self.navigate_flow_printer_name_location_page(skip=False)
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.fc.fd["ecp"].url if self.ecp else self.p_oobe.poobe_url)
        self.email_0, self.pwd_0 = self.navigate_flow_printer_name_location_page(skip=True)
        self.fc.remove_printer(self.printer_info, self.biz_model, timeout=90)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        self.fc.delete_email_from_main_account(email_to=self.email_0, email_from="donotreply@email.hpsmart.com")

    ################################ Private Function ##################################


    def navigate_flow_printer_name_location_page(self, skip=False):
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp : self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        self.printer_name_and_location.verify_printer_name_location_header(raise_e=True)
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile, skip=skip)
        if self.biz_model == "E2E": self.p_oobe.click_continue_btn()
        return self.email, self.pwd