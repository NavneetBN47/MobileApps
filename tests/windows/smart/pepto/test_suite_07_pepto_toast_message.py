import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_07_Pepto_Toast_Message(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.p = load_printers_session

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]

        cls.build_version = (cls.driver.session_data["app_info"])["GOTHAM"].split('-')[1]

        cls.ipAddress = cls.p.p_obj.ipAddress
        cls.model_name = cls.p.get_printer_information()["model name"].split('[')[0].strip()
        if 'HP' not in cls.model_name:
            cls.model_name = 'HP ' + cls.model_name
            
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True

        sleep(1)
        close_activity = eval("w_const.CLOSE_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
        self.driver.terminate_app(close_activity)

    def test_02_click_toast_message_to_launch_app(self):
        self.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized')     
        sleep(5)
        self.sf.select_printer_on_win_settings()
        self.sf.launch_app_on_toast_message()
        self.fc.go_home()

    def test_03_check_pepto_data(self):
        """
        Verify the Lifecycle tracking event is posted for the Toast, and that the app_id is returning 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541238
        """ 
        check_event_list = ['"app_event_action":"started","app_event_object":"session","app_event_object_label":"/start_app/desktop_toast"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_03_check_pepto_data(self):
        """
        Click on the toast message to launch the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961268
        """ 
        check_event_list = ['"app_id":"AioRemote_winbackgroundtask']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
