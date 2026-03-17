import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_04_P2_Retargeting_Data_Collection(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.home = cls.fc.fd["home"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.softfax_home = cls.fc.fd["softfax_home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_login_via_person_icon(self):
        """
        Sign in via any available entry point

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30594235
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen()
        
        check_event_list = ['Ui\|DataCollection:LoginChangedHandler\|TID:[0-9]+\|	\|Thr:[0-9]+\| valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":null,"EdgeType":null,"AppInstanceId":"[0-9a-z-]+","AssetType":null,"AccountLoginId":"[0-9a-z]+","StratusUserId":"[0-9a-z]{24}","TenantId":null,"ModelNumber":null} loginChanged:']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_02_add_printer_from_device_picker(self):
        """
        Pick a printer from the device picker

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309105
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29548763
        """  
        self.fc.select_a_printer(self.p)
        
        check_event_list = ['Ui\|DataCollection:PrinterChangedAction\|TID:[0-9]+\|	productNumber: [A-Za-z0-9-]{6}, uuid: [a-z0-9-]{36}', 'Ui\|DataCollection:PrinterChangedAction\|TID:[0-9]+\|	valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":"[a-z0-9-]{36}","EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":"[a-z0-9]{32}","StratusUserId":"[a-z0-9]{24}","TenantId":null,"ModelNumber":null}'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")
    
    def test_03_turn_off_advertising_toggle(self):
        """
        go to privacy settings and turn off the advertising toggle from Manage your HP Smart privacy preference screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309037
        """ 
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.privacy_preference.click_toggle("advertising_toggle")
        self.privacy_preference.click_continue()
        self.home.verify_home_screen()

        check_event_list = ['NonUi\|DataCollection:LoginChangedHandler\|TID:[0-9]+\|	\|Thr:[0-9]+\| valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":null,"EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":"[a-z0-9]{32}","StratusUserId":"[a-z0-9]{24}","TenantId":null,"ModelNumber":null} loginChanged:True'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_04_turn_on_advertising_toggle(self):
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.privacy_preference.click_toggle("advertising_toggle")
        self.privacy_preference.click_continue()
        self.home.verify_home_screen()

    def test_05_click_shortcurs_tile(self):
        """
        Click on the Shortcuts tile on the main page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309091
        """ 
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:Shortcuts-v01, Path:\/, mode:, control:ShortcutsTile, detail:, actionAuxParameters:', 'appInstanceId=[0-9a-z-]{36}'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_06_click_printables_tile(self):
        """
        Click on the Printables tile on the main page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309092
        """
        self.home.select_printables_tile()

        self.web_driver.add_window("printables")
        self.web_driver.switch_window("printables")
        current_url = self.web_driver.get_current_url()
        assert "hp.com" in current_url
        self.web_driver.set_size('min')
        self.home.verify_home_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintablesTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:Printables-v01, Path:\/, mode:, control:PrintablesTile, detail:, actionAuxParameters:'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_07_click_mobile_fax_tile(self):
        """
        Click on the Mobile Fax tile on the main page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309093
        """
        self.home.select_mobile_fax_tile()
        if self.softfax_home.verify_mobile_fax_get_started_screen():
            self.softfax_home.click_mobile_fax_get_started_btn()
        self.home.select_navbar_back_btn()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:MobileFax-v01, Path:\/, mode:, control:MobileFaxTile, detail:, actionAuxParameters:'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_08_click_print_photos_tile(self):
        """
        Click Print Photos Tile
        Click print button via Print Photos

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309094
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309100
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintPhotosTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:Print-v01, Path:\/, mode:, control:PrintPhotosTile, detail:, actionAuxParameters:', 'NonUi\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:PrintPreview, activity:Print-v01, Path:\/, mode:, control:PrintButton, detail:, actionAuxParameters:', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintButton'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_09_click_print_documets_tile(self):
        """
        Click Print Documents tile and sign in
        Click print button via Print Documents

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309095
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309101
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

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintDocumentsTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:Print-v01, Path:\/, mode:, control:PrintDocumentsTile, detail:, actionAuxParameters:', 'NonUi\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintButton', 'NonUi\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: PrintButton', 'NonUi\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:PrintPreview, activity:Print-v01, Path:\/, mode:, control:PrintButton, detail:, actionAuxParameters:'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_10_click_printer_settings_tile(self):
        """
        Click Printer settings Tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309097
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()

        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: SettingsTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:PrinterSettings-v01, Path:\/, mode:, control:PrinterSettingsTile, detail:, actionAuxParameters:'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_11_click_help_and_support_tile(self):
        """
        Click help & Support tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309098
        """
        self.home.select_help_and_support_tile()
        self.home.verify_help_and_support_page()

        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	ClickEvent: HelpTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|	SendUiEvent action:ControlTileClicked, screen:Home, activity:HelpCenter-v01, Path:\/, mode:, control:HelpAndSupportTile, detail:, actionAuxParameters:'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_12_click_shortcut_button_on_scan_preview(self):
        """
        Click the shortcut option on the Scan result page to bring out the Shortcut flyout

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30796897
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

        check_event_list = ['Ui\|ScanResultsMainVm:InitVm\|TID:[0-9]+\|	Setting flyout JWeb control URI to: https://assets.hpsmart[a-z]+.com/shortcuts/management/flyout\?appInstanceId=[a-z0-9-]{36}']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")
