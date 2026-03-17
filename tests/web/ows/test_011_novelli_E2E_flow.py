import time
import pytest
import logging
pytest.app_info = "OWS"

class Test_OWS_Novelli_A_B_test(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc, self.yeti_fc, self.status_and_login_info = ows_test_setup
        if self.status_and_login_info: ows_status, self.access_token, self.id_token = self.status_and_login_info
        self.hp_plus =False
        if "hpplus" in self.profile:
            self.hp_plus = True
            self.profile = self.profile.split('_')[0]

    
    """
    Some of the steps in this flow will change. Currently, this test is designed to handle two flow B and C Flow B will give user the option to enroll in HP+ and skip HP+ Flow C will give user the option to enroll in ink and skip ink
    Depending on how A/B testing goes two of the A,B,C,D,E will be finalized and others will be removed.
    
    https://hp-testrail.external.hp.com/index.php?/suites/view/3841&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=5116960
    https://hp-jira.external.hp.com/browse/OWS-69635

    """
    
    
    def test_01_novelli_flow(self):
        self.fc.navigate_ows(self.ows_printer, stop_at="end")
        self.ows_printer.send_action("PerformInlineOwsActivities")
        if self.fc.flow["ucde_offer"].verify_ucde_hp_plus_benefits_page(timeout=50, raise_e=False):
            logging.info("Flow B") # hp plus offer page (Enroll hp plus and skip hp plus. both case) if skip hp+ fw notice ink page if skip ink then end if enroll ink then login
            self.fc.navigate_hp_plus_features_and_offer(hp_plus=self.hp_plus)
        else:
            logging.info("Flow C") # no hp plus offer straight to ink offer page (Enroll ink and skip ink both case) Dynamic printer notice (fw notice) then end
            self.fc.fd["instant_ink_value_prop"].verify_value_proposition_page(timeout=20)
            self.fc.fd["instant_ink_value_prop"].click_continue_btn()
        time.sleep(5)
        self.yeti_fc.perform_login_via_emulator(self.ows_printer, self.access_token, self.id_token)
        self.fc.navigate_instant_ink(enroll=False)
        self.fc.navigate_firmware_update_choice()