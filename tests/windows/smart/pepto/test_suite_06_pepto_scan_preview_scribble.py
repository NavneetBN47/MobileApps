import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_06_Pepto_Scan_Preview_Scribble(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
    
    def test_01_add_printer_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True

    def test_02_click_back_btn_on_scribble_screen(self):
        """
        Click on Scribble on the Preview screen
        While in Scribble screen click on back arrow

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31186969
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31445972
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_scribble_btn()
        self.scan.verify_place_your_mark_screen()
        self.scan.click_back_btn()
        self.scan.verify_scan_result_screen()

    def test_03_click_done_btn_on_scribble_screen(self):
        """
        Click on Scribble on the Preview screen
        Make reduction to the scanned page and click on Done button
        Click Done button on the confirmation dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31186968
        """ 
        self.scan.click_scribble_btn()
        self.scan.verify_place_your_mark_screen()
        creat_scribble = False
        if self.scan.verify_mark_text_exist() is False:
            creat_scribble = True
            self.scan.click_create_btn()
            self.scan.select_mart_text_opt()
            self.scan.verify_new_mark_screen()
            self.scan.select_mart_text_opt()
            self.scan.enter_mart_text()
            self.scan.click_mart_done_btn()
        self.scan.select_first_mart_text()
        self.scan.click_done_btn()
        self.scan.verify_scan_result_screen()
        if creat_scribble:
            self.scan.click_scribble_btn()
            self.scan.verify_place_your_mark_screen()
            self.scan.click_manage_btn()
            self.scan.select_first_mart_box()
            self.scan.click_mark_delete_btn()
        
        sleep(1)
        self.driver.terminate_app()

    def test_04_check_pepto_data(self):
        """
        Choose the scribble feature
        While in Scribble screen click on back arrow
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31445972
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31186969
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults-Photo#ScribbleSelected"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/Photo#ScribblebackButton"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_05_check_pepto_data(self):
        """
        Make reduction to the scanned page and click on Done button
        Click Done button on the confirmation dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31186968
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/Photo#ScribbleYesButton"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
