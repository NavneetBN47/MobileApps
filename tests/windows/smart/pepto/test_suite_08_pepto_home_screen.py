import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_08_Pepto_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]

        cls.build_version = cls.driver.session_data["app_info"][pytest.app_info].split('-')[1]
        cls.printer_ip_address = cls.p.p_obj.ipAddress
        
        cls.model_name = cls.p.get_printer_information()["model name"].split('[')[0].strip()
        if 'HP' not in cls.model_name:
            cls.model_name = 'HP ' + cls.model_name

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True
    
    def test_02_clean_state_and_relaunch(self):
        """
        Launch the app for the first time
        Click "Accept All" button on the welcome screen
        Click skip for now on the OWS value prop and land on the Main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961223
        """ 
        self.fc.reset_hp_smart()
        self.welcome.click_accept_all_btn()
        self.ows_value_prop.select_native_value_prop_buttons(index=3)
        self.home.verify_home_screen()

    def test_03_add_device(self):
        """
        Land on the home page
        Click the "+" on Main UI to go to the device picker.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961225
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961270
        """ 
        self.home.click_big_add_printer_btn()
        self.printers.verify_device_picker_screen()
        printer = self.printers.search_printer(self.printer_ip_address)
        printer.click()

        if self.home.verify_home_screen(raise_e=False) is False:
            if self.printers.verify_pin_dialog(raise_e=False):
                if self.printers.input_pin(self.p.get_pin()):
                    self.printers.select_pin_dialog_submit_btn()

            if self.printers.verify_printer_setup_webpage(raise_e=False):
                self.printers.select_printer_setup_accept_all_btn()

            if self.printers.verify_exit_setup_btn(raise_e=False):
                self.printers.select_exit_setup()
                self.printers.select_pop_up_exit_setup()
                if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
                    self.printers.select_pop_up_exit_setup()

            self.home.verify_home_screen()

    def test_04_add_another_printer(self):
        """
        Click "Add another Printer" option

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961224
        """     
        self.home.click_add_new_printer_link()
        self.printers.verify_device_picker_screen()
        self.printers.select_first_printer_item()

        if self.home.verify_home_screen(raise_e=False) is False:
            if self.printers.verify_pin_dialog(raise_e=False):
                if self.printers.input_pin(self.p.get_pin()):
                    self.printers.select_pin_dialog_submit_btn()

            if self.printers.verify_printer_setup_webpage(raise_e=False):
                self.printers.select_printer_setup_accept_all_btn()

            if self.printers.verify_exit_setup_btn(raise_e=False):
                self.printers.select_exit_setup()
                self.printers.select_pop_up_exit_setup()
                if self.printers.verify_printer_setup_is_incomplete_dialog(raise_e=False):
                    self.printers.select_pop_up_exit_setup()

            self.home.verify_home_screen()

    def test_05_click_help_and_support_tile(self):
        """
        Click "Help Center" tile on Main UI.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961227
        """     
        self.home.select_help_and_support_tile()
        self.home.verify_help_and_support_page()

        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_06_check_pepto_data(self):
        """
        Land on the home page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309034
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30163153        
        """ 
        check_event_list = ['"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/MainPage-HomeBackgroundFastTasksDone"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_07_check_pepto_data(self):
        """
        Verify the Application Activated event and a Session Started event shows in the beginning of the Pepto log.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541232
        """ 
        check_event_list = ['"app_event_actor":"self","app_event_action":"activated","app_event_object":"application"', '"app_event_actor":"app","app_event_action":"started","app_event_object":"session"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_08_check_pepto_data(self):
        """
        Verify that the captured value is consistent with the PC information.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541233
        """ 
        check_event_list = ['"schema":"sys_info_base/1.2.1","pc_touchenabled":"false","pc_battery":"false","pc_architecture":"x64","os_name":"unknown"', '"os_version"', '"os_architecture":"unknown","os_screenresolution"', '"os_language":"en-US","os_country":"US","pc_manufacturer":"HP","pc_modelname"', '"pc_category":"desktop","pc_sku"', '"app_session_uuid"', '"sys_uuid"', '"app_id":"AioRemote_win/{}.0","app_deployed_id":"AioRemote_win/'.format(self.build_version), '"app_deployed_uuid"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_09_check_pepto_data(self):
        """
        Verify below fields and possible values are present in Log.txt and consistent with the printers on the network:
        Verify the values consistent with the printers found on device picker page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541234
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541235
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541237
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961270
        """ 
        check_event_list = ['"schema":"sys_printer_discoverylist/1.1.1"', '"dev_biid"', '"sys_printer_discovery_modelname":"{}"'.format(self.model_name), '"sys_printer_discovery_manufacturer":"HP"', '"sys_printer_discovery_connectiontype":"network"', '"sys_printer_discovery_discoverymethod"', '"app_session_uuid"', '"sys_uuid"', '"app_id":"AioRemote_win/{}.0","app_deployed_id":"AioRemote_win/'.format(self.build_version), '"app_deployed_uuid"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_10_check_pepto_data(self):
        """
        Verify the Session Stopped event, and a Application Terminated event shows in the beginning of the Pepto log.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541239
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"self","app_event_action":"terminated","app_event_object":"application"', '"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"stopped","app_event_object":"session"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_11_check_pepto_data(self):
        """
        GO to other extension in the app and come back to Main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27674427
        """ 
        check_event_list = ['"moniker":"x-cscr_gotham_report_deviceselectionreport/1.0"','"printer_uuid"','"printer_sku"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_12_check_pepto_data(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961223
        """ 
        check_event_list = ['"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/WelcomePage-TrackingStarted"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_13_check_pepto_data(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961224
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/MainPage","app_event_context":{"schema":"app_event_context/1.0.0"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_14_check_pepto_data(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961225
        """ 
        check_event_list = ['{"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#DeviceSelectionAndDiscovery"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_15_check_pepto_data(self):
        """
        each of the print queues on the system

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541236
        """ 
        check_event_list = ['"schema":"sys_printer_queueinfo/1.1.0"', '"sys_printer_queue_modelname"', '"sys_printer_queue_manufacturer":"hp"', '"sys_printer_queue_connectiontype":"network"', '"sys_printer_queue_driverversion"', '"sys_printer_queue_online"', '"dev_biid"', '"sys_printer_queue_portmon"', '"sys_printer_queue_defaultprinter"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_16_check_pepto_data(self):
        """
        Click "Help Center" tile on Main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961227
        """ 
        check_event_list = ['{"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#OnlineProductSupport4"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_17_check_pepto_data(self):
        """
        Verify you can see "MainPage-SortedTiles" display event in the pepto log

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17153676
        """ 
        check_event_list = ['{"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/MainPage-SortedTiles"', '"context_local":{"sorted_tiles":"HpMnsTile,ScanCapture,SmartTasks,FunTile,PrintDocument,SoftFax,OnlineProductSupport4,PrintPhotos4,PrinterInfoMaster","sort_type":"Default"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
