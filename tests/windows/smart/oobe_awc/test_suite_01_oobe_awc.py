import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_01_OOBE_AWC(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        
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
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12607633
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797882
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Skip oobe flow...")
        self.p.exit_oobe()
        self.web_driver.set_size('min')

    def test_02_go_to_device_picker_screen(self):
        """
        Go through flow to Device picker screen
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)

    def test_03_check_we_found_your_printer_screen(self):
        """
        Check “We found your printer!” screen, verify functionality
        “We found your printer!” screen UI

        Verify "Printer setup is incomplete" dialog shows after click on "Exit Setup" for Win/Home icon for mac. 
        Verify "Connect printer to Wi-Fi" screen shows after click on "Continue" button.
        Put printer in beaconing mode, verify printer is found in Device Picker
        Select a found beaconing printer, verify OOBE is initiated
        Click on "Set Up" button on a discovered beaconing printer, verify OOBE is initialized 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12607635
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12607638
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029630
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13258910
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13258914
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16942938
        """
        self.moobe.verify_we_found_your_printer_screen()
        
        self.__check_exit_setup_btn()
        self.moobe.verify_we_found_your_printer_screen()

        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)
        
    def test_04_check_connect_printer_to_wifi_screen(self):
        """
        Check “Connect printer to Wi-Fi” screen, verify functionality
        “Connect printer to Wi-Fi” screen UI
        Click "No, Thanks" button on "Access Wi-Fi Password for [network]” dialog, verify dialog dismisses and "Connect printer to Wi-Fi" screen shows 
        "Need help connecting printer to Wi-Fi?" dialog UI
        Click "Continue" button on the "Need help connecting printer to Wi-Fi?" dialog, verify "Connect printer to Wi-Fi"screen show

        Verify info icon opens up "Need help connecting printer to Wi-Fi" dialog.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12607637
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12701123
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029958
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28800039
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28800040
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28800046
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029971
        """
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.moobe.verify_connect_printer_to_wifi_screen(self.printer_name, self.ssid)

        self.__check_exit_setup_btn()
        self.moobe.verify_connect_printer_to_wifi_screen(self.printer_name, self.ssid)

        self.moobe.click_connect_printer_to_wifi_screen_i_icon_btn()
        self.moobe.verify_need_help_connecting_printer_to_wifi_dialog()
        self.moobe.click_help_dialog_continue_btn()

        self.moobe.click_connect_printer_to_wifi_screen_change_network_link()
        self.moobe.verify_change_wifi_network_dialog()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()

    def test_05_input_password(self):
        self.moobe.input_password(self.password)
        self.moobe.click_connect_printer_to_wifi_screen_connect_btn()
        self.web_driver.set_size('min')

    def test_06_check_connect_to_wifi_screen(self):
        """
        Check “Connect to Wi-Fi” screen, verify functionality
        “Connect to Wi-Fi” screen UI 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12610932
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029635
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12701125
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17465447
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17465457
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464921(high)
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464930(low)
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/25430559
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17408611
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464881(low)
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29970868
        """
        self.moobe.verify_connect_to_wifi_progress_screen()

        # Handle popup and click buttons on printer
        self.moobe.handle_popup_on_connect_to_wifi_progress_screen(self.p)

    def test_07_check_connect_to_wifi_screen(self):
        """
        Check “Printer connected to Wi-Fi” screen, verify functionality
        "Printer Connected to Wi-Fi” screen UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12610935
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029636
        """
        self.moobe.verify_printer_connected_to_wifi_screen(self.printer_name, self.ssid)

        self.__check_exit_setup_btn()
        self.moobe.verify_printer_connected_to_wifi_screen(self.printer_name, self.ssid)

    def test_08_complete_awc_flow_to_home(self):
        self.printers.select_exit_setup()
        self.printers.select_pop_up_exit_setup()
        if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
            self.printers.select_pop_up_exit_setup()

        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()

    def test_09_check_privacy_preference(self):
        """
        Click "Exit setup" on the printer privacy screen during OOBE and land on the Main ui
        Check printer privacy preference under printer setting

        Verify Privacy preference entry should not display under printer settings

        https://hp-testrail.external.hp.com/index.php?/cases/view/29364538
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        assert self.printer_settings.verify_privacy_preferences_tile(raise_e=False) is False
        self.home.select_navbar_back_btn()

    def test_10_send_print_job(self):
        """
        Set up printer via AWC on 2.4G network, verify setup is successful
        Send a print job after flow is completed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12612371
        """
        self.web_driver.set_size('min')
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen(timeout=60)
        self.home.select_print_documents_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            if self.home.verify_success_printer_installed_dialog(timeout=120, raise_e=False):
                self.home.select_success_printer_installed_ok_btn()
                self.home.verify_home_screen()
                self.home.select_print_documents_tile()
            else:
                self.home.verify_printer_driver_installed_failed_dialog(timeout=300)
                self.home.select_printer_driver_installed_failed_later_btn()
                self.home.verify_home_screen()
                pytest.skip("Printer driver could not be installed successfully, so skip this test")
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_supported_document_file_types_dialog_ok_btn()

        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        hostname = self.p.get_printer_information()["host name"][:-1]
        self.print.select_printer(hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

    def test_10_delete_wifi_profile(self):
        self.driver.ssh.send_command('netsh wlan delete profile "HP*"')
    

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __check_exit_setup_btn(self):
        """
        Check "Setup incomplete" dialog during AWC flow, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12812960
        """
        self.printers.verify_exit_setup_btn()
        self.printers.select_exit_setup()
        self.printers.verify_printer_setup_is_incomplete_dialog()
        self.printers.select_popup_back_btn()
        assert self.printers.verify_printer_setup_is_incomplete_dialog(timeout=5, raise_e=False) is False