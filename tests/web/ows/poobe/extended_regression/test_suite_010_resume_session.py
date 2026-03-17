import pytest
import time
import datetime
from MobileApps.libs.flows.web.poobe.flow_container import FlowContainer
pytest.app_info = "POOBE"

class Test_010_resume_session_modal(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = self.driver.session_data['stack']
        self.printer_type = self.driver.session_data["request"].config.getoption("--printer-operation")
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.pairing_code_page = self.fc.fd["pairing_code_page"]
        self.resume_session_modal = self.fc.fd["resume_session_modal"]
        self.printer_consents_page = self.fc.fd["connected_printing_services"]
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts

        if self.printer_profile not in self.fc.ecp_printers:
            self.printer_info = self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)
        
    """
    C43366639
    ONBP-1601: Resume Session Modal   
    """        

    def test_01_resume_session_modal_pairing_code_page(self):
        if self.printer_info is None: pytest.skip()
        if self.printer_profile not in ["hulk"]: pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.pairing_code_page.verify_pairing_code_screen()
        self.p_oobe.verify_left_panel_printer_container(self.biz_model)
        self.driver.open_window("", "new_main")                         # This Opens a new tab not a window
        self.driver.add_window("new_main")                          # This adds the new tab to the main Window Handle
        self.driver.switch_window("new_main")                       # This switches to the new tab                          
        self.driver.navigate(self.p_oobe.poobe_url)
        new_window_fc = FlowContainer(self.driver, endpoint=self.fc.endpoint, window="new_main")
        assert new_window_fc.fd["resume_session_modal"].verify_resume_session_modal_elements(False) is False, "Resume Session Modal is displayed"
        new_window_fc.fd["value_prop_page"].verify_value_prop_page()
        self.resume_session_modal_printer_consents_page(new_window_fc)
        if self.biz_model == "Flex":
            self.resume_session_modal_iris_fw_update_notice_page(new_window_fc)
        self.resume_session_modal_printer_name_location_page(new_window_fc)
        self.resume_session_modal_hp_plus_benefits_and_requirements_page(new_window_fc)
        self.resume_session_modal_flow_from_printer_activation_page(new_window_fc)
        self.resume_session_modal_install_drivers_modal(new_window_fc)

    def resume_session_modal_printer_consents_page(self, new_window_fc):
        new_window_fc.start_flow_and_continue_to_specific_page_in_flow(self.printer_profile, self.printer_type, self.company_name, self.stack, self.printer_info, self.biz_model, "printer_consents_page")
        new_window_fc.fd["connected_printing_services"].click_connected_printing_services_manage_options_btn()
        new_window_fc.fd["connected_printing_services"].click_connected_printing_services_manage_options_back_btn()
        self.close_current_tab_and_relaunch_on_new_tab_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_resume_btn()
        new_window_fc.fd["connected_printing_services"].verify_connected_printing_services()
        time.sleep(5)
        self.relaunch_flow_and_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_start_new_session_btn()
        new_window_fc.fd["value_prop_page"].verify_value_prop_page()

    def resume_session_modal_iris_fw_update_notice_page(self, new_window_fc):
        new_window_fc.start_flow_and_continue_to_specific_page_in_flow(self.printer_profile, self.printer_type, self.company_name, self.stack, self.printer_info, self.biz_model, "iris_fw_update_notice")
        new_window_fc.fd["iris_fw_update_notice"].click_cancel_and_manual_setup()
        new_window_fc.fd["iris_fw_update_notice"].click_close_fw_overlay()
        self.close_current_tab_and_relaunch_on_new_tab_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_resume_btn()
        new_window_fc.fd["iris_fw_update_notice"].verify_fw_update_modal_page()        
        time.sleep(5)
        self.relaunch_flow_and_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_start_new_session_btn()
        new_window_fc.fd["value_prop_page"].verify_value_prop_page()
    
    
    def resume_session_modal_printer_name_location_page(self, new_window_fc):
        new_window_fc.start_flow_and_continue_to_specific_page_in_flow(self.printer_profile, self.printer_type, self.company_name, self.stack, self.printer_info, self.biz_model, "printer_name_location_page")
        self.close_current_tab_and_relaunch_on_new_tab_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_resume_btn()
        new_window_fc.fd["printer_name_location_page"].verify_printer_name_location_page()
        time.sleep(5)
        self.relaunch_flow_and_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_start_new_session_btn()
        new_window_fc.fd["value_prop_page"].verify_value_prop_page()

    def resume_session_modal_hp_plus_benefits_and_requirements_page(self, new_window_fc):
        if self.biz_model == "E2E":
            new_window_fc.start_flow_and_continue_to_specific_page_in_flow(self.printer_profile, self.printer_type, self.company_name, self.stack, self.printer_info, self.biz_model, "hp_plus_smart_printer_requirements_page")
            self.close_current_tab_and_relaunch_on_new_tab_verify_resume_modal()
            new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
            new_window_fc.fd["resume_session_modal"].click_resume_btn()
            new_window_fc.fd["hp_plus_smart_printer_requirements"].verify_hp_plus_smart_printer_requirements_page()
            time.sleep(5)
            self.relaunch_flow_and_verify_resume_modal()
            new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
            new_window_fc.fd["resume_session_modal"].click_start_new_session_btn()
            new_window_fc.fd["value_prop_page"].verify_value_prop_page()
    
    def resume_session_modal_flow_from_printer_activation_page(self, new_window_fc):
        new_window_fc.start_flow_and_continue_to_specific_page_in_flow(self.printer_profile, self.printer_type, self.company_name, self.stack, self.printer_info, self.biz_model, "activating_printer_page")
        self.close_current_tab_and_relaunch_on_new_tab_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_resume_btn()
        new_window_fc.fd["printer_name_location_page"].verify_printer_name_location_page()
        time.sleep(5)
        self.relaunch_flow_and_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_start_new_session_btn()
        new_window_fc.fd["value_prop_page"].verify_value_prop_page()

    def resume_session_modal_install_drivers_modal(self, new_window_fc):
        new_window_fc.start_flow_and_continue_to_specific_page_in_flow(self.printer_profile, self.printer_type, self.company_name, self.stack, self.printer_info, self.biz_model, "install_printer_driver_page")
        self.close_current_tab_and_relaunch_on_new_tab_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_resume_btn()
        new_window_fc.fd["poobe"].verify_install_printer_driver_page(self.driver.get_browser_platform())
        time.sleep(5)
        self.relaunch_flow_and_verify_resume_modal()
        new_window_fc.fd["resume_session_modal"].verify_resume_session_modal()
        new_window_fc.fd["resume_session_modal"].click_start_new_session_btn()
        new_window_fc.fd["value_prop_page"].verify_value_prop_page()


    ############################# Private Function #####################################        

    def close_current_tab_and_relaunch_on_new_tab_verify_resume_modal(self):
        time.sleep(5)
        self.driver.navigate(self.p_oobe.poobe_url)
        if self.driver.check_if_browser_alert_present(raise_e=False):
            self.driver.accept_or_dismiss_browser_alert(accept=True)

    def relaunch_flow_and_verify_resume_modal(self):
        self.driver.navigate(self.p_oobe.poobe_url)
        if self.driver.check_if_browser_alert_present(raise_e=False):
            self.driver.accept_or_dismiss_browser_alert(accept=True)