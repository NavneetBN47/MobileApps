import pytest
import datetime
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

pytest.app_info = "POOBE"

class Test_01_Create_Account_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup

        if self.printer_profile in self.fc.ecp_printers:
            self.printer_profile = self.printer_profile.split("_")[0]
        
    def test_01_create_account_page(self):
        if self.biz_model == "E2E" and self.printer_profile in self.fc.ecp_printers or self.printer_profile in self.fc.smb_flowers or self.printer_profile in self.fc.smb_flex_printer:
            pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.fc.fd["value_prop_page"].click_landing_page_sign_in_btn()
        self.fc.create_hpid_login_credentials()