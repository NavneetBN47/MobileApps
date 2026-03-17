import pytest
import logging
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_02_OWS_Sign_In_Flow(object):
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
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.pepto = cls.fc.fd["pepto"]

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

    def test_03_finish_awc_sign_in_flow(self):
        """
        Finish AWC flow
        Change printer stack to the one that app is
        """
        self.ows_flow.find_printer_to_finish_awc_flow(self.ssid, self.password, self.p, self.printer_name)

        if not self.p.send_secure_cfg(self.stack):
            raise Exception("Printer stack reset failed")

    def test_04_finish_ows_sign_in_flow(self):
        """
        Click "Sign in" button on the "Sign in to register your printer for warranty screen".

        https://hp-testrail.external.hp.com/index.php?/cases/view/27818954 (only for OOBE_AWC)
        """
        username = self.login_info["email"]
        password = self.login_info["password"]
        self.ows_flow.go_through_ows_sign_in_flow(self.printer_ows_type, username, password, yeti_type="Flex")
        self.home.verify_printer_add_to_carousel()

    def test_05_check_log_info(self):
        """
        Verify User Onboarding screens don't display
        Verify Device onboarded successfully
        Verify Device status is ready on the Main UI
        Verify No setup button is shown on the Main UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/27793125 (only for OOBE_AWC) 
        """
        if self.p.is_yeti():
            check_event_list = ['"noRemainingActions": false, "actions": [{"command": "PerformPostOwsActivities", "params": {"activities": [{"printerInstallSession": true}, {"firstPrint": false}, {"printFromOtherDevices": false}, {"addPrinter": false}, {"postAfuPrinterInstallSession": false}]}', '"SetUserOnboardingCompleted","PerformPostOwsActivities","SetOWSSetupCompletedFlag"],"onboardingType":"printerSetup"'] 
        else:
            check_event_list = ['"SetUserOnboardingCompleted","PerformPostOwsActivities"],"onboardingType":"printerSetup"']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_06_check_driver_queue(self):
        """
        Verify Roam queue (HP Smart Printing queue) is created.
        Verify normal driver is created if it's installed during the flow successfully. If not, the normal driver queue will not display.
        Verify "HP Print Scan Doctor" folder with "Printer Health Monitor" and "Printer Health Monitor logon" tasks list under the Task Scheduler (Local)->Task Scheduler Library->HP folder after accept UAC.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878058 (only for OOBE_AWC)
        https://hp-testrail.external.hp.com/index.php?/cases/view/27878057 (only for OOBE_AWC)
        """
        self.fc.check_task_scheduler()
        bonjour_name = self.p.get_printer_information()['bonjour name']
        self.fc.verify_hp_smart_driver_install(bonjour_name)

    def test_07_check_print_experience_is_remote(self):
        """
        Put PC and printer in different network.

        """
        self.driver.ssh.send_command("netsh wlan disconnect")
        sleep(2)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.home.select_navbar_back_btn()

    def test_08_print_via_print_documents(self):
        """
        Click the "Print Documents" tile on the Main UI to Print.

        Verify remote print UI shows when send print job.
        """
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.__start_a_remote_print(print_type='doc')

    def test_09_print_via_print_photos(self):
        """
        Click the "Print Photos" tile on the Main UI to Print.

        Verify remote print UI shows when send print job.
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.__start_a_remote_print(print_type='pho')
        self.print.verify_ipp_print_screen_photo_preview_image()

    def test_10_print_via_shortcuts_job(self):
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
        self.scan.verify_couldnt_connect_to_scanner_screen()
        self.scan.click_get_started_btn()
        self.scan.select_import_btn()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)       
        self.scan.verify_import_screen()
        sleep(1)
        self.scan.click_import_apply_btn()
        self.scan.verify_start_btn()
        self.scan.click_start_btn()
        self.__start_a_remote_print(w_const.TEST_DATA.FISH_PNG, print_type='pho')
    
    def test_11_print_via_scan_results(self):
        """
        Send print job from Scan Result screen.

        Verify remote print UI shows when send print job.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27894514
        """
        self.home.select_scan_tile()
        self.scan.verify_couldnt_connect_to_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)       
        self.scan.verify_import_screen()
        sleep(1)
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.__start_a_remote_print(w_const.TEST_DATA.FISH_PNG, print_type='pho')

    def test_12_disconnect_printer_wireless(self):
        """
        Simulate an error for the remote printer (Put printer offline/ Disconnect network).

        """
        self.p.turn_off_fake_mode()
        self.home.verify_carousel_printer_offline_status()

    def test_13_verify_we_are_having_trouble_dialog(self):
        """
        Click "Print" button on the Scan Result screen to go to the Print Documents screen and check.

        Verify timeout dialogue appears with "Try Again" and "Cancel" button.
        Verify "Cancel" button dismiss the Time out dialog.
        Verify "Try Again" button shows the Print Documents screen with getting your printer status string.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/14064113
        """
        self.home.select_scan_tile()
        self.scan.verify_couldnt_connect_to_scanner_screen()
        self.scan.select_import_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)       
        self.scan.verify_import_screen()
        sleep(1)
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.print.verify_getting_remote_printer_status_text()
        self.scan.verify_we_are_having_trouble_dialog()
        self.scan.click_ipp_try_again_button()
        self.scan.verify_we_are_having_trouble_dialog()
        self.scan.click_ipp_cancel_button()
        self.scan.verify_scan_result_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __start_a_remote_print(self, print_type):
        self.print.verify_ipp_print_screen_no_preview_image(raise_e=False)
        self.print.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.print.verify_creating_preview_text(timeout=45, invisible=True)
        
        if print_type == 'doc':
            self.print.verify_ipp_print_screen_document_preview_image()
        elif print_type == 'pho':
            self.print.verify_ipp_print_screen_photo_preview_image()

        self.print.select_ipp_print_screen_print_btn()
        self.print.verify_optimize_for_faster_remote_printing_dialog()
        self.print.select_dialog_optimize_and_print_btn()
        self.print.verify_sending_file_dialog()
        self.print.verify_file_send_dialog(timeout=120)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()

    