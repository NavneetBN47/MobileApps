import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_15_Pepto_Scan_Fax_Shortcuts_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

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

    def test_02_go_to_scan_results_page(self):
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

    def test_03_click_fax_btn_on_preview(self):
        """
        Click "Fax" button on the scan result page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27885257
        """ 
        self.home.select_scan_tile()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_fax_btn()
        self.home.select_mobile_fax_tile()
        if self.softfax_home.verify_mobile_fax_get_started_screen():
            self.softfax_home.click_mobile_fax_get_started_btn()
        self.home.select_navbar_back_btn()

    def test_04_click_shortcuts_btn_on_preview(self):
        """
        Click "Shortcuts" button on the scan result page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27885258
        """ 
        self.home.select_scan_tile()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog_disappear()

        sleep(1)
        self.driver.terminate_app()

    def test_05_check_pepto_data(self):
        """
        Click "Fax" button on the scan result page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27885257
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults#SoftFax"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_check_pepto_data(self):
        """
        Click "Shortcuts" button on the scan result page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27885258
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults#SmartTasks"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
