import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
import logging


pytest.app_info = "GOTHAM"
class Test_Suite_01_Check_OOBE_Log(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        # Initializing Printer1
        cls.p = load_printers_session
        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()
        logging.info("Another Printer Information:\n {}".format(cls.printer_info2))

        cls.home = cls.fc.fd["home"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.printers = cls.fc.fd["printers"]
        cls.about = cls.fc.fd["about"]

        cls.stack = request.config.getoption("--stack")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

        cls.compare_size = {}
        cls.logs_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\Logs'
        cls.gotham_oobe_log = cls.logs_path + '\HPSmart_OOBE.log'

    def test_01_printer_oobe_reset(self):
        """
        Precondition: Do an OOBE reset for printer
        Start and finish an OOBE_AWC setup flow.
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer_1 = self.p.oobe_reset_printer()
        oobe_reset_printer_2 = self.p2.oobe_reset_printer()
        if not oobe_reset_printer_1 or not oobe_reset_printer_2:
            raise Exception("Printer OOBE reset failed")
        self.p.exit_oobe()
        self.p2.exit_oobe()

    def test_02_uncheck_oobe_logging_toggle(self):
        """
        Uncheck the OOBE logging checkbox.
        Save the setting.

        Verify OOBE logging is turned off.
        Verify "Settings saved" dialog displays with a close button.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815133
        """   
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)
        assert self.about.get_toggle_status(0) == 1
        self.about.click_toggle(0)
        assert self.about.get_toggle_status(0) == 0
        self.about.click_save_setting_button()
        self.about.verify_settings_saved_dialog()
        self.about.click_dialog_close_button()
        sleep(1)
        self.compare_size['f_size'] = self.about.get_file_size(self.gotham_oobe_log)

    def test_03_start_a_awc_flow(self):
        """
        Go to the main page
        Select a beaconing printer to finish AWC flow  
        """
        self.home.select_navbar_back_btn(return_home=False)
        self.about.verify_about_screen()
        self.home.select_navbar_back_btn()
        self.__start_awc_flow(self.p)

    def test_04_check_log_size_not_increase(self):
        """
        Start a new OOBE process.  

        Verify the size of OOBE log file does not increase

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815134
        """
        self.compare_size['s_size'] = self.about.get_file_size(self.gotham_oobe_log)
        logging.info("first size {} / second size {}".format(self.compare_size['f_size'], self.compare_size['s_size']))
        assert self.compare_size['f_size'] == self.compare_size['s_size']

    def test_05_relaunch_app_and_start_another_awc_flow(self):
        """
        Re-launch App to start a new OOBE process.  
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.__start_awc_flow(self.p2)

    def test_06_check_log_size_not_increase(self):
        """
        Verify no new OOBE log file is created under HPSmart folder.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815135
        """
        self.compare_size['t_size'] = self.about.get_file_size(self.gotham_oobe_log)
        logging.info("first size {} / third size {}".format(self.compare_size['f_size'], self.compare_size['t_size']))
        assert self.compare_size['f_size'] == self.compare_size['t_size']

    def __start_awc_flow(self, p_obj):
        """
        Select a beaconing printer to start a AWC flow  
        """   
        bonjour_name = p_obj.get_printer_information()['bonjour name']
        printer_name = bonjour_name[bonjour_name.find("HP ") + 3:bonjour_name.find("series") - 1]
        self.fc.select_a_printer(p_obj, exit_setup=False, beaconing_printer=True)
        self.moobe.verify_we_found_your_printer_screen()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)
        self.moobe.click_access_wifi_password_dialog_no_thanks_btn()
        self.moobe.input_password(self.password)
        self.moobe.click_connect_printer_to_wifi_screen_connect_btn()
        self.moobe.verify_connect_to_wifi_progress_screen()
        # Handle popup and click buttons on printer
        self.moobe.click_button_on_fp_from_printer(p_obj)
        self.moobe.verify_printer_connected_to_wifi_screen(printer_name, self.ssid)
        self.printers.select_exit_setup()
        self.printers.verify_exit_setup_btn()
        if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
            self.printers.select_pop_up_exit_setup()
        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()