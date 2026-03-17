import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_03_Cdm_Print_Buttons(object):
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
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

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

    def test_02_click_print_photos_print_btn(self):
        """
        Click print button via Print Photos

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309100
        """ 
        self.home.select_print_photos_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=300)
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
            self.home.verify_home_screen()
            self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintButton', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:PrintPreview, activity:Print-v01, Path:\/, mode:, control:PrintButton, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_03_click_print_documets_print_btn(self):
        """
        Click print button via Print Documents

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309101
        """
        self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_do_not_show_this_message_checkbox()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintButton', 'NonUi\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:PrintPreview, activity:Print-v01, Path:\/, mode:, control:PrintButton, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_04_click_scan_print_btn(self):
        """
        Click print scan landing page

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309099
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.print.verify_simple_print_dialog(invisible=True)
        self.scan.verify_scan_result_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: ScanPrintButton', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Preview, activity:Print-v01, Path:/, mode:, control:PrintButton, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")
        
