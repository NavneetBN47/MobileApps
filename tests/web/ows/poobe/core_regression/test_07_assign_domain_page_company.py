import time
import pytest
import datetime
from MobileApps.libs.flows.web.ows import ows_utility
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

pytest.app_info = "POOBE"

class Test_07_Assign_Domain_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = request.config.getoption("--stack")
        self.browser = request.config.getoption("--browser-type")
        self.printer_type = request.config.getoption("--printer-operation") 
        self.connected_printing_services = ConnectedPrintingServices(self.driver)
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) 
        self.company_name_1 = "MIS{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts
        self.assign_printer_organization = self.fc.fd["assign_printer_organization"]
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.ecp, self.enroll = False, False
        
        self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True
        
        """
        TestRail: C31186722
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3291724 
        """
        
    def test_01_assign_domain_page_company(self):
        if self.printer_info is None: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.password = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp : self.fc.handle_printer_fw_page()
        self.fc.verify_assign_organization_step(self.biz_model, self.company_name, ecp=self.ecp)
        self.p_oobe.verify_continue_btn()
        self.assign_printer_organization.clear_entered_name_from_the_box()
        assert self.p_oobe.verify_continue_btn(clickable=True, raise_e=False) is False
        self.assign_printer_organization.select_organization_country_region_seclector()
        self.assign_printer_organization.verify_country_region_drop_down_listbox()
        self.assign_printer_organization.select_orgnization_country_region_option_from_the_drop_down()
        assert self.assign_printer_organization.verify_country_region_drop_down_listbox(raise_e=False) is False
        self.assign_printer_organization.select_organization_country_region_seclector()
        self.verify_organization_selector_error_msg()
        self.driver.send_keys("organization_name_box", self.company_name)
        if self.biz_model == "E2E":
            self.verify_hp_plus_error_modals()
        else:
            self.p_oobe.click_continue_btn()
            self.fc.navigate_printer_consents_page(self.ecp)
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.fc.fd["ecp"].url if self.ecp else self.p_oobe.poobe_url)
        self.fc.value_prop_page(self.biz_model, self.printer_profile, logged_in=True)
        self.hpid.handle_privacy_popup()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.hpid.login(self.email, self.password)
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp : self.fc.handle_printer_fw_page()
        self.fc.verify_assign_organization_step(self.biz_model, self.company_name_1, self.ecp)
        self.driver.send_keys("organization_name_box", "<>~^Â¡Â®`@Â¡Â°")
        self.assign_printer_organization.verify_organization_labels_invalid_name_text()
        if self.biz_model == "E2E":
            self.assign_printer_organization.select_organization_country_region_seclector()
            self.assign_printer_organization.select_trinidad_and_tobago_country_region()
            self.assign_printer_organization.verify_organization_labels_country_error_text()
            self.assign_printer_organization.click_supported_countries_hyperlink()
            self.assign_printer_organization.verify_supported_countries_modal()
        else:
            self.assign_printer_organization.clear_entered_name_from_the_box()
            self.driver.send_keys("organization_name_box", self.company_name_1)
            self.p_oobe.click_continue_btn()
            self.connected_printing_services.verify_connected_printing_services()
        self.fc.remove_printer(self.printer_info, self.biz_model)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        
    ############################## Private Function #################################

    def verify_organization_selector_error_msg(self):
        # This to validate if the error msg 'selected country/Region is not HP+ eligible' should show for /activate not for /connect.
        self.assign_printer_organization.select_trinidad_and_tobago_country_region()
        if self.biz_model == 'E2E':
            self.assign_printer_organization.verify_organization_labels_country_error_text()
        else:
            assert self.assign_printer_organization.verify_organization_labels_country_error_text(raise_e=False) is False
        self.assign_printer_organization.select_organization_country_region_seclector()
        self.assign_printer_organization.select_united_states_country_region()
        assert self.assign_printer_organization.verify_organization_labels_country_error_text(raise_e=False) is False

    def verify_hp_plus_error_modals(self):
        self.assign_printer_organization.select_organization_country_region_seclector()
        self.assign_printer_organization.select_trinidad_and_tobago_country_region()
        self.p_oobe.click_continue_btn()
        self.assign_printer_organization.verify_printer_is_not_supported_in_selected_region_modal()
        self.assign_printer_organization.click_printer_is_not_supported_in_selected_region_modal_support_btn()
        self.driver.add_window("admin-tou")
        self.driver.close_window("admin-tou")