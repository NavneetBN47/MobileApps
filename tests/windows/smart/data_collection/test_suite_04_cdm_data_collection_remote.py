import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_04_Cdm_Data_Collection_Remote(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_add_remote_printer(self):
        """
        Add a remote printer to Main UI.
        
        Verify PrinterChangedAction shows with productNumber and uuid in gotham log and data sent to server

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309107 (only Gotham log)
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.home.verify_activity_btn()
        self.fc.select_a_remote_printer()
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()

    def test_03_click_print_photos_print_btn(self):
        """
        Start remote print photos
        Send remote print job

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309103 (only Gotham log)
        """ 
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.start_a_remote_print(type='photo')

    def test_04_click_print_documets_print_btn(self):
        """
        Start remote print documents
        Send remote print job

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309104 (only Gotham log)
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.start_a_remote_print(type='doc')

    def test_02_click_scan_print_btn(self):
        """
        Click on the scan tile
        Start the scan via any available entry and land on the scan result screen
        Click print button on the scan result screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309102
        """ 
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_scan_tile()
        self.scan.click_get_started_btn()
        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)       
        self.scan.verify_import_screen()
        sleep(1)
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_print_btn()
        self.print.start_a_remote_print(type='doc')

    def test_05_check_log_info(self):
        self.fc.restart_hp_smart()
        sleep(30)
        self.home.verify_home_screen()
        # Add a remote printer to Main UI.
        check_event_list = ['Ui\|DataCollection:PrinterChangedAction\|TID:[0-9]+\|(\s)productNumber: [A-Z0-9]{6}, uuid:[a-z0-9-]{36}', 'Ui\|DataCollection:PrinterChangedAction\|TID:[0-9]+\|(\s)valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":"[a-z0-9-]{36}","EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":"[a-z0-9]{32}"'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

        # Click print button on the scan result screen
        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: ScanPrintButton', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:Preview, activity:Print-v01, Path:/, mode:, control:PrintButton, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

        # Start remote print photos
        check_event_list = ['Ui\|DataCollection:TrackForDataCollection\|TID:[0-9]+\|(\s)ClickEventAction \/Print\/PrintPhotosIppPreview mapped to PrintPhotosTile', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: PrintButton', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:PrintPreview, activity:Print-v01, Path:\/, mode:, control:PrintButton, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

        # Start remote print documents
        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: PrintButton', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlTileClicked, screen:PrintPreview, activity:Print-v01, Path:\/, mode:, control:PrintButton, detail:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")