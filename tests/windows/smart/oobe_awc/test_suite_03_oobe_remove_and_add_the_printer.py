import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_03_OOBE_Remove_And_Add_The_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, clear_printer_data):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.sf = SystemFlow(cls.driver)
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.system_preferences = cls.fc.fd["system_preferences"]

        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]
        cls.printer_ows_type = cls.p.get_printer_information()['firmware version'][:3]

        cls.stack = request.config.getoption("--stack")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

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
        Launch the app and click on the plus '+' icon
        Click on 'Set up a new printer' link and choose a beaconing printer
        """
        self.fc.disable_printer_driver_auto_install()
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

    def test_04_go_to_remove_and_add_the_printer_screen(self):
        """
        Select "Driver Unavailable"

        Ensure the title of the page is "Remove and add printer again"
        Ensure the page is displayed and matches the images below

        https://hp-testrail.external.hp.com/index.php?/cases/view/31531283
        https://hp-testrail.external.hp.com/index.php?/cases/view/31531340
        """
        self.ows_flow.go_through_ows_skip_flow(self.printer_ows_type, yeti_type="Flex", install_driver=True)
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.moobe.verify_print_from_other_devices()
        self.moobe.select_skip_this_step()
        self.moobe.verify_install_driver_to_print_screen()
        self.moobe.click_driver_unavailable_btn()
        self.moobe.verify_remove_and_add_screen()

    def test_05_click_hp_support_link_and_back_button(self):
        """
        Verify Functionality of the "Back" button, and return
        Verify Functionality of the "Hp Support" link and return
        
        Verify selecting "back" takes the user to the previous page
        Ensure selecting "hp support" takes the user the HP support web page
        """
        self.moobe.click_hp_support_link()
        self.web_driver.wait_for_new_window(timeout=15)
        self.web_driver.add_window("hp_support")
        sleep(3)
        self.web_driver.switch_window("hp_support")
        sleep(3)
        current_url = self.web_driver.get_current_url()
        if 'support.hp.com' in current_url:
            raise NoSuchElementException('Failed launch HP Support url')
        self.web_driver.close_window("hp_support")

        self.moobe.click_back_btn()
        self.moobe.verify_install_driver_to_print_screen()

    def test_06_click_printers_and_scanners_button(self):
        """
        Verify Functionality of the "printer & Scanners" and return

        Verify Selecting "printers & scanners" opens the devices printers and scanner screen
        """
        self.moobe.click_driver_unavailable_btn()
        self.moobe.verify_remove_and_add_screen()
        self.moobe.click_printers_scanners_btn()
        self.system_preferences.verify_win_printers_and_scanners_screen()
        try:
            value_name = self.host_name.split("HP")[1]
            self.sf.select_printer_on_win_settings(value_name)
        finally:
            sleep(2)
            self.driver.ssh.send_command('Stop-Process -Name "*SystemSettings*"')

    def test_07_click_continue_button(self):
        """
        Select "Continue"
        Verify selecting "Continue" continues the flow
        Check “Setup complete! Let's print” screen when os language is ENU/ESN/DEU/FRA/CHS, verify functionality
        “Setup complete! Let's print” screen UI 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12612358
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12701145
        """
        self.moobe.select_continue()
        self.moobe.verify_setup_complete_lets_print()
        self.moobe.select_print_btn()

        self.print.verify_simple_print_dialog()
        hostname = self.p.get_printer_information()["host name"]
        self.print.select_printer(hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_printer_add_to_carousel()
