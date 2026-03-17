import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow

pytest.app_info = "GOTHAM"
class Test_Suite_01_Cdm_Printer_Connected(object):
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

        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]
        cls.printer_ows_type = cls.p.get_printer_information()['firmware version'][:3]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

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
        
    def test_02_select_a_beaconing_printer(self):
        """
        select a beaconing printer
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)

    def test_03_go_to_printer_connected_to_wifi_screen(self):
        """
        Follow on screen instruction until printer is connected to network
        Observe " Printer connected to Wi-Fi" "Printer Connected"(oobePrinterConnected) screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/37527506
        """
        self.moobe.verify_we_found_your_printer_screen()
        self.moobe.select_continue()
        self.moobe.verify_awc_flow(self.ssid, self.password, self.p)
        self.moobe.verify_printer_connected_to_wifi_screen(self.printer_name, self.ssid)

    def test_04_click_exit_setup_button(self):
        """
        Click "ExitSetup" button on Printer connected to Wi-Fi screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/37527508
        """
        self.printers.click_exit_setup_btn()
        self.printers.verify_printer_setup_is_incomplete_dialog()
        self.printers.select_popup_back_btn()
        self.moobe.verify_printer_connected_to_wifi_screen(self.printer_name, self.ssid)

    def test_05_click_continue_button(self):
        """
        Click "Continue" button "Printer connected to Wi-Fi" /"Printer Connected"(oobePrinterConnected) screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/37527507
        """
        self.moobe.select_continue(check_kibana=True)
        self.moobe.verify_connected_printing_services_screen()
