import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_15_Pepto_Scan_Extract_Button(object):
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

    def test_02_go_to_scan_results_page(self):
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()

    def test_03_preview_text_extract(self):
        """
        Click on Text Extract on the Preview screen
        Select any already installed language from "Select Language..." dialog
        Click on "Continue" button on "Select Language..." dialog with newly installed lang
        Text Edit screen -> Delete all text and click on "Done" button -> click on "Start New Scan" button from "Are you sure?..." dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206022
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31186970
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31187097
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206021
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206023
        """ 
        self.scan.click_text_extract_btn()
        self.scan.verify_select_language_dialog()
        self.scan.click_continue_btn()
        if self.scan.verify_text_not_detected_dialog(raise_e=False) is False:
            self.scan.verify_extracting_text_dialog()
            self.scan.verify_text_edit_screen()
            self.scan.click_copy_all_btn()
            self.scan.verify_copie_text_message()
            self.scan.click_copy_all_btn()
            self.scan.click_done_btn()
            self.scan.verify_multi_scribble_scan_result_screen()
        else:
            self.scan.click_extract_ok_btn()
            self.scan.verify_scribble_scan_result_screen()

        self.scan.click_text_extract_btn()
        self.scan.verify_select_language_dialog()
        self.scan.click_continue_btn()
        if self.scan.verify_text_not_detected_dialog(raise_e=False) is False:
            self.scan.verify_extracting_text_dialog()
            self.scan.clear_text_extract_content()
            self.scan.click_done_btn()
            self.scan.verify_extract_are_you_sure_screen()
            self.scan.click_extract_start_new_scan_btn()
            self.scan.verify_scan_result_screen()
        else:
            self.scan.click_extract_ok_btn()
            self.scan.verify_scribble_scan_result_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_04_check_pepto_data(self):
        """
        Click on Text Extract on the Preview screen
        Select any already installed language from "Select Language..." dialog
        Click on "Continue" button on "Select Language..." dialog with newly installed lang
        Text Edit screen -> Delete all text and click on "Done" button -> click on "Start New Scan" button from "Are you sure?..." dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206022
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31186970
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31187097
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206021
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31206023
        """ 
        check_event_list = ['"app_event_details":{"preset":"Photo","source":"Scanner Glass","resolution"','"Is_Detect_Edges_Checked"', '"moniker":"x-cscr_gotham_report_textextractreport/1.0"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/Scan#TextExtractClicked"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults-en#SelectedLangugeForTextExtract"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/Photo#TextEditYesButton"', '"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/ScanCapture.flow/ExtractTextNotDetectedScreen"']
        
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

