import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "GOTHAM"
class Test_Suite_01_OWS_Sign_Up_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, clear_printer_data):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]

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

    def test_03_finish_awc_flow(self):
        """
        Finish AWC flow
        Change printer stack to the one that app is
        """
        self.ows_flow.find_printer_to_finish_awc_flow(self.ssid, self.password, self.p, self.printer_name)

        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")

    def test_04_finish_ows_sign_up_flow(self):
        """
        Try to claim yeti flex printer using the same account
        Install yeti flex printer
        Go through the printer setup flow till you see the HP+ introduction splash screen
        Click on "Do not active HP+" on the HP+ introduction screen
        Click on the "Decline HP+" button on HP+ activation decline confirmation
        Click "Continue" button on the HP+ activation decline confirmation
        Check “Setup complete! Let's print” screen when os language is ENU/ESN/DEU/FRA/CHS, verify functionality 

        Verify flow continue to printer installation and then to main UI
        Verify UCDE user remains UCDE user
        Verify "Get supplies/Ink" tile doesn't change to "Print Plan" ----N/A
        Verify HP+ orange banner doesn't show on main UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/27876769
        https://hp-testrail.external.hp.com/index.php?/cases/view/27876772
        https://hp-testrail.external.hp.com/index.php?/cases/view/14887448
        https://hp-testrail.external.hp.com/index.php?/cases/view/27876761
        https://hp-testrail.external.hp.com/index.php?/cases/view/12612358
        """
        self.ows_flow.go_through_ows_flow(self.printer_ows_type, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()

    def test_05_print_via_print_documents(self):
        """
        Click the "Print Documents" tile on the Main UI to Print.

        Verify local print UI shows when send print job.
        """
        self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_do_not_show_this_message_checkbox()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_06_print_via_print_photos(self):
        """
        Click the "Print Photos" tile on the Main UI to Print.

        Verify local print UI shows when send print job.
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()

        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_07_print_via_shortcuts_job(self):
        """
        Send a Shortcuts job which only include print job. (Shortcuts tile or scan result screen, choose one and record you option in the result part)
        
        Verify local print UI shows when send print job.
        """
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)
        self.shortcuts.click_save_shortcut_btn()
        if self.shortcuts.verify_file_already_exists_dialog():
            self.shortcuts.click_already_exists_no_btn()
        self.shortcuts.click_start_shortcut_btn()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_start_btn()
        self.scan.click_start_btn()
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.scan.verify_your_shortcut_dialog()
        sleep(5)
        self.scan.click_home_btn()
        self.home.verify_home_screen()

    def test_08_print_via_scan_results(self):
        """
        Send print job from Scan Result screen.

        Verify local print UI shows when send print job.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27894498
        """
        self.home.select_scan_tile()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.print.verify_simple_print_dialog(invisible=True)
        self.scan.verify_scan_result_screen()

    def test_09_check_print_experience_is_remote(self):
        """
        Put PC and printer in different network.

        """
        self.driver.ssh.send_command("netsh wlan disconnect")
        sleep(2)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.home.select_navbar_back_btn()

    def test_10_click_get_supplies_tile(self):
        """
        Click "Get Supplies" tile on the Main UI
        
        Verify P2 page open within the app
        Verify enrollment done in the external browser after clicking the "Get Started Now!" button
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/17155822
        """  
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_not_now_dialog():
            self.dedicated_supplies_page.select_not_now_btn()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
        else:
            self.web_driver.add_window("get_supplies")
            sleep(3)
            self.web_driver.switch_window("get_supplies")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                raise NoSuchElementException('Failed launch instant ink url')
            self.web_driver.close_window("get_supplies")
        self.home.verify_home_screen()

