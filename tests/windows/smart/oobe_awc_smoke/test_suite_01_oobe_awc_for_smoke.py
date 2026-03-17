import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_01_OOBE_AWC_For_Smoke(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.stack = request.config.getoption("--stack")
        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

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

    def test_02_select_a_beaconing_printer(self):
        """
        Go through flow to Device picker screen and select a beaconing printer.
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)

    def test_03_check_awc_flow(self):
        """
        Check AWC flow
        """
        self.moobe.verify_we_found_your_printer_screen()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)
        
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.moobe.verify_connect_printer_to_wifi_screen(self.printer_name, self.ssid)

        self.moobe.input_password(self.password)
        self.moobe.click_connect_printer_to_wifi_screen_connect_btn()

        self.moobe.verify_connect_to_wifi_progress_screen()
        # Handle popup and click buttons on printer
        self.moobe.handle_popup_on_connect_to_wifi_progress_screen(self.p)
        self.moobe.verify_printer_connected_to_wifi_screen(self.printer_name, self.ssid)
        self.moobe.select_continue(change_check={"wait_obj": "printer_connected_to_wifi_screen_title", "invisible": True})
        self.moobe.verify_connected_printing_services_screen(timeout=60)

    def test_04_exit_awc_flow_to_home(self):
        self.printers.select_exit_setup()
        self.printers.select_pop_up_exit_setup()
        if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
            self.printers.select_pop_up_exit_setup()

        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()

    def test_05_delete_wifi_profile(self):
        self.driver.ssh.send_command('netsh wlan delete profile "HP*"')
    