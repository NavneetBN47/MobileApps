import pytest
pytest.app_info = "POOBE"
pytest.localization = []

class Test_01_Landing_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup

        self.value_prop_page = self.fc.fd["value_prop_page"]

        if self.printer_profile in self.fc.ecp_printers:
            self.printer_profile = self.printer_profile.split("_")[0]
            if self.biz_model != "E2E":
                self.fc.add_translations_to_app_strings("value_prop_page", self.biz_model)

        if self.printer_profile in self.fc.smb_flowers and self.biz_model == "Flex":
            self.fc.add_translations_to_app_strings("value_prop_page", self.biz_model)
        
    def test_01_landing_value_prop_page(self):
        if self.biz_model == "E2E" and (self.printer_profile in self.fc.ecp_printers or self.printer_profile in self.fc.smb_flowers or self.printer_profile in self.fc.smb_flex_printer):
            pytest.skip()
        self.fc.value_prop_page(self.biz_model, self.printer_profile)
        self.value_prop_page.verify_landing_page_create_account_btn()
        self.value_prop_page.verify_landing_page_sign_in_btn()
        if self.printer_profile in self.fc.smb_flowers:
            self.value_prop_page.verify_stepper_step_0(raise_e=True)
            self.value_prop_page.verify_stepper_step_1(raise_e=True)
            self.value_prop_page.verify_stepper_step_2(raise_e=True)
            self.value_prop_page.verify_stepper_step_3(raise_e=True)
        # Cleanup emails
        self.fc.fd["gmail_api"].batch_delete_from_sender("donotreply@email.hpsmart.com")
        self.fc.fd["gmail_api"].batch_delete_from_sender("donotreply@instantink.hpsmart.com")
        if False in pytest.localization:
            pytest.fail("Localization string validation failed for one or multiple stings check log for specific errors")