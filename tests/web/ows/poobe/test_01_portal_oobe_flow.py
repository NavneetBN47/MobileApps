import pytest
import datetime

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.enroll, self.ecp = False, False
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation")
        if "ink" in self.biz_model.lower():
            self.biz_model = self.biz_model.split("_")[0]
            self.enroll = True
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.iris_fw_update_notice = self.fc.fd["iris_fw_update_notice"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
         
        is_real_printer = "real" in self.printer_profile.lower()
        if is_real_printer:
            self.printer_info = self.request.getfixturevalue('load_printer_session_without_manager')
            self.printer_info.send_secure_cfg(self.stack)
        else:
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True

        """
        testRail: C29699056, C29699057, C29699058, C29699060  C29699057 C29696191 C29699171
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&group_id=3132839
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3447627
        """
    
    def test_01_portal_oobe_bat_flow(self): 
        if self.printer_info is None: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, self.biz_model)
        if self.ecp: self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        if self.printer_profile != "beam" or self.ecp: self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E": self.p_oobe.click_continue_btn()
        if self.printer_profile == "beam" and self.ecp is False: self.fc.handle_printer_fw_page()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@instantink.hpsmart.com")