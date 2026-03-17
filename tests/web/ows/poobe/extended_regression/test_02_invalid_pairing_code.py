import pytest
import time
import datetime
from MobileApps.libs.flows.web.ows import ows_utility

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.ecp = False
        self.printer_type = self.request.config.getoption("--printer-operation")
        self.browser = self.request.config.getoption("--browser-type")
        self.locale = self.request.config.getoption("--locale")
        self.har = self.request.config.getoption("--har")

        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.pairing_code_page = self.fc.fd["pairing_code_page"]
        self.portal_oobe_error = self.fc.fd["portal_error_modal"]
        self.company_name = "KIC{:%m%d%H%M%S}".format(datetime.datetime.now())
        self.invalid_code = "QWDVGLPV"
        
        self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        self.printer_info_1 = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True

        """https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3440684
           https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3440685
        """

    def test_01_invalid_pairing_code_page(self):
        if self.printer_profile in self.fc.ecp_printers: pytest.skip()
        if self.printer_profile in self.fc.smb_lf_printer and self.biz_model == "E2E": pytest.skip()
        self.username, self.pwd = self.navigate_to_pairing_code_page()
        if self.printer_profile in self.fc.dual_sku_printers and self.biz_model == "Flex":
            self.pairing_code_page.verify_cant_find_pairing_code_madal_btn()
            self.pairing_code_page.click_cant_find_pairing_code_btn()
            self.pairing_code_page.verify_cant_find_pairing_code_modal()
            self.pairing_code_page.click_cant_find_pairing_code_modal_close_btn()
        assert self.p_oobe.verify_continue_btn(clickable=True, raise_e=False) is False
        list1 = [self.invalid_code[:6], self.invalid_code,"!@#$%A&*"]
        for i in list1:
            self.pairing_code_page.input_pairing_code(code=i)
            if i == self.invalid_code[:6]:
                assert self.p_oobe.verify_continue_btn(clickable=True, raise_e=False) is False
            if i == self.invalid_code:
                self.p_oobe.click_continue_btn()
                self.portal_oobe_error.verify_invalid_pairing_code_error_msg()
            self.pairing_code_page.clear_entered_code()
            if i == "!@#$%A&*":
                if len(self.pairing_code_page.get_pairing_code_value()) != 0:
                    raise Exception("pairing code value error")
        self.pairing_code_page.input_pairing_code(code=list1[1])
        for _ in range(5):
            self.p_oobe.click_continue_btn()
        self.portal_oobe_error.verify_too_many_pairing_code_attempt_error_modal(timeout=15)
        self.portal_oobe_error.verify_too_many_pairing_code_attempt_header()
        self.portal_oobe_error.verify_too_many_pairing_code_attempt_and_body()
        time.sleep(280)  # Reducing hard wait as selenium driver dies after 5 mins of inactivity
        assert self.portal_oobe_error.verify_too_many_pairing_code_attempt_header(raise_e=False, timeout=30, invisible=True), "Error Modal still seen after timeout"
        self.pairing_code_page.clear_entered_code()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, self.biz_model)
        if self.ecp: self.fc.handle_printer_fw_page()
        self.fc.verify_assign_organization_step(self.biz_model, name=self.company_name)
        self.p_oobe.click_continue_btn()
        self.fc.navigate_printer_consents_page()
        if self.printer_profile != "beam" or self.ecp: 
            self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E": 
            self.p_oobe.click_continue_btn()
        if self.printer_profile == "beam" and self.ecp is False: 
            self.fc.handle_printer_fw_page()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, ecp=False)
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.email_1, self.pwd_1 = self.navigate_to_pairing_code_page()
        if self.har:
            self.driver.request_interceptor = lambda request: self.driver.block_request_call(request, "deviceauthgrant")
            self.pairing_details_1 = ows_utility.get_pairing_code(self.printer_profile, self.stack, self.printer_info_1["fingerprint"], 
                                                                        self.printer_info_1["claim_postcard"], self.printer_info_1["model_number"], self.printer_info_1["uuid"])
            self.pairing_code_page.input_pairing_code(self.pairing_details_1['user_code'])
            self.p_oobe.click_continue_btn()
            self.portal_oobe_error.verify_error_modal(timeout=30)
            self.portal_oobe_error.click_try_again_btn()
            del self.driver.request_interceptor
            self.pairing_code_page.input_pairing_code(self.pairing_details_1['user_code'])
            self.pairing_code_page.click_continue_btn()
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.remove_printer(self.printer_info_1, self.biz_model, timeout=10)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        self.fc.delete_email_from_main_account(email_to=self.email_1, email_from="donotreply@email.hpsmart.com")


    ################################ Private Function ##################################

    def navigate_to_pairing_code_page(self):
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.pairing_code_page.verify_pairing_code_screen()
        return self.email, self.pwd