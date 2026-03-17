import pytest
import logging
import time

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc
import SPL.driver.driver_factory as driver_factory
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"

class Test_Suite_03_2N_2_Printers_Install(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.sf = SystemFlow(cls.driver)
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.ows = OwsFlow(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
   
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        system_cfg = ma_misc.load_system_config_file()
        pp_info = system_cfg["printer_power_config"]
        db_info = system_cfg.get("database_info", None)
        cls.p_2 = driver_factory.get_printer(pp_info , db_info = db_info)
        cls.host_name_1 = cls.p.get_printer_information()['host name']
        cls.bonjour_name_1 = cls.p.get_printer_information()['bonjour name']
        cls.host_name_2 = cls.p_2.get_printer_information()['host name']
        cls.firmware = cls.p.get_printer_information()["firmware version"]
        logging.info("host name:\n {}".format(cls.host_name_1))
        logging.info("reset 1st printer ....")
        cls.p.oobe_reset_printer()
        logging.info("skip 1st printer oobe ...")
        cls.p.exit_oobe()
        logging.info("1st printer connecting wifi...")
        cls.p.connect_to_wifi(ssid, password)
        meg = cls.p.is_connected_to_wifi()
        logging.info("is 1st printer connected wifi?:\n {}".format(meg))
        logging.info("reset 2nd printer ....")
        cls.p_2.oobe_reset_printer()
        logging.info("skip 2nd printer oobe ...")
        cls.p_2.exit_oobe()
        logging.info("2nd printer connecting wifi...")
        cls.p_2.connect_to_wifi(ssid, password)
        meg_2 = cls.p_2.is_connected_to_wifi()
        logging.info("is 2nd printer connected wifi?:\n {}".format(meg_2))

    def test_01_install_2_printers_on_win_settings(self):
        value_name_1 = self.host_name_1.split("HP")[1]
        value_name_2 = self.host_name_2.split("HP")[1]
        close_activity = eval("w_const.CLOSE_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
        self.driver.terminate_app(close_activity)
        time.sleep(1)
        self.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized') 
        self.sf.select_printer_on_win_settings(value_name_1)
        time.sleep(1)
        self.sf.select_printer_on_win_settings(value_name_2)
    
    def test_02_check_choose_printer_dialog_on_main_ui(self):
        """
        Go through the privacy screens and land on the Main UI
        Select one printer form the "Choose a printer" dialog and click "Continue" button
        Click the "Finish setup" button next to the printer image
        Launch app.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/26956453
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27090169
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27090171
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731314
        """ 
        launch_activity = eval("w_const.LAUNCH_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
        printer_name_1 = self.bonjour_name_1.split(" series")[0]
        printer_type = (self.firmware)[:3]
        self.driver.launch_app(launch_activity)
        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()
        self.ows_value_prop.select_native_value_prop_buttons(index=3)
        self.home.verify_choose_a_printer_dialog()
        self.home.select_skip_btn()
        self.home.verify_carousel_add_printer_btn()
        self.fc.reset_hp_smart()
        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()
        self.ows_value_prop.select_native_value_prop_buttons(index=3)
        self.home.verify_choose_a_printer_dialog()
        self.home.click_dynamic_printer_name_locator(printer_name_1)
        self.home.verify_carousel_finish_setup_btn()
        self.home.click_finish_setup_btn()
        self.moobe.click_button_on_fp_from_printer(self.p)
        self.ows.go_through_ows_flow(printer_type)

      