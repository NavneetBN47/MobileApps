import logging
import time
import pytest
import datetime

pytest.app_info = "POOBE"

class Test_existing_account_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.request = self.driver.session_data["request"]
        self.stack = self.driver.session_data["stack"]
        self.printer_type = self.request.config.getoption("--printer-operation") 
        self.browser = self.request.config.getoption("--browser-type")
        self.ecp = False
        
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.assign_printer_organization = self.fc.fd["assign_printer_organization"]
        self.connected_printing_services = self.fc.fd["connected_printing_services"]
        self.smb_dashboard_home = self.fc.fd["smb_dashboard_home"]
        self.smb_dashboard_login = self.fc.fd["smb_dashboard_login"]
        self.printer_name_location_page = self.fc.fd["printer_name_location_page"]

        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.company_name_1 = "WIC{:%m%d%H%M%S}".format(datetime.datetime.now())
        self.company_name_2 = "CIG{:%m%d%H%M%S}".format(datetime.datetime.now())
        
        self.printer_info = None if self.printer_profile not in self.fc.dual_sku_printers else self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        

    """
    https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3282714
    ONBP-494 ONBP-888
    1. Launch Flow Ceate Account, assign organization and Re-start flow.
    2. continue flow untill assign organization page (verify continue btn disabled)
    3. Select old or add a new organization
    4. Select Old organization click continue and verify Printer consents page.
    5. Re-start flow sign into same account continue untill Assign organization page and add new organization.
    6. click continue and verify HP+ Pairing code page.
    7. Re-start Flow E2E or Flex should already be signed in and continue till Assign printer owner page.
    8. Create new organization and continue flow.
    """

    def test_01_existing_account_flow(self):
        if self.printer_info is None: pytest.skip()
        self.fc.landing_page(biz = self.biz_model)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.username, self.password = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        
        # assign organization
        
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        
        # clear browser and re-start the flow sign in the same account
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.navigate_to_assign_printer_organization(self.username, self.password)
        self.assign_printer_organization.select_already_existing_organization(self.company_name)
        self.p_oobe.click_continue_btn()
        self.connected_printing_services.verify_connected_printing_services()
        
        # Re-start the flow fresh and sign in to same account
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.navigate_to_assign_printer_organization(self.username, self.password)
        
        # Enter another valid organization
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name_1)
        self.fc.navigate_printer_consents_page(self.ecp)
        
        # verify printer name and location page for /connect and then Re-start flow sign into same account continue to assign org page
        if self.printer_profile != "beam" or self.ecp: 
            self.printer_name_location_page.verify_printer_name_location_page()


        # Re-start the flow sign into same account.
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.navigate_to_assign_printer_organization(self.username, self.password)
        
        # Verify all organization shown entered previously can be seen on this page. Select 2nd organization and continue the Flow to dashboard page.
        self.assign_printer_organization.select_already_existing_organization(self.company_name)
        self.assign_printer_organization.select_already_existing_organization(self.company_name_1)
        logging.info("Organization name: {}".format(self.company_name_1))
        self.p_oobe.click_continue_btn()
        self.connected_printing_services.verify_connected_printing_services()
        self.connected_printing_services.click_connected_printing_services()
        self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.biz_model == "E2E":
            self.p_oobe.click_continue_btn()
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, enroll=False, ecp=False)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, ecp=False)
        self.smb_dashboard_home.verify_home_menu_btn()
        self.smb_dashboard_home.verify_smb_home_title_bar()
        time.sleep(3)
        self.fc.verify_organization_name_from_smb_dashboard_account_tab([self.company_name,self.company_name_1])
        # sign out and clear history, cookies sign in same account
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url="https://smb.{}.portalshell.int.hp.com".format(self.stack))
        self.hpid.login(self.username, self.password)
        self.smb_dashboard_login.verify_organization_page()
        self.smb_dashboard_login.verify_oraganization_name_in_list(self.company_name)
        self.smb_dashboard_login.verify_oraganization_name_in_list(self.company_name_1)

        # Sign Into personal Account and validate organization page does not show
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.fc.landing_page(biz = self.biz_model)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.username_p, self.password_p = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        # Re-start, Sign in and Select For Business Use
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser)
        self.navigate_to_assign_printer_organization(self.username_p, self.password_p)
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name_2)
        self.connected_printing_services.verify_connected_printing_services()
        self.fc.remove_printer(self.printer_info, self.biz_model, timeout=45)

    ############################# Private Function #######################################
    
    def navigate_to_assign_printer_organization(self, username, password):
        self.fc.landing_page(biz = self.biz_model)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.hpid.login(username, password)
        time.sleep(5)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        self.assign_printer_organization.verify_assign_printer_owner_page()
        self.p_oobe.verify_left_panel_printer_container(self.biz_model)   
        self.assign_printer_organization.verify_oranganization_option()