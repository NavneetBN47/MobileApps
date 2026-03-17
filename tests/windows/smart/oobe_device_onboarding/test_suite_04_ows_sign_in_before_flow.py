import pytest
import logging

import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_04_OWS_Sign_In_Before_Flow(object):
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
        Sign in/Sign up before the flow
        select a beaconing printer
        """
        self.fc.go_home(create_account=True)
        assert self.home.verify_logged_in() is True
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)

    def test_03_finish_ows_flow(self):
        """
        Finish OWS flow
        Change printer stack to the one that app is
        Continue the flow and decline on the HP+ screen and all the pop up.
        """
        self.ows_flow.find_printer_to_finish_awc_flow(self.ssid, self.password, self.p, self.printer_name)

        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")

        self.ows_flow.go_through_ows_flow(self.printer_ows_type, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()

    def test_04_check_optimize_dialog_missing(self):
        """
        Verify POTG optimize dialog with "Optimize Printers" button don't show when printer display on Main UI.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27949557 (only for OOBE_AWC)
        """
        assert self.fc.enable_print_anywhere_dialog(raise_e=False) is False

    def test_05_check_print_job(self):
        """
        Put PC and printer in the same network.
        Send print job from "Print Documents"/"Print Photos"/"Scan Results"-Print icon/"Scan Results"-Smart Task icon/"Smart Tasks" with print only ST.
        
        Verify print experience is local.
        Verify print job is sent and printed right away.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27930561 (only for OOBE_AWC)
        """
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.ONE_PAGE_DOC)
        self.print.verify_ipp_print_screen_no_preview_image(raise_e=False)
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)
        self.print.verify_ipp_print_screen_document_preview_image()
        self.print.select_ipp_print_screen_print_btn()
        if self.print.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.print.select_dialog_optimize_and_print_btn()
        self.print.verify_sending_file_dialog()
        self.print.verify_file_send_dialog(timeout=120)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()

    def test_04_check_print_job(self):
        """
        Put PC and printer in the different network.
        Send print job from "Print Documents"/"Print Photos"/"Scan Results"-Print icon/"Scan Results"-Smart Task icon/"Smart Tasks" with print only ST.
        
        Verify printer shows offline after network is changed.
        Verify print experience is local.
        Verify print job is sent but cannot be printed due to printer is offline.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27961606 (only for OOBE_AWC)
        """
        self.driver.ssh.send_command("netsh wlan disconnect")
        sleep(2)
        self.home.verify_carousel_printer_status('Printer offline')
