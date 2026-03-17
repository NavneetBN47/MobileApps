import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows import utility

pytest.app_info = "GOTHAM"
class Test_Suite_03_Check_Gotham_Logging_Files(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.about = cls.fc.fd["about"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
                
        cls.logs_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\Logs'
        cls.gotham_log = w_const.TEST_DATA.HP_SMART_LOG_PATH
        cls.logging_data = cls.logs_path + '\LoggingData.xml'
        cls.gotham_oobe_log = cls.logs_path + '\HPSmart_OOBE.log'
        cls.new_file = 'HPSmart_OOBE_savedAt_([0-9-]+).log'

    def test_01_go_home_and_enable_developer_tools_screen(self):
        """
        Open Developer Tools screen by Click 10 or more times on the app logo of about screen.
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)
        assert utility.check_path_exist(self.driver.ssh, self.gotham_oobe_log) is True
        assert self.about.check_new_file_created(self.new_file) == 0 

    def test_02_check_gotham_log_file_size(self):
        """
        Enable logging and save settings.
        Visit a few screens.

        Verify the log file "HPSmart.log" size increased.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815142
        """       
        log_size = self.about.get_file_size(self.gotham_log)
        self.home.select_navbar_back_btn(return_home=False)
        self.about.verify_about_screen()
        self.home.select_navbar_back_btn()
        sleep(1)
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        sleep(2)
        self.home.select_navbar_back_btn()
        recheck_log_size = self.about.get_file_size(self.gotham_log)
        assert  recheck_log_size > log_size

    def test_03_check_new_gotham_log_file_after_relaunch(self):
        """
        Enable logging and save settings.
        Close and re-launch App.

        Verify new "HP Smart.log" file is created under HPSmart folder.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815144
        """       
        log_size = self.about.get_file_size(self.gotham_log)
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        sleep(5)
        relaunch_log_size = self.about.get_file_size(self.gotham_log)
        assert  relaunch_log_size < log_size

    def test_04_check_additional_oobe_log(self):
        """
        Close and re-launch App.

        Verify there is 1 additional OOBE log files being created under

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815130
        """  
        assert self.about.check_new_file_created(self.new_file) == 1
        log_list = self.about.get_logs_file()
        assert log_list.count('HPSmart_OOBE.log') == 1

    def test_05_disable_logging_and_relaunch_app(self):
        """
        Uncheck the logging checkbox
        Save the setting
        Close and re-launch the App
        Use scanner to perform some scanning job.
        Check logging folder.

        Verify the logging can be unchecked successfully.
        Verify log file size does not increase when using app after unchecked logging.
        Verify no new "HP Smart.log" file is created under HP Smart folder when close and re-launch app, or using scan.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815145
        """  
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)
        self.about.enable_or_disable_toggle(index=1, enable=False)        
        before_size = self.about.get_file_size(self.gotham_log)
        sleep(2)
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        after_size = self.about.get_file_size(self.gotham_log)
        assert before_size == after_size
        log_list = self.about.get_logs_file()
        assert log_list.count('HPSmart.log') == 1
