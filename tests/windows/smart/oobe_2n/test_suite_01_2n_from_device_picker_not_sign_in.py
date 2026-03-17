import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_2N_From_Device_Picker_Not_Sign_In(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.printers = cls.fc.fd["printers"]

        cls.printer_ows_type = cls.p.get_printer_information()['firmware version'][:3]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        
    def test_01_printer_oobe_reset(self):
        """
        Test printer: Novelli-086 (HP ENVY Inspire 7200 series)

        Precondition: 
        *1 Clear printer data in Cloud 
        *2 Do an OOBE reset for printer
        *3 Change printer stack to the that one app is
        *4 Connect printer wifi
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Stack Reset for printer...")
        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")
        self.p.exit_oobe()
        self.p.connect_to_wifi(self.ssid, self.password)

    def test_02_select_a_printer(self):
        """
        Select network printer under test in device picker.
        Sign in with the new account
        Try to claim yeti e2e printer using same accountss
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/24615695

        https://hp-testrail.external.hp.com/index.php?/cases/view/24641220
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False)
        self.ows_flow.go_through_wireless_ows_flow(self.printer_ows_type, self.p, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()

    def test_04_check_driver_queue(self):
        """
        Verify Roam queue (HP Smart Printing queue) is created.
        Verify normal driver is created if it's installed during the flow successfully. If not, the normal driver queue will not display.
        Verify "HP Print Scan Doctor" folder with "Printer Health Monitor" and "Printer Health Monitor logon" tasks list under the Task Scheduler (Local)->Task Scheduler Library->HP folder after accept UAC.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/27885670 (only for 2-N OOBE Wireless)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878720 (only for 2-N OOBE Wireless)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878722 (only for 2-N OOBE Wireless)
        """
        self.fc.check_task_scheduler()
        bonjour_name = self.p.get_printer_information()['bonjour name']
        self.fc.verify_hp_smart_driver_install(bonjour_name)
      