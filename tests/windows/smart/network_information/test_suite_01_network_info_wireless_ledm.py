import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Network_Info_Wireless_Ledm(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
       
        cls.bon_name = cls.p.get_printer_information()["bonjour name"]
        cls.host_name = cls.p.get_printer_information()["host name"]
        cls.ip = cls.p.get_printer_information()["ip address"]
        cls.is_dune = False
        if 'dune' in str(cls.p):
            cls.is_dune = True
            cls.ip = cls.p.p_con.ethernet_ip_address

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, cls.ssid, password)
        sleep(3)

    def test_01_add_a_printer(self):
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_go_to_network_info_screen(self):
        """
        Wireless connected + LEDM printer

        Verify Network Information is displayed correctly like below:
        * Network + LEDM = Network Information screen
        Verify the "Wi-fi Direct" section doesn't show
        Verify BLE information shows in Network Information page
        Verify Ethernet and Wireless section shows as connected in in Network Information page

        https://hp-testrail.external.hp.com/index.php?/cases/view/14788133
        https://hp-testrail.external.hp.com/index.php?/cases/view/29628392
        https://hp-testrail.external.hp.com/index.php?/cases/view/29628393
        https://hp-testrail.external.hp.com/index.php?/cases/view/29639937
        https://hp-testrail.external.hp.com/index.php?/cases/view/25355812
        https://hp-testrail.external.hp.com/index.php?/cases/view/14788147 (part)
        https://hp-testrail.external.hp.com/index.php?/cases/view/14788144
        """
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.select_network_information()
        self.printer_settings.verify_network_info_page(self.bon_name, self.ip, self.host_name, self.ssid, self.is_dune)

    def test_03_turn_off_printer_wireless(self):
        """
        Trigger a printer offline status for the test printer.
        """
        self.fc.trigger_printer_offline_status(self.p)
        self.home.select_navbar_back_btn()
        self.home.verify_carousel_printer_offline_status()

    def test_04_verify_network_info_list_unclickable(self):
        """
        Click Printer Settings->Network Information

        Verify Network Information is grayed out and unclickable.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14788134
        https://hp-testrail.external.hp.com/index.php?/cases/view/14788135
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_network_information()
        self.printer_settings.verify_printer_settings_page()
        