import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow
import logging


pytest.app_info = "GOTHAM"
class Test_Suite_02_Check_OOBE_Log_Checked(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ows_flow = OwsFlow(cls.driver, cls.web_driver)
        cls.p = load_printers_session

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
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        self.p.exit_oobe()

    def test_02_go_to_developer_tools_screen(self):
        """
        Open Developer Tools screen by Click 10 or more times on the app logo of about screen.
        """   
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)
        assert self.about.get_toggle_status(0) == 1
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

    def test_04_check_log_size_increase(self):
        """
        Run OOBE and then go to HP Smart folder.

        Verify the OOBE log file is created

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815129
        """
        self.compare_size['s_size'] = self.about.get_file_size(self.gotham_oobe_log)
        logging.info("first size {} / second size {}".format(self.compare_size['f_size'], self.compare_size['s_size']))
        assert self.compare_size['f_size'] < self.compare_size['s_size']

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
        self.moobe.handle_popup_on_connect_to_wifi_progress_screen(p_obj)
        self.moobe.verify_printer_connected_to_wifi_screen(printer_name, self.ssid)
        self.printers.select_exit_setup()
        self.printers.verify_exit_setup_btn()
        if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
            self.printers.select_pop_up_exit_setup()
        self.home.verify_home_screen()
        self.home.verify_carousel_printer_image()