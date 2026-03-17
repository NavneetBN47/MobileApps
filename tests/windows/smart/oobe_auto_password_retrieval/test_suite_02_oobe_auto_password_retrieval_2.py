import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_02_OOBE_Auto_Password_Retrieval_2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.stack = request.config.getoption("--stack")
        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

        try:
            logging.info("OOBE Reset for printer...")
            oobe_reset_printer = cls.p.oobe_reset_printer()
        except Exception as e:
            pytest.skip(f"Skip this test and please test again as: {e}")
        if oobe_reset_printer:
            logging.info("Skip OOBE flow...")
            cls.p.exit_oobe()

    def test_01_select_beaconing_printer(self):
        """
        "Access Wi-Fi Password for [network]” dialog UI 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029630
        """
        self.web_driver.set_size('min')
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)
        self.moobe.verify_we_found_your_printer_screen()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)

    def test_02_input_illegal_password(self):
        """
        Click "Connect" button on "Connect printer to Wi-Fi" screen with illegal password entered, verify error message shows under password text box without proceeding
        Enter incorrect password in "Connect Printer to WiFi" screen, verify the wifi password error
        If enter a short incorrect password, the screen displays red text "Incorrect password. Try entering it again."
        "Connect printer to Wi-Fi" screen (illegal password) UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029976
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27598062
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029634
        """
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.moobe.verify_connect_printer_to_wifi_screen(self.printer_name, self.ssid)
        self.moobe.input_password("1")
        self.moobe.click_connect_printer_to_wifi_screen_connect_btn()
        self.moobe.verify_incorrect_password_text_shows()

    def test_03_input_incorrect_password(self):
        """
        Enter incorrect password in "Connect Printer to WiFi" screen, verify the wifi password error
        Click "Connect" button on "Connect printer to Wi-Fi" screen with legal/correct password entered, verify "Connecting printer to Wi-Fi" shows 
        If enter a long incorrect password, the AWC flow begin and then back to "Connect printer to Wi-Fi" screen, auto "access Wi FI password" dialog shows on "Connect printer to Wi-Fi" screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27598062
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25433910
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/32047457
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33327124
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33350374
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33350376(#2)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029974
        """
        self.moobe.input_password("incorrect_password")
        self.moobe.click_connect_printer_to_wifi_screen_connect_btn()
        self.moobe.verify_connect_to_wifi_progress_screen()
        # Handle popup and click buttons on printer
        self.moobe.handle_popup_on_connect_to_wifi_progress_screen(self.p)
        self.moobe.verify_unable_to_connect_printer_to_network_dialog(timeout=180)


    def test_04_delete_wifi_profile(self):
        self.driver.ssh.send_command('netsh wlan delete profile "HP*"')       




