import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ecp.ecp_utility import load_journey_printer_info
from selenium.common.exceptions import TimeoutException
pytest.app_info = "ECP"

class Test_02_ECP_Device(object):

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


    def test_01_verify_device_online(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236562
        #Verify the 'online' status of AT LEAST 1 known device (known devices listed in resources/test_data/ecp/accounts.json
        # in production_journey_testing.printers and stage_journey_testing.printers)
        print(f"Using account: {self.hpid_username}")
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, retry=2)
        self.home.verify_notification_mfe_card()
        self.home.click_devices_menu_btn()

        online_count = 0
        for printer in self.p_info:
            self.device.click_devices_group(printer[1]["group"])
            self.device.verify_device_page()
            if self.device.verify_device_status_by_serial_number(printer[1]["name"], printer[0]):
                online_count += 1

        assert online_count > 0  # At least 1 device found online
