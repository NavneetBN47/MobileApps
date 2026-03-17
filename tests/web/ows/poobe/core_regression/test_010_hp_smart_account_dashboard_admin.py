import time
import pytest
import datetime

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        
        if self.printer_profile in self.fc.dual_sku_printers:
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        """
        testRail: C29699056, C29699057, C29699058, C29699060  C29699057 C29696191 C29699171
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&group_id=3132839
        """
    
    def test_01_hp_smart_account_dashboard_admin(self):
        if self.printer_profile not in self.fc.dual_sku_printers or self.biz_model != "E2E":
            pytest.skip()
        self.hpid.handle_privacy_popup(timeout=5)
        self.fc.landing_page(biz = self.biz_model)
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(False)
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E":
            self.p_oobe.click_continue_btn()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, enroll=False, ecp=False)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, ecp=False)
        self.fc.verify_organization_name_from_smb_dashboard_account_tab(self.company_name)
        #self.fc.verify_printer_connected_status_and_printer_name()
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")