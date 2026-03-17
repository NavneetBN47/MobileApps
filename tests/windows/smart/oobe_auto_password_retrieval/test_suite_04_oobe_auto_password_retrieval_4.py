import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_04_OOBE_Auto_Password_Retrieval_4(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

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
        self.fc.go_home()
        self.fc.select_a_printer(self.p, exit_setup=False, beaconing_printer=True)
        self.moobe.verify_we_found_your_printer_screen()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.moobe.verify_connect_printer_to_wifi_screen(self.printer_name, self.ssid)
        
    def test_02_click_access_password_automatically_link(self):
        """
        Go through OOBE AWC flow(Win RS5+) (Mac 10.15+), verify flow access Wi-Fi password via link
        Click "Access my Wi-Fi password automatically" link on "Connect printer to Wi-Fi" screen, verify UAC popup shows for Win and Mac OS dialog shows for Mac
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029606
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17029973
        """
        self.moobe.click_access_password_automatically_link()
        self.moobe.verify_accessing_wifi_password_text(raise_e=False)
        self.moobe.verify_connect_to_wifi_progress_screen()
        # Handle popup and click buttons on printer
        self.moobe.handle_popup_on_connect_to_wifi_progress_screen(self.p)
        self.moobe.verify_printer_connected_to_wifi_screen(self.printer_name, self.ssid)

    def test_03_delete_wifi_profile(self):
        self.driver.ssh.send_command('netsh wlan delete profile "HP*"')       




