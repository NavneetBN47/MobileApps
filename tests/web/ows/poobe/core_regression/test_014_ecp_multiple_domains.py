import pytest
import time
import datetime

pytest.app_info = "POOBE"

class Test_014_ecp_multiple_domain(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser = request.config.getoption("--browser-type")
        self.ecp, self.enroll = False, False
        
        self.assign_printer_organization = self.fc.fd["assign_printer_organization"]
        self.value_prop_page = self.fc.fd["value_prop_page"]
        
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        time.sleep(1)
        self.company_name_1 = "DIP{:%m%d%H%M%S}".format(datetime.datetime.now())
        time.sleep(1)
        self.company_name_2 = "DIS{:%m%d%H%M%S}".format(datetime.datetime.now())
        self.org_name = [self.company_name, self.company_name_1, self.company_name_2]
        self.ecp = False 


        if self.printer_profile in self.fc.ecp_printers and self.biz_model == "Flex": 
            self.printer_profile = self.printer_profile.split("_")[0]; self.ecp=True
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        
        """
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3435464
        """
    def test_01_ecp_multiple_domain_page(self):
        if self.ecp is False:
            pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.fc.handle_printer_fw_page()
        self.fc.navigate_printer_owner_page(self.biz_model, self.company_name)
        self.fc.fd["connected_printing_services"].verify_connected_printing_services()
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.fc.fd["ecp"].url)
        self.verify_organization_page(self.org_name[:1])
        self.fc.navigate_printer_owner_page(self.biz_model, self.company_name_1)
        self.fc.fd["connected_printing_services"].verify_connected_printing_services()
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.fc.fd["ecp"].url)  
        self.verify_organization_page(self.org_name[:2])
        self.fc.navigate_printer_owner_page(self.biz_model, self.company_name_2)
        self.fc.fd["connected_printing_services"].verify_connected_printing_services()
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.fc.fd["ecp"].url)      
        self.verify_organization_page(self.org_name[:3])
        self.assign_printer_organization.verify_existing_organization_page(self.company_name_2)
        self.p_oobe.click_continue_btn()
        self.fc.navigate_printer_consents_page(self.ecp)
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")

    ######################### Private function ##########################

    def navigate_to_assign_organization_page(self):
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.hpid.handle_privacy_popup()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.email, self.pwd)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        
    def verify_organization_page(self, org):
        self.navigate_to_assign_organization_page()
        self.fc.handle_printer_fw_page()
        self.assign_printer_organization.verify_assign_printer_owner_page()
        for i in org:
            self.assign_printer_organization.verify_existing_organization_page(i)
        self.assign_printer_organization.select_new_organization_option()
        assert self.p_oobe.verify_continue_btn(clickable=True, raise_e=False) is False
        for i in org:
            self.assign_printer_organization.select_already_existing_organization(i)
        self.p_oobe.verify_continue_btn()