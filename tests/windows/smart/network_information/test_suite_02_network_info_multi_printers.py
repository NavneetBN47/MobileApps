import pytest
from time import sleep
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import SPL.driver.driver_factory as p_driver_factory

pytest.app_info = "GOTHAM"
class Test_Suite_02_Network_Info_Multi_Printers(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        # # Initializing Printer1
        cls.p = load_printers_session
        cls.bon_name = cls.p.get_printer_information()["bonjour name"]
        cls.host_name = cls.p.get_printer_information()["host name"]
        cls.ip = cls.p.get_printer_information()["ip address"]
        cls.is_dune = False
        if 'dune' in str(cls.p):
            cls.is_dune = True
            cls.ip = cls.p.p_con.ethernet_ip_address

        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()
        logging.info("Another Printer Information:\n {}".format(cls.printer_info2))

        cls.bon_name2 = cls.p2.get_printer_information()["bonjour name"]
        cls.host_name2 = cls.p2.get_printer_information()["host name"]
        cls.ip2 = cls.p2.get_printer_information()["ip address"]
        cls.is_dune2 = False
        if 'dune' in str(cls.p):
            cls.is_dune2 = True
            cls.ip2 = cls.p2.p_con.ethernet_ip_address

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.printer_status = {}

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

    def test_01_add_two_printers(self):
        """
        Select a different random printer from the following list from device picker to main UI.
        USB connected + LEDM printer (not covered) 
        USB connected + non-LEDM printer (not covered)
        Wireless connected + LEDM printer
        Wireless connected + non-LEDM printer *Wired connected + LEDM printer
        Wired connected + non-LEDM printer
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        self.fc.select_a_printer(self.p2, add_new=True)
        assert self.home.verify_pagination_text().get_attribute("Name") == "2 of 2 printers."
        
    def test_02_verify_second_printer_network_info(self):
        """
        Click Printer Settings->Network Information

        Use Network Information_values.xlsx to check all applicable settings display correctly.
        """
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.select_network_information()
        self.printer_settings.verify_network_info_page(self.bon_name2, self.ip2, self.host_name2, self.ssid, self.is_dune2)

    def test_03_switch_to_first_printer(self):
        """
        Switch between different printers.
        """
        self.home.select_navbar_back_btn()
        self.home.click_previous_device_btn()
        self.home.verify_setup_or_add_printer_card()
        sleep(8)
        assert self.home.verify_pagination_text().get_attribute("Name") == "1 of 2 printers."

    def test_04_verify_first_printer_network_info(self):
        """
        Click Printer Settings->Network Information

        Use Network Information_values.xlsx to check all applicable settings display correctly.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14788132
        """
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.select_network_information()
        self.printer_settings.verify_network_info_page(self.bon_name, self.ip, self.host_name, self.ssid, self.is_dune)
