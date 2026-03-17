import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_04_Entry_Hp_Webpage(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.sf = SystemFlow(cls.driver)
        cls.p = load_printers_session
        
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]

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
        Precondition: Do an OOBE reset for printer
        Start and finish an OOBE_AWC setup flow.
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Skip oobe flow...")
        self.p.exit_oobe()
        self.p.connect_to_wifi(self.ssid, self.password)

    def test_02_open_hp_webpage(self):
        """
        Open IE/Edge, input "123.hp.com"
        Input a printer series name (like "HP Envy 7640") and then click "Next" button on the webpage
        Click on the "Install HP Smart App" button on the webpage
        """  
        self.web_driver.set_size("max")
        self.sf.install_app_on_123_hp_web('9010')
        self.sf.launch_app_on_mircosoft_store()

    def test_03_finish_oobe_flow(self):
        """
        Click big "+" on the Main UI.
        Click "My printer isn't listed " link on the Device picker screen.
        Follow and finish the flow with the testing printer.

        Verify Gotham app directs to OOBE flow where a user can install the not discovered printer in Device Picker via USB/Ethernet/Wireless.
        Verify setup is successful.
        Verify printer is added to main UI after flow completed.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/12797529
        """
        self.fc.go_home(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p, exit_setup=False)
        self.ows_flow.go_through_wireless_ows_flow(self.printer_ows_type, self.p, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()
