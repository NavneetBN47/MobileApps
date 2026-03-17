import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_02_Cdm_Home_Page_Tiles(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.softfax_home = cls.fc.fd["softfax_home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.build_version = cls.driver.session_data["app_info"][pytest.app_info].split('-')[1]
        cls.printer_ip_address = cls.p.p_obj.ipAddress
        
        cls.model_name = cls.p.get_printer_information()["model name"].split('[')[0].strip()
        if 'HP' not in cls.model_name:
            cls.model_name = 'HP ' + cls.model_name

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_add_a_printer_without_sign_in(self):
        """
        Add a printer
        User account is not signed in
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_click_print_documets_tile(self):
        """
        User account not signed in

        Click Print Documents tile and sign in
        Select the file from the picker

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309095
        """
        self.home.select_print_documents_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        if self.home.verify_welcome_back_dialog(raise_e=False):
            self.home.select_welcome_back_continue_btn()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=300)
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
            self.home.verify_home_screen()
            self.home.select_print_documents_tile() 
        self.print.verify_supported_document_file_types_dialog()
        self.print.select_do_not_show_this_message_checkbox()
        self.print.select_supported_document_file_types_dialog_ok_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        self.print.select_print_dialog_cancel_btn()
        self.home.verify_home_screen()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: PrintDocumentsTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:Print-v01, Path:\/, mode:, control:PrintDocumentsTile, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_03_click_mobile_fax_tile(self):
        """
        User account is not signed in

        Land on the home page
        Click on the Mobile Fax tile on the main page
        Perform the login in action.

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309093
        """
        self.fc.sign_out()
        self.home.select_mobile_fax_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
        if self.home.verify_welcome_back_dialog(raise_e=False):
            self.home.select_welcome_back_continue_btn()
        self.softfax_home.verify_mobile_fax_home_screen()
        self.home.select_navbar_back_btn()
        sleep(3)
        
        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: SoftFaxTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:MobileFax-v01, Path:\/, mode:, control:MobileFaxTile, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_04_click_shortcuts_tile(self):
        """
        User account must be signed in

        Click on the Shortcuts tile on the main page

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309091
        """  
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: ShortcutsTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:Shortcuts-v01, Path:\/, mode:, control:ShortcutsTile, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_05_click_printables_tile(self):
        """
        Click on the Printables tile on the main page

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309092
        """
        self.home.select_printables_tile()
        self.web_driver.add_window("printables")
        self.web_driver.switch_window("printables")
        sleep(3)
        current_url = self.web_driver.get_current_url()
        assert "hp.com" in current_url
        self.web_driver.close_window("printables")
        self.home.verify_home_screen()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: PrintablesTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:Printables-v01, Path:\/, mode:, control:PrintablesTile, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_06_click_print_photos_tile(self):
        """
        User account must be signed in

        Add printer to carousel
        Click Print Photos Tile

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309094
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.select_file_picker_dialog_cancel_btn()
        self.home.verify_home_screen()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: PrintPhotosTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:Print-v01, Path:\/, mode:, control:PrintPhotosTile, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_07_click_printer_settings_tile(self):
        """
        User account must be signed in

        Click Printer settings Tile
        Click the shortcut option on the printer settings page

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309097
        https://hp-testrail.external.hp.com/index.php?/cases/view/30796898
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        check_event_list_2 = []

        if "DunePrinterInfo" in str(self.p.p_obj):
            self.printer_settings.select_shortcuts_option()
            sleep(3)
            check_event_list_2.append('"AppInstanceId":"[a-z0-9-]{36}"')
        self.home.select_navbar_back_btn()
        sleep(3)

        check_event_list_1 = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: SettingsTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:PrinterSettings-v01, Path:\/, mode:, control:PrinterSettingsTile, detail:'] 
        check_event_list = check_event_list_1 + check_event_list_2
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_08_click_help_and_support_tile(self):
        """
        Click help & Support tile

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309098
        """
        self.home.select_help_and_support_tile()
        self.home.verify_help_and_support_page()
        self.home.select_navbar_back_btn()
        sleep(3)

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: HelpTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:HelpCenter-v01, Path:\/, mode:, control:HelpAndSupportTile, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_09_click_scan_tile(self):
        """
        Click Scan tile

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309096
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.home.select_navbar_back_btn()
        sleep(3)
        
        check_event_list = ['ClickEvent: ScanTile, cardType: Unknown optArg: null', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:Scan-v01, Path:/, mode:, control:ScanTile, detail:, actionAuxParameters:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_10_click_instant_ink_tile(self):
        """
        Click on the Instant Ink tile on the main page

        verify Instant Ink tile ScreenDisplayed event shows in gotham log and data sent to server.

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309090
        """ 
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_not_now_dialog():
            self.dedicated_supplies_page.select_not_now_btn()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
        else:
            self.web_driver.add_window("get_supplies")
            sleep(3)
            self.web_driver.switch_window("get_supplies")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')
        self.home.verify_home_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: InstantInkTile, cardType: Unknown optArg: null', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Home, activity:InstantInk-v01, Path:/, mode:, control:InstantInkTile, detail:, actionAuxParameters:']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")
