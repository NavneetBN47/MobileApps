import pytest
import time
import datetime
from MobileApps.libs.flows.web.ows import ows_utility
pytest.localization = []
pytest.app_info = "POOBE"

class Test_06_Flex_Iris_FW_Update(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser = request.config.getoption("--browser-type")
        self.value_prop_page = self.fc.fd["value_prop_page"]
        self.iris_fw_update_notice = self.fc.fd["iris_fw_update_notice"]
        self.ecp, self.enroll = False, False
        self.company_name = "SIC{:%m%d%H%M%S}".format(datetime.datetime.now()) # Organization name must be different for different Accounts

        if self.biz_model == "Flex" and (self.printer_profile in self.fc.smb_flowers or self.printer_profile in self.fc.dual_sku_printers): pytest.skip()
        
        self.printer_info = None if self.biz_model == "E2E" else self.fc.generate_simulator_printer(self.printer_profile, self.stack, self.biz_model)

        if self.biz_model == "Flex" and (self.printer_profile in self.fc.smb_flowers or self.printer_profile in self.fc.dual_sku_printers):
            self.fc.add_translations_to_app_strings("iris_firmware_update", self.biz_model)
        
        if self.printer_profile in self.fc.ecp_printers and self.printer_info:
            self.printer_profile = self.printer_profile.split("_")[0]
            self.ecp = True
        
        """
        https://hp-testrail.external.hp.com/index.php?/suites/view/41965&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3132847
        """
    def test_01_flex_iris_fw_update(self):
        if self.printer_info is None: pytest.skip()
        try:
            self.email, self.pwd, self.device_code = self.navigate_to_firmware_update_page()
            self.iris_fw_update_notice.verify_fw_update_modal_page()
            self.iris_fw_update_notice.verify_fw_update_notice_content()
            self.iris_fw_update_notice.verify_hp_learn_url_fw_page()
            self.p_oobe.verify_left_panel_printer_container()
            if self.ecp or (self.printer_profile in self.fc.smb_flowers) or (self.printer_profile in self.fc.dual_sku_printers):
                self.iris_fw_update_notice.click_cancel_and_manual_setup()
                self.iris_fw_update_notice.verify_cancel_and_setup_manually_overlay()
                self.iris_fw_update_notice.verify_overlay_close_btn()
                self.iris_fw_update_notice.verify_continue_online_setup_pop_model_btn()
                self.iris_fw_update_notice.verify_cancel_online_setup_pop_model_btn()
                self.iris_fw_update_notice.click_close_fw_overlay()
                self.iris_fw_update_notice.click_cancel_and_manual_setup()
                self.iris_fw_update_notice.click_cancel_online_setup_overlay_model_btn()
                self.fc.value_prop_page(self.biz_model, self.printer_profile, logged_in=True)
                self.value_prop_page.verify_landing_page_continue_btn()
            else:
                self.iris_fw_update_notice.click_accept_auto_fw_updates()
                if self.ecp or self.printer_profile in self.fc.smb_flowers:
                    self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
                    self.fc.navigate_printer_consents_page(self.ecp)
                self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
                self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
            if self.ecp:
                self.url = self.fc.fd["ecp"].url
            elif self.printer_profile in self.fc.smb_lf_printer:
                return        
            else:
                self.url = self.p_oobe.poobe_url
            self.fc.clear_browsing_data_and_relaunch_flow(self.browser, url=self.url)
            self.email, self.pwd, self.device_code = self.navigate_to_firmware_update_page(connect=True if "connect" in self.url else False)
            self.iris_fw_update_notice.verify_fw_update_modal_page()
            self.iris_fw_update_notice.click_cancel_and_manual_setup()
            self.iris_fw_update_notice.click_continue_online_setup_overlay_model_btn()
            if self.ecp: self.iris_fw_update_notice.click_accept_auto_fw_updates()
            if self.ecp:
                self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
                self.fc.navigate_printer_consents_page(self.ecp)
                self.fc.navigate_printer_name_location_page(biz=self.biz_model, printer_profile=self.printer_profile)
                self.fc.navigate_flow_from_printer_activation_page(self.printer_profile, self.stack, self.biz_model, self.printer_info, self.device_code, self.enroll, self.ecp)
                self.fc.verify_finish_printer_setup_page(self.biz_model, self.printer_profile, self.ecp)
        finally:
            self.fc.remove_printer(self.printer_info, self.biz_model, timeout=100)
            self.fc.delete_email_from_main_account(email_to=self.email, email_from="donotreply@email.hpsmart.com")

    ######################### Private function ##########################

    def navigate_to_firmware_update_page(self, connect=False):
        self.hpid.handle_privacy_popup(timeout=5)
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.click_landing_page_sign_in_btn()
        self.email, self.pwd = self.fc.create_hpid_login_credentials()
        self.device_code = self.fc.navigate_pairing_code_success_page(self.printer_profile, self.stack, self.printer_info, biz = self.biz_model)
        if self.ecp or (self.printer_profile != "beam" and self.biz_model == "Flex") or connect:
            return self.email, self.pwd, self.device_code
        self.fc.navigate_printer_owner_page(self.biz_model, name=self.company_name)
        self.fc.navigate_printer_consents_page(self.ecp)
        return self.email, self.pwd, self.device_code