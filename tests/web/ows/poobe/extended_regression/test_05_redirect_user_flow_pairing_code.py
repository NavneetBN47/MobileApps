import time
import pytest
import datetime
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ows import ows_utility

pytest.app_info = "POOBE"

class Test_Redirect_user_printer_pairing_code(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation") 
        self.browser_type = self.request.config.getoption("--browser-type")
        self.poobe_url = self.biz_model+'_'+self.stack
        
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.pairing_code_page = self.fc.fd["pairing_code_page"]
        self.portal_error_modal = self.fc.fd["portal_error_modal"]
        self.ecp, self.enroll = False, False
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        
        self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        
        """
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3319660
        ONBP-622
        1. Launch Flex url or /connect landing page.
        2. Continue the flow untill pairing code page.
        3. Enter HP+ pairing code (Yes HP+ printer pairing code for Flex flow)
        4. Verify Error Overlay.
        5. Click continue setup on the error overlay.
        6. The flow will be re-directed to E2E Landing page /activate.
        7. Continue the Flow. 
        """
    def test_01_redirect_user_via_printer_pairing_code(self):
        if self.printer_profile in self.fc.ecp_printers : pytest.skip()
        if self.printer_profile in self.fc.smb_lf_printer and self.biz_model == "E2E": pytest.skip()
        if self.printer_profile in ["marconi_pdl", "beam", "jupiter"] and self.biz_model == "E2E": pytest.skip()
        if self.printer_profile in self.fc.dual_sku_printers and self.biz_model == "Flex": endpoint, biz = "activate", "E2E"
        if self.printer_profile in self.fc.dual_sku_printers and self.biz_model == "E2E": endpoint, biz = "connect", "Flex"
        if self.printer_profile in self.fc.single_sku_printers: endpoint, biz = "connect", "Flex"
        if self.printer_profile in self.fc.smb_lf_printer : endpoint, biz = "activate", "E2E"
        self.driver.navigate("smb.{}.portalshell.int.hp.com/{}".format(self.stack, endpoint))
        if self.driver.check_if_browser_alert_present(raise_e=False) is True:
            self.driver.accept_or_dismiss_browser_alert(accept=True)
        self.email, self.pwd, self.pairing_code = self.navigate_to_pairing_code_page(biz)
        self.pairing_code_page.verify_pairing_code_screen()
        self.p_oobe.verify_left_panel_printer_container()
        self.pairing_code_page.input_pairing_code(code=self.pairing_code['user_code'])
        self.p_oobe.click_continue_btn()
        # Verify incorrect flow error modal
        if self.portal_error_modal.verify_incorrect_flow_modal(raise_e=False) is False:
            self.p_oobe.click_continue_btn()
        self.fc.incorrect_flow_modal(self.pairing_code['user_code'])
        self.p_oobe.handle_browser_alert_present()
        # Verify page redirected to Correct Landing page
        self.fc.value_prop_page(self.biz_model, self.printer_profile, logged_in=True)
        # Complete the onboarding flow.
        self.value_prop_page.click_landing_page_continue_btn()
        self.pairing_code_page.verify_pairing_code_screen()
        self.pairing_code_page.input_pairing_code(code=self.pairing_code['user_code'])
        self.p_oobe.click_continue_btn()
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)    
        if self.printer_profile not in self.fc.smb_lf_printer: self.fc.navigate_printer_name_location_page(biz= self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E" and self.printer_profile in self.fc.dual_sku_printers: self.p_oobe.click_continue_btn()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.pairing_code['device_code'], self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")

    ################################ Private Function ##################################

    def navigate_to_pairing_code_page(self, biz):
        self.fc.landing_page(biz)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.pairing_code = ows_utility.get_pairing_code(self.printer_profile, stack = self.stack, post_card=self.printer_info['claim_postcard'], finger_print=self.printer_info['fingerprint'], 
                                                  model_number=self.printer_info['model_number'], uuid=self.printer_info['uuid'])
        return self.email, self.pwd, self.pairing_code