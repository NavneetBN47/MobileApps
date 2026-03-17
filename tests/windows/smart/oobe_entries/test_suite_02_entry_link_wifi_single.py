import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow

pytest.app_info = "GOTHAM"
class Test_Suite_02_Entry_Link_Wifi_Single(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session
        
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]

        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]
        cls.printer_ows_type = cls.p.get_printer_information()['firmware version'][:3]
        
        cls.stack = request.config.getoption("--stack")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)

    def test_01_printer_oobe_reset(self):
        """
        Precondition: 
        Do an OOBE reset for printer
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        self.p.exit_oobe()
    
    def test_02_go_through_choose_a_printer_to_set_up_flow(self):
        """
        Click the "Set up a new printer" button on the UCDE value prop.

        Verify Device picker is launched after clicking the "Set up a new printer" button
        """
        self.fc.set_up_a_new_printer_flow()
        self.printers.verify_device_picker_screen()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)

    def test_03_select_a_beaconing_printer_to_finish_oobe_flow(self):
        """
        Select the beaconing printer on the Device picker screen.
        Follow and finish the flow with the testing printer.
        
        Verify the Gotham app directs to OOBE flow.
        Verify setup is successful.
        Verify the printer is added to the main UI after flow completed
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/28139250
        """
        self.ows_flow.find_printer_to_finish_awc_flow(self.ssid, self.password, self.p, self.printer_name)

        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")
        self.ows_flow.go_through_ows_flow(self.printer_ows_type, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()
