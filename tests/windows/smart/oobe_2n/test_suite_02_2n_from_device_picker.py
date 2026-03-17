import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SPL.libs.printer.frontpanel import FrontPanel
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow

pytest.app_info = "GOTHAM"
class Test_Suite_02_2N_from_device_picker(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.fp = FrontPanel(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.yf = YetiFlowContainer(cls.driver)
        cls.moobe = cls.fc.fd["moobe"]
        cls.printers = cls.fc.fd["printers"]
        cls.ows = OwsFlow(cls.driver, cls.web_driver)
        cls.pepto = cls.fc.fd["pepto"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.firmware = cls.p.get_printer_information()["firmware version"]
        logging.debug("reset printer ....")
        cls.p.oobe_reset_printer()
        logging.debug("skip oobe ...")
        cls.p.exit_oobe()
        logging.debug("printer connecting wifi...")
        cls.p.connect_to_wifi(ssid, password)

    def test_01_2_n_oobe_from_device_picker(self):
        """
        Select network printer under test in device picker.
        Observe the flow.
        Complete the flow till printer got added to the Main UI

        Verify printer got added to the main UI
        Verify Finish setup button is not seen on the main UI
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26950682
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/26976215
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001769(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001770(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717282
        """
        printer_type = (self.firmware)[:3]
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_printer(self.p, exit_setup=False)
        self.moobe.click_button_on_fp_from_printer(self.p)
        self.yf.flow["smart_printer_consent"].verify_printer_consent_screen()
        # self.moobe.click_accept_all()
        # self.moobe.click_button_on_fp_from_printer(self.p)
        #click Learn more about this data link
        self.yf.flow["smart_printer_consent"].click_learn_more_link()
        self.web_driver.add_window("learn_more_link")
        self.web_driver.switch_window("learn_more_link")
        current_url = self.web_driver.get_current_url()
        assert "www.hpsmart.com" in current_url
        self.web_driver.close_window("learn_more_link")
        #click HP Privacy Statement link
        self.yf.flow["smart_printer_consent"].hp_privacy_statement_link()
        self.web_driver.add_window("hp_privacy_link")
        self.web_driver.switch_window("hp_privacy_link")
        current_url = self.web_driver.get_current_url()
        assert "www.hp.com" in current_url
        self.web_driver.close_window("hp_privacy_link")
        self.ows.go_through_ows_flow(printer_type, yeti_type="Flex")
      
    def test_02_check_log_info(self):
        """
        Verify User Onboarding screens don't display
        Verify Device onboarded successfully
        Verify Let's print and Share printer (invite to print) screen shows
        Verify Device status is ready on the Main UI
        Verify No setup button is shown on the Main UI
        Verify correct log line shows in the Gotham log file according to the printer type
        https://hp-testrail.external.hp.com/index.php?/cases/view/27790536 (only for Wireless connection printer)
        """
        check_event_list = ['"SetUserOnboardingCompleted","PerformPostOwsActivities","SetOWSSetupCompletedFlag"],"onboardingType":"printerSetup"'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_03_check_driver_queue(self):
        """
        Verify Roam queue (HP Smart Printing queue) is created.
        Verify normal driver is created if it's installed during the flow successfully. If not, the normal driver queue will not display.
        Verify "HP Print Scan Doctor" folder with "Printer Health Monitor" and "Printer Health Monitor logon" tasks list under the Task Scheduler (Local)->Task Scheduler Library->HP folder after accept UAC.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878719 (only for 2-N OOBE Wireless)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878721 (only for 2-N OOBE Wireless)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27885669 (only for 2-N OOBE Wireless)

        """
        self.fc.check_task_scheduler()
        bonjour_name = self.p.get_printer_information()['bonjour name']
        self.fc.verify_hp_smart_driver_install(bonjour_name)
        