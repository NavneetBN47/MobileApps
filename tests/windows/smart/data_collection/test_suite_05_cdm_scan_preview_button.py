import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_05_cdm_Scan_Preview_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1] 

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_add_printer_and_sign_in(self):
        """
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True

    def test_02_scan_shortcut(self):
        """
        Click on the Scan tile on the main page
        Click the shortcut option on the Scan result page to bring out the Shortcut flyout

        https://hp-testrail.external.hp.com/index.php?/cases/view/30796897
        https://hp-testrail.external.hp.com/index.php?/cases/view/38974988
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog()
        self.scan.click_shortcuts_btn()
        self.scan.verify_shortcuts_dialog_disappear()
        sleep(1)
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        sleep(1)
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_home_screen()

        check_event_list = ['Ui\|ScanResultsMainVm:InitVm\|TID:[0-9]+\|(\s)Setting flyout JWeb control URI to:(\s)https://assets.hpsmart.*?.com/shortcuts/management/flyout\?appInstanceId=[a-z0-9-]{36}', '"eventCategory":"scanAcquireTask","eventDetail":{"version":".*?","taskDuration":[0-9]{5},"taskResult":"success","scanAcquireItemType":"photo","scanAcquireResolution":"dpi_[0-9]{3,4}","scanAcquireColorMode":"color","scanAcquirePageSize":"entirearea","scanAcquireSource":"flatbed","scanAcquirePages":[0-9]+}']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_03_finish_scan_import_flow(self):
        """
        Click Scan tile -> Import tab and import a image.
        Check the "Pdsmq.Data.txt".

        https://hp-testrail.external.hp.com/index.php?/cases/view/15961267
        """ 
        self.home.select_scan_tile()
        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)       
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()

        check_event_list = ['"app_event_actor":"self","app_event_action":"initiated","app_event_object":"task","app_event_object_label":"task_image_acquire"', '"app_event_actor":"self","app_event_action":"completed","app_event_object":"task","app_event_object_label":"task_image_acquire"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
