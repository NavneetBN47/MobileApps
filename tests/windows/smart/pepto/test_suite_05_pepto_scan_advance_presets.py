import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_Pepto_Scan_Advance_Presets(object):
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

    def test_02_go_to_scanner_screen(self):
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.verify_scanner_screen()

    @pytest.mark.parametrize("preset_item", ["Document", "Photo", "Multi-Item", "Book"])
    def test_03_select_advance_preset_item(self, preset_item):
        """
        Set Advance Presets to document     
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076318

        Set Advance Presets to "Photo"
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076320

        Set Advance Presets to "Multi-Item"
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076319
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29106032
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862846

        Set Advance Presets to "Book"
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076321
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862846

        """ 
        self.scan.select_dropdown_listitem("preset", preset_item)
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        sleep(1)
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        sleep(1)

    def test_04_check_pepto_data(self):
        """
        Set Advance Presets to document 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076318
        """ 
        check_event_list = ['"scan_preset":"adv_scan","scan_flow_type":"Document","is_advance_user":"True","scan_time"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_05_check_pepto_data(self):
        """
        Set Advance Presets to "Photo" 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309096
        """ 
        check_event_list = ['"scan_preset":"adv_scan","scan_flow_type":"Photo","is_advance_user":"True","scan_time"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_check_pepto_data(self):
        """
        Set Advance Presets to "Multi-Item"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076319
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29106032
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862846
        """ 
        check_event_list = ['"scan_preset":"adv_scan","scan_flow_type":"MultiItem","is_advance_user":"True","scan_time"', '"IsMultiPageScan":"true"', '"IsHpSmartAdvanceUser":"true"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_07_check_pepto_data(self):
        """
        Set Advance Presets to "Book"
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29076321
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862846
        """ 
        check_event_list = ['"scan_preset":"adv_scan","scan_flow_type":"Book","is_advance_user":"True","scan_time"', '"IsBookScan":"true"', '"IsHpSmartAdvanceUser":"true"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
