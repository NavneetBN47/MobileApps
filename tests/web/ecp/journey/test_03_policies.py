import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.web.ecp.ecp_utility import load_journey_printer_info
pytest.app_info = "ECP"

class Test_03_Policies(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.device = self.fc.fd["devices"]
        self.es = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack + "_journey_testing")
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        self.p_info = load_journey_printer_info(self.stack + "_journey_testing")

        yield # Cleanup:
        try:
            self.home.logout()
        except TimeoutException as err:
            # logout is 'best effort' only for this journey. We don't care if the logout fails here
            print(f"Unable to complete teardown. {err}")

    def test_01_verify_assess_remediation(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236562
        #Verify that user can can view a specific policy in a specific group, as well as confirm a known active policy
        #in the policy table.
        print(f"Using account: {self.hpid_username}")
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, retry=2, raise_e=True)
        self.home.verify_notification_mfe_card()
        self.home.click_policies_menu_btn()
        self.es.select_group("JourneyTesting")
        self.es.verify_table_policy_by_name("JourneyTestingPolicy")
        self.es.click_policies_tab()
        self.es.verify_table_policy_by_name("JourneyTestingPolicy", policy_search=True, policy_status="Active")
