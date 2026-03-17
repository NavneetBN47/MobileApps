import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_15_Pepto_Scan_Preview_Print_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]

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

    def test_02_click_preview_btn_on_scanner_page(self):
        """
        Click "Preview" button on the scan screen and wait until you see the preview

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29880325
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792492 
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_preview_btn()
        self.scan.verify_scanner_preview_screen()

    def test_03_print_scan_landing_page(self):
        """
        Click print scan landing page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309099
        """ 
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        assert self.print.verify_simple_print_dialog(raise_e=False) is False
        self.scan.verify_scan_result_screen()

        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        sleep(1)
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_home_screen()

        sleep(1)
        self.driver.terminate_app()
    
    def test_04_check_pepto_data(self):
        """
        Click print scan landing page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309096
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309099
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#ScanCapture"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults#Print"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_05_check_pepto_data(self):
        """
        Click "Preview" button on the scan screen and wait until you see the preview

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29880325
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanStart#Preview"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

