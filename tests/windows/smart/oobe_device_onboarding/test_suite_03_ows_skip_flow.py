import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow

pytest.app_info = "GOTHAM"
class Test_Suite_03_OWS_Skip_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, clear_printer_data):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]
        cls.printer_ows_type = cls.p.get_printer_information()['firmware version'][:3]

        cls.stack = request.config.getoption("--stack")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

    def test_01_printer_oobe_reset(self):
        """
        Precondition: 
        *1 Clear printer data in Cloud 
        *2 Do an OOBE reset for printer
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        self.p.exit_oobe()
        
    def test_02_select_a_beaconing_printer(self):
        """
        select a beaconing printer
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)

    def test_03_finish_awc_flow(self):
        """
        Finish AWC flow
        Change printer stack to the one that app is
        """
        self.ows_flow.find_printer_to_finish_awc_flow(self.ssid, self.password, self.p, self.printer_name)

        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")

    def test_04_finish_ows_sign_in_flow(self):
        """
        Continue the flow and decline on the HP+ screen and all the pop up.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27809295 (only for OOBE_AWC)
        """
        self.ows_flow.go_through_ows_skip_flow(self.printer_ows_type, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()
