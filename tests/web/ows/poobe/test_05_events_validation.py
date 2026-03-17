import time
import pytest
import datetime
from MobileApps.libs.flows.web.ows import ows_utility
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices
from SAF.misc.kibana_api import KibanaAPI
import difflib
import json

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.enroll, self.ecp = False, False
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        if "ink" in self.biz_model.lower():
            self.biz_model = self.biz_model.split("_")[0]
            self.enroll = True
        self.connected_printing_services = ConnectedPrintingServices(self.driver)
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.iris_fw_update_notice = self.fc.fd["iris_fw_update_notice"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts

        self.sim_printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        if self.printer_profile in self.fc.ecp_printers and self.sim_printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True        
        
        """
        Data-analytics Test Aim to cover all events in happy path and validate against the spec and opensearch formely Kibana
        Cmd line arguments --analytics and --har required for validation
        """
    def test_01_portal_oobe_bat_flow(self): 
        if self.sim_printer_info is None: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.sim_printer_info, self.biz_model)
        #Pairing Code Sucess event controlDetail: Factory_Flex        
        if self.ecp is False and self.printer_profile !="beam": # Two flows for Beam ECP flow and LF SMB flow
            self.fc.select_how_to_setup_printer_company_or_personal(self.printer_profile, self.biz_model, self.printer_type)
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.connected_printing_services.verify_connected_printing_services()
        self.connected_printing_services.click_connected_printing_services()
        if self.biz_model == "Flex" and self.printer_profile not in self.fc.single_sku_printers:
            self.iris_fw_update_notice.verify_fw_update_modal_page()
            self.iris_fw_update_notice.click_accept_auto_fw_updates()
        if self.printer_profile != "beam" or self.ecp: # Beam LF /go is smb so flow includes Printer Name and Location page just like ecp flow
            self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
        if self.printer_profile in self.fc.dual_sku_printers and self.biz_model == "E2E":
            self.p_oobe.click_continue_btn()
        if self.printer_profile in self.fc.single_sku_printers:
            if self.biz_model == "Flex": self.fc.navigate_hp_plus_benefits_and_requirments_page(hp_plus="decline", printer_profile=self.printer_profile)
            else: self.fc.navigate_hp_plus_benefits_and_requirments_page(hp_plus="accept", printer_profile=self.printer_profile)
        self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.sim_printer_info, self.device_code, self.enroll, self.ecp)
        self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        ows_utility.remove_printer(self.sim_printer_info['serial_number'])
        time.sleep(100) # Adding time delay to avoid 500 server error. wpp api will block calls if too many api calls done frequently.
        events_request = self.driver.get_all_requests_matching_url("clienttelemetry/v3/telemetry/client")
        events_captured = self.p_oobe.log_event_parse_kibana_format(events_request, "simpleUi")
        visit_uuid = self.p_oobe.get_visituuid(events_request)
        kibana_data = self.driver.analytics_container.get_kibana_result("https://search-xray-x54sy5knolm6hdgr4zwifl5oiu.us-west-2.es.amazonaws.com", "ows", visit_uuid, 100)
        self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")
        kibana_result = self.driver.analytics_container.compare_results(kibana_data)
        har_result = self.driver.analytics_container.compare_results(events_captured)
        if False in kibana_result or False in har_result:
            raise AssertionError("Events captured does not match with the spec events on file see below:\n following events on file but not in kibana:{}\n following events on file but not in network logs:{}".format(kibana_result, har_result))
        