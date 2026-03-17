import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_preferences import SystemPreferences
from SPL.libs.printer.frontpanel import FrontPanel
from MobileApps.libs.ma_misc import ma_misc
import SPL.driver.driver_factory as driver_factory

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"

class Test_Suite_07_non_hero_computer_on_wifi(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.fp = FrontPanel(cls.driver)
        
        cls.home = cls.fc.fd["home"]
        cls.sp = SystemPreferences(cls.driver)

        cls.moobe = cls.fc.fd["moobe"]
        cls.printers = cls.fc.fd["printers"]
        cls.stack = request.config.getoption("--stack")
        system_cfg = ma_misc.load_system_config_file()
        pp_info = system_cfg["printer_power_config"]
        db_info = system_cfg.get("database_info", None)
        cls.p_2 = driver_factory.get_printer(pp_info , db_info = db_info)
   
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.host_name = cls.p.get_printer_information()['model name']
        logging.debug("reset 1st printer ....")
        cls.p.oobe_reset_printer()
        logging.debug("skip 1st printer oobe ...")
        cls.p.exit_oobe()
        logging.debug("reset 2nd printer ....")
        cls.p_2.oobe_reset_printer()
        logging.debug("skip 2nd printer oobe ...")
        cls.p_2.exit_oobe()

    def test_01_check_choose_a_printer_to_set_up_screen(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797885(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24409871
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29597046
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_choose_a_printer_to_set_up_screen()

    def test_02_check_change_wifi_network_dialog(self):
        """
        Check "Change Wi-Fi network" dialog, verify functionality
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797892(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797524
        """
        printer_name=self.host_name.split(" series")[0]
        special_name=self.host_name.split(" series")[0].split("HP ")[1]
        self.printers.select_set_up_printer(printer_name)
        self.moobe.verify_access_wifi_password_dialog()
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.printers.select_exit_setup()
        self.printers.verify_setup_incomplete_dialog_2()
        self.printers.select_popup_back_btn()
        self.moobe.verify_connect_printer_to_wifi_screen(special_name, self.ssid)
        self.moobe.click_change_network_link()
        self.moobe.verify_change_wifi_network_dialog()
        self.moobe.click_dialog_open_network_settings_btn()
        self.sp.verify_network_status_page()
        self.sp.click_close_btn()
 
    def test_03_check_change_wifi_network_dialog(self):
        """
        Check "Need help connecting printer to Wifi?" dialog, verify functionality
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797890(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797521
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797870
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12865244
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28800043
        """
        self.moobe.verify_change_wifi_network_dialog()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog()
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.moobe.verify_connect_printer_to_wifi_screen()
        self.moobe.click_connect_printer_to_wifi_screen_i_icon_btn()
        self.moobe.verify_need_help_connecting_printer_to_wifi_dialog()
        self.moobe.click_dialog_change_connection_btn()
        self.printers.verify_what_type_of_printer_screen()
        self.printers.select_exit_setup()
        self.printers.verify_setup_incomplete_dialog_2()
