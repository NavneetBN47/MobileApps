import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_10_Pepto_Supply_Status_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]

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

    def test_02_go_to_supply_status(self):
        """
        Click Printer Settings tile
        navigating to supply status form the Printer settings
        navigating to supply status form the Printer status
        navigating to supply status form the Main Page by clicking the Ink icon on the Main UI
        clicking Get supplies tile on the Main Page
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

        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_supply_status_option()
        if self.printer_settings.verify_supply_status_page():
            sleep(1)
            self.home.select_navbar_back_btn()           
        else:
            self.web_driver.switch_window("supply_status")
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')
        self.home.verify_home_screen()

        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_printer_status_item()
        self.printer_settings.select_supply_status_option()
        if self.printer_settings.verify_supply_status_page():
            sleep(1)
            self.home.select_navbar_back_btn()           
        else:
            self.web_driver.switch_window("supply_status")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            assert "hp.com" in current_url
            self.web_driver.set_size('min')
        self.home.verify_home_screen()

    def test_03_go_to_supply_status_and_check_pepto_data(self):
        """
        navigating to supply status form the Main Page by clicking the Ink icon on the Main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17133798
        """       
        if self.home.click_carousel_estimated_supply_levels():
            if self.printer_settings.verify_supply_status_page():
                sleep(1)
                self.home.select_navbar_back_btn()           
            else:
                self.web_driver.add_window("supply_status")
                sleep(3)
                self.web_driver.switch_window("supply_status")
                sleep(3)
                current_url = self.web_driver.get_current_url()
                assert "hp.com" in current_url
                self.web_driver.set_size('min')
            self.home.verify_home_screen()
            sleep(1)
            self.driver.terminate_app()

            check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#SupplyDetail"'] 

            for each_event in check_event_list:
                self.pepto.check_pepto_data(each_event)

    def test_04_check_pepto_data(self):
        """
        Click Printer Settings tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17133797
        """ 
        check_event_list = ['"app_event_details":{"schema":"generic/1.0.0","moniker":"x-cscr_ad_basic/1.0","campaign_type":"tile","campaign_product":"Supplies","campaign_name":"generic","campaign_variant":"Mns"}',
'"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/SupplyDetail.flow/SupplyDetailPage"']
 
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
    
    def test_05_check_pepto_data(self):
        """
        navigating to supply status form the Printer settings

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17133798
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/PrinterInformation.flow/MasterPage#SupplyDetail"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_check_pepto_data(self):
        """
        navigating to supply status form the Printer status

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17133798
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/ActionCenter.flow/MasterPage#SupplyDetail"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_07_check_pepto_data(self):
        """
        Click on the Instant Ink tile on the main page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17133795
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17133796 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309090
        """ 
        check_event_list = ['"campaign_type":"tile","campaign_product":"Supplies"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#MnsInstantInk"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_08_check_pepto_data(self):
        """
        Verify the log is within the screen displayed event
        The Instant Ink capable flag is in the local context under the following flag name and response

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512802
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512803
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512804
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512805
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512806
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/MainPage-Associated', '"is_instantink_capable"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
    
    def test_09_check_pepto_data(self):
        """
        Click "Printer Settings" tile on Main UI.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961228
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#PrinterInformation"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
