import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Cdm_Add_Printer_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.printers = cls.fc.fd["printers"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)
    
    def test_01_land_on_home_page(self):
        """
        Land on the home page
        Go to any other screen and come back to the home page

        verify home ScreenDisplayed event shows in gotham log and data sent to server.

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309034
        https://hp-testrail.external.hp.com/index.php?/cases/view/30163153
        https://hp-testrail.external.hp.com/index.php?/cases/view/36047320
        https://hp-testrail.external.hp.com/index.php?/cases/view/36047321
        """  
        self.fc.go_home()
        self.home.click_carousel_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_search_again_link()
        self.printers.verify_device_picker_screen()
        self.home.select_navbar_back_btn(check_kibana=True)
        sleep(3)

        check_event_list = ['Log pepto ScreenDisplayedAsync - flow:, screen:MainPage, mode:[A-Za-z]+', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlButtonClicked, screen:Home, activity:AddPrinter-v01, Path:\/, mode:, control:AddPrinter, detail:', 'Ui\|DataCollection:SendSimpleUiEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ScreenDisplayed, screen:Home, activity:, Path:\/, mode:, control:, detail:, actionAuxParameters:'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_02_pick_a_printer(self):
        """
        Land on the home page
        Pick a printer from the device picker

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309105
        https://hp-testrail.external.hp.com/index.php?/cases/view/29309109
        https://hp-testrail.external.hp.com/index.php?/cases/view/29309108
        https://hp-testrail.external.hp.com/index.php?/cases/view/29548763
        https://hp-testrail.external.hp.com/index.php?/cases/view/36047322
        """ 
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        sleep(5)

        check_event_list = ['Ui\|DataCollection:PrinterChangedAction\|.*?\|(\s)productNumber: [A-Z0-9]{6}, uuid: [a-z0-9-]{36}', 'Ui\|DataCollection:PrinterChangedAction\|.*?\|(\s)valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":"[a-z0-9-]{36}","EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":null,"StratusUserId":null,"TenantId":null,"ModelNumber":.*?}']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_03_turn_off_advertising_toggle_not_sign_in(self):
        """
        If not sign in account:
        go to privacy settings and turn off the advertising toggle from Manage your HP Smart privacy preference screen
        come back to the home page and navigate to some more extension

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309089
        https://hp-testrail.external.hp.com/index.php?/cases/view/29309037 (not sign in)
        """ 
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.privacy_preference.click_toggle("advertising_toggle")
        self.fc.check_toggle_status("advertising_toggle", "privacy_close_toggle.png")
        self.privacy_preference.click_continue()
        self.home.verify_home_screen()
        sleep(5)

        check_event_list = ['NonUi\|UsageDateCollectionSettingsHelper:GetUsageDataCollectionSettings\|TID:[0-9]+\|(\s)UsageDataCollectionSetting Device PurposeUndefined','NonUi\|UsageDateCollectionSettingsHelper:GetUsageDataCollectionSettings\|TID:[0-9]+\|(\s)Exit', 'Ui\|DataCollection:PrinterChangedAction\|.*?\|(\s)valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":.*?,"EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":null,"StratusUserId":null,"TenantId":null,"ModelNumber":null}']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_04_sign_in_with_advertising_toggle_off(self):
        """
        sign in account:

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309037 (sign in)
        https://hp-testrail.external.hp.com/index.php?/cases/view/31582047        
        """ 
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen()
        self.home.verify_activity_btn()

        check_event_list = ['NonUi\|DataCollection:LoginChangedHandler\|.*\|(\s)valveControllerMetaData: {"Country":"US","AssetUnit":"desktop","DeviceId":.*?,"EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":"[a-z0-9]{32}","StratusUserId":"[a-z0-9]{24}","TenantId":null,"ModelNumber":null}']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_05_turn_on_advertising_toggle(self):
        """
        go to privacy settings and turn on the advertising toggle 

        Verify LoginChangedAction shows with account ID in gotham log and data sent to server

        https://hp-testrail.external.hp.com/index.php?/cases/view/29309106
        https://hp-testrail.external.hp.com/index.php?/cases/view/30594235
        """ 
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.privacy_preference.click_toggle("advertising_toggle")
        self.privacy_preference.click_continue()
        self.home.verify_home_screen()

    def test_06_disconnect_printer(self):
        """
        Make printer goes offline
        """ 
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.restart_hp_smart()
        self.home.verify_carousel_printer_offline_status()
        self.home.verify_carousel_estimated_supply_image(invisible=True)

    def test_07_click_get_support_btn(self):
        """
        Click on "Get Support" button that shows to the right of printer card
        Make printer goes offline, wait 60 seconds, Click on "Get Support" button that shows on printer card, verify support page shows 

        https://hp-testrail.external.hp.com/index.php?/cases/view/32759609
        https://hp-testrail.external.hp.com/index.php?/cases/view/32759529
        https://hp-testrail.external.hp.com/index.php?/cases/view/32759530
        """ 
        self.home.verify_get_support_btn()
        self.home.click_get_support_btn()
        self.home.verify_connect_to_your_printer_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: GetSupportButton, cardType: Unknown optArg: null', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlButtonClicked, screen:Carousel, activity:GetSupport-v01, Path:/Home/, mode:, control:.*?, detail:, actionAuxParameters:']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_08_click_diagnose_and_fix_link(self):
        """
        Click on the "Diagnose and Fix" link in the hard-coded support page

        https://hp-testrail.external.hp.com/index.php?/cases/view/32759612
        """ 
        self.home.click_diagnose_and_fix_link()
        self.home.verify_diagnose_and_fix_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_connect_to_your_printer_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: GetSupportDiagnoseAndFix, cardType: Unknown optArg: null', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlHyperLinkClicked, screen:GetSupportPage, activity:DiagnoseAndFix-v01, Path:/, mode:, control:, detail:, actionAuxParameters:']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_09_click_get_more_help_link(self):
        """
        Click on the "Get More Help" link in the hard-coded support page

        https://hp-testrail.external.hp.com/index.php?/cases/view/32759613 (only Gotham log)
        """ 
        self.home.click_get_more_help_link()
        self.web_driver.add_window("get_more_help")
        sleep(3)
        self.web_driver.switch_window("get_more_help")
        sleep(3)
        current_url = self.web_driver.get_current_url()
        assert "support.hp.com" in current_url
        self.web_driver.close_window("get_more_help")
        self.home.verify_connect_to_your_printer_screen()

        check_event_list = ['Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)ClickEvent: GetSupportMorehelp, cardType: Unknown optArg: null', 'Ui\|DataCollection:ClickEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlHyperLinkClicked, screen:GetSupportPage, activity:GetMoreHelpLink-v01, Path:/, mode:, control:, detail:, actionAuxParameters:']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_10_restore_priner_status_online(self):
        self.fc.restore_printer_online_status(self.p)
        self.fc.restart_hp_smart()

    def test_11_check_log_file(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/29309106
        https://hp-testrail.external.hp.com/index.php?/cases/view/30594235
        """
        check_event_list = ['{"Country":"US","AssetUnit":"desktop","DeviceId":"[a-z0-9-]{36}","EdgeType":null,"AppInstanceId":"[a-z0-9-]{36}","AssetType":null,"AccountLoginId":"[0-9a-z]{32}","StratusUserId":"[0-9a-z]{24}","TenantId":"[a-z0-9-]{36}","ModelNumber":"[0-9A-Z]{6}"}'] 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")
