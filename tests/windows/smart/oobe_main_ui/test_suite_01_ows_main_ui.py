import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_01_OWS_Main_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, clear_printer_data):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]

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
        
    def test_02_go_through_ows_flow_and_claimed_a_printer(self):
        """
        Claimed a printer
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)
        self.ows_flow.find_printer_to_finish_awc_flow(self.ssid, self.password, self.p, self.printer_name)

        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")

        username = self.login_info["email"]
        password = self.login_info["password"]
        self.ows_flow.go_through_ows_sign_in_flow(self.printer_ows_type, username, password, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()

    def test_03_check_printer_is_remote(self):
        """
        Put PC and printer in different network.
        """
        self.driver.ssh.send_command("netsh wlan disconnect")
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.home.select_navbar_back_btn()

    def test_04_clear_app_data_and_relaunch(self):
        """
        Clear HP Smart app data
        Launch App and sign in a HP account claimed with printer. (Make sure claimed printer and computer are don't in the same network)
        """
        self.fc.sign_out()
        self.fc.reset_hp_smart()
        self.fc.go_home(self.username, self.password)

    def test_05_select_a_remote_printer_and_check_printer_is_local(self):
        """
        Launch Device Picker.
        Select a remote printer from device picker.

        Verify printer icon is the local icon.
        Verify ink level shows on main UI.
        Verify local printer features are seen in Printer Settings.
       
        Verify Scan print experience shows local print experience.

        https://hp-testrail.external.hp.com/index.php?/cases/view/17843677
        https://hp-testrail.external.hp.com/index.php?/cases/view/17843674
        """
        self.fc.select_a_remote_printer()
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        self.home.verify_carousel_estimated_supply_image(raise_e=False)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_status_tile()
        self.printer_settings.verify_information_tile()
        self.printer_settings.verify_settings_tile()
        self.printer_settings.verify_tools_tile()
        self.printer_settings.verify_manage_tile()
        self.printer_settings.verify_print_anywhere_option_is_hidden()

    def test_06_print_via_print_documents(self):
        """
        Verify native print experience is seen.
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

    def test_07_print_via_print_photos(self):
        """
        Verify native print experience is seen.
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()

        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.verify_simple_print_dialog()

        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_08_print_via_shortcuts_job(self):
        """
        Verify Smart Tasks print experience shows local print experience.
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

    def test_09_print_via_scan_results(self):
        """
        Verify Scan print experience shows local print experience.
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

    def test_10_check_printer_is_remote_and_logout(self):
        """
        Change printer or computer network to make them in different network, the printer become remote status again.
        Launch App Settings->click "Sign out"->sign out the hp account.
        
        Verify printer is not removed from main UI [Note: Once printer becomes local printer will not remove after signout]

        https://hp-testrail.external.hp.com/index.php?/cases/view/17843689
        """
        self.driver.ssh.send_command("netsh wlan disconnect")
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.home.select_navbar_back_btn()
        self.fc.sign_out()
        self.home.verify_carousel_printer_image()

